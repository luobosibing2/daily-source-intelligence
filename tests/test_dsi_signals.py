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

    def test_aihot_signals_dedup_originals_keep_secondary_discovery_provenance(self):
        original = "https://www.microsoft.com/en-us/research/blog/agent-lightning-v1-0/"
        item = {
            "title": "AIHOT: Agent Lightning 中文摘要",
            "url": original + "?utm_source=aihot&ref=feed",
            "published": "2026-07-18T16:00:00Z",
            "published_basis": "aihot-feed-pubdate",
            "relevance_status": "matched",
            "matched_topics": ["ai-agent"],
            "fulltext_status": "limited",
            "aggregator_url": "https://aihot.news/items/first",
            "guid": "first",
            "feed_url": "https://aihot.news/feed.xml",
            "feed_author": "noreply@aihot.news (Microsoft Research 博客)",
            "intelligence_department": "should-not-upgrade-aggregator",
        }
        second = {**item, "url": original, "guid": "second", "aggregator_url": "https://aihot.news/items/second"}
        self.write_json("rss-items.json", {"sources": [{
            "source_id": "aihot-selected",
            "topics": ["llm", "ai-agent"],
            "feed_snapshot_path": "raw/2026-07-19/rss-feeds/aihot-selected.xml",
            "feed_sha256": "feed-hash",
            "items": [item, second],
        }]})

        payload = self.module.build_signals(self.run_date, self.root)

        self.assertEqual(len(payload["signals"]), 1)
        signal = payload["signals"][0]
        self.assertEqual(signal["canonical_url"], original.rstrip("/"))
        self.assertEqual(signal["signal_id"], "url:" + original.rstrip("/"))
        self.assertEqual(signal["evidence_level"], "secondary-source")
        self.assertEqual(signal["topics"], ["ai-agent"])
        self.assertEqual(signal["content"], {"status": "limited", "path": ""})
        self.assertEqual({row["guid"] for row in signal["provenance"]}, {"first", "second"})
        discovery = signal["provenance"][0]
        self.assertEqual(discovery["aggregator_name"], "AIHOT")
        self.assertEqual(discovery["feed_url"], "https://aihot.news/feed.xml")
        self.assertEqual(discovery["feed_sha256"], "feed-hash")
        self.assertEqual(discovery["discovery_title"], item["title"])
        self.assertEqual(discovery["published_basis"], "aihot-feed-pubdate")
        self.assertEqual(discovery["evidence_level"], "secondary-source")
        reading_list = self.module.build_reading_list(payload, "now")
        self.assertEqual(reading_list["entries"][0]["provenance"], signal["provenance"])
        self.assertEqual(reading_list["entries"][0]["local_body_path"], "")

    def test_aihot_official_duplicates_keep_independent_official_item(self):
        original = "https://openai.com/index/new-model"
        aihot = {"source_id": "aihot-selected", "items": [{
            "title": "AIHOT 中文模型摘要",
            "url": original + "/?utm_source=aihot",
            "published": "2026-07-18T16:00:00Z",
            "relevance_status": "matched",
            "matched_topics": ["llm"],
            "fulltext_status": "limited",
            "aggregator_url": "https://aihot.news/items/model",
            "guid": "model",
        }]}
        official = {"source_id": "openai-blog", "items": [{
            "title": "Official model announcement",
            "url": original,
            "published": "2026-07-18T16:00:00Z",
            "relevance_status": "always_read",
            "matched_topics": ["ai-agent"],
            "intelligence_department": "first-party-openai",
            "fulltext_status": "limited",
        }]}
        other_rss = {"source_id": "another-discovery-feed", "items": [{
            "title": "Another secondary discovery",
            "url": original,
            "published": "2026-07-18T16:00:00Z",
            "relevance_status": "matched",
            "matched_topics": ["llm"],
        }]}
        for sources in ([aihot, official], [official, aihot], [other_rss, aihot, official]):
            with self.subTest(first_source=sources[0]["source_id"]):
                self.write_json("rss-items.json", {"sources": sources})

                signal = self.module.build_signals(self.run_date, self.root)["signals"][0]

                self.assertEqual(signal["title"], "Official model announcement")
                self.assertEqual(signal["source_id"], "openai-blog")
                self.assertEqual(signal["evidence_level"], "official-source")
                self.assertEqual(signal["topics"], ["ai-agent", "llm"])
                self.assertEqual(len(signal["provenance"]), len(sources))
                by_source = {row["source_id"]: row for row in signal["provenance"]}
                self.assertEqual(by_source["aihot-selected"]["evidence_level"], "secondary-source")
                self.assertEqual(by_source["openai-blog"]["evidence_level"], "official-source")
                self.assertEqual(by_source["aihot-selected"]["discovery_title"], "AIHOT 中文模型摘要")

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

    def test_anthropic_engineering_articles_keep_body_and_boundary(self):
        body_path = self.root / "raw" / self.run_date / "anthropic-engineering" / "inside.md"
        body_path.parent.mkdir(parents=True)
        body_path.write_text("article body", encoding="utf-8")
        self.write_json(
            "official-pages.json",
            {
                "sources": [
                    {
                        "source_id": "anthropic-engineering",
                        "topics": ["agents"],
                        "items": [
                            {
                                "title": "Inside article",
                                "url": "https://www.anthropic.com/engineering/inside",
                                "published": "2026-07-19",
                                "window_status": "inside",
                                "fulltext_status": "ok",
                                "fulltext_path": f"raw/{self.run_date}/anthropic-engineering/inside.md",
                            },
                            {
                                "title": "Unknown-date article",
                                "url": "https://www.anthropic.com/engineering/unknown",
                                "published": "",
                                "window_status": "unknown",
                                "fulltext_status": "skipped",
                            },
                        ],
                    },
                    {
                        "source_id": "claude-blog",
                        "items": [
                            {
                                "title": "Existing index-only behavior",
                                "url": "https://claude.com/blog/existing",
                                "published": "2026-07-19",
                            }
                        ],
                    },
                ]
            },
        )

        payload = self.module.build_signals(self.run_date, self.root)
        articles = [item for item in payload["signals"] if item["source_type"] == "official-page-article"]
        by_title = {item["title"]: item for item in articles}

        self.assertEqual(set(by_title), {"Inside article", "Unknown-date article"})
        self.assertEqual(by_title["Inside article"]["evidence_level"], "official-source")
        self.assertEqual(
            by_title["Inside article"]["content"]["path"],
            f"raw/{self.run_date}/anthropic-engineering/inside.md",
        )
        self.assertEqual(by_title["Unknown-date article"]["content"], {"status": "skipped", "path": ""})
        self.assertIn("boundary row", by_title["Unknown-date article"]["why_read"])
        self.assertIn(f"raw/{self.run_date}/official-pages.json", payload["raw_inputs"])

        reading = self.module.build_reading_list(payload, "2026-07-19T12:00:00+08:00")
        reading_by_title = {item["title"]: item for item in reading["entries"]}
        self.assertEqual(
            reading_by_title["Inside article"]["local_body_path"],
            f"raw/{self.run_date}/anthropic-engineering/inside.md",
        )
        self.assertEqual(reading_by_title["Unknown-date article"]["local_body_path"], "")

    def test_podcast_transcript_uses_guid_identity_and_only_emits_inside_readable_items(self):
        transcript = self.root / "raw" / self.run_date / "podcasts" / "ai-i" / "episode-1.md"
        transcript.parent.mkdir(parents=True)
        transcript.write_text("# Transcript\n\nSpeaker 1 | 00:00 - 00:30\nUseful evidence.", encoding="utf-8")
        self.write_json(
            "podcast-items.json",
            {
                "source_id": "follow-builders",
                "feed_url": "https://raw.githubusercontent.com/example/feed-podcasts.json",
                "raw_feed_path": f"raw/{self.run_date}/podcasts/feed-podcasts.json",
                "episodes": [
                    {
                        "allowed": True,
                        "episode_status": "ok",
                        "show_id": "ai-i-by-every",
                        "show_name": "AI & I by Every",
                        "guid": "episode-1",
                        "title": "Inside readable episode",
                        "published_at": "2026-07-18T16:00:00Z",
                        "window_status": "inside",
                        "canonical_url": "https://example.com/episodes/1",
                        "link_status": "ok",
                        "transcript_status": "ok",
                        "transcript_path": f"raw/{self.run_date}/podcasts/ai-i/episode-1.md",
                        "topics": ["agents"],
                    },
                    {
                        "allowed": True,
                        "episode_status": "ok",
                        "show_id": "ai-i-by-every",
                        "guid": "episode-2",
                        "title": "Inside limited episode",
                        "published_at": "2026-07-19T03:00:00Z",
                        "window_status": "inside",
                        "transcript_status": "limited",
                    },
                    {
                        "allowed": True,
                        "episode_status": "ok",
                        "show_id": "ai-i-by-every",
                        "guid": "episode-3",
                        "title": "Outside episode",
                        "published_at": "2026-07-17T03:00:00Z",
                        "window_status": "outside",
                        "transcript_status": "ok",
                        "transcript_path": f"raw/{self.run_date}/podcasts/ai-i/episode-1.md",
                    },
                ],
            },
        )

        payload = self.module.build_signals(self.run_date, self.root)
        podcasts = [item for item in payload["signals"] if item["source_type"] == "podcast-transcript"]

        self.assertEqual(len(podcasts), 1)
        signal = podcasts[0]
        self.assertEqual(signal["signal_id"], "podcast:ai-i-by-every:episode-1")
        self.assertEqual(signal["evidence_level"], "secondary-source")
        self.assertEqual(signal["content"]["path"], f"raw/{self.run_date}/podcasts/ai-i/episode-1.md")
        self.assertEqual(signal["topics"], ["agents"])
        self.assertTrue(any(item.get("source_type") == "podcast-aggregator-feed" for item in signal["provenance"]))
        self.assertIn(f"raw/{self.run_date}/podcast-items.json", payload["raw_inputs"])

        reading = self.module.build_reading_list(payload, "2026-07-19T12:00:00+08:00")
        self.assertEqual(reading["entries"][0]["signal_id"], "podcast:ai-i-by-every:episode-1")
        self.assertEqual(reading["entries"][0]["provenance"], signal["provenance"])

    def test_podcast_seen_dedup_uses_episode_identity_not_shared_feed_url(self):
        transcript = self.root / "raw" / self.run_date / "podcasts" / "new.md"
        transcript.parent.mkdir(parents=True)
        transcript.write_text("Speaker 1 | 00:00\nNew episode transcript.", encoding="utf-8")
        (self.root / "state").mkdir()
        (self.root / "state" / "seen.json").write_text(
            json.dumps(
                {
                    "items": [
                        {
                            "id": "podcast:ai-i-by-every:old-guid",
                            "first_seen": "2026-07-18",
                            "url": "https://raw.githubusercontent.com/example/feed-podcasts.json",
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        self.write_json(
            "podcast-items.json",
            {
                "source_id": "follow-builders",
                "feed_url": "https://raw.githubusercontent.com/example/feed-podcasts.json",
                "episodes": [
                    {
                        "allowed": True,
                        "episode_status": "ok",
                        "show_id": "ai-i-by-every",
                        "guid": "new-guid",
                        "title": "New unresolved-link episode",
                        "published_at": "2026-07-19T03:00:00Z",
                        "window_status": "inside",
                        "canonical_url": "",
                        "link_status": "limited",
                        "transcript_status": "ok",
                        "transcript_path": f"raw/{self.run_date}/podcasts/new.md",
                    }
                ],
            },
        )

        podcasts = [
            item
            for item in self.module.build_signals(self.run_date, self.root)["signals"]
            if item["source_type"] == "podcast-transcript"
        ]

        self.assertEqual([item["signal_id"] for item in podcasts], ["podcast:ai-i-by-every:new-guid"])


if __name__ == "__main__":
    unittest.main()
