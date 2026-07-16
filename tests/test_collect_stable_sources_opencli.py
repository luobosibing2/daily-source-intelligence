import importlib.util
import subprocess
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def load_collect_stable_sources():
    path = ROOT / "scripts" / "collect-stable-sources.py"
    spec = importlib.util.spec_from_file_location("collect_stable_sources", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class OpenCliFallbackTest(unittest.TestCase):
    def test_opencli_read_markdown_uses_web_read_stdout(self):
        module = load_collect_stable_sources()
        calls = []

        def fake_run(cmd, **kwargs):
            calls.append((cmd, kwargs))
            return subprocess.CompletedProcess(
                cmd,
                0,
                stdout=b"# Example\n\nThis is a long enough readable markdown body for fallback testing.\n" * 8,
                stderr=b"",
            )

        with patch.object(module.subprocess, "run", side_effect=fake_run):
            result = module.opencli_read_markdown("https://example.com/article")

        self.assertTrue(result["ok"])
        self.assertEqual(result["method"], "opencli-read")
        self.assertEqual(calls[0][0], [
            "opencli",
            "web",
            "read",
            "--url",
            "https://example.com/article",
            "--stdout",
            "true",
            "--download-images",
            "false",
            "-f",
            "md",
        ])

    def test_opencli_read_markdown_reports_missing_binary(self):
        module = load_collect_stable_sources()

        with patch.object(module.subprocess, "run", side_effect=FileNotFoundError):
            result = module.opencli_read_markdown("https://example.com/article")

        self.assertFalse(result["ok"])
        self.assertEqual(result["error"], "opencli executable not found")

    def test_opencli_read_markdown_passes_profile_when_configured(self):
        module = load_collect_stable_sources()
        module.OPENCLI_PROFILE = "t26bdsv2"
        calls = []

        def fake_run(cmd, **kwargs):
            calls.append((cmd, kwargs))
            return subprocess.CompletedProcess(
                cmd,
                0,
                stdout=b"# Example\n\nThis readable markdown body confirms the profile flag is preserved.\n" * 8,
                stderr=b"",
            )

        with patch.object(module.subprocess, "run", side_effect=fake_run):
            result = module.opencli_read_markdown("https://example.com/article")

        self.assertTrue(result["ok"])
        self.assertEqual(calls[0][0][:3], ["opencli", "--profile", "t26bdsv2"])


if __name__ == "__main__":
    unittest.main()
