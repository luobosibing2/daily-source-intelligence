#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
MARKER_RE = re.compile(r"dsi-candidate-audit:\s*covered=(\d+)\s+missed=(\d+)", re.I)
PAIR_RE = re.compile(r"covered\s*[=:]\s*(\d+)\D{0,20}missed\s*[=:]\s*(\d+)", re.I)
ZH_RE = re.compile(r"覆盖\s*(\d+)\s*条[^\n]{0,20}?标记\s*(\d+)\s*条[^\n]{0,8}?missed", re.I)


def read_json(path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def declared_counts(report_text):
    for pattern in (MARKER_RE, PAIR_RE, ZH_RE):
        matches = list(pattern.finditer(report_text))
        if matches:
            match = matches[-1]
            return {"covered": int(match.group(1)), "missed": int(match.group(2))}
    return None


def broken_local_links(path, root):
    if not path.exists():
        return []
    broken = []
    for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(Path(root).resolve())
        except ValueError:
            broken.append(target)
            continue
        if not resolved.exists():
            broken.append(target)
    return broken


def validate(run_date, root=ROOT, strict=False):
    root = Path(root)
    report_path = root / "docs" / f"{run_date}-daily-intel.md"
    audit_path = root / "reviews" / f"{run_date}-candidate-audit.json"
    errors = []
    warnings = []
    if not report_path.is_file():
        errors.append(f"daily report missing: {report_path.relative_to(root)}")
    if not audit_path.is_file():
        errors.append(f"candidate audit JSON missing: {audit_path.relative_to(root)}")
    if errors:
        return {"event": "daily_report_check", "ok": False, "errors": errors, "warnings": warnings}

    report_text = report_path.read_text(encoding="utf-8")
    audit = read_json(audit_path, {})
    expected_report = f"docs/{run_date}-daily-intel.md"
    if audit.get("daily_report") != expected_report:
        errors.append(f"audit daily_report mismatch: expected {expected_report!r}, got {audit.get('daily_report')!r}")
    actual_sha = hashlib.sha256(report_text.encode("utf-8")).hexdigest()
    if audit.get("daily_report_sha256") != actual_sha:
        errors.append("candidate audit report SHA256 does not match the current daily report")

    rows = audit.get("rows") or []
    actual_counts = {
        "total": len(rows),
        "covered": sum(1 for row in rows if row.get("status") == "covered"),
        "missed": sum(1 for row in rows if row.get("status") == "missed"),
    }
    if audit.get("counts") != actual_counts:
        errors.append(f"candidate audit counts do not match rows: stored={audit.get('counts')}, actual={actual_counts}")

    declared = declared_counts(report_text)
    if declared is None:
        message = "daily report does not declare final candidate audit covered/missed counts"
        (errors if strict else warnings).append(message)
    elif declared != {key: actual_counts[key] for key in ("covered", "missed")}:
        errors.append(
            "candidate audit count mismatch: "
            f"report covered={declared['covered']} missed={declared['missed']}; "
            f"audit covered={actual_counts['covered']} missed={actual_counts['missed']}"
        )

    contradictory = [
        row.get("candidate_id") or row.get("signal")
        for row in rows
        if row.get("status") == "missed" and row.get("disposition") == "covered_in_report"
    ]
    if contradictory:
        errors.append("missed candidates cannot use covered_in_report: " + ", ".join(contradictory))

    unresolved = [
        row.get("candidate_id") or row.get("signal")
        for row in rows
        if row.get("status") == "missed"
        and row.get("category") == "official-link-candidate"
        and not row.get("disposition")
    ]
    if unresolved:
        errors.append(f"missed official-link candidates require disposition: {', '.join(unresolved)}")

    unresolved_articles = [
        row.get("candidate_id") or row.get("signal")
        for row in rows
        if row.get("status") == "missed"
        and row.get("category") == "official-page-article"
        and (not row.get("disposition") or not str(row.get("disposition_note") or "").strip())
    ]
    if strict and unresolved_articles:
        errors.append(
            "missed official-page articles require disposition and disposition note: "
            + ", ".join(unresolved_articles)
        )

    unresolved_podcasts = [
        row.get("candidate_id") or row.get("signal")
        for row in rows
        if row.get("status") == "missed"
        and row.get("category") == "podcast-transcript"
        and not row.get("disposition")
    ]
    if strict and unresolved_podcasts:
        errors.append(
            "missed podcast transcripts require disposition: "
            + ", ".join(unresolved_podcasts)
        )

    for path in (report_path, root / "reviews" / f"{run_date}-candidate-audit.md"):
        broken = broken_local_links(path, root)
        if broken:
            errors.append(f"broken local links in {path.relative_to(root)}: {', '.join(broken)}")

    return {
        "event": "daily_report_check",
        "run_date": run_date,
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "counts": actual_counts,
        "report_sha256": actual_sha,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate a DSI daily report against its audit artifact.")
    parser.add_argument("--date", required=True)
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)
    result = validate(args.date, root=Path(args.root), strict=args.strict)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
