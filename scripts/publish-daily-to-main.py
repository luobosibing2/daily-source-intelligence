#!/usr/bin/env python3
"""Publish one generated daily report from develop to the main worktree."""

import argparse
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MAIN_WORKTREE = ROOT.parent / f"{ROOT.name}-main"
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class PublishError(RuntimeError):
    """Raised when publishing cannot proceed without risking unrelated data."""


def git(worktree, *args):
    command = ["git", "-C", str(worktree), *args]
    result = subprocess.run(command, text=True, capture_output=True)
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        raise PublishError(f"{' '.join(command)} failed: {detail}")
    return result.stdout.strip()


def git_exit_code(worktree, *args):
    command = ["git", "-C", str(worktree), *args]
    result = subprocess.run(command, text=True, capture_output=True)
    if result.returncode not in {0, 1}:
        detail = (result.stderr or result.stdout).strip()
        raise PublishError(f"{' '.join(command)} failed: {detail}")
    return result.returncode


def validate_run_date(run_date):
    if not DATE_PATTERN.fullmatch(run_date):
        raise PublishError(f"invalid run date: {run_date!r}")
    try:
        datetime.strptime(run_date, "%Y-%m-%d")
    except ValueError as exc:
        raise PublishError(f"invalid run date: {run_date!r}") from exc


def worktree_root(worktree):
    return Path(git(worktree, "rev-parse", "--show-toplevel")).resolve()


def remote_url(worktree):
    return git(worktree, "remote", "get-url", "origin")


def ensure_source_is_develop(source_root):
    if worktree_root(source_root) != source_root.resolve():
        raise PublishError(f"source path is not the repository root: {source_root}")
    branch = git(source_root, "symbolic-ref", "--short", "HEAD")
    if branch != "develop":
        raise PublishError(f"source worktree must be on develop, found {branch!r}")


def ensure_main_is_safe(source_root, main_worktree):
    if not main_worktree.exists():
        raise PublishError(
            f"main worktree does not exist: {main_worktree}; "
            "create it with git worktree add <path> main"
        )
    if worktree_root(main_worktree) != main_worktree.resolve():
        raise PublishError(f"main path is not the expected worktree root: {main_worktree}")
    branch = git(main_worktree, "symbolic-ref", "--short", "HEAD")
    if branch != "main":
        raise PublishError(f"main worktree is not on main, found {branch!r}")
    status = git(main_worktree, "status", "--porcelain=v1")
    if status:
        raise PublishError(
            "main worktree is dirty; refusing to overwrite or commit unrelated changes:\n"
            + status
        )
    if remote_url(source_root) != remote_url(main_worktree):
        raise PublishError("source and main worktrees do not use the same origin URL")


def sync_main_from_origin(main_worktree):
    git(main_worktree, "fetch", "origin", "main")
    counts = git(main_worktree, "rev-list", "--left-right", "--count", "main...origin/main")
    ahead, behind = (int(value) for value in counts.split())
    if ahead and behind:
        raise PublishError("main has diverged from origin/main; refusing automatic repair")
    if ahead:
        pending_paths = git(main_worktree, "diff", "--name-only", "origin/main...main").splitlines()
        pending_subjects = git(main_worktree, "log", "--format=%s", "origin/main..main").splitlines()
        if not pending_subjects or any(
            not subject.startswith("data: daily source intelligence ") for subject in pending_subjects
        ):
            raise PublishError("main is ahead of origin/main with non-publisher commits; refusing automatic push")
        if any(
            not re.fullmatch(r"docs/\d{4}-\d{2}-\d{2}-daily-intel\.md", path)
            for path in pending_paths
        ):
            raise PublishError("main has pending changes outside dated daily reports; refusing automatic push")
        return True
    if behind:
        git(main_worktree, "merge", "--ff-only", "origin/main")
    return False


def report_paths(source_root, main_worktree, run_date):
    relative = Path("docs") / f"{run_date}-daily-intel.md"
    source_report = source_root / relative
    main_report = main_worktree / relative
    if not source_report.is_file():
        raise PublishError(f"daily report does not exist: {source_report}")
    return relative, source_report, main_report


def atomic_copy(source_report, main_report):
    main_report.parent.mkdir(parents=True, exist_ok=True)
    temporary = main_report.with_name(f".{main_report.name}.publish-tmp")
    try:
        shutil.copy2(source_report, temporary)
        os.replace(temporary, main_report)
    finally:
        if temporary.exists():
            temporary.unlink()


def publish(run_date, *, source_root=ROOT, main_worktree=None, push=False, dry_run=False):
    source_root = Path(source_root).resolve()
    main_worktree = Path(main_worktree or os.environ.get("DSI_MAIN_WORKTREE", DEFAULT_MAIN_WORKTREE)).resolve()
    validate_run_date(run_date)
    ensure_source_is_develop(source_root)
    ensure_main_is_safe(source_root, main_worktree)
    pending_push = sync_main_from_origin(main_worktree)
    relative, source_report, main_report = report_paths(source_root, main_worktree, run_date)

    if dry_run:
        return {
            "status": "dry-run",
            "branch": "main",
            "source_report": str(source_report),
            "target_report": str(main_report),
            "push": bool(push),
        }

    previous = main_report.read_bytes() if main_report.exists() else None
    committed = False
    try:
        atomic_copy(source_report, main_report)
        git(main_worktree, "add", "-f", "--", str(relative))
        staged = git(main_worktree, "diff", "--cached", "--name-only").splitlines()
        if not staged and pending_push and push:
            commit = git(main_worktree, "rev-parse", "HEAD")
            git(main_worktree, "push", "origin", "main")
            remote_head = git(main_worktree, "ls-remote", "origin", "refs/heads/main").split()[0]
            if remote_head != commit:
                raise PublishError(
                    f"push completed but origin/main is {remote_head}, expected {commit}"
                )
            return {
                "status": "published-pending",
                "branch": "main",
                "commit": commit,
                "target_report": str(main_report),
                "push": True,
            }
        if not staged:
            return {
                "status": "no-op",
                "branch": "main",
                "target_report": str(main_report),
                "push": False,
            }
        if staged != [relative.as_posix()]:
            raise PublishError(f"unexpected staged paths: {staged!r}")
        if git_exit_code(main_worktree, "diff", "--cached", "--quiet") == 0:
            if pending_push and push:
                commit = git(main_worktree, "rev-parse", "HEAD")
                git(main_worktree, "push", "origin", "main")
                remote_head = git(main_worktree, "ls-remote", "origin", "refs/heads/main").split()[0]
                if remote_head != commit:
                    raise PublishError(
                        f"push completed but origin/main is {remote_head}, expected {commit}"
                    )
                return {
                    "status": "published-pending",
                    "branch": "main",
                    "commit": commit,
                    "target_report": str(main_report),
                    "push": True,
                }
            return {
                "status": "no-op",
                "branch": "main",
                "target_report": str(main_report),
                "push": False,
            }
        git(main_worktree, "diff", "--cached", "--check")
        git(main_worktree, "commit", "-m", f"data: daily source intelligence {run_date}")
        committed = True
        commit = git(main_worktree, "rev-parse", "HEAD")
        if push:
            git(main_worktree, "push", "origin", "main")
            remote_head = git(main_worktree, "ls-remote", "origin", "refs/heads/main").split()[0]
            if remote_head != commit:
                raise PublishError(
                    f"push completed but origin/main is {remote_head}, expected {commit}"
                )
        return {
            "status": "published" if push else "committed",
            "branch": "main",
            "commit": commit,
            "target_report": str(main_report),
            "push": bool(push),
        }
    except Exception:
        if committed:
            raise
        if previous is None:
            if main_report.exists():
                main_report.unlink()
        else:
            main_report.write_bytes(previous)
        subprocess.run(
            ["git", "-C", str(main_worktree), "reset", "--quiet", "HEAD", "--", str(relative)],
            check=False,
            text=True,
            capture_output=True,
        )
        raise


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, help="report date in YYYY-MM-DD format")
    parser.add_argument(
        "--main-worktree",
        default=None,
        help="path to the dedicated main worktree; defaults to DSI_MAIN_WORKTREE or a sibling worktree",
    )
    parser.add_argument("--push", action="store_true", help="push the committed report to origin/main")
    parser.add_argument("--dry-run", action="store_true", help="validate paths and print the planned target")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    try:
        result = publish(
            args.date,
            main_worktree=args.main_worktree,
            push=args.push,
            dry_run=args.dry_run,
        )
    except PublishError as exc:
        print(f"publish failed: {exc}", file=sys.stderr)
        return 1
    for key, value in result.items():
        print(f"{key}={value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
