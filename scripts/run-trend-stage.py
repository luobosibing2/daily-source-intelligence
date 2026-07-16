#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timedelta
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DB_RELATIVE_PATH = Path("state/trend-state.sqlite")
LIFECYCLE_STATUSES = {
    "active",
    "replaced",
    "outdated",
    "weakened",
    "contradicted",
    "limited",
    "needs-verification",
    "archived",
}
CANDIDATE_STATUSES = {
    "new-signal",
    "no-new-signal",
    "limited",
    "needs-fulltext",
    "skipped",
    "failed",
}
NON_CLAIM_CANDIDATE_STATUSES = {"no-new-signal", "skipped"}
STATE_INDEX_HEADING = "状态索引"
LEGACY_STATE_INDEX_HEADING = "状态索引 / Claim State Index"
UPDATE_LOG_HEADING = "更新日志"
LEGACY_UPDATE_LOG_HEADING = "更新日志 / Update Log"
LEGACY_TOPIC_BODY_HEADING = "自动专题正文"
MANAGED_TOPIC_BODY_REQUIRED_HEADINGS = [
    "本次更新",
    "当前活跃判断",
    "受限与待验证",
    "已替代/削弱/过时判断",
    "对长期趋势的含义",
    "短时间线",
    "证据入口",
]
TOPIC_BODY_CLAIM_STATUSES = {"new-signal", "limited", "needs-fulltext"}
TOPIC_CONSOLIDATION_MODEL = "gpt-5.5"
TOPIC_CONSOLIDATION_REASONING_EFFORT = "high"


class VerifyResult:
    def __init__(self, errors):
        self.errors = errors
        self.ok = not errors

    def to_dict(self):
        return {"ok": self.ok, "errors": self.errors}


def now_local():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_text(path, default=""):
    path = Path(path)
    if not path.exists():
        return default
    return path.read_text(encoding="utf-8")


def read_json(path, default):
    path = Path(path)
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def json_dumps(payload):
    return json.dumps(payload, ensure_ascii=False, sort_keys=True)


def validate_lifecycle_status(status):
    if status not in LIFECYCLE_STATUSES:
        allowed = ", ".join(sorted(LIFECYCLE_STATUSES))
        raise ValueError(f"unknown lifecycle_status {status!r}; allowed: {allowed}")
    return status


def connect_db(root=ROOT):
    root = Path(root)
    db_path = root / DB_RELATIVE_PATH
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def migrate(conn):
    lifecycle_values = ", ".join(f"'{status}'" for status in sorted(LIFECYCLE_STATUSES))
    conn.executescript(
        f"""
        CREATE TABLE IF NOT EXISTS trend_candidates (
            candidate_id TEXT PRIMARY KEY,
            run_date TEXT NOT NULL,
            trend_id TEXT NOT NULL,
            source_path TEXT NOT NULL,
            archive_path TEXT NOT NULL,
            source_content_hash TEXT NOT NULL,
            candidate_status TEXT NOT NULL,
            evidence_level TEXT NOT NULL,
            signal_summary TEXT NOT NULL,
            trend_meaning TEXT NOT NULL,
            boundary_note TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_trend_candidates_run_date_trend
            ON trend_candidates(run_date, trend_id, candidate_status);

        CREATE TABLE IF NOT EXISTS trend_topics (
            trend_id TEXT PRIMARY KEY,
            label TEXT NOT NULL,
            timeline TEXT NOT NULL,
            report_section TEXT NOT NULL,
            enabled INTEGER NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS trend_claims (
            claim_id TEXT PRIMARY KEY,
            trend_id TEXT NOT NULL,
            claim_date TEXT NOT NULL,
            claim_text TEXT NOT NULL,
            evidence_refs_json TEXT NOT NULL,
            lifecycle_status TEXT NOT NULL CHECK (lifecycle_status IN ({lifecycle_values})),
            replacement_claim_id TEXT NOT NULL,
            status_note TEXT NOT NULL,
            markdown_anchor TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_trend_claims_trend_status
            ON trend_claims(trend_id, lifecycle_status, claim_date);

        CREATE TABLE IF NOT EXISTS trend_jobs (
            kind TEXT NOT NULL,
            job_key TEXT NOT NULL,
            status TEXT NOT NULL,
            worker_id TEXT NOT NULL,
            ownership_token TEXT NOT NULL,
            retry_remaining INTEGER NOT NULL,
            input_watermark TEXT NOT NULL,
            last_success_watermark TEXT NOT NULL,
            lease_until TEXT NOT NULL,
            retry_at TEXT NOT NULL,
            started_at TEXT NOT NULL,
            finished_at TEXT NOT NULL,
            last_error TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            PRIMARY KEY (kind, job_key)
        );

        CREATE INDEX IF NOT EXISTS idx_trend_jobs_kind_status
            ON trend_jobs(kind, status, lease_until);

        CREATE TABLE IF NOT EXISTS trend_phase2_runs (
            run_date TEXT PRIMARY KEY,
            status TEXT NOT NULL,
            input_watermark TEXT NOT NULL,
            files_changed_json TEXT NOT NULL,
            verification_ok INTEGER NOT NULL,
            error TEXT NOT NULL,
            started_at TEXT NOT NULL,
            finished_at TEXT NOT NULL
        );
        """
    )
    conn.commit()


def load_enabled_trends(root=ROOT):
    root = Path(root)
    path = root / "config" / "trends.yaml"
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    trends = []
    for item in payload.get("trends", []):
        if not item.get("enabled"):
            continue
        trend_id = str(item["id"])
        trends.append(
            {
                "id": trend_id,
                "label": str(item.get("label") or trend_id),
                "timeline": str(item.get("timeline") or f"trend/{trend_id}.md"),
                "report_section": str(item.get("report_section") or item.get("label") or trend_id),
            }
        )
    return trends


def state_trends(conn, root=ROOT):
    rows = [
        dict(row)
        for row in conn.execute(
            """
            SELECT trend_id AS id, label, timeline, report_section
            FROM trend_topics
            WHERE enabled = 1
            ORDER BY trend_id
            """
        )
    ]
    if rows:
        return rows
    return load_enabled_trends(root)


def upsert_trend_topic(conn, trend):
    conn.execute(
        """
        INSERT INTO trend_topics (
            trend_id, label, timeline, report_section, enabled, updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(trend_id) DO UPDATE SET
            label = excluded.label,
            timeline = excluded.timeline,
            report_section = excluded.report_section,
            enabled = excluded.enabled,
            updated_at = excluded.updated_at
        """,
        (
            trend["id"],
            trend["label"],
            trend["timeline"],
            trend["report_section"],
            1,
            now_local(),
        ),
    )


def relative_to_root(root, path):
    if not path:
        return ""
    root = Path(root)
    path = Path(path)
    if path.is_absolute():
        try:
            path = path.relative_to(root)
        except ValueError:
            return path.as_posix()
    return path.as_posix()


def sha256_text(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def content_hash(root, *relative_paths, fallback_parts=None):
    root = Path(root)
    for relative_path in relative_paths:
        if not relative_path:
            continue
        path = root / relative_path
        if path.exists() and path.is_file():
            return hashlib.sha256(path.read_bytes()).hexdigest()
    fallback_parts = [str(part or "") for part in (fallback_parts or [])]
    return sha256_text("\n".join(fallback_parts))


def short_id(prefix, *parts):
    digest = sha256_text("\n".join(str(part or "") for part in parts))[:16]
    return f"{prefix}-{digest}"


def compact_text(text, limit=120):
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def first_markdown_heading(root, relative_path):
    if not relative_path:
        return ""
    text = read_text(Path(root) / relative_path)
    for line in text.splitlines():
        if line.startswith("#"):
            return compact_text(line.lstrip("#").strip(), limit=90)
    return Path(relative_path).stem


def infer_evidence_level(source_path, archive_path):
    joined = f"{source_path} {archive_path}".lower()
    if "twitterapi" in joined or "/x/" in joined or "direct-x" in joined:
        return "direct-x"
    if "official" in joined or "openai" in joined or "anthropic" in joined or "claude" in joined:
        return "official-source"
    if "github" in joined or "rss" in joined or "blog" in joined or "newsletter" in joined:
        return "secondary-source"
    return "inference"


def normalize_candidate_status(manifest_status, entry_status):
    manifest_status = str(manifest_status or "").strip()
    entry_status = str(entry_status or "").strip()
    if entry_status in {"limited", "needs-fulltext", "skipped", "failed"}:
        return entry_status
    if entry_status == "ok" and manifest_status == "new-signal":
        return "new-signal"
    if manifest_status in CANDIDATE_STATUSES:
        return manifest_status
    if entry_status in CANDIDATE_STATUSES:
        return entry_status
    return "skipped"


def candidate_from_entry(root, run_date, trend, manifest, entry):
    trend_id = trend["id"]
    source_path = relative_to_root(root, entry.get("source_path", ""))
    archive_path = relative_to_root(root, entry.get("archive_path", ""))
    status = normalize_candidate_status(manifest.get("status"), entry.get("status"))
    fallback = [
        run_date,
        trend_id,
        source_path,
        archive_path,
        status,
        entry.get("reason"),
        entry.get("method"),
    ]
    digest = content_hash(root, archive_path, source_path, fallback_parts=fallback)
    source_title = first_markdown_heading(root, archive_path) or Path(source_path).stem or status
    boundary_note = entry.get("reason") or entry.get("note") or ""
    if status in {"limited", "needs-fulltext", "skipped", "failed"} and not boundary_note:
        boundary_note = f"`entry.status` 为 `{status}`，需要在报告中保留证据边界。"
    candidate_id = short_id("trend-candidate", run_date, trend_id, source_path, archive_path, status)
    return {
        "candidate_id": candidate_id,
        "run_date": run_date,
        "trend_id": trend_id,
        "source_path": source_path,
        "archive_path": archive_path,
        "source_content_hash": digest,
        "candidate_status": status,
        "evidence_level": infer_evidence_level(source_path, archive_path),
        "signal_summary": compact_text(source_title),
        "trend_meaning": compact_text(
            f"从 {source_title} 看到 {trend['label']} 新信号：如果证据仍然有效，应更新该专题的状态判断。"
        ),
        "boundary_note": compact_text(boundary_note, limit=240),
    }


def candidate_from_no_signal(root, run_date, trend, payload, path):
    reason = payload.get("reason") or "当天没有记录到新的趋势信号。"
    relative_path = relative_to_root(root, path)
    candidate_id = short_id("trend-candidate", run_date, trend["id"], relative_path, "no-new-signal")
    return {
        "candidate_id": candidate_id,
        "run_date": run_date,
        "trend_id": trend["id"],
        "source_path": "",
        "archive_path": relative_path,
        "source_content_hash": content_hash(root, relative_path, fallback_parts=[run_date, trend["id"], reason]),
        "candidate_status": "no-new-signal",
        "evidence_level": "inference",
        "signal_summary": compact_text(reason),
        "trend_meaning": "当天不应把该专题提升为新的长期趋势判断。",
        "boundary_note": compact_text(reason, limit=240),
    }


def candidate_from_missing_raw(run_date, trend):
    reason = f"`{trend['id']}` 缺少 trend raw manifest 或 no-new-signal 标记。"
    candidate_id = short_id("trend-candidate", run_date, trend["id"], "missing-trend-raw")
    return {
        "candidate_id": candidate_id,
        "run_date": run_date,
        "trend_id": trend["id"],
        "source_path": "",
        "archive_path": "",
        "source_content_hash": sha256_text(reason),
        "candidate_status": "skipped",
        "evidence_level": "inference",
        "signal_summary": reason,
        "trend_meaning": "缺少已归档证据时，Trend 阶段不能提升新的长期判断。",
        "boundary_note": reason,
    }


def upsert_trend_candidate(conn, candidate):
    timestamp = now_local()
    conn.execute(
        """
        INSERT INTO trend_candidates (
            candidate_id, run_date, trend_id, source_path, archive_path,
            source_content_hash, candidate_status, evidence_level, signal_summary,
            trend_meaning, boundary_note, created_at, updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(candidate_id) DO UPDATE SET
            source_content_hash = excluded.source_content_hash,
            candidate_status = excluded.candidate_status,
            evidence_level = excluded.evidence_level,
            signal_summary = excluded.signal_summary,
            trend_meaning = excluded.trend_meaning,
            boundary_note = excluded.boundary_note,
            updated_at = excluded.updated_at
        """,
        (
            candidate["candidate_id"],
            candidate["run_date"],
            candidate["trend_id"],
            candidate["source_path"],
            candidate["archive_path"],
            candidate["source_content_hash"],
            candidate["candidate_status"],
            candidate["evidence_level"],
            candidate["signal_summary"],
            candidate["trend_meaning"],
            candidate["boundary_note"],
            timestamp,
            timestamp,
        ),
    )


def upsert_trend_claim(
    conn,
    claim_id,
    trend_id,
    claim_date,
    claim_text,
    evidence_refs,
    lifecycle_status,
    replacement_claim_id="",
    status_note="",
    markdown_anchor="",
):
    lifecycle_status = validate_lifecycle_status(lifecycle_status)
    timestamp = now_local()
    markdown_anchor = markdown_anchor or claim_id
    conn.execute(
        """
        INSERT INTO trend_claims (
            claim_id, trend_id, claim_date, claim_text, evidence_refs_json,
            lifecycle_status, replacement_claim_id, status_note, markdown_anchor,
            created_at, updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(claim_id) DO UPDATE SET
            trend_id = excluded.trend_id,
            claim_date = excluded.claim_date,
            claim_text = excluded.claim_text,
            evidence_refs_json = excluded.evidence_refs_json,
            lifecycle_status = excluded.lifecycle_status,
            replacement_claim_id = excluded.replacement_claim_id,
            status_note = excluded.status_note,
            markdown_anchor = excluded.markdown_anchor,
            updated_at = excluded.updated_at
        """,
        (
            claim_id,
            trend_id,
            claim_date,
            claim_text,
            json_dumps(list(evidence_refs or [])),
            lifecycle_status,
            replacement_claim_id or "",
            status_note or "",
            markdown_anchor,
            timestamp,
            timestamp,
        ),
    )


def run_phase1(run_date, root=ROOT):
    root = Path(root)
    read_text(root / "runbook.md")
    read_text(root / "docs" / f"{run_date}-daily-intel.md")
    raw_dir = root / "raw" / run_date
    if raw_dir.exists():
        list(raw_dir.iterdir())
    trends = load_enabled_trends(root)
    candidates = []
    for trend in trends:
        trend_raw_dir = root / "trend" / "raw" / run_date / trend["id"]
        manifest_path = trend_raw_dir / "manifest.json"
        no_signal_path = trend_raw_dir / "no-new-signal.json"
        if manifest_path.exists():
            manifest = read_json(manifest_path, {})
            entries = manifest.get("entries") or []
            if entries:
                candidates.extend(candidate_from_entry(root, run_date, trend, manifest, entry) for entry in entries)
            else:
                candidates.append(
                    candidate_from_entry(
                        root,
                        run_date,
                        trend,
                        manifest,
                        {
                            "source_path": "",
                            "archive_path": relative_to_root(root, manifest_path),
                            "status": manifest.get("status") or "skipped",
                            "reason": manifest.get("reason") or "manifest has no entries",
                        },
                    )
                )
        elif no_signal_path.exists():
            payload = read_json(no_signal_path, {})
            candidates.append(candidate_from_no_signal(root, run_date, trend, payload, no_signal_path))
        else:
            candidates.append(candidate_from_missing_raw(run_date, trend))

    with connect_db(root) as conn:
        migrate(conn)
        for trend in trends:
            upsert_trend_topic(conn, trend)
        for candidate in candidates:
            upsert_trend_candidate(conn, candidate)
        conn.commit()
    return candidates


def candidate_rows(conn, run_date):
    return [
        dict(row)
        for row in conn.execute(
            """
            SELECT * FROM trend_candidates
            WHERE run_date = ?
            ORDER BY trend_id, candidate_status, archive_path, source_path
            """,
            (run_date,),
        )
    ]


def claim_rows(conn, trend_id=None):
    if trend_id:
        return [
            dict(row)
            for row in conn.execute(
                """
                SELECT * FROM trend_claims
                WHERE trend_id = ?
                ORDER BY claim_date, claim_id
                """,
                (trend_id,),
            )
        ]
    return [
        dict(row)
        for row in conn.execute(
            """
            SELECT * FROM trend_claims
            ORDER BY trend_id, claim_date, claim_id
            """
        )
    ]


def phase2_input_watermark(candidates):
    payload = [
        {
            "candidate_id": row["candidate_id"],
            "hash": row["source_content_hash"],
            "status": row["candidate_status"],
        }
        for row in candidates
    ]
    return sha256_text(json_dumps(payload))


def acquire_global_job(conn, run_date, input_watermark):
    timestamp = now_local()
    token = str(uuid.uuid4())
    worker_id = f"trend-stage:{token}"
    lease_until = (datetime.now().astimezone() + timedelta(minutes=30)).isoformat(timespec="seconds")
    conn.execute(
        """
        INSERT INTO trend_jobs (
            kind, job_key, status, worker_id, ownership_token, retry_remaining,
            input_watermark, last_success_watermark, lease_until, retry_at,
            started_at, finished_at, last_error, updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(kind, job_key) DO UPDATE SET
            status = excluded.status,
            worker_id = excluded.worker_id,
            ownership_token = excluded.ownership_token,
            retry_remaining = excluded.retry_remaining,
            input_watermark = excluded.input_watermark,
            lease_until = excluded.lease_until,
            retry_at = excluded.retry_at,
            started_at = excluded.started_at,
            finished_at = excluded.finished_at,
            last_error = excluded.last_error,
            updated_at = excluded.updated_at
        """,
        (
            "trend_consolidate_global",
            run_date,
            "running",
            worker_id,
            token,
            3,
            input_watermark,
            "",
            lease_until,
            "",
            timestamp,
            "",
            "",
            timestamp,
        ),
    )
    return token


def finish_global_job(conn, run_date, status, input_watermark, error=""):
    timestamp = now_local()
    last_success = input_watermark if status == "succeeded" else ""
    conn.execute(
        """
        UPDATE trend_jobs
        SET status = ?,
            last_success_watermark = CASE WHEN ? != '' THEN ? ELSE last_success_watermark END,
            finished_at = ?,
            last_error = ?,
            updated_at = ?
        WHERE kind = 'trend_consolidate_global' AND job_key = ?
        """,
        (status, last_success, last_success, timestamp, error or "", timestamp, run_date),
    )


def lifecycle_for_candidate(candidate):
    status = candidate["candidate_status"]
    if status == "new-signal":
        return "active"
    if status == "limited":
        return "limited"
    return "needs-verification"


def evidence_refs_for_candidate(candidate):
    refs = []
    if candidate.get("archive_path"):
        refs.append(candidate["archive_path"])
    elif candidate.get("source_path"):
        refs.append(candidate["source_path"])
    return refs


def claim_id_for_candidate(candidate):
    return short_id(
        "trend-claim",
        candidate["run_date"],
        candidate["trend_id"],
        candidate["archive_path"],
        candidate["source_content_hash"],
        candidate["candidate_status"],
    )


def candidate_should_produce_claim(candidate):
    return candidate["candidate_status"] not in NON_CLAIM_CANDIDATE_STATUSES


def promote_candidates_to_claims(conn, run_date, candidates):
    claims = []
    for candidate in candidates:
        if not candidate_should_produce_claim(candidate):
            continue
        lifecycle_status = lifecycle_for_candidate(candidate)
        note = ""
        if lifecycle_status != "active":
            note = candidate["boundary_note"] or f"candidate_status 为 `{candidate['candidate_status']}`，需要保留边界说明。"
        claim_id = claim_id_for_candidate(candidate)
        claim_text = compact_text(candidate["trend_meaning"], limit=180)
        upsert_trend_claim(
            conn,
            claim_id=claim_id,
            trend_id=candidate["trend_id"],
            claim_date=run_date,
            claim_text=claim_text,
            evidence_refs=evidence_refs_for_candidate(candidate),
            lifecycle_status=lifecycle_status,
            status_note=note,
            markdown_anchor=claim_id,
        )
        claims.append(claim_id)
    return claims


def rel_link_from_file(root, from_file, target_relative, label=None):
    target_relative = str(target_relative or "")
    label = label or Path(target_relative).name or "link"
    if not target_relative:
        return ""
    target = Path(root) / target_relative
    href = relative_href_from_file(root, from_file, target_relative)
    return f"[{label}]({href})"


def relative_href_from_file(root, from_file, target_relative):
    target = Path(root) / str(target_relative or "")
    return os.path.relpath(target, Path(from_file).parent).replace(os.sep, "/")


def status_marker_for_trend(root, run_date, trend):
    manifest = Path("trend") / "raw" / run_date / trend["id"] / "manifest.json"
    no_signal = Path("trend") / "raw" / run_date / trend["id"] / "no-new-signal.json"
    if (Path(root) / manifest).exists():
        return manifest.as_posix(), "manifest"
    if (Path(root) / no_signal).exists():
        return no_signal.as_posix(), "no-new-signal"
    return "", "missing"


def validate_marker_payload(payload, run_date, trend, marker_path, marker_kind, root=ROOT):
    errors = []
    if payload.get("run_date") != run_date:
        errors.append(
            f"{marker_kind} marker {relative_to_root(root, marker_path)} has run_date {payload.get('run_date')!r}, expected {run_date!r}"
        )
    if payload.get("trend_id") != trend["id"]:
        errors.append(
            f"{marker_kind} marker for {trend['id']} has trend_id {payload.get('trend_id')!r}, expected {trend['id']!r}"
        )
    return errors


def preflight_trend_markers(run_date, trends, root=ROOT):
    root = Path(root)
    errors = []
    statuses = {}
    for trend in trends:
        trend_raw_dir = root / "trend" / "raw" / run_date / trend["id"]
        manifest_path = trend_raw_dir / "manifest.json"
        no_signal_path = trend_raw_dir / "no-new-signal.json"
        has_manifest = manifest_path.exists()
        has_no_signal = no_signal_path.exists()
        if has_manifest and has_no_signal:
            errors.append(f"trend {trend['id']} has both manifest.json and no-new-signal.json markers")
            continue
        if not has_manifest and not has_no_signal:
            errors.append(f"missing trend marker for {trend['id']}")
            continue
        if has_manifest:
            manifest = read_json(manifest_path, {})
            errors.extend(validate_marker_payload(manifest, run_date, trend, manifest_path, "manifest", root=root))
            for entry in manifest.get("entries") or []:
                archive_path = relative_to_root(root, entry.get("archive_path", ""))
                if archive_path and not (root / archive_path).exists():
                    errors.append(f"trend {trend['id']} manifest has missing archive_path: {archive_path}")
            statuses[trend["id"]] = {
                "marker": "manifest",
                "path": relative_to_root(root, manifest_path),
                "status": manifest.get("status") or "",
            }
            continue
        payload = read_json(no_signal_path, {})
        errors.extend(validate_marker_payload(payload, run_date, trend, no_signal_path, "no-new-signal", root=root))
        statuses[trend["id"]] = {
            "marker": "no-new-signal",
            "path": relative_to_root(root, no_signal_path),
            "status": payload.get("status") or "no-new-signal",
        }
    if errors:
        raise RuntimeError("\n".join(errors))
    return statuses


def render_daily_trend_report(root, run_date, trends, candidates_by_trend):
    report_path = Path(root) / "trend" / "reports" / f"{run_date}-trend-report.md"
    lines = [
        f"# {run_date} 趋势报告",
        "",
        "## 今日趋势结论",
        "",
        "本报告由 `scripts/run-trend-stage.py` 根据当天日报、原始证据、趋势归档清单和 SQLite 状态索引生成。",
        "它负责记录每个已启用趋势的当天状态，并把长期判断的可追溯索引交给各专题报告维护。",
        "",
        "## 已启用趋势检查结果",
        "",
        "| 趋势 | 今日状态 | 归档 | 专题报告 |",
        "| --- | --- | --- | --- |",
    ]
    for trend in trends:
        rows = candidates_by_trend.get(trend["id"], [])
        statuses = ", ".join(sorted({row["candidate_status"] for row in rows})) or "missing"
        marker, marker_label = status_marker_for_trend(root, run_date, trend)
        archive_link = rel_link_from_file(root, report_path, marker, marker_label) if marker else "`missing`"
        topic_link = rel_link_from_file(root, report_path, trend["timeline"], trend["label"])
        lines.append(f"| `{trend['id']}` / {trend['label']} | `{statuses}` | {archive_link} | {topic_link} |")

    for trend in trends:
        lines.extend(["", f"## {trend['report_section']}", ""])
        rows = candidates_by_trend.get(trend["id"], [])
        if not rows:
            lines.append("- `missing`: Phase 1 没有生成 candidate row；请先检查 SQLite 中的 `trend_candidates` 和当天 `trend/raw/` 归档。")
            continue
        for row in rows:
            marker = row["archive_path"] or row["source_path"]
            link = rel_link_from_file(root, report_path, marker, Path(marker).name) if marker else "`missing`"
            note = row["boundary_note"] or row["trend_meaning"]
            lines.append(
                f"- `{row['candidate_status']}` / `{row['evidence_level']}`: {row['signal_summary']} "
                f"({link})。{note}"
            )

    lines.extend(
        [
            "",
            "## 边界与下一步",
            "",
            "- Phase 2 不重新联网找证据，只读取 SQLite、`trend/raw/` 和现有 `trend/*.md`。",
            "- 每个 enabled 专题报告会直接重写主体正文，并刷新 `## 状态索引` 和 `## 更新日志`；主体正文由 LLM 整理，父脚本负责校验和落盘。",
            "- 旧判断允许被重排、压缩和改写，但不能静默删除；生命周期状态必须继续保存在 SQLite 与专题报告状态索引中。",
            "",
        ]
    )
    return "\n".join(lines)


def remove_section(text, heading):
    pattern = re.compile(rf"^## {re.escape(heading)}\n.*?(?=^## |\Z)", re.MULTILINE | re.DOTALL)
    return pattern.sub("", text).rstrip() + "\n"


def markdown_table_escape(value):
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def parse_evidence_refs(row):
    try:
        refs = json.loads(row["evidence_refs_json"])
    except json.JSONDecodeError:
        return []
    if not isinstance(refs, list):
        return []
    return [str(ref) for ref in refs]


def render_status_index(root, topic_path, claims):
    lines = [
        f"## {STATE_INDEX_HEADING}",
        "",
        "| Claim ID | 日期 | 生命周期状态 | 判断内容 | 证据 | 锚点 | 状态说明 | 替代判断 |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    if not claims:
        lines.append("| _无_ | - | - | - | - | - | - | - |")
    for claim in claims:
        refs = parse_evidence_refs(claim)
        links = []
        for index, ref in enumerate(refs, start=1):
            if ref:
                links.append(rel_link_from_file(root, topic_path, ref, f"证据{index}"))
        evidence = ", ".join(links) if links else "-"
        anchor = claim["markdown_anchor"] or claim["claim_id"]
        lines.append(
            "| `{claim_id}` | {claim_date} | `{status}` | {claim_text} | {evidence} | [{anchor}](#{anchor}) | {note} | {replacement} |".format(
                claim_id=claim["claim_id"],
                claim_date=claim["claim_date"],
                status=claim["lifecycle_status"],
                claim_text=markdown_table_escape(claim["claim_text"]),
                evidence=evidence,
                anchor=markdown_table_escape(anchor),
                note=markdown_table_escape(claim["status_note"]),
                replacement=f"`{claim['replacement_claim_id']}`" if claim["replacement_claim_id"] else "-",
            )
        )
    lines.append("")
    return "\n".join(lines)


def render_update_log(trend, run_date, candidates, rewrite_performed=True):
    lines = [
        f"## {UPDATE_LOG_HEADING}",
        "",
        f"### {run_date}",
        "",
    ]
    if not rewrite_performed:
        lines.append("- 已检查，无新增或仅有 skipped/no-new-signal 状态，未触发 LLM rewrite。")
    if not candidates:
        lines.append("- `missing`: Phase 1 没有生成 candidate row；请检查当天 `trend/raw/` 归档。")
    for row in candidates:
        if candidate_should_produce_claim(row):
            lines.append(
                f"- `{row['candidate_status']}` -> `{claim_id_for_candidate(row)}`: "
                f"{row['signal_summary']}。{row['trend_meaning']} {row['boundary_note']}".rstrip()
            )
        else:
            lines.append(f"- `{row['candidate_status']}`: {row['signal_summary']}。{row['boundary_note']}")
    lines.append("")
    return "\n".join(lines)


def audit_section_start(text):
    starts = []
    for heading in [STATE_INDEX_HEADING, LEGACY_STATE_INDEX_HEADING, UPDATE_LOG_HEADING, LEGACY_UPDATE_LOG_HEADING]:
        match = re.search(rf"^## {re.escape(heading)}\n", text, flags=re.MULTILINE)
        if match:
            starts.append(match.start())
    return min(starts) if starts else len(text)


def h1_end(text):
    match = re.search(r"^# .*(?:\n|\Z)", text, flags=re.MULTILINE)
    if match:
        return match.end()
    return 0


def topic_title_text(text, fallback_title):
    title_end = h1_end(text)
    if title_end:
        return text[:title_end].strip()
    return fallback_title.strip()


def managed_topic_body(text):
    body_start = h1_end(text)
    body_end = audit_section_start(text)
    return text[body_start:body_end].strip() + "\n"


def audit_tail(text):
    start = audit_section_start(text)
    if start >= len(text):
        return ""
    return text[start:].strip() + "\n"


def replace_managed_topic_body(text, body):
    title = topic_title_text(text, "# Trend Report")
    body = str(body or "").strip()
    tail = audit_tail(text).strip()
    parts = [title, body]
    if tail:
        parts.append(tail)
    return "\n\n".join(part for part in parts if part).rstrip() + "\n"


def expected_topic_body_claim_ids(candidates):
    return [
        claim_id_for_candidate(candidate)
        for candidate in candidates
        if candidate["candidate_status"] in TOPIC_BODY_CLAIM_STATUSES and candidate_should_produce_claim(candidate)
    ]


def validate_managed_topic_body(body, run_date, trend, claims, candidates, root=ROOT, topic_path=None):
    errors = []
    body = str(body or "").strip()
    topic_path = Path(topic_path or Path(root) / trend["timeline"])
    if f"## {LEGACY_TOPIC_BODY_HEADING}" in body:
        errors.append(f"topic {trend['id']} contains legacy generated body section ## {LEGACY_TOPIC_BODY_HEADING}")
    for heading in MANAGED_TOPIC_BODY_REQUIRED_HEADINGS:
        if f"## {heading}" not in body:
            errors.append(f"topic {trend['id']} managed body missing required section: {heading}")
    for forbidden in [STATE_INDEX_HEADING, LEGACY_STATE_INDEX_HEADING, UPDATE_LOG_HEADING, LEGACY_UPDATE_LOG_HEADING]:
        if f"## {forbidden}" in body:
            errors.append(f"topic {trend['id']} managed body contains script-owned section: {forbidden}")

    claims_by_id = {claim["claim_id"]: claim for claim in claims}
    current_claim_ids = {claim_id for claim_id, claim in claims_by_id.items() if claim.get("claim_date") == run_date}
    for claim_id in expected_topic_body_claim_ids(candidates):
        if claim_id not in current_claim_ids:
            errors.append(f"topic {trend['id']} expected current claim {claim_id} is missing from SQLite")
            continue
        if claim_id not in body:
            errors.append(f"claim {claim_id} missing from topic managed body {trend.get('timeline', trend['id'])}")
        refs = parse_evidence_refs(claims_by_id[claim_id])
        if refs:
            expected_hrefs = [relative_href_from_file(root, topic_path, ref) for ref in refs if ref]
            if not any(href in body for href in expected_hrefs):
                errors.append(f"claim {claim_id} missing evidence link in topic managed body {trend.get('timeline', trend['id'])}")
    return errors


def build_topic_consolidation_prompt(root, run_date, trend, claims, candidates):
    topic_path = trend["timeline"]
    trend_raw = Path("trend") / "raw" / run_date / trend["id"]
    payload = {
        "run_date": run_date,
        "trend": trend,
        "topic_path": topic_path,
        "trend_raw_path": trend_raw.as_posix(),
        "claims": claims,
        "candidates": candidates,
        "required_claim_ids": expected_topic_body_claim_ids(candidates),
        "required_sections": MANAGED_TOPIC_BODY_REQUIRED_HEADINGS,
    }
    return f"""
你正在执行 Daily Source Intelligence Trend Phase 2 的专题正文整理。

工作目录已经是 `{root}`。

你是父级脚本调度的非交互式 topic consolidation subagent。不要读取 skills、memory、计划文档、日报或联网资料；不要等待用户确认；不要修改任何文件。你只需要输出专题报告主体正文，父级脚本会负责写文件和校验。

允许读取的输入只有：
- SQLite 派生 payload（见下方 JSON）。
- 现有专题文件 `{topic_path}`。
- 当天证据归档目录 `{trend_raw.as_posix()}`。

输出要求：
1. 直接重写 topic 主体正文；不要输出 H1 标题、解释、计划、代码块或额外前后缀。
2. 内容使用中文自然写作；保留英文产品名、repo、API、命令、版本号、status enum、claim id。
3. 采用 Forward Deployed Engineering 专题当前使用的正文逻辑，必须包含这些二级小节：{", ".join(f"`## {heading}`" for heading in MANAGED_TOPIC_BODY_REQUIRED_HEADINGS)}。
4. 不要生成 `## {LEGACY_TOPIC_BODY_HEADING}`；这个旧的外层自动生成区已经废弃，但它里面“本次更新 / 当前活跃判断 / 受限与待验证 / 已替代或削弱判断 / 长期趋势含义 / 证据入口”的阅读逻辑需要保留。
5. `## 短时间线` 必须按日期列出历史消息源：日期、1-2 句趋势含义、claim id、证据链接、lifecycle status。不要继续堆长篇历史“延续判断”正文。
6. 必须把 payload 中的 `required_claim_ids` 原样写进正文，作为可追溯锚点，并为每个 claim 列出至少一个 evidence link。
   证据链接必须是相对于专题文件所在目录的可用 Markdown 相对链接；例如专题文件在 `trend/foo.md`、证据在 `raw/2026-07-15/bar.md` 时，必须写成 `[证据](../raw/2026-07-15/bar.md)`，不能写成从仓库根目录计算的 `raw/...`。
7. 可以重排、压缩和改写长期判断，但不能让旧判断静默消失；被替代、削弱、过时、受限或待验证的判断必须在正文中保留状态语义。
8. 不要生成 `## {STATE_INDEX_HEADING}` 或 `## {UPDATE_LOG_HEADING}`；这些由父级脚本生成。
9. 不要新增未归档证据，不要根据外部知识补写事实。

SQLite 派生 payload:
```json
{json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)}
```
""".strip()


def build_topic_consolidator_command(root, run_date, trend, claims, candidates, output_path):
    return [
        "codex",
        "exec",
        "--color",
        "never",
        "--model",
        TOPIC_CONSOLIDATION_MODEL,
        "-c",
        'service_tier="fast"',
        "-c",
        f'model_reasoning_effort="{TOPIC_CONSOLIDATION_REASONING_EFFORT}"',
        "--cd",
        str(root),
        "--sandbox",
        "read-only",
        "--ephemeral",
        "--output-last-message",
        str(output_path),
        build_topic_consolidation_prompt(root, run_date, trend, claims, candidates),
    ]


def run_topic_consolidator(root, run_date, trend, claims, candidates, runner=subprocess.run):
    root = Path(root)
    with tempfile.TemporaryDirectory(prefix="dsi-trend-topic-") as tmp_dir:
        output_path = Path(tmp_dir) / f"{trend['id']}.md"
        cmd = build_topic_consolidator_command(root, run_date, trend, claims, candidates, output_path)
        proc = runner(
            cmd,
            cwd=str(root),
            text=True,
            check=False,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if proc.returncode != 0:
            stderr = (proc.stderr or "").strip()
            raise RuntimeError(f"topic consolidator failed for {trend['id']} with exit {proc.returncode}: {stderr}")
        section = read_text(output_path).strip()
    errors = validate_managed_topic_body(
        section,
        run_date,
        trend,
        claims,
        candidates,
        root=root,
        topic_path=root / trend["timeline"],
    )
    if errors:
        raise RuntimeError("\n".join(errors))
    return section


def render_topic_report(root, trend, run_date, claims, candidates, body_section, rewrite_performed=True):
    topic_path = Path(root) / trend["timeline"]
    existing = read_text(topic_path, f"# {trend['label']} 趋势报告\n")
    existing = replace_managed_topic_body(existing, body_section)
    for heading in [STATE_INDEX_HEADING, LEGACY_STATE_INDEX_HEADING, UPDATE_LOG_HEADING, LEGACY_UPDATE_LOG_HEADING]:
        existing = remove_section(existing, heading)
    section = render_status_index(root, topic_path, claims)
    update_log = render_update_log(trend, run_date, candidates, rewrite_performed=rewrite_performed)
    return existing.rstrip() + "\n\n" + section + "\n" + update_log


def record_phase2_run(conn, run_date, status, input_watermark, files_changed, verification_ok, error=""):
    timestamp = now_local()
    conn.execute(
        """
        INSERT INTO trend_phase2_runs (
            run_date, status, input_watermark, files_changed_json,
            verification_ok, error, started_at, finished_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(run_date) DO UPDATE SET
            status = excluded.status,
            input_watermark = excluded.input_watermark,
            files_changed_json = excluded.files_changed_json,
            verification_ok = excluded.verification_ok,
            error = excluded.error,
            finished_at = excluded.finished_at
        """,
        (
            run_date,
            status,
            input_watermark,
            json_dumps(files_changed),
            1 if verification_ok else 0,
            error or "",
            timestamp,
            timestamp,
        ),
    )


def trend_requires_topic_rewrite(candidates):
    return any(
        candidate["candidate_status"] in TOPIC_BODY_CLAIM_STATUSES and candidate_should_produce_claim(candidate)
        for candidate in candidates
    )


def run_phase2(run_date, root=ROOT, runner=subprocess.run):
    root = Path(root)
    with connect_db(root) as conn:
        migrate(conn)
        trends = state_trends(conn, root=root)
        candidates = candidate_rows(conn, run_date)
        preflight_trend_markers(run_date, trends, root=root)
        watermark = phase2_input_watermark(candidates)
        acquire_global_job(conn, run_date, watermark)
        try:
            promote_candidates_to_claims(conn, run_date, candidates)
            conn.commit()

            refreshed_claims = claim_rows(conn)
            candidates_by_trend = {
                trend["id"]: [row for row in candidates if row["trend_id"] == trend["id"]] for trend in trends
            }
            claims_by_trend = {
                trend["id"]: [row for row in refreshed_claims if row["trend_id"] == trend["id"]] for trend in trends
            }
            topic_body_sections = {}
            rewrite_performed_by_trend = {}
            rewritten_trends = []
            skipped_rewrite_trends = []
            for trend in trends:
                trend_candidates = candidates_by_trend.get(trend["id"], [])
                if trend_requires_topic_rewrite(trend_candidates):
                    topic_body_sections[trend["id"]] = run_topic_consolidator(
                        root,
                        run_date,
                        trend,
                        claims_by_trend[trend["id"]],
                        trend_candidates,
                        runner=runner,
                    )
                    rewrite_performed_by_trend[trend["id"]] = True
                    rewritten_trends.append(trend["id"])
                else:
                    topic_path = root / trend["timeline"]
                    topic_body_sections[trend["id"]] = managed_topic_body(read_text(topic_path))
                    rewrite_performed_by_trend[trend["id"]] = False
                    skipped_rewrite_trends.append(trend["id"])

            daily_report_path = Path(root) / "trend" / "reports" / f"{run_date}-trend-report.md"
            rendered_files = {
                daily_report_path: render_daily_trend_report(root, run_date, trends, candidates_by_trend)
            }
            for trend in trends:
                topic_path = Path(root) / trend["timeline"]
                rendered_files[topic_path] = render_topic_report(
                    root,
                    trend,
                    run_date,
                    claims_by_trend[trend["id"]],
                    candidates_by_trend.get(trend["id"], []),
                    topic_body_sections[trend["id"]],
                    rewrite_performed=rewrite_performed_by_trend[trend["id"]],
                )

            for path, text in rendered_files.items():
                write_text(path, text)
            files_changed = [relative_to_root(root, path) for path in rendered_files]
            result = verify_non_destructive(run_date, root=root)
            status = "succeeded" if result.ok else "failed"
            error = "\n".join(result.errors)
            record_phase2_run(conn, run_date, status, watermark, files_changed, result.ok, error)
            finish_global_job(conn, run_date, status, watermark, error=error)
            conn.commit()
            if not result.ok:
                raise SystemExit(error)
            return {
                "files_changed": files_changed,
                "verification": result.to_dict(),
                "rewritten_trends": rewritten_trends,
                "skipped_rewrite_trends": skipped_rewrite_trends,
            }
        except Exception as exc:
            error = str(exc)
            record_phase2_run(conn, run_date, "failed", watermark, [], False, error)
            finish_global_job(conn, run_date, "failed", watermark, error=error)
            conn.commit()
            raise


def state_index_section(text):
    heading_pattern = rf"(?:{re.escape(STATE_INDEX_HEADING)}|{re.escape(LEGACY_STATE_INDEX_HEADING)})"
    match = re.search(
        rf"^## {heading_pattern}\n(?P<body>.*?)(?=^## |\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not match:
        return ""
    return match.group("body")


def claim_ids_in_state_index(text):
    section = state_index_section(text)
    return set(re.findall(r"`((?:trend-claim|claim)-[^`]+)`", section))


def markdown_links(text):
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def validate_markdown_links(root, file_path, errors):
    root = Path(root)
    file_path = Path(file_path)
    text = read_text(file_path)
    for href in markdown_links(text):
        if href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_part = href.split("#", 1)[0]
        if not target_part:
            continue
        target = (file_path.parent / target_part).resolve()
        try:
            target.relative_to(root.resolve())
        except ValueError:
            errors.append(f"{relative_to_root(root, file_path)} has link outside repo: {href}")
            continue
        if not target.exists():
            errors.append(f"{relative_to_root(root, file_path)} has missing relative link: {href}")


def verify_non_destructive(run_date, root=ROOT):
    root = Path(root)
    errors = []
    db_path = root / DB_RELATIVE_PATH
    if not db_path.exists():
        return VerifyResult([f"missing SQLite state database: {DB_RELATIVE_PATH.as_posix()}"])

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        trends = state_trends(conn, root=root)
        candidates = candidate_rows(conn, run_date)
        claims = claim_rows(conn)

    claims_by_id = {claim["claim_id"]: claim for claim in claims}
    daily_report_path = root / "trend" / "reports" / f"{run_date}-trend-report.md"
    daily_report = read_text(daily_report_path)
    if not daily_report:
        errors.append(f"missing daily trend report: {relative_to_root(root, daily_report_path)}")
    for trend in trends:
        if trend["id"] not in daily_report and trend["label"] not in daily_report:
            errors.append(f"daily trend report is missing enabled trend {trend['id']}")

    for trend in trends:
        marker, _ = status_marker_for_trend(root, run_date, trend)
        if not marker:
            errors.append(f"missing trend raw manifest/no-new-signal for {trend['id']}")

    claims_by_trend = {trend["id"]: [] for trend in trends}
    for claim in claims:
        claims_by_trend.setdefault(claim["trend_id"], []).append(claim)
        if claim["lifecycle_status"] != "active":
            if not claim["status_note"].strip():
                errors.append(f"claim {claim['claim_id']} has non-active status without status_note")
            refs = parse_evidence_refs(claim)
            if not refs and not claim["replacement_claim_id"].strip():
                errors.append(f"claim {claim['claim_id']} has non-active status without evidence or replacement pointer")

    for candidate in candidates:
        if not candidate_should_produce_claim(candidate):
            continue
        expected_claim_id = claim_id_for_candidate(candidate)
        claim = claims_by_id.get(expected_claim_id)
        if not claim:
            errors.append(
                f"candidate {candidate['candidate_id']} missing expected claim {expected_claim_id} for trend {candidate['trend_id']}"
            )
            continue
        if claim["trend_id"] != candidate["trend_id"]:
            errors.append(
                f"candidate {candidate['candidate_id']} routed to wrong trend: {claim['trend_id']} != {candidate['trend_id']}"
            )
        if claim["claim_date"] != run_date:
            errors.append(f"candidate {candidate['candidate_id']} claim {expected_claim_id} has wrong claim_date")
        expected_text = compact_text(candidate["trend_meaning"], limit=180)
        if claim["claim_text"] != expected_text:
            errors.append(f"candidate {candidate['candidate_id']} claim_text does not match expected trend meaning")

    candidates_by_trend = {trend["id"]: [] for trend in trends}
    for candidate in candidates:
        candidates_by_trend.setdefault(candidate["trend_id"], []).append(candidate)

    for trend in trends:
        topic_path = root / trend["timeline"]
        topic_text = read_text(topic_path)
        if not topic_text:
            errors.append(f"missing topic report for {trend['id']}: {trend['timeline']}")
            continue
        if f"## {STATE_INDEX_HEADING}" not in topic_text and f"## {LEGACY_STATE_INDEX_HEADING}" not in topic_text:
            errors.append(f"topic report {trend['timeline']} missing Claim State Index")
            continue
        body_section = managed_topic_body(topic_text)
        if not body_section:
            errors.append(f"topic report {trend['timeline']} missing managed topic body")
        elif trend_requires_topic_rewrite(candidates_by_trend.get(trend["id"], [])):
            errors.extend(
                validate_managed_topic_body(
                    body_section,
                    run_date,
                    trend,
                    claims_by_trend.get(trend["id"], []),
                    candidates_by_trend.get(trend["id"], []),
                    root=root,
                    topic_path=topic_path,
                )
            )
        index_ids = claim_ids_in_state_index(topic_text)
        expected_ids = {claim["claim_id"] for claim in claims_by_trend.get(trend["id"], [])}
        for claim in claims_by_trend.get(trend["id"], []):
            section = state_index_section(topic_text)
            if claim["claim_id"] not in index_ids:
                errors.append(f"claim {claim['claim_id']} missing from topic status index {trend['timeline']}")
            if claim["lifecycle_status"] not in section:
                errors.append(f"claim {claim['claim_id']} status mismatch in topic status index {trend['timeline']}")
            if claim["claim_text"] and claim["claim_text"] not in section:
                errors.append(f"claim {claim['claim_id']} claim_text missing from topic status index {trend['timeline']}")
            if claim["markdown_anchor"] and claim["markdown_anchor"] not in section:
                errors.append(f"claim {claim['claim_id']} anchor missing in topic status index {trend['timeline']}")
        for extra_id in sorted(index_ids - expected_ids):
            errors.append(f"topic status index {trend['timeline']} has claim not present in SQLite: {extra_id}")
        validate_markdown_links(root, topic_path, errors)

    if daily_report:
        validate_markdown_links(root, daily_report_path, errors)

    return VerifyResult(errors)


def run_all(run_date, root=ROOT, runner=subprocess.run):
    candidates = run_phase1(run_date, root=root)
    phase2 = run_phase2(run_date, root=root, runner=runner)
    return {"candidates": len(candidates), **phase2}


def main(argv=None, runner=subprocess.run):
    parser = argparse.ArgumentParser(description="Run DSI trend Phase 1/Phase 2 state machine.")
    parser.add_argument("--date", required=True)
    parser.add_argument("--phase", choices=["phase1", "phase2", "all"], default="all")
    parser.add_argument("--check", action="store_true", help="Run the non-destructive verifier only.")
    parser.add_argument("--root", default=str(ROOT))
    args = parser.parse_args(argv)

    root = Path(args.root)
    if args.check:
        result = verify_non_destructive(args.date, root=root)
        print(json.dumps({"event": "trend_stage_check", **result.to_dict()}, ensure_ascii=False, indent=2))
        return 0 if result.ok else 1

    if args.phase == "phase1":
        candidates = run_phase1(args.date, root=root)
        payload = {"event": "trend_phase1_complete", "candidate_count": len(candidates)}
    elif args.phase == "phase2":
        payload = {"event": "trend_phase2_complete", **run_phase2(args.date, root=root, runner=runner)}
    else:
        payload = {"event": "trend_stage_complete", **run_all(args.date, root=root, runner=runner)}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
