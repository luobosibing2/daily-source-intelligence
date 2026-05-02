# Raw Archive

每日自动化将当天采集到的原始材料写入 `YYYY-MM-DD/` 子目录。

预期文件包括：

- `manifest.json`：采集范围、来源、命中数量、失败来源。
- `rss-items.json`：RSS/Atom 条目。
- `github-items.json`：GitHub release、tag 或 changelog 条目。
- `official-pages.json`：官方页面检查结果。
- `twitterapi-io-results.json`：`twitterapi.io` X/Twitter 直接证据或 skipped/failed 状态。
- 原文 HTML、Markdown 或文本提取文件：仅对高信号材料保存。

辅助提取文件只用于本地检索，不替代官方原文链接。
