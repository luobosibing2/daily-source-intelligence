import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    path = ROOT / "scripts" / name
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ExtractCodexSessionsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "repo"
        self.codex_home = Path(self.tmp.name) / "codex"
        self.date = "2026-05-23"
        self.sessions_dir = self.codex_home / "sessions" / "2026" / "05" / "23"
        self.sessions_dir.mkdir(parents=True)
        self.root.mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def write_jsonl(self, name, records):
        path = self.sessions_dir / name
        path.write_text(
            "\n".join(json.dumps(record, ensure_ascii=False) for record in records) + "\n",
            encoding="utf-8",
        )
        return path

    def message(self, role, text, timestamp="2026-05-23T08:00:00.000Z"):
        return {
            "timestamp": timestamp,
            "type": "response_item",
            "payload": {
                "type": "message",
                "role": role,
                "content": [{"type": "input_text", "text": text}],
            },
        }

    def session_meta(self, session_id, cwd):
        return {
            "timestamp": "2026-05-23T07:56:34.886Z",
            "type": "session_meta",
            "payload": {
                "id": session_id,
                "timestamp": "2026-05-23T07:56:26.457Z",
                "cwd": cwd,
                "source": "vscode",
                "thread_source": "user",
            },
        }

    def test_extracts_real_user_questions_and_writes_raw_json(self):
        self.write_jsonl(
            "rollout-a.jsonl",
            [
                self.session_meta("session-a", str(self.root)),
                self.message(
                    "user",
                    "# AGENTS.md instructions for /tmp/repo\n\n<INSTRUCTIONS>skip me</INSTRUCTIONS>",
                ),
                self.message(
                    "user",
                    "Run the daily source intelligence workflow for /Users/chengyizhou/code/research-docs.",
                ),
                self.message(
                    "user",
                    "<turn_aborted> The user interrupted the previous turn on purpose. </turn_aborted>",
                ),
                self.message("developer", "developer text should not appear"),
                self.message("assistant", "assistant text should not appear"),
                self.message("user", "ChromeDevTools/chrome-devtools-mcp 这个 mcp 安装一下"),
            ],
        )
        self.write_jsonl(
            "rollout-b.jsonl",
            [
                self.session_meta("session-b", "/Users/chengyizhou/code/research-docs"),
                self.message(
                    "user",
                    "\n".join(
                        [
                            "# Applications mentioned by the user:",
                            "<appshot app=\"Google Chrome\">very large browser dump</appshot>",
                            "",
                            "## My request for Codex:",
                            "朋友, 看完这个帮我想想有没有什么方案?",
                            "<image>empty rendered image marker</image>",
                        ]
                    ),
                    timestamp="2026-05-23T09:00:00.000Z",
                ),
            ],
        )

        module = load_script("extract-codex-sessions.py")
        result = module.extract_for_date(
            self.date,
            root=self.root,
            codex_home=self.codex_home,
        )

        self.assertEqual(result["session_count"], 2)
        self.assertEqual(result["question_count"], 2)
        texts = [
            question["text"]
            for session in result["sessions"]
            for question in session["user_questions"]
        ]
        self.assertEqual(
            texts,
            [
                "ChromeDevTools/chrome-devtools-mcp 这个 mcp 安装一下",
                "朋友, 看完这个帮我想想有没有什么方案?",
            ],
        )
        output = self.root / "reviews" / "raw" / self.date / "codex-sessions.json"
        self.assertTrue(output.exists())
        saved = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(saved["question_count"], 2)


if __name__ == "__main__":
    unittest.main()
