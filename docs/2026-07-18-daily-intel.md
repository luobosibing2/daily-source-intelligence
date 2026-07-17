# 2026-07-18 Daily Source Intelligence

## 0. 采集范围

- 本次运行日期：`2026-07-18`，时区 `Asia/Shanghai`。关注范围依据 [`watch.md`](../config/watch.md)、[`topics.yaml`](../config/topics.yaml)、[`sources.yaml`](../config/sources.yaml) 和 [`trends.yaml`](../config/trends.yaml)。RSS 保留各源自己的近期窗口；因此“已读正文”不等于“今天发布”，判断当天新信号时以发布时间和去重状态为准。
- 原始归档：[`raw/2026-07-18/`](../raw/2026-07-18/)；流程摘要：[`run-summary.json`](../raw/2026-07-18/run-summary.json)；正文阅读清单：[`report-reading-list.json`](../raw/2026-07-18/report-reading-list.json)。首次 `update-state.py` 新增 `39` 条去重记录，`state/seen.json` 累计 `3227` 条。
- RSS/Atom：32 个源中 31 个成功；51 条命中关注方向或一手重点源条目均完成全文尝试且 `fulltext_status=ok`。失败源是 `nabeel-qureshi`，原因是 malformed XML（第 1 行第 54 列），不解释为“没有更新”。
- GitHub release：7/7 个源通过 Atom 成功；10 条一手 release 尝试归档正文，4 条可读、6 条 `limited`。OpenAI Codex 的 `0.145.0-alpha.18`–`.22` 不能从短 Atom 内容推导功能；Claude Code 的 `v2.1.212`、`v2.1.211`、`v2.1.210`、`v2.1.208` 正文可读，`v2.1.209` 受限。
- GitHub Trending：成功解析 10 个仓库，10/10 份 README 归档成功；Trending 是 `secondary-source` 发现线索，不代表官方发布、质量背书、采用率或长期趋势。
- `twitterapi.io`：27/27 个配置账号请求成功，窗口 36 小时、`includeReplies=false`，保留 126 条 `direct-x` 证据。部分账号返回 0 条只表示本次接口筛选结果为空，不能写成账号无更新。没有使用登录态浏览器、官方 X API、Exa MCP 或任何 X/Twitter 写操作。
- 阅读清单共 359 条，其中 30 条有本地正文，329 条只有结构化证据或受限边界；报告只把有本地归档的 RSS/release/README 写成“已读原文”。中文译读阶段已退役，没有创建 `translations/2026-07-18/`。

## 1. 今日高信号

| 等级 | 主题 | 标题/信号 | 来源 | 证据等级 | 为什么重要 |
| --- | --- | --- | --- | --- | --- |
| 高 | AI Governance / AI Agent | OpenAI 发布 GPT-Red：用自动化红队模型通过自博弈寻找提示注入，再把攻击样本用于提高 GPT-5.6 的稳健性；文章报告在一个新场景中攻击成功率 84% 对人工 13%，并称 GPT-5.6 Sol 在其最难直接注入基准上失败次数减少 6 倍。 | [GPT-Red 原文](https://openai.com/index/unlocking-self-improvement-gpt-red)；正文归档 [`gpt-red...opencli.md`](../raw/2026-07-18/rss-fulltext/openai-blog/openai-blog-gpt-red-unlocking-self-improvement-for-robustness-ee230258f2.opencli.md) | `official-source`，`fulltext_status=ok`，`opencli-read` | 今天最清晰的变化不是再加一条拒答规则，而是把攻击生成、对抗训练、留出评估和运行时监控连成安全自改进闭环。84%/13%、0.05% 等数字仍是 OpenAI 自报，测试环境和样本定义需要独立复核。 |
| 高 | Product / Enterprise AI | OpenAI 的《A scorecard for the AI age》把企业 AI 价值从席位数转向“每美元完成的有用工作”：成功任务成本、可依赖程度、规模化后的单位价值都要在真实工作系统里测量。 | [官方原文](https://openai.com/index/a-scorecard-for-the-ai-age)；正文归档 [`scorecard...opencli.md`](../raw/2026-07-18/rss-fulltext/openai-blog/openai-blog-a-scorecard-for-the-ai-age-3ebda52fc8.opencli.md) | `official-source`，`fulltext_status=ok`，`opencli-read` | 这是企业采购和 FDE 评估口径的明显转向：不再只比较 token 价格或模型榜单，而要把重试、人工复核、延迟和最终交付结果一起计入。文章同时引用 GPT-5.6 与 Claude Fable 5 的供应商/第三方基准，不能视为独立采购结论。 |
| 高 | Forward Deployed / Enterprise AI | Cars24 把 OpenAI agent 用在买车、卖车、融资、跟进和客服，另把 Codex 接入 Linear、GitHub 及财务、法务、市场等工作流；客户案例自报每月 100 万以上对话分钟、客服解决率增加 50%、周转时间减少 80%、挽回 12% 流失线索。 | [Cars24 客户案例](https://openai.com/index/cars24)；正文归档 [`cars24.opencli.md`](../raw/2026-07-18/rss-fulltext/openai-blog/openai-blog-how-cars24-scales-conversations-and-builds-faster-with-openai-6f16a999c8.opencli.md) | `official-source`，`fulltext_status=ok`，`opencli-read` | 信号在于 agent 已从单点客服扩展到跨部门“操作层”，但所有效果指标均来自供应商客户案例，仍需客户侧上线周期、失败率、维护责任和成本数据。 |
| 高 | AI Coding / Developer Tools | Claude Code `v2.1.211`–`v2.1.212` 连续修复控制面：`/fork`/`/subtask`、后台会话恢复、WebSearch 与子 agent 会话预算、MCP 长调用自动后台化、计划模式写文件确认、worktree 符号链接边界、hook 原因传播和 SIGTERM 进程树清理。 | [v2.1.212](https://github.com/anthropics/claude-code/releases/tag/v2.1.212)、[v2.1.211](https://github.com/anthropics/claude-code/releases/tag/v2.1.211)；本地 release body [`v2.1.212`](../raw/2026-07-18/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.212-daf0d7c636.atom.md)、[`v2.1.211`](../raw/2026-07-18/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.211-ced8cc7595.atom.md) | `official-source`，release body `ok` | 版本变化集中在权限、并发、恢复和资源边界，而不是表面 UI；这说明 coding agent 的可靠性瓶颈正在转向运行时控制面。仍应在实际终端、SDK 和 worktree 环境回归。 |
| 高 | LLM / Frontier Models | Moonshot AI 发布 Kimi K3；Simon Willison 归档了 2.8T 参数、计划 7 月 27 日开放权重、价格、任务成本和“pelican”体验，并明确提醒该小测试已不能代表长程工具调用能力。 | [Simon Willison 原文](https://simonwillison.net/2026/Jul/16/kimi-k3/)、[Kimi K3 直链](https://x.com/simonw/status/2077852005129933247)；正文归档 [`kimi-k3...extracted.md`](../raw/2026-07-18/rss-fulltext/simonwillison/simonwillison-kimi-k3-and-what-we-can-still-learn-from-the-pelican-benchmark-546beebc58.extracted.md) | `secondary-source` + `direct-x` | 开放权重模型继续向更大规模和更高价格带移动；真正可比的不是单次 SVG，而是工具调用、长上下文、成本和本地部署。参数、基准和开放权重日期主要是 Moonshot/作者转述，需等发布与复测。 |
| 中高 | AI Coding / AI Systems | GitHub Trending 的 `github/copilot-sdk` 提供 Python、TypeScript、Go、.NET、Java、Rust SDK，把 Copilot CLI 作为 JSON-RPC agent runtime 嵌入应用，并支持 BYOK、权限处理、自定义 agent/skill/tool。 | [GitHub 仓库](https://github.com/github/copilot-sdk)；README 归档 [`github__copilot-sdk.md`](../raw/2026-07-18/github-trending-readmes/github__copilot-sdk.md) | `secondary-source` | 这是“把 coding agent 变成应用运行时”的具体工程入口，但 README 不能证明生产稳定性、账单边界或默认工具安全；认证、权限回调和 CLI 进程生命周期应先做隔离验证。 |
| 中高 | AI Coding / Context Engineering | Trending 的 `tirth8205/code-review-graph` 用 Tree-sitter 建立代码结构图和增量索引，通过 MCP/CLI 计算变更影响范围，让 AI 只读取相关调用者、依赖和测试；README 自报在大仓库中可显著减少上下文 token。 | [GitHub 仓库](https://github.com/tirth8205/code-review-graph)；README 归档 [`tirth8205__code-review-graph.md`](../raw/2026-07-18/github-trending-readmes/tirth8205__code-review-graph.md) | `secondary-source` | 直接回应 coding agent 的上下文成本和 review 噪声问题；“93 倍减少”等数字来自仓库自带图示，尚未在本仓复测，安装器写入 MCP/skills 前要检查变更范围。 |

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- OpenAI 的五条 `fulltext_policy=always` 博客条目均有正文归档且 `fulltext_status=ok`。GPT-Red 把自动攻击搜索接入模型训练；《A scorecard for the AI age》把真实工作完成量、成功任务成本、可依赖性和规模化回报作为企业衡量框架；Cars24 展示跨客服、销售、融资、财务和研发的 agent/Codex 落地；[青少年安全文章](https://openai.com/index/why-teens-deserve-access-safe-ai)和[美国 AI 安全政策文章](https://openai.com/index/advancing-ai-safety-through-state-and-federal-action)分别提供年龄适配保护与政策立场背景。它们共同把“模型能力”延伸为安全控制、工作结果和组织流程，但指标与政策判断大多是 OpenAI 自述。
- Claude Code `v2.1.212` 的可读 release body 明确加入 `/fork` 生成后台会话、`/subtask`、WebSearch 200 次默认会话上限、子 agent 200 次默认上限、MCP 两分钟自动后台化、计划模式写文件确认、worktree 符号链接边界和 SIGTERM 进程树清理；`v2.1.211` 补上权限预览中的双向控制字符/零宽字符、hook ask 决策、后台 agent 虚构结果、模型覆盖恢复和 worktree 持久权限等问题。`v2.1.209` 的正文 limited，不据此推导更多功能。
- Claude Blog 官方页面发现 7 月 15–17 日的 Fable 5/Cowork、CISO agentic AI、代码迁移等条目，但页面列表没有为这些单篇文章提供本地正文路径；本日报只记录发现，不把其标题升级为已读的机制判断。页面快照见 [`official-pages.json`](../raw/2026-07-18/official-pages.json)。

### LLM / Frontier Models

- Kimi K3 的二手长文给出较具体的可验证线索：2.8T 总参数、计划 7 月 27 日开放权重、输入/输出价格、一次 SVG 任务的 token/成本，以及相对 Kimi K2.6 的 token 使用变化。作者同时强调“pelican”已与真实 agent 工具调用能力脱钩，因此本次把它作为模型发布和测量方法信号，不作为综合能力排名；同日的[简短引用条目](https://simonwillison.net/2026/Jul/17/kimi-k3/#atom-everything)只作为同一文章的重复发现。
- `simonw` 的 `direct-x` 推文链接到同一 Kimi K3 笔记；`levelsio` 则分享用 Kimi K3 通过 OpenCode 编程的个人体验。后者只证明发布者的实际尝试与感受，不能替代官方 API、开放权重包或可重复基准。
- Google DeepMind 的 Nano Banana 2 Lite、Gemini Omni Flash 和 Gemini 3.5 Flash computer use 仍在 feed 中，正文可读但发布时间较早；今天只作背景，不把历史发布当作新增。

### AI Governance / Public Legitimacy

- GPT-Red 把治理讨论落到攻击面、工具调用、浏览器/文件/邮件中的第三方数据、留出场景和实时监控。文章展示了“安全红队也要扩展”的因果链，但所有成功率与防御指标是 OpenAI 内部评估，不是跨实验室审计。
- OpenAI 的“州级对齐—联邦测试—国际标准”文章与青少年安全文章继续提供供应商政策立场：年龄预测、家长控制、学习模式、严重事件报告和独立审计被放在同一套产品/政策叙事中。它们是 `official-source` 正文，但不等于法规已经通过，也不能独立证明年龄判断、隐私或教育效果。
- `direct-x` 中 OpenAI 关于赛车 AI 的帖子和 GPT-5.6 Sol 用户评价只保留为官方账号直接发布的产品/体验线索，不把宣传或转述当作治理事实。

### AI Agent / Agentic Workflow

- GPT-Red 的攻击者—防御者自博弈是今天最完整的 agent 安全闭环：攻击模型控制网页、文件或工具输出中的恶意内容，防御模型必须保持原任务，同时通过训练吸收成功攻击。Vendy 模拟案例显示，提示注入可以把高权限 agent 的业务结果改写；这类结果应推动权限隔离、工具审计和回放测试，而不是只增加系统提示。
- Anthropic `cwc-workshops` 登上 Trending，README 列出模型选择评测、技能与 MCP 的多 agent 分解、managed agent、共享记忆/Dreaming Service、评测驱动 PPTX 和研究桌面等完整练习。仓库明确写着“不维护且不接受贡献”，所以它更像教学样例集合，不能当作当前产品承诺。
- `mattpocockuk` 的 `direct-x` 分享 `/grill-with-docs` 分轮提问、`/wayfinder` 制作问题地图，以及把 13 轮问题压缩到 3 轮的体验；它说明“先澄清依赖再编排技能”是实践方向，但没有独立效率实验。

### AI Coding / Developer Tools

- Claude Code 两个版本的修复集中在真正会造成事故的边界：计划模式未经确认执行写文件命令、worktree 路径逃逸、视觉字符欺骗、MCP/后台任务阻塞、子 agent/搜索无界循环和进程树孤儿。版本说明本身是直接证据，生产环境仍需在隔离 worktree 和 SDK/headless 模式回归。
- `antirez` 的《Control the ideas, not the code》是较强的工程观点：AI 时代应把 review 重心从逐行阅读转到设计模型、测试、质量和 `DESIGN.md`，因为局部代码生成已经不再是稀缺环节。文章同时承认年轻开发者建立心智模型仍是未决问题；这是作者判断，不是普遍工程规范。
- `code-review-graph` 以 AST/调用关系/测试覆盖图压缩 review 上下文；`Nutlope/hallmark` 则把网页结构、主题和 57 个“反模板化”检查做成 Claude Code/Cursor/Codex skill。两者都说明工具层正从“写代码”转向上下文筛选和输出审查，但 README 的 benchmark/质量主张需要实测。
- `rileybrown` 的 `direct-x` 指出 Codex Skills 与 GPT Work 会话之间不迁移；这条反馈可作为跨产品状态/技能边界的回归线索，不足以代表所有账号或版本。

### AI Infrastructure / Open Source

- `PrismML-Eng/Bonsai-demo` README 描述本地 1-bit/ternary Bonsai 模型，27B 版本支持视觉输入、OpenAI 风格工具调用、MCP、可调推理强度和 256k+ 上下文，并覆盖 Mac Metal、CUDA、Vulkan、ROCm 与 CPU。README 还写到 1-bit 版本可在现代 iPhone 上运行；模型许可、硬件吞吐、私有权重访问和真实工具安全仍待验证。
- `antirez` 的 DwarfStar/本地推理文章和 `simonw` 的 Firefox in WebAssembly 记录，分别展示大模型推理的内存/分布式工程与受限运行时中的浏览器组合；它们是已归档工程背景，不是今天的发布。
- `github/copilot-sdk` 与 `PostHog/posthog` 共同体现“可观测性 + agent runtime”方向：前者将 CLI agent 以 JSON-RPC 嵌入多语言应用，后者把分析、回放、错误、日志、AI trace 和可审阅 PR 汇成自驱动产品闭环。权限、数据隔离、默认工具和自动生成 PR 必须单独审查。

### Forward Deployed Engineering / Enterprise AI Deployment

- 本次没有新的 FDE 一手报道。`fde-hub` 的 7 月 14 日《What Thirty Recruiter Messages Say About the FDE Market》已读正文，但属于作者对约 30 条招聘私信的个人样本；它能说明岗位需求感知，不足以证明市场规模、客户交付周期或组织形态。
- Cars24 是本次最接近企业部署的新增材料，但它是 OpenAI 客户案例。要把它升级为 FDE 趋势证据，还需要客户侧说明现场数据接入、上线时间、失败项目、维护归属和反馈如何回到产品。

### Indie Hacking / Solo Founder

- `levelsio` 的多条 `direct-x` 把 Kimi K3、OpenCode 和 Windows XP 模拟器串在一起，属于个人开发者的模型迁移/工具试用线索；它体现模型与 harness 可替换性，但没有可重复的任务集、成本和失败率。
- `marclou` 关于 TrustMRR 收入分布的推文可作为独立开发者收入透明化线索；`jackfriks` 关于产品被 AI 回答提及的帖子可作为“AI 结果中的分发”线索。两者均为 `direct-x` 个人/产品方陈述，不能升级为市场统计或增长因果。

### Product / Growth / GTM

- OpenAI 的 scorecard 把产品/增长指标从席位和活跃用户转向完成的工作量、成功任务成本和可依赖性；Cars24 则提供了从获客、售后到内部流程的应用样例。这两条合在一起，说明企业价值叙事正在围绕“工作流闭环”而非单次聊天展开。
- `Nutlope/hallmark` 将网页生成从模板套色变成宏观结构、主题选择、反模式检查和人工审阅；它适合记录为产品化设计流程线索，不代表生成页面的转化或品牌效果。

### AI Systems / Automation

- `github/copilot-sdk` 的架构是“应用 → SDK → JSON-RPC → Copilot CLI server”，SDK 负责 CLI 进程生命周期，应用可以提供权限处理、自定义 agent、技能和工具。它把 agent 的控制面暴露给产品开发者，但默认工具接近 `--allow-all` 的说明意味着集成时必须显式收紧权限。
- `tirth8205/code-review-graph` 的增量 AST 图、变更影响范围和 MCP 查询形成“只读必要上下文”的自动化链路；`PostHog` README 的 self-driving mode 则把产品信号转成研究报告和待审阅 PR。两者都是 Trending/README 证据，尚无本仓安装或性能复现。

### X/Twitter 推主主题摘要

以下内容来自 [`twitter-topic-brief.json`](../raw/2026-07-18/twitter-topic-brief.json)。每条只证明发布者说过这些话，均保留 `direct-x`，不代表独立事实核验；同一推文在多个主题出现时按一条直接证据理解。

- **LLM / Frontier Models**：`levelsio` 的 [Kimi K3 + OpenCode 编程步骤](https://x.com/levelsio/status/2078097783140053340)、[K3 实际使用反馈](https://x.com/levelsio/status/2078170967998689480)和 `simonw` 的 [Kimi K3 笔记](https://x.com/simonw/status/2077852005129933247)是高分 `direct-x`；前两条是个人体验，后者链接到可读二手长文。
- **AI Agent / Agentic Workflow**：`mattpocockuk` 的 [`/grill-with-docs` + `/wayfinder`](https://x.com/mattpocockuk/status/2078031590337245518)、[分轮提问](https://x.com/mattpocockuk/status/2078077849785815465)和 `EXM7777` 对 Claude Code harness 的[体验评价](https://x.com/EXM7777/status/2078201571675128314)均为 `direct-x`；没有独立效率或可靠性数据。
- **AI Coding / Developer Tools**：`levelsio` 的 [Kimi K3/OpenCode](https://x.com/levelsio/status/2078093365455790526)、`rileybrown` 的 [Skills 不跨 GPT Work 会话](https://x.com/rileybrown/status/2078164670406402361)和 `mattpocockuk` 的 [问题地图工作流](https://x.com/mattpocockuk/status/2078031590337245518)是主要直接线索；只把它们当回归/试用线索。
- **AI Governance / Public Legitimacy**：OpenAI 的[赛车 AI 讨论](https://x.com/OpenAI/status/2077807977193714080)、`simonw` 对 Kimi K3 的[基准边界说明](https://x.com/simonw/status/2077852005129933247)和 OpenAI 的[GPT-5.6 Sol 用户反馈转发](https://x.com/OpenAI/status/2077928568894709905)为 `direct-x`，其中前后两条是宣传或转述，不能替代政策/安全正文。
- **Indie Hacking / Solo Founder**：`levelsio` 的[模型迁移体验](https://x.com/levelsio/status/2078097783140053340)、`marclou` 的[TrustMRR 收入分布](https://x.com/marclou/status/2078137404180005137)与 `jackfriks` 的[AI 结果分发](https://x.com/jackfriks/status/2077824704774025317)为 `direct-x`；收入、曝光和效果均待核验。
- **Product / Growth / GTM**：`levelsio` 的[Kimi K3 生成浏览器桌面](https://x.com/levelsio/status/2078083496950501746)、`marclou` 的[收入透明化产品](https://x.com/marclou/status/2077736510657626203)和 `rileybrown` 的[技能迁移抱怨](https://x.com/rileybrown/status/2078164670406402361)提供产品线索，但没有留存/转化证据。
- **AI Systems / Automation**：`EXM7777` 关于“系统而非单模型”的[创意工作流观点](https://x.com/EXM7777/status/2078102076396335241)、`steipete` 的[提交实时吐槽工具](https://x.com/steipete/status/2078014859896336892)和 `cnyzgkc` 的 Codex[活动信息](https://x.com/cnyzgkc/status/2077993721279422600)为 `direct-x`；后者属于活动线索，需官方页面核验。
- **AI Infrastructure / Open Source**、**Forward Deployed Engineering / Enterprise AI Deployment**：本次 topic brief 没有足够的高分直接条目；不把账号没有进入主题摘要解释成账号无更新。

### GitHub Trending / Daily Repos

本次页面解析 10 个仓库，Trending description 与 README 均可读，以下统一标为 `secondary-source`。上榜只代表当天发现信号；涉及自动执行、凭据、注入器或数据/许可风险的项目必须隔离验证。

- [`codecrafters-io/build-your-own-x`](https://github.com/codecrafters-io/build-your-own-x)：按主题收集从零实现 Kafka、数据库、编译器、浏览器、神经网络等教程，适合把抽象系统拆成可运行练习；它是学习资源索引，不保证外链维护、代码质量或许可一致性。
- [`PostHog/posthog`](https://github.com/PostHog/posthog)：开源产品分析与 AI 可观测平台，把事件、回放、错误、日志、实验、成本和 agent trace 汇到同一产品面，并能把信号形成报告与待审阅 PR。它适合关注“观测—诊断—修复”闭环，但自动读取业务数据、生成修改和发布门禁必须审查。
- [`HenryNdubuaku/maths-cs-ai-compendium`](https://github.com/HenryNdubuaku/maths-cs-ai-compendium)：以直觉优先的开放教材覆盖数学、计算机和 AI，从向量、概率到生产工程、GPU、推理和系统设计，并附 MCP 知识库服务。它面向想建立完整心智模型的学习者；教材自述的学习效果和 MCP 工具边界仍需自行核验。
- [`Nutlope/hallmark`](https://github.com/Nutlope/hallmark)：面向 Claude Code、Cursor 和 Codex 的设计 skill，按 brief 选择宏观结构和主题，运行 57 个反模板化检查，也支持 audit、redesign、study。它解决网页生成同质化，不等于通用设计质量保证；安装前应审查 skill 脚本与输出。
- [`github/copilot-sdk`](https://github.com/github/copilot-sdk)：为六种语言提供 Copilot CLI SDK，通过 JSON-RPC 连接 CLI server，支持 BYOK、权限处理、自定义 agent/skill/tool 和外部 server。README 说 Node/Python/.NET 可自动携带 CLI，Go/Java/Rust 需额外准备；订阅、账单和默认工具权限是集成前置条件。
- [`anthropics/cwc-workshops`](https://github.com/anthropics/cwc-workshops)：Anthropic 的 Code with Claude 教学材料，覆盖模型选择、技能/MCP 多 agent 分解、managed agent、记忆服务、评测驱动生成和研究桌面。README 明确“不维护、不接受贡献”，只能当 workshop 样例，不当作当前产品路线。
- [`PrismML-Eng/Bonsai-demo`](https://github.com/PrismML-Eng/Bonsai-demo)：本地运行 1-bit/ternary Bonsai 模型的示例，支持多种硬件；27B README 描述视觉、原生工具调用、MCP、推理强度和 256k+ 上下文。私有模型访问、量化质量、硬件吞吐和 tool sandbox 都要实测。
- [`protocolbuffers/protobuf`](https://github.com/protocolbuffers/protobuf)：Google 的跨语言结构化数据序列化格式，README 提醒优先使用稳定 release，并给出 Bazel/Bzlmod 与各语言 runtime 安装路径。它是基础设施维护信号，不是 AI 专属项目；主分支兼容性和构建稳定性仍应按 release pin。
- [`tirth8205/code-review-graph`](https://github.com/tirth8205/code-review-graph)：用 Tree-sitter、增量更新、调用/继承/测试边构建代码图，通过 MCP 返回变更 blast radius 和最小 review 集合，并提供多平台安装器。README 自报大仓库 token 减少和秒级增量索引，需在目标仓库复现，安装器写入配置前先用 dry-run。
- [`docusealco/docuseal`](https://github.com/docusealco/docuseal)：开源 PDF 表单填写与电子签名平台，支持 API/webhook、SMTP、对象存储、Docker 和多种嵌入方式，AGPLv3 另有附加条款。它与 AI 主线弱相关，但可作为企业文档自动化发现；合规、身份验证和许可证义务必须单独评估。

## 3. 来源证据表

| 来源 | 当日覆盖 | 证据归档 | 证据边界 |
| --- | --- | --- | --- |
| RSS/Atom | 32 源，31 成功；51 个匹配/一手条目正文 51/51 `ok` | [`rss-items.json`](../raw/2026-07-18/rss-items.json)、[`rss-fulltext/`](../raw/2026-07-18/rss-fulltext/) | `nabeel-qureshi` XML 解析失败；正文使用 `curl` 或失败后的 `opencli-read`，历史条目仍按发布时间判断新旧。 |
| GitHub release | 7 源通过 Atom 成功；一手正文 4/10 `ok`、6/10 `limited` | [`github-items.json`](../raw/2026-07-18/github-items.json)、[`github-release-fulltext/`](../raw/2026-07-18/github-release-fulltext/) | OpenAI Codex alpha 与 Claude Code `v2.1.209` 的 limited 正文不支持具体功能判断。 |
| GitHub Trending | 10 个仓库，Trending description 10/10，README 10/10 成功 | [`github-trending.json`](../raw/2026-07-18/github-trending.json)、[`github-trending-readmes/`](../raw/2026-07-18/github-trending-readmes/) | 全部 `secondary-source` discovery signal，不代表质量、采用或安全。 |
| 官方页面 | 4/4 页面状态 `ok` | [`official-pages.json`](../raw/2026-07-18/official-pages.json)、[`official-page-text/`](../raw/2026-07-18/official-page-text/) | OpenAI News 页面正文通过 `opencli-read`；Claude Blog 只有页面列表中的新条目，没有单篇正文归档。 |
| X/Twitter | 27/27 账号请求 `ok`，126 条保留 | [`twitterapi-io-results.json`](../raw/2026-07-18/twitterapi-io-results.json)、[`twitter-topic-brief.json`](../raw/2026-07-18/twitter-topic-brief.json) | 只使用 `GET /twitter/user/last_tweets`；每条直接证据标为 `direct-x`，不证明完整时间线覆盖。 |
| 官方链接候选 | 0 条候选 | [`official-link-candidates.json`](../raw/2026-07-18/official-link-candidates.json) | 本次 priority X 账号没有达到候选阈值或强治理关键词的官方域名链接；不使用 Exa 补漏。 |

## 4. X/Twitter 覆盖说明

- 本次通过 `twitterapi.io` 结构化只读接口采集，27 个账号均请求成功；接口只返回有限列表，无法证明任一账号完整覆盖过去 24 小时。`karpathy`、`AnthropicAI`、部分中文账号等没有进入保留集时，只能记录筛选边界。
- `direct-x` 只证明账号发布了对应内容。官方账号的产品/政策宣称仍需可读官方正文才能升级为 `official-source + direct-x`；普通账号的个人体验、转述、收入和 benchmark 评价不升级为独立事实。
- `official-link-candidates.json` 本次为空，因此没有可升级的官方链接候选；这不是“没有官方更新”，只是候选规则未命中。

## 5. 不确定性与待验证项

- **来源窗口**：部分 feed 返回历史条目。需要回答“今天发生了什么”时，优先查看条目时间、`state/seen.json` 和 [`manifest.json`](../raw/2026-07-18/manifest.json)，不要把旧正文当新信号。
- **RSS 失败**：`nabeel-qureshi` 因 malformed XML 失败。最小复核路径是下一次运行重试并检查源站 RSS；本次没有用 Exa 或登录态浏览器替代。
- **GitHub limited**：OpenAI Codex `0.145.0-alpha.18`–`.22` 和 Claude Code `v2.1.209` 的 release body 不足以支持功能判断；等 Atom/REST 正文可读后再补充。
- **供应商指标**：GPT-Red 的 84%/13%、0.05% 失败率、scorecard 的模型比较、Cars24 的 1M+/50%/80%/12% 和青少年使用比例均来自供应商或其客户案例。需要第三方复现、客户侧数据、真实日志和统一任务集。
- **Kimi K3**：2.8T 参数、价格、开放权重日期、基准和任务成本来自 Moonshot/作者转述；最小验证是等待开放权重或官方 API 文档，并用固定长程工具任务比较成本、错误率和上下文稳定性。
- **Claude Blog 页面发现**：CISO agentic AI、代码迁移和 Fable 5/Cowork 页面条目已发现但没有单篇本地正文；只能作为待验证候选，不能从标题推导机制或效果。
- **安全复现**：GPT-Red 涉及提示注入与高权限 agent；任何复现都应在隔离账户、临时文件系统、最小权限、可回放日志和人工审批下进行，不要把攻击样例放入真实凭据、生产浏览器或真实 home 目录。
- **Trending 项目**：README 可读只证明项目文档声称了某种机制，不证明安装成功、性能、维护质量、许可或安全；Copilot SDK、Hallmark、code-review-graph、Bonsai 涉及进程、MCP、文件和模型下载，需先审查安装脚本与权限。
- **FDE 覆盖**：本日没有新增 FDE 一手证据。Cars24 是供应商客户案例，FDE Hub 是个人样本；需要客户侧交付周期、失败项目、反馈回流和维护责任来验证长期趋势。
- **候选审计处置**：[`candidate-audit.md`](../reviews/2026-07-18-candidate-audit.md) 的 `missed` 行主要是已读但较早的背景或弱相关条目（例如 [ATL Saathi](https://deepmind.google/blog/empowering-indias-next-generation-of-innovators-with-atl-saathi/)、[LLM cliché highlighter](https://simonwillison.net/2026/Jul/17/llm-cliche-highlighter/#atom-everything)、[The Tower Keeps Rising](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/)、旧 FDE/产品文章），本日报仅在主题或边界中说明，未把它们冒充今日新增。高分 `direct-x` 中，[Claude 抱怨](https://x.com/levelsio/status/2078098490618478815)、[Kimi 的宣传性转述](https://x.com/Hesamation/status/2077870952168251690)、[GPT-5.6 文件删除转述](https://x.com/sama/status/2077810840309510550)、[投资建议](https://x.com/levelsio/status/2078148081137185116)、[Fable pelican 转发](https://x.com/simonw/status/2077868517496590685)和[OpenAI 促销帖](https://x.com/OpenAI/status/2078223217773474134)分别因个人体验、二手/宣传、缺乏原始复现或金融风险而保留为边界，不升级为事实；完整逐项状态见 audit。

## 6. 运行统计

- 新增去重条目：`39`（首次 `RUN_DATE=2026-07-18 python3 scripts/update-state.py`；后续派生步骤未新增）。
- 高信号条目：`7` 条（其中 5 条 `official-source`/官方 release 或官方客户案例，2 条为 `secondary-source`/README 组合证据）。
- 失败来源：RSS `nabeel-qureshi` 1 个；GitHub release 一手正文 `limited` 6 条；X/Twitter 无请求失败；官方链接候选 0 条，不视为失败。
- `twitter-topic-brief`：[`raw/2026-07-18/twitter-topic-brief.json`](../raw/2026-07-18/twitter-topic-brief.json)，27/27 账号成功，126 条 direct-x。
- `report-reading-list`：[`raw/2026-07-18/report-reading-list.json`](../raw/2026-07-18/report-reading-list.json)，359 条，其中 30 条有本地正文。
- 候选审计：写入 [`reviews/2026-07-18-candidate-audit.md`](../reviews/2026-07-18-candidate-audit.md)（日报完成后运行）。

## 7. 完成审计

- 日报已写入 [`docs/2026-07-18-daily-intel.md`](2026-07-18-daily-intel.md)，并按 [`report-reading-list.json`](../raw/2026-07-18/report-reading-list.json) 逐项区分可读正文与结构化边界。
- 所有稳定来源输出、`manifest.json`、`state/source-health.json`、`state/seen.json`、Twitter 原始结果、官方链接候选和主题摘要均已写入当天或状态目录。
- candidate audit 已生成并已对 missed 候选做上述弱相关/边界处置；Trend Phase 2 已写入 [`trend/reports/2026-07-18-trend-report.md`](../trend/reports/2026-07-18-trend-report.md)，并刷新 9 个 enabled 专题：[`memory-dream`](../trend/memory-dream.md)、[`financial-agents`](../trend/financial-agents.md)、[`forward-deployed-engineering`](../trend/forward-deployed-engineering.md)、[`enterprise-delivery-system`](../trend/enterprise-delivery-system.md)、[`codex-feature-watch`](../trend/codex-feature-watch.md)、[`ai-governance-legitimacy`](../trend/ai-governance-legitimacy.md)、[`claude-code-feature-watch`](../trend/claude-code-feature-watch.md)、[`codex-claude-usage-tactics`](../trend/codex-claude-usage-tactics.md)；[`claude-tag-identity`](../trend/claude-tag-identity.md) 保留 `no-new-signal` marker。`python3 scripts/run-trend-stage.py --date 2026-07-18 --check` 已返回 `ok=true`；本日报不创建 `translations/` 输出。
