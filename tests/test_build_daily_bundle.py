import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module():
    path = ROOT / "scripts" / "build-daily-bundle.py"
    spec = importlib.util.spec_from_file_location("build_daily_bundle", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BuildDailyBundleTest(unittest.TestCase):
    def test_bundle_links_report_sha_and_builds_static_index(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            date = "2026-07-19"
            (root / "docs").mkdir()
            (root / "raw" / date).mkdir(parents=True)
            report = root / "docs" / f"{date}-daily-intel.md"
            report.write_text(
                "# 日报\n\n"
                "<!-- hidden audit marker -->\n\n"
                "## 今日高信号\n\n"
                "| 等级 | 信号 |\n"
                "| --- | --- |\n"
                "| 高 | **重点** `signal` |\n\n"
                "- [证据](../raw/2026-07-19/signals.json)\n",
                encoding="utf-8",
            )
            (root / "raw" / date / "signals.json").write_text(
                json.dumps({"counts": {"total": 3, "inside_window": 2, "unknown_time_boundary": 1}}),
                encoding="utf-8",
            )

            result = module.build_bundle(date, root=root)

            payload = json.loads((root / result["index_json"]).read_text(encoding="utf-8"))
            html = (root / result["daily_html"]).read_text(encoding="utf-8")
            self.assertEqual(payload["signals"]["counts"]["total"], 3)
            self.assertEqual(len(payload["report"]["sha256"]), 64)
            self.assertIn("<strong>3</strong><span>唯一信号", html)
            self.assertIn("<table>", html)
            self.assertIn("<strong>重点</strong> <code>signal</code>", html)
            self.assertNotIn("hidden audit marker", html)
            self.assertIn('class="metrics-grid"', html)
            self.assertIn('id="今日高信号"', html)
            self.assertIn('href="#今日高信号"', html)
            self.assertIn("<small>本地证据</small>", html)
            self.assertNotIn('href="../raw/', html)
            site_index = (root / "docs" / "index.html").read_text(encoding="utf-8")
            self.assertIn(date, site_index)
            self.assertIn('class="landing-hero"', site_index)
            self.assertIn('class="report-card report-card-latest"', site_index)
            self.assertIn('href="#content"', site_index)


if __name__ == "__main__":
    unittest.main()
