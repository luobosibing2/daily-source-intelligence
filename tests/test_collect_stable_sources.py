import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


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


if __name__ == "__main__":
    unittest.main()
