import contextlib
import hashlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]


def load_module():
    path = ROOT / "scripts" / "dsi.py"
    spec = importlib.util.spec_from_file_location("dsi_cli", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DsiCliTest(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_channel_aliases_expand(self):
        self.assertEqual(self.module.expand_channels(["stable"]), self.module.STABLE_CHANNELS)
        self.assertEqual(self.module.expand_channels(["all"]), self.module.ALL_CHANNELS)
        self.assertIn("podcasts", self.module.STABLE_CHANNELS)

    def test_source_requires_one_concrete_channel(self):
        with self.assertRaises(ValueError):
            self.module.parse_sources(["rss:openai-blog"], {"rss", "x"})
        self.assertEqual(
            self.module.parse_sources(["rss:openai-blog"], {"rss"}),
            {"rss": ["openai-blog"]},
        )

    def test_run_dry_run_prints_plan_without_writes(self):
        state = ROOT / "raw" / "2099-01-01" / "run-state.json"
        before = state.exists()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = self.module.main(
                ["run", "--date", "2099-01-01", "--channel", "rss", "--source", "rss:openai-blog", "--dry-run"]
            )
        payload = json.loads(output.getvalue())
        self.assertEqual(code, 0)
        self.assertEqual(payload["channels"], ["rss"])
        self.assertEqual(state.exists(), before)

    def test_podcast_dry_run_accepts_follow_builders_source(self):
        state = ROOT / "raw" / "2099-01-02" / "run-state.json"
        before = state.exists()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = self.module.main(
                [
                    "run",
                    "--date",
                    "2099-01-02",
                    "--channel",
                    "podcasts",
                    "--source",
                    "podcasts:follow-builders",
                    "--dry-run",
                ]
            )
        payload = json.loads(output.getvalue())
        self.assertEqual(code, 0)
        self.assertEqual(payload["channels"], ["podcasts"])
        self.assertEqual(payload["sources"], {"podcasts": ["follow-builders"]})
        self.assertEqual(state.exists(), before)

    def test_resume_requires_matching_output_hashes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            date = "2026-07-19"
            raw = root / "raw" / date
            raw.mkdir(parents=True)
            output = raw / "rss-items.json"
            output.write_text("{}", encoding="utf-8")
            fingerprint = "input"
            self.module.write_json(
                raw / "run-state.json",
                {
                    "collection": {
                        "status": "ok",
                        "input_sha256": fingerprint,
                        "outputs": {"rss": self.module.sha256_path(output)},
                    }
                },
            )
            self.assertTrue(self.module.resume_hit(root, date, {"rss"}, fingerprint))
            output.write_text("changed", encoding="utf-8")
            self.assertFalse(self.module.resume_hit(root, date, {"rss"}, fingerprint))

    def test_prepare_resume_requires_matching_input_and_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            date = "2026-07-19"
            (root / "raw" / date).mkdir(parents=True)
            (root / "docs").mkdir()
            (root / "reviews").mkdir()
            (root / "state").mkdir()
            (root / "docs" / f"{date}-daily-intel.md").write_text("# Daily", encoding="utf-8")
            for relative in self.module.prepare_output_hashes(root, date):
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(relative, encoding="utf-8")
            fingerprint = self.module.prepare_fingerprint(root, date)
            self.module.write_json(
                root / "raw" / date / "run-state.json",
                {
                    "prepare": {
                        "status": "ok",
                        "input_sha256": fingerprint,
                        "outputs": self.module.prepare_output_hashes(root, date),
                    }
                },
            )

            self.assertTrue(self.module.prepare_resume_hit(root, date, fingerprint))
            (root / "docs" / f"{date}-daily-intel.html").write_text("changed", encoding="utf-8")
            self.assertFalse(self.module.prepare_resume_hit(root, date, fingerprint))

    def test_resume_rejects_missing_output_even_when_empty_hash_matches(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            date = "2099-01-01"
            self.module.write_json(root / "raw" / date / "run-state.json", {
                "collection": {"status": "ok", "input_sha256": "input", "outputs": {"x": ""}},
            })
            self.assertFalse(self.module.resume_hit(root, date, {"x"}, "input"))

    def test_missing_x_key_aborts_prepare_and_cannot_resume_legacy_success(self):
        spec = importlib.util.spec_from_file_location("x_collector", ROOT / "scripts/collect-twitterapi-io.py")
        collector = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(collector)
        for existing in (False, True):
            for legacy_state in (False, True):
                with self.subTest(existing=existing, legacy_state=legacy_state), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    date = "2099-01-01"
                    raw = root / "raw" / date
                    raw.mkdir(parents=True)
                    if existing:
                        self.module.write_json(raw / "twitterapi-io-results.json", {"accounts": [
                            {"account_id": "selected", "handle": "Selected", "status": "ok", "tweets": [{"id": "stale"}]},
                        ]})
                    if legacy_state:
                        # Pre-fix fingerprint: missing-key runs could record either stale or empty output hashes.
                        payload = {
                            "run_date": date, "channels": ["x"], "sources": {"x": ["selected"]},
                            "config": {"sources": "", "topics": ""},
                        }
                        legacy_fingerprint = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
                        self.module.write_json(raw / "run-state.json", {"collection": {
                            "status": "ok", "input_sha256": legacy_fingerprint,
                            "outputs": self.module.output_hashes(root, date, {"x"}),
                        }})
                    args = self.module.build_parser().parse_args([
                        "run", "--root", str(root), "--date", date, "--channel", "x",
                        "--source", "x:selected", "--resume",
                    ])
                    def run_collector(command_root, command, env=None):
                        self.assertEqual(command_root, root.resolve())
                        self.assertEqual(command[1], "scripts/collect-twitterapi-io.py")
                        return collector.main(command[2:])
                    with (
                        mock.patch.object(collector, "RAW_ROOT", root / "raw"),
                        mock.patch.object(collector, "parse_accounts", return_value=[{"id": "selected", "handle": "Selected"}]),
                        mock.patch.object(collector, "get_api_key", return_value=None),
                        mock.patch.object(collector, "collect_account") as collect,
                        mock.patch.object(self.module, "run_command", side_effect=run_collector) as run,
                        mock.patch.object(self.module, "prepare", return_value=0) as prepare,
                        contextlib.redirect_stdout(io.StringIO()),
                    ):
                        self.assertNotEqual(self.module.run_collection(args), 0)
                        self.assertNotEqual(self.module.run_collection(args), 0)
                    self.assertEqual(run.call_count, 2)
                    prepare.assert_not_called()
                    collect.assert_not_called()
                    state = self.module.read_json(raw / "run-state.json", {})
                    self.assertEqual(state["collection"]["status"], "failed")
                    fingerprint = self.module.collection_fingerprint(root, date, {"x"}, {"x": ["selected"]})
                    self.assertFalse(self.module.resume_hit(root, date, {"x"}, fingerprint))
                    self.assertEqual(self.module.read_json(raw / "twitterapi-io-results.json", {})["accounts"][0]["tweets"], [])

    def test_successful_x_collection_records_state_and_resumes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            date = "2099-01-01"
            args = self.module.build_parser().parse_args([
                "run", "--root", str(root), "--date", date, "--channel", "x", "--resume",
            ])
            def write_output(*args, **kwargs):
                self.module.write_json(root / "raw" / date / "twitterapi-io-results.json", {"status": "ok", "accounts": []})
                return 0
            with (
                mock.patch.object(self.module, "run_command", side_effect=write_output) as run,
                mock.patch.object(self.module, "prepare", return_value=0) as prepare,
                contextlib.redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(self.module.run_collection(args), 0)
                self.assertEqual(self.module.run_collection(args), 0)
            self.assertEqual(run.call_count, 1)
            self.assertEqual(prepare.call_count, 2)


if __name__ == "__main__":
    unittest.main()
