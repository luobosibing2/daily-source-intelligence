#!/usr/bin/env python3
"""Build the derived daily signal plane from archived raw inputs.

Raw collection files remain the evidence source of truth.  This module only
normalizes, filters, and deduplicates them for downstream report preparation.
"""

import hashlib
import json
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from zoneinfo import ZoneInfo


BEIJING = ZoneInfo("Asia/Shanghai")
TRACKING_PARAMS = {
    "fbclid",
    "gclid",
    "igshid",
    "ref",
    "source",
    "si",
    "spm",
}


def read_json(path, default):
    path = Path(path)
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def compact_text(value, limit=180):
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def canonicalize_url(value):
    value = str(value or "").strip()
    if not value:
        return ""
    try:
        parts = urlsplit(value)
    except ValueError:
        return value
    if not parts.scheme or not parts.netloc:
        return value
    scheme = parts.scheme.lower()
    host = parts.hostname.lower() if parts.hostname else ""
    port = parts.port
    if port and not ((scheme == "http" and port == 80) or (scheme == "https" and port == 443)):
        host = f"{host}:{port}"
    path = parts.path or "/"
    if path != "/":
        path = path.rstrip("/")
    query = []
    for key, item_value in parse_qsl(parts.query, keep_blank_values=True):
        lowered = key.lower()
        if lowered.startswith("utm_") or lowered in TRACKING_PARAMS:
            continue
        query.append((key, item_value))
    query.sort()
    return urlunsplit((scheme, host, path, urlencode(query, doseq=True), ""))


def parse_datetime(value):
    if value in (None, ""):
        return None
    if isinstance(value, (int, float)):
        raw = float(value)
        if raw > 10_000_000_000:
            raw /= 1000
        return datetime.fromtimestamp(raw, tz=timezone.utc)
    text = str(value).strip()
    if not text:
        return None
    if text.isdigit():
        return parse_datetime(int(text))
    normalized = text[:-1] + "+00:00" if text.endswith("Z") else text
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        try:
            parsed = parsedate_to_datetime(text)
        except (TypeError, ValueError, OverflowError):
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=BEIJING)
    return parsed


def window_status(value, run_date):
    parsed = parse_datetime(value)
    if parsed is None:
        return "unknown", ""
    local = parsed.astimezone(BEIJING)
    status = "inside" if local.date() == date.fromisoformat(run_date) else "outside"
    return status, local.isoformat(timespec="seconds")


def relative_body_path(root, status, value):
    if status != "ok" or not value:
        return ""
    root = Path(root)
    path = Path(value)
    if path.is_absolute():
        try:
            path = path.relative_to(root)
        except ValueError:
            return ""
    if not (root / path).is_file():
        return ""
    return path.as_posix()


def signal_id(*, url="", tweet_id="", repo="", source_type="", title=""):
    if tweet_id:
        return f"tweet:{tweet_id}"
    if repo:
        return f"github-trending:{str(repo).lower()}"
    canonical = canonicalize_url(url)
    if canonical:
        return f"url:{canonical}"
    fallback = f"{source_type}:{compact_text(title).casefold()}"
    digest = hashlib.sha256(fallback.encode("utf-8")).hexdigest()[:20]
    return f"fallback:{digest}"


def load_seen(root, run_date):
    payload = read_json(Path(root) / "state" / "seen.json", {"items": []})
    ids = set()
    urls = set()
    for item in payload.get("items", []) or []:
        first_seen = str(item.get("first_seen") or "")[:10]
        if first_seen and first_seen >= run_date:
            continue
        item_id = str(item.get("id") or "").strip()
        canonical = canonicalize_url(item.get("url"))
        if item_id:
            ids.add(item_id)
            if item_id.startswith("url:"):
                ids.add(f"url:{canonicalize_url(item_id[4:])}")
        if canonical:
            urls.add(canonical)
            ids.add(f"url:{canonical}")
    return {"ids": ids, "urls": urls}


def is_seen(seen, item):
    if item["signal_id"] in seen["ids"]:
        return True
    canonical = item.get("canonical_url") or ""
    return bool(canonical and canonical in seen["urls"])


def make_signal(
    *,
    root,
    run_date,
    source_type,
    source_id="",
    title="",
    url="",
    tweet_id="",
    repo="",
    published_at="",
    topics=None,
    evidence_level="",
    content_status="",
    content_path="",
    score_total=0,
    score_breakdown=None,
    why_read="",
):
    canonical = canonicalize_url(url)
    status, normalized_time = window_status(published_at, run_date)
    body_path = relative_body_path(root, content_status, content_path)
    content_status = content_status or "unknown"
    if content_status == "ok" and not body_path:
        content_status = "missing"
    signal = {
        "signal_id": signal_id(
            url=canonical,
            tweet_id=tweet_id,
            repo=repo,
            source_type=source_type,
            title=title,
        ),
        "source_type": source_type,
        "source_id": source_id or "",
        "title": compact_text(title),
        "url": str(url or ""),
        "canonical_url": canonical,
        "published_at": normalized_time,
        "window_status": status,
        "topics": sorted({str(topic) for topic in (topics or []) if topic}),
        "evidence_level": evidence_level or "",
        "content": {"status": content_status, "path": body_path},
        "score": {
            "total": int(score_total or 0),
            "breakdown": score_breakdown or {},
        },
        "why_read": why_read,
    }
    signal["provenance"] = [
        {
            "source_type": source_type,
            "source_id": source_id or "",
            "url": str(url or ""),
            "evidence_level": evidence_level or "",
        }
    ]
    return signal


def merge_signal(existing, incoming):
    existing["topics"] = sorted(set(existing.get("topics", [])) | set(incoming.get("topics", [])))
    existing_score = int(existing.get("score", {}).get("total") or 0)
    incoming_score = int(incoming.get("score", {}).get("total") or 0)
    if incoming_score > existing_score:
        existing["score"] = incoming["score"]
        existing["why_read"] = incoming.get("why_read") or existing.get("why_read")
    if not existing.get("content", {}).get("path") and incoming.get("content", {}).get("path"):
        existing["content"] = incoming["content"]
    if existing.get("window_status") == "unknown" and incoming.get("window_status") == "inside":
        existing["window_status"] = "inside"
        existing["published_at"] = incoming.get("published_at") or ""
    provenance = existing.get("provenance", []) + incoming.get("provenance", [])
    unique = {}
    for item in provenance:
        key = (item.get("source_type"), item.get("source_id"), item.get("url"))
        unique[key] = item
    existing["provenance"] = list(unique.values())
    return existing


def _append(signals, signal, seen):
    if signal["window_status"] == "outside" or is_seen(seen, signal):
        return
    current = signals.get(signal["signal_id"])
    signals[signal["signal_id"]] = merge_signal(current, signal) if current else signal


def build_signals(run_date, root):
    root = Path(root)
    raw_dir = root / "raw" / run_date
    seen = load_seen(root, run_date)
    signals = {}

    rss = read_json(raw_dir / "rss-items.json", {"sources": []})
    for source in rss.get("sources", []) or []:
        for item in source.get("items", []) or []:
            relevance = item.get("relevance_status")
            if relevance not in {"matched", "always_read"}:
                continue
            status = item.get("fulltext_status") or ""
            body = relative_body_path(root, status, item.get("fulltext_path"))
            _append(
                signals,
                make_signal(
                    root=root,
                    run_date=run_date,
                    source_type="rss-fulltext",
                    source_id=source.get("source_id"),
                    title=item.get("title") or item.get("url"),
                    url=item.get("url"),
                    published_at=item.get("published"),
                    topics=item.get("matched_topics") or source.get("topics") or [],
                    evidence_level="official-source" if item.get("intelligence_department") else "secondary-source",
                    content_status=status,
                    content_path=item.get("fulltext_path"),
                    score_total=70 if relevance == "always_read" else 50,
                    score_breakdown={"relevance": 70 if relevance == "always_read" else 50},
                    why_read="read matched RSS fulltext body" if body else "boundary row: matched RSS item without readable fulltext body",
                ),
                seen,
            )

    official = read_json(raw_dir / "official-link-candidates.json", {"candidates": []})
    for item in official.get("candidates", []) or []:
        status = item.get("fulltext_status") or ""
        body = relative_body_path(root, status, item.get("fulltext_path"))
        total = int(item.get("score") or 60)
        _append(
            signals,
            make_signal(
                root=root,
                run_date=run_date,
                source_type="official-link-candidate",
                source_id=item.get("handle"),
                title=item.get("fulltext_title") or item.get("expanded_url") or item.get("tweet_url"),
                url=item.get("expanded_url") or item.get("tweet_url"),
                tweet_id="" if item.get("expanded_url") else item.get("tweet_id"),
                published_at=item.get("created_at"),
                topics=item.get("matched_topics") or ["official-link-candidate"],
                evidence_level=item.get("evidence_level") or "direct-x",
                content_status=status,
                content_path=item.get("fulltext_path"),
                score_total=total,
                score_breakdown={"official_link_candidate": total},
                why_read="read official link candidate body" if body else "boundary row: official link candidate without readable fulltext body",
            ),
            seen,
        )

    trending = read_json(raw_dir / "github-trending.json", {"sources": []})
    for source in trending.get("sources", []) or []:
        for item in source.get("items", []) or []:
            status = item.get("readme_status") or ""
            body = relative_body_path(root, status, item.get("readme_path"))
            _append(
                signals,
                make_signal(
                    root=root,
                    run_date=run_date,
                    source_type="github-trending-readme",
                    source_id=source.get("source_id"),
                    title=item.get("readme_title") or item.get("repo"),
                    url=item.get("url"),
                    repo=item.get("repo"),
                    topics=["github-trending"],
                    evidence_level="secondary-source",
                    content_status=status,
                    content_path=item.get("readme_path"),
                    score_total=35,
                    score_breakdown={"github_trending": 35},
                    why_read="read GitHub Trending README body" if body else "boundary row: GitHub Trending repo without readable README",
                ),
                seen,
            )

    github = read_json(raw_dir / "github-items.json", {"sources": []})
    for source in github.get("sources", []) or []:
        for item in source.get("items", []) or []:
            relevance = item.get("relevance_status")
            if relevance != "always_read" and not item.get("fulltext_path"):
                continue
            status = item.get("fulltext_status") or ""
            body = relative_body_path(root, status, item.get("fulltext_path"))
            total = 65 if relevance == "always_read" else 45
            _append(
                signals,
                make_signal(
                    root=root,
                    run_date=run_date,
                    source_type="github-release-body",
                    source_id=source.get("source_id"),
                    title=item.get("title") or item.get("url"),
                    url=item.get("url"),
                    published_at=item.get("updated"),
                    topics=source.get("topics") or [],
                    evidence_level="official-source",
                    content_status=status,
                    content_path=item.get("fulltext_path"),
                    score_total=total,
                    score_breakdown={"release_relevance": total},
                    why_read="read release Atom body" if body else "boundary row: release entry without readable body",
                ),
                seen,
            )

    topic_brief = read_json(raw_dir / "twitter-topic-brief.json", {"topics": []})
    tweet_items = {}
    selected_ids = set()
    for topic in topic_brief.get("topics", []) or []:
        topic_id = topic.get("id") or topic.get("label") or ""
        per_topic = {}
        for item in topic.get("items", []) or []:
            item_window, _ = window_status(item.get("created_at"), run_date)
            if item_window == "outside":
                continue
            tweet_id = str(item.get("tweet_id") or "")
            key = tweet_id or canonicalize_url(item.get("url"))
            if not key:
                continue
            current = per_topic.get(key)
            if current is None or int(item.get("score") or 0) > int(current.get("score") or 0):
                per_topic[key] = item
            aggregate = tweet_items.setdefault(key, {"item": item, "topics": set()})
            aggregate["topics"].add(topic_id)
            if int(item.get("score") or 0) > int(aggregate["item"].get("score") or 0):
                aggregate["item"] = item
        ranked = sorted(per_topic.items(), key=lambda pair: (-int(pair[1].get("score") or 0), pair[0]))
        selected_ids.update(key for key, _ in ranked[:3])

    for key in selected_ids:
        aggregate = tweet_items[key]
        item = aggregate["item"]
        total = int(item.get("score") or 0)
        _append(
            signals,
            make_signal(
                root=root,
                run_date=run_date,
                source_type="topic-direct-x",
                source_id=item.get("handle"),
                title=item.get("text_excerpt") or item.get("tweet_id"),
                url=item.get("url"),
                tweet_id=item.get("tweet_id"),
                published_at=item.get("created_at"),
                topics=aggregate["topics"],
                evidence_level=item.get("evidence_level") or "direct-x",
                content_status="n/a",
                score_total=total,
                score_breakdown={
                    "topic_brief": total,
                    "matched_keyword_count": len(item.get("matched_keywords") or []),
                },
                why_read="read structured priority X topic item; direct evidence is in twitter-topic-brief.json",
            ),
            seen,
        )

    ordered = sorted(
        signals.values(),
        key=lambda item: (-int(item["score"]["total"]), item["source_type"], item["title"]),
    )
    next_date = (date.fromisoformat(run_date) + timedelta(days=1)).isoformat()
    return {
        "schema_version": 1,
        "run_date": run_date,
        "timezone": "Asia/Shanghai",
        "window": {"start": f"{run_date}T00:00:00+08:00", "end_exclusive": f"{next_date}T00:00:00+08:00"},
        "raw_inputs": [
            f"raw/{run_date}/rss-items.json",
            f"raw/{run_date}/official-link-candidates.json",
            f"raw/{run_date}/github-trending.json",
            f"raw/{run_date}/github-items.json",
            f"raw/{run_date}/twitter-topic-brief.json",
        ],
        "signals": ordered,
        "counts": {
            "total": len(ordered),
            "inside_window": sum(1 for item in ordered if item["window_status"] == "inside"),
            "unknown_time_boundary": sum(1 for item in ordered if item["window_status"] == "unknown"),
        },
    }


def build_reading_list(signals_payload, generated_at):
    entries = []
    for signal in signals_payload.get("signals", []):
        content = signal.get("content") or {}
        entries.append(
            {
                "signal_id": signal["signal_id"],
                "source_type": signal["source_type"],
                "topic": ",".join(signal.get("topics") or []),
                "topics": signal.get("topics") or [],
                "priority": int(signal.get("score", {}).get("total") or 0),
                "score_breakdown": signal.get("score", {}).get("breakdown") or {},
                "evidence_level": signal.get("evidence_level") or "",
                "title": signal.get("title") or "",
                "url": signal.get("url") or "",
                "canonical_url": signal.get("canonical_url") or "",
                "published_at": signal.get("published_at") or "",
                "window_status": signal.get("window_status") or "unknown",
                "local_body_path": content.get("path") or "",
                "fulltext_status": content.get("status") or "",
                "why_read": signal.get("why_read") or "",
            }
        )
    return {
        "schema_version": 2,
        "run_date": signals_payload["run_date"],
        "generated_at": generated_at,
        "signals": f"raw/{signals_payload['run_date']}/signals.json",
        "entries": entries,
    }
