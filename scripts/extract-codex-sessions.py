#!/usr/bin/env python3
"""Extract real user questions from local Codex session JSONL files."""

from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


SCHEMA_VERSION = 1
MY_REQUEST_MARKER = "## My request for Codex:"
SKIP_PREFIXES = (
    "# AGENTS.md instructions",
    "<environment_context>",
    "Run the daily source intelligence workflow",
)


def today_shanghai() -> str:
    return datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d")


def session_dir_for(date: str, codex_home: Path) -> Path:
    year, month, day = date.split("-")
    return codex_home / "sessions" / year / month / day


def text_from_content(content: Any) -> str:
    if not isinstance(content, list):
        return ""
    pieces: list[str] = []
    for item in content:
        if not isinstance(item, dict):
            continue
        text = item.get("text") or item.get("input_text")
        if isinstance(text, str):
            pieces.append(text)
    return "\n".join(piece for piece in pieces if piece).strip()


def strip_large_embeds(text: str) -> str:
    text = re.sub(r"<appshot\b.*?</appshot>", "", text, flags=re.DOTALL)
    text = re.sub(r"<image>.*?</image>", "", text, flags=re.DOTALL)
    return text.strip()


def clean_user_text(raw_text: str) -> str | None:
    text = raw_text.strip()
    if MY_REQUEST_MARKER in text:
        text = text.split(MY_REQUEST_MARKER, 1)[1].strip()
    text = strip_large_embeds(text)

    if not text:
        return None
    if any(text.startswith(prefix) for prefix in SKIP_PREFIXES):
        return None
    if text.startswith("<turn_aborted>"):
        return None
    if "<INSTRUCTIONS>" in text or "</INSTRUCTIONS>" in text:
        return None
    if text.startswith("# Applications mentioned by the user:"):
        return None
    if "daily-source-intelligence/runbook.md first and follow it as the source of truth" in text:
        return None

    return re.sub(r"\n{3,}", "\n\n", text).strip()


def load_session(path: Path) -> dict[str, Any]:
    session: dict[str, Any] = {
        "session_id": path.stem.replace("rollout-", ""),
        "started_at": None,
        "cwd": None,
        "source": None,
        "thread_source": None,
        "source_path": str(path),
        "user_questions": [],
        "read_errors": [],
    }

    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                session["read_errors"].append(
                    {"line": line_number, "error": f"{exc.__class__.__name__}: {exc}"}
                )
                continue

            if record.get("type") == "session_meta":
                payload = record.get("payload") or {}
                if isinstance(payload, dict):
                    session["session_id"] = payload.get("id") or session["session_id"]
                    session["started_at"] = payload.get("timestamp") or record.get("timestamp")
                    session["cwd"] = payload.get("cwd")
                    session["source"] = payload.get("source")
                    session["thread_source"] = payload.get("thread_source")
                continue

            if record.get("type") != "response_item":
                continue
            payload = record.get("payload") or {}
            if not isinstance(payload, dict):
                continue
            if payload.get("type") != "message" or payload.get("role") != "user":
                continue
            text = clean_user_text(text_from_content(payload.get("content")))
            if not text:
                continue
            session["user_questions"].append(
                {
                    "timestamp": record.get("timestamp"),
                    "text": text,
                }
            )

    return session


def extract_for_date(
    date: str,
    *,
    root: Path | str = Path.cwd(),
    codex_home: Path | str | None = None,
) -> dict[str, Any]:
    root_path = Path(root)
    codex_home_path = Path(codex_home or os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    source_dir = session_dir_for(date, codex_home_path)
    sessions = [load_session(path) for path in sorted(source_dir.glob("*.jsonl"))]
    question_count = sum(len(session["user_questions"]) for session in sessions)

    result = {
        "schema_version": SCHEMA_VERSION,
        "date": date,
        "generated_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "source_dir": str(source_dir),
        "session_count": len(sessions),
        "question_count": question_count,
        "sessions": sessions,
    }

    output_path = root_path / "reviews" / "raw" / date / "codex-sessions.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=today_shanghai())
    parser.add_argument("--root", default=Path.cwd())
    parser.add_argument("--codex-home", default=os.environ.get("CODEX_HOME") or str(Path.home() / ".codex"))
    args = parser.parse_args(argv)

    result = extract_for_date(args.date, root=Path(args.root), codex_home=Path(args.codex_home))
    print(
        json.dumps(
            {
                "date": result["date"],
                "session_count": result["session_count"],
                "question_count": result["question_count"],
                "output": f"reviews/raw/{args.date}/codex-sessions.json",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
