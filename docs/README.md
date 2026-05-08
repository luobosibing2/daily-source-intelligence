# Daily Reports

每日自动化将中文日报写入此目录，文件名格式：

`YYYY-MM-DD-daily-intel.md`

日报必须标注每条 X/Twitter 相关内容的证据等级：

- `direct-x`：直接 `x.com/.../status/...` 原帖链接。
- `secondary-source`：可信媒体、博客、GitHub issue 或官方页面转述。

本 workflow 不使用 Exa MCP；如果 `twitterapi.io` 缺失或失败，日报只记录覆盖失败，不用搜索线索替代直接 X 证据。

GitHub Trending 每日热门项目写入 `raw/YYYY-MM-DD/github-trending.json`，对应 README 原文归档到 `raw/YYYY-MM-DD/github-trending-readmes/`。日报中作为 `secondary-source` discovery signal 使用；上榜只能说明当天 GitHub Trending 页面可见热度，不代表官方发布、质量背书或长期趋势。项目总结必须把 Trending description 和 README 合成一段自然语言归纳：先说它解决什么问题，再说 README 能确认的功能边界、使用场景或机制；不要写成固定字段拆分。

## 长期趋势分析

日报正文不包含 trend 小节。每日任务在日报完成后，按 [`../config/trends.yaml`](../config/trends.yaml) 更新 [`../trend/`](../trend/) 下的独立每日趋势分析报告，以及两个长期专题报告输出路径：`trend/memory-dream.md` 和 `trend/financial-agents.md`。

## RSS 扩展来源

2026-05-01 根据 Karpathy 关于 RSS/Atom 的帖子，参考 emschwartz 的 HN 2025 热门博客 OPML，向 `config/sources.yaml` 增加了一组 curated RSS feeds。当前保留范围是 AI/LLM/agent、AI coding、独立开发/产品增长，以及泛 infra/security/systems/ops；Apple 评论、泛前端随笔、写作/元数据来源已移除。来源归档见：

`daily-source-intelligence/raw/2026-05-01/rss-subscription-source-karpathy.md`
