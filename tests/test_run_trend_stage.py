import importlib.util
import json
import re
import sqlite3
import subprocess
import sys
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


class RunTrendStageTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.date = "2026-06-08"
        self.write_text(
            "config/trends.yaml",
            "\n".join(
                [
                    "schema_version: 1",
                    "trends:",
                    "  - id: memory-dream",
                    "    label: Memory & Dream",
                    "    enabled: true",
                    "    timeline: trend/memory-dream.md",
                    "    report_section: Memory & Dream",
                    "  - id: financial-agents",
                    "    label: Financial Agents",
                    "    enabled: true",
                    "    timeline: trend/financial-agents.md",
                    "    report_section: Financial Agents",
                    "  - id: disabled-topic",
                    "    label: Disabled Topic",
                    "    enabled: false",
                    "    timeline: trend/disabled-topic.md",
                    "    report_section: Disabled Topic",
                    "",
                ]
            ),
        )
        self.write_text(
            f"docs/{self.date}-daily-intel.md",
            "\n".join(
                [
                    f"# {self.date} Daily Source Intelligence",
                    "",
                    "## 今日高信号",
                    "- Memory agent evidence is selected for trend follow-up.",
                    "",
                ]
            ),
        )
        self.write_text(
            "trend/memory-dream.md",
            "# Memory & Dream Trend Report\n\n## 当前判断\n\n旧判断仍然可读。\n",
        )
        self.write_text(
            "trend/financial-agents.md",
            "# Financial Agents Trend Report\n\n## 当前判断\n\n暂无新增。\n",
        )

    def tearDown(self):
        self.tmp.cleanup()

    def write_text(self, relative_path, text):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def write_json(self, relative_path, data):
        return self.write_text(
            relative_path,
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        )

    def seed_trend_raw(self):
        self.write_text(
            f"raw/{self.date}/github-trending-readmes/mempalace.md",
            "# MemPalace\n\nPersistent agent memory palace.\n",
        )
        self.write_text(
            f"trend/raw/{self.date}/memory-dream/mempalace.md",
            "# MemPalace\n\nPersistent agent memory palace.\n",
        )
        self.write_text(
            f"trend/raw/{self.date}/memory-dream/rss-summary.md",
            "# Summary only\n\nA partial RSS summary.\n",
        )
        self.write_json(
            f"trend/raw/{self.date}/memory-dream/manifest.json",
            {
                "schema_version": 1,
                "run_date": self.date,
                "trend_id": "memory-dream",
                "status": "new-signal",
                "entries": [
                    {
                        "source_path": f"raw/{self.date}/github-trending-readmes/mempalace.md",
                        "archive_path": f"trend/raw/{self.date}/memory-dream/mempalace.md",
                        "status": "ok",
                        "method": "reuse-daily-raw",
                    },
                    {
                        "source_path": f"raw/{self.date}/rss/rss-summary.json",
                        "archive_path": f"trend/raw/{self.date}/memory-dream/rss-summary.md",
                        "status": "limited",
                        "reason": "Only RSS summary was available.",
                    },
                ],
            },
        )
        self.write_json(
            f"trend/raw/{self.date}/financial-agents/no-new-signal.json",
            {
                "schema_version": 1,
                "run_date": self.date,
                "trend_id": "financial-agents",
                "status": "no-new-signal",
                "reason": "No regulated finance workflow evidence selected today.",
            },
        )

    def connect_rows(self, table):
        db_path = self.root / "state" / "trend-state.sqlite"
        with sqlite3.connect(db_path) as conn:
            conn.row_factory = sqlite3.Row
            return [dict(row) for row in conn.execute(f"SELECT * FROM {table}")]

    def fake_topic_runner(self, returncode=0, legacy_section=False):
        calls = []

        def runner(cmd, **kwargs):
            calls.append((cmd, kwargs))
            if returncode == 0:
                output_path = Path(cmd[cmd.index("--output-last-message") + 1])
                prompt = cmd[-1]
                payload_match = re.search(r"```json\n(.*?)\n```", prompt, flags=re.DOTALL)
                payload = json.loads(payload_match.group(1)) if payload_match else {}
                claims = payload.get("claims", [])
                claim_lines = []
                for claim in claims:
                    refs = json.loads(claim.get("evidence_refs_json") or "[]")
                    ref = refs[0] if refs else ""
                    href = ref.removeprefix("trend/") if ref else ""
                    evidence = f"[消息源]({href})" if href else "-"
                    claim_lines.append(
                        "| {date} | {meaning} | `{claim_id}` | {evidence} | `{status}` |".format(
                            date=claim.get("claim_date", self.date),
                            meaning="短趋势含义：当天消息源已合入长期判断。",
                            claim_id=claim["claim_id"],
                            evidence=evidence,
                            status=claim.get("lifecycle_status", "active"),
                        )
                    )
                if not claim_lines:
                    claim_lines.append(f"| {self.date} | 当天没有新的可提升判断。 | - | - | `no-new-signal` |")
                if legacy_section:
                    output_lines = [
                        "## 自动专题正文",
                        "",
                        "### 本次更新",
                        "- 旧 section-only 输出。",
                        "",
                    ]
                else:
                    output_lines = [
                        "## 本次更新",
                        "",
                        "Phase 2 现在直接重写专题主体正文，并保留 SQL 审计区。",
                        "",
                        "## 当前活跃判断",
                        "",
                        "新增 claim 会进入正文判断，而不是只停留在额外生成区。",
                        "",
                        "## 受限与待验证",
                        "",
                        "仅使用 SQLite、trend raw 和现有 topic 文件，不重新联网扩大证据范围。",
                        "",
                        "## 已替代/削弱/过时判断",
                        "",
                        "本次没有删除旧判断；需要降权的内容只在 lifecycle status 和正文语义里标注。",
                        "",
                        "## 对长期趋势的含义",
                        "",
                        "长期判断可以被压缩和改写，但 SQL 与状态索引继续保留可追溯链路。",
                        "",
                        "## 短时间线",
                        "",
                        "| 日期 | 趋势含义 | Claim ID | 消息源 | 生命周期状态 |",
                        "| --- | --- | --- | --- | --- |",
                        *claim_lines,
                        "",
                        "## 证据入口",
                        "",
                        "- 当前正文中的消息源链接来自 SQLite evidence refs。",
                        "",
                    ]
                output_path.write_text(
                    "\n".join(output_lines),
                    encoding="utf-8",
                )
            return subprocess.CompletedProcess(cmd, returncode, stdout="", stderr="boom" if returncode else "")

        return calls, runner

    def test_migration_creates_core_tables_and_indexes(self):
        module = load_script("run-trend-stage.py")
        with module.connect_db(self.root) as conn:
            module.migrate(conn)
            names = {
                row[0]
                for row in conn.execute(
                    "SELECT name FROM sqlite_master WHERE type IN ('table', 'index')"
                )
            }

        self.assertTrue(
            {
                "trend_candidates",
                "trend_topics",
                "trend_claims",
                "trend_jobs",
                "trend_phase2_runs",
                "idx_trend_candidates_run_date_trend",
                "idx_trend_claims_trend_status",
                "idx_trend_jobs_kind_status",
            }.issubset(names)
        )

    def test_lifecycle_status_enum_rejects_unknown_values(self):
        module = load_script("run-trend-stage.py")

        self.assertEqual(module.validate_lifecycle_status("active"), "active")
        with self.assertRaises(ValueError):
            module.validate_lifecycle_status("deleted")

    def test_phase1_discovers_manifest_no_new_signal_and_limited_candidates(self):
        self.seed_trend_raw()
        module = load_script("run-trend-stage.py")

        candidates = module.run_phase1(self.date, root=self.root)
        rows = sorted(
            self.connect_rows("trend_candidates"),
            key=lambda row: (row["trend_id"], row["candidate_status"], row["archive_path"]),
        )

        self.assertEqual(len(candidates), 3)
        self.assertEqual(
            [(row["trend_id"], row["candidate_status"]) for row in rows],
            [
                ("financial-agents", "no-new-signal"),
                ("memory-dream", "limited"),
                ("memory-dream", "new-signal"),
            ],
        )
        self.assertIn("No regulated finance", rows[0]["boundary_note"])
        self.assertIn("Only RSS summary", rows[1]["boundary_note"])
        self.assertEqual(rows[2]["evidence_level"], "secondary-source")
        self.assertEqual(len(rows[2]["source_content_hash"]), 64)

    def test_verifier_fails_when_status_note_is_missing_for_non_active_claim(self):
        module = load_script("run-trend-stage.py")
        with module.connect_db(self.root) as conn:
            module.migrate(conn)
            module.upsert_trend_claim(
                conn,
                claim_id="claim-replaced",
                trend_id="memory-dream",
                claim_date=self.date,
                claim_text="A replaced claim.",
                evidence_refs=["trend/raw/2026-06-08/memory-dream/mempalace.md"],
                lifecycle_status="replaced",
                replacement_claim_id="claim-new",
                status_note="",
                markdown_anchor="claim-replaced",
            )
        self.seed_trend_raw()
        self.write_text(
            f"trend/reports/{self.date}-trend-report.md",
            "# Trend Report\n\n## Memory & Dream\n\n## Financial Agents\n",
        )
        self.write_text(
            "trend/memory-dream.md",
            "\n".join(
                [
                    "# Memory & Dream Trend Report",
                    "",
                    "## 状态索引 / Claim State Index",
                    "",
                    "| Claim ID | Date | Status | Evidence | Anchor | Note | Replacement |",
                    "| --- | --- | --- | --- | --- | --- | --- |",
                    "| `claim-replaced` | 2026-06-08 | `replaced` | [e](raw/2026-06-08/memory-dream/mempalace.md) | [claim-replaced](#claim-replaced) |  | `claim-new` |",
                    "",
                ]
            ),
        )

        result = module.verify_non_destructive(self.date, root=self.root)

        self.assertFalse(result.ok)
        self.assertTrue(
            any("status_note" in error and "claim-replaced" in error for error in result.errors)
        )

    def test_verifier_fails_when_topic_status_index_loses_sql_claim(self):
        self.seed_trend_raw()
        module = load_script("run-trend-stage.py")
        module.run_phase1(self.date, root=self.root)
        _, runner = self.fake_topic_runner()
        module.run_phase2(self.date, root=self.root, runner=runner)

        memory_topic = self.root / "trend/memory-dream.md"
        memory_topic.write_text(
            memory_topic.read_text(encoding="utf-8").replace("trend-claim-", "missing-claim-"),
            encoding="utf-8",
        )

        result = module.verify_non_destructive(self.date, root=self.root)

        self.assertFalse(result.ok)
        self.assertTrue(any("missing from topic status index" in error for error in result.errors))

    def test_verifier_fails_when_topic_loses_candidate_content(self):
        self.seed_trend_raw()
        module = load_script("run-trend-stage.py")
        module.run_phase1(self.date, root=self.root)
        _, runner = self.fake_topic_runner()
        module.run_phase2(self.date, root=self.root, runner=runner)

        memory_topic = self.root / "trend/memory-dream.md"
        memory_topic.write_text(
            memory_topic.read_text(encoding="utf-8").replace("MemPalace", "内容已丢失"),
            encoding="utf-8",
        )

        result = module.verify_non_destructive(self.date, root=self.root)

        self.assertFalse(result.ok)
        self.assertTrue(any("claim_text" in error for error in result.errors))

    def test_verifier_fails_when_enabled_trend_is_missing_from_daily_report(self):
        self.seed_trend_raw()
        module = load_script("run-trend-stage.py")
        module.run_phase1(self.date, root=self.root)
        self.write_text(
            f"trend/reports/{self.date}-trend-report.md",
            "# Trend Report\n\n## Memory & Dream\n",
        )

        result = module.verify_non_destructive(self.date, root=self.root)

        self.assertFalse(result.ok)
        self.assertTrue(any("financial-agents" in error for error in result.errors))

    def test_managed_topic_body_replace_removes_legacy_body_and_preserves_audit_sections(self):
        module = load_script("run-trend-stage.py")

        existing = "\n".join(
            [
                "# Memory & Dream Trend Report",
                "",
                "## 自动专题正文",
                "",
                "旧自动正文。",
                "",
                "## 当前判断",
                "",
                "旧主体正文。",
                "",
                "## 状态索引",
                "",
                "| Claim ID | 日期 |",
                "| --- | --- |",
                "",
                "## 更新日志",
                "",
                "### 2026-06-08",
                "",
            ]
        )
        replacement = "\n\n".join(
            [
                "## 本次更新\n\n新的主体正文。",
                "## 当前活跃判断\n\n新判断。",
                "## 受限与待验证\n\n边界。",
                "## 已替代/削弱/过时判断\n\n无删除。",
                "## 对长期趋势的含义\n\n新趋势。",
                "## 短时间线\n\n短线。",
                "## 证据入口\n\n消息源。",
            ]
        )

        updated = module.replace_managed_topic_body(existing, replacement)

        self.assertTrue(updated.startswith("# Memory & Dream Trend Report"))
        self.assertIn("新的主体正文", updated)
        self.assertIn("## 状态索引", updated)
        self.assertIn("## 更新日志", updated)
        self.assertNotIn("## 自动专题正文", updated)
        self.assertNotIn("旧自动正文", updated)
        self.assertNotIn("旧主体正文", updated)

    def test_topic_consolidator_command_uses_gpt55_high_readonly(self):
        self.seed_trend_raw()
        module = load_script("run-trend-stage.py")
        candidates = module.run_phase1(self.date, root=self.root)
        with module.connect_db(self.root) as conn:
            module.promote_candidates_to_claims(conn, self.date, candidates)
            conn.commit()
            claims = module.claim_rows(conn)
        calls, runner = self.fake_topic_runner()

        section = module.run_topic_consolidator(
            self.root,
            self.date,
            {"id": "memory-dream", "label": "Memory & Dream", "timeline": "trend/memory-dream.md"},
            [claim for claim in claims if claim["trend_id"] == "memory-dream"],
            [candidate for candidate in candidates if candidate["trend_id"] == "memory-dream"],
            runner=runner,
        )

        cmd, kwargs = calls[0]
        self.assertEqual(cmd[:2], ["codex", "exec"])
        self.assertEqual(cmd[cmd.index("--model") + 1], "gpt-5.5")
        self.assertIn('service_tier="fast"', cmd)
        self.assertIn('model_reasoning_effort="high"', cmd)
        self.assertEqual(cmd[cmd.index("--sandbox") + 1], "read-only")
        self.assertIn("--ephemeral", cmd)
        self.assertIn("--output-last-message", cmd)
        self.assertIs(kwargs["stdin"], module.subprocess.DEVNULL)
        self.assertIn("## 短时间线", section)
        self.assertNotIn("## 自动专题正文", section)

    def test_topic_body_validator_rejects_missing_short_timeline_claim_link_and_legacy_sections(self):
        self.seed_trend_raw()
        module = load_script("run-trend-stage.py")
        candidates = module.run_phase1(self.date, root=self.root)
        memory_candidates = [candidate for candidate in candidates if candidate["trend_id"] == "memory-dream"]
        expected_claim_id = module.claim_id_for_candidate(
            next(candidate for candidate in memory_candidates if candidate["candidate_status"] == "new-signal")
        )
        claims = [
            {
                "claim_id": expected_claim_id,
                "claim_date": self.date,
                "evidence_refs_json": json.dumps([f"trend/raw/{self.date}/memory-dream/mempalace.md"]),
            }
        ]

        errors = module.validate_managed_topic_body(
            "\n".join(
                [
                    "## 本次更新",
                    "",
                    "没有短时间线。",
                    "",
                    "## 当前活跃判断",
                    "",
                    "缺少 claim。",
                    "",
                    "## 受限与待验证",
                    "",
                    "边界。",
                    "",
                    "## 已替代/削弱/过时判断",
                    "",
                    "无。",
                    "",
                    "## 对长期趋势的含义",
                    "",
                    "含义。",
                    "",
                    "## 证据入口",
                    "",
                    "消息源。",
                ]
            ),
            self.date,
            {"id": "memory-dream", "label": "Memory & Dream"},
            claims,
            memory_candidates,
            root=self.root,
            topic_path=self.root / "trend/memory-dream.md",
        )

        self.assertTrue(any("missing required section" in error and "短时间线" in error for error in errors))
        self.assertTrue(any(expected_claim_id in error for error in errors))

        legacy_section_errors = module.validate_managed_topic_body(
            "\n".join(
                [
                    "## 自动专题正文",
                    "",
                    "### 本次更新",
                    f"- `{expected_claim_id}`",
                    "",
                    "### 当前活跃判断",
                    "",
                    "### 受限与待验证",
                    "",
                    "### 已替代/削弱/过时判断",
                    "",
                    "### 对长期趋势的含义",
                    "",
                    "### 证据入口",
                    "",
                    "## 状态索引",
                ]
            ),
            self.date,
            {"id": "memory-dream", "label": "Memory & Dream"},
            claims,
            memory_candidates,
            root=self.root,
            topic_path=self.root / "trend/memory-dream.md",
        )

        self.assertTrue(any("legacy generated body" in error for error in legacy_section_errors))
        self.assertTrue(any("script-owned section" in error for error in legacy_section_errors))

    def test_phase_all_writes_topic_body_reports_sql_and_check_passes(self):
        self.seed_trend_raw()
        module = load_script("run-trend-stage.py")
        _, runner = self.fake_topic_runner()

        status = module.main(
            [
                "--root",
                str(self.root),
                "--date",
                self.date,
                "--phase",
                "all",
            ],
            runner=runner,
        )
        self.assertEqual(status, 0)

        claims = self.connect_rows("trend_claims")
        self.assertEqual(len(claims), 2)
        daily_report = (self.root / f"trend/reports/{self.date}-trend-report.md").read_text(encoding="utf-8")
        memory_topic = (self.root / "trend/memory-dream.md").read_text(encoding="utf-8")
        self.assertIn(f"# {self.date} 趋势报告", daily_report)
        self.assertIn("| 趋势 | 今日状态 | 归档 | 专题报告 |", daily_report)
        self.assertNotIn("Enabled trend", daily_report)
        self.assertIn("## 状态索引", memory_topic)
        self.assertIn("| Claim ID | 日期 | 生命周期状态 | 判断内容 | 证据 | 锚点 | 状态说明 | 替代判断 |", memory_topic)
        self.assertNotIn("| Claim ID | Date | Status | Evidence | Anchor | Note | Replacement |", memory_topic)
        self.assertIn("从 MemPalace 看到 Memory & Dream 新信号", memory_topic)
        self.assertNotIn("signal from MemPalace", memory_topic)
        self.assertNotIn("## 自动专题正文", memory_topic)
        self.assertIn("## 本次更新", memory_topic)
        self.assertIn("## 当前活跃判断", memory_topic)
        self.assertIn("## 受限与待验证", memory_topic)
        self.assertIn("## 已替代/削弱/过时判断", memory_topic)
        self.assertIn("## 对长期趋势的含义", memory_topic)
        self.assertIn("## 短时间线", memory_topic)
        self.assertIn("## 证据入口", memory_topic)
        self.assertIn("[消息源](raw/2026-06-08/memory-dream/mempalace.md)", memory_topic)
        self.assertIn(
            "trend-claim-",
            memory_topic,
        )

        check = module.main(
            [
                "--root",
                str(self.root),
                "--date",
                self.date,
                "--check",
            ],
        )
        self.assertEqual(check, 0)

    def test_phase2_preflight_fails_before_consolidator_when_marker_is_missing(self):
        self.write_text(
            f"trend/raw/{self.date}/memory-dream/mempalace.md",
            "# MemPalace\n\nPersistent agent memory palace.\n",
        )
        self.write_json(
            f"trend/raw/{self.date}/memory-dream/manifest.json",
            {
                "schema_version": 1,
                "run_date": self.date,
                "trend_id": "memory-dream",
                "status": "new-signal",
                "entries": [
                    {
                        "archive_path": f"trend/raw/{self.date}/memory-dream/mempalace.md",
                        "status": "ok",
                    }
                ],
            },
        )
        module = load_script("run-trend-stage.py")
        module.run_phase1(self.date, root=self.root)
        calls, runner = self.fake_topic_runner()

        with self.assertRaises(RuntimeError) as ctx:
            module.run_phase2(self.date, root=self.root, runner=runner)

        self.assertIn("missing trend marker", str(ctx.exception))
        self.assertIn("financial-agents", str(ctx.exception))
        self.assertEqual(calls, [])

    def test_phase2_preflight_fails_when_manifest_and_no_signal_both_exist(self):
        self.seed_trend_raw()
        self.write_json(
            f"trend/raw/{self.date}/financial-agents/manifest.json",
            {
                "schema_version": 1,
                "run_date": self.date,
                "trend_id": "financial-agents",
                "status": "new-signal",
                "entries": [],
            },
        )
        module = load_script("run-trend-stage.py")
        module.run_phase1(self.date, root=self.root)
        calls, runner = self.fake_topic_runner()

        with self.assertRaises(RuntimeError) as ctx:
            module.run_phase2(self.date, root=self.root, runner=runner)

        self.assertIn("both manifest.json and no-new-signal.json", str(ctx.exception))
        self.assertIn("financial-agents", str(ctx.exception))
        self.assertEqual(calls, [])

    def test_phase2_preflight_fails_when_manifest_archive_path_is_missing(self):
        self.seed_trend_raw()
        (self.root / f"trend/raw/{self.date}/memory-dream/mempalace.md").unlink()
        module = load_script("run-trend-stage.py")
        module.run_phase1(self.date, root=self.root)
        calls, runner = self.fake_topic_runner()

        with self.assertRaises(RuntimeError) as ctx:
            module.run_phase2(self.date, root=self.root, runner=runner)

        self.assertIn("missing archive_path", str(ctx.exception))
        self.assertIn("mempalace.md", str(ctx.exception))
        self.assertEqual(calls, [])

    def test_phase2_rewrites_only_trends_with_signal_markers(self):
        self.seed_trend_raw()
        module = load_script("run-trend-stage.py")
        module.run_phase1(self.date, root=self.root)
        calls, runner = self.fake_topic_runner()

        result = module.run_phase2(self.date, root=self.root, runner=runner)

        called_prompts = [call[0][-1] for call in calls]
        self.assertEqual(len(called_prompts), 1)
        self.assertIn('"id": "memory-dream"', called_prompts[0])
        self.assertNotIn('"id": "financial-agents"', called_prompts[0])
        self.assertEqual(result["rewritten_trends"], ["memory-dream"])
        self.assertEqual(result["skipped_rewrite_trends"], ["financial-agents"])
        financial_topic = (self.root / "trend/financial-agents.md").read_text(encoding="utf-8")
        self.assertIn("暂无新增。", financial_topic)
        self.assertIn("## 状态索引", financial_topic)
        self.assertIn("未触发 LLM rewrite", financial_topic)

    def test_phase2_fails_when_topic_consolidator_fails_and_records_error(self):
        self.seed_trend_raw()
        module = load_script("run-trend-stage.py")
        module.run_phase1(self.date, root=self.root)
        _, runner = self.fake_topic_runner(returncode=2)

        with self.assertRaises(RuntimeError):
            module.run_phase2(self.date, root=self.root, runner=runner)

        runs = self.connect_rows("trend_phase2_runs")
        self.assertEqual(runs[0]["status"], "failed")
        self.assertEqual(runs[0]["verification_ok"], 0)
        self.assertIn("topic consolidator failed", runs[0]["error"])

    def test_phase2_fails_when_topic_consolidator_returns_legacy_section_only_output(self):
        self.seed_trend_raw()
        module = load_script("run-trend-stage.py")
        module.run_phase1(self.date, root=self.root)
        _, runner = self.fake_topic_runner(legacy_section=True)

        with self.assertRaises(RuntimeError):
            module.run_phase2(self.date, root=self.root, runner=runner)

        runs = self.connect_rows("trend_phase2_runs")
        self.assertEqual(runs[0]["status"], "failed")
        self.assertIn("legacy generated body", runs[0]["error"])

    def test_verifier_fails_when_topic_body_loses_current_claim(self):
        self.seed_trend_raw()
        module = load_script("run-trend-stage.py")
        module.run_phase1(self.date, root=self.root)
        _, runner = self.fake_topic_runner()
        module.run_phase2(self.date, root=self.root, runner=runner)

        claims = self.connect_rows("trend_claims")
        memory_claim = next(claim for claim in claims if claim["trend_id"] == "memory-dream")
        memory_topic = self.root / "trend/memory-dream.md"
        topic_text = memory_topic.read_text(encoding="utf-8")
        body = module.managed_topic_body(topic_text)
        memory_topic.write_text(
            topic_text.replace(body, body.replace(memory_claim["claim_id"], "missing-current-claim")),
            encoding="utf-8",
        )

        result = module.verify_non_destructive(self.date, root=self.root)

        self.assertFalse(result.ok)
        self.assertTrue(any("missing from topic managed body" in error for error in result.errors))

    def test_verifier_fails_when_short_timeline_loses_current_evidence_link(self):
        self.seed_trend_raw()
        module = load_script("run-trend-stage.py")
        module.run_phase1(self.date, root=self.root)
        _, runner = self.fake_topic_runner()
        module.run_phase2(self.date, root=self.root, runner=runner)

        memory_topic = self.root / "trend/memory-dream.md"
        topic_text = memory_topic.read_text(encoding="utf-8")
        memory_topic.write_text(
            topic_text.replace("raw/2026-06-08/memory-dream/mempalace.md", "raw/2026-06-08/memory-dream/missing.md"),
            encoding="utf-8",
        )

        result = module.verify_non_destructive(self.date, root=self.root)

        self.assertFalse(result.ok)
        self.assertTrue(any("missing evidence link" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
