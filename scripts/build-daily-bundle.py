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
INLINE_RE = re.compile(r"(`[^`]+`|\*\*[^*]+\*\*|\[([^\]]+)\]\(([^)]+)\))")
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
TABLE_SEPARATOR_RE = re.compile(r"^:?-{3,}:?$")

BASE_STYLES = """
:root {
  --ink: #17202e;
  --muted: #697382;
  --paper: #fbfaf7;
  --canvas: #f0eee8;
  --line: #d9d6ce;
  --navy: #101c2c;
  --navy-soft: #18283d;
  --accent: #d5a650;
  --accent-soft: #f5e8c9;
  --blue: #356ba6;
  --white: #ffffff;
  color-scheme: light;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--canvas);
  color: var(--ink);
  font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI",
    "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  font-size: 16px;
  line-height: 1.75;
  -webkit-font-smoothing: antialiased;
}
a { color: var(--blue); text-decoration-thickness: 1px; text-underline-offset: 0.2em; }
a:hover { color: #1e4f83; }
a:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 2px;
}
.skip-link {
  position: fixed;
  z-index: 100;
  top: 12px;
  left: 12px;
  padding: 10px 14px;
  background: var(--white);
  color: var(--navy);
  font-weight: 700;
  transform: translateY(-180%);
}
.skip-link:focus { transform: translateY(0); }
.shell { width: min(1160px, calc(100% - 40px)); margin: 0 auto; }
.site-header {
  background: var(--navy);
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  color: var(--white);
}
.site-header .shell {
  min-height: 68px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}
.brand {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  color: var(--white);
  font-size: 0.78rem;
  font-weight: 760;
  letter-spacing: 0.14em;
  text-decoration: none;
  text-transform: uppercase;
}
.brand-mark {
  width: 31px;
  height: 31px;
  display: grid;
  place-items: center;
  border: 1px solid rgba(255, 255, 255, 0.5);
  color: var(--accent);
  font: 700 0.72rem/1 ui-monospace, SFMono-Regular, Menlo, monospace;
}
.header-note {
  color: #aeb8c5;
  font-size: 0.78rem;
  letter-spacing: 0.04em;
}
.eyebrow {
  margin: 0 0 18px;
  color: var(--accent);
  font: 700 0.72rem/1.3 ui-monospace, SFMono-Regular, Menlo, monospace;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}
.button {
  min-height: 48px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 0 20px;
  border: 1px solid currentColor;
  font-weight: 700;
  text-decoration: none;
}
.button-primary { background: var(--accent); border-color: var(--accent); color: var(--navy); }
.button-primary:hover { background: #e1b766; color: var(--navy); }
.button-quiet { color: #dbe2eb; }
.button-quiet:hover { background: rgba(255, 255, 255, 0.08); color: var(--white); }
.site-footer {
  background: var(--navy);
  color: #9ca8b7;
  padding: 32px 0;
  font-size: 0.82rem;
}
.site-footer .shell { display: flex; justify-content: space-between; gap: 24px; }
.site-footer a { color: #dce3eb; }
.local-evidence {
  display: inline;
  color: #5f6874;
  text-decoration: underline dotted;
  text-underline-offset: 0.2em;
}
.local-evidence small {
  display: inline-block;
  margin-left: 0.32em;
  padding: 0.08em 0.38em;
  border: 1px solid #c9c4b9;
  border-radius: 999px;
  color: #73684f;
  font-size: 0.68em;
  line-height: 1.45;
  text-decoration: none;
  vertical-align: 0.08em;
}
@media (max-width: 680px) {
  .shell { width: min(100% - 28px, 1160px); }
  .header-note { display: none; }
  .site-footer .shell { display: block; }
}
"""

REPORT_STYLES = """
.report-hero {
  background: var(--navy);
  color: var(--white);
  padding: 72px 0 78px;
}
.report-hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(360px, 0.72fr);
  gap: 80px;
  align-items: end;
}
.report-hero h1 {
  max-width: 720px;
  margin: 0;
  font-family: Georgia, "Noto Serif SC", "Songti SC", serif;
  font-size: clamp(3rem, 7vw, 6.4rem);
  font-weight: 500;
  letter-spacing: -0.055em;
  line-height: 0.92;
}
.report-hero h1 span { display: block; color: #cfd8e4; }
.report-deck {
  max-width: 620px;
  margin: 26px 0 0;
  color: #b9c4d1;
  font-size: 1rem;
}
.metrics-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.metric { min-height: 122px; padding: 22px; border-right: 1px solid rgba(255, 255, 255, 0.14); }
.metric:last-child { border-right: 0; }
.metric strong {
  display: block;
  color: var(--white);
  font: 500 clamp(1.7rem, 4vw, 2.6rem)/1 Georgia, "Noto Serif SC", serif;
}
.metric span {
  display: block;
  margin-top: 12px;
  color: #9eabba;
  font-size: 0.72rem;
  line-height: 1.45;
  letter-spacing: 0.08em;
}
.report-layout {
  width: min(1160px, calc(100% - 40px));
  margin: 0 auto;
  display: grid;
  grid-template-columns: 176px minmax(0, 1fr);
  gap: 70px;
  padding: 64px 0 100px;
}
.report-rail { align-self: start; position: sticky; top: 28px; }
.rail-date {
  display: block;
  padding-top: 15px;
  border-top: 3px solid var(--accent);
  font: 700 0.76rem/1.5 ui-monospace, SFMono-Regular, Menlo, monospace;
  letter-spacing: 0.08em;
}
.rail-note { margin: 14px 0 26px; color: var(--muted); font-size: 0.78rem; }
.rail-link { font-size: 0.82rem; font-weight: 700; }
.rail-toc { margin: 28px 0; padding: 20px 0; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }
.rail-toc strong {
  display: block;
  margin-bottom: 10px;
  color: #7b705c;
  font: 700 0.68rem/1.4 ui-monospace, SFMono-Regular, Menlo, monospace;
  letter-spacing: 0.1em;
}
.rail-toc a {
  display: block;
  padding: 5px 0;
  color: #5d6875;
  font-size: 0.74rem;
  line-height: 1.45;
  text-decoration: none;
}
.rail-toc a:hover { color: var(--blue); }
.report-content {
  min-width: 0;
  padding: 8px 0 0;
  font-size: 1rem;
}
.report-content > h2 {
  margin: 72px 0 28px;
  padding-top: 24px;
  border-top: 1px solid var(--line);
  font-family: Georgia, "Noto Serif SC", "Songti SC", serif;
  font-size: clamp(1.8rem, 3vw, 2.5rem);
  font-weight: 600;
  letter-spacing: -0.03em;
  line-height: 1.25;
}
.report-content > h2:first-child { margin-top: 0; }
.report-content h3 {
  margin: 46px 0 17px;
  color: #24354a;
  font-size: 1.18rem;
  line-height: 1.4;
}
.report-content p { margin: 0 0 20px; }
.report-content ul, .report-content ol { margin: 0 0 26px; padding-left: 1.3em; }
.report-content li { margin: 0 0 12px; padding-left: 0.28em; }
.report-content li::marker { color: #b8852e; }
.report-content code {
  padding: 0.12em 0.38em;
  border: 1px solid #e0ddd5;
  border-radius: 3px;
  background: #f5f2eb;
  color: #28486b;
  font: 0.88em/1.5 ui-monospace, SFMono-Regular, Menlo, monospace;
}
.report-content pre {
  overflow-x: auto;
  margin: 28px 0;
  padding: 22px;
  border-left: 3px solid var(--accent);
  background: var(--navy);
  color: #e7edf4;
}
.report-content pre code { padding: 0; border: 0; background: transparent; color: inherit; }
.report-content blockquote {
  margin: 28px 0;
  padding: 4px 0 4px 22px;
  border-left: 3px solid var(--accent);
  color: #4e5b69;
}
.table-wrap {
  overflow-x: auto;
  margin: 30px 0 42px;
  border: 1px solid var(--line);
  background: var(--paper);
  box-shadow: 0 14px 34px rgba(28, 37, 48, 0.06);
}
table { width: 100%; border-collapse: collapse; min-width: 820px; }
th, td { padding: 16px 17px; border-bottom: 1px solid #e3e0d9; text-align: left; vertical-align: top; }
th {
  background: #e9e6de;
  color: #4f5964;
  font-size: 0.7rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
td { font-size: 0.9rem; line-height: 1.62; }
tbody tr:last-child td { border-bottom: 0; }
tbody tr:hover { background: #f8f5ee; }
td:first-child { color: #8b631e; font-weight: 750; white-space: nowrap; }
@media (max-width: 900px) {
  .report-hero { padding: 54px 0 60px; }
  .report-hero-grid { grid-template-columns: 1fr; gap: 44px; }
  .report-layout { grid-template-columns: 1fr; gap: 36px; }
  .report-rail { position: static; display: grid; grid-template-columns: 1fr 1fr; gap: 18px 36px; align-items: end; }
  .rail-toc { grid-column: 1 / -1; margin: 4px 0; }
  .rail-toc a { display: inline-block; margin-right: 16px; }
  .rail-note { margin-bottom: 0; }
}
@media (max-width: 680px) {
  .report-hero h1 { font-size: clamp(3rem, 16vw, 4.6rem); }
  .metrics-grid { grid-template-columns: 1fr; }
  .metric { min-height: auto; border-right: 0; border-bottom: 1px solid rgba(255, 255, 255, 0.14); }
  .metric:last-child { border-bottom: 0; }
  .report-layout { width: min(100% - 28px, 1160px); padding-top: 42px; }
  .report-rail { display: block; }
  .report-content { font-size: 0.96rem; }
}
@media print {
  .site-header, .report-rail, .site-footer { display: none; }
  body { background: #fff; }
  .report-hero { padding: 24px 0; background: #fff; color: #000; }
  .report-hero h1, .report-hero h1 span { color: #000; }
  .report-deck, .eyebrow { color: #444; }
  .metrics-grid { border-color: #aaa; }
  .metric, .metric strong, .metric span { color: #000; border-color: #aaa; }
  .report-layout { display: block; width: 100%; padding: 24px 0; }
}
"""

INDEX_STYLES = """
.landing-hero { background: var(--navy); color: var(--white); padding: 88px 0 96px; }
.landing-hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.35fr) minmax(300px, 0.65fr);
  gap: 90px;
  align-items: end;
}
.landing-hero h1 {
  margin: 0;
  max-width: 820px;
  font-family: Georgia, "Noto Serif SC", "Songti SC", serif;
  font-size: clamp(3.4rem, 7.5vw, 7rem);
  font-weight: 500;
  letter-spacing: -0.065em;
  line-height: 0.94;
}
.landing-hero h1 span { color: #cbd5e1; }
.landing-deck { max-width: 680px; margin: 30px 0 0; color: #b9c4d1; font-size: 1.02rem; }
.hero-actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 34px; }
.edition-panel { border-top: 3px solid var(--accent); padding-top: 22px; }
.edition-panel strong {
  display: block;
  font: 500 clamp(2.5rem, 5vw, 4.6rem)/1 Georgia, "Noto Serif SC", serif;
  letter-spacing: -0.04em;
}
.edition-panel span { display: block; margin-top: 12px; color: #9fabb9; font-size: 0.78rem; letter-spacing: 0.08em; }
.archive { padding: 78px 0 96px; }
.archive-head { display: flex; justify-content: space-between; gap: 28px; align-items: end; margin-bottom: 34px; }
.archive h2 {
  margin: 0;
  font-family: Georgia, "Noto Serif SC", "Songti SC", serif;
  font-size: clamp(2.2rem, 5vw, 4rem);
  font-weight: 600;
  letter-spacing: -0.04em;
  line-height: 1;
}
.archive-summary { max-width: 460px; margin: 0; color: var(--muted); font-size: 0.9rem; }
.report-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1px;
  margin: 0;
  padding: 1px;
  background: var(--line);
  list-style: none;
}
.report-card { min-height: 235px; background: var(--paper); }
.report-card a {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 26px;
  color: var(--ink);
  text-decoration: none;
  transition: background 150ms ease, color 150ms ease;
}
.report-card a:hover { background: var(--navy-soft); color: var(--white); }
.report-card-latest a { background: var(--accent-soft); }
.card-kicker {
  display: flex;
  justify-content: space-between;
  gap: 18px;
  color: #737c87;
  font: 700 0.68rem/1.4 ui-monospace, SFMono-Regular, Menlo, monospace;
  letter-spacing: 0.1em;
}
.report-card a:hover .card-kicker { color: #aeb8c5; }
.card-date {
  display: block;
  font-family: Georgia, "Noto Serif SC", serif;
  font-size: clamp(2.4rem, 4vw, 3.8rem);
  line-height: 0.95;
  letter-spacing: -0.05em;
}
.card-date small { display: block; margin-top: 12px; font: 500 0.82rem/1.3 ui-sans-serif, sans-serif; letter-spacing: 0.02em; }
.card-arrow { align-self: flex-end; font-size: 1.4rem; }
@media (max-width: 900px) {
  .landing-hero-grid { grid-template-columns: 1fr; gap: 54px; }
  .report-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 680px) {
  .landing-hero { padding: 58px 0 64px; }
  .landing-hero h1 { font-size: clamp(3.1rem, 16vw, 5rem); }
  .archive-head { display: block; }
  .archive-summary { margin-top: 18px; }
  .report-grid { grid-template-columns: 1fr; }
  .report-card { min-height: 190px; }
}
"""


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
    for match in INLINE_RE.finditer(value):
        parts.append(html.escape(value[cursor : match.start()]))
        token = match.group(0)
        if token.startswith("`"):
            parts.append(f"<code>{html.escape(token[1:-1])}</code>")
        elif token.startswith("**"):
            parts.append(f"<strong>{html.escape(token[2:-2])}</strong>")
        else:
            target = match.group(3)
            if target.startswith(("../raw/", "../state/", "../reviews/", "../trend/")):
                parts.append(
                    f'<span class="local-evidence" title="本地证据归档未随公开站点发布">'
                    f"{html.escape(match.group(2))}<small>本地证据</small></span>"
                )
                cursor = match.end()
                continue
            if target.startswith(("../config/", "../scripts/")):
                target = (
                    "https://github.com/luobosibing2/daily-source-intelligence/blob/develop/"
                    + target[3:]
                )
            external = target.startswith(("https://", "http://"))
            attributes = ' target="_blank" rel="noopener noreferrer"' if external else ""
            parts.append(
                f'<a href="{html.escape(target, quote=True)}"{attributes}>'
                f"{html.escape(match.group(2))}</a>"
            )
        cursor = match.end()
    parts.append(html.escape(value[cursor:]))
    return "".join(parts)


def split_table_row(line):
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_table_separator(line):
    cells = split_table_row(line)
    return bool(cells) and all(TABLE_SEPARATOR_RE.fullmatch(cell) for cell in cells)


def heading_entries(markdown):
    entries = []
    seen = {}
    for line in COMMENT_RE.sub("", markdown).splitlines():
        heading = re.match(r"^(#{2,3})\s+(.+)$", line.rstrip())
        if not heading:
            continue
        plain = re.sub(r"[`*_]", "", heading.group(2)).strip()
        base = re.sub(r"[^\w\u4e00-\u9fff]+", "-", plain.lower()).strip("-") or "section"
        seen[base] = seen.get(base, 0) + 1
        slug = base if seen[base] == 1 else f"{base}-{seen[base]}"
        entries.append((len(heading.group(1)), plain, slug))
    return entries


def markdown_to_html(markdown, headings=None):
    output = []
    list_tag = None
    lines = COMMENT_RE.sub("", markdown).splitlines()
    heading_ids = iter(slug for _, _, slug in (headings or []))

    def close_list():
        nonlocal list_tag
        if list_tag:
            output.append(f"</{list_tag}>")
            list_tag = None

    index = 0
    while index < len(lines):
        raw = lines[index]
        line = raw.rstrip()
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        unordered = re.match(r"^[-*]\s+(.+)$", line)
        ordered = re.match(r"^\d+\.\s+(.+)$", line)

        if line.startswith("```"):
            close_list()
            language = line[3:].strip()
            code_lines = []
            index += 1
            while index < len(lines) and not lines[index].rstrip().startswith("```"):
                code_lines.append(lines[index])
                index += 1
            language_attr = f' data-language="{html.escape(language, quote=True)}"' if language else ""
            output.append(
                f"<pre><code{language_attr}>{html.escape(chr(10).join(code_lines))}</code></pre>"
            )
        elif (
            line.strip().startswith("|")
            and index + 1 < len(lines)
            and is_table_separator(lines[index + 1])
        ):
            close_list()
            headers = split_table_row(line)
            index += 2
            rows = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                rows.append(split_table_row(lines[index]))
                index += 1
            head = "".join(f"<th>{inline_markdown(cell)}</th>" for cell in headers)
            body = "\n".join(
                "<tr>"
                + "".join(
                    f"<td>{inline_markdown(row[position]) if position < len(row) else ''}</td>"
                    for position in range(len(headers))
                )
                + "</tr>"
                for row in rows
            )
            output.append(
                '<div class="table-wrap" role="region" aria-label="数据表" tabindex="0">'
                f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>"
            )
            continue
        elif heading:
            close_list()
            level = len(heading.group(1))
            identifier = next(heading_ids, "")
            id_attribute = f' id="{html.escape(identifier, quote=True)}"' if identifier else ""
            output.append(
                f"<h{level}{id_attribute}>{inline_markdown(heading.group(2))}</h{level}>"
            )
        elif unordered or ordered:
            tag = "ul" if unordered else "ol"
            if list_tag != tag:
                close_list()
                output.append(f"<{tag}>")
                list_tag = tag
            output.append(f"<li>{inline_markdown((unordered or ordered).group(1))}</li>")
        elif line.startswith("> "):
            close_list()
            output.append(f"<blockquote>{inline_markdown(line[2:])}</blockquote>")
        elif line:
            close_list()
            output.append(f"<p>{inline_markdown(line)}</p>")
        else:
            close_list()
        index += 1
    close_list()
    return "\n".join(output)


def render_page(run_date, markdown, index_payload):
    counts = index_payload.get("signals", {}).get("counts", {})
    report_lines = markdown.splitlines()
    if report_lines and report_lines[0].startswith("# "):
        report_lines = report_lines[1:]
    report_markdown = "\n".join(report_lines)
    headings = heading_entries(report_markdown)
    report_body = markdown_to_html(report_markdown, headings=headings)
    toc = "".join(
        f'<a href="#{html.escape(slug, quote=True)}">{html.escape(title)}</a>'
        for level, title, slug in headings
        if level == 2
    )
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{run_date} Daily Source Intelligence 中文日报">
  <meta name="theme-color" content="#101c2c">
  <title>{run_date} Daily Source Intelligence</title>
  <style>{BASE_STYLES}{REPORT_STYLES}</style>
</head>
<body>
  <a class="skip-link" href="#content">跳到日报正文</a>
  <header class="site-header">
    <div class="shell">
      <a class="brand" href="index.html"><span class="brand-mark">DSI</span>Daily Source Intelligence</a>
      <span class="header-note">公开信号 · 来源证据 · 中文简报</span>
    </div>
  </header>
  <section class="report-hero">
    <div class="shell report-hero-grid">
      <div>
        <p class="eyebrow">Daily briefing / {run_date}</p>
        <h1>Daily Source <span>Intelligence</span></h1>
        <p class="report-deck">围绕预设主题整理公开信号，保留证据边界，并转化为结构化中文日报。</p>
      </div>
      <div class="metrics-grid" aria-label="本期信号统计">
        <div class="metric"><strong>{counts.get('total', 0)}</strong><span>唯一信号<br>UNIQUE SIGNALS</span></div>
        <div class="metric"><strong>{counts.get('inside_window', 0)}</strong><span>北京时间窗口内<br>IN WINDOW</span></div>
        <div class="metric"><strong>{counts.get('unknown_time_boundary', 0)}</strong><span>时间未知边界<br>TIME UNKNOWN</span></div>
      </div>
    </div>
  </section>
  <main class="report-layout" id="content">
    <aside class="report-rail">
      <div>
        <span class="rail-date">{run_date}</span>
        <p class="rail-note">Asia / Shanghai<br>Evidence-backed</p>
      </div>
      <nav class="rail-toc" aria-label="日报目录"><strong>CONTENTS</strong>{toc}</nav>
      <a class="rail-link" href="index.html">← 返回日报归档</a>
    </aside>
    <article class="report-content">{report_body}</article>
  </main>
  <footer class="site-footer">
    <div class="shell">
      <span>Daily Source Intelligence · Evidence before interpretation.</span>
      <a href="https://github.com/luobosibing2/daily-source-intelligence">GitHub repository ↗</a>
    </div>
  </footer>
</body>
</html>
"""


def render_site_index(dated_pages):
    latest = dated_pages[0] if dated_pages else None
    cards = []
    weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    for position, path in enumerate(dated_pages):
        report_date = datetime.strptime(path.name[:10], "%Y-%m-%d")
        label = "Latest briefing" if position == 0 else "Daily briefing"
        cards.append(
            f'<li class="report-card{" report-card-latest" if position == 0 else ""}">'
            f'<a href="{html.escape(path.name, quote=True)}">'
            f'<span class="card-kicker"><span>{label}</span><span>{report_date.year}</span></span>'
            f'<span class="card-date">{report_date:%m / %d}'
            f"<small>{weekdays[report_date.weekday()]} · 中文情报日报</small></span>"
            '<span class="card-arrow" aria-hidden="true">↗</span></a></li>'
        )
    latest_date = latest.name[:10] if latest else "尚未发布"
    latest_link = latest.name if latest else "#archive"
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Daily Source Intelligence 中文公开信息情报日报">
  <meta name="theme-color" content="#101c2c">
  <title>Daily Source Intelligence</title>
  <style>{BASE_STYLES}{INDEX_STYLES}</style>
</head>
<body>
  <a class="skip-link" href="#content">跳到日报归档</a>
  <header class="site-header">
    <div class="shell">
      <a class="brand" href="index.html"><span class="brand-mark">DSI</span>Daily Source Intelligence</a>
      <span class="header-note">公开信号 · 来源证据 · 中文简报</span>
    </div>
  </header>
  <main id="content">
    <section class="landing-hero">
      <div class="shell landing-hero-grid">
        <div>
          <p class="eyebrow">Open-source intelligence / China edition</p>
          <h1>把公开信号，变成<br><span>可追溯的中文情报。</span></h1>
          <p class="landing-deck">收集官方博客、RSS、GitHub Releases、GitHub Trending 与公开 X/Twitter 信号，保留来源证据、生成阅读清单，并输出结构化日报。</p>
          <div class="hero-actions">
            <a class="button button-primary" href="{html.escape(latest_link, quote=True)}">阅读最新日报 <span aria-hidden="true">→</span></a>
            <a class="button button-quiet" href="https://github.com/luobosibing2/daily-source-intelligence">查看 GitHub <span aria-hidden="true">↗</span></a>
            <a class="button button-quiet" href="https://github.com/luobosibing2/daily-source-intelligence/blob/main/runbook.md">运行手册 <span aria-hidden="true">↗</span></a>
          </div>
        </div>
        <div class="edition-panel">
          <p class="eyebrow">Current edition</p>
          <strong>{latest_date}</strong>
          <span>BEIJING TIME · {len(dated_pages):02d} EDITIONS ARCHIVED</span>
        </div>
      </div>
    </section>
    <section class="archive" id="archive">
      <div class="shell">
        <div class="archive-head">
          <div><p class="eyebrow">Archive / 日报归档</p><h2>每一期，都能回到证据。</h2></div>
          <p class="archive-summary">按日期浏览已发布的中文情报简报。最新一期置顶，历史日报保留原始发布日期与完整内容。</p>
        </div>
        <ol class="report-grid">{"".join(cards)}</ol>
      </div>
    </section>
  </main>
  <footer class="site-footer">
    <div class="shell">
      <span>Daily Source Intelligence · Evidence before interpretation.</span>
      <a href="https://github.com/luobosibing2/daily-source-intelligence">GitHub repository ↗</a>
    </div>
  </footer>
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
    write_text(docs / "index.html", render_site_index(dated_pages))
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
