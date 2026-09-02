import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def load_module():
    path = ROOT / "scripts" / "collect-stable-sources.py"
    spec = importlib.util.spec_from_file_location("collect_stable_sources", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CollectStableSourcesTest(unittest.TestCase):
    def test_partial_source_merge_keeps_unselected_records(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "rss-items.json"
            path.write_text(
                json.dumps({"sources": [{"source_id": "keep", "status": "ok"}, {"source_id": "replace", "status": "failed"}]}),
                encoding="utf-8",
            )
            payload = {"sources": [{"source_id": "replace", "status": "ok"}]}

            merged = module.merge_selected_sources(path, payload, {"replace"})

            by_id = {item["source_id"]: item for item in merged["sources"]}
            self.assertEqual(by_id["keep"]["status"], "ok")
            self.assertEqual(by_id["replace"]["status"], "ok")

    def test_parse_anthropic_engineering_items_reads_visible_and_embedded_dates(self):
        module = load_module()
        html = """
        <article class="ArticleList__article ArticleList__featured">
          <a href="/engineering/featured"><h2>Featured article</h2></a>
        </article>
        <article class="ArticleList__article">
          <a href="/engineering/daily"><h3>Daily article</h3><div class="card__date">Sep 03, 2026</div></a>
        </article>
        <article class="ArticleList__article">
          <a href="/engineering/daily"><h3>Duplicate daily article</h3><div class="card__date">Sep 03, 2026</div></a>
        </article>
        <script>{\"publishedOn\":\"2026-09-02\",\"slug\":{\"current\":\"featured\"}}</script>
        """

        items = module.parse_anthropic_engineering_items(html)

        self.assertEqual(len(items), 2)
        by_url = {item["url"]: item for item in items}
        self.assertEqual(by_url["https://www.anthropic.com/engineering/featured"]["title"], "Featured article")
        self.assertEqual(by_url["https://www.anthropic.com/engineering/featured"]["published"], "2026-09-02")
        self.assertEqual(by_url["https://www.anthropic.com/engineering/daily"]["published"], "Sep 03, 2026")

    def test_anthropic_engineering_zero_new_is_ok_when_index_cards_parse(self):
        module = load_module()
        index_html = self.anthropic_index_html("Apr 23, 2026")
        with tempfile.TemporaryDirectory() as tmp:
            module.ROOT = Path(tmp)
            output_dir = Path(tmp) / "raw" / "2026-09-03"
            with patch.object(module, "curl_text", return_value={"ok": True, "status": 0, "body": index_html, "stderr": ""}):
                result = module.collect_official_pages([self.anthropic_source()], output_dir, run_date="2026-09-03")[0]

            self.assertEqual(result["status"], "ok")
            self.assertEqual(result["index_status"], "ok")
            self.assertEqual(result["index_card_count"], 1)
            self.assertEqual(result["items"], [])
            self.assertTrue((Path(tmp) / result["index_snapshot_path"]).is_file())

    def test_anthropic_engineering_parser_loss_is_limited_not_zero_new(self):
        module = load_module()
        index_html = "<html><title>Engineering</title><main>Layout changed</main></html>"
        with tempfile.TemporaryDirectory() as tmp:
            module.ROOT = Path(tmp)
            output_dir = Path(tmp) / "raw" / "2026-09-03"
            with patch.object(module, "curl_text", return_value={"ok": True, "status": 0, "body": index_html, "stderr": ""}):
                result = module.collect_official_pages([self.anthropic_source()], output_dir, run_date="2026-09-03")[0]

            self.assertEqual(result["status"], "limited")
            self.assertEqual(result["index_status"], "limited")
            self.assertEqual(result["index_card_count"], 0)
            self.assertIn("no valid article cards", result["reason"])

    def test_anthropic_engineering_index_opencli_fallback_is_limited(self):
        module = load_module()
        fallback_body = "# Engineering\n\n" + ("Readable index snapshot. " * 20)
        with tempfile.TemporaryDirectory() as tmp:
            module.ROOT = Path(tmp)
            output_dir = Path(tmp) / "raw" / "2026-09-03"
            with patch.object(
                module,
                "curl_text",
                return_value={"ok": False, "status": 28, "body": "", "stderr": "timeout"},
            ), patch.object(
                module,
                "opencli_read_markdown",
                return_value={"ok": True, "body": fallback_body, "method": "opencli-read", "attempts": 1},
            ):
                result = module.collect_official_pages([self.anthropic_source()], output_dir, run_date="2026-09-03")[0]

            self.assertEqual(result["status"], "limited")
            self.assertEqual(result["index_status"], "limited")
            self.assertEqual(result["index_card_count"], 0)
            self.assertEqual(result["fetch_method"], "opencli-read")
            self.assertTrue((Path(tmp) / result["index_snapshot_path"]).is_file())

    def test_anthropic_engineering_index_challenge_archives_raw_and_readable_snapshots(self):
        module = load_module()
        challenge = "<html><title>Just a moment...</title><p>Cloudflare challenge</p></html>"
        fallback_body = "# Engineering\n\n" + ("Readable index snapshot. " * 20)
        with tempfile.TemporaryDirectory() as tmp:
            module.ROOT = Path(tmp)
            output_dir = Path(tmp) / "raw" / "2026-09-03"
            with patch.object(
                module,
                "curl_text",
                return_value={"ok": True, "status": 0, "body": challenge, "stderr": ""},
            ), patch.object(
                module,
                "opencli_read_markdown",
                return_value={"ok": True, "body": fallback_body, "method": "opencli-read", "attempts": 1},
            ):
                result = module.collect_official_pages([self.anthropic_source()], output_dir, run_date="2026-09-03")[0]

            self.assertEqual(result["status"], "limited")
            self.assertEqual(result["index_status"], "limited")
            self.assertTrue((Path(tmp) / result["index_snapshot_path"]).is_file())
            self.assertTrue((Path(tmp) / result["index_readable_path"]).is_file())
            self.assertNotEqual(result["index_snapshot_path"], result["index_readable_path"])

    def test_anthropic_engineering_fetches_only_inside_window_article(self):
        module = load_module()
        index_html = self.anthropic_index_html("Sep 03, 2026")
        article_html = "<html><title>Article</title><main>" + ("Detailed engineering evidence. " * 20) + "</main></html>"
        responses = [
            {"ok": True, "status": 0, "body": index_html, "stderr": ""},
            {"ok": True, "status": 0, "body": article_html, "stderr": ""},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            module.ROOT = Path(tmp)
            output_dir = Path(tmp) / "raw" / "2026-09-03"
            with patch.object(module, "curl_text", side_effect=responses) as mocked_curl:
                result = module.collect_official_pages([self.anthropic_source()], output_dir, run_date="2026-09-03")[0]

            self.assertEqual(mocked_curl.call_count, 2)
            item = result["items"][0]
            self.assertEqual(item["window_status"], "inside")
            self.assertEqual(item["fulltext_status"], "ok")
            self.assertEqual(item["fulltext_method"], "curl")
            self.assertTrue((Path(tmp) / item["raw_html_path"]).is_file())
            self.assertTrue((Path(tmp) / item["fulltext_path"]).is_file())
            self.assertEqual(result["article_fulltext_counts"], {"ok": 1, "limited": 0, "failed": 0})

    def test_anthropic_engineering_uses_opencli_fallback_for_article_body(self):
        module = load_module()
        index_html = self.anthropic_index_html("Sep 03, 2026")
        responses = [
            {"ok": True, "status": 0, "body": index_html, "stderr": ""},
            {"ok": True, "status": 0, "body": "<html><title>Just a moment...</title><p>Cloudflare challenge</p></html>", "stderr": ""},
        ]
        fallback_body = "# Daily article\n\n" + ("Readable engineering transcript. " * 20)
        with tempfile.TemporaryDirectory() as tmp:
            module.ROOT = Path(tmp)
            output_dir = Path(tmp) / "raw" / "2026-09-03"
            with patch.object(module, "curl_text", side_effect=responses), patch.object(
                module,
                "opencli_read_markdown",
                return_value={"ok": True, "body": fallback_body, "method": "opencli-read", "attempts": 1},
            ):
                result = module.collect_official_pages([self.anthropic_source()], output_dir, run_date="2026-09-03")[0]

            item = result["items"][0]
            self.assertEqual(item["fulltext_status"], "ok")
            self.assertEqual(item["fulltext_method"], "opencli-read")
            self.assertTrue((Path(tmp) / item["fulltext_path"]).is_file())
            self.assertIn("limited/challenge", item["fallback_reason"])

    def test_anthropic_engineering_records_failed_article_body(self):
        module = load_module()
        index_html = self.anthropic_index_html("Sep 03, 2026")
        responses = [
            {"ok": True, "status": 0, "body": index_html, "stderr": ""},
            {"ok": False, "status": 28, "body": "", "stderr": "timeout"},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            module.ROOT = Path(tmp)
            output_dir = Path(tmp) / "raw" / "2026-09-03"
            with patch.object(module, "curl_text", side_effect=responses), patch.object(
                module,
                "opencli_read_markdown",
                return_value={"ok": False, "error": "browser unavailable"},
            ):
                result = module.collect_official_pages([self.anthropic_source()], output_dir, run_date="2026-09-03")[0]

            item = result["items"][0]
            self.assertEqual(item["fulltext_status"], "failed")
            self.assertEqual(item["fulltext_method"], "curl")
            self.assertNotIn("fulltext_path", item)
            self.assertIn("browser unavailable", item["fulltext_error"])
            self.assertEqual(result["article_fulltext_counts"], {"ok": 0, "limited": 0, "failed": 1})

    def test_anthropic_engineering_unknown_date_is_boundary_without_body_fetch(self):
        module = load_module()
        index_html = self.anthropic_index_html("")
        with tempfile.TemporaryDirectory() as tmp:
            module.ROOT = Path(tmp)
            output_dir = Path(tmp) / "raw" / "2026-09-03"
            with patch.object(module, "curl_text", return_value={"ok": True, "status": 0, "body": index_html, "stderr": ""}) as mocked_curl:
                result = module.collect_official_pages([self.anthropic_source()], output_dir, run_date="2026-09-03")[0]

            self.assertEqual(mocked_curl.call_count, 1)
            item = result["items"][0]
            self.assertEqual(item["window_status"], "unknown")
            self.assertEqual(item["fulltext_status"], "skipped")
            self.assertIn("publication date is unknown", item["fulltext_reason"])

    @staticmethod
    def anthropic_source():
        return {
            "id": "anthropic-engineering",
            "name": "Anthropic Engineering",
            "url": "https://www.anthropic.com/engineering",
            "enabled": True,
        }

    @staticmethod
    def anthropic_index_html(published):
        date_html = f'<div class="ArticleList__date">{published}</div>' if published else ""
        return f"""
        <html><title>Engineering | Anthropic</title><body>
          <article class="ArticleList__article">
            <a href="/engineering/daily"><h3>Daily article</h3>{date_html}</a>
          </article>
        </body></html>
        """


if __name__ == "__main__":
    unittest.main()
