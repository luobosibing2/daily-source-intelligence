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


class BuildTwitterTopicBriefTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.date = "2026-06-28"
        (self.root / "config").mkdir()
        (self.root / "raw" / self.date).mkdir(parents=True)
        self.write_json(
            "config/topics.yaml",
            {
                "topics": [
                    {
                        "id": "ai-agent",
                        "label": "AI Agent / Agentic Workflow",
                        "keywords": ["agent", "memory", "MCP"],
                        "exclude": ["travel agent"],
                    },
                    {
                        "id": "ai-coding",
                        "label": "AI Coding / Developer Tools",
                        "keywords": ["Claude Code", "Codex", "IDE"],
                        "exclude": [],
                    },
                    {
                        "id": "product-growth",
                        "label": "Product / Growth / GTM",
                        "keywords": ["launch", "revenue"],
                        "exclude": [],
                    },
                ]
            },
        )

    def tearDown(self):
        self.tmp.cleanup()

    def write_json(self, relative_path, payload):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return path

    def item_by_tweet_id(self, payload, tweet_id):
        for topic in payload["topics"]:
            for item in topic["items"]:
                if item["tweet_id"] == tweet_id:
                    return item
        for item in payload["ungrouped"]:
            if item["tweet_id"] == tweet_id:
                return item
        return None

    def test_priority_account_defaults_to_configured_topics_without_keyword_match(self):
        self.write_json(
            "config/sources.yaml",
            {
                "x_accounts": [
                    {
                        "id": "alice",
                        "name": "Alice",
                        "handle": "alice",
                        "enabled": True,
                        "priority": True,
                        "topics": ["ai-agent"],
                    }
                ]
            },
        )
        self.write_json(
            f"raw/{self.date}/twitterapi-io-results.json",
            {
                "status": "ok",
                "accounts": [
                    {
                        "handle": "alice",
                        "name": "Alice",
                        "status": "ok",
                        "tweets": [
                            {
                                "id": "1",
                                "url": "https://x.com/alice/status/1",
                                "text": "Shipping a tiny thing today.",
                                "likeCount": 0,
                            }
                        ],
                    }
                ],
            },
        )

        module = load_script("build-twitter-topic-brief.py")
        payload = module.build_brief(self.date, root=self.root)

        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["topics"][0]["id"], "ai-agent")
        item = payload["topics"][0]["items"][0]
        self.assertEqual(item["tweet_id"], "1")
        self.assertEqual(item["matched_topics"], ["ai-agent"])
        self.assertEqual(item["account_topics"], ["ai-agent"])
        self.assertEqual(item["matched_keywords"], [])
        self.assertGreater(item["score"], 0)

    def test_items_include_author_url_and_tweet_markdown_for_report_writing(self):
        self.write_json(
            "config/sources.yaml",
            {
                "x_accounts": [
                    {
                        "id": "alice",
                        "name": "Alice",
                        "handle": "Alice_Builder",
                        "enabled": True,
                        "priority": True,
                        "topics": ["ai-agent"],
                    }
                ]
            },
        )
        self.write_json(
            f"raw/{self.date}/twitterapi-io-results.json",
            {
                "status": "ok",
                "accounts": [
                    {
                        "handle": "Alice_Builder",
                        "name": "Alice",
                        "status": "ok",
                        "tweets": [
                            {
                                "id": "123",
                                "text": "Agent memory launch.",
                            }
                        ],
                    }
                ],
            },
        )

        module = load_script("build-twitter-topic-brief.py")
        payload = module.build_brief(self.date, root=self.root)
        item = self.item_by_tweet_id(payload, "123")

        self.assertEqual(item["url"], "https://x.com/Alice_Builder/status/123")
        self.assertEqual(item["author_url"], "https://x.com/Alice_Builder")
        self.assertEqual(item["tweet_markdown"], "[123](https://x.com/Alice_Builder/status/123)")
        self.assertEqual(item["citation_markdown"], "`Alice_Builder` 的 [123](https://x.com/Alice_Builder/status/123)")

    def test_text_and_card_keywords_add_multiple_topic_matches(self):
        self.write_json(
            "config/sources.yaml",
            {
                "x_accounts": [
                    {
                        "id": "bob",
                        "name": "Bob",
                        "handle": "bob",
                        "enabled": True,
                        "priority": False,
                        "topics": [],
                    }
                ]
            },
        )
        self.write_json(
            f"raw/{self.date}/twitterapi-io-results.json",
            {
                "status": "ok",
                "accounts": [
                    {
                        "handle": "bob",
                        "name": "Bob",
                        "status": "ok",
                        "tweets": [
                            {
                                "id": "2",
                                "url": "https://x.com/bob/status/2",
                                "text": "Claude Code agent memory update",
                                "card": {"binding_values": {"title": {"string_value": "MCP tools"}}},
                            }
                        ],
                    }
                ],
            },
        )

        module = load_script("build-twitter-topic-brief.py")
        payload = module.build_brief(self.date, root=self.root)
        item = self.item_by_tweet_id(payload, "2")

        self.assertEqual(item["matched_topics"], ["ai-agent", "ai-coding"])
        self.assertEqual(item["matched_keywords"], ["Claude Code", "MCP", "agent", "memory"])

    def test_short_ascii_keywords_do_not_match_inside_words(self):
        self.write_json(
            "config/sources.yaml",
            {
                "x_accounts": [
                    {
                        "id": "hesamation",
                        "name": "Hesamation",
                        "handle": "Hesamation",
                        "enabled": True,
                        "priority": False,
                        "topics": [],
                    }
                ]
            },
        )
        self.write_json(
            f"raw/{self.date}/twitterapi-io-results.json",
            {
                "status": "ok",
                "accounts": [
                    {
                        "handle": "Hesamation",
                        "name": "Hesamation",
                        "status": "ok",
                        "tweets": [
                            {
                                "id": "short-keyword",
                                "url": "https://x.com/Hesamation/status/short-keyword",
                                "text": "The president talked about policy.",
                            }
                        ],
                    }
                ],
            },
        )

        module = load_script("build-twitter-topic-brief.py")
        payload = module.build_brief(self.date, root=self.root)
        item = self.item_by_tweet_id(payload, "short-keyword")

        self.assertNotIn("ai-coding", item["matched_topics"])
        self.assertNotIn("IDE", item["matched_keywords"])

    def test_failed_and_skipped_accounts_are_reported_as_coverage_limits(self):
        self.write_json("config/sources.yaml", {"x_accounts": []})
        self.write_json(
            f"raw/{self.date}/twitterapi-io-results.json",
            {
                "status": "ok",
                "accounts": [
                    {"handle": "failed_ai", "status": "failed", "error": "timeout", "tweets": []},
                    {"handle": "skipped_ai", "status": "skipped", "reason": "missing key", "tweets": []},
                ],
            },
        )

        module = load_script("build-twitter-topic-brief.py")
        payload = module.build_brief(self.date, root=self.root)

        self.assertEqual(payload["status"], "partial")
        self.assertEqual(payload["coverage"]["failed_accounts"][0]["handle"], "failed_ai")
        self.assertEqual(payload["coverage"]["skipped_accounts"][0]["handle"], "skipped_ai")

    def test_retweets_and_replies_are_downranked_but_retained(self):
        self.write_json(
            "config/sources.yaml",
            {
                "x_accounts": [
                    {
                        "id": "builder",
                        "name": "Builder",
                        "handle": "builder",
                        "enabled": True,
                        "priority": False,
                        "topics": ["ai-agent"],
                    }
                ]
            },
        )
        self.write_json(
            f"raw/{self.date}/twitterapi-io-results.json",
            {
                "status": "ok",
                "accounts": [
                    {
                        "handle": "builder",
                        "name": "Builder",
                        "status": "ok",
                        "tweets": [
                            {
                                "id": "3",
                                "url": "https://x.com/builder/status/3",
                                "text": "agent launch",
                                "likeCount": 100,
                            },
                            {
                                "id": "4",
                                "url": "https://x.com/builder/status/4",
                                "text": "RT @other: agent launch",
                                "likeCount": 100,
                                "isReply": True,
                            },
                        ],
                    }
                ],
            },
        )

        module = load_script("build-twitter-topic-brief.py")
        payload = module.build_brief(self.date, root=self.root)
        original = self.item_by_tweet_id(payload, "3")
        retweet = self.item_by_tweet_id(payload, "4")

        self.assertIsNotNone(original)
        self.assertIsNotNone(retweet)
        self.assertLess(retweet["score"], original["score"])


if __name__ == "__main__":
    unittest.main()
