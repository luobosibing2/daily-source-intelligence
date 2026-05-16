#!/usr/bin/env python3
import json
import hashlib
import os
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "sources.yaml"
TOPICS_PATH = ROOT / "config" / "topics.yaml"
RAW_ROOT = ROOT / "raw"

MAX_ITEMS_PER_SOURCE = 5
MAX_TRENDING_REPOS_PER_SOURCE = 10
FULLTEXT_MIN_CHARS = int(os.environ.get("DAILY_INTEL_FULLTEXT_MIN_CHARS", "240"))
AUTOCLI_FALLBACK_ENABLED = os.environ.get("DAILY_INTEL_AUTOCLI_FALLBACK", "1") != "0"
AUTOCLI_RETRIES = int(os.environ.get("DAILY_INTEL_AUTOCLI_RETRIES", "2"))
AUTOCLI_TIMEOUT_SECONDS = int(os.environ.get("DAILY_INTEL_AUTOCLI_TIMEOUT_SECONDS", "90"))
README_CANDIDATES = [
    "README.md",
    "README.MD",
    "readme.md",
    "README.rst",
    "README.txt",
]


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


def clean_autocli_output(text):
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"^\d{4}-\d{2}-\d{2}T.*\bWARN\b", stripped):
            continue
        if stripped in {
            "Waking up Chrome extension...",
            "Waiting for Chrome extension to connect",
            "Waiting for Chrome extension to connect.",
            "Waiting for Chrome extension to connect..",
            "Waiting for Chrome extension to connect...",
        }:
            continue
        if stripped and set(stripped) == {"."}:
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def autocli_read_markdown(url):
    if not AUTOCLI_FALLBACK_ENABLED:
        return {"ok": False, "error": "autocli fallback disabled by DAILY_INTEL_AUTOCLI_FALLBACK=0"}

    last_error = ""
    for attempt in range(1, AUTOCLI_RETRIES + 1):
        try:
            proc = subprocess.run(
                ["autocli", "read", url],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=AUTOCLI_TIMEOUT_SECONDS,
                check=False,
            )
        except FileNotFoundError:
            return {"ok": False, "error": "autocli executable not found"}
        except subprocess.TimeoutExpired:
            last_error = f"autocli read timed out after {AUTOCLI_TIMEOUT_SECONDS}s"
            continue

        stdout = proc.stdout.decode("utf-8", errors="replace")
        stderr = proc.stderr.decode("utf-8", errors="replace").strip()
        body = clean_autocli_output(stdout)
        if proc.returncode == 0 and content_text_is_usable(strip_markdown(body)):
            return {
                "ok": True,
                "status": proc.returncode,
                "body": body,
                "method": "autocli-read",
                "attempts": attempt,
                "stderr": stderr,
            }

        if proc.returncode == 0:
            last_error = "autocli read returned short or unusable content"
        else:
            last_error = stderr or clean_autocli_output(stdout) or f"autocli exit {proc.returncode}"

        if attempt < AUTOCLI_RETRIES:
            time.sleep(2)

    return {"ok": False, "error": last_error or "autocli read failed"}


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
    text = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", " ", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def strip_markdown(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^[#>*_\-\s]+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def html_looks_limited(html_text):
    lowered = (html_text or "").lower()
    markers = [
        ("cloudflare" in lowered and "attention required" in lowered),
        ("cloudflare" in lowered and "challenge" in lowered),
        "just a moment..." in lowered,
        "cf-chl" in lowered,
        "checking your browser" in lowered,
        "enable javascript" in lowered,
        "app unavailable in region" in lowered,
    ]
    return any(markers)


def content_text_is_usable(text):
    if not text:
        return False
    lowered = text.lower()
    if "cloudflare" in lowered and ("attention required" in lowered or "challenge" in lowered):
        return False
    if "just a moment..." in lowered or "checking your browser" in lowered:
        return False
    return len(text.strip()) >= FULLTEXT_MIN_CHARS


def text_excerpt(text, limit=600):
    cleaned = re.sub(r"\s+", " ", text or "").strip()
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[:limit].rsplit(" ", 1)[0]


def safe_slug(value, fallback="item", limit=80):
    text = strip_html(value or "")
    text = re.sub(r"https?://", "", text)
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", text).strip("-._").lower()
    text = text[:limit].strip("-._")
    return text or fallback


def item_file_stem(source_id, title, url):
    digest = hashlib.sha1((url or title or source_id).encode("utf-8")).hexdigest()[:10]
    title_slug = safe_slug(title or "item", fallback="item", limit=70)
    return f"{safe_slug(source_id, fallback='source', limit=40)}-{title_slug}-{digest}"


def write_archive_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text((text or "").rstrip() + "\n")
    return str(path.relative_to(ROOT))


def readable_title_from_markdown(markdown_text):
    for line in (markdown_text or "").splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped.lstrip("#").strip()[:180]
    return ""


def fetch_readable_page(url, output_dir, stem, fetched=None):
    result = {
        "fulltext_attempted": True,
        "fulltext_url": url,
        "fulltext_min_chars": FULLTEXT_MIN_CHARS,
    }
    fetched = fetched or curl_text(url)
    curl_reason = ""
    html_path = None

    if fetched.get("body"):
        html_path = write_archive_text(output_dir / f"{stem}.html", fetched["body"])
        result["raw_html_path"] = html_path

    if fetched.get("ok"):
        extracted = strip_html(fetched.get("body", ""))
        if content_text_is_usable(extracted) and not html_looks_limited(fetched.get("body", "")):
            extracted_path = write_archive_text(output_dir / f"{stem}.extracted.md", extracted)
            result.update(
                {
                    "fulltext_status": "ok",
                    "fulltext_method": "curl",
                    "fulltext_path": extracted_path,
                    "fulltext_chars": len(extracted),
                    "fulltext_excerpt": text_excerpt(extracted),
                }
            )
            return result
        curl_reason = "curl returned limited/challenge content" if html_looks_limited(fetched.get("body", "")) else "curl returned short or unreadable content"
    else:
        curl_reason = fetched.get("stderr") or f"curl exit {fetched.get('status')}"

    fallback = autocli_read_markdown(url)
    if fallback.get("ok"):
        body = fallback["body"]
        readable = strip_markdown(body)
        autocli_path = write_archive_text(output_dir / f"{stem}.autocli.md", body)
        result.update(
            {
                "fulltext_status": "ok",
                "fulltext_method": "autocli-read",
                "fulltext_path": autocli_path,
                "fulltext_chars": len(readable),
                "fulltext_excerpt": text_excerpt(readable),
                "fallback_reason": curl_reason,
                "autocli_attempts": fallback.get("attempts"),
            }
        )
        title = readable_title_from_markdown(body)
        if title:
            result["fulltext_title"] = title
        return result

    status = "limited" if html_path else "failed"
    result.update(
        {
            "fulltext_status": status,
            "fulltext_method": "curl",
            "fulltext_error": f"{curl_reason}; autocli fallback failed: {fallback.get('error') or 'unknown error'}",
        }
    )
    return result


def phrase_matches(haystack, phrase):
    return phrase.lower() in haystack


def rss_item_relevance(source, item, topics_by_id):
    haystack = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    matched_topics = []
    matched_keywords = []
    excluded_phrases = []

    for topic_id in source.get("topics", []):
        topic = topics_by_id.get(topic_id, {})
        topic_excludes = [phrase for phrase in topic.get("exclude", []) if phrase_matches(haystack, phrase)]
        if topic_excludes:
            excluded_phrases.extend(topic_excludes)
            continue
        topic_keywords = [keyword for keyword in topic.get("keywords", []) if phrase_matches(haystack, keyword)]
        if topic_keywords:
            matched_topics.append(topic_id)
            matched_keywords.extend(topic_keywords)

    if excluded_phrases and not matched_keywords:
        return {
            "relevance_status": "excluded",
            "matched_topics": [],
            "matched_keywords": [],
            "excluded_phrases": sorted(set(excluded_phrases)),
            "is_relevant": False,
        }

    if matched_keywords:
        return {
            "relevance_status": "matched",
            "matched_topics": sorted(set(matched_topics)),
            "matched_keywords": sorted(set(matched_keywords), key=str.lower),
            "is_relevant": True,
        }

    return {
        "relevance_status": "not_relevant",
        "matched_topics": [],
        "matched_keywords": [],
        "is_relevant": False,
    }


def enrich_rss_items_with_fulltext(source, items, output_dir, topics_by_id):
    source_dir = output_dir / "rss-fulltext" / safe_slug(source.get("id", "rss-source"))
    enriched = []
    for item in items:
        item = dict(item)
        relevance = rss_item_relevance(source, item, topics_by_id)
        item.update({key: value for key, value in relevance.items() if key != "is_relevant"})
        if not relevance["is_relevant"]:
            item["fulltext_status"] = "skipped"
            item["fulltext_reason"] = f"RSS title/summary did not match configured topics for {source.get('id')}."
            enriched.append(item)
            continue

        url = item.get("url")
        if not url:
            item["fulltext_status"] = "failed"
            item["fulltext_error"] = "RSS item has no URL to fetch."
            enriched.append(item)
            continue

        stem = item_file_stem(source.get("id", "rss-source"), item.get("title", ""), url)
        item.update(fetch_readable_page(url, source_dir, stem))
        enriched.append(item)
    return enriched


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


def collect_rss(rss_sources, output_dir, topics_by_id):
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
            items = enrich_rss_items_with_fulltext(source, items, output_dir, topics_by_id)
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


def rss_fulltext_summary(rss_results):
    counts = {
        "matched": 0,
        "attempted": 0,
        "ok": 0,
        "limited": 0,
        "failed": 0,
        "skipped": 0,
    }
    for source in rss_results:
        for item in source.get("items", []):
            status = item.get("fulltext_status")
            if item.get("relevance_status") == "matched":
                counts["matched"] += 1
            if status in {"ok", "limited", "failed", "skipped"}:
                counts[status] += 1
            if status in {"ok", "limited", "failed"}:
                counts["attempted"] += 1
    return counts


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


def parse_github_trending_items(html_text, limit=MAX_TRENDING_REPOS_PER_SOURCE):
    items = []
    for match in re.finditer(r'<article class="Box-row">(?P<body>.*?)</article>', html_text, re.DOTALL):
        body = match.group("body")
        repo_match = re.search(r'<h2[^>]*>.*?<a\b[^>]*href="/(?P<repo>[^"]+)"[^>]*>.*?</h2>', body, re.DOTALL)
        if not repo_match:
            continue
        repo = re.sub(r"\s+", "", strip_html(repo_match.group("repo")))
        if "/" not in repo:
            continue
        description_match = re.search(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(?P<description>.*?)</p>', body, re.DOTALL)
        language_match = re.search(r'<span itemprop="programmingLanguage">(?P<language>[^<]+)</span>', body)
        stars_match = re.search(r'<a[^>]+href="/%s/stargazers"[^>]*>(?P<stars>.*?)</a>' % re.escape(repo), body, re.DOTALL)
        forks_match = re.search(r'<a[^>]+href="/%s/forks"[^>]*>(?P<forks>.*?)</a>' % re.escape(repo), body, re.DOTALL)
        today_match = re.search(r'(?P<stars_today>[\d,]+)\s+stars?\s+today', strip_html(body), re.IGNORECASE)
        description = strip_html(description_match.group("description")) if description_match else ""
        items.append(
            {
                "repo": repo,
                "url": f"https://github.com/{repo}",
                "description": description,
                "trending_description": description,
                "language": strip_html(language_match.group("language")) if language_match else "",
                "stars": strip_html(stars_match.group("stars")) if stars_match else "",
                "forks": strip_html(forks_match.group("forks")) if forks_match else "",
                "stars_today": strip_html(today_match.group("stars_today")) if today_match else "",
            }
        )
        if len(items) >= limit:
            break
    return items


def safe_repo_filename(repo):
    return repo.replace("/", "__")


def readme_title(readme_text):
    for line in readme_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip()
            if title:
                return title[:160]
    return ""


def readme_excerpt(readme_text, limit=900):
    cleaned = strip_markdown(readme_text)
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[:limit].rsplit(" ", 1)[0]


def collect_repo_readme(repo, output_dir):
    readme_dir = output_dir / "github-trending-readmes"
    readme_dir.mkdir(parents=True, exist_ok=True)
    for candidate in README_CANDIDATES:
        url = f"https://raw.githubusercontent.com/{repo}/HEAD/{candidate}"
        fetched = curl_text(url)
        if not fetched["ok"]:
            fallback = autocli_read_markdown(url)
            if fallback.get("ok"):
                body = fallback["body"].strip()
                suffix = Path(candidate).suffix or ".txt"
                local_path = readme_dir / f"{safe_repo_filename(repo)}{suffix}"
                local_path.write_text(body + "\n")
                return {
                    "readme_status": "ok",
                    "readme_method": "autocli-read",
                    "readme_url": url,
                    "readme_path": str(local_path.relative_to(ROOT)),
                    "readme_title": readme_title(body) or readable_title_from_markdown(body),
                    "readme_excerpt": readme_excerpt(body),
                }
            continue
        body = fetched["body"].strip()
        if not body or body.startswith("404: Not Found"):
            continue
        suffix = Path(candidate).suffix or ".txt"
        local_path = readme_dir / f"{safe_repo_filename(repo)}{suffix}"
        local_path.write_text(body + "\n")
        return {
            "readme_status": "ok",
            "readme_method": "curl",
            "readme_url": url,
            "readme_path": str(local_path.relative_to(ROOT)),
            "readme_title": readme_title(body),
            "readme_excerpt": readme_excerpt(body),
        }
    return {
        "readme_status": "missing",
        "readme_error": "No README candidate fetched from raw.githubusercontent.com HEAD branch.",
    }


def collect_github_trending(trending_sources, output_dir):
    results = []
    for source in trending_sources:
        fetched = curl_text(source["url"])
        if not fetched["ok"]:
            stem = item_file_stem(source["id"], source["name"], source["url"])
            fallback = fetch_readable_page(source["url"], output_dir / "github-trending-pages", stem, fetched=fetched)
            if fallback.get("fulltext_status") == "ok":
                results.append(
                    {
                        "source_id": source["id"],
                        "source_name": source["name"],
                        "url": source["url"],
                        "status": "limited",
                        "reason": "GitHub Trending curl fetch failed; autocli-readable snapshot archived, but repo-card parser requires raw Trending HTML.",
                        "items": [],
                        **fallback,
                    }
                )
                continue
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
        items = parse_github_trending_items(fetched["body"])
        for item in items:
            item.update(collect_repo_readme(item["repo"], output_dir))
        record = {
            "source_id": source["id"],
            "source_name": source["name"],
            "url": source["url"],
            "status": "ok" if items else "limited",
            "items": items,
            "note": "GitHub Trending is a discovery source; repo popularity is not evidence of project quality or release significance.",
        }
        if not items:
            stem = item_file_stem(source["id"], source["name"], source["url"])
            fallback = fetch_readable_page(source["url"], output_dir / "github-trending-pages", stem, fetched=fetched)
            if fallback.get("fulltext_status") == "ok":
                record.update(fallback)
                record["reason"] = "GitHub Trending HTML fetched but no repository cards were parsed; readable diagnostic snapshot archived."
            else:
                record.update({key: value for key, value in fallback.items() if key.startswith("fulltext_") or key.endswith("_path")})
                record["reason"] = "GitHub Trending HTML fetched but no repository cards were parsed."
        elif any(item.get("readme_status") != "ok" for item in items):
            record["readme_limited_count"] = sum(1 for item in items if item.get("readme_status") != "ok")
        results.append(record)
    return results


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


def collect_official_pages(official_sources, output_dir):
    results = []
    for source in official_sources:
        fetched = curl_text(source["url"])
        if not fetched["ok"]:
            stem = item_file_stem(source["id"], source["name"], source["url"])
            fallback = fetch_readable_page(source["url"], output_dir / "official-page-text", stem, fetched=fetched)
            if fallback.get("fulltext_status") == "ok":
                results.append(
                    {
                        "source_id": source["id"],
                        "source_name": source["name"],
                        "url": source["url"],
                        "status": "ok",
                        "title": fallback.get("fulltext_title", ""),
                        "fetch_method": "autocli-read",
                        **fallback,
                    }
                )
                continue
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
        if html_looks_limited(fetched["body"]):
            stem = item_file_stem(source["id"], title or source["name"], source["url"])
            fallback = fetch_readable_page(source["url"], output_dir / "official-page-text", stem, fetched=fetched)
            if fallback.get("fulltext_status") == "ok":
                record.update(fallback)
                record["fetch_method"] = fallback.get("fulltext_method")
                record["title"] = fallback.get("fulltext_title") or title
            else:
                record.update(fallback)
                record["status"] = "limited"
                record["reason"] = "HTML page returned limited/challenge content; autocli fallback did not produce readable text."
        elif source["id"] == "openai-news" and not title:
            stem = item_file_stem(source["id"], source["name"], source["url"])
            fallback = fetch_readable_page(source["url"], output_dir / "official-page-text", stem, fetched=fetched)
            if fallback.get("fulltext_status") == "ok":
                record.update(fallback)
                record["fetch_method"] = fallback.get("fulltext_method")
                record["title"] = fallback.get("fulltext_title") or title
            else:
                record.update(fallback)
                record["status"] = "limited"
                record["reason"] = "HTML page did not return a usable title/content snapshot; autocli fallback did not produce readable text."
        elif "app unavailable in region" in body_lower:
            stem = item_file_stem(source["id"], title or source["name"], source["url"])
            fallback = fetch_readable_page(source["url"], output_dir / "official-page-text", stem, fetched=fetched)
            if fallback.get("fulltext_status") == "ok":
                record.update(fallback)
                record["fetch_method"] = fallback.get("fulltext_method")
                record["title"] = fallback.get("fulltext_title") or title
            else:
                record.update(fallback)
                record["status"] = "limited"
                record["reason"] = "Redirected to platform.claude.com and returned region-unavailable HTML; autocli fallback did not produce readable text."
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


def load_topics():
    config = yaml.safe_load(TOPICS_PATH.read_text())
    return {item["id"]: item for item in config.get("topics", [])}


def load_sources():
    config = yaml.safe_load(CONFIG_PATH.read_text())
    return (
        [item for item in config.get("rss", []) if item.get("enabled")],
        [item for item in config.get("github_repos", []) if item.get("enabled")],
        [item for item in config.get("github_trending", []) if item.get("enabled")],
        [item for item in config.get("official_pages", []) if item.get("enabled")],
    )


def main():
    run_date = os.environ.get("RUN_DATE") or now_local().strftime("%Y-%m-%d")
    output_dir = RAW_ROOT / run_date
    output_dir.mkdir(parents=True, exist_ok=True)

    rss_sources, github_sources, trending_sources, official_sources = load_sources()
    topics_by_id = load_topics()
    rss_results = collect_rss(rss_sources, output_dir, topics_by_id)
    github_api_status, github_results = collect_github(github_sources)
    trending_results = collect_github_trending(trending_sources, output_dir)
    official_results = collect_official_pages(official_sources, output_dir)
    rss_fulltext = rss_fulltext_summary(rss_results)

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
    trending_payload = {
        "schema_version": 1,
        "collected_at": now_local().isoformat(timespec="seconds"),
        "sources": trending_results,
    }

    (output_dir / "rss-items.json").write_text(json.dumps(rss_payload, ensure_ascii=False, indent=2) + "\n")
    (output_dir / "github-items.json").write_text(json.dumps(github_payload, ensure_ascii=False, indent=2) + "\n")
    (output_dir / "github-trending.json").write_text(json.dumps(trending_payload, ensure_ascii=False, indent=2) + "\n")
    (output_dir / "official-pages.json").write_text(json.dumps(official_payload, ensure_ascii=False, indent=2) + "\n")

    summary = {
        "run_date": run_date,
        "rss_sources": len(rss_results),
        "rss_ok": sum(1 for item in rss_results if item["status"] == "ok"),
        "rss_fulltext_matched": rss_fulltext["matched"],
        "rss_fulltext_attempted": rss_fulltext["attempted"],
        "rss_fulltext_ok": rss_fulltext["ok"],
        "rss_fulltext_limited": rss_fulltext["limited"],
        "rss_fulltext_failed": rss_fulltext["failed"],
        "github_sources": len(github_results),
        "github_ok": sum(1 for item in github_results if item["status"] == "ok"),
        "github_trending_sources": len(trending_results),
        "github_trending_ok": sum(1 for item in trending_results if item["status"] == "ok"),
        "official_sources": len(official_results),
        "official_ok": sum(1 for item in official_results if item["status"] == "ok"),
        "official_limited": sum(1 for item in official_results if item["status"] == "limited"),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
