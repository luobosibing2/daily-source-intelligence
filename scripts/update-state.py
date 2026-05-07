#!/usr/bin/env python3
import json
import os
import re
import sys
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "raw"
STATE_ROOT = ROOT / "state"

PROXY = {
    "http_proxy": "http://127.0.0.1:7890",
    "https_proxy": "http://127.0.0.1:7890",
    "all_proxy": "socks5://127.0.0.1:7890",
}

X_KEYWORDS = [
    "agent",
    "agents",
    "ai",
    "claude",
    "codex",
    "cursor",
    "llm",
    "mcp",
    "openclaw",
    "openai",
    "revenue",
    "saas",
    "startup",
    "vibe",
    "自动化",
    "独立开发",
]
X_MAX_AUTO_SEEN = int(os.environ.get("DAILY_INTEL_X_MAX_AUTO_SEEN", "40"))
X_MIN_SCORE = int(os.environ.get("DAILY_INTEL_X_MIN_SCORE", "20"))


def now_local():
    return datetime.now().astimezone()


def read_json(path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text())


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def parse_date(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except Exception:
        pass
    try:
        return parsedate_to_datetime(value).date().isoformat()
    except Exception:
        return None


def in_daily_window(value, run_date, lookback_days=1):
    parsed = parse_date(value)
    if not parsed:
        return True
    run_day = datetime.fromisoformat(run_date).date()
    parsed_day = datetime.fromisoformat(parsed).date()
    return run_day - timedelta(days=lookback_days) <= parsed_day <= run_day


def today_from_run(run_date):
    return run_date or now_local().date().isoformat()


def load_raw(run_date):
    raw_dir = RAW_ROOT / run_date
    return {
        "raw_dir": raw_dir,
        "rss": read_json(raw_dir / "rss-items.json", {"sources": []}),
        "github": read_json(raw_dir / "github-items.json", {"sources": [], "api_status": {}}),
        "github_trending": read_json(raw_dir / "github-trending.json", {"sources": []}),
        "official": read_json(raw_dir / "official-pages.json", {"sources": []}),
        "twitter": read_json(raw_dir / "twitterapi-io-results.json", {"status": "missing", "accounts": []}),
    }


def status_counts(sources):
    return {
        "ok": sum(1 for item in sources if item.get("status") == "ok"),
        "limited": sum(1 for item in sources if item.get("status") == "limited"),
        "failed": sum(1 for item in sources if item.get("status") not in {"ok", "limited"}),
    }


def twitter_collection_status(twitter):
    provider_status = twitter.get("status")
    if provider_status != "ok":
        return provider_status or "failed"
    accounts = twitter.get("accounts", [])
    if not accounts:
        return "ok"
    ok_count = sum(1 for account in accounts if account.get("status") == "ok")
    if ok_count == len(accounts):
        return "ok"
    if ok_count > 0:
        return "partial"
    return "failed"


def source_health(raw, run_date):
    sources = {}

    for source in raw["rss"].get("sources", []):
        source_id = source.get("source_id")
        if not source_id:
            continue
        if source.get("status") == "ok":
            sources[source_id] = {
                "status": "ok",
                "last_success": run_date,
                "consecutive_failures": 0,
            }
        else:
            sources[source_id] = {
                "status": "failed",
                "last_checked": run_date,
                "consecutive_failures": 1,
                "note": source.get("error") or "RSS fetch or parsing failed.",
            }

    github_api = raw["github"].get("api_status", {})
    for source in raw["github"].get("sources", []):
        source_id = source.get("source_id")
        if not source_id:
            continue
        if source.get("status") == "ok":
            sources[source_id] = {
                "status": "ok_via_atom",
                "last_success": run_date,
                "consecutive_failures": 0,
                "api_status": github_api.get("status"),
            }
        else:
            sources[source_id] = {
                "status": "failed",
                "last_checked": run_date,
                "consecutive_failures": 1,
                "note": source.get("error") or "GitHub release feed failed.",
            }

    for source in raw["github_trending"].get("sources", []):
        source_id = source.get("source_id")
        if not source_id:
            continue
        if source.get("status") == "ok":
            sources[source_id] = {
                "status": "ok",
                "last_success": run_date,
                "consecutive_failures": 0,
                "note": f"{len(source.get('items', []))} daily trending repositories parsed.",
            }
        elif source.get("status") == "limited":
            sources[source_id] = {
                "status": "limited",
                "last_checked": run_date,
                "consecutive_failures": 1,
                "note": source.get("reason") or "GitHub Trending page returned limited parseable content.",
            }
        else:
            sources[source_id] = {
                "status": "failed",
                "last_checked": run_date,
                "consecutive_failures": 1,
                "note": source.get("error") or "GitHub Trending fetch or parsing failed.",
            }

    for source in raw["official"].get("sources", []):
        source_id = source.get("source_id")
        if not source_id:
            continue
        if source.get("status") == "ok":
            sources[source_id] = {
                "status": "ok",
                "last_success": run_date,
                "consecutive_failures": 0,
            }
        elif source.get("status") == "limited":
            sources[source_id] = {
                "status": "limited",
                "last_checked": run_date,
                "consecutive_failures": 1,
                "note": source.get("reason") or "Official page returned limited content.",
            }
        else:
            sources[source_id] = {
                "status": "failed",
                "last_checked": run_date,
                "consecutive_failures": 1,
                "note": source.get("error") or "Official page fetch failed.",
            }

    twitter = raw["twitter"]
    twitter_status = twitter_collection_status(twitter)
    twitter_ok = twitter_status == "ok"
    kept_total = sum(account.get("kept_count", 0) for account in twitter.get("accounts", []))
    failed_accounts = [account.get("handle") for account in twitter.get("accounts", []) if account.get("status") != "ok"]
    sources["twitterapi.io"] = {
        "status": twitter_status,
        "last_success" if twitter_ok else "last_checked": run_date,
        "consecutive_failures": 0 if twitter_ok else 1,
        "note": f"{len(twitter.get('accounts', []))} configured accounts processed; {kept_total} direct X items kept in the {twitter.get('window_hours', 36)}h window.",
    }
    if failed_accounts:
        sources["twitterapi.io"]["failed_accounts"] = failed_accounts
    sources["x-twitter"] = {
        "status": "ok_via_twitterapi_io" if twitter_ok else twitter_status,
        "last_checked": run_date,
        "consecutive_failures": 0 if twitter_ok else 1,
        "note": "Direct X evidence is collected only through twitterapi.io; Exa MCP is not used.",
    }

    return {
        "schema_version": 1,
        "updated_at": now_local().isoformat(timespec="seconds"),
        "sources": sources,
    }


def manifest(raw, run_date):
    rss_counts = status_counts(raw["rss"].get("sources", []))
    official_counts = status_counts(raw["official"].get("sources", []))
    trending_counts = status_counts(raw["github_trending"].get("sources", []))
    github_sources = raw["github"].get("sources", [])
    github_api_status = raw["github"].get("api_status", {})
    twitter = raw["twitter"]
    twitter_status = twitter_collection_status(twitter)
    kept_total = sum(account.get("kept_count", 0) for account in twitter.get("accounts", []))
    collected_times = [
        raw["rss"].get("collected_at"),
        raw["github"].get("collected_at"),
        raw["github_trending"].get("collected_at"),
        raw["official"].get("collected_at"),
        twitter.get("collected_at"),
    ]
    collected_at = max([value for value in collected_times if value], default=now_local().isoformat(timespec="seconds"))

    return {
        "schema_version": 1,
        "run_date": run_date,
        "collected_at": collected_at,
        "timezone": "Asia/Shanghai",
        "mode": "manual_or_automation",
        "network_mode": "script_default_proxy_or_existing_env",
        "proxy": PROXY,
        "window": {
            "primary": f"{run_date} daily run with source-specific recency windows",
            "fallback": "recent feed entries when source does not expose exact 24h filtering",
        },
        "outputs": {
            "rss_items": f"daily-source-intelligence/raw/{run_date}/rss-items.json",
            "github_items": f"daily-source-intelligence/raw/{run_date}/github-items.json",
            "github_trending": f"daily-source-intelligence/raw/{run_date}/github-trending.json",
            "official_pages": f"daily-source-intelligence/raw/{run_date}/official-pages.json",
            "twitterapi_io_results": f"daily-source-intelligence/raw/{run_date}/twitterapi-io-results.json",
            "daily_report": f"daily-source-intelligence/docs/{run_date}-daily-intel.md",
        },
        "summary": {
            "rss_sources_ok": rss_counts["ok"],
            "rss_sources_failed": rss_counts["failed"],
            "github_sources_ok_via_atom": sum(1 for item in github_sources if item.get("status") == "ok"),
            "github_api_status": github_api_status.get("status"),
            "github_trending_sources_ok": trending_counts["ok"],
            "github_trending_sources_limited": trending_counts["limited"],
            "github_trending_sources_failed": trending_counts["failed"],
            "github_trending_repo_count": sum(len(source.get("items", [])) for source in raw["github_trending"].get("sources", [])),
            "official_pages_ok": official_counts["ok"],
            "official_pages_limited": official_counts["limited"],
            "official_pages_failed": official_counts["failed"],
            "twitterapi_io_used": twitter.get("status") == "ok",
            "twitterapi_io_status": twitter_status,
            "x_twitter_direct_count": kept_total,
            "x_twitter_used": twitter_status in {"ok", "partial"},
        },
        "notable_limitations": build_limitations(raw),
    }


def build_limitations(raw):
    limitations = []
    github_status = raw["github"].get("api_status", {})
    if github_status.get("status") == "failed":
        limitations.append("GitHub REST API failed or was rate-limited; GitHub releases Atom feeds were used as fallback.")
    for source in raw["official"].get("sources", []):
        if source.get("status") == "limited":
            reason = (source.get("reason") or source.get("observed_title") or "limited content").rstrip(".")
            limitations.append(f"{source.get('source_id')} limited: {reason}.")
    failed_rss = [source.get("source_id") for source in raw["rss"].get("sources", []) if source.get("status") != "ok"]
    if failed_rss:
        limitations.append(f"RSS failed sources: {', '.join(failed_rss)}.")
    for source in raw["github_trending"].get("sources", []):
        if source.get("status") == "limited":
            reason = (source.get("reason") or "limited parseable content").rstrip(".")
            limitations.append(f"{source.get('source_id')} limited: {reason}.")
        elif source.get("status") not in {"ok", "limited"}:
            limitations.append(f"{source.get('source_id')} failed: {source.get('error') or 'GitHub Trending fetch or parsing failed'}.")
    twitter = raw["twitter"]
    twitter_status = twitter_collection_status(twitter)
    if twitter_status in {"failed", "partial"}:
        failed_accounts = [account.get("handle") for account in twitter.get("accounts", []) if account.get("status") != "ok"]
        if failed_accounts:
            limitations.append(f"twitterapi.io {twitter_status}: failed accounts: {', '.join(failed_accounts)}.")
    return limitations


def stable_seen_items(raw, run_date):
    items = []
    for source in raw["rss"].get("sources", []):
        if source.get("status") != "ok":
            continue
        for item in source.get("items", []):
            url = item.get("url")
            if not url:
                continue
            if not in_daily_window(item.get("published"), run_date):
                continue
            items.append(
                {
                    "id": f"url:{url}",
                    "first_seen": run_date,
                    "source": source.get("source_id"),
                    "title": item.get("title") or url,
                    "url": url,
                    "evidence_level": "official-source" if is_official_source(source.get("source_id")) else "secondary-source",
                }
            )

    for source in raw["github"].get("sources", []):
        if source.get("status") != "ok":
            continue
        for item in source.get("items", []):
            url = item.get("url")
            if not url:
                continue
            if not in_daily_window(item.get("updated"), run_date):
                continue
            items.append(
                {
                    "id": f"url:{url}",
                    "first_seen": run_date,
                    "source": source.get("source_id"),
                    "title": item.get("title") or url,
                    "url": url,
                    "evidence_level": "official-source",
                }
            )

    for source in raw["official"].get("sources", []):
        if source.get("status") != "ok":
            continue
        source_items = source.get("items") or []
        if not source_items and source.get("url") and source.get("source_id") not in {"anthropic-news-page"}:
            source_items = [{"title": source.get("title"), "url": source.get("url"), "published": source.get("published")}]
        for item in source_items:
            url = item.get("url")
            if not url:
                continue
            if not in_daily_window(item.get("published"), run_date):
                continue
            items.append(
                {
                    "id": f"url:{url}",
                    "first_seen": run_date,
                    "source": source.get("source_id"),
                    "title": item.get("title") or url,
                    "url": url,
                    "evidence_level": "official-source",
                }
            )

    for source in raw["github_trending"].get("sources", []):
        if source.get("status") != "ok":
            continue
        for item in source.get("items", []):
            url = item.get("url")
            repo = item.get("repo")
            if not url or not repo:
                continue
            title_bits = [repo]
            trending_description = item.get("trending_description") or item.get("description")
            if trending_description:
                title_bits.append(trending_description)
            items.append(
                {
                    "id": f"github-trending:{repo}",
                    "first_seen": run_date,
                    "source": source.get("source_id"),
                    "title": " - ".join(title_bits)[:180],
                    "url": url,
                    "evidence_level": "secondary-source",
                }
            )
    return items


def is_official_source(source_id):
    return source_id in {
        "openai-blog",
        "google-deepmind-blog",
        "huggingface-blog",
        "claude-blog",
        "anthropic-news-page",
    }


def x_seen_items(raw, run_date):
    candidates = []
    for account in raw["twitter"].get("accounts", []):
        handle = account.get("handle")
        if account.get("status") != "ok":
            continue
        for tweet in account.get("tweets", []):
            tweet_id = tweet.get("id")
            url = tweet.get("url") or tweet.get("twitterUrl")
            text = tweet.get("text") or ""
            if not tweet_id or not url:
                continue
            score = tweet_score(tweet, text)
            if score < X_MIN_SCORE:
                continue
            title = compact_title(text) or f"X post by {handle}"
            candidates.append(
                {
                    "id": f"tweet:{tweet_id}",
                    "first_seen": run_date,
                    "source": f"x:{handle}",
                    "title": title,
                    "url": url,
                    "evidence_level": "direct-x",
                    "_score": score,
                }
            )
    candidates.sort(key=lambda item: (-item["_score"], item["id"]))
    selected = candidates[:X_MAX_AUTO_SEEN]
    for item in selected:
        item.pop("_score", None)
    return selected


def tweet_score(tweet, text):
    engagement = sum(int(tweet.get(key) or 0) for key in ["retweetCount", "replyCount", "likeCount", "quoteCount"])
    lowered = text.lower()
    keyword_hits = sum(1 for keyword in X_KEYWORDS if keyword.lower() in lowered)
    score = min(engagement // 25, 40) + keyword_hits * 12
    if text.strip().startswith("RT @"):
        score -= 15
    if tweet.get("isReply"):
        score -= 10
    return score


def compact_title(text):
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return ""
    return text[:120]


def update_seen(raw, run_date):
    path = STATE_ROOT / "seen.json"
    if os.environ.get("DAILY_INTEL_REBUILD_SEEN") == "1":
        payload = {"schema_version": 1, "items": []}
    else:
        payload = read_json(path, {"schema_version": 1, "items": []})
    items = payload.setdefault("items", [])
    by_id = {item.get("id"): item for item in items if item.get("id")}
    added = 0
    for item in stable_seen_items(raw, run_date) + x_seen_items(raw, run_date):
        existing = by_id.get(item["id"])
        if existing:
            existing.setdefault("url", item.get("url"))
            existing.setdefault("evidence_level", item.get("evidence_level"))
            continue
        by_id[item["id"]] = item
        items.append(item)
        added += 1
    payload["items"] = sorted(items, key=lambda item: (item.get("first_seen", ""), item.get("id", "")))
    write_json(path, payload)
    return added, len(payload["items"])


def main():
    run_date = today_from_run(os.environ.get("RUN_DATE"))
    raw = load_raw(run_date)
    if not raw["raw_dir"].exists():
        print(f"raw directory does not exist: {raw['raw_dir']}", file=sys.stderr)
        return 1

    write_json(raw["raw_dir"] / "manifest.json", manifest(raw, run_date))
    write_json(STATE_ROOT / "source-health.json", source_health(raw, run_date))
    added_seen, total_seen = update_seen(raw, run_date)

    summary = {
        "run_date": run_date,
        "manifest": str((raw["raw_dir"] / "manifest.json").relative_to(ROOT.parent)),
        "source_health": str((STATE_ROOT / "source-health.json").relative_to(ROOT.parent)),
        "seen_added": added_seen,
        "seen_total": total_seen,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
