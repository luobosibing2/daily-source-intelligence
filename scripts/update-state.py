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

PROXY_ENV_KEYS = [
    "http_proxy",
    "https_proxy",
    "all_proxy",
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "no_proxy",
    "NO_PROXY",
]

X_KEYWORDS = [
    "agent",
    "agents",
    "ai",
    "claude",
    "codex",
    "cursor",
    "fde",
    "fdse",
    "llm",
    "mcp",
    "openclaw",
    "openai",
    "palantirization",
    "revenue",
    "saas",
    "startup",
    "vibe",
    "forward deployed",
    "forward-deployed",
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


def proxy_env_snapshot():
    return {key: redact_proxy_value(os.environ[key]) for key in PROXY_ENV_KEYS if os.environ.get(key)}


def redact_proxy_value(value):
    return re.sub(r"://[^/@]+@", "://<redacted>@", value)


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


def rss_fulltext_counts(rss_sources):
    counts = {
        "ok": 0,
        "limited": 0,
        "failed": 0,
        "skipped": 0,
        "attempted": 0,
        "matched": 0,
    }
    for source in rss_sources:
        for item in source.get("items", []):
            status = item.get("fulltext_status")
            if item.get("relevance_status") in {"matched", "always_read"}:
                counts["matched"] += 1
            if status in {"ok", "limited", "failed", "skipped"}:
                counts[status] += 1
            if status in {"ok", "limited", "failed"}:
                counts["attempted"] += 1
    return counts


def github_release_fulltext_counts(github_sources):
    counts = {
        "ok": 0,
        "limited": 0,
        "failed": 0,
        "attempted": 0,
        "always_read": 0,
    }
    for source in github_sources:
        for item in source.get("items", []):
            status = item.get("fulltext_status")
            if item.get("relevance_status") == "always_read":
                counts["always_read"] += 1
            if status in {"ok", "limited", "failed"}:
                counts[status] += 1
                counts["attempted"] += 1
    return counts


def official_article_counts(official_sources):
    counts = {
        "index_cards": 0,
        "daily_items": 0,
        "fulltext_ok": 0,
        "fulltext_limited": 0,
        "fulltext_failed": 0,
    }
    for source in official_sources:
        if source.get("source_id") != "anthropic-engineering":
            continue
        counts["index_cards"] += int(source.get("index_card_count") or 0)
        items = source.get("items", []) or []
        counts["daily_items"] += len(items)
        for item in items:
            status = item.get("fulltext_status")
            if status in {"ok", "limited", "failed"}:
                counts[f"fulltext_{status}"] += 1
    return counts


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


def current_records(payload, key, id_key):
    records = payload.get(key, []) or []
    if not payload.get("partial_update"):
        return records
    selected = set(payload.get("selected_source_ids") or [])
    return [record for record in records if record.get(id_key) in selected]


def current_sources(payload):
    return current_records(payload, "sources", "source_id")


def current_twitter(twitter):
    if not twitter.get("partial_update"):
        return twitter
    payload = dict(twitter)
    payload["accounts"] = current_records(twitter, "accounts", "account_id")
    return payload


def source_health(raw, run_date, previous=None):
    sources = {}

    for source in current_sources(raw["rss"]):
        source_id = source.get("source_id")
        if not source_id:
            continue
        if source.get("status") == "ok":
            fulltext = rss_fulltext_counts([source])
            sources[source_id] = {
                "status": "ok",
                "last_success": run_date,
                "consecutive_failures": 0,
                "note": f"{len(source.get('items', []))} feed items parsed; relevant fulltext ok={fulltext['ok']}, limited={fulltext['limited']}, failed={fulltext['failed']}.",
            }
        else:
            sources[source_id] = {
                "status": "failed",
                "last_checked": run_date,
                "consecutive_failures": 1,
                "note": source.get("error") or "RSS fetch or parsing failed.",
            }

    github_api = raw["github"].get("api_status", {})
    for source in current_sources(raw["github"]):
        source_id = source.get("source_id")
        if not source_id:
            continue
        if source.get("status") == "ok":
            fulltext = github_release_fulltext_counts([source])
            sources[source_id] = {
                "status": "ok_via_atom",
                "last_success": run_date,
                "consecutive_failures": 0,
                "api_status": github_api.get("status"),
            }
            if fulltext["attempted"]:
                sources[source_id]["note"] = (
                    f"{len(source.get('items', []))} release Atom items parsed; "
                    f"first-party release fulltext ok={fulltext['ok']}, limited={fulltext['limited']}, failed={fulltext['failed']}."
                )
        else:
            sources[source_id] = {
                "status": "failed",
                "last_checked": run_date,
                "consecutive_failures": 1,
                "note": source.get("error") or "GitHub release feed failed.",
            }

    for source in current_sources(raw["github_trending"]):
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

    for source in current_sources(raw["official"]):
        source_id = source.get("source_id")
        if not source_id:
            continue
        article_counts = official_article_counts([source])
        article_fields = {}
        if source_id == "anthropic-engineering":
            article_fields = {
                "index_status": source.get("index_status") or source.get("status") or "failed",
                "index_card_count": article_counts["index_cards"],
                "daily_item_count": article_counts["daily_items"],
                "article_fulltext_counts": {
                    "ok": article_counts["fulltext_ok"],
                    "limited": article_counts["fulltext_limited"],
                    "failed": article_counts["fulltext_failed"],
                },
            }
        if source.get("status") == "ok":
            sources[source_id] = {
                "status": "ok",
                "last_success": run_date,
                "consecutive_failures": 0,
                **article_fields,
            }
            if article_fields:
                sources[source_id]["note"] = (
                    f"{article_counts['index_cards']} index cards parsed; "
                    f"{article_counts['daily_items']} daily article items; "
                    f"fulltext ok={article_counts['fulltext_ok']}, limited={article_counts['fulltext_limited']}, "
                    f"failed={article_counts['fulltext_failed']}."
                )
        elif source.get("status") == "limited":
            sources[source_id] = {
                "status": "limited",
                "last_checked": run_date,
                "consecutive_failures": 1,
                "note": source.get("reason") or "Official page returned limited content.",
                **article_fields,
            }
        else:
            sources[source_id] = {
                "status": "failed",
                "last_checked": run_date,
                "consecutive_failures": 1,
                "note": source.get("error") or "Official page fetch failed.",
                **article_fields,
            }

    twitter = current_twitter(raw["twitter"])
    if not raw["twitter"].get("partial_update"):
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

    previous_sources = (previous or {}).get("sources", {}) or {}
    merged_sources = dict(previous_sources)
    for source_id, current in sources.items():
        previous_item = previous_sources.get(source_id, {}) or {}
        if int(current.get("consecutive_failures") or 0) > 0:
            current["consecutive_failures"] = int(previous_item.get("consecutive_failures") or 0) + 1
            if previous_item.get("last_success") and not current.get("last_success"):
                current["last_success"] = previous_item["last_success"]
        merged_sources[source_id] = current

    return {
        "schema_version": 1,
        "updated_at": now_local().isoformat(timespec="seconds"),
        "sources": merged_sources,
    }


def manifest(raw, run_date):
    rss_sources = current_sources(raw["rss"])
    github_sources = current_sources(raw["github"])
    trending_sources = current_sources(raw["github_trending"])
    official_sources = current_sources(raw["official"])
    rss_counts = status_counts(rss_sources)
    rss_fulltext = rss_fulltext_counts(rss_sources)
    github_release_fulltext = github_release_fulltext_counts(github_sources)
    official_counts = status_counts(official_sources)
    official_articles = official_article_counts(official_sources)
    trending_counts = status_counts(trending_sources)
    github_api_status = raw["github"].get("api_status", {})
    twitter = current_twitter(raw["twitter"])
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
        "network_mode": "system_network_or_existing_proxy_env",
        "proxy_env": proxy_env_snapshot(),
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
            "twitter_topic_brief": f"daily-source-intelligence/raw/{run_date}/twitter-topic-brief.json",
            "signals": f"daily-source-intelligence/raw/{run_date}/signals.json",
            "daily_report": f"daily-source-intelligence/docs/{run_date}-daily-intel.md",
        },
        "summary": {
            "rss_sources_ok": rss_counts["ok"],
            "rss_sources_failed": rss_counts["failed"],
            "rss_fulltext_matched": rss_fulltext["matched"],
            "rss_fulltext_attempted": rss_fulltext["attempted"],
            "rss_fulltext_ok": rss_fulltext["ok"],
            "rss_fulltext_limited": rss_fulltext["limited"],
            "rss_fulltext_failed": rss_fulltext["failed"],
            "rss_fulltext_skipped": rss_fulltext["skipped"],
            "github_sources_ok_via_atom": sum(1 for item in github_sources if item.get("status") == "ok"),
            "github_api_status": github_api_status.get("status"),
            "github_release_fulltext_always_read": github_release_fulltext["always_read"],
            "github_release_fulltext_attempted": github_release_fulltext["attempted"],
            "github_release_fulltext_ok": github_release_fulltext["ok"],
            "github_release_fulltext_limited": github_release_fulltext["limited"],
            "github_release_fulltext_failed": github_release_fulltext["failed"],
            "github_trending_sources_ok": trending_counts["ok"],
            "github_trending_sources_limited": trending_counts["limited"],
            "github_trending_sources_failed": trending_counts["failed"],
            "github_trending_repo_count": sum(len(source.get("items", [])) for source in trending_sources),
            "official_pages_ok": official_counts["ok"],
            "official_pages_limited": official_counts["limited"],
            "official_pages_failed": official_counts["failed"],
            "official_page_index_cards": official_articles["index_cards"],
            "official_page_article_items": official_articles["daily_items"],
            "official_page_article_fulltext_ok": official_articles["fulltext_ok"],
            "official_page_article_fulltext_limited": official_articles["fulltext_limited"],
            "official_page_article_fulltext_failed": official_articles["fulltext_failed"],
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
    for source in current_sources(raw["official"]):
        if source.get("status") == "limited":
            reason = (source.get("reason") or source.get("observed_title") or "limited content").rstrip(".")
            limitations.append(f"{source.get('source_id')} limited: {reason}.")
        limited_items = [
            item.get("title") or item.get("url")
            for item in source.get("items", []) or []
            if item.get("fulltext_status") in {"limited", "failed"}
        ]
        if limited_items:
            sample = "; ".join(limited_items[:3])
            more = f" (+{len(limited_items) - 3} more)" if len(limited_items) > 3 else ""
            limitations.append(
                f"{source.get('source_id')} official article fulltext limited/failed for "
                f"{len(limited_items)} item(s): {sample}{more}."
            )
    failed_rss = [source.get("source_id") for source in current_sources(raw["rss"]) if source.get("status") != "ok"]
    if failed_rss:
        limitations.append(f"RSS failed sources: {', '.join(failed_rss)}.")
    for source in current_sources(raw["rss"]):
        limited_items = [
            item.get("title") or item.get("url")
            for item in source.get("items", [])
            if item.get("fulltext_status") in {"limited", "failed"}
        ]
        if limited_items:
            sample = "; ".join(limited_items[:3])
            more = f" (+{len(limited_items) - 3} more)" if len(limited_items) > 3 else ""
            limitations.append(f"{source.get('source_id')} RSS fulltext limited/failed for {len(limited_items)} matched item(s): {sample}{more}.")
    for source in current_sources(raw["github"]):
        limited_items = [
            item.get("title") or item.get("url")
            for item in source.get("items", [])
            if item.get("fulltext_status") in {"limited", "failed"}
        ]
        if limited_items:
            sample = "; ".join(limited_items[:3])
            more = f" (+{len(limited_items) - 3} more)" if len(limited_items) > 3 else ""
            limitations.append(f"{source.get('source_id')} release fulltext limited/failed for {len(limited_items)} first-party item(s): {sample}{more}.")
    for source in current_sources(raw["github_trending"]):
        if source.get("status") == "limited":
            reason = (source.get("reason") or "limited parseable content").rstrip(".")
            limitations.append(f"{source.get('source_id')} limited: {reason}.")
        elif source.get("status") not in {"ok", "limited"}:
            limitations.append(f"{source.get('source_id')} failed: {source.get('error') or 'GitHub Trending fetch or parsing failed'}.")
    twitter = current_twitter(raw["twitter"])
    twitter_status = twitter_collection_status(twitter)
    if twitter_status in {"failed", "partial"}:
        failed_accounts = [account.get("handle") for account in twitter.get("accounts", []) if account.get("status") != "ok"]
        if failed_accounts:
            limitations.append(f"twitterapi.io {twitter_status}: failed accounts: {', '.join(failed_accounts)}.")
    return limitations


def stable_seen_items(raw, run_date):
    items = []
    for source in current_sources(raw["rss"]):
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

    for source in current_sources(raw["github"]):
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

    for source in current_sources(raw["official"]):
        if source.get("status") != "ok":
            continue
        source_items = source.get("items") or []
        if not source_items and source.get("url") and source.get("source_id") not in {
            "anthropic-news-page",
            "anthropic-engineering",
        }:
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

    for source in current_sources(raw["github_trending"]):
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
        "palantir-blog",
        "ramp-builders",
        "a16z-news",
    }


def x_seen_items(raw, run_date):
    candidates = []
    for account in current_twitter(raw["twitter"]).get("accounts", []):
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
    health_path = STATE_ROOT / "source-health.json"
    previous_health = read_json(health_path, {"sources": {}})
    write_json(health_path, source_health(raw, run_date, previous=previous_health))
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
