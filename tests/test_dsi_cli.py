import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path


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


if __name__ == "__main__":
    unittest.main()
