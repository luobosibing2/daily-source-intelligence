#!/usr/bin/env python3
import argparse
import hashlib
import html
import json
import re
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def read_json(path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def inline_markdown(value):
    parts = []
    cursor = 0
    for match in LINK_RE.finditer(value):
        parts.append(html.escape(value[cursor : match.start()]))
        parts.append(
            f'<a href="{html.escape(match.group(2), quote=True)}">{html.escape(match.group(1))}</a>'
        )
        cursor = match.end()
    parts.append(html.escape(value[cursor:]))
    return "".join(parts)


def markdown_to_html(markdown):
    output = []
    in_list = False
    for raw in markdown.splitlines():
        line = raw.rstrip()
        if line.startswith("#"):
            if in_list:
                output.append("</ul>")
                in_list = False
            level = min(6, len(line) - len(line.lstrip("#")))
            output.append(f"<h{level}>{inline_markdown(line[level:].strip())}</h{level}>")
        elif line.startswith("- "):
            if not in_list:
                output.append("<ul>")
                in_list = True
            output.append(f"<li>{inline_markdown(line[2:])}</li>")
        elif line:
            if in_list:
                output.append("</ul>")
                in_list = False
            output.append(f"<p>{inline_markdown(line)}</p>")
        elif in_list:
            output.append("</ul>")
            in_list = False
    if in_list:
        output.append("</ul>")
    return "\n".join(output)


def render_page(run_date, markdown, index_payload):
    counts = index_payload.get("signals", {}).get("counts", {})
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{run_date} Daily Source Intelligence</title>
  <style>
    body {{ font: 16px/1.7 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 0 auto; max-width: 960px; padding: 32px 20px 80px; color: #17202a; }}
    header {{ border-bottom: 1px solid #dfe6e9; margin-bottom: 28px; }}
    .meta {{ color: #636e72; }}
    a {{ color: #0969da; }}
    code {{ background: #f6f8fa; padding: 2px 4px; }}
  </style>
</head>
<body>
<header><a href="index.html">全部日报</a><p class="meta">唯一信号 {counts.get('total', 0)} · 北京时间窗口内 {counts.get('inside_window', 0)} · 时间未知边界 {counts.get('unknown_time_boundary', 0)}</p></header>
<main>{markdown_to_html(markdown)}</main>
</body>
</html>
"""


def build_bundle(run_date, root=ROOT):
    root = Path(root)
    docs = root / "docs"
    report_path = docs / f"{run_date}-daily-intel.md"
    if not report_path.is_file():
        raise FileNotFoundError(f"daily report missing: {report_path}")
    report = report_path.read_text(encoding="utf-8")
    signals_path = root / "raw" / run_date / "signals.json"
    audit_path = root / "reviews" / f"{run_date}-candidate-audit.json"
    signals = read_json(signals_path, {"counts": {}, "signals": []})
    audit = read_json(audit_path, {"counts": {}})
    payload = {
        "schema_version": 1,
        "run_date": run_date,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "report": {
            "path": f"docs/{run_date}-daily-intel.md",
            "sha256": hashlib.sha256(report.encode("utf-8")).hexdigest(),
        },
        "signals": {
            "path": f"raw/{run_date}/signals.json" if signals_path.exists() else "",
            "counts": signals.get("counts") or {},
        },
        "candidate_audit": {
            "path": f"reviews/{run_date}-candidate-audit.json" if audit_path.exists() else "",
            "counts": audit.get("counts") or {},
            "report_sha256": audit.get("daily_report_sha256") or "",
        },
        "trend_report": f"trend/reports/{run_date}-trend-report.md" if (root / "trend" / "reports" / f"{run_date}-trend-report.md").exists() else "",
    }
    index_path = docs / f"{run_date}-daily-intel.index.json"
    html_path = docs / f"{run_date}-daily-intel.html"
    write_text(index_path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    write_text(html_path, render_page(run_date, report, payload))

    dated_pages = sorted(docs.glob("????-??-??-daily-intel.html"), reverse=True)
    links = "\n".join(
        f'<li><a href="{html.escape(path.name)}">{html.escape(path.name[:10])}</a></li>'
        for path in dated_pages
    )
    site_index = f"<!doctype html><html lang=\"zh-CN\"><meta charset=\"utf-8\"><title>Daily Source Intelligence</title><body><h1>Daily Source Intelligence</h1><ul>{links}</ul></body></html>\n"
    write_text(docs / "index.html", site_index)
    return {
        "index_json": str(index_path.relative_to(root)),
        "daily_html": str(html_path.relative_to(root)),
        "site_index": "docs/index.html",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build derived JSON and static HTML views for a daily report.")
    parser.add_argument("--date", required=True)
    parser.add_argument("--root", default=str(ROOT))
    args = parser.parse_args(argv)
    try:
        result = build_bundle(args.date, root=Path(args.root))
    except (FileNotFoundError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
