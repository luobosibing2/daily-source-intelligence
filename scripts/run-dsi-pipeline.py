#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def now_local():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_json(path, default):
    path = Path(path)
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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


def compact_text(value, limit=180):
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def body_path_if_readable(root, fulltext_status, path):
    relative = relative_to_root(root, path)
    if fulltext_status == "ok" and relative and (Path(root) / relative).exists():
        return relative
    return ""


def seen_before_run_date(item, run_date):
    first_seen = str(item.get("first_seen") or "")[:10]
    return not first_seen or first_seen < run_date


def load_seen_before_run_date(root, run_date):
    payload = read_json(Path(root) / "state" / "seen.json", {"items": []})
    ids = set()
    urls = set()
    for item in payload.get("items", []) or []:
        if not seen_before_run_date(item, run_date):
            continue
        item_id = str(item.get("id") or "").strip()
        url = str(item.get("url") or "").strip()
        if item_id:
            ids.add(item_id)
        if url:
            urls.add(url)
            ids.add(f"url:{url}")
    return {"ids": ids, "urls": urls}


def already_seen(seen, *, ids=(), urls=()):
    for item_id in ids:
        if item_id and item_id in seen["ids"]:
            return True
    for url in urls:
        if url and (url in seen["urls"] or f"url:{url}" in seen["ids"]):
            return True
    return False


def reading_entry(
    *,
    root,
    source_type,
    topic,
    priority,
    evidence_level,
    title,
    url,
    local_body_path,
    fulltext_status,
    why_read,
):
    return {
        "source_type": source_type,
        "topic": topic,
        "priority": int(priority or 0),
        "evidence_level": evidence_level or "",
        "title": compact_text(title),
        "url": url or "",
        "local_body_path": relative_to_root(root, local_body_path),
        "fulltext_status": fulltext_status or "",
        "why_read": why_read or "",
    }


def build_report_reading_list(run_date, root=ROOT):
    root = Path(root)
    raw_dir = root / "raw" / run_date
    entries = []
    seen = load_seen_before_run_date(root, run_date)

    rss = read_json(raw_dir / "rss-items.json", {"sources": []})
    for source in rss.get("sources", []) or []:
        for item in source.get("items", []) or []:
            if item.get("relevance_status") not in {"matched", "always_read"}:
                continue
            url = item.get("url")
            if already_seen(seen, ids=[f"url:{url}" if url else ""], urls=[url]):
                continue
            status = item.get("fulltext_status") or ""
            body_path = body_path_if_readable(root, status, item.get("fulltext_path"))
            why = "read matched RSS fulltext body" if body_path else "boundary row: matched RSS item without readable fulltext body"
            entries.append(
                reading_entry(
                    root=root,
                    source_type="rss-fulltext",
                    topic=",".join(item.get("matched_topics") or source.get("topics") or []),
                    priority=70 if item.get("relevance_status") == "always_read" else 50,
                    evidence_level="official-source" if item.get("intelligence_department") else "secondary-source",
                    title=item.get("title") or item.get("url"),
                    url=item.get("url"),
                    local_body_path=body_path,
                    fulltext_status=status,
                    why_read=why,
                )
            )

    official = read_json(raw_dir / "official-link-candidates.json", {"candidates": []})
    for candidate in official.get("candidates", []) or []:
        expanded_url = candidate.get("expanded_url")
        tweet_url = candidate.get("tweet_url")
        tweet_id = candidate.get("tweet_id")
        if already_seen(
            seen,
            ids=[
                f"url:{expanded_url}" if expanded_url else "",
                f"url:{tweet_url}" if tweet_url else "",
                f"tweet:{tweet_id}" if tweet_id else "",
            ],
            urls=[expanded_url, tweet_url],
        ):
            continue
        status = candidate.get("fulltext_status") or ""
        body_path = body_path_if_readable(root, status, candidate.get("fulltext_path"))
        entries.append(
            reading_entry(
                root=root,
                source_type="official-link-candidate",
                topic="official-link-candidate",
                priority=candidate.get("score") or 60,
                evidence_level=candidate.get("evidence_level") or "direct-x",
                title=candidate.get("expanded_url") or candidate.get("tweet_url") or candidate.get("tweet_id"),
                url=candidate.get("expanded_url") or candidate.get("tweet_url"),
                local_body_path=body_path,
                fulltext_status=status,
                why_read="read official link candidate body" if body_path else "boundary row: official link candidate without readable fulltext body",
            )
        )

    trending = read_json(raw_dir / "github-trending.json", {"sources": []})
    for source in trending.get("sources", []) or []:
        for item in source.get("items", []) or []:
            repo = item.get("repo")
            url = item.get("url")
            if already_seen(seen, ids=[f"github-trending:{repo}" if repo else "", f"url:{url}" if url else ""], urls=[url]):
                continue
            status = item.get("readme_status") or ""
            body_path = body_path_if_readable(root, "ok" if status == "ok" else status, item.get("readme_path"))
            entries.append(
                reading_entry(
                    root=root,
                    source_type="github-trending-readme",
                    topic="github-trending",
                    priority=35,
                    evidence_level="secondary-source",
                    title=item.get("readme_title") or item.get("repo"),
                    url=item.get("url"),
                    local_body_path=body_path,
                    fulltext_status=status,
                    why_read="read GitHub Trending README body" if body_path else "boundary row: GitHub Trending repo without readable README",
                )
            )

    github = read_json(raw_dir / "github-items.json", {"sources": []})
    for source in github.get("sources", []) or []:
        for item in source.get("items", []) or []:
            if item.get("relevance_status") != "always_read" and not item.get("fulltext_path"):
                continue
            url = item.get("url")
            if already_seen(seen, ids=[f"url:{url}" if url else ""], urls=[url]):
                continue
            status = item.get("fulltext_status") or ""
            body_path = body_path_if_readable(root, status, item.get("fulltext_path"))
            entries.append(
                reading_entry(
                    root=root,
                    source_type="github-release-body",
                    topic=",".join(source.get("topics") or []),
                    priority=65 if item.get("relevance_status") == "always_read" else 45,
                    evidence_level="official-source",
                    title=item.get("title") or item.get("url"),
                    url=item.get("url"),
                    local_body_path=body_path,
                    fulltext_status=status,
                    why_read="read release Atom body" if body_path else "boundary row: release entry without readable body",
                )
            )

    topic_brief = read_json(raw_dir / "twitter-topic-brief.json", {"topics": []})
    for topic in topic_brief.get("topics", []) or []:
        for item in topic.get("items", []) or []:
            tweet_id = item.get("tweet_id")
            url = item.get("url")
            if already_seen(seen, ids=[f"tweet:{tweet_id}" if tweet_id else "", f"url:{url}" if url else ""], urls=[url]):
                continue
            entries.append(
                reading_entry(
                    root=root,
                    source_type="topic-direct-x",
                    topic=topic.get("id") or topic.get("label") or "",
                    priority=item.get("score") or 0,
                    evidence_level=item.get("evidence_level") or "direct-x",
                    title=item.get("text_excerpt") or item.get("tweet_id"),
                    url=item.get("url"),
                    local_body_path="",
                    fulltext_status="n/a",
                    why_read="read structured priority X topic item; direct evidence is in twitter-topic-brief.json",
                )
            )

    entries.sort(key=lambda item: (-item["priority"], item["source_type"], item["title"]))
    return {
        "schema_version": 1,
        "run_date": run_date,
        "generated_at": now_local(),
        "entries": entries,
    }


def build_run_summary(run_date, root=ROOT, reading_list=None, command_results=None):
    root = Path(root)
    raw_dir = root / "raw" / run_date
    reading_list = reading_list or read_json(raw_dir / "report-reading-list.json", {"entries": []})
    manifest = read_json(raw_dir / "manifest.json", {})
    entries = reading_list.get("entries", [])
    by_type = {}
    for entry in entries:
        by_type[entry["source_type"]] = by_type.get(entry["source_type"], 0) + 1
    return {
        "schema_version": 1,
        "run_date": run_date,
        "generated_at": now_local(),
        "reading_list": f"raw/{run_date}/report-reading-list.json",
        "manifest": f"raw/{run_date}/manifest.json" if (raw_dir / "manifest.json").exists() else "",
        "candidate_audit": f"reviews/{run_date}-candidate-audit.md" if (root / "reviews" / f"{run_date}-candidate-audit.md").exists() else "",
        "counts": {
            "reading_list_entries": len(entries),
            "readable_body_entries": sum(1 for entry in entries if entry.get("local_body_path")),
            "boundary_entries": sum(1 for entry in entries if not entry.get("local_body_path")),
            "by_source_type": by_type,
        },
        "manifest_summary": manifest.get("summary") or {},
        "commands": command_results or [],
    }


def run_command(root, cmd, env=None):
    proc = subprocess.run(
        cmd,
        cwd=str(root),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        env=env,
    )
    return {
        "cmd": " ".join(cmd),
        "returncode": proc.returncode,
        "stdout_excerpt": compact_text(proc.stdout, limit=500),
        "stderr_excerpt": compact_text(proc.stderr, limit=500),
    }


def run_pipeline(run_date, root=ROOT, run_collection=True):
    root = Path(root)
    env = dict(os.environ)
    env["RUN_DATE"] = run_date
    results = []
    if run_collection:
        results.append(run_command(root, ["python3", "scripts/collect-stable-sources.py"], env=env))
        results.append(run_command(root, ["python3", "scripts/collect-twitterapi-io.py"], env=env))
    results.append(run_command(root, ["python3", "scripts/official-link-candidates.py", "--date", run_date, "--root", str(root)], env=env))
    results.append(run_command(root, ["python3", "scripts/build-twitter-topic-brief.py", "--date", run_date, "--root", str(root)], env=env))
    results.append(run_command(root, ["python3", "scripts/update-state.py"], env=env))

    report_path = root / "docs" / f"{run_date}-daily-intel.md"
    if report_path.exists():
        results.append(run_command(root, ["python3", "scripts/candidate-audit.py", "--date", run_date, "--root", str(root)], env=env))

    reading_list = build_report_reading_list(run_date, root=root)
    write_json(root / "raw" / run_date / "report-reading-list.json", reading_list)
    summary = build_run_summary(run_date, root=root, reading_list=reading_list, command_results=results)
    write_json(root / "raw" / run_date / "run-summary.json", summary)
    return summary


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run deterministic DSI collection and write report input controls.")
    parser.add_argument("--date", default=os.environ.get("RUN_DATE") or datetime.now().astimezone().date().isoformat())
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--skip-collection", action="store_true", help="Only rebuild derived controls from existing raw files.")
    args = parser.parse_args(argv)

    summary = run_pipeline(args.date, root=Path(args.root), run_collection=not args.skip_collection)
    print(json.dumps({"event": "dsi_pipeline_complete", **summary}, ensure_ascii=False, indent=2))
    return 0 if all(item.get("returncode") == 0 for item in summary.get("commands", [])) else 1


if __name__ == "__main__":
    sys.exit(main())
