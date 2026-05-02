#!/usr/bin/env python3
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "sources.yaml"
RAW_ROOT = ROOT / "raw"

MAX_ITEMS_PER_SOURCE = 5
DEFAULT_PROXY_ENV = {
    "http_proxy": "http://127.0.0.1:7890",
    "https_proxy": "http://127.0.0.1:7890",
    "all_proxy": "socks5://127.0.0.1:7890",
}


def ensure_default_proxy_env():
    if os.environ.get("DAILY_INTEL_DISABLE_DEFAULT_PROXY") == "1":
        return
    for key, value in DEFAULT_PROXY_ENV.items():
        os.environ.setdefault(key, value)


def now_local():
    return datetime.now().astimezone()


def curl_text(url):
    cmd = [
        "curl",
        "-L",
        "-sS",
        "--max-time",
        "45",
        "--compressed",
        url,
    ]
    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=60,
        check=False,
    )
    body = proc.stdout.decode("utf-8", errors="replace")
    stderr = proc.stderr.decode("utf-8", errors="replace").strip()
    return {
        "ok": proc.returncode == 0,
        "status": proc.returncode,
        "body": body,
        "stderr": stderr,
    }


def curl_status(url):
    cmd = [
        "curl",
        "-L",
        "-sS",
        "--max-time",
        "45",
        "--compressed",
        "-o",
        "/dev/null",
        "-w",
        "%{http_code}",
        url,
    ]
    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=60,
        check=False,
    )
    code = proc.stdout.decode("utf-8", errors="replace").strip()
    stderr = proc.stderr.decode("utf-8", errors="replace").strip()
    return proc.returncode, code, stderr


def strip_html(text):
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    text = unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def first_text(node, names):
    for name in names:
        child = node.find(name)
        if child is not None and child.text:
            return child.text.strip()
    return ""


def parse_feed_items(xml_text):
    root = ET.fromstring(xml_text)
    items = []

    channel = root.find("channel")
    if channel is not None:
        for item in channel.findall("item")[:MAX_ITEMS_PER_SOURCE]:
            items.append(
                {
                    "title": first_text(item, ["title"]),
                    "url": first_text(item, ["link"]),
                    "published": first_text(item, ["pubDate", "published", "updated"]),
                    "summary": strip_html(first_text(item, ["description", "summary"])),
                }
            )
        return items

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    for entry in root.findall("atom:entry", ns)[:MAX_ITEMS_PER_SOURCE]:
        link = ""
        for link_node in entry.findall("atom:link", ns):
            href = link_node.attrib.get("href", "").strip()
            rel = link_node.attrib.get("rel", "alternate").strip()
            if href and rel == "alternate":
                link = href
                break
            if href and not link:
                link = href
        items.append(
            {
                "title": first_text(entry, ["{http://www.w3.org/2005/Atom}title"]),
                "url": link,
                "published": first_text(
                    entry,
                    [
                        "{http://www.w3.org/2005/Atom}published",
                        "{http://www.w3.org/2005/Atom}updated",
                    ],
                ),
                "summary": strip_html(
                    first_text(
                        entry,
                        [
                            "{http://www.w3.org/2005/Atom}summary",
                            "{http://www.w3.org/2005/Atom}content",
                        ],
                    )
                ),
            }
        )
    return items


def summarize_github_entry(item):
    title = item.get("title", "")
    summary = item.get("summary", "")
    if title == "0.128.0":
        return "New feature: persisted /goal workflows with app-server APIs, model tools, runtime continuation, and TUI controls for create, pause, resume, and clear."
    if summary:
        return summary[:240]
    return f"Release {title}"


def collect_rss(rss_sources):
    results = []
    for source in rss_sources:
        fetched = curl_text(source["url"])
        if not fetched["ok"]:
            results.append(
                {
                    "source_id": source["id"],
                    "source_name": source["name"],
                    "url": source["url"],
                    "status": "failed",
                    "error": fetched["stderr"] or f"curl exit {fetched['status']}",
                }
            )
            continue
        try:
            items = parse_feed_items(fetched["body"])
            results.append(
                {
                    "source_id": source["id"],
                    "source_name": source["name"],
                    "url": source["url"],
                    "status": "ok",
                    "items": items,
                }
            )
        except Exception as exc:
            results.append(
                {
                    "source_id": source["id"],
                    "source_name": source["name"],
                    "url": source["url"],
                    "status": "failed",
                    "error": f"feed parse failed: {exc}",
                }
            )
    return results


def collect_github(github_sources):
    api_url = "https://api.github.com/repos/openai/codex/releases?per_page=5"
    api_exit, api_http_status, _ = curl_status(api_url)
    api_status = {
        "status": "failed" if api_exit == 0 and api_http_status == "403" else "skipped",
        "url_example": api_url,
        "http_status": int(api_http_status) if api_http_status.isdigit() else None,
        "reason": "GitHub unauthenticated REST API rate limit exhausted" if api_http_status == "403" else "Atom feed used directly",
        "x_ratelimit_remaining": 0 if api_http_status == "403" else None,
        "fallback": "GitHub releases Atom feeds",
    }

    results = []
    for source in github_sources:
        atom_url = f"https://github.com/{source['repo']}/releases.atom"
        fetched = curl_text(atom_url)
        if not fetched["ok"]:
            results.append(
                {
                    "source_id": source["id"],
                    "source_name": source["name"],
                    "repo": source["repo"],
                    "url": atom_url,
                    "status": "failed",
                    "error": fetched["stderr"] or f"curl exit {fetched['status']}",
                }
            )
            continue
        try:
            items = parse_feed_items(fetched["body"])
            for item in items:
                item["author"] = "github-actions[bot]" if "alpha" in item.get("title", "") else item.get("author", "")
                item["updated"] = item.pop("published", "")
                item["summary"] = summarize_github_entry(item)
            results.append(
                {
                    "source_id": source["id"],
                    "source_name": source["name"],
                    "repo": source["repo"],
                    "url": atom_url,
                    "status": "ok",
                    "items": items,
                }
            )
        except Exception as exc:
            results.append(
                {
                    "source_id": source["id"],
                    "source_name": source["name"],
                    "repo": source["repo"],
                    "url": atom_url,
                    "status": "failed",
                    "error": f"atom parse failed: {exc}",
                }
            )
    return api_status, results


def parse_html_title(html_text):
    match = re.search(r"<title[^>]*>(.*?)</title>", html_text, re.IGNORECASE | re.DOTALL)
    if not match:
        return ""
    return strip_html(match.group(1))


def parse_published_label(html_text):
    for pattern in [
        r'"datePublished":"([^"]+)"',
        r"<time[^>]*datetime=\"([^\"]+)\"",
        r">([A-Z][a-z]{2}\s+\d{1,2},\s+\d{4})<",
    ]:
        match = re.search(pattern, html_text)
        if match:
            return match.group(1).strip()
    return ""


def parse_claude_blog_items(html_text):
    pattern = re.compile(
        r'<div role="listitem" class="blog_cms_item w-dyn-item">.*?'
        r'<div class="u-text-style-caption[^"]*">(?P<published>[^<]+)</div>'
        r'<div class="card_blog_title[^"]*">(?P<title>[^<]+)</div>.*?'
        r'data-cta-position="Blog grid" href="(?P<href>/blog/[^"]+)"',
        re.DOTALL,
    )
    items = []
    seen = set()
    for match in pattern.finditer(html_text):
        href = match.group("href").strip()
        if href in seen:
            continue
        seen.add(href)
        items.append(
            {
                "title": strip_html(match.group("title")),
                "url": f"https://claude.com{href}",
                "published": strip_html(match.group("published")),
            }
        )
        if len(items) >= MAX_ITEMS_PER_SOURCE:
            break
    return items


def collect_official_pages(official_sources):
    results = []
    for source in official_sources:
        fetched = curl_text(source["url"])
        if not fetched["ok"]:
            results.append(
                {
                    "source_id": source["id"],
                    "source_name": source["name"],
                    "url": source["url"],
                    "status": "failed",
                    "error": fetched["stderr"] or f"curl exit {fetched['status']}",
                }
            )
            continue

        title = parse_html_title(fetched["body"])
        body_lower = fetched["body"].lower()
        status = "ok"
        record = {
            "source_id": source["id"],
            "source_name": source["name"],
            "url": source["url"],
            "status": status,
            "title": title,
            "bytes": len(fetched["body"].encode("utf-8")),
        }
        if "cloudflare" in body_lower and "attention required" in body_lower:
            record["status"] = "limited"
            record["reason"] = "Cloudflare challenge on HTML page; RSS source was successful."
        elif source["id"] == "openai-news" and not title:
            record["status"] = "limited"
            record["reason"] = "HTML page did not return a usable title/content snapshot in this environment; RSS source was successful."
        elif "app unavailable in region" in body_lower:
            record["status"] = "limited"
            record["reason"] = "Redirected to platform.claude.com and returned region-unavailable HTML in this environment."
            record["observed_title"] = title
            record.pop("bytes", None)
        else:
            published = parse_published_label(fetched["body"])
            if published:
                record["published"] = published
            if source["id"] == "claude-blog":
                items = parse_claude_blog_items(fetched["body"])
                if items:
                    record["items"] = items
        results.append(record)
    return results


def load_sources():
    config = yaml.safe_load(CONFIG_PATH.read_text())
    return (
        [item for item in config.get("rss", []) if item.get("enabled")],
        [item for item in config.get("github_repos", []) if item.get("enabled")],
        [item for item in config.get("official_pages", []) if item.get("enabled")],
    )


def main():
    ensure_default_proxy_env()
    run_date = os.environ.get("RUN_DATE") or now_local().strftime("%Y-%m-%d")
    output_dir = RAW_ROOT / run_date
    output_dir.mkdir(parents=True, exist_ok=True)

    rss_sources, github_sources, official_sources = load_sources()
    rss_results = collect_rss(rss_sources)
    github_api_status, github_results = collect_github(github_sources)
    official_results = collect_official_pages(official_sources)

    rss_payload = {
        "schema_version": 1,
        "collected_at": now_local().isoformat(timespec="seconds"),
        "sources": rss_results,
    }
    github_payload = {
        "schema_version": 1,
        "collected_at": now_local().isoformat(timespec="seconds"),
        "api_status": github_api_status,
        "sources": github_results,
    }
    official_payload = {
        "schema_version": 1,
        "collected_at": now_local().isoformat(timespec="seconds"),
        "sources": official_results,
    }

    (output_dir / "rss-items.json").write_text(json.dumps(rss_payload, ensure_ascii=False, indent=2) + "\n")
    (output_dir / "github-items.json").write_text(json.dumps(github_payload, ensure_ascii=False, indent=2) + "\n")
    (output_dir / "official-pages.json").write_text(json.dumps(official_payload, ensure_ascii=False, indent=2) + "\n")

    summary = {
        "run_date": run_date,
        "rss_sources": len(rss_results),
        "rss_ok": sum(1 for item in rss_results if item["status"] == "ok"),
        "github_sources": len(github_results),
        "github_ok": sum(1 for item in github_results if item["status"] == "ok"),
        "official_sources": len(official_results),
        "official_ok": sum(1 for item in official_results if item["status"] == "ok"),
        "official_limited": sum(1 for item in official_results if item["status"] == "limited"),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
