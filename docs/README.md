# Daily Reports

每日自动化将中文日报写入此目录，文件名格式：

`YYYY-MM-DD-daily-intel.md`

日报必须标注每条 X/Twitter 相关内容的证据等级：

- `direct-x`：直接 `x.com/.../status/...` 原帖链接。
- `secondary-source`：可信媒体、博客、GitHub issue 或官方页面转述。

本 workflow 不使用 Exa MCP；如果 `twitterapi.io` 缺失或失败，日报只记录覆盖失败，不用搜索线索替代直接 X 证据。

## RSS 扩展来源

2026-05-01 根据 Karpathy 关于 RSS/Atom 的帖子，参考 emschwartz 的 HN 2025 热门博客 OPML，向 `config/sources.yaml` 增加了一组 curated RSS feeds。当前保留范围是 AI/LLM/agent、AI coding、独立开发/产品增长，以及泛 infra/security/systems/ops；Apple 评论、泛前端随笔、写作/元数据来源已移除。来源归档见：

`daily-source-intelligence/raw/2026-05-01/rss-subscription-source-karpathy.md`
