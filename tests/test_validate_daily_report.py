import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module():
    path = ROOT / "scripts" / "validate-daily-report.py"
    spec = importlib.util.spec_from_file_location("validate_daily_report", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ValidateDailyReportTest(unittest.TestCase):
    def setUp(self):
        self.module = load_module()
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.date = "2026-07-19"
        (self.root / "docs").mkdir()
        (self.root / "reviews").mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def seed(self, report_counts=(1, 0), audit_counts=(1, 0), disposition="covered_in_report"):
        report = (
            "# Daily\n\n"
            f"<!-- dsi-candidate-audit: covered={report_counts[0]} missed={report_counts[1]} -->\n"
        )
        report_path = self.root / "docs" / f"{self.date}-daily-intel.md"
        report_path.write_text(report, encoding="utf-8")
        rows = []
        for index in range(audit_counts[0]):
            rows.append({"candidate_id": f"c{index}", "category": "rss", "status": "covered", "disposition": "covered_in_report"})
        for index in range(audit_counts[1]):
            rows.append(
                {
                    "candidate_id": f"m{index}",
                    "category": "official-link-candidate",
                    "status": "missed",
                    "disposition": disposition,
                }
            )
        audit = {
            "daily_report": f"docs/{self.date}-daily-intel.md",
            "daily_report_sha256": hashlib.sha256(report.encode("utf-8")).hexdigest(),
            "counts": {"total": len(rows), "covered": audit_counts[0], "missed": audit_counts[1]},
            "rows": rows,
        }
        (self.root / "reviews" / f"{self.date}-candidate-audit.json").write_text(json.dumps(audit), encoding="utf-8")
        (self.root / "reviews" / f"{self.date}-candidate-audit.md").write_text("# Audit\n", encoding="utf-8")
        return report_path

    def test_matching_report_and_audit_pass(self):
        self.seed()
        result = self.module.validate(self.date, root=self.root, strict=True)
        self.assertTrue(result["ok"])

    def test_report_count_mismatch_is_rejected(self):
        self.seed(report_counts=(12, 69), audit_counts=(16, 65), disposition="deferred")
        result = self.module.validate(self.date, root=self.root)
        self.assertFalse(result["ok"])
        self.assertIn("report covered=12 missed=69", "\n".join(result["errors"]))

    def test_report_change_breaks_sha(self):
        report_path = self.seed()
        report_path.write_text("changed", encoding="utf-8")
        result = self.module.validate(self.date, root=self.root)
        self.assertFalse(result["ok"])
        self.assertIn("SHA256", "\n".join(result["errors"]))

    def test_missed_official_candidate_needs_disposition(self):
        self.seed(report_counts=(0, 1), audit_counts=(0, 1), disposition="")
        result = self.module.validate(self.date, root=self.root)
        self.assertFalse(result["ok"])
        self.assertIn("require disposition", "\n".join(result["errors"]))

    def test_strict_missed_official_article_needs_disposition_and_note(self):
        self.seed(report_counts=(0, 1), audit_counts=(0, 1), disposition="deferred")
        audit_path = self.root / "reviews" / f"{self.date}-candidate-audit.json"
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        audit["rows"][0]["category"] = "official-page-article"
        audit["rows"][0]["disposition_note"] = ""
        audit_path.write_text(json.dumps(audit), encoding="utf-8")

        non_strict = self.module.validate(self.date, root=self.root, strict=False)
        strict = self.module.validate(self.date, root=self.root, strict=True)

        self.assertTrue(non_strict["ok"])
        self.assertFalse(strict["ok"])
        self.assertIn("disposition and disposition note", "\n".join(strict["errors"]))

        audit["rows"][0]["disposition_note"] = "Not material to today's themes."
        audit_path.write_text(json.dumps(audit), encoding="utf-8")
        resolved = self.module.validate(self.date, root=self.root, strict=True)
        self.assertTrue(resolved["ok"])

    def test_strict_missed_podcast_needs_disposition(self):
        self.seed(report_counts=(0, 1), audit_counts=(0, 1), disposition="")
        audit_path = self.root / "reviews" / f"{self.date}-candidate-audit.json"
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        audit["rows"][0]["category"] = "podcast-transcript"
        audit_path.write_text(json.dumps(audit), encoding="utf-8")

        self.assertTrue(self.module.validate(self.date, root=self.root, strict=False)["ok"])
        strict = self.module.validate(self.date, root=self.root, strict=True)
        self.assertFalse(strict["ok"])
        self.assertIn("missed podcast transcripts require disposition", "\n".join(strict["errors"]))

        audit["rows"][0]["disposition"] = "read_not_relevant"
        audit_path.write_text(json.dumps(audit), encoding="utf-8")
        self.assertTrue(self.module.validate(self.date, root=self.root, strict=True)["ok"])

    def test_missed_rows_cannot_claim_covered_in_report_even_with_a_note(self):
        for category in ("official-link-candidate", "official-page-article", "podcast-transcript", "rss"):
            with self.subTest(category=category):
                self.seed(report_counts=(0, 1), audit_counts=(0, 1), disposition="covered_in_report")
                path = self.root / "reviews" / f"{self.date}-candidate-audit.json"
                audit = json.loads(path.read_text())
                audit["rows"][0]["category"] = category
                audit["rows"][0]["disposition_note"] = "Previously covered."
                path.write_text(json.dumps(audit))
                result = self.module.validate(self.date, root=self.root, strict=True)
                self.assertFalse(result["ok"])
                self.assertIn("missed candidates cannot use covered_in_report", "\n".join(result["errors"]))


if __name__ == "__main__":
    unittest.main()
