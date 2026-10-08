import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module():
    path = ROOT / "scripts" / "collect-podcasts.py"
    spec = importlib.util.spec_from_file_location("collect_podcasts", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CollectPodcastsTest(unittest.TestCase):
    def setUp(self):
        self.module = load_module()
        self.source = {
            "id": "follow-builders",
            "name": "follow-builders Podcast Transcript Feed",
            "url": "https://raw.example/feed-podcasts.json",
            "provider": "follow-builders",
            "topics": ["llm"],
            "shows": [
                {
                    "id": "ai-and-i",
                    "name": "AI & I by Every",
                    "rss_url": "https://rss.example/ai-and-i.xml",
                    "url": "https://www.youtube.com/playlist?list=playlist",
                    "enabled": True,
                    "topics": ["llm", "ai-agent"],
                },
            ],
        }

    def test_window_status_uses_beijing_day(self):
        self.assertEqual(self.module.window_status("2026-09-03T16:00:00Z", "2026-09-04"), "inside")
        self.assertEqual(self.module.window_status("2026-09-03T15:59:59Z", "2026-09-04"), "outside")
        self.assertEqual(self.module.window_status("not-a-date", "2026-09-04"), "unknown")

    def test_rss_link_requires_exact_guid_and_ignores_enclosure(self):
        rss = b"""
        <rss><channel>
          <item>
            <guid>other</guid>
            <link>https://example.test/other</link>
          </item>
          <item>
            <guid>episode-1</guid>
            <link>https://example.test/episode-1</link>
            <enclosure url="https://cdn.example/episode-1.mp3" type="audio/mpeg" />
          </item>
        </channel></rss>
        """
        self.assertEqual(self.module.rss_episode_link(rss, "episode-1"), "https://example.test/episode-1")
        self.assertEqual(self.module.rss_episode_link(rss, "episode"), "")

    def test_collect_source_archives_feed_transcript_and_resolves_playlist_by_rss_guid(self):
        run_date = "2026-09-04"
        feed = {
            "generatedAt": "2026-09-04T06:00:00Z",
            "lookbackHours": 336,
            "errors": None,
            "podcasts": [
                {
                    "name": "AI & I by Every",
                    "title": "Episode One",
                    "guid": "episode-1",
                    "url": "https://www.youtube.com/playlist?list=playlist",
                    "publishedAt": "2026-09-03T16:00:00Z",
                    "transcript": "Speaker 1 | 00:00 - 00:30\n" + ("A concrete transcript point. " * 20),
                },
                {
                    "name": "AI & I by Every",
                    "title": "Episode Two",
                    "guid": "episode-2",
                    "url": "https://podcasters.spotify.com/pod/show/show/episodes/episode-2",
                    "publishedAt": "2026-09-02T16:00:00Z",
                    "transcript": "",
                },
                {
                    "name": "Unknown Show",
                    "title": "Ignored Show",
                    "guid": "episode-3",
                    "url": "https://www.youtube.com/@unknown",
                    "publishedAt": "2026-09-03T16:00:00Z",
                    "transcript": "Speaker 1 | 00:00\n" + ("Unknown show transcript. " * 20),
                },
            ],
        }
        rss = b"""
        <rss><channel><item>
          <guid>episode-1</guid>
          <link>https://pod.example/episodes/episode-1</link>
          <enclosure url="https://cdn.example/episode-1.mp3" type="audio/mpeg" />
        </item></channel></rss>
        """
        calls = []

        def fetcher(url):
            calls.append(url)
            if url == self.source["url"]:
                return {"ok": True, "status": 200, "body": json.dumps(feed).encode("utf-8")}
            if url == self.source["shows"][0]["rss_url"]:
                return {"ok": True, "status": 200, "body": rss}
            raise AssertionError(f"unexpected request: {url}")

        with tempfile.TemporaryDirectory() as tmp:
            payload = self.module.collect_source(self.source, run_date, root=Path(tmp), fetcher=fetcher)
            self.assertEqual(payload["status"], "ok")
            self.assertEqual(payload["upstream_generated_at"], "2026-09-04T06:00:00Z")
            self.assertEqual(payload["lookback_hours"], 336)
            self.assertEqual(payload["coverage"]["offered"], 3)
            self.assertEqual(payload["coverage"]["allowed"], 2)
            self.assertEqual(payload["coverage"]["inside"], 1)
            self.assertEqual(payload["coverage"]["outside"], 1)
            self.assertEqual(payload["coverage"]["unconfigured"], 1)
            self.assertEqual(payload["coverage"]["transcript_ok"], 1)
            self.assertEqual(payload["coverage"]["transcript_limited"], 1)
            self.assertEqual(payload["coverage"]["link_ok"], 2)
            self.assertEqual(payload["coverage"]["link_limited"], 0)
            by_guid = {episode["guid"]: episode for episode in payload["episodes"]}
            episode = by_guid["episode-1"]
            self.assertEqual(episode["episode_id"], "podcast:ai-and-i:episode-1")
            self.assertEqual(episode["episode_status"], "ok")
            self.assertEqual(episode["canonical_url"], "https://pod.example/episodes/episode-1")
            self.assertEqual(episode["link_status"], "ok")
            self.assertTrue(episode["transcript_path"])
            transcript_path = Path(tmp) / episode["transcript_path"]
            self.assertTrue(transcript_path.is_file())
            self.assertIn("Speaker 1", transcript_path.read_text(encoding="utf-8"))
            self.assertEqual(by_guid["episode-2"]["episode_status"], "limited")
            self.assertEqual(calls, [self.source["url"], self.source["shows"][0]["rss_url"]])
            snapshot = Path(tmp) / payload["raw_feed_path"]
            self.assertEqual(snapshot.read_bytes(), json.dumps(feed).encode("utf-8"))

    def test_empty_feed_is_ok_and_feed_errors_are_partial(self):
        def fetcher(url):
            return {"ok": True, "status": 200, "body": json.dumps({"podcasts": [], "errors": None}).encode("utf-8")}

        with tempfile.TemporaryDirectory() as tmp:
            payload = self.module.collect_source(self.source, "2026-09-04", root=Path(tmp), fetcher=fetcher)
            self.assertEqual(payload["status"], "ok")
            self.assertEqual(payload["coverage"]["offered"], 0)
            self.assertEqual(payload["episodes"], [])

        def partial_fetcher(url):
            return {
                "ok": True,
                "status": 200,
                "body": json.dumps({"podcasts": [], "errors": ["one show failed"]}).encode("utf-8"),
            }

        with tempfile.TemporaryDirectory() as tmp:
            payload = self.module.collect_source(self.source, "2026-09-04", root=Path(tmp), fetcher=partial_fetcher)
            self.assertEqual(payload["status"], "partial")
            self.assertEqual(payload["coverage"]["upstream_error_count"], 1)

    def test_duplicate_guid_writes_the_winning_transcript_and_matching_hash(self):
        short = "Speaker 1 | 00:00\nshort transcript"
        long = "Speaker 1 | 00:00\n" + ("Longer winning transcript. " * 30)
        feed = {
            "podcasts": [
                {
                    "name": "AI & I by Every",
                    "title": "Same Episode",
                    "guid": "same-guid",
                    "url": "https://podcasters.spotify.com/pod/show/show/episodes/same",
                    "publishedAt": "2026-09-04T00:00:00Z",
                    "transcript": long,
                },
                {
                    "name": "AI & I by Every",
                    "title": "Same Episode",
                    "guid": "same-guid",
                    "url": "https://podcasters.spotify.com/pod/show/show/episodes/same",
                    "publishedAt": "2026-09-04T00:00:00Z",
                    "transcript": short,
                },
            ]
        }

        def fetcher(url):
            return {"ok": True, "status": 200, "body": json.dumps(feed).encode("utf-8")}

        with tempfile.TemporaryDirectory() as tmp:
            payload = self.module.collect_source(self.source, "2026-09-04", root=Path(tmp), fetcher=fetcher)
            self.assertEqual(len(payload["episodes"]), 1)
            episode = payload["episodes"][0]
            path = Path(tmp) / episode["transcript_path"]
            body = path.read_text(encoding="utf-8").rstrip("\n")
            self.assertEqual(body, long.strip())
            self.assertEqual(episode["transcript_chars"], len(body))
            self.assertEqual(episode["transcript_sha256"], self.module.sha256_text(body))

    def test_fetch_and_schema_failures_are_failed(self):
        with tempfile.TemporaryDirectory() as tmp:
            payload = self.module.collect_source(
                self.source,
                "2026-09-04",
                root=Path(tmp),
                fetcher=lambda url: {"ok": False, "status": 503, "body": b"", "error": "HTTP 503"},
            )
            self.assertEqual(payload["status"], "failed")
            self.assertEqual(payload["errors"], ["HTTP 503"])

        with tempfile.TemporaryDirectory() as tmp:
            payload = self.module.collect_source(
                self.source,
                "2026-09-04",
                root=Path(tmp),
                fetcher=lambda url: {"ok": True, "status": 200, "body": b"not-json"},
            )
            self.assertEqual(payload["status"], "failed")
            self.assertIn("Invalid JSON feed", payload["errors"][0])


if __name__ == "__main__":
    unittest.main()
