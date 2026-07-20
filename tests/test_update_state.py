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


if __name__ == "__main__":
    unittest.main()
