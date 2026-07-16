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


class RunDsiPipelineTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.date = "2026-06-30"
        (self.root / "raw" / self.date).mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def write_text(self, relative_path, text):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def write_json(self, relative_path, payload):
        return self.write_text(relative_path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

    def seed_raw_inputs(self):
        self.write_text(
            f"raw/{self.date}/rss-fulltext/openai-blog/agents.extracted.md",
            "# OpenAI Agents\n\nFull body about agents transforming work.\n",
        )
        self.write_text(
            f"raw/{self.date}/official-link-candidates/anthropic-policy.opencli.md",
            "# Anthropic Policy\n\nFull official policy text.\n",
        )
        self.write_text(
            f"raw/{self.date}/github-trending-readmes/acme__agent-memory.md",
            "# Agent Memory\n\nREADME confirms the project stores agent context.\n",
        )
        self.write_text(
            f"raw/{self.date}/github-release-fulltext/openai-codex/codex-release.atom.md",
            "# 0.130.0\n\nRelease body for Codex.\n",
        )
        self.write_json(
            f"raw/{self.date}/rss-items.json",
            {
                "sources": [
                    {
                        "source_id": "openai-blog",
                        "items": [
                            {
                                "title": "OpenAI Agents",
                                "url": "https://openai.com/index/agents",
                                "relevance_status": "matched",
                                "matched_topics": ["ai-agent"],
                                "fulltext_status": "ok",
                                "fulltext_path": f"raw/{self.date}/rss-fulltext/openai-blog/agents.extracted.md",
                            },
                            {
                                "title": "Limited post",
                                "url": "https://example.com/limited",
                                "relevance_status": "matched",
                                "matched_topics": ["ai-agent"],
                                "fulltext_status": "limited",
                                "fulltext_error": "short content",
                            },
                        ],
                    }
                ]
            },
        )
        self.write_json(
            f"raw/{self.date}/official-link-candidates.json",
            {
                "candidates": [
                    {
                        "expanded_url": "https://anthropic.com/news/policy",
                        "tweet_url": "https://x.com/AnthropicAI/status/1",
                        "fulltext_status": "ok",
                        "fulltext_path": f"raw/{self.date}/official-link-candidates/anthropic-policy.opencli.md",
                        "evidence_level": "direct-x",
                        "trigger_reason": "strong_keyword:policy",
                    }
                ]
            },
        )
        self.write_json(
            f"raw/{self.date}/github-trending.json",
            {
                "sources": [
                    {
                        "items": [
                            {
                                "repo": "acme/agent-memory",
                                "url": "https://github.com/acme/agent-memory",
                                "readme_status": "ok",
                                "readme_path": f"raw/{self.date}/github-trending-readmes/acme__agent-memory.md",
                                "readme_title": "Agent Memory",
                                "trending_description": "Agent context store",
                            }
                        ]
                    }
                ]
            },
        )
        self.write_json(
            f"raw/{self.date}/github-items.json",
            {
                "sources": [
                    {
                        "source_id": "openai-codex",
                        "items": [
                            {
                                "title": "0.130.0",
                                "url": "https://github.com/openai/codex/releases/tag/v0.130.0",
                                "relevance_status": "always_read",
                                "fulltext_status": "ok",
                                "fulltext_path": f"raw/{self.date}/github-release-fulltext/openai-codex/codex-release.atom.md",
                            }
                        ],
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
                        "label": "AI Agent / Agentic Workflow",
                        "items": [
                            {
                                "tweet_id": "1",
                                "url": "https://x.com/simonw/status/1",
                                "text_excerpt": "Agent memory field note",
                                "score": 44,
                                "evidence_level": "direct-x",
                            }
                        ],
                    }
                ]
            },
        )

    def test_report_reading_list_keeps_body_paths_and_boundary_rows(self):
        self.seed_raw_inputs()
        module = load_script("run-dsi-pipeline.py")

        payload = module.build_report_reading_list(self.date, root=self.root)

        entries = payload["entries"]
        body_paths = {entry["local_body_path"] for entry in entries}
        self.assertIn(f"raw/{self.date}/rss-fulltext/openai-blog/agents.extracted.md", body_paths)
        self.assertIn(f"raw/{self.date}/official-link-candidates/anthropic-policy.opencli.md", body_paths)
        self.assertIn(f"raw/{self.date}/github-trending-readmes/acme__agent-memory.md", body_paths)
        self.assertIn(f"raw/{self.date}/github-release-fulltext/openai-codex/codex-release.atom.md", body_paths)
        self.assertTrue(any(entry["source_type"] == "topic-direct-x" and entry["local_body_path"] == "" for entry in entries))

        limited = next(entry for entry in entries if entry["title"] == "Limited post")
        self.assertEqual(limited["fulltext_status"], "limited")
        self.assertEqual(limited["local_body_path"], "")
        self.assertIn("boundary", limited["why_read"])

    def test_report_reading_list_filters_items_seen_before_run_date(self):
        self.seed_raw_inputs()
        self.write_json(
            "state/seen.json",
            {
                "schema_version": 1,
                "items": [
                    {
                        "id": "url:https://openai.com/index/agents",
                        "first_seen": "2026-06-29",
                        "title": "OpenAI Agents",
                        "url": "https://openai.com/index/agents",
                    },
                    {
                        "id": "url:https://anthropic.com/news/policy",
                        "first_seen": "2026-06-29",
                        "title": "Anthropic Policy",
                        "url": "https://anthropic.com/news/policy",
                    },
                    {
                        "id": "github-trending:acme/agent-memory",
                        "first_seen": "2026-06-29",
                        "title": "acme/agent-memory",
                        "url": "https://github.com/acme/agent-memory",
                    },
                    {
                        "id": "tweet:1",
                        "first_seen": "2026-06-29",
                        "title": "Agent memory field note",
                        "url": "https://x.com/simonw/status/1",
                    },
                    {
                        "id": "url:https://github.com/openai/codex/releases/tag/v0.130.0",
                        "first_seen": self.date,
                        "title": "0.130.0",
                        "url": "https://github.com/openai/codex/releases/tag/v0.130.0",
                    },
                ],
            },
        )
        module = load_script("run-dsi-pipeline.py")

        payload = module.build_report_reading_list(self.date, root=self.root)

        titles = {entry["title"] for entry in payload["entries"]}
        urls = {entry["url"] for entry in payload["entries"]}
        self.assertNotIn("OpenAI Agents", titles)
        self.assertNotIn("https://anthropic.com/news/policy", urls)
        self.assertNotIn("Agent Memory", titles)
        self.assertNotIn("Agent memory field note", titles)
        self.assertIn("0.130.0", titles)

    def test_run_summary_is_status_only_not_evidence_body(self):
        self.seed_raw_inputs()
        module = load_script("run-dsi-pipeline.py")

        reading_list = module.build_report_reading_list(self.date, root=self.root)
        summary = module.build_run_summary(self.date, root=self.root, reading_list=reading_list)

        self.assertEqual(summary["run_date"], self.date)
        self.assertEqual(summary["reading_list"], f"raw/{self.date}/report-reading-list.json")
        self.assertNotIn("Full body about agents transforming work", json.dumps(summary, ensure_ascii=False))
        self.assertGreaterEqual(summary["counts"]["reading_list_entries"], 5)


if __name__ == "__main__":
    unittest.main()
