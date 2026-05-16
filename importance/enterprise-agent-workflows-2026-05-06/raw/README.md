# Raw Archive: Enterprise Agent Workflows 2026-05-06

本目录归档 2026-05-06 前后 OpenAI 与 Claude/Anthropic 关于 enterprise agent workflow、Managed Agents、企业 AI adoption 的一手材料与辅助检索文件。

## 官方原文与本地归档

| 来源 | 官方 URL | 本地归档 | 说明 |
| --- | --- | --- | --- |
| OpenAI / Singular Bank | https://openai.com/index/singular-bank/ | [`openai-singular-bank.autocli.md`](openai-singular-bank.autocli.md), [`openai-singular-bank.html`](openai-singular-bank.html) | `autocli.md` 是可读正文；`html` 是 curl 原始响应，本轮为 Cloudflare challenge 页面。 |
| OpenAI / Uber | https://openai.com/index/uber/ | [`openai-uber.autocli.md`](openai-uber.autocli.md), [`openai-uber.html`](openai-uber.html) | `autocli.md` 是可读正文；`html` 是 curl 原始响应，本轮为 Cloudflare challenge 页面。 |
| OpenAI / B2B Signals | https://openai.com/index/introducing-b2b-signals/ | [`openai-b2b-signals.autocli.md`](openai-b2b-signals.autocli.md), [`openai-b2b-signals.html`](openai-b2b-signals.html) | `autocli.md` 是可读正文；`html` 是 curl 原始响应，本轮为 Cloudflare challenge 页面。 |
| Claude Blog / Managed Agents | https://claude.com/blog/new-in-claude-managed-agents | [`claude-managed-agents.html`](claude-managed-agents.html), [`claude-managed-agents.extracted.md`](claude-managed-agents.extracted.md) | curl 获取到完整 HTML；`.extracted.md` 是辅助检索文本。 |
| Anthropic GitHub README / financial services | https://github.com/anthropics/financial-services | [`anthropics-financial-services-readme.md`](anthropics-financial-services-readme.md) | 来自 daily-source-intelligence 的 GitHub Trending README 归档副本。 |
| Daily source RSS evidence | N/A | [`daily-source-openai-rss-items-2026-05-07.json`](daily-source-openai-rss-items-2026-05-07.json) | OpenAI RSS 原始采集输出副本。 |
| Daily official page evidence | N/A | [`daily-source-official-pages-2026-05-07.json`](daily-source-official-pages-2026-05-07.json) | Claude Blog official page 采集输出副本。 |

## 派生文件说明

- `*.autocli.md`：通过 `autocli read` 从官方 URL 提取的正文 Markdown，适合检索和引用。
- `*.extracted.md`：从 HTML 机械抽取的辅助文本，适合检索，不替代官方原文。
- OpenAI 的 `*.html` 是 curl 原始响应，但本轮命中 Cloudflare challenge；可读证据以 `*.autocli.md` 和 RSS JSON 为准。
- Claude 的 `claude-managed-agents.html` 是完整官方页面 HTML；`claude-managed-agents.extracted.md` 是辅助检索版本。
