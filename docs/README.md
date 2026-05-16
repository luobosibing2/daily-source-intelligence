# Daily Reports

每日自动化将中文日报写入此目录，文件名格式：

`YYYY-MM-DD-daily-intel.md`

日报必须标注每条 X/Twitter 相关内容的证据等级：

- `direct-x`：直接 `x.com/.../status/...` 原帖链接。
- `secondary-source`：可信媒体、博客、GitHub issue 或官方页面转述。

本 workflow 不使用 Exa MCP；如果 `twitterapi.io` 缺失或失败，日报只记录覆盖失败，不用搜索线索替代直接 X 证据。

GitHub Trending 每日热门项目写入 `raw/YYYY-MM-DD/github-trending.json`，对应 README 原文归档到 `raw/YYYY-MM-DD/github-trending-readmes/`。日报中作为 `secondary-source` discovery signal 使用；上榜只能说明当天 GitHub Trending 页面可见热度，不代表官方发布、质量背书或长期趋势。

GitHub 项目总结必须写成读者能看懂的项目介绍，而不是标签堆叠。每个 repo 至少讲清楚：它到底是什么、解决什么具体问题、给谁用或怎么用、README 能确认的核心机制/功能边界/部署形态、为什么今天值得记录、还有哪些风险或待验证点。必须把 Trending description 和 README 合成一段自然语言归纳，不要写成 `Trending description:` / `README 归纳:` 这种固定字段拆分。遇到金融、交易、浏览器绕检测、凭据路由、自动执行、隐私或安全敏感项目时，必须单独写清风险边界；README 缺失时只能列为待读候选，不写机制总结。

RSS/Atom 高信号不能只凭 feed 摘要写强判断。collector 会用 [`../config/topics.yaml`](../config/topics.yaml) 与 source `topics` 标记 `relevance_status`，相关条目会继续打开原文并归档到 `raw/YYYY-MM-DD/rss-fulltext/<source-id>/`。日报引用 RSS 高信号时必须检查 `fulltext_status`：`ok` 可以写已读原文，`limited` / `failed` / `skipped` 只能写成摘要线索并说明边界。

OpenAI 与 Claude Code 是一手重点源，地位不同于普通 RSS/blog。配置了 `fulltext_policy: always` 的 source 不按普通 topic match 跳过；只要 feed/release Atom 里有条目，就写入 `relevance_status=always_read` 并提取可用正文。日报必须放到“一手重点源 / First-party OpenAI & Claude Code”部门，保留 `intelligence_department`、`fulltext_status` 和本地归档链接。

网页或公开文件的 `curl` 抓取失败、Cloudflare/JS challenge、正文太短或不可读时，collector 会尝试 `autocli read`。如果成功，本地归档使用 `.autocli.md`，证据方法写作 `autocli-read`；如果仍失败，日报必须保留 `needs-fulltext` / `limited` 边界。

## 长期趋势分析

日报正文不包含 trend 小节。每日任务在日报完成后，按 [`../config/trends.yaml`](../config/trends.yaml) 更新 [`../trend/`](../trend/) 下的独立每日趋势分析报告，以及每个 enabled trend 配置的长期专题报告输出路径，例如 `trend/memory-dream.md`、`trend/financial-agents.md` 和 `trend/forward-deployed-engineering.md`。

## RSS 扩展来源

2026-05-01 根据 Karpathy 关于 RSS/Atom 的帖子，参考 emschwartz 的 HN 2025 热门博客 OPML，向 `config/sources.yaml` 增加了一组 curated RSS feeds。当前保留范围是 AI/LLM/agent、AI coding、独立开发/产品增长，以及泛 infra/security/systems/ops；Apple 评论、泛前端随笔、写作/元数据来源已移除。来源归档见：

`daily-source-intelligence/raw/2026-05-01/rss-subscription-source-karpathy.md`
