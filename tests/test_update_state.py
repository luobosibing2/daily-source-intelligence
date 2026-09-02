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


if __name__ == "__main__":
    unittest.main()
