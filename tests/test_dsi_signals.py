import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module():
    path = ROOT / "scripts" / "dsi_signals.py"
    spec = importlib.util.spec_from_file_location("dsi_signals_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DsiSignalsTest(unittest.TestCase):
    def setUp(self):
        self.module = load_module()
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.run_date = "2026-07-19"
        (self.root / "raw" / self.run_date).mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def write_json(self, name, payload):
        path = self.root / "raw" / self.run_date / name
        path.write_text(json.dumps(payload), encoding="utf-8")

    def test_canonical_url_drops_tracking_and_normalizes(self):
        left = "HTTPS://Example.COM/post/?utm_source=x&b=2&a=1#part"
        right = "https://example.com/post?a=1&b=2"
        self.assertEqual(self.module.canonicalize_url(left), right)

    def test_exact_beijing_day_excludes_outside_timestamp(self):
        self.write_json(
            "rss-items.json",
            {
                "sources": [
                    {
                        "source_id": "feed",
                        "items": [
                            {
                                "title": "inside",
                                "url": "https://example.com/inside",
                                "published": "2026-07-18T16:00:00Z",
                                "relevance_status": "matched",
                            },
                            {
                                "title": "outside",
                                "url": "https://example.com/outside",
                                "published": "2026-07-18T15:59:59Z",
                                "relevance_status": "matched",
                            },
                            {
                                "title": "unknown",
                                "url": "https://example.com/unknown",
                                "relevance_status": "matched",
                            },
                        ],
                    }
                ]
            },
        )

        payload = self.module.build_signals(self.run_date, self.root)
        by_title = {item["title"]: item for item in payload["signals"]}

        self.assertEqual(set(by_title), {"inside", "unknown"})
        self.assertEqual(by_title["inside"]["window_status"], "inside")
        self.assertEqual(by_title["unknown"]["window_status"], "unknown")

    def test_same_tweet_is_one_signal_with_all_topics_and_top_three_per_topic(self):
        topics = []
        for topic_id in ("agents", "memory"):
            items = []
            for index, score in enumerate((50, 40, 30, 20), start=1):
                tweet_id = str(index if topic_id == "agents" else index + 3)
                if topic_id == "memory" and index == 1:
                    tweet_id = "1"
                items.append(
                    {
                        "tweet_id": tweet_id,
                        "url": f"https://x.com/user/status/{tweet_id}",
                        "text_excerpt": f"tweet {tweet_id}",
                        "score": score,
                        "created_at": "2026-07-19T04:00:00Z",
                    }
                )
            topics.append({"id": topic_id, "items": items})
        self.write_json("twitter-topic-brief.json", {"topics": topics})

        payload = self.module.build_signals(self.run_date, self.root)
        tweets = [item for item in payload["signals"] if item["source_type"] == "topic-direct-x"]
        by_id = {item["signal_id"]: item for item in tweets}

        self.assertEqual(len(tweets), 5)
        self.assertEqual(by_id["tweet:1"]["topics"], ["agents", "memory"])
        self.assertNotIn("tweet:4", by_id)
        self.assertIn("tweet:6", by_id)

    def test_score_and_content_are_explainable(self):
        body = self.root / "raw" / self.run_date / "body.md"
        body.write_text("body", encoding="utf-8")
        self.write_json(
            "github-items.json",
            {
                "sources": [
                    {
                        "source_id": "repo",
                        "topics": ["codex"],
                        "items": [
                            {
                                "title": "release",
                                "url": "https://github.com/o/r/releases/tag/v1",
                                "updated": "2026-07-19T00:00:00Z",
                                "relevance_status": "always_read",
                                "fulltext_status": "ok",
                                "fulltext_path": f"raw/{self.run_date}/body.md",
                            }
                        ],
                    }
                ]
            },
        )

        signal = self.module.build_signals(self.run_date, self.root)["signals"][0]

        self.assertEqual(signal["score"], {"total": 65, "breakdown": {"release_relevance": 65}})
        self.assertEqual(signal["content"]["path"], f"raw/{self.run_date}/body.md")
        self.assertEqual(signal["topics"], ["codex"])


if __name__ == "__main__":
    unittest.main()
