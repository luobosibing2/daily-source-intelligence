#!/usr/bin/env python3
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "raw"
REVIEWS_ROOT = ROOT / "reviews"
X_MIN_SCORE = 20


def read_json(path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path):
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def compact_text(text, limit=90):
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def is_covered(values, report_text):
    for value in values:
        value = str(value or "").strip()
        if value and value in report_text:
            return True
    return False


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


def candidate_rows(root, run_date, report_text, seen=None):
    seen = seen or {"ids": set(), "urls": set()}
    payload = read_json(root / "raw" / run_date / "official-link-candidates.json", {"candidates": []})
    rows = []
    for candidate in payload.get("candidates", []):
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
        values = [
            expanded_url,
            tweet_url,
            tweet_id,
        ]
        rows.append(
            {
                "category": "official-link-candidate",
                "status": "covered" if is_covered(values, report_text) else "missed",
                "signal": candidate.get("expanded_url") or candidate.get("tweet_url") or candidate.get("tweet_id"),
                "source": candidate.get("tweet_url"),
                "tweet_id": candidate.get("tweet_id"),
                "reason": candidate.get("trigger_reason", ""),
                "score": candidate.get("score"),
                "fulltext_status": candidate.get("fulltext_status"),
            }
        )
    return rows


def rss_rows(root, run_date, report_text, seen=None):
    seen = seen or {"ids": set(), "urls": set()}
    payload = read_json(root / "raw" / run_date / "rss-items.json", {"sources": []})
    rows = []
    for source in payload.get("sources", []):
        for item in source.get("items", []):
            if item.get("relevance_status") not in {"matched", "always_read"}:
                continue
            url = item.get("url")
            if already_seen(seen, ids=[f"url:{url}" if url else ""], urls=[url]):
                continue
            values = [item.get("url"), item.get("title"), item.get("fulltext_path")]
            rows.append(
                {
                    "category": "matched-rss",
                    "status": "covered" if is_covered(values, report_text) else "missed",
                    "signal": item.get("title") or item.get("url"),
                    "source": item.get("url"),
                    "reason": ",".join(item.get("matched_keywords") or []),
                    "score": "",
                    "fulltext_status": item.get("fulltext_status"),
                }
            )
    return rows


def tweet_score(tweet):
    engagement = sum(int(tweet.get(key) or 0) for key in ["retweetCount", "replyCount", "likeCount", "quoteCount"])
    text = (tweet.get("text") or "").lower()
    keyword_hits = sum(1 for keyword in ["agent", "ai", "claude", "codex", "llm", "mcp"] if keyword in text)
    return min(engagement // 25, 40) + keyword_hits * 12


def tweet_id_from_row(row):
    if row.get("tweet_id"):
        return str(row.get("tweet_id"))
    source = str(row.get("source") or "")
    if source:
        return source.rstrip("/").split("/")[-1]
    return ""


def normalize_handle(value):
    return str(value or "").strip().lstrip("@").lower()


def twitter_topic_summary_section(report_text):
    lines = []
    in_section = False
    for line in report_text.splitlines():
        if line.strip() == "### X/Twitter 推主主题摘要":
            in_section = True
            continue
        if in_section and line.startswith("### "):
            break
        if in_section:
            lines.append(line)
    return "\n".join(lines)


def handle_mentioned(line, handle):
    handle = normalize_handle(handle)
    if not handle:
        return False
    return re.search(rf"(?<![A-Za-z0-9_])@?{re.escape(handle)}(?![A-Za-z0-9_])", line, re.IGNORECASE) is not None


def line_has_tweet_link_for_handle(line, handle, urls):
    line_lower = line.lower()
    for url in urls:
        if url and str(url).lower() in line_lower:
            return True
    handle = normalize_handle(handle)
    if not handle:
        return False
    return re.search(rf"https://(?:x|twitter)\.com/{re.escape(handle)}/status/[0-9A-Za-z_]+", line, re.IGNORECASE) is not None


def twitter_topic_items_by_handle(root, run_date):
    payload = read_json(root / "raw" / run_date / "twitter-topic-brief.json", {"topics": []})
    by_handle = {}
    for topic in payload.get("topics", []) or []:
        for item in topic.get("items", []) or []:
            handle = normalize_handle(item.get("handle"))
            url = item.get("url")
            if not handle or not url:
                continue
            by_handle.setdefault(handle, []).append(item)
    for items in by_handle.values():
        items.sort(key=lambda item: (-int(item.get("score") or 0), str(item.get("tweet_id") or "")))
    return by_handle


def twitter_topic_summary_link_rows(root, run_date, report_text):
    section = twitter_topic_summary_section(report_text)
    if not section.strip():
        return []
    rows = []
    by_handle = twitter_topic_items_by_handle(root, run_date)
    for line_no, line in enumerate(section.splitlines(), start=1):
        for handle in sorted(by_handle):
            if not handle_mentioned(line, handle):
                continue
            urls = [item.get("url") for item in by_handle[handle]]
            if line_has_tweet_link_for_handle(line, handle, urls):
                continue
            item = by_handle[handle][0]
            rows.append(
                {
                    "category": "twitter-topic-summary-link",
                    "status": "missed",
                    "signal": f"{handle} mentioned without same-line tweet link",
                    "source": item.get("url"),
                    "tweet_id": item.get("tweet_id"),
                    "reason": f"X/Twitter 推主主题摘要 line {line_no} lacks same-line tweet link",
                    "score": item.get("score", ""),
                    "fulltext_status": "n/a",
                }
            )
    return rows


def topic_direct_x_rows(root, run_date, report_text, existing_tweet_ids, seen=None):
    seen = seen or {"ids": set(), "urls": set()}
    payload = read_json(root / "raw" / run_date / "twitter-topic-brief.json", {"topics": []})
    rows = []
    seen_tweet_ids = {str(tweet_id) for tweet_id in existing_tweet_ids if tweet_id}
    for topic in payload.get("topics", []) or []:
        topic_id = topic.get("id") or ""
        for item in topic.get("items", []) or []:
            tweet_id = str(item.get("tweet_id") or "")
            if not tweet_id or tweet_id in seen_tweet_ids:
                continue
            url = item.get("url")
            if already_seen(seen, ids=[f"tweet:{tweet_id}", f"url:{url}" if url else ""], urls=[url]):
                continue
            score = int(item.get("score") or 0)
            if score < X_MIN_SCORE:
                continue
            values = [item.get("url"), tweet_id, compact_text(item.get("text_excerpt"), 60)]
            rows.append(
                {
                    "category": "topic-direct-x",
                    "status": "covered" if is_covered(values, report_text) else "missed",
                    "signal": compact_text(item.get("text_excerpt")),
                    "source": item.get("url"),
                    "tweet_id": tweet_id,
                    "reason": f"topic:{topic_id}; score>={X_MIN_SCORE}",
                    "score": score,
                    "fulltext_status": "n/a",
                }
            )
            seen_tweet_ids.add(tweet_id)
    rows.sort(key=lambda item: (-int(item.get("score") or 0), item.get("signal") or ""))
    return rows


def direct_x_rows(root, run_date, report_text, existing_tweet_ids, seen=None):
    seen = seen or {"ids": set(), "urls": set()}
    payload = read_json(root / "raw" / run_date / "twitterapi-io-results.json", {"accounts": []})
    rows = []
    for account in payload.get("accounts", []):
        if account.get("status") != "ok":
            continue
        for tweet in account.get("tweets", []):
            tweet_id = tweet.get("id") or tweet.get("tweet_id")
            if tweet_id in existing_tweet_ids:
                continue
            url = tweet.get("url") or tweet.get("twitterUrl")
            if already_seen(seen, ids=[f"tweet:{tweet_id}" if tweet_id else "", f"url:{url}" if url else ""], urls=[url]):
                continue
            score = tweet_score(tweet)
            if score < X_MIN_SCORE:
                continue
            values = [tweet.get("url"), tweet.get("twitterUrl"), tweet_id, compact_text(tweet.get("text"), 60)]
            rows.append(
                {
                    "category": "top-direct-x",
                    "status": "covered" if is_covered(values, report_text) else "missed",
                    "signal": compact_text(tweet.get("text")),
                    "source": tweet.get("url") or tweet.get("twitterUrl"),
                    "tweet_id": tweet_id,
                    "reason": f"score>={X_MIN_SCORE}",
                    "score": score,
                    "fulltext_status": "n/a",
                }
            )
    rows.sort(key=lambda item: (-int(item.get("score") or 0), item.get("signal") or ""))
    return rows[:10]


def build_audit(run_date, root=ROOT):
    root = Path(root)
    report_path = root / "docs" / f"{run_date}-daily-intel.md"
    report_text = read_text(report_path)
    seen = load_seen_before_run_date(root, run_date)
    rows = candidate_rows(root, run_date, report_text, seen=seen)
    existing_tweet_ids = {tweet_id_from_row(row) for row in rows if tweet_id_from_row(row)}
    rows.extend(rss_rows(root, run_date, report_text, seen=seen))
    topic_rows = topic_direct_x_rows(root, run_date, report_text, existing_tweet_ids, seen=seen)
    rows.extend(topic_rows)
    existing_tweet_ids.update(tweet_id_from_row(row) for row in topic_rows if tweet_id_from_row(row))
    rows.extend(twitter_topic_summary_link_rows(root, run_date, report_text))
    rows.extend(direct_x_rows(root, run_date, report_text, existing_tweet_ids, seen=seen))
    counts = {
        "covered": sum(1 for row in rows if row["status"] == "covered"),
        "missed": sum(1 for row in rows if row["status"] == "missed"),
    }
    return {
        "schema_version": 1,
        "run_date": run_date,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "daily_report": str(report_path.relative_to(root)),
        "counts": counts,
        "rows": rows,
    }


def link(value):
    value = str(value or "")
    if not value:
        return ""
    if value.startswith("http://") or value.startswith("https://"):
        return f"[link]({value})"
    return value


def render_markdown(audit):
    lines = [
        f"# {audit['run_date']} Candidate Audit",
        "",
        f"- daily_report: [{audit['daily_report']}](../{audit['daily_report']})",
        f"- covered: {audit['counts']['covered']}",
        f"- missed: {audit['counts']['missed']}",
        "",
        "| Status | Category | Signal | Source | Score | Fulltext | Reason |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in audit["rows"]:
        lines.append(
            "| {status} | {category} | {signal} | {source} | {score} | {fulltext} | {reason} |".format(
                status=row["status"],
                category=row["category"],
                signal=compact_text(row.get("signal")),
                source=link(row.get("source")),
                score=row.get("score", ""),
                fulltext=row.get("fulltext_status", ""),
                reason=compact_text(row.get("reason"), 80),
            )
        )
    lines.append("")
    return "\n".join(lines)


def write_audit(run_date, root=ROOT):
    audit = build_audit(run_date, root=root)
    output_path = Path(root) / "reviews" / f"{run_date}-candidate-audit.md"
    write_text(output_path, render_markdown(audit))
    return audit


def main(argv=None):
    parser = argparse.ArgumentParser(description="Audit high-signal candidates against the daily report.")
    parser.add_argument("--date", required=True)
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args(argv)
    audit = write_audit(args.date, root=Path(args.root))
    if args.stdout:
        print(json.dumps(audit, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
