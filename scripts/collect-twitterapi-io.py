#!/usr/bin/env python3
import json
import os
import subprocess
import sys
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from email.utils import parsedate_to_datetime
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "config" / "sources.yaml"
RAW_ROOT = ROOT / "raw"
LOCAL_ENV = ROOT / ".env.local"


def load_local_env():
    if not LOCAL_ENV.exists():
        return
    for raw in LOCAL_ENV.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def fail(message, output_path=None):
    payload = {
        "schema_version": 1,
        "provider": "twitterapi.io",
        "status": "skipped",
        "reason": message,
        "accounts": [],
    }
    if output_path:
        output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


def get_api_key():
    load_local_env()
    key = os.environ.get("TWITTERAPI_IO_KEY")
    if key:
        return key

    service = os.environ.get("TWITTERAPI_IO_KEYCHAIN_SERVICE", "twitterapi.io")
    account = os.environ.get("TWITTERAPI_IO_KEYCHAIN_ACCOUNT") or os.environ.get("USER")
    if not account:
        return None

    try:
        key = subprocess.check_output(
            ["security", "find-generic-password", "-a", account, "-s", service, "-w"],
            stderr=subprocess.DEVNULL,
            timeout=5,
        ).decode("utf-8").strip()
        return key or None
    except Exception:
        return None


def parse_accounts():
    accounts = []
    in_accounts = False
    current = None
    for raw in SOURCES.read_text().splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if stripped == "x_accounts:":
            in_accounts = True
            continue
        if in_accounts and stripped and not raw.startswith(" ") and not raw.startswith("-"):
            break
        if not in_accounts:
            continue
        if stripped.startswith("- id:"):
            if current:
                accounts.append(current)
            current = {"id": stripped.split(":", 1)[1].strip()}
            continue
        if current and ":" in stripped:
            key, value = stripped.split(":", 1)
            value = value.strip()
            if value in ("true", "false"):
                value = value == "true"
            current[key] = value
    if current:
        accounts.append(current)
    return [a for a in accounts if a.get("enabled") is True and a.get("handle")]


def curl_json(url, api_key):
    cmd = [
        "curl",
        "-sS",
        "--max-time",
        "30",
        "--get",
        url,
        "--header",
        f"X-API-Key: {api_key}",
    ]
    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=40,
            check=False,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError("curl timed out") from None

    text = proc.stdout.decode("utf-8", errors="replace")
    if proc.returncode != 0:
        stderr = proc.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"curl failed with exit_code={proc.returncode}; stderr={stderr}") from None

    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"invalid JSON response: {exc}") from None


def extract_tweets(data):
    if isinstance(data, dict):
        if isinstance(data.get("tweets"), list):
            return data["tweets"]
        nested = data.get("data")
        if isinstance(nested, dict) and isinstance(nested.get("tweets"), list):
            return nested["tweets"]
    return []


def response_status(data):
    if not isinstance(data, dict):
        return {}
    return {
        "status": data.get("status"),
        "message": data.get("message") or data.get("msg"),
        "has_more": data.get("has_next_page") or data.get("hasMore"),
    }


def classify_response(data):
    meta = response_status(data)
    message = (meta.get("message") or "").lower()
    if meta.get("status") == "success":
        return "ok"
    if "qps" in message or "rate" in message or "limit" in message:
        return "rate_limited"
    if meta.get("message"):
        return "failed"
    return "ok"


def parse_created_at(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except Exception:
        pass
    try:
        return parsedate_to_datetime(value)
    except Exception:
        return None


def get_last_tweets(handle, api_key):
    params = urllib.parse.urlencode({"userName": handle, "includeReplies": "false"})
    url = f"https://api.twitterapi.io/twitter/user/last_tweets?{params}"
    return curl_json(url, api_key)


def collect_account(account, api_key, since):
    handle = account["handle"]
    try:
        data = get_last_tweets(handle, api_key)
        tweets = extract_tweets(data)
        kept = []
        for tweet in tweets:
            created_dt = parse_created_at(tweet.get("createdAt"))
            keep = created_dt is None or created_dt >= since
            if keep:
                kept.append(tweet)
        status = classify_response(data)
        return {
            "account_id": account.get("id"),
            "name": account.get("name"),
            "handle": handle,
            "status": status,
            "response": response_status(data),
            "raw_count": len(tweets),
            "kept_count": len(kept),
            "tweets": kept,
        }
    except Exception as exc:
        return {
            "account_id": account.get("id"),
            "name": account.get("name"),
            "handle": handle,
            "status": "failed",
            "error": repr(exc),
            "tweets": [],
        }


def main():
    run_date = os.environ.get("RUN_DATE") or datetime.now().strftime("%Y-%m-%d")
    output_dir = RAW_ROOT / run_date
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "twitterapi-io-results.json"

    api_key = get_api_key()
    if not api_key:
        return fail("TWITTERAPI_IO_KEY is not set and macOS Keychain fallback did not return a key", output_path)

    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=int(os.environ.get("TWITTERAPI_IO_WINDOW_HOURS", "36")))
    accounts = parse_accounts()
    request_interval = float(os.environ.get("TWITTERAPI_IO_REQUEST_INTERVAL_SECONDS", "0"))
    max_workers = max(1, int(os.environ.get("TWITTERAPI_IO_MAX_WORKERS", "5")))

    indexed_results = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        for index, account in enumerate(accounts):
            if index > 0 and request_interval > 0:
                time.sleep(request_interval)
            future = executor.submit(collect_account, account, api_key, since)
            futures[future] = index

        for future in as_completed(futures):
            indexed_results[futures[future]] = future.result()

    results = [indexed_results[index] for index in range(len(accounts))]

    payload = {
        "schema_version": 1,
        "provider": "twitterapi.io",
        "status": "ok",
        "collected_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "run_date": run_date,
        "window_hours": int(os.environ.get("TWITTERAPI_IO_WINDOW_HOURS", "36")),
        "request_interval_seconds": request_interval,
        "max_workers": max_workers,
        "endpoint": "GET https://api.twitterapi.io/twitter/user/last_tweets",
        "include_replies": False,
        "accounts": results,
    }
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    summary = {
        "schema_version": 1,
        "provider": "twitterapi.io",
        "status": payload["status"],
        "output": str(output_path.relative_to(ROOT.parent)),
        "accounts": [
            {
                "handle": item["handle"],
                "status": item["status"],
                "raw_count": item.get("raw_count", 0),
                "kept_count": item.get("kept_count", 0),
                "message": item.get("response", {}).get("message"),
            }
            for item in results
        ],
    }
    if os.environ.get("TWITTERAPI_IO_PRINT_FULL") == "1":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
