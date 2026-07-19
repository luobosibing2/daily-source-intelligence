# 2026-07-20 Daily Source Intelligence

## 0. 采集范围

- 本次运行日期：`2026-07-20`，时区 `Asia/Shanghai`。关注方向依据 [`watch.md`](../config/watch.md#L1)、[`topics.yaml`](../config/topics.yaml#L1)、[`sources.yaml`](../config/sources.yaml#L1) 和 [`trends.yaml`](../config/trends.yaml#L1)。原始归档在 [`raw/2026-07-20/`](../raw/2026-07-20/)，摘要与失败边界见 [`manifest.json`](../raw/2026-07-20/manifest.json#L1)。
- RSS/Atom：32 个源中 31 个成功；49 条命中关注方向或一手重点源的条目均完成正文尝试且 `fulltext_status=ok`。`nabeel-qureshi` 因 XML 在第 1 行第 54 列 malformed 失败，不解释为“没有更新”。
- GitHub release：7/7 个仓库源通过 Atom 成功。10 条一手 release 正文尝试中 5 条可读、5 条 `limited`；OpenAI Codex 的 `0.145.0-alpha.21`–`.24` 及 Claude Code `v2.1.215` 的短 Atom 内容不能支持功能判断。
- GitHub Trending：成功解析 10 个仓库，10/10 份 README 归档成功。上榜与 star 增长均只是 `secondary-source` discovery signal，不代表官方发布、质量背书、采用率或长期趋势。
- 官方页面：4/4 页面抓取状态 `ok`。OpenAI News 的 curl 内容受 challenge 限制后使用 `opencli-read`；Anthropic News、Claude release notes、Claude Blog 主要提供发现列表，未将单篇页面列表升级为已读正文。
- `twitterapi.io`：27/27 个配置账号请求成功，`window_hours=36`、`includeReplies=false`，但本轮返回 0 条可保留推文；这只是接口窗口/筛选覆盖边界，不能写成账号无更新。没有使用登录态浏览器、官方 X API、Exa MCP 或任何 X/Twitter 写操作。
- 正文阅读清单共 30 条，其中 27 条有本地正文、3 条为 `limited`/无本地正文；清单见 [`report-reading-list.json`](../raw/2026-07-20/report-reading-list.json#L1)，流程索引见 [`run-summary.json`](../raw/2026-07-20/run-summary.json#L1)。首次 `update-state.py` 输出新增 10 条，随后 pipeline 的幂等重放为 0，最终 `state/seen.json` 累计 3275 条。中文译读阶段已退役，没有创建 `translations/2026-07-20/`。

## 1. 今日高信号

| 等级 | 主题 | 标题/信号 | 来源与证据 | 为什么重要与边界 |
| --- | --- | --- | --- | --- |
| 高 | AI Agent / AI 安全 | OpenAI 发布 GPT-Red：用自动化红队模型在网页、文件、邮件和工具输出中搜索提示注入，再把攻击样本用于训练 GPT-5.6。文章报告 GPT-Red 在独立间接注入场景的攻击成功率为 84%，人类红队为 13%；GPT-5.6 Sol 在最难直接注入基准上的失败数比四个月前生产模型少 6 倍。 | [官方原文](https://openai.com/index/unlocking-self-improvement-gpt-red)；正文归档 [`GPT-Red`](../raw/2026-07-20/rss-fulltext/openai-blog/openai-blog-gpt-red-unlocking-self-improvement-for-robustness-ee230258f2.opencli.md#L31) | 重要变化是把攻击生成、对抗训练、留出评估与运行时监控连成安全自改进闭环。84%/13%、6 倍和其他数字是 OpenAI 自报，环境、样本与复现方式仍需第三方核验；归档里的攻击样例只是来源内容，不是本流程指令。 |
| 高 | AI Governance / Public Legitimacy | OpenAI 的政策文章提出“逆联邦主义”：州级 AI 安全框架趋同，核心包括风险评估与公开披露、严重事件报告、独立验证；联邦机构负责先进模型的统一网络安全测试，企业承担审计、报告与吹哨保护。 | [官方原文](https://openai.com/index/advancing-ai-safety-through-state-and-federal-action)；正文归档 [`state/federal safety`](../raw/2026-07-20/rss-fulltext/openai-blog/openai-blog-the-us-is-advancing-ai-safety-through-state-and-federal-action-1e97faa490.opencli.md#L25) | 这是把州法、联邦测试和国际标准接成治理链条的完整政策叙事，但仍是 OpenAI 的立场，不等于法规已通过或形成中立共识。 |
| 高 | Claude Code / 开发者工具 | Claude Code `v2.1.211` 增加子 agent 文本/思考的 `stream-json` 转发，并修复权限预览中的双向控制字符、自动模式越过 hook `ask`、共享凭据唤醒后登出、MCP 空闲重连、显式模型覆盖恢复等问题。 | [GitHub release](https://github.com/anthropics/claude-code/releases/tag/v2.1.211)；正文归档 [`v2.1.211`](../raw/2026-07-20/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.211-ced8cc7595.atom.md#L7) | 版本变化集中在权限、恢复、字符安全与子 agent 状态，而非表面 UI，说明 coding agent 的可靠性瓶颈正在转向运行时控制面。`v2.1.215` 仅有“默认不再自行运行 `/verify`/`/code-review`”的短说明，不能从中推导更多功能。 |
| 高 | Codex / 模型运行时 | OpenAI Codex `0.144.6` 刷新 GPT-5.6 Sol、Terra、Luna 的 bundled instructions，并把上下文窗口更正为 272,000 tokens。 | [GitHub release](https://github.com/openai/codex/releases/tag/rust-v0.144.6)；正文归档 [`0.144.6`](../raw/2026-07-20/github-release-fulltext/openai-codex/openai-codex-0.144.6-7abc1a3960.atom.md#L7) | 这是当前 Codex release 中可读的明确 feature delta；其他 alpha 条目只证明版本存在，正文过短，不能假装读到功能变化。 |
| 高 | AI Coding / 运行时 | Simon Willison 通过本地二进制 `strings` 检查，记录 Claude Code v2.1.181 之后使用 Rust 重写的 Bun；他观察到内嵌 Bun 版本为 1.4.0，并以 563 个 Rust 源文件路径作交叉证据。 | [原文](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/)；正文归档 [`Claude Code uses Bun`](../raw/2026-07-20/rss-fulltext/simonwillison/simonwillison-claude-code-uses-bun-written-in-rust-now-165d33e669.extracted.md#L1) | 这是独立工程观察，提示 CLI 启动性能和运行时替换正在变成产品稳定性工作；不是 Anthropic 官方公告，需按对应版本与平台复测。 |
| 中高 | Agent 对齐 / 组织协作 | `Forward Deployed` 第 5 集讨论 agent 对齐：对话把公司、Toyota 生产系统和“模式语言”作为协调机制类比，指出 agent 让个人更快改代码，却可能让共享架构理解、规格边界和跨团队沟通成为新瓶颈。 | [节目原文](https://www.forwarddeployed.com/p/forward-deployed-episode-5-aligning)；正文归档 [`Aligning Agents`](../raw/2026-07-20/rss-fulltext/forward-deployed/forward-deployed-forward-deployed-episode-5-aligning-agents-e3c7f6c544.opencli.md#L1) | 该材料适合做 FDE/企业交付的机制线索：瓶颈可能从写代码上游移动到澄清、规格、共同语言和反馈回流。它是访谈观点，不是组织效率实证。 |
| 中高 | Product / AI 采用 | SVPG 的“Build to Learn vs Build to Earn”认为生成式 AI 大幅降低交付成本后，真正瓶颈转为发现值得构建的方案；原型用于验证价值、可用性、可行性和商业可行性，产品化则必须满足可靠性、规模、隐私、安全和运维。 | [原文](https://www.svpg.com/build-to-learn-vs-build-to-earn/)；正文归档 [`Build to Learn`](../raw/2026-07-20/rss-fulltext/svpg/svpg-build-to-learn-vs-build-to-earn-b8c1e5da1a.extracted.md#L1) | 这为企业评估“AI 加速”提供了可操作的 discovery/delivery 分界，但文章为产品方法论，不能替代具体团队的上线数据。 |
| 中高 | Product / Growth / Agent 可见性 | Ramp 在约 50 个营销页面上测试面向 AI bot 的激励内容：作者自报 Markdown 比 schema/HTML 更容易被模型引用，Claude、Perplexity、ChatGPT 的转发行为差异很大，ChatGPT 在其测试窗口内一直没有展示该优惠。 | [实验原文](https://builders.ramp.com/post/marketing-to-ai-agents)；正文归档 [`marketing to agents`](../raw/2026-07-20/rss-fulltext/ramp-builders/ramp-builders-we-tested-marketing-incentives-to-ai-agents.-here-s-what-happened-6c77d49472.opencli.md#L33) | 它把“agent 可读内容”从 SEO 讨论推进到可测的 bot 日志、引用和归因问题；样本、模型版本、抓取缓存和公司自选指标都限制了外推。 |
| 中高 | AI Coding / 工程方法 | antirez 主张 AI 时代工程师应更多控制设计意图、测试、质量和 `DESIGN.md`，少把时间花在逐行检查机器生成代码；他以本地 LLM 推理实现中的细微错误说明“代码能跑”不等于设计和性能正确。 | [原文](http://antirez.com/news/169)；正文归档 [`Control the ideas`](../raw/2026-07-20/rss-fulltext/antirez/antirez-control-the-ideas-not-the-code-b872d6d479.opencli.md#L1) | 这是经验性判断，不是普遍规范；它与 Claude Code release 的控制面修复共同指向“设计、测试和可追溯证据”而非纯生成吞吐。 |

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- OpenAI 的 GPT-Red 和美国 AI 安全文章均有 `fulltext_status=ok`，前者是自动攻击—防御训练闭环，后者是州—联邦—国际治理主张。OpenAI News 页面还发现《A scorecard for the AI age》、GPT-5.6 Microsoft 365 Copilot、GPT-5.5 生物安全漏洞赏金计划和 GPT-5.6 System Card 等标题；页面正文通过 `opencli-read` 归档，但单篇页面没有全部补抓，因此只作为官方页面 discovery signal，见 [`official-pages.json`](../raw/2026-07-20/official-pages.json#L1)。
- Codex `0.144.6` 的可读正文只说明模型提示与上下文窗口修正；`0.145.0-alpha.21`–`.24` 是 `limited`。Claude Code `v2.1.211` 可读，重点在权限预览字符安全、hook 决策、MCP 重连和子 agent 模型恢复；`v2.1.215` 只读到 `/verify`/`/code-review` 默认行为变化。所有版本说明都应在目标 CLI、SDK/headless 和隔离 worktree 中回归。

### LLM / Frontier Models

- GPT-Red 还展示了从模拟场景转移到真实 agent 的风险：文章称其能在 Vendy 风格自动售货 agent 中改变昂贵商品价格、取消订单，并在 10 个 Codex 数据外泄场景上做留出测试。实验由 OpenAI 设计并自报，不能替代独立红队。
- Simon Willison 的“AI Mania Is Eviscerating Global Decision-Making”收集企业把 AI 目标夸大为生产力承诺的匿名轶事；它适合作为叙事反证，正文没有可审计的样本，不作定量结论。Lilian Weng 的《Extrinsic Hallucinations in LLMs》是历史正文，提供幻觉机制背景，不是本日新发布。

### AI Agent / Agentic Workflow

- `Forward Deployed` 访谈把 agent 看作组织协调问题：当多个 agent 并行修改系统时，规格、共享词汇、所有权和“遇到不确定就停下询问”的机制变得更重要。它与 GPT-Red 的攻击—防御闭环共同支持先设计边界、回放和评估，再扩大工具权限。
- Ramp 的实验显示 agent 可能成为 B2B 购买入口；Markdown、bot 识别、缓存和按模型测试会影响是否被引用。当前只证明一家公司在一段窗口中的观察，不证明通用的“agent SEO”规则。

### AI Coding / Developer Tools

- Claude Code 连续 release 修复权限检查、hook ask、worktree 隔离、MCP 重连、后台任务恢复、终止进程树和字符混淆等控制面问题；这是比“生成更多代码”更直接的可靠性信号。
- Claude Code 使用 Rust 版 Bun 的本地二进制证据和 antirez 关于 `DESIGN.md`/QA 的主张都指向同一边界：开发者需要理解架构和测试证据，不能只看生成速度。前者是独立复核，后者是个人判断。

### AI Governance / Public Legitimacy

- OpenAI 的“逆联邦主义”文章主张州级披露/审计与联邦统一测试互补，并把高级模型安全、国家安全和民主治理连在一起。下一步应对照真实州法、联邦测试框架、CAISI 角色和其他实验室立场。
- 本轮没有 `direct-x` 政策证据；政策判断均来自可读官方文章或发现列表，不把供应商立场写成法规事实。

### AI Infrastructure / Open Source

- KTransformers README 描述 CPU-GPU 异构推理与微调框架，提供 inference 和 SFT 两条入口，并列出 MiniMax-M3、GLM-5.2 等支持更新；这是 Trending README 自述，硬件兼容、吞吐和模型许可需复现。归档见 [`KTransformers`](../raw/2026-07-20/github-trending-readmes/kvcache-ai__ktransformers.md#L1)。
- GitHub Trending 还出现 GitHub Copilot SDK、Voicebox 等本地/嵌入式 agent 与语音工具；均为发现线索，不表示官方质量或采用率。

### Forward Deployed Engineering / Enterprise AI Deployment

- `Forward Deployed` 第 5 集强调 FDE/企业部署的核心不只是把 agent 接入工具，而是重构协作、规格和反馈机制。SVPG 的 build-to-learn 文章进一步把“先发现方案、再交付产品”分开，适合用作企业交付阶段门的背景。
- 本轮没有新的客户侧 FDE 交付指标；不能用访谈、SVPG 方法论或供应商文章推导市场规模、交付成本或成功率。

### Product / Growth / GTM

- Ramp 的 agent-facing 内容实验把营销问题转成可观测性问题：哪些 bot 访问了页面、模型是否引用、是否把优惠传给用户、是否发生可追踪行动。作者自报的 Claude/ChatGPT 差异需要跨模型、跨缓存窗口复测。
- SVPG 的“build to learn”框架说明 AI 交付加速后，产品发现和结果验证更可能成为瓶颈；它与 OpenAI scorecard 的“每个成功任务的全成本”方向一致，但两者都不是独立采购评估。

### AI Systems / Automation

- 本轮稳定来源没有新的可读自动化系统 release；`Forward Deployed` 访谈和 Trending 的本地 Web/语音工具显示“本地能力 + agent 编排”仍在扩展，但安装、权限、网络和隐私边界都未在本仓 live-verified。

### X/Twitter 推主主题摘要

本轮 [`twitter-topic-brief.json`](../raw/2026-07-20/twitter-topic-brief.json#L1) 状态为 `ok`，27/27 个账号请求成功，但 `tweet_count=0`、没有主题条目。因此本节不补造推文链接，也不把空结果解释成账号没有更新；下次采集仍需按相同的结构化只读接口复核。

### GitHub Trending 每日发现

本次 Trending 页面成功解析 10 个仓库，10/10 份 README 通过 `curl` 归档；以下项目介绍把 Trending description 与 README 合并，证据等级统一为 `secondary-source`。上榜不代表质量、采用或安全性。

- [`bojieli/ai-agent-book`](https://github.com/bojieli/ai-agent-book)：开源中英双语 AI Agent 教材和配套代码，围绕“LLM + 上下文 + 工具”讲上下文工程、记忆、MCP、coding agent、评估和后训练，并提供可编译 PDF；适合学习与复现实验，不等于生产架构标准。README 归档 [`ai-agent-book`](../raw/2026-07-20/github-trending-readmes/bojieli__ai-agent-book.md#L1)。
- [`tirth8205/code-review-graph`](https://github.com/tirth8205/code-review-graph)：用 Tree-sitter 建立增量代码结构图、变更影响范围和测试边，通过 MCP/CLI 让 coding agent 只读取必要上下文；README 自带 token 减少 benchmark，但本仓未复测，安装器对 MCP/hooks 的改动需先检查。归档 [`code-review-graph`](../raw/2026-07-20/github-trending-readmes/tirth8205__code-review-graph.md#L1)。
- [`kvcache-ai/ktransformers`](https://github.com/kvcache-ai/ktransformers)：面向 CPU-GPU 异构计算的 LLM 推理与微调研究项目，README 提供 inference 与 SFT 入口及若干模型支持教程；它解决本地硬件上的显存/吞吐约束，但性能、精度和许可仍需按具体硬件验证。归档 [`KTransformers`](../raw/2026-07-20/github-trending-readmes/kvcache-ai__ktransformers.md#L1)。
- [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch)：以 503 课、20 个阶段覆盖 Python、TypeScript、Rust、Julia，并要求每课留下 prompt、skill、agent 或 MCP artifact；这是教育课程，不能当作生产 agent 平台，课程统计也需核对日期。归档 [`AI engineering from scratch`](../raw/2026-07-20/github-trending-readmes/rohitg00__ai-engineering-from-scratch.md#L1)。
- [`jamiepine/voicebox`](https://github.com/jamiepine/voicebox)：本地运行的开源语音工作室，提供声音克隆、语音生成、跨应用听写与给 agent 配音的 API/桌面流程；涉及声音授权、隐私、模型下载和本地权限，不能只因上榜就视为安全。归档 [`Voicebox`](../raw/2026-07-20/github-trending-readmes/jamiepine__voicebox.md#L1)。
- [`KnockOutEZ/wigolo`](https://github.com/KnockOutEZ/wigolo)：本地优先的 Web 搜索、抓取、抽取、缓存和研究 MCP/REST/SDK，面向 Claude Code、Cursor、Codex 等，README 称无需 API key；`npx wigolo init` 会下载浏览器引擎与本地模型，public beta、AGPL-3.0，需在无生产凭据的隔离环境审查网络和文件变更。归档 [`wigolo`](../raw/2026-07-20/github-trending-readmes/KnockOutEZ__wigolo.md#L1)。
- [`andrewrabert/jellium-desktop`](https://github.com/andrewrabert/jellium-desktop)：基于 CEF 与 mpv 的非官方 Jellyfin 桌面客户端，提供 Linux AppImage/Flatpak、macOS 和 Windows 构建；它是桌面媒体工具，不是 AI 信号，安装时要按 README 处理 macOS quarantine。归档 [`Jellium Desktop`](../raw/2026-07-20/github-trending-readmes/andrewrabert__jellium-desktop.md#L1)。
- [`github/copilot-sdk`](https://github.com/github/copilot-sdk)：把 GitHub Copilot CLI 背后的 agent 引擎嵌入 Python、TypeScript、Go、.NET、Java 和 Rust 应用，面向把 agent 工作流集成到产品/服务的开发者；README 的生产化描述仍需检查认证、计费、权限和运行隔离。归档 [`Copilot SDK`](../raw/2026-07-20/github-trending-readmes/github__copilot-sdk.md#L1)。
- [`PostHog/posthog`](https://github.com/PostHog/posthog)：把分析、会话回放、feature flags、实验、错误、日志和 AI observability 汇成“自驱动产品”平台，面向观测—诊断—修复闭环；自动读取业务数据或生成修改建议时必须审查隐私、权限与发布门禁。归档 [`PostHog`](../raw/2026-07-20/github-trending-readmes/PostHog__posthog.md#L1)。
- [`microsoft/terminal`](https://github.com/microsoft/terminal)：Windows Terminal、Console Host 和命令行组件的官方开源仓库，README 给出 Microsoft Store、GitHub、winget 等安装/构建路径；它是通用开发基础设施发现信号，不应被写成 AI 发布。归档 [`Windows Terminal`](../raw/2026-07-20/github-trending-readmes/microsoft__terminal.md#L1)。

## 3. 来源证据表

| 来源 | 当日覆盖 | 证据归档 | 说明 |
| --- | --- | --- | --- |
| RSS/Atom | 32 源，31 成功；49 条命中/一手条目正文 49/49 `ok` | [`rss-items.json`](../raw/2026-07-20/rss-items.json#L1)、[`rss-fulltext/`](../raw/2026-07-20/rss-fulltext/) | `nabeel-qureshi` malformed XML；其他命中正文按 curl 或失败后的 `opencli-read` 归档。 |
| GitHub release | 7 源通过 Atom 成功；一手正文 5/10 `ok`、5/10 `limited` | [`github-items.json`](../raw/2026-07-20/github-items.json#L1)、[`github-release-fulltext/`](../raw/2026-07-20/github-release-fulltext/) | limited release 只保留版本/短摘要边界，不推导功能。 |
| GitHub Trending | 10 个仓库，README 10/10 成功 | [`github-trending.json`](../raw/2026-07-20/github-trending.json#L1)、[`github-trending-readmes/`](../raw/2026-07-20/github-trending-readmes/) | 全部标记为 `secondary-source` discovery signal。 |
| 官方页面 | 4/4 页面抓取状态 `ok` | [`official-pages.json`](../raw/2026-07-20/official-pages.json#L1)、[`official-page-text/`](../raw/2026-07-20/official-page-text/) | OpenAI News 使用 `opencli-read`；Claude 页面主要提供发现列表。 |
| X/Twitter | 27/27 账号请求 `ok`，0 条保留 | [`twitterapi-io-results.json`](../raw/2026-07-20/twitterapi-io-results.json#L1)、[`twitter-topic-brief.json`](../raw/2026-07-20/twitter-topic-brief.json#L1) | 仅使用 `GET /twitter/user/last_tweets`，`includeReplies=false`；空结果是覆盖边界，不是无更新结论。 |
| 官方链接候选 | 0 条 | [`official-link-candidates.json`](../raw/2026-07-20/official-link-candidates.json#L1) | 本轮没有可升级的 priority X 官方链接候选。 |

## 4. X/Twitter 覆盖说明

- 本次使用 `twitterapi.io` 结构化只读接口，27 个账号请求均成功；接口返回有限时间窗列表，本轮没有返回可保留推文，不能证明任何账号完整覆盖过去 24 小时，更不能证明账号没有发文。
- `direct-x` 本轮计数为 0，故没有制造主题摘要、推文链接或“高信号 direct-x”。如果下一轮出现条目，仍需为每条保留 tweet 链接与 `direct-x` 证据等级，并把个人体验、转述、收入主张或 benchmark 评价与官方正文分开。
- official-link candidate 生成成功但候选数为 0；没有使用 Exa 或登录态浏览器补漏。

## 5. 不确定性与待验证项

- **来源窗口**：部分 RSS feed 会返回历史条目；可读不等于当天发布。判断“今天发生了什么”时应优先检查发布时间、去重状态和 [`manifest.json`](../raw/2026-07-20/manifest.json#L1)，不要把旧正文当成当天新增。
- **RSS 失败**：`nabeel-qureshi` 因 malformed XML（第 1 行第 54 列）失败。下一步只需下次重试并检查源站 XML 是否恢复，本次不使用其他 discovery 层替代。
- **GitHub limited**：OpenAI Codex alpha `0.145.0-alpha.21`–`.24` 与 Claude Code `v2.1.215` 的 Atom body 过短；最小复核路径是打开对应 release 页面，或等待下一轮 Atom/REST 正文可读。
- **供应商指标与政策**：GPT-Red 的攻击成功率/鲁棒性、Ramp 的 bot 引用数据、OpenAI 的政策主张和 SVPG 的产品方法论都需要第三方复现、法规原文、跨模型实验或客户侧交付数据，不能直接升级为普遍事实。
- **X 覆盖**：`twitterapi.io` 0 条保留只说明本次接口筛选没有返回可用条目；下次仍需复核时间窗、账号覆盖和 API 响应，不以空结果替代抓取。
- **Trending 项目**：README 可读只证明文档声称了某种机制，不证明安装成功、性能、安全、许可或维护质量。对 `wigolo`、`Voicebox`、`PostHog`、`code-review-graph` 等涉及浏览器、声音、业务数据或安装器的项目，最小验证路径是隔离环境、最小权限、无生产凭据，并记录网络/文件变更。
- **FDE 覆盖**：本轮有 FDE 访谈和产品方法论，但没有新的客户侧交付指标；需要现场数据接入、上线时间、失败项目、维护归属和反馈回流证据，才能升级长期趋势判断。
- **候选审计处置**：初次报告完成后运行 [`candidate-audit.md`](../reviews/2026-07-20-candidate-audit.md)；对 `missed` 的历史背景、弱匹配或无可读正文条目保留边界，不把它们强行升级为今日高信号。
- 本轮 audit 的 12 条 `missed` 已逐项核对：其中包括较早的教育项目、代码代理长文、两篇教学/创业材料、数篇产品方法论文章、FDE 背景文和两篇通用 Rails/Node 分发技术文。它们虽然正文可读，但发布时间、主题强度或与当日新增的关系不足，故保留在审计表而不升级；本轮没有 `official-link-candidate` 或高分 `direct-x` 漏写项。

## 6. 本次流程输出

- 日报：[`docs/2026-07-20-daily-intel.md`](2026-07-20-daily-intel.md)
- 流程摘要：[`raw/2026-07-20/run-summary.json`](../raw/2026-07-20/run-summary.json#L1)
- 正文阅读清单：[`raw/2026-07-20/report-reading-list.json`](../raw/2026-07-20/report-reading-list.json#L1)
- 原始 manifest：[`raw/2026-07-20/manifest.json`](../raw/2026-07-20/manifest.json#L1)
- 候选审计：[`reviews/2026-07-20-candidate-audit.md`](../reviews/2026-07-20-candidate-audit.md)
