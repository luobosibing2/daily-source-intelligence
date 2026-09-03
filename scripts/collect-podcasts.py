#!/usr/bin/env python3
"""Collect follow-builders podcast transcripts without audio or ASR."""

import argparse
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import parse_qs, urljoin, urlparse
from zoneinfo import ZoneInfo

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "sources.yaml"
RAW_ROOT = ROOT / "raw"
BEIJING = ZoneInfo("Asia/Shanghai")
DEFAULT_TIMEOUT_SECONDS = 45
DEFAULT_TRANSCRIPT_MIN_CHARS = 240
FEED_SNAPSHOT_NAME = "feed-podcasts.json"


def now_beijing():
    return datetime.now(BEIJING).isoformat(timespec="seconds")


def read_json(path, default):
    path = Path(path)
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_bytes(body):
    return hashlib.sha256(body).hexdigest()


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def relative_path(root, path):
    return str(Path(path).resolve().relative_to(Path(root).resolve()))


def safe_slug(value, fallback="episode"):
    value = str(value or "").lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return (value[:80].rstrip("-") or fallback)


def fetch_url(url, timeout=DEFAULT_TIMEOUT_SECONDS):
    """Fetch only the requested text endpoint; never follows an enclosure URL."""

    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json, text/plain, application/rss+xml, application/atom+xml, */*",
            "User-Agent": "daily-source-intelligence/podcast-collector",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read()
            return {
                "ok": True,
                "status": int(getattr(response, "status", 200) or 200),
                "body": body,
                "content_type": response.headers.get("Content-Type", ""),
            }
    except urllib.error.HTTPError as exc:
        body = exc.read() if hasattr(exc, "read") else b""
        return {
            "ok": False,
            "status": int(exc.code),
            "body": body,
            "error": f"HTTP {exc.code}: {exc.reason}",
        }
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"ok": False, "status": 0, "body": b"", "error": str(exc)}


def load_sources(root=ROOT):
    config_path = Path(root) / "config" / "sources.yaml"
    config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    configured = config.get("podcasts") or []
    if isinstance(configured, dict):
        configured = [configured]
    return [source for source in configured if source.get("enabled", True)]


def enabled_shows(source):
    return [show for show in source.get("shows", []) or [] if show.get("enabled", True)]


def normalize_name(value):
    value = str(value or "").strip().lower()
    value = value.replace("&", "and")
    return re.sub(r"[^a-z0-9]+", "", value)


def show_index(source):
    index = {}
    for show in enabled_shows(source):
        names = [show.get("name"), show.get("id")]
        names.extend(show.get("aliases", []) or [])
        for name in names:
            key = normalize_name(name)
            if key:
                index[key] = show
    return index


def parse_datetime(value):
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        try:
            return datetime.fromtimestamp(value, tz=timezone.utc)
        except (ValueError, OverflowError, OSError):
            return None
    text = str(value).strip()
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        try:
            parsed = parsedate_to_datetime(text)
        except (TypeError, ValueError, IndexError, OverflowError):
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def window_status(value, run_date):
    parsed = parse_datetime(value)
    if parsed is None:
        return "unknown"
    try:
        target = date.fromisoformat(str(run_date))
    except ValueError:
        return "unknown"
    return "inside" if parsed.astimezone(BEIJING).date() == target else "outside"


def beijing_window_status(value, run_date):
    """Explicit alias for callers that want the timezone contract in the name."""

    return window_status(value, run_date)


def normalize_guid(value):
    return str(value or "").strip()


def is_episode_url(url):
    if not url:
        return False
    try:
        parsed = urlparse(str(url).strip())
    except ValueError:
        return False
    host = parsed.netloc.lower().split(":", 1)[0]
    path = parsed.path.lower()
    query = parse_qs(parsed.query)
    if host in {"youtu.be", "youtube.com", "www.youtube.com", "m.youtube.com"}:
        return bool(query.get("v")) and not query.get("list")
    if "podcasters.spotify.com" in host or host.endswith("anchor.fm"):
        return "/episode/" in path or "/episodes/" in path
    if "podcasts.apple.com" in host:
        return bool(query.get("i")) or "/podcast/" in path and path.rsplit("/", 1)[-1].startswith("id")
    return "/episode/" in path or "/episodes/" in path


def xml_local_name(tag):
    return str(tag or "").rsplit("}", 1)[-1].lower()


def child_text(node, names):
    names = {name.lower() for name in names}
    for child in list(node):
        if xml_local_name(child.tag) not in names:
            continue
        text = (child.text or "").strip()
        if text:
            return text
        href = (child.attrib.get("href") or "").strip()
        if href:
            return href
    return ""


def rss_episode_link(xml_body, guid):
    """Return the page link for the item whose GUID exactly matches ``guid``."""

    try:
        root = ET.fromstring(xml_body)
    except (ET.ParseError, TypeError):
        return ""
    expected = normalize_guid(guid)
    if not expected:
        return ""
    for node in root.iter():
        if xml_local_name(node.tag) not in {"item", "entry"}:
            continue
        node_guid = child_text(node, {"guid", "id"})
        if normalize_guid(node_guid) != expected:
            continue
        links = []
        for child in list(node):
            if xml_local_name(child.tag) != "link":
                continue
            rel = (child.attrib.get("rel") or "alternate").lower()
            if rel == "enclosure":
                continue
            link = (child.text or "").strip() or (child.attrib.get("href") or "").strip()
            if link:
                links.append(link)
        return links[0] if links else ""
    return ""


def resolve_episode_link(upstream_url, guid, show, fetcher=fetch_url):
    """Resolve canonical URL without guessing and without touching audio enclosures."""

    upstream_url = str(upstream_url or "").strip()
    if is_episode_url(upstream_url):
        return {
            "canonical_url": upstream_url,
            "upstream_url": upstream_url,
            "link_status": "ok",
            "link_method": "upstream-episode-url",
        }

    rss_url = str(show.get("rss_url") or show.get("rssUrl") or "").strip()
    if not rss_url:
        return {
            "canonical_url": "",
            "upstream_url": upstream_url,
            "link_status": "limited",
            "link_method": "no-configured-rss",
            "link_error": "No RSS URL configured for this show.",
        }
    fetched = fetcher(rss_url)
    if not fetched.get("ok"):
        return {
            "canonical_url": "",
            "upstream_url": upstream_url,
            "link_status": "limited",
            "link_method": "rss-guid-match",
            "link_error": fetched.get("error") or f"RSS fetch failed with status {fetched.get('status')}",
            "rss_url": rss_url,
        }
    link = rss_episode_link(fetched.get("body", b""), guid)
    if not link:
        return {
            "canonical_url": "",
            "upstream_url": upstream_url,
            "link_status": "limited",
            "link_method": "rss-guid-match",
            "link_error": "No RSS episode matched the GUID exactly.",
            "rss_url": rss_url,
        }
    return {
        "canonical_url": urljoin(rss_url, link),
        "upstream_url": upstream_url,
        "link_status": "ok",
        "link_method": "rss-guid-match",
        "rss_url": rss_url,
    }


def transcript_text(value):
    if value is None:
        return ""
    if isinstance(value, str):
        return value.replace("\r\n", "\n").replace("\r", "\n").strip()
    return ""


def write_transcript(root, run_date, source_id, episode, transcript):
    digest = sha256_text(episode["episode_id"])[:12]
    stem = f"{safe_slug(episode.get('title'), 'episode')}-{digest}.md"
    path = Path(root) / "raw" / str(run_date) / "podcasts" / safe_slug(source_id) / "transcripts" / stem
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(transcript + "\n", encoding="utf-8")
    return relative_path(root, path)


def normalize_episode(raw, source, run_date, root, show_by_name, fetcher=fetch_url, min_chars=DEFAULT_TRANSCRIPT_MIN_CHARS):
    raw = raw if isinstance(raw, dict) else {}
    show_name = str(
        raw.get("name")
        or raw.get("show_name")
        or raw.get("showName")
        or raw.get("show_id")
        or raw.get("showId")
        or ""
    ).strip()
    configured_show = show_by_name.get(normalize_name(show_name))
    show_id = str((configured_show or {}).get("id") or "").strip()
    show_name_canonical = str((configured_show or {}).get("name") or show_name).strip()
    guid = normalize_guid(raw.get("guid") or raw.get("id"))
    title = str(raw.get("title") or "").strip()
    published_at = raw.get("publishedAt") or raw.get("published_at") or raw.get("published") or ""
    upstream_url = str(raw.get("url") or "").strip()
    transcript = transcript_text(raw.get("transcript"))
    allowed = bool(configured_show and guid)
    episode_id = f"podcast:{show_id}:{guid}" if allowed else ""
    status = window_status(published_at, run_date)
    topics = list((configured_show or {}).get("topics") or source.get("topics") or [])

    episode = {
        "episode_id": episode_id,
        "show_id": show_id,
        "show_name": show_name_canonical,
        "guid": guid,
        "title": title,
        "published_at": published_at,
        "window_status": status,
        "transcript_status": "ok" if len(transcript) >= min_chars else "limited",
        "transcript_path": "",
        "transcript_sha256": sha256_text(transcript) if transcript else "",
        "transcript_chars": len(transcript),
        "transcript_provider": source.get("provider") or "follow-builders",
        "transcript_method": "aggregator-transcript",
        "canonical_url": "",
        "upstream_url": upstream_url,
        "link_status": "limited",
        "topics": topics,
        "allowed": allowed,
        "speaker_coverage": bool(re.search(r"(?im)^\s*(speaker|host|guest)\b", transcript)),
        "timestamp_coverage": bool(re.search(r"(?im)\b\d{1,2}:\d{2}(?::\d{2})?\b", transcript)),
    }

    if not configured_show:
        episode["episode_status"] = "unconfigured"
        episode["transcript_status"] = "limited" if transcript else "limited"
        episode["link_status"] = "limited"
        episode["link_error"] = "Show is not in the local allowlist."
        return episode
    if not guid:
        episode["episode_status"] = "limited"
        episode["transcript_status"] = "limited"
        episode["link_error"] = "Episode has no GUID; it cannot become a stable identity."
        return episode

    episode["episode_status"] = "ok" if episode["transcript_status"] == "ok" else "limited"
    if not transcript:
        episode["transcript_error"] = "Transcript is missing from the upstream feed."
    elif episode["transcript_status"] == "limited":
        episode["transcript_error"] = f"Transcript is shorter than the {min_chars}-character readability threshold."
    # Keep the body private until duplicate identities have been reduced.  Writing
    # here would allow a shorter duplicate to overwrite the winner's transcript
    # file while the winner's hash and character count still describe the longer
    # record.
    if transcript:
        episode["_transcript_body"] = transcript
    episode.update(resolve_episode_link(upstream_url, guid, configured_show, fetcher=fetcher))
    return episode


def deduplicate_episodes(episodes):
    """Keep one record per formal identity, preferring the most complete transcript."""

    by_id = {}
    passthrough = []
    for episode in episodes:
        episode_id = episode.get("episode_id")
        if not episode_id:
            passthrough.append(episode)
            continue
        current = by_id.get(episode_id)
        if current is None or int(episode.get("transcript_chars") or 0) > int(current.get("transcript_chars") or 0):
            by_id[episode_id] = episode
    return list(by_id.values()) + passthrough


def empty_coverage():
    return {
        "offered": 0,
        "allowed": 0,
        "inside": 0,
        "outside": 0,
        "unknown": 0,
        "transcript_ok": 0,
        "transcript_limited": 0,
        "link_ok": 0,
        "link_limited": 0,
        "upstream_error_count": 0,
        "unconfigured": 0,
        "missing_guid": 0,
    }


def build_coverage(episodes, offered, errors):
    coverage = empty_coverage()
    coverage["offered"] = int(offered)
    coverage["upstream_error_count"] = len(errors)
    for episode in episodes:
        if not episode.get("allowed"):
            if episode.get("episode_status") == "unconfigured":
                coverage["unconfigured"] += 1
            if not episode.get("guid"):
                coverage["missing_guid"] += 1
            continue
        coverage["allowed"] += 1
        status = episode.get("window_status") or "unknown"
        coverage[status] = coverage.get(status, 0) + 1
        transcript_status = episode.get("transcript_status")
        if transcript_status == "ok":
            coverage["transcript_ok"] += 1
        else:
            coverage["transcript_limited"] += 1
        if episode.get("link_status") == "ok":
            coverage["link_ok"] += 1
        else:
            coverage["link_limited"] += 1
    return coverage


def normalize_errors(value):
    if value in (None, "", []):
        return []
    if isinstance(value, list):
        return [item if isinstance(item, str) else json.dumps(item, ensure_ascii=False, sort_keys=True) for item in value]
    if isinstance(value, dict):
        return [json.dumps(value, ensure_ascii=False, sort_keys=True)]
    return [str(value)]


def collect_source(source, run_date, root=ROOT, fetcher=fetch_url, min_chars=DEFAULT_TRANSCRIPT_MIN_CHARS):
    root = Path(root)
    source_id = str(source.get("id") or "follow-builders")
    source_url = str(source.get("url") or source.get("feed_url") or "").strip()
    output_dir = root / "raw" / str(run_date)
    snapshot_path = output_dir / "podcasts" / safe_slug(source_id) / FEED_SNAPSHOT_NAME
    fetched = fetcher(source_url)
    body = fetched.get("body", b"")
    if isinstance(body, str):
        body = body.encode("utf-8")
    if body:
        snapshot_path.parent.mkdir(parents=True, exist_ok=True)
        snapshot_path.write_bytes(body)

    base = {
        "schema_version": 1,
        "run_date": str(run_date),
        "source_id": source_id,
        "source_name": source.get("name") or source_id,
        "feed_url": source_url,
        "collected_at": now_beijing(),
        "upstream_generated_at": "",
        "lookback_hours": None,
        "errors": [],
        "coverage": empty_coverage(),
        "episodes": [],
        "raw_feed_path": relative_path(root, snapshot_path) if body else "",
        "raw_feed_sha256": sha256_bytes(body) if body else "",
        "http_status": fetched.get("status") or 0,
        "provider": source.get("provider") or "follow-builders",
        "transcript_policy": "aggregator-transcript-only-no-asr",
    }

    if not fetched.get("ok"):
        base["status"] = "failed"
        base["errors"] = [fetched.get("error") or f"Feed fetch failed with status {fetched.get('status')}."]
        return base

    try:
        payload = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        base["status"] = "failed"
        base["errors"] = [f"Invalid JSON feed: {exc}"]
        return base
    if not isinstance(payload, dict) or not isinstance(payload.get("podcasts"), list):
        base["status"] = "failed"
        base["errors"] = ["Feed schema is missing a podcasts array."]
        return base

    base["upstream_generated_at"] = payload.get("generatedAt") or payload.get("generated_at") or ""
    base["lookback_hours"] = payload.get("lookbackHours") or payload.get("lookback_hours")
    errors = normalize_errors(payload.get("errors"))
    show_by_name = show_index(source)
    episodes = [
        normalize_episode(item, source, run_date, root, show_by_name, fetcher=fetcher, min_chars=min_chars)
        for item in payload.get("podcasts", [])
    ]
    episodes = deduplicate_episodes(episodes)
    for episode in episodes:
        transcript = episode.pop("_transcript_body", "")
        if transcript and episode.get("episode_id"):
            episode["transcript_path"] = write_transcript(
                root,
                run_date,
                source.get("id", "follow-builders"),
                episode,
                transcript,
            )
    base["episodes"] = episodes
    base["errors"] = errors
    base["coverage"] = build_coverage(episodes, len(payload.get("podcasts", [])), errors)
    base["status"] = "partial" if errors else "ok"
    return base


def select_sources(sources, selected_ids):
    if not selected_ids:
        return sources
    by_id = {str(source.get("id")): source for source in sources}
    missing = sorted(set(selected_ids) - set(by_id))
    if missing:
        raise ValueError(f"unknown or disabled podcast source(s): {', '.join(missing)}")
    return [by_id[source_id] for source_id in selected_ids]


def merge_selected_source(path, payload, selected_ids):
    """Preserve other configured aggregators if targeted collection is ever added."""

    if not selected_ids or not Path(path).exists():
        return payload
    previous = read_json(path, {})
    previous_source_id = previous.get("source_id")
    if previous_source_id and previous_source_id not in selected_ids:
        return previous
    return payload


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=False)
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--source", action="append", default=[], help="configured podcast aggregator id")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    run_date = args.date or datetime.now(BEIJING).date().isoformat()
    sources = select_sources(load_sources(root), args.source)
    if args.dry_run:
        print(json.dumps({
            "event": "podcast_collection_plan",
            "run_date": run_date,
            "sources": [source.get("id") for source in sources],
            "feed_urls": [source.get("url") for source in sources],
            "transcript_policy": "aggregator-transcript-only-no-asr",
            "audio_download": False,
        }, ensure_ascii=False, indent=2))
        return 0
    output_dir = root / "raw" / str(run_date)
    output_dir.mkdir(parents=True, exist_ok=True)
    payloads = [collect_source(source, run_date, root=root) for source in sources]
    if len(payloads) == 1:
        payload = payloads[0]
    else:
        # The current configuration has one aggregator. Keep a deterministic wrapper
        # for future sources without changing the per-source episode contract.
        payload = {
            "schema_version": 1,
            "run_date": run_date,
            "source_id": "multiple",
            "source_name": "Configured podcast transcript feeds",
            "feed_url": "",
            "collected_at": now_beijing(),
            "upstream_generated_at": "",
            "lookback_hours": None,
            "errors": [error for item in payloads for error in item.get("errors", [])],
            "coverage": empty_coverage(),
            "episodes": [episode for item in payloads for episode in item.get("episodes", [])],
            "raw_feed_path": "",
            "raw_feed_sha256": "",
            "provider": "follow-builders",
            "transcript_policy": "aggregator-transcript-only-no-asr",
            "status": "partial" if any(item.get("status") != "ok" for item in payloads) else "ok",
        }
        payload["coverage"] = build_coverage(payload["episodes"], sum(item.get("coverage", {}).get("offered", 0) for item in payloads), payload["errors"])
    write_json(output_dir / "podcast-items.json", payload)
    print(json.dumps({
        "run_date": run_date,
        "status": payload.get("status"),
        "source_id": payload.get("source_id"),
        "episodes": len(payload.get("episodes", [])),
        "coverage": payload.get("coverage", {}),
    }, ensure_ascii=False, indent=2))
    return 1 if payload.get("status") == "failed" else 0


if __name__ == "__main__":
    sys.exit(main())
