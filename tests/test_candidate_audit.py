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


class CandidateAuditTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.date = "2026-05-26"
        (self.root / "docs").mkdir()
        (self.root / "raw" / self.date).mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def write_text(self, relative_path, text):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def write_json(self, relative_path, payload):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return path

    def test_official_link_candidate_not_in_daily_report_is_missed(self):
        self.write_text(f"docs/{self.date}-daily-intel.md", "# Daily\n\n## 今日高信号\n\n- Other signal.\n")
        self.write_json(
            f"raw/{self.date}/official-link-candidates.json",
            {
                "candidates": [
                    {
                        "handle": "AnthropicAI",
                        "tweet_id": "2058983299092009421",
                        "tweet_url": "https://x.com/AnthropicAI/status/2058983299092009421",
                        "expanded_url": "https://www.anthropic.com/news/chris-olah-pope-leo-encyclical",
                        "domain": "www.anthropic.com",
                        "score": 40,
                        "trigger_reason": "strong_keyword:Pope",
                        "fulltext_status": "ok",
                    }
                ]
            },
        )

        module = load_script("candidate-audit.py")
        payload = module.build_audit(self.date, root=self.root)

        self.assertEqual(payload["rows"][0]["status"], "missed")
        self.assertEqual(payload["rows"][0]["category"], "official-link-candidate")

    def test_official_link_candidate_in_daily_report_is_covered(self):
        url = "https://www.anthropic.com/news/chris-olah-pope-leo-encyclical"
        self.write_text(f"docs/{self.date}-daily-intel.md", f"# Daily\n\n- Covered: {url}\n")
        self.write_json(
            f"raw/{self.date}/official-link-candidates.json",
            {
                "candidates": [
                    {
                        "handle": "AnthropicAI",
                        "tweet_id": "2058983299092009421",
                        "tweet_url": "https://x.com/AnthropicAI/status/2058983299092009421",
                        "expanded_url": url,
                        "domain": "www.anthropic.com",
                        "score": 40,
                        "trigger_reason": "strong_keyword:Pope",
                        "fulltext_status": "ok",
                    }
                ]
            },
        )

        module = load_script("candidate-audit.py")
        payload = module.build_audit(self.date, root=self.root)

        self.assertEqual(payload["rows"][0]["status"], "covered")

    def test_anthropic_engineering_articles_are_audited_with_stable_ids(self):
        covered_url = "https://www.anthropic.com/engineering/covered"
        missed_url = "https://www.anthropic.com/engineering/missed"
        self.write_text(f"docs/{self.date}-daily-intel.md", f"# Daily\n\n- Covered: {covered_url}\n")
        self.write_json(
            f"raw/{self.date}/official-pages.json",
            {
                "sources": [
                    {
                        "source_id": "anthropic-engineering",
                        "items": [
                            {
                                "title": "Covered article",
                                "url": covered_url,
                                "window_status": "inside",
                                "fulltext_status": "ok",
                                "fulltext_path": f"raw/{self.date}/official-page-articles/covered.md",
                            },
                            {
                                "title": "Missed article",
                                "url": missed_url,
                                "window_status": "unknown",
                                "fulltext_status": "skipped",
                            },
                        ],
                    }
                ]
            },
        )

        module = load_script("candidate-audit.py")
        first = module.build_audit(self.date, root=self.root)
        second = module.build_audit(self.date, root=self.root)
        articles = [row for row in first["rows"] if row["category"] == "official-page-article"]

        self.assertEqual([row["status"] for row in articles], ["covered", "missed"])
        self.assertEqual([row["candidate_id"] for row in first["rows"]], [row["candidate_id"] for row in second["rows"]])
        self.assertEqual(articles[1]["fulltext_status"], "skipped")

    def test_anthropic_engineering_article_seen_before_run_is_not_audited(self):
        url = "https://www.anthropic.com/engineering/already-seen"
        self.write_text(f"docs/{self.date}-daily-intel.md", "# Daily\n")
        self.write_json(
            "state/seen.json",
            {"items": [{"id": f"url:{url}", "url": url, "first_seen": "2026-05-25"}]},
        )
        self.write_json(
            f"raw/{self.date}/official-pages.json",
            {
                "sources": [
                    {
                        "source_id": "anthropic-engineering",
                        "items": [{"title": "Already seen", "url": url, "window_status": "inside"}],
                    }
                ]
            },
        )

        module = load_script("candidate-audit.py")
        payload = module.build_audit(self.date, root=self.root)

        self.assertEqual(payload["rows"], [])

    def test_write_audit_writes_json_sha_and_preserves_disposition(self):
        report = self.write_text(f"docs/{self.date}-daily-intel.md", "# Daily\n\n- Other signal.\n")
        self.write_json(
            f"raw/{self.date}/official-link-candidates.json",
            {
                "candidates": [
                    {
                        "tweet_id": "1",
                        "tweet_url": "https://x.com/a/status/1",
                        "expanded_url": "https://example.com/post",
                        "score": 40,
                    }
                ]
            },
        )
        module = load_script("candidate-audit.py")

        first = module.write_audit(self.date, root=self.root)
        row = first["rows"][0]
        json_path = self.root / "reviews" / f"{self.date}-candidate-audit.json"
        stored = json.loads(json_path.read_text(encoding="utf-8"))
        stored["rows"][0]["disposition"] = "deferred"
        stored["rows"][0]["disposition_note"] = "not material today"
        json_path.write_text(json.dumps(stored), encoding="utf-8")

        second = module.write_audit(self.date, root=self.root)

        self.assertEqual(second["counts"]["total"], len(second["rows"]))
        self.assertEqual(second["rows"][0]["candidate_id"], row["candidate_id"])
        self.assertEqual(second["rows"][0]["disposition"], "deferred")
        self.assertEqual(
            second["daily_report_sha256"],
            __import__("hashlib").sha256(report.read_text(encoding="utf-8").encode("utf-8")).hexdigest(),
        )

    def test_topic_direct_x_not_in_daily_report_is_missed(self):
        self.write_text(f"docs/{self.date}-daily-intel.md", "# Daily\n\n- Other signal.\n")
        self.write_json(
            f"raw/{self.date}/twitter-topic-brief.json",
            {
                "topics": [
                    {
                        "id": "ai-agent",
                        "items": [
                            {
                                "tweet_id": "2059000000000000001",
                                "url": "https://x.com/simonw/status/2059000000000000001",
                                "text_excerpt": "Agent memory launch with MCP context",
                                "score": 44,
                            }
                        ],
                    }
                ]
            },
        )

        module = load_script("candidate-audit.py")
        payload = module.build_audit(self.date, root=self.root)

        rows = [row for row in payload["rows"] if row["category"] == "topic-direct-x"]
        self.assertEqual(rows[0]["status"], "missed")

    def test_topic_direct_x_in_daily_report_is_covered(self):
        tweet_url = "https://x.com/simonw/status/2059000000000000001"
        self.write_text(f"docs/{self.date}-daily-intel.md", f"# Daily\n\n- Covered: {tweet_url}\n")
        self.write_json(
            f"raw/{self.date}/twitter-topic-brief.json",
            {
                "topics": [
                    {
                        "id": "ai-agent",
                        "items": [
                            {
                                "tweet_id": "2059000000000000001",
                                "url": tweet_url,
                                "text_excerpt": "Agent memory launch with MCP context",
                                "score": 44,
                            }
                        ],
                    }
                ]
            },
        )

        module = load_script("candidate-audit.py")
        payload = module.build_audit(self.date, root=self.root)

        rows = [row for row in payload["rows"] if row["category"] == "topic-direct-x"]
        self.assertEqual(rows[0]["status"], "covered")

    def test_twitter_topic_summary_handle_mentions_require_same_line_tweet_links(self):
        greg_url = "https://x.com/gregisenberg/status/2059000000000000001"
        kloss_url = "https://x.com/kloss_xyz/status/2059000000000000002"
        self.write_text(
            f"docs/{self.date}-daily-intel.md",
            "\n".join(
                [
                    "# Daily",
                    "",
                    "### X/Twitter 推主主题摘要",
                    "",
                    f"- `AI Agent`：`gregisenberg` 的 [2059000000000000001]({greg_url}) 有链接。",
                    "- `Product / Growth / GTM`：`gregisenberg`、`kloss_xyz` 多条推文都围绕 agent 工具展开。",
                    "",
                    "### 下一节",
                ]
            ),
        )
        self.write_json(
            f"raw/{self.date}/twitter-topic-brief.json",
            {
                "topics": [
                    {
                        "id": "ai-agent",
                        "items": [
                            {
                                "tweet_id": "2059000000000000001",
                                "handle": "gregisenberg",
                                "url": greg_url,
                                "text_excerpt": "Build startups for agents",
                                "score": 44,
                            },
                            {
                                "tweet_id": "2059000000000000002",
                                "handle": "kloss_xyz",
                                "url": kloss_url,
                                "text_excerpt": "Fable 5 use cases",
                                "score": 44,
                            },
                        ],
                    }
                ]
            },
        )

        module = load_script("candidate-audit.py")
        payload = module.build_audit(self.date, root=self.root)

        rows = [row for row in payload["rows"] if row["category"] == "twitter-topic-summary-link"]
        self.assertEqual([row["status"] for row in rows], ["missed", "missed"])
        self.assertEqual({row["source"] for row in rows}, {greg_url, kloss_url})

    def test_topic_direct_x_is_deduped_with_official_link_candidate(self):
        tweet_id = "2058983299092009421"
        tweet_url = f"https://x.com/AnthropicAI/status/{tweet_id}"
        self.write_text(f"docs/{self.date}-daily-intel.md", "# Daily\n\n- Other signal.\n")
        self.write_json(
            f"raw/{self.date}/official-link-candidates.json",
            {
                "candidates": [
                    {
                        "handle": "AnthropicAI",
                        "tweet_id": tweet_id,
                        "tweet_url": tweet_url,
                        "expanded_url": "https://www.anthropic.com/news/example",
                        "score": 40,
                        "trigger_reason": "score>=20",
                        "fulltext_status": "ok",
                    }
                ]
            },
        )
        self.write_json(
            f"raw/{self.date}/twitter-topic-brief.json",
            {
                "topics": [
                    {
                        "id": "ai-governance",
                        "items": [
                            {
                                "tweet_id": tweet_id,
                                "url": tweet_url,
                                "text_excerpt": "AI governance update",
                                "score": 40,
                            }
                        ],
                    }
                ]
            },
        )

        module = load_script("candidate-audit.py")
        payload = module.build_audit(self.date, root=self.root)

        self.assertEqual([row["category"] for row in payload["rows"]].count("official-link-candidate"), 1)
        self.assertEqual([row["category"] for row in payload["rows"]].count("topic-direct-x"), 0)

    def test_audit_filters_items_seen_before_run_date(self):
        tweet_id = "2059000000000000001"
        tweet_url = f"https://x.com/simonw/status/{tweet_id}"
        rss_url = "https://example.com/already-seen"
        official_url = "https://www.anthropic.com/news/already-seen"
        self.write_text(f"docs/{self.date}-daily-intel.md", "# Daily\n\n- Other signal.\n")
        self.write_json(
            "state/seen.json",
            {
                "schema_version": 1,
                "items": [
                    {
                        "id": f"url:{rss_url}",
                        "first_seen": "2026-05-25",
                        "title": "Already seen RSS",
                        "url": rss_url,
                    },
                    {
                        "id": f"url:{official_url}",
                        "first_seen": "2026-05-25",
                        "title": "Already seen official link",
                        "url": official_url,
                    },
                    {
                        "id": f"tweet:{tweet_id}",
                        "first_seen": "2026-05-25",
                        "title": "Already seen tweet",
                        "url": tweet_url,
                    },
                ],
            },
        )
        self.write_json(
            f"raw/{self.date}/rss-items.json",
            {
                "sources": [
                    {
                        "items": [
                            {
                                "title": "Already seen RSS",
                                "url": rss_url,
                                "relevance_status": "matched",
                                "matched_keywords": ["agent"],
                                "fulltext_status": "ok",
                            }
                        ]
                    }
                ]
            },
        )
        self.write_json(
            f"raw/{self.date}/official-link-candidates.json",
            {
                "candidates": [
                    {
                        "tweet_id": "2058983299092009421",
                        "tweet_url": "https://x.com/AnthropicAI/status/2058983299092009421",
                        "expanded_url": official_url,
                        "score": 40,
                        "trigger_reason": "strong_keyword:policy",
                        "fulltext_status": "ok",
                    }
                ]
            },
        )
        self.write_json(
            f"raw/{self.date}/twitter-topic-brief.json",
            {
                "topics": [
                    {
                        "id": "ai-agent",
                        "items": [
                            {
                                "tweet_id": tweet_id,
                                "url": tweet_url,
                                "text_excerpt": "Already seen direct X",
                                "score": 44,
                            }
                        ],
                    }
                ]
            },
        )

        module = load_script("candidate-audit.py")
        payload = module.build_audit(self.date, root=self.root)

        self.assertEqual(payload["rows"], [])


if __name__ == "__main__":
    unittest.main()
