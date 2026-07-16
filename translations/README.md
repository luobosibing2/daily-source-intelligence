# Retired Chinese Reading Translations

本目录只保留历史中文译读稿产物。Daily Source Intelligence 已移除中文译读生成能力。

从 2026-06-16 起，workflow 不再为 `trend/raw/YYYY-MM-DD/<trend-id>/` 或日报“今日高信号”中的本地归档材料生成 `.zh.md` 译读稿，也不再维护翻译 manifest、index、shard 或检查阶段。证据真相源仍然是 [`../raw/`](../raw/) 与 [`../trend/raw/`](../trend/raw/) 中的本地归档，以及日报和 trend report 中列出的官方 URL。

## 历史产物

旧日期下可能仍存在：

- `translations/YYYY-MM-DD/manifest.json`
- `translations/YYYY-MM-DD/index.md`
- `translations/YYYY-MM-DD/<trend-id>/<source-stem>.zh.md`
- `translations/YYYY-MM-DD/daily-high-signal/<source-stem>.zh.md`

这些文件只是历史派生阅读材料，不应作为新工作流的输入，也不应作为证据真相源。

## 退役边界

不要恢复旧的翻译 runner、target discovery、Codex shard、manifest/check 或“skipped”占位流程。未来日报和 trend 只写中文分析正文；如需阅读原文，直接使用 `raw/` 与 `trend/raw/` 归档材料。
