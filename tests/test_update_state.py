import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module():
    path = ROOT / "scripts" / "update-state.py"
    spec = importlib.util.spec_from_file_location("update_state", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SourceHealthTest(unittest.TestCase):
    def setUp(self):
        self.module = load_module()
        self.raw = {
            "rss": {"sources": []},
            "github": {"sources": [], "api_status": {}},
            "github_trending": {"sources": []},
            "official": {"sources": []},
            "twitter": {"status": "ok", "accounts": []},
            "podcasts": {"status": "missing", "episodes": []},
        }

    def test_failure_increments_and_keeps_last_success(self):
        self.raw["rss"]["sources"] = [{"source_id": "feed", "status": "failed", "error": "down"}]
        previous = {
            "sources": {
                "feed": {"status": "failed", "consecutive_failures": 2, "last_success": "2026-07-16"},
                "not-collected": {"status": "ok", "consecutive_failures": 0},
            }
        }

        payload = self.module.source_health(self.raw, "2026-07-19", previous=previous)

        self.assertEqual(payload["sources"]["feed"]["consecutive_failures"], 3)
        self.assertEqual(payload["sources"]["feed"]["last_success"], "2026-07-16")
        self.assertIn("not-collected", payload["sources"])

    def test_success_resets_failure_count(self):
        self.raw["rss"]["sources"] = [{"source_id": "feed", "status": "ok", "items": []}]
        previous = {"sources": {"feed": {"status": "failed", "consecutive_failures": 4}}}

        payload = self.module.source_health(self.raw, "2026-07-19", previous=previous)

        self.assertEqual(payload["sources"]["feed"]["consecutive_failures"], 0)
        self.assertEqual(payload["sources"]["feed"]["last_success"], "2026-07-19")

    def test_partial_collection_does_not_refresh_unselected_sources(self):
        self.raw["rss"] = {
            "partial_update": True,
            "selected_source_ids": ["selected"],
            "sources": [
                {"source_id": "selected", "status": "ok", "items": []},
                {"source_id": "preserved", "status": "ok", "items": []},
            ],
        }
        previous = {
            "sources": {
                "preserved": {"status": "failed", "last_checked": "2026-07-18", "consecutive_failures": 2}
            }
        }

        payload = self.module.source_health(self.raw, "2026-07-19", previous=previous)

        self.assertEqual(payload["sources"]["selected"]["last_success"], "2026-07-19")
        self.assertEqual(payload["sources"]["preserved"]["last_checked"], "2026-07-18")
        self.assertEqual(payload["sources"]["preserved"]["consecutive_failures"], 2)

    def test_anthropic_engineering_health_manifest_and_seen_counts(self):
        article_url = "https://www.anthropic.com/engineering/new-article"
        self.raw["official"]["sources"] = [
            {
                "source_id": "anthropic-engineering",
                "status": "ok",
                "index_status": "ok",
                "index_card_count": 24,
                "items": [
                    {
                        "title": "New article",
                        "url": article_url,
                        "published": "2026-07-19",
                        "window_status": "inside",
                        "fulltext_status": "ok",
                    },
                    {
                        "title": "Unknown date",
                        "url": "https://www.anthropic.com/engineering/unknown",
                        "published": "",
                        "window_status": "unknown",
                        "fulltext_status": "skipped",
                    },
                    {
                        "title": "Failed body",
                        "url": "https://www.anthropic.com/engineering/failed",
                        "published": "2026-07-19",
                        "window_status": "inside",
                        "fulltext_status": "failed",
                    },
                ],
            }
        ]

        health = self.module.source_health(self.raw, "2026-07-19")
        source = health["sources"]["anthropic-engineering"]
        self.assertEqual(source["index_card_count"], 24)
        self.assertEqual(source["daily_item_count"], 3)
        self.assertEqual(source["article_fulltext_counts"], {"ok": 1, "limited": 0, "failed": 1})

        manifest = self.module.manifest(self.raw, "2026-07-19")
        self.assertEqual(manifest["summary"]["official_page_index_cards"], 24)
        self.assertEqual(manifest["summary"]["official_page_article_items"], 3)
        self.assertEqual(manifest["summary"]["official_page_article_fulltext_ok"], 1)
        self.assertEqual(manifest["summary"]["official_page_article_fulltext_failed"], 1)

        seen = self.module.stable_seen_items(self.raw, "2026-07-19")
        by_url = {item["url"]: item for item in seen}
        self.assertEqual(by_url[article_url]["id"], f"url:{article_url}")
        self.assertIn("https://www.anthropic.com/engineering/unknown", by_url)

    def test_anthropic_engineering_zero_new_does_not_mark_index_as_seen(self):
        self.raw["official"]["sources"] = [
            {
                "source_id": "anthropic-engineering",
                "status": "ok",
                "url": "https://www.anthropic.com/engineering",
                "index_status": "ok",
                "index_card_count": 25,
                "items": [],
            }
        ]

        seen = self.module.stable_seen_items(self.raw, "2026-09-03")

        self.assertEqual(seen, [])

    def test_podcast_health_manifest_and_seen_use_offered_denominator_and_guid_identity(self):
        self.raw["podcasts"] = {
            "source_id": "follow-builders",
            "status": "partial",
            "collected_at": "2026-07-19T12:00:00+08:00",
            "upstream_generated_at": "2026-07-19T01:00:00Z",
            "lookback_hours": 336,
            "errors": ["one upstream show failed"],
            "episodes": [
                {
                    "show_id": "ai-i-by-every",
                    "guid": "guid-1",
                    "title": "Readable",
                    "published_at": "2026-07-19T01:00:00+08:00",
                    "window_status": "inside",
                    "canonical_url": "https://example.com/episodes/1",
                    "link_status": "ok",
                    "transcript_status": "ok",
                    "allowed": True,
                },
                {
                    "show_id": "latent-space",
                    "guid": "guid-2",
                    "title": "Outside",
                    "window_status": "outside",
                    "link_status": "limited",
                    "transcript_status": "limited",
                    "allowed": True,
                },
                {
                    "show_id": "",
                    "guid": "guid-3",
                    "title": "Unconfigured",
                    "window_status": "unknown",
                    "admission_status": "unconfigured",
                    "episode_status": "unconfigured",
                    "allowed": False,
                    "transcript_status": "ok",
                },
            ],
        }

        health = self.module.source_health(self.raw, "2026-07-19")
        source = health["sources"]["follow-builders"]
        self.assertEqual(source["status"], "partial")
        self.assertEqual(source["offered_count"], 3)
        self.assertEqual(source["inside_count"], 1)
        self.assertEqual(source["transcript_counts"], {"ok": 1, "limited": 1})

        manifest = self.module.manifest(self.raw, "2026-07-19")
        self.assertEqual(manifest["summary"]["podcast_offered"], 3)
        self.assertEqual(manifest["summary"]["podcast_inside"], 1)
        self.assertEqual(manifest["summary"]["podcast_outside"], 1)
        self.assertEqual(manifest["summary"]["podcast_unknown"], 0)
        self.assertEqual(manifest["summary"]["podcast_transcript_ok"], 1)
        self.assertEqual(manifest["summary"]["podcast_upstream_errors"], 1)
        self.assertEqual(manifest["summary"]["podcast_unconfigured"], 1)

        seen = self.module.stable_seen_items(self.raw, "2026-07-19")
        self.assertEqual(len(seen), 1)
        self.assertEqual(seen[0]["id"], "podcast:ai-i-by-every:guid-1")
        self.assertEqual(seen[0]["transcript_status"], "ok")
        self.assertEqual(seen[0]["evidence_level"], "secondary-source")

    def test_same_day_podcast_seen_record_upgrades_from_limited_to_ok(self):
        with __import__("tempfile").TemporaryDirectory() as tmp:
            state_root = Path(tmp) / "state"
            state_root.mkdir()
            self.module.STATE_ROOT = state_root
            (state_root / "seen.json").write_text(
                __import__("json").dumps(
                    {
                        "schema_version": 1,
                        "items": [
                            {
                                "id": "podcast:ai-i-by-every:guid-1",
                                "first_seen": "2026-07-19",
                                "transcript_status": "limited",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            self.raw["podcasts"] = {
                "source_id": "follow-builders",
                "status": "ok",
                "episodes": [
                    {
                        "show_id": "ai-i-by-every",
                        "guid": "guid-1",
                        "title": "Now readable",
                        "window_status": "inside",
                        "transcript_status": "ok",
                    }
                ],
            }

            self.module.update_seen(self.raw, "2026-07-19")
            payload = __import__("json").loads((state_root / "seen.json").read_text(encoding="utf-8"))

        self.assertEqual(payload["items"][0]["transcript_status"], "ok")


if __name__ == "__main__":
    unittest.main()
