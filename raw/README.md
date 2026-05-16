# Raw Archive

每日自动化将当天采集到的原始材料写入 `YYYY-MM-DD/` 子目录。

预期文件包括：

- `manifest.json`：采集范围、来源、命中数量、失败来源。
- `rss-items.json`：RSS/Atom 条目。
- `github-items.json`：GitHub release、tag 或 changelog 条目。
- `official-pages.json`：官方页面检查结果。
- `twitterapi-io-results.json`：`twitterapi.io` X/Twitter 直接证据或 skipped/failed 状态。
- `rss-fulltext/<source-id>/`：RSS/Atom 条目命中关注方向后的原文归档；`.html` 是 `curl` 原始响应，`.extracted.md` 是本地文本提取，`.autocli.md` 是 `autocli read` fallback 提取的正文。
- `github-release-fulltext/<source-id>/`：一手 release Atom 源的正文归档；`.atom.md` 是从 GitHub release Atom `<content>` 提取的可读正文。
- `official-page-text/`：官方页面在 `curl` limited/failed 后的可读正文归档或诊断快照。
- 原文 HTML、Markdown 或文本提取文件：对高信号材料和相关 RSS 条目保存。

辅助提取文件只用于本地检索，不替代官方原文链接。
