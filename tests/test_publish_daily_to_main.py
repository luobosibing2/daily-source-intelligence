import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_script():
    path = ROOT / "scripts" / "publish-daily-to-main.py"
    spec = importlib.util.spec_from_file_location("publish_daily_to_main", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(cwd, *args):
    result = subprocess.run(
        ["git", "-C", str(cwd), *args],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


class PublishDailyToMainTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.origin = self.root / "origin.git"
        self.source = self.root / "source"
        self.main = self.root / "main"
        self.date = "2026-07-16"
        subprocess.run(["git", "init", "--bare", str(self.origin)], check=True, capture_output=True)
        self.source.mkdir()
        git(self.source, "init", "-b", "main")
        git(self.source, "config", "user.email", "test@example.com")
        git(self.source, "config", "user.name", "Test User")
        git(self.source, "remote", "add", "origin", str(self.origin))
        self.write_source("README.md", "test\n")
        git(self.source, "add", "README.md")
        git(self.source, "commit", "-m", "initial")
        git(self.source, "push", "-u", "origin", "main")
        git(self.source, "checkout", "-b", "develop")
        git(self.source, "worktree", "add", str(self.main), "main")

    def tearDown(self):
        self.tmp.cleanup()

    def write_source(self, relative, content):
        path = self.source / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_publish_pushes_only_the_dated_report_to_main(self):
        module = load_script()
        report = self.write_source(
            f"docs/{self.date}-daily-intel.md",
            "# Daily report\n\nOnly this file belongs on main.\n",
        )

        result = module.publish(self.date, source_root=self.source, main_worktree=self.main, push=True)

        self.assertEqual(result["status"], "published")
        self.assertEqual(
            git(self.source, "show", f"origin/main:docs/{self.date}-daily-intel.md"),
            report.read_text(encoding="utf-8").rstrip(),
        )
        self.assertEqual(git(self.main, "show", "--format=", "--name-only", "HEAD"), f"docs/{self.date}-daily-intel.md")
        self.assertEqual(git(self.main, "status", "--porcelain"), "")

    def test_dirty_main_is_rejected_before_copy(self):
        module = load_script()
        self.write_source(f"docs/{self.date}-daily-intel.md", "# Daily report\n")
        (self.main / "unrelated.txt").write_text("do not overwrite\n", encoding="utf-8")

        with self.assertRaises(module.PublishError):
            module.publish(self.date, source_root=self.source, main_worktree=self.main, push=True)

        self.assertFalse((self.main / f"docs/{self.date}-daily-intel.md").exists())
        self.assertEqual((self.main / "unrelated.txt").read_text(encoding="utf-8"), "do not overwrite\n")

    def test_publish_commits_complete_bundle_only(self):
        module = load_script()
        files = {
            f"docs/{self.date}-daily-intel.md": "# Daily\n",
            f"docs/{self.date}-daily-intel.index.json": "{}\n",
            f"docs/{self.date}-daily-intel.html": "<html>daily</html>\n",
            "docs/index.html": "<html>index</html>\n",
        }
        for path, content in files.items():
            self.write_source(path, content)

        result = module.publish(self.date, source_root=self.source, main_worktree=self.main, push=False)

        self.assertEqual(result["status"], "committed")
        self.assertEqual(
            set(git(self.main, "show", "--format=", "--name-only", "HEAD").splitlines()),
            set(files),
        )
        self.assertEqual(len(result["target_reports"]), 4)

    def test_partial_bundle_is_rejected(self):
        module = load_script()
        self.write_source(f"docs/{self.date}-daily-intel.md", "# Daily\n")
        self.write_source(f"docs/{self.date}-daily-intel.html", "<html></html>\n")

        with self.assertRaises(module.PublishError):
            module.publish(self.date, source_root=self.source, main_worktree=self.main, push=False)

    def test_dry_run_does_not_fetch_or_sync(self):
        module = load_script()
        self.write_source(f"docs/{self.date}-daily-intel.md", "# Daily\n")

        def unexpected_sync(_):
            self.fail("dry-run must not sync main")

        module.sync_main_from_origin = unexpected_sync
        result = module.publish(
            self.date,
            source_root=self.source,
            main_worktree=self.main,
            push=True,
            dry_run=True,
        )

        self.assertEqual(result["status"], "dry-run")
        self.assertFalse((self.main / f"docs/{self.date}-daily-intel.md").exists())

    def test_wrong_source_branch_is_rejected(self):
        module = load_script()
        self.write_source(f"docs/{self.date}-daily-intel.md", "# Daily report\n")
        git(self.source, "checkout", "-b", "feature")

        with self.assertRaises(module.PublishError):
            module.publish(self.date, source_root=self.source, main_worktree=self.main, push=True)


if __name__ == "__main__":
    unittest.main()
