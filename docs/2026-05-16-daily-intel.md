# 2026-05-16 Daily Source Intelligence

## 采集范围

- 运行时间：2026-05-16 Asia/Shanghai，本轮写入 [`../raw/2026-05-16/`](../raw/2026-05-16/)。
- 稳定来源：RSS/Atom 31 个源，31 个成功；GitHub releases 6 个源，6 个通过 Atom feed 成功；GitHub Trending 1 个源成功，解析 10 个每日热门 repo；official pages 4 个源，2 个成功、2 个 limited、0 个 failed。
- X/Twitter：通过 `twitterapi.io` read endpoint 成功采集，顶层状态 `ok`；26 个账号均返回 `ok`，保留 131 条 direct-x 原始条目。
- 状态更新：[`../raw/2026-05-16/manifest.json`](../raw/2026-05-16/manifest.json)、[`../state/source-health.json`](../state/source-health.json)、[`../state/seen.json`](../state/seen.json) 已由 `update-state.py` 更新；本轮 `seen_added=44`，累计 719 条。
- 本次没有使用 Exa MCP、登录态浏览器、X/Twitter 账号凭证、写操作 endpoint、posting、liking、following 或 DM。
- 本地归档：[`../raw/2026-05-16/rss-items.json`](../raw/2026-05-16/rss-items.json)、[`../raw/2026-05-16/github-items.json`](../raw/2026-05-16/github-items.json)、[`../raw/2026-05-16/github-trending.json`](../raw/2026-05-16/github-trending.json)、[`../raw/2026-05-16/github-trending-readmes/`](../raw/2026-05-16/github-trending-readmes/)、[`../raw/2026-05-16/official-pages.json`](../raw/2026-05-16/official-pages.json)、[`../raw/2026-05-16/twitterapi-io-results.json`](../raw/2026-05-16/twitterapi-io-results.json)。

## 今日高信号

1. OpenAI Blog RSS 新增 `A new personal finance experience in ChatGPT`，并由 `@sama` direct-x 转发 ChatGPT app 预览信息。它把 ChatGPT 推到个人金融账户连接、上下文化 insights 和 guidance，但当前只来自 RSS 摘要与 direct-x，全文 HTML 触发 Cloudflare challenge，不能细化权限、数据处理和投资建议边界。【有明确证据支撑 / official-source RSS + direct-x / limited-fulltext】
2. OpenAI Blog RSS 新增 `Databricks brings GPT-5.5 to enterprise agent workflows`。这是 enterprise agent workflow 与 benchmark/客户平台结合的官方信号，但本地全文归档同样受 Cloudflare challenge 限制，不能只凭摘要推断 Databricks 具体部署架构。【有明确证据支撑 / official-source RSS / limited-fulltext】
3. Claude Blog official page 新增 `Deploying Claude across the legal industry`。这说明 Anthropic 今天继续按行业场景包装 Claude adoption，尤其 legal workflow；本轮已归档 HTML，但未抽出完整可读正文，趋势判断只按行业部署线索处理。【有明确证据支撑 / official-page metadata + archived HTML / limited】
4. GitHub Trending Daily 中 `anthropics/skills` 上榜，README 明确把 skills 定义为可动态加载的 instructions、scripts 和 resources，并给出 Claude Code plugin、Claude.ai 和 API 使用路径。这是 Agent Skills 从概念走向官方 repo / marketplace / API surface 的强 discovery signal。【有明确证据支撑 / secondary-source】
5. GitHub Trending Daily 中 `czlonkowski/n8n-mcp` 上榜，README 记录它给 AI assistants 提供 n8n 节点、属性、操作、模板和 AI tools 的结构化知识，并明确警告不要直接用 AI 改 production workflows。这是 workflow automation + MCP + agent safety 的高信号。【有明确证据支撑 / secondary-source】
6. GitHub Trending Daily 中 `NVIDIA-AI-Blueprints/video-search-and-summarization` 上榜，README 把 VSS 定位为 GPU 加速 vision agents / video analytics reference architecture，含 real-time video intelligence、downstream analytics、agentic/offline processing 和 MCP 工具接口。这是 enterprise vision-agent deployment substrate 线索。【有明确证据支撑 / secondary-source】
7. `@gregisenberg` direct-x 长帖把 agent memory、skills files、local models、regulated verticals、YAML config/org chart、human approval latency 等放在同一组创业观察里。这是 direct-x 思想线索，不是产品事实；价值在于它和当天 `anthropics/skills`、`OpenHuman`、`n8n-mcp` 同向。【有明确证据支撑 / direct-x】
8. `@AnthropicAI` direct-x 发布 AI competition paper 与 Gates Foundation 合作；`@frxiaobei` direct-x 讨论 OpenEvidence 医生自用和医院 shadow AI。它们共同提示行业部署、监管和 shadow adoption 是今天 enterprise AI 的辅助线索，但需要官方全文或行业材料验证。【有明确证据支撑 / direct-x】

## 按主题分组摘要

### LLM / Frontier Models

- OpenAI RSS 今天新增 personal finance、Databricks/GPT-5.5、Sea/Codex、Codex mobile 和 sensitive conversation context 等条目。最值得提升的是 personal finance 和 Databricks，但本轮 OpenAI HTML 归档只拿到 challenge 页面，所以正文层面的权限、评测和部署细节仍不能断言。
- Anthropic official page 成功返回 Claude Blog 列表，新增 legal industry、AI-native startup、Claude Code large codebases、computer/browser use best practices 等近期条目。`claude-docs-release-notes` 仍 limited，原因是跳转到 `platform.claude.com` 后返回 region-unavailable HTML。
- Hugging Face、DeepMind 等源今天没有比 OpenAI/Anthropic/GitHub Trending 更强的新高信号；保留为背景，不强行扩写。

### AI Agent / Agentic Workflow

- `anthropics/skills` 是今天 Memory & Dream 主线：它把 skill 做成 folder-level instruction/script/resource 包，并说明可通过 Claude Code plugin marketplace、Claude.ai 和 Claude API 使用。它的意义不是又一个 README，而是官方把 repeatable task knowledge 做成可安装 surface。
- `OpenHuman`、`Superpowers`、`Scientific Agent Skills` 连续多日上榜，今天和 `anthropics/skills` 同时出现，说明 skills/memory/workflow methodology 仍是 GitHub discovery surface 的热点。日报不重复昨日全部结论，只记录持续热度与官方 skills repo 的新增权重。
- `n8n-mcp` 把 workflow automation 平台的节点、参数、操作、模板和 validation knowledge 通过 MCP 暴露给 AI assistants；重要边界是 README 自己提醒不能直接修改生产 workflows，必须先复制、开发环境测试和备份。

### AI Coding / Developer Tools

- OpenAI Codex release Atom feed 今天可见 `0.131.0-alpha.22`、`.21`、`rust-v0.131.0-alpha.20`、`.19`、`.18`；Atom 摘要不足以判断用户可见变化，需后续打开 release body 或 diff。
- LangChain releases 可见 `langchain==1.3.1`，LlamaIndex 到 `v0.14.22`，vLLM 到 `v0.21.1rc0`，vLLM Ascend 到 `v0.19.1rc1`。日报只记录 release surface，不从 Atom 摘要推断 breaking change。
- direct-x 中 `@simonw` 提到 coding agents 降低 native mobile app porting 成本，`@levelsio` 抱怨 Claude Code 速度并提到可能转向 Codex；这些是用户体验和竞争线索，不是正式规格。

### Forward Deployed Engineering / Enterprise AI

- OpenAI Databricks/GPT-5.5、Claude legal industry、NVIDIA VSS blueprint、n8n-MCP 都指向 enterprise deployment substrate：模型能力要落到行业 workflow、自动化平台、vision analytics、MCP 工具接口和生产安全边界。
- `NVIDIA-AI-Blueprints/video-search-and-summarization` 的 README 不是泛 AI demo，而是 reference architecture：real-time video intelligence、downstream analytics、agentic/offline processing、NIM microservices、MCP tool interface 和部署硬件要求都在同一个 repo 里。它值得作为 FDE/enterprise AI 的 visual operations 线索。
- `n8n-mcp` 的 production workflow 警告非常关键：企业 agent 能否可靠落地，取决于是否有 dev/prod 分离、backup、validation 和 human review，而不是只看能不能生成 workflow。

### Financial Agents

- OpenAI personal finance experience 是今天 financial-agents 的官方强线索，但全文未读，只能按 RSS 摘要和 direct-x 处理：它涉及金融账户连接、AI-powered insights 和 grounded guidance。不能写成投资建议能力、交易能力或完整金融 advisor。
- `@frxiaobei` direct-x 提到 OpenEvidence 覆盖美国医生和 shadow AI，这更接近 healthcare/regulated vertical adoption；它不是 financial-agents 主线，但对 regulated enterprise deployment 的权限与合规边界有参考价值。
- 今天没有新的 trading/copy-trading 类 repo 进入高信号；Financial Agents trend 更新重点是把 personal finance 放到 `advice/guidance with connected data` 的高风险边界，而不是交易执行。

### Product / Growth / Indie Founder

- `@gregisenberg` 的 agent observations 把 founders 可用的 agent moat 解释为 memory、knowledge base、local models、skills files、agent latency 和 human approval。它对产品判断有价值，但属于 direct-x 观点，不是行业事实。
- `@EXM7777`、`@kloss_xyz`、`@marclou` 继续提供 AI content operations、skills versioning、docs-as-markdown-for-agents、micro-acquisition 等 product/growth 线索。它们适合保留为方向感，不进入技术强结论。

## GitHub Trending / Daily Repos

本轮 GitHub Trending Daily 成功解析 10 个 repo，10/10 README 文件已写入目录。索引见 [`../raw/2026-05-16/github-trending.json`](../raw/2026-05-16/github-trending.json)，README 原文见 [`../raw/2026-05-16/github-trending-readmes/`](../raw/2026-05-16/github-trending-readmes/)。证据等级统一按 `secondary-source` 处理：它只能说明项目当天在 GitHub Trending 页面可见，不代表官方发布、质量背书或长期趋势。

- [`tinyhumansai/openhuman`](https://github.com/tinyhumansai/openhuman)：personal AI assistant / desktop agent，README 继续强调 118+ integrations、auto-fetch、Memory Tree、Obsidian wiki、TokenJuice compression 和本地/加密工作流。它解决的是个人 agent 如何持续获得 inbox、calendar、repo、docs、messages 等上下文；风险仍是 OAuth 权限、后台同步、删除治理和记忆污染。归档：[`../raw/2026-05-16/github-trending-readmes/tinyhumansai__openhuman.md`](../raw/2026-05-16/github-trending-readmes/tinyhumansai__openhuman.md)。
- [`obra/superpowers`](https://github.com/obra/superpowers)：agentic skills framework / software development methodology。README 说明它让 coding agent 先澄清意图、形成 spec、拿 sign-off、生成 implementation plan，再进入 subagent-driven-development，并支持 Claude Code、Codex CLI、Codex App、Gemini CLI、OpenCode、Cursor 等 harness。归档：[`../raw/2026-05-16/github-trending-readmes/obra__superpowers.md`](../raw/2026-05-16/github-trending-readmes/obra__superpowers.md)。
- [`K-Dense-AI/scientific-agent-skills`](https://github.com/K-Dense-AI/scientific-agent-skills)：scientific/research agent skills 集合，README 写到 135 skills、100+ scientific/financial databases、70+ optimized Python package skills、Cursor/Claude Code/Codex support，以及本地 BYOK research workspace。它是 domain skills productization 的延续信号；专业输出仍需 provenance、license 和人工 review。归档：[`../raw/2026-05-16/github-trending-readmes/K-Dense-AI__scientific-agent-skills.md`](../raw/2026-05-16/github-trending-readmes/K-Dense-AI__scientific-agent-skills.md)。
- [`supertone-inc/supertonic`](https://github.com/supertone-inc/supertonic)：on-device multilingual TTS，README 记录 ONNX Runtime、本地推理和多语言语音能力。它和 agent 主线的交集在端侧 voice interface，不是今天强 agent workflow 信号。归档：[`../raw/2026-05-16/github-trending-readmes/supertone-inc__supertonic.md`](../raw/2026-05-16/github-trending-readmes/supertone-inc__supertonic.md)。
- [`ruvnet/RuView`](https://github.com/ruvnet/RuView)：把 commodity WiFi/ESP32 CSI 信号用于空间感知、presence detection 和 vital sign monitoring。它属于 camera-free sensing / edge intelligence discovery signal；不能把 README claim 当作医疗、安防或可部署能力。归档：[`../raw/2026-05-16/github-trending-readmes/ruvnet__RuView.md`](../raw/2026-05-16/github-trending-readmes/ruvnet__RuView.md)。
- [`influxdata/telegraf`](https://github.com/influxdata/telegraf)：metrics/logs/arbitrary data collection agent，README 记录 300+ plugins、TOML config、standalone static binary 和 monitoring/messaging integrations。它与 AI 主线弱相关，但对 observability/agent telemetry 有类比价值。归档：[`../raw/2026-05-16/github-trending-readmes/influxdata__telegraf.md`](../raw/2026-05-16/github-trending-readmes/influxdata__telegraf.md)。
- [`anthropics/skills`](https://github.com/anthropics/skills)：Anthropic Agent Skills official repo，README 把 skills 定义为 Claude 动态加载的 instructions、scripts 和 resources，并说明 repo 包含 creative、technical、enterprise 和 document skills，以及 Claude Code、Claude.ai、Claude API 三条使用路径。它值得记录是因为 skills 从社区模式变成官方 marketplace/API surface；边界是 README 明确说示例实现和 Claude 实际行为可能不同。归档：[`../raw/2026-05-16/github-trending-readmes/anthropics__skills.md`](../raw/2026-05-16/github-trending-readmes/anthropics__skills.md)。
- [`czlonkowski/n8n-mcp`](https://github.com/czlonkowski/n8n-mcp)：n8n workflow automation 的 MCP server，README 写到 1,650 个 n8n nodes、schema、operation、docs、AI tools、workflow templates 和多 IDE/agent 集成。它解决的是让 AI assistant 理解和构建 n8n workflow；风险是生产 workflow 修改必须备份、复制、dev 环境测试和 validation。归档：[`../raw/2026-05-16/github-trending-readmes/czlonkowski__n8n-mcp.md`](../raw/2026-05-16/github-trending-readmes/czlonkowski__n8n-mcp.md)。
- [`NVIDIA-AI-Blueprints/video-search-and-summarization`](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization)：NVIDIA VSS reference architecture，README 描述 GPU-accelerated vision agents、video analytics、real-time video intelligence、downstream analytics、agentic/offline processing、NIM microservices 和 MCP tool interface。它是 enterprise visual operations / vision-agent deployment 的强 discovery signal；风险在硬件、数据隐私、视频监控场景和误报验证。归档：[`../raw/2026-05-16/github-trending-readmes/NVIDIA-AI-Blueprints__video-search-and-summarization.md`](../raw/2026-05-16/github-trending-readmes/NVIDIA-AI-Blueprints__video-search-and-summarization.md)。
- [`oven-sh/bun`](https://github.com/oven-sh/bun)：JavaScript runtime/bundler/test runner/package manager。它是基础开发工具热度，不是 AI/agent 主线；本轮仅作 infra 背景。归档：[`../raw/2026-05-16/github-trending-readmes/oven-sh__bun.md`](../raw/2026-05-16/github-trending-readmes/oven-sh__bun.md)。

## 来源证据表

| 信号 | 证据等级 | 来源 | URL | 本地归档 |
| --- | --- | --- | --- | --- |
| ChatGPT personal finance preview | official-source RSS / direct-x / limited-fulltext | OpenAI RSS + `@sama` | https://openai.com/index/personal-finance-chatgpt | [`../raw/2026-05-16/rss-items.json`](../raw/2026-05-16/rss-items.json), [`../raw/2026-05-16/twitterapi-io-results.json`](../raw/2026-05-16/twitterapi-io-results.json), [`../trend/raw/2026-05-16/financial-agents/fulltext/openai-personal-finance.html`](../trend/raw/2026-05-16/financial-agents/fulltext/openai-personal-finance.html) |
| Databricks GPT-5.5 enterprise agent workflows | official-source RSS / limited-fulltext | OpenAI RSS | https://openai.com/index/databricks | [`../raw/2026-05-16/rss-items.json`](../raw/2026-05-16/rss-items.json), [`../trend/raw/2026-05-16/forward-deployed-engineering/fulltext/openai-databricks.html`](../trend/raw/2026-05-16/forward-deployed-engineering/fulltext/openai-databricks.html) |
| Claude legal industry deployment | official-page metadata / limited | Claude Blog official page | https://claude.com/blog/deploying-claude-across-the-legal-industry | [`../raw/2026-05-16/official-pages.json`](../raw/2026-05-16/official-pages.json), [`../trend/raw/2026-05-16/forward-deployed-engineering/fulltext/claude-legal-industry.html`](../trend/raw/2026-05-16/forward-deployed-engineering/fulltext/claude-legal-industry.html) |
| Anthropic Agent Skills official repo | secondary-source | GitHub Trending / repo README | https://github.com/anthropics/skills | [`../raw/2026-05-16/github-trending-readmes/anthropics__skills.md`](../raw/2026-05-16/github-trending-readmes/anthropics__skills.md) |
| n8n-MCP | secondary-source | GitHub Trending / repo README | https://github.com/czlonkowski/n8n-mcp | [`../raw/2026-05-16/github-trending-readmes/czlonkowski__n8n-mcp.md`](../raw/2026-05-16/github-trending-readmes/czlonkowski__n8n-mcp.md) |
| NVIDIA VSS Blueprint | secondary-source | GitHub Trending / repo README | https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization | [`../raw/2026-05-16/github-trending-readmes/NVIDIA-AI-Blueprints__video-search-and-summarization.md`](../raw/2026-05-16/github-trending-readmes/NVIDIA-AI-Blueprints__video-search-and-summarization.md) |
| Agent memory / skills / local models product observations | direct-x | `@gregisenberg` | https://x.com/gregisenberg/status/2055354334737543217 | [`../raw/2026-05-16/twitterapi-io-results.json`](../raw/2026-05-16/twitterapi-io-results.json) |
| Anthropic AI competition / Gates Foundation | direct-x | `@AnthropicAI` | https://x.com/AnthropicAI/status/2054987444664377374, https://x.com/AnthropicAI/status/2054941901900611787 | [`../raw/2026-05-16/twitterapi-io-results.json`](../raw/2026-05-16/twitterapi-io-results.json) |

## X/Twitter 覆盖说明

- 本次 X/Twitter 只使用 `twitterapi.io` 的 `GET https://api.twitterapi.io/twitter/user/last_tweets` read endpoint，`includeReplies=false`。
- `twitterapi.io` 顶层状态为 `ok`，26 个账号均返回 `status=ok`；没有把任何 credential/API 异常当作“无推文”。
- 本轮共保留 131 条 direct-x 原始条目。保留数较高的账号包括 `steipete` 20 条、`corbin_braun` 20 条、`Hesamation` 14 条、`cellinlab` 13 条、`rileybrown` 12 条、`kloss_xyz` 9 条。
- `karpathy`、`rryssf_`、`Yangyixxxx`、`zhaogua61654931`、`lidang`、`cnyzgkc`、`_LuoFuli` 请求成功但 kept_count 为 0；这表示 36 小时窗口和脚本过滤下没有保留条目，不等于账号没有更新。
- direct-x 内容包含个人观点、短评论、转发、产品线索和活动宣传；日报只把它们作为直接来源线索，不把个人观点写成官方事实。

## 运行结果与失败源

- RSS：31/31 成功；本轮没有 RSS failed source。
- GitHub releases：6/6 release Atom feed 成功；GitHub REST API 状态为 `skipped`，脚本按设计使用 Atom feed。
- GitHub Trending：1/1 成功，解析 10 个每日热门 repo，10 个 README 文件已归档。
- 官方页面：`anthropic-news-page`、`claude-blog` 成功；`openai-news` limited，原因是 HTML 页面未返回可用 title/content snapshot，但 OpenAI RSS 成功；`claude-docs-release-notes` limited，原因是跳转到 `platform.claude.com` 后返回 region-unavailable HTML。
- X/Twitter：`twitterapi.io` 顶层 `ok`，26 个账号请求成功；没有 failed accounts，没有 Exa fallback。

## 不确定性与待验证项

- 已确认边界：本日报覆盖 2026-05-16 raw 输出、[`../raw/2026-05-16/manifest.json`](../raw/2026-05-16/manifest.json)、[`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)；GitHub Trending 只覆盖 `https://github.com/trending?since=daily` 当前 HTML 中解析到的前 10 个 repo，以及脚本归档的 README；X/Twitter 只覆盖 `twitterapi.io` 返回并被 36 小时窗口保留的 direct-x 条目。
- 未覆盖范围：没有抓取登录态网页、没有补采 X thread/context、没有打开每个 GitHub release 的完整正文、没有浏览器渲染 OpenAI/Anthropic official pages、没有验证 Trending repo 的源码质量或运行效果。
- 推断项：【推断得出】本日报把“official skills surface + enterprise agent workflow + regulated/personal finance + workflow automation safety”作为今天主线。依据是 OpenAI RSS、Claude official page metadata、GitHub Trending README 和 direct-x 同日出现；失效条件是后续全文、产品文档或源码显示这些只是 marketing framing、demo 项目或不可复现实现。
- 待验证项：读取 OpenAI personal finance 全文确认 account linking、data sharing、advice/regulated boundary 和 human review；读取 Databricks/GPT-5.5 全文确认 benchmark、deployment pattern 和 enterprise agent workflow；抽取 Claude legal industry 正文；审计 `anthropics/skills` spec 与 Claude runtime 强制边界；审计 `n8n-mcp` validation、credential、production workflow safety；细读 NVIDIA VSS docs 的 hardware、privacy 和 false-positive verification。

## 运行统计

- 新增条目：`seen_added=44`。
- 高信号条目：8 条。
- 失败来源：official page failed 0 个；twitterapi.io failed accounts 0 个。
- limited 来源：official page limited 2 个：`openai-news`、`claude-docs-release-notes`；trend fulltext limited 2 个：OpenAI personal finance、OpenAI Databricks 页面只归档到 Cloudflare challenge HTML。

## 完成审计

- 用户目标拆解：稳定来源采集、twitterapi.io direct-x 采集、状态更新、日报生成、trend report 生成、enabled trends 检查、失败/limited 来源说明、输出路径汇总。
- 证据对应：raw JSON 写入 [`../raw/2026-05-16/`](../raw/2026-05-16/)，状态文件写入 [`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)，日报为当前文件。
- 状态同步：`update-state.py` 已生成 [`../raw/2026-05-16/manifest.json`](../raw/2026-05-16/manifest.json)，并更新 source health 与 seen。
- 来源边界：所有 X/Twitter 内容标为 `direct-x`，GitHub Trending 标为 `secondary-source`，官方 RSS/GitHub release/official pages 标为 `official-source`、official metadata 或 limited；未用 Exa fallback。
- Trend 检查：`memory-dream`、`financial-agents`、`forward-deployed-engineering` 均有新增趋势信号并已更新专题；OpenAI 全文受 Cloudflare challenge 限制，相关趋势只作为 limited official RSS signal。
