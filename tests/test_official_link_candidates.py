import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OfficialLinkCandidatesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.date = "2026-05-26"
        (self.root / "config").mkdir()
        (self.root / "raw" / self.date).mkdir(parents=True)
        self.write_json(
            "config/sources.yaml",
            {
                "official_link_candidates": {
                    "enabled": True,
                    "official_domains": ["anthropic.com"],
                    "strong_keywords": ["Pope", "Vatican", "encyclical"],
                    "min_score": 20,
                },
                "x_accounts": [
                    {
                        "id": "anthropic",
                        "name": "Anthropic",
                        "handle": "AnthropicAI",
                        "enabled": True,
                        "priority": True,
                    },
                    {
                        "id": "other",
                        "name": "Other",
                        "handle": "OtherAI",
                        "enabled": True,
                        "priority": False,
                    },
                ],
            },
        )

    def tearDown(self):
        self.tmp.cleanup()

    def write_json(self, relative_path, payload):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return path

    def test_priority_official_url_with_governance_keywords_generates_candidate(self):
        self.write_json(
            f"raw/{self.date}/twitterapi-io-results.json",
            {
                "accounts": [
                    {
                        "handle": "AnthropicAI",
                        "status": "ok",
                        "tweets": [
                            {
                                "id": "2058983299092009421",
                                "url": "https://x.com/AnthropicAI/status/2058983299092009421",
                                "text": "Chris Olah spoke at Pope Leo XIV's encyclical presentation.",
                                "retweetCount": 1,
                                "replyCount": 1,
                                "likeCount": 1,
                                "quoteCount": 0,
                                "entities": {
                                    "urls": [
                                        {
                                            "expanded_url": "https://www.anthropic.com/news/chris-olah-pope-leo-encyclical"
                                        }
                                    ]
                                },
                            }
                        ],
                    }
                ]
            },
        )

        def fake_fetcher(url, output_dir, stem):
            self.assertEqual(url, "https://www.anthropic.com/news/chris-olah-pope-leo-encyclical")
            return {
                "fulltext_status": "ok",
                "fulltext_method": "test",
                "fulltext_path": f"raw/{self.date}/official-link-candidates/{stem}.md",
            }

        module = load_script("official-link-candidates.py")
        payload = module.generate_candidates(self.date, root=self.root, fetcher=fake_fetcher)

        self.assertEqual(len(payload["candidates"]), 1)
        candidate = payload["candidates"][0]
        self.assertEqual(candidate["handle"], "AnthropicAI")
        self.assertEqual(candidate["tweet_id"], "2058983299092009421")
        self.assertEqual(candidate["domain"], "www.anthropic.com")
        self.assertEqual(candidate["fulltext_status"], "ok")
        self.assertEqual(candidate["evidence_level"], "direct-x")
        self.assertIn("strong_keyword", candidate["trigger_reason"])

    def test_non_priority_or_unofficial_low_signal_tweets_are_ignored(self):
        self.write_json(
            f"raw/{self.date}/twitterapi-io-results.json",
            {
                "accounts": [
                    {
                        "handle": "OtherAI",
                        "status": "ok",
                        "tweets": [
                            {
                                "id": "1",
                                "url": "https://x.com/OtherAI/status/1",
                                "text": "Pope AI governance note",
                                "entities": {"urls": [{"expanded_url": "https://www.anthropic.com/news/example"}]},
                            }
                        ],
                    },
                    {
                        "handle": "AnthropicAI",
                        "status": "ok",
                        "tweets": [
                            {
                                "id": "2",
                                "url": "https://x.com/AnthropicAI/status/2",
                                "text": "low signal blog link",
                                "entities": {"urls": [{"expanded_url": "https://example.com/news"}]},
                            }
                        ],
                    },
                ]
            },
        )

        module = load_script("official-link-candidates.py")
        payload = module.generate_candidates(self.date, root=self.root, fetcher=lambda *_: {})

        self.assertEqual(payload["candidates"], [])

    def test_fetch_failure_is_recorded_as_candidate_boundary(self):
        self.write_json(
            f"raw/{self.date}/twitterapi-io-results.json",
            {
                "accounts": [
                    {
                        "handle": "AnthropicAI",
                        "status": "ok",
                        "tweets": [
                            {
                                "id": "3",
                                "url": "https://x.com/AnthropicAI/status/3",
                                "text": "AI governance update",
                                "retweetCount": 500,
                                "replyCount": 20,
                                "likeCount": 900,
                                "quoteCount": 10,
                                "entities": {
                                    "urls": [{"expanded_url": "https://www.anthropic.com/news/governance"}]
                                },
                            }
                        ],
                    }
                ]
            },
        )

        def failing_fetcher(url, output_dir, stem):
            return {"fulltext_status": "failed", "fulltext_error": "curl failed"}

        module = load_script("official-link-candidates.py")
        payload = module.generate_candidates(self.date, root=self.root, fetcher=failing_fetcher)

        self.assertEqual(len(payload["candidates"]), 1)
        self.assertEqual(payload["candidates"][0]["fulltext_status"], "failed")
        self.assertEqual(payload["candidates"][0]["fulltext_error"], "curl failed")


if __name__ == "__main__":
    unittest.main()
