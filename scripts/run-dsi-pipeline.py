#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from dsi_signals import build_reading_list, build_signals


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


def compact_text(value, limit=180):
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def build_report_reading_list(run_date, root=ROOT):
    signals = build_signals(run_date, root=Path(root))
    return build_reading_list(signals, generated_at=now_local())


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
        "signals": f"raw/{run_date}/signals.json" if (raw_dir / "signals.json").exists() else "",
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
        results.append(run_command(root, ["python3", "scripts/collect-podcasts.py", "--date", run_date], env=env))
        results.append(run_command(root, ["python3", "scripts/collect-twitterapi-io.py"], env=env))
    results.append(run_command(root, ["python3", "scripts/official-link-candidates.py", "--date", run_date, "--root", str(root)], env=env))
    results.append(run_command(root, ["python3", "scripts/build-twitter-topic-brief.py", "--date", run_date, "--root", str(root)], env=env))
    results.append(run_command(root, ["python3", "scripts/update-state.py"], env=env))

    report_path = root / "docs" / f"{run_date}-daily-intel.md"
    if report_path.exists():
        results.append(run_command(root, ["python3", "scripts/candidate-audit.py", "--date", run_date, "--root", str(root)], env=env))

    signals = build_signals(run_date, root=root)
    write_json(root / "raw" / run_date / "signals.json", signals)
    reading_list = build_reading_list(signals, generated_at=now_local())
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
