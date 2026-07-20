#!/usr/bin/env python3
"""Unified command-line entry point for Daily Source Intelligence."""

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STABLE_CHANNELS = {"rss", "github-releases", "github-trending", "official-pages"}
ALL_CHANNELS = STABLE_CHANNELS | {"x"}
OUTPUT_BY_CHANNEL = {
    "rss": "rss-items.json",
    "github-releases": "github-items.json",
    "github-trending": "github-trending.json",
    "official-pages": "official-pages.json",
    "x": "twitterapi-io-results.json",
}
PREPARE_INPUTS = [
    "rss-items.json",
    "github-items.json",
    "github-trending.json",
    "official-pages.json",
    "twitterapi-io-results.json",
    "official-link-candidates.json",
    "twitter-topic-brief.json",
]


def sha256_path(path):
    path = Path(path)
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else ""


def read_json(path, default):
    if not Path(path).exists():
        return default
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def expand_channels(values):
    values = values or ["all"]
    result = set()
    for value in values:
        if value == "all":
            result.update(ALL_CHANNELS)
        elif value == "stable":
            result.update(STABLE_CHANNELS)
        else:
            result.add(value)
    return result


def parse_sources(values, channels):
    if values and len(channels) != 1:
        raise ValueError("--source requires exactly one concrete --channel")
    selected = {}
    for value in values or []:
        if ":" not in value:
            if len(channels) != 1:
                raise ValueError(f"ambiguous source {value!r}; use channel:id")
            channel, source_id = next(iter(channels)), value
        else:
            channel, source_id = value.split(":", 1)
        if channel not in channels:
            raise ValueError(f"source channel {channel!r} is not selected")
        if channel not in ALL_CHANNELS or not source_id:
            raise ValueError(f"invalid source selector: {value!r}")
        selected.setdefault(channel, []).append(source_id)
    if len(selected) > 1:
        raise ValueError("source targeting currently accepts one channel per run")
    return selected


def run_command(root, command, env=None):
    result = subprocess.run(command, cwd=str(root), env=env, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
    if result.stderr:
        print(result.stderr, file=sys.stderr, end="" if result.stderr.endswith("\n") else "\n")
    return result.returncode


def collection_fingerprint(root, run_date, channels, sources):
    payload = {
        "run_date": run_date,
        "channels": sorted(channels),
        "sources": sources,
        "config": {
            "sources": sha256_path(Path(root) / "config" / "sources.yaml"),
            "topics": sha256_path(Path(root) / "config" / "topics.yaml"),
        },
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()


def output_hashes(root, run_date, channels):
    raw_dir = Path(root) / "raw" / run_date
    return {channel: sha256_path(raw_dir / OUTPUT_BY_CHANNEL[channel]) for channel in sorted(channels)}


def resume_hit(root, run_date, channels, fingerprint):
    state = read_json(Path(root) / "raw" / run_date / "run-state.json", {})
    collection = state.get("collection") or {}
    expected = collection.get("outputs") or {}
    return (
        collection.get("status") == "ok"
        and collection.get("input_sha256") == fingerprint
        and expected
        and expected == output_hashes(root, run_date, channels)
    )


def record_collection(root, run_date, channels, fingerprint):
    path = Path(root) / "raw" / run_date / "run-state.json"
    state = read_json(path, {"schema_version": 1, "run_date": run_date})
    state["collection"] = {
        "status": "ok",
        "input_sha256": fingerprint,
        "outputs": output_hashes(root, run_date, channels),
        "completed_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    write_json(path, state)


def prepare_fingerprint(root, run_date):
    root = Path(root)
    payload = {
        "raw": {name: sha256_path(root / "raw" / run_date / name) for name in PREPARE_INPUTS},
        "seen": sha256_path(root / "state" / "seen.json"),
        "report": sha256_path(root / "docs" / f"{run_date}-daily-intel.md"),
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()


def prepare_output_hashes(root, run_date):
    root = Path(root)
    paths = [
        root / "raw" / run_date / "signals.json",
        root / "raw" / run_date / "report-reading-list.json",
        root / "raw" / run_date / "run-summary.json",
        root / "reviews" / f"{run_date}-candidate-audit.json",
        root / "docs" / f"{run_date}-daily-intel.index.json",
        root / "docs" / f"{run_date}-daily-intel.html",
        root / "docs" / "index.html",
    ]
    return {str(path.relative_to(root)): sha256_path(path) for path in paths}


def prepare_resume_hit(root, run_date, fingerprint):
    state = read_json(Path(root) / "raw" / run_date / "run-state.json", {})
    step = state.get("prepare") or {}
    outputs = step.get("outputs") or {}
    return (
        step.get("status") == "ok"
        and step.get("input_sha256") == fingerprint
        and outputs
        and outputs == prepare_output_hashes(root, run_date)
    )


def record_prepare(root, run_date, fingerprint):
    path = Path(root) / "raw" / run_date / "run-state.json"
    state = read_json(path, {"schema_version": 1, "run_date": run_date})
    state["prepare"] = {
        "status": "ok",
        "input_sha256": fingerprint,
        "outputs": prepare_output_hashes(root, run_date),
        "completed_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    write_json(path, state)


def prepare(root, run_date, dry_run=False, resume=False):
    plan = [
        ["python3", "scripts/run-dsi-pipeline.py", "--date", run_date, "--skip-collection"],
        ["python3", "scripts/validate-daily-report.py", "--date", run_date, "--strict"],
        ["python3", "scripts/build-daily-bundle.py", "--date", run_date],
    ]
    fingerprint = prepare_fingerprint(root, run_date)
    hit = bool(resume and prepare_resume_hit(root, run_date, fingerprint))
    if dry_run:
        print(json.dumps({"event": "dsi_plan", "command": "prepare", "resume_hit": hit, "steps": plan}, ensure_ascii=False, indent=2))
        return 0
    if hit:
        print(json.dumps({"event": "prepare_resumed", "input_sha256": fingerprint}, ensure_ascii=False))
        return 0
    code = run_command(root, plan[0])
    report = Path(root) / "docs" / f"{run_date}-daily-intel.md"
    if code or not report.exists():
        return code
    code = run_command(root, plan[1])
    if code:
        return code
    code = run_command(root, plan[2])
    if code == 0:
        record_prepare(root, run_date, prepare_fingerprint(root, run_date))
    return code


def run_collection(args):
    root = Path(args.root).resolve()
    channels = expand_channels(args.channel)
    try:
        selected = parse_sources(args.source, channels)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    fingerprint = collection_fingerprint(root, args.date, channels, selected)
    plan = {
        "event": "dsi_plan",
        "command": "run",
        "run_date": args.date,
        "channels": sorted(channels),
        "sources": selected,
        "resume_hit": bool(args.resume and resume_hit(root, args.date, channels, fingerprint)),
    }
    if args.dry_run:
        print(json.dumps(plan, ensure_ascii=False, indent=2))
        return 0
    if plan["resume_hit"]:
        print(json.dumps({"event": "collection_resumed", "input_sha256": fingerprint}, ensure_ascii=False))
        return prepare(root, args.date, resume=args.resume)

    env = dict(os.environ)
    env["RUN_DATE"] = args.date
    codes = []
    stable = sorted(channels & STABLE_CHANNELS)
    if stable:
        command = ["python3", "scripts/collect-stable-sources.py", "--date", args.date]
        for channel in stable:
            command.extend(["--channel", channel])
        for source_id in selected.get(stable[0], []) if len(stable) == 1 else []:
            command.extend(["--source", source_id])
        codes.append(run_command(root, command, env=env))
    if "x" in channels:
        command = ["python3", "scripts/collect-twitterapi-io.py", "--date", args.date]
        for source_id in selected.get("x", []):
            command.extend(["--source", source_id])
        codes.append(run_command(root, command, env=env))
    if all(code == 0 for code in codes):
        record_collection(root, args.date, channels, fingerprint)
    prepare_code = prepare(root, args.date, resume=args.resume)
    return next((code for code in codes if code), prepare_code)


def check(root, run_date):
    commands = [
        ["python3", "scripts/validate-daily-report.py", "--date", run_date, "--strict"],
        ["python3", "scripts/run-trend-stage.py", "--date", run_date, "--check"],
    ]
    codes = [run_command(root, command) for command in commands]
    return next((code for code in codes if code), 0)


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--date", required=True)
    common.add_argument("--root", default=str(ROOT))

    run_parser = subparsers.add_parser("run", parents=[common])
    run_parser.add_argument("--channel", action="append", choices=sorted(ALL_CHANNELS | {"stable", "all"}))
    run_parser.add_argument("--source", action="append", default=[], help="channel:id")
    run_parser.add_argument("--dry-run", action="store_true")
    run_parser.add_argument("--resume", action="store_true")

    prepare_parser = subparsers.add_parser("prepare", parents=[common])
    prepare_parser.add_argument("--dry-run", action="store_true")
    prepare_parser.add_argument("--resume", action="store_true", help="accepted for command symmetry")

    subparsers.add_parser("check", parents=[common])
    publish_parser = subparsers.add_parser("publish", parents=[common])
    publish_parser.add_argument("--main-worktree")
    publish_parser.add_argument("--push", action="store_true")
    publish_parser.add_argument("--dry-run", action="store_true")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    root = Path(args.root).resolve()
    if root != ROOT.resolve():
        print("collection/state scripts currently require --root to be the repository root", file=sys.stderr)
        return 2
    if args.command == "run":
        return run_collection(args)
    if args.command == "prepare":
        return prepare(root, args.date, dry_run=args.dry_run, resume=args.resume)
    if args.command == "check":
        return check(root, args.date)
    if args.command == "publish":
        if not args.dry_run:
            code = check(root, args.date)
            if code:
                return code
        command = ["python3", "scripts/publish-daily-to-main.py", "--date", args.date]
        if args.main_worktree:
            command.extend(["--main-worktree", args.main_worktree])
        if args.push:
            command.append("--push")
        if args.dry_run:
            command.append("--dry-run")
        return run_command(root, command)
    return 2


if __name__ == "__main__":
    sys.exit(main())
