#!/usr/bin/env python3
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
X_MIN_SCORE = 20
TOP_ITEMS_LIMIT = 20
PRIORITY_ACCOUNT_BONUS = 10


def read_json(path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_yaml(path, default):
    if not path.exists():
        return default
    return yaml.safe_load(path.read_text(encoding="utf-8")) or default


def compact_text(text, limit=180):
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def normalize_handle(value):
    return str(value or "").strip().lstrip("@").lower()


def collect_string_values(value):
    if isinstance(value, dict):
        results = []
        for child in value.values():
            results.extend(collect_string_values(child))
        return results
    if isinstance(value, list):
        results = []
        for child in value:
            results.extend(collect_string_values(child))
        return results
    if isinstance(value, str):
        return [value]
    return []


def tweet_text_for_matching(tweet):
    parts = [tweet.get("text") or ""]
    parts.extend(collect_string_values(tweet.get("card") or {}))
    return "\n".join(part for part in parts if part)


def phrase_matches(haystack, phrase):
    phrase = str(phrase or "").lower()
    if not phrase:
        return False
    if re.fullmatch(r"[a-z0-9][a-z0-9._+-]*", phrase):
        return re.search(rf"(?<![a-z0-9]){re.escape(phrase)}(?![a-z0-9])", haystack) is not None
    return phrase in haystack


def load_topics(root):
    payload = read_yaml(Path(root) / "config" / "topics.yaml", {"topics": []})
    return [
        {
            "id": str(topic.get("id") or ""),
            "label": str(topic.get("label") or topic.get("id") or ""),
            "keywords": [str(keyword) for keyword in topic.get("keywords", []) or []],
            "exclude": [str(keyword) for keyword in topic.get("exclude", []) or []],
        }
        for topic in payload.get("topics", [])
        if topic.get("id")
    ]


def load_accounts(root):
    payload = read_yaml(Path(root) / "config" / "sources.yaml", {"x_accounts": []})
    accounts = {}
    for account in payload.get("x_accounts", []) or []:
        handle = normalize_handle(account.get("handle"))
        if not handle:
            continue
        accounts[handle] = {
            "id": account.get("id"),
            "name": account.get("name"),
            "handle": account.get("handle"),
            "enabled": account.get("enabled") is True,
            "priority": account.get("priority") is True,
            "topics": [str(topic) for topic in account.get("topics", []) or []],
        }
    return accounts


def topic_keyword_matches(tweet, topics):
    haystack = tweet_text_for_matching(tweet).lower()
    matched_topic_ids = []
    matched_keywords = []
    for topic in topics:
        if any(phrase_matches(haystack, exclude) for exclude in topic["exclude"]):
            continue
        hits = [keyword for keyword in topic["keywords"] if phrase_matches(haystack, keyword)]
        if hits:
            matched_topic_ids.append(topic["id"])
            matched_keywords.extend(hits)
    return matched_topic_ids, sorted(set(matched_keywords))


def ordered_topic_union(topics, *topic_lists):
    requested = set()
    for topic_list in topic_lists:
        requested.update(topic for topic in topic_list if topic)
    known = [topic["id"] for topic in topics if topic["id"] in requested]
    unknown = sorted(requested.difference(known))
    return known + unknown


def int_value(value):
    try:
        return int(value or 0)
    except Exception:
        return 0


def tweet_score(tweet, matched_keywords, account):
    engagement = sum(int_value(tweet.get(key)) for key in ["retweetCount", "replyCount", "likeCount", "quoteCount"])
    score = min(engagement // 25, 40) + len(set(matched_keywords)) * 12
    if account.get("priority"):
        score += PRIORITY_ACCOUNT_BONUS
    text = tweet.get("text") or ""
    if text.strip().startswith("RT @") or tweet.get("retweeted_tweet"):
        score -= 15
    if tweet.get("isReply"):
        score -= 10
    return max(score, 0)


def boundary_note(tweet):
    notes = ["direct-x from twitterapi.io"]
    text = tweet.get("text") or ""
    if text.strip().startswith("RT @") or tweet.get("retweeted_tweet"):
        notes.append("retweet downranked but retained")
    if tweet.get("isReply"):
        notes.append("reply downranked but retained")
    return "; ".join(notes)


def clean_handle(handle):
    return str(handle or "").strip().lstrip("@")


def author_url(handle):
    handle = clean_handle(handle)
    if not handle:
        return ""
    return f"https://x.com/{handle}"


def tweet_url(tweet, handle=None):
    url = tweet.get("url") or tweet.get("twitterUrl") or ""
    if url:
        return url
    tweet_id = tweet.get("id") or tweet.get("tweet_id")
    handle = clean_handle(handle)
    if tweet_id and handle:
        return f"https://x.com/{handle}/status/{tweet_id}"
    return ""


def tweet_markdown(tweet_id, url):
    if tweet_id and url:
        return f"[{tweet_id}]({url})"
    return str(tweet_id or "")


def build_item(account_result, configured_account, tweet, topics):
    keyword_topics, matched_keywords = topic_keyword_matches(tweet, topics)
    account_topics = configured_account.get("topics", [])
    matched_topics = ordered_topic_union(topics, keyword_topics, account_topics)
    score = tweet_score(tweet, matched_keywords, configured_account)
    handle = account_result.get("handle") or configured_account.get("handle")
    tweet_id = tweet.get("id") or tweet.get("tweet_id")
    url = tweet_url(tweet, handle)
    link = tweet_markdown(tweet_id, url)
    return {
        "tweet_id": tweet_id,
        "handle": handle,
        "name": account_result.get("name") or configured_account.get("name"),
        "author_url": author_url(handle),
        "url": url,
        "tweet_markdown": link,
        "citation_markdown": f"`{handle}` 的 {link}" if handle and link else link,
        "created_at": tweet.get("createdAt"),
        "text_excerpt": compact_text(tweet.get("text")),
        "score": score,
        "matched_topics": matched_topics,
        "matched_keywords": matched_keywords,
        "account_topics": account_topics,
        "evidence_level": "direct-x",
        "boundary_note": boundary_note(tweet),
    }


def sort_items(items):
    return sorted(
        items,
        key=lambda item: (
            -int_value(item.get("score")),
            str(item.get("created_at") or ""),
            str(item.get("tweet_id") or ""),
        ),
    )


def coverage_status(twitter):
    provider_status = twitter.get("status") or "missing"
    accounts = twitter.get("accounts", []) or []
    failed_accounts = [
        {
            "handle": account.get("handle"),
            "status": account.get("status"),
            "error": account.get("error"),
            "reason": account.get("reason"),
        }
        for account in accounts
        if account.get("status") not in {"ok", "skipped"}
    ]
    skipped_accounts = [
        {
            "handle": account.get("handle"),
            "status": account.get("status"),
            "reason": account.get("reason"),
        }
        for account in accounts
        if account.get("status") == "skipped"
    ]
    if provider_status in {"skipped", "failed", "missing"}:
        status = provider_status
    elif failed_accounts or skipped_accounts:
        status = "partial"
    else:
        status = "ok"
    return status, failed_accounts, skipped_accounts


def build_brief(run_date, root=ROOT):
    root = Path(root)
    topics = load_topics(root)
    accounts = load_accounts(root)
    twitter_path = root / "raw" / run_date / "twitterapi-io-results.json"
    twitter = read_json(twitter_path, {"status": "missing", "accounts": []})
    status, failed_accounts, skipped_accounts = coverage_status(twitter)

    items = []
    for account_result in twitter.get("accounts", []) or []:
        if account_result.get("status") != "ok":
            continue
        configured_account = accounts.get(normalize_handle(account_result.get("handle")), {})
        for tweet in account_result.get("tweets", []) or []:
            item = build_item(account_result, configured_account, tweet, topics)
            if not item.get("tweet_id"):
                continue
            items.append(item)

    grouped = {topic["id"]: [] for topic in topics}
    ungrouped = []
    for item in items:
        if item["matched_topics"]:
            for topic_id in item["matched_topics"]:
                grouped.setdefault(topic_id, []).append(item)
        else:
            ungrouped.append(item)

    topic_payloads = []
    topic_labels = {topic["id"]: topic["label"] for topic in topics}
    for topic in topics:
        topic_items = sort_items(grouped.get(topic["id"], []))
        if not topic_items:
            continue
        topic_payloads.append(
            {
                "id": topic["id"],
                "label": topic["label"],
                "tweet_count": len(topic_items),
                "items": topic_items,
            }
        )
    for topic_id in sorted(set(grouped).difference(topic_labels)):
        topic_items = sort_items(grouped.get(topic_id, []))
        if topic_items:
            topic_payloads.append(
                {
                    "id": topic_id,
                    "label": topic_id,
                    "tweet_count": len(topic_items),
                    "items": topic_items,
                }
            )

    payload = {
        "schema_version": 1,
        "run_date": run_date,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "status": status,
        "coverage": {
            "provider": "twitterapi.io",
            "provider_status": twitter.get("status") or "missing",
            "account_count": len(twitter.get("accounts", []) or []),
            "ok_accounts": sum(1 for account in twitter.get("accounts", []) or [] if account.get("status") == "ok"),
            "failed_accounts": failed_accounts,
            "skipped_accounts": skipped_accounts,
            "tweet_count": len(items),
        },
        "topics": topic_payloads,
        "ungrouped": sort_items(ungrouped),
        "top_items": sort_items(items)[:TOP_ITEMS_LIMIT],
    }
    write_json(root / "raw" / run_date / "twitter-topic-brief.json", payload)
    return payload


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build a topic-grouped summary of twitterapi.io direct X items.")
    parser.add_argument("--date", required=True)
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args(argv)
    payload = build_brief(args.date, root=Path(args.root))
    if args.stdout:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
