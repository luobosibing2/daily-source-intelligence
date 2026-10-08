import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
import urllib.parse
from pathlib import Path
from unittest import mock

import yaml


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = "e4efaac15dbd2154dc2f342a439c56cd267339e6"
NEW_HANDLES = {
    "swyx",
    "joshwoodward",
    "bcherny",
    "thsottiaux",
    "petergyang",
    "thenanyu",
    "realmadhuguru",
    "amandaaskell",
    "_catwu",
    "trq212",
    "googlelabs",
    "amasad",
    "rauchg",
    "alexalbert__",
    "levie",
    "ryolu_",
    "garrytan",
    "mattturck",
    "zarazhangrui",
    "nikunj",
    "danshipper",
    "adityaag",
    "claudeai",
}


def load_script():
    path = ROOT / "scripts" / "collect-twitterapi-io.py"
    spec = importlib.util.spec_from_file_location("collect_twitterapi_io", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CollectTwitterApiIoTest(unittest.TestCase):
    def test_config_enables_exact_new_handles_without_priority_or_default_topics(self):
        payload = yaml.safe_load((ROOT / "config" / "sources.yaml").read_text(encoding="utf-8"))
        active = [account for account in payload["x_accounts"] if account.get("enabled") is True]
        by_handle = {str(account["handle"]).casefold(): account for account in active}

        self.assertEqual(len(active), 50)
        self.assertEqual(len(by_handle), 50)
        self.assertTrue(NEW_HANDLES.issubset(by_handle))
        for handle in NEW_HANDLES:
            account = by_handle[handle]
            self.assertIs(account.get("enabled"), True)
            self.assertIs(account.get("priority"), False)
            self.assertNotIn("topics", account)
            self.assertIn(SNAPSHOT, account.get("note", ""))

    def test_dry_run_lists_all_50_active_sources(self):
        module = load_script()
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            code = module.main(["--date", "2099-01-01", "--dry-run"])
        payload = json.loads(stdout.getvalue())

        self.assertEqual(code, 0)
        self.assertEqual(payload["event"], "x_collection_plan")
        self.assertEqual(len(payload["sources"]), 50)
        self.assertEqual(len(set(payload["sources"])), 50)

    def test_case_insensitive_duplicate_fails_before_credentials_are_read(self):
        module = load_script()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sources = root / "sources.yaml"
            sources.write_text(
                """x_accounts:
  - id: first
    handle: ExampleAI
    enabled: true
  - id: second
    handle: exampleai
    enabled: true
twitterapi_io:
  enabled: true
""",
                encoding="utf-8",
            )
            stderr = io.StringIO()
            with (
                mock.patch.object(module, "SOURCES", sources),
                mock.patch.object(module, "RAW_ROOT", root / "raw"),
                mock.patch.object(module, "get_api_key") as get_api_key,
                contextlib.redirect_stderr(stderr),
            ):
                code = module.main(["--date", "2099-01-01"])

            self.assertEqual(code, 2)
            self.assertIn("duplicate enabled X handle(s)", stderr.getvalue())
            self.assertIn("first, second", stderr.getvalue())
            get_api_key.assert_not_called()
            self.assertFalse((root / "raw").exists())

    def test_last_tweets_request_keeps_read_only_reply_boundary(self):
        module = load_script()
        with mock.patch.object(module, "curl_json", return_value={}) as curl_json:
            module.get_last_tweets("ExampleAI", "secret")

        url, api_key = curl_json.call_args.args
        query = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        self.assertEqual(api_key, "secret")
        self.assertEqual(query, {"userName": ["ExampleAI"], "includeReplies": ["false"]})


if __name__ == "__main__":
    unittest.main()
