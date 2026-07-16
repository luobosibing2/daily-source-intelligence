#!/usr/bin/env python3
import argparse
import importlib.util
import json
import re
import sys
import urllib.parse
from datetime import datetime
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "raw"
SOURCES = ROOT / "config" / "sources.yaml"

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


DEFAULT_CONFIG = {
    "enabled": False,
    "official_domains": [],
    "strong_keywords": [],
    "min_score": 20,
}


def read_json(path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_sources(root):
    path = root / "config" / "sources.yaml"
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def candidate_config(sources):
    config = dict(DEFAULT_CONFIG)
    config.update(sources.get("official_link_candidates") or {})
    config["official_domains"] = [normalize_domain(item) for item in config.get("official_domains", [])]
    config["strong_keywords"] = [str(item) for item in config.get("strong_keywords", [])]
    config["min_score"] = int(config.get("min_score") or 20)
    return config


def priority_handles(sources):
    handles = {}
    for account in sources.get("x_accounts", []) or []:
        if account.get("enabled") is True and account.get("priority") is True and account.get("handle"):
            handles[str(account["handle"]).lower()] = account
    return handles


def normalize_domain(value):
    value = str(value or "").strip().lower()
    if not value:
        return ""
    parsed = urllib.parse.urlparse(value if "://" in value else f"https://{value}")
    return parsed.netloc.lower().split("@")[-1].split(":")[0]


def domain_matches(domain, allowed_domains):
    domain = normalize_domain(domain)
    for allowed in allowed_domains:
        if not allowed:
            continue
        if domain == allowed or domain.endswith(f".{allowed}"):
            return True
    return False


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


def collect_string_values(value):
    if isinstance(value, dict):
        results = []
        for key, child in value.items():
            if key == "string_value" and isinstance(child, str):
                results.append(child)
            else:
                results.extend(collect_string_values(child))
        return results
    if isinstance(value, list):
        results = []
        for child in value:
            results.extend(collect_string_values(child))
        return results
    return []


def tweet_text_for_matching(tweet):
    parts = [tweet.get("text") or ""]
    parts.extend(collect_string_values(tweet.get("card") or {}))
    return "\n".join(part for part in parts if part)


def strong_keyword_hits(text, keywords):
    lowered = text.lower()
    return [keyword for keyword in keywords if keyword.lower() in lowered]


def expanded_urls(tweet):
    urls = []
    for item in ((tweet.get("entities") or {}).get("urls") or []):
        url = item.get("expanded_url") or item.get("expandedUrl") or item.get("url")
        if url:
            urls.append(url)
    return sorted(set(urls))


def safe_slug(value):
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip("-").lower()
    return slug[:120] or "official-link"


def candidate_stem(handle, tweet_id, url):
    parsed = urllib.parse.urlparse(url)
    name = Path(parsed.path).name or parsed.netloc or "official-link"
    return safe_slug(f"{handle}-{tweet_id}-{name}")


def load_collect_stable_sources():
    path = ROOT / "scripts" / "collect-stable-sources.py"
    spec = importlib.util.spec_from_file_location("collect_stable_sources", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def default_fetcher(url, output_dir, stem):
    module = load_collect_stable_sources()
    if len(output_dir.parents) >= 3:
        module.ROOT = output_dir.parents[2]
        module.RAW_ROOT = module.ROOT / "raw"
    return module.fetch_readable_page(url, output_dir, stem)


def build_candidate(account, tweet, expanded_url, config, fetcher, root, run_date):
    text = tweet_text_for_matching(tweet)
    score = tweet_score(tweet, text)
    hits = strong_keyword_hits(text, config["strong_keywords"])
    trigger_reasons = []
    if score >= config["min_score"]:
        trigger_reasons.append(f"score>={config['min_score']}")
    if hits:
        trigger_reasons.append(f"strong_keyword:{','.join(hits)}")
    if not trigger_reasons:
        return None

    parsed = urllib.parse.urlparse(expanded_url)
    domain = normalize_domain(parsed.netloc)
    if not parsed.scheme.startswith("http") or not domain_matches(domain, config["official_domains"]):
        return None

    handle = account.get("handle") or ""
    tweet_id = tweet.get("id") or tweet.get("tweet_id") or ""
    stem = candidate_stem(handle, tweet_id, expanded_url)
    fetch_result = fetcher(expanded_url, root / "raw" / run_date / "official-link-candidates", stem) or {}
    candidate = {
        "handle": handle,
        "tweet_id": tweet_id,
        "tweet_url": tweet.get("url") or tweet.get("twitterUrl"),
        "score": score,
        "trigger_reason": "; ".join(trigger_reasons),
        "matched_strong_keywords": hits,
        "expanded_url": expanded_url,
        "domain": domain,
        "evidence_level": "direct-x",
        "fulltext_status": fetch_result.get("fulltext_status", "failed"),
    }
    for key, value in fetch_result.items():
        if key.startswith("fulltext_") or key in {"raw_html_path", "fallback_reason", "opencli_attempts"}:
            candidate[key] = value
    return candidate


def generate_candidates(run_date, root=ROOT, fetcher=None):
    root = Path(root)
    sources = load_sources(root)
    config = candidate_config(sources)
    fetcher = fetcher or default_fetcher
    payload = {
        "schema_version": 1,
        "run_date": run_date,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "status": "ok" if config.get("enabled") else "disabled",
        "candidates": [],
    }
    if not config.get("enabled"):
        write_json(root / "raw" / run_date / "official-link-candidates.json", payload)
        return payload

    handles = priority_handles(sources)
    twitter = read_json(root / "raw" / run_date / "twitterapi-io-results.json", {"accounts": []})
    seen = set()
    for account in twitter.get("accounts", []):
        if account.get("status") != "ok":
            continue
        handle = str(account.get("handle") or "").lower()
        if handle not in handles:
            continue
        configured_account = handles[handle]
        for tweet in account.get("tweets", []):
            for url in expanded_urls(tweet):
                key = (tweet.get("id") or tweet.get("tweet_id"), url)
                if key in seen:
                    continue
                seen.add(key)
                candidate = build_candidate(configured_account, tweet, url, config, fetcher, root, run_date)
                if candidate:
                    payload["candidates"].append(candidate)

    payload["candidates"].sort(key=lambda item: (-int(item.get("score") or 0), item.get("expanded_url") or ""))
    write_json(root / "raw" / run_date / "official-link-candidates.json", payload)
    return payload


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate official-link candidates from priority X account URLs.")
    parser.add_argument("--date", required=True)
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args(argv)
    payload = generate_candidates(args.date, root=Path(args.root))
    if args.stdout:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
