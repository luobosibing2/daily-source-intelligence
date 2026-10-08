# 2026-07-04 Daily Source Intelligence

## 0. 采集范围

- 时间窗口：2026-07-04 日跑；RSS/Atom、GitHub release、GitHub Trending、官方页面按最近窗口采集，X/Twitter 使用 `twitterapi.io` 的 24-36 小时窗口。
- 配置来源：[config/watch.md](../config/watch.md)、[config/topics.yaml](../config/topics.yaml)、[config/sources.yaml](../config/sources.yaml)、[config/trends.yaml](../config/trends.yaml)。
- 生成时间：2026-07-04T23:02:01+08:00。
- 原始归档目录：[raw/2026-07-04/](../raw/2026-07-04/)。
- 阅读清单：[report-reading-list.json](../raw/2026-07-04/report-reading-list.json)，共 397 条，其中 68 条有本地正文，329 条为结构化或边界条目。
- GitHub Trending：1 个 daily trending 源成功，解析 10 个 repo，10 个 Trending description 均保留，10 个 README 均写入本地归档；Trending 只作为 discovery signal，不作为质量、采用、安全或投资收益背书。

## 1. 今日高信号

| 等级 | 主题 | 标题/信号 | 来源 | 证据等级 | 链接 | 为什么重要 |
| --- | --- | --- | --- | --- | --- | --- |
| 高 | 科研 Agent 评测 | OpenAI 发布 `GeneBench-Pro`，用 129 个计算生物学任务测试模型在含噪数据、目标估计、诊断和迭代分析中的判断能力 | OpenAI Blog | official-source | [原文](https://openai.com/index/introducing-genebench-pro) / [归档](../raw/2026-07-04/rss-fulltext/openai-blog/openai-blog-introducing-genebench-pro-3c92349443.opencli.md) | 这是“agent 能不能做真实研究判断”的官方 benchmark，不只是工具调用准确率；它把歧义处理、路径选择、假设修正和决策就绪性变成评测对象。 |
| 高 | AI 普及 / 政策数据 | OpenAI Signals 显示 ChatGPT 使用深度、任务广度、地区覆盖和非英语使用继续扩张 | OpenAI Blog | official-source | [原文](https://openai.com/index/how-chatgpt-adoption-has-expanded) / [归档](../raw/2026-07-04/rss-fulltext/openai-blog/openai-blog-how-chatgpt-adoption-has-expanded-fb435a036a.opencli.md) | 这是官方一手的全球使用数据，适合支撑 AI 普及与公共合法性讨论；边界是聚合统计和分类方法来自 OpenAI 自述。 |
| 高 | Claude Code / 成本与调度 | Simon Willison 记录 Fable/Claude Code 使用经验：把小型编码任务委托给低功耗 subagent，把判断、审计和综合留给主模型 | RSS fulltext | secondary-source + direct-X | [原文](https://simonwillison.net/2026/Jul/3/judgement/) / [归档](../raw/2026-07-04/rss-fulltext/simonwillison/simonwillison-fable-s-judgement-01284d0383.extracted.md) | 这条信号把“模型能力”转成“多模型成本路由和任务分层”的实操模式；它是开发者经验，不是官方能力承诺。 |
| 中高 | 企业 Agent 生产化 | FDE Hub 的 eval lifecycle 把 PoC 到生产拆成检索评测、忠实性、引用准确率、guardrail、adversarial test 和上线 gate | RSS fulltext | secondary-source | [原文](https://www.fdehub.org/p/the-eval-lifecycle) / [归档](../raw/2026-07-04/rss-fulltext/fde-hub/fde-hub-the-eval-lifecycle-what-actually-happens-between-proof-of-concept-and-af0c7a85ff.extracted.md) | 它给企业交付系统补了一套可执行的质量门槛：demo 之后不是“润色”，而是从可控输入转向真实用户、脏数据、数字指标和持续监控。 |
| 中高 | Agent 机制设计 | Forward Deployed Episode 6 讨论把市场机制、价格、竞争和生态学习引入 agent 系统，而不是只靠中央规划式 orchestration | RSS fulltext | secondary-source | [原文](https://www.forwarddeployed.com/p/forward-deployed-episode-6-market) / [归档](../raw/2026-07-04/rss-fulltext/forward-deployed/forward-deployed-forward-deployed-episode-6-market-mechanisms-for-agents-88f1c49929.opencli.md) | 这是 FDE/agent 系统设计的机制信号：长期问题可能不只是模型更强，而是 agent 之间如何分工、出价、竞争和反馈学习。 |
| 中高 | 企业迁移评测 | Hugging Face / IBM Research 发布 `ScarfBench`，面向企业 Java 框架迁移评测 AI agents | Hugging Face Blog | secondary-source | [原文](https://huggingface.co/blog/ibm-research/scarfbench) / [归档](../raw/2026-07-04/rss-fulltext/huggingface-blog/huggingface-blog-scarfbench-benchmarking-ai-agents-for-enterprise-java-framework-migrat-8654826289.opencli.md) | 企业代码迁移是比玩具 repo 更硬的 agent 场景；这条线索适合进入“企业交付系统”和“agent 评测”观察，但 benchmark 效果仍需看任务集与复现实验。 |
| 中高 | Agent 间工具分发 | `openai/codex-plugin-cc` 上榜，README 确认 Claude Code 内可用 Codex 做代码审查、委托任务、后台状态和结果管理 | GitHub Trending | secondary-source | [repo](https://github.com/openai/codex-plugin-cc) / [README](../raw/2026-07-04/github-trending-readmes/openai__codex-plugin-cc.md) | 这是 Codex 与 Claude Code 工作流互嵌的强 discovery signal；它说明 agent 工具不只竞争，也开始以插件方式互相调用。 |
| 中高 | 浏览器 Agent | `alibaba/page-agent` 上榜，README 描述在网页内注入 JavaScript，让用户用自然语言控制 Web 界面，并支持 BYO LLM、扩展和 MCP | GitHub Trending | secondary-source | [repo](https://github.com/alibaba/page-agent) / [README](../raw/2026-07-04/github-trending-readmes/alibaba__page-agent.md) | 它代表轻量 in-page GUI agent 路线：不依赖截图、多模态或 headless browser，把 agent 控制面嵌进产品页面。 |
| 中高 | Agent 安全测试 | `usestrix/strix` 上榜，README 描述多 agent 渗透测试、动态运行、PoC 验证、自动修复和 CI/CD 阻断 | GitHub Trending | secondary-source | [repo](https://github.com/usestrix/strix) / [README](../raw/2026-07-04/github-trending-readmes/usestrix__strix.md) | 安全测试正在成为 agent 发布门禁的一部分；高风险边界是 README 自述不能替代靶场复现或漏洞验证质量证明。 |
| 中 | Agent 终端编排 | `ogulcancelik/herdr` 上榜，README 描述在真实终端中运行多个 coding agents，显示 blocked/working/done，并支持持久会话和远程重连 | GitHub Trending | secondary-source | [repo](https://github.com/ogulcancelik/herdr) / [README](../raw/2026-07-04/github-trending-readmes/ogulcancelik__herdr.md) | 多 agent 工作流开始需要“队列/状态/终端会话”层；它是 workflow infra discovery signal，未验证稳定性和跨工具状态识别准确率。 |

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog 今天可读正文质量较高：`GeneBench-Pro` 聚焦计算生物学研究判断，`How ChatGPT adoption has expanded` 聚焦全球使用扩张，`Core dump epidemiology` 属于数据基础设施事故复盘，`Mapping Europe’s AI Workforce Opportunity` 是劳动力政策材料，`Inside Genebench-Pro` 提供案例页。
- OpenAI/Codex GitHub release Atom 今天 5 条均归档，但 `fulltext_status=limited`，只作为 release 线索，不写具体机制结论。
- Claude Code release Atom 今天 5 条归档，其中 `v2.1.197` 到 `v2.1.200` 为可读，`v2.1.201` 为 limited；今天没有像 2026-07-02 那样明确的默认模型级 release 主信号，更多是版本跟踪。

### X/Twitter 推主主题摘要

- AI Agent / Agentic Workflow：高分 direct-X 包括 `marclou` 的“commodity SaaS 做成 AI agent first”、`steipete` 的 Codex 设计迭代和给 agent 独立电脑做端到端测试、`EXM7777` 的 Fable/Obsidian/Claude Code 使用流。它们是 field note，不代表行业统计。
- AI Coding / Developer Tools：`simonw` 的 Fable 判断力用法与本地 RSS 正文互相印证；`steipete`、`mattpocockuk`、`EXM7777` 继续围绕 Codex、Claude Code、skills 和 subagent 成本控制出现大量实践贴。
- AI Governance / Public Legitimacy：今天 direct-X 中有“让模型自己判断何时测试/何时委托”的使用治理信号，但它主要是个人 workflow 规则，不能等同于组织级合规。
- Product / Growth / Indie：`marclou`、`levelsio` 等账号出现较多收入、产品、增长和 agent-first SaaS 观点；日报只保留与 agent 分发、成本控制、工具使用直接相关的部分。
- 覆盖边界：`twitterapi.io` 总体 `ok`，27 个账号均 `ok`，保留 110 条 direct-X；部分账号原始返回为 0，只能说明本轮 API 返回情况。

### LLM / Frontier Models

- `GeneBench-Pro` 说明前沿模型评测正在从“能否回答标准题”转向“能否在真实科研脏数据中做判断”。它把研究 taste、诊断、迭代、目标估计和决策就绪性列为能力对象。
- OpenAI Signals 的使用扩张材料提供了普及侧证据：用户随时间发更多消息、尝试更多任务，非英语和全球南方使用占比继续增长。
- Fable/Claude Code 相关信号来自 Simon Willison 与 direct-X，核心不是单次输出质量，而是把昂贵模型用于判断、审查、综合，把实现工作路由给低功耗模型或 subagent。

### AI Agent / Agentic Workflow

- `codex-plugin-cc` 是今天最直观的 agent 间互操作信号：Claude Code 用户可以通过插件调用 Codex 做 review、rescue、transfer、status、result、cancel 等任务。
- `page-agent` 代表产品内 GUI agent：通过网页内 JavaScript 读取和操作 DOM，用自然语言完成表单、ERP/CRM/admin 流程和多页任务。
- `herdr` 代表多 agent 运行时管理：它不是模型能力，而是让多个 coding agent 在真实终端里可视化、可恢复、可远程重连。

### AI Coding / Developer Tools

- Simon Willison 的 Fable 使用经验值得进入 coding-agent 使用策略：让模型自己判断何时写测试、何时降级委托，可能比人手写死规则更稳；边界是它来自个人项目实践。
- `ChromeDevTools/chrome-devtools-mcp` 上榜显示浏览器调试和性能诊断继续向 MCP 暴露；README 同时明确浏览器内容会暴露给 MCP client，隐私边界需要用户主动管理。
- `system_prompts_leaks` 上榜属于高热度但高风险/低可信 discovery：README 自述收集多家模型和工具的 system prompt，适合作为生态现象记录，不作为事实权威或合规材料。

### AI Infrastructure / Open Source

- `Strix` 把 agent 放进安全测试和 CI/CD；如果后续能复现，它可能连接“agent 生成代码”与“agent 验证/修复代码”的闭环。
- `page-agent`、`chrome-devtools-mcp` 和 `herdr` 分别覆盖网页内控制、浏览器调试、终端编排，显示 agent 工具层正在围绕真实执行环境分化。
- `Zackriya-Solutions/meetily` 是本地优先会议助手，README 强调 Rust、Parakeet/Whisper、说话人分离、Ollama 总结和不依赖云；与 agent 主线弱一些，但属于隐私优先 AI app discovery。

### Forward Deployed Engineering / Enterprise AI Deployment

- FDE Hub eval lifecycle 的价值在于把企业 AI 生产化拆成 gate：检索召回/准确率、回答忠实性、引用准确率、guardrail 违规率、人工专家标注、上线后 SLO 和监控。
- `ScarfBench` 把 enterprise Java migration 作为 agent benchmark，说明企业遗留系统迁移正在成为比 demo 更硬的评测场景。
- Forward Deployed Episode 6 的“market mechanisms for agents”把 agent 系统从单体编排转向生态机制：价格、竞争、选择和反馈可能成为长期交付效率的关键变量。

### AI Governance / Public Legitimacy

- OpenAI Signals 是今天最强的治理/公共叙事材料：它把用户普及、地区扩张、语言变化和研究数据下载放进官方解释框架。
- `GeneBench-Pro` 也有治理含义：当 AI 进入科研判断，评测需要避免捷径、泄漏、任意偏好和数值不敏感问题；这比普通 benchmark 更强调审计设计。
- 浏览器/MCP/GUI agent 工具上榜时也暴露治理边界：`chrome-devtools-mcp` 明确提示浏览器内容会暴露给客户端，`page-agent` 的 demo LLM 仅适合技术评估。

### Financial Agents

- 今天没有新的强金融 agent 一手信号。`levelsio` 的股票泡沫检测、产品增长和收入类 direct-X 只能作为个人产品/市场情绪，不写成金融 agent 趋势判断。
- 任何交易、投资、收益或市场指标相关 direct-X 都不作为投资建议或效果证明。

### GitHub Trending / Daily Repos

- `openai/codex-plugin-cc`：Claude Code 插件，用 Codex 做代码 review、任务委托和后台 job 管理；README 可确认 slash commands、安装路径和 Codex 登录要求。
- `JuliusBrussee/caveman`：Claude Code skill，用极简表达压缩交互 token；这是成本/提示风格 experiment，需实测节省和质量影响。
- `alibaba/page-agent`：网页内 GUI agent，用 JavaScript 和文本 DOM 操作让用户自然语言控制 Web 界面；适合 SaaS copilot、表单和 admin 流程。
- `usestrix/strix`：开源 AI 渗透测试工具，强调动态运行、PoC 验证、多 agent、自动修复和 CI/CD 阻断；安全效果需独立复现。
- `ChromeDevTools/chrome-devtools-mcp`：面向 coding agents 的 Chrome DevTools MCP server，覆盖截图、网络、console、性能 trace 和自动等待；隐私/遥测边界需注意。
- `Zackriya-Solutions/meetily`：本地优先 AI 会议助手，主打本地转录、说话人分离、Ollama 总结和无云处理。
- `asgeirtj/system_prompts_leaks`：system prompt 收集仓，生态热度高但真实性、来源授权和合规边界需谨慎。
- `harvard-edge/cs249r_book`：机器学习系统教材，适合作为 ML systems 背景材料，不是今日 agent 产品信号。
- `rommapp/romm`：自托管 ROM 管理器/播放器，与本仓主线弱相关。
- `ogulcancelik/herdr`：终端内 agent multiplexer，支持真实终端、多 pane、agent 状态、持久会话和远程重连。

## 3. 来源证据表

| 来源 | 类型 | 原文链接 | 本地归档 | 证据等级 | 备注 |
| --- | --- | --- | --- | --- | --- |
| GeneBench-Pro | OpenAI Blog | <https://openai.com/index/introducing-genebench-pro> | [opencli.md](../raw/2026-07-04/rss-fulltext/openai-blog/openai-blog-introducing-genebench-pro-3c92349443.opencli.md) | official-source | 研究级计算生物学 agent benchmark。 |
| ChatGPT adoption | OpenAI Blog | <https://openai.com/index/how-chatgpt-adoption-has-expanded> | [opencli.md](../raw/2026-07-04/rss-fulltext/openai-blog/openai-blog-how-chatgpt-adoption-has-expanded-fb435a036a.opencli.md) | official-source | OpenAI Signals 使用扩张数据。 |
| Fable's judgement | Simon Willison | <https://simonwillison.net/2026/Jul/3/judgement/> | [extracted.md](../raw/2026-07-04/rss-fulltext/simonwillison/simonwillison-fable-s-judgement-01284d0383.extracted.md) | secondary-source | Fable/Claude Code 使用策略。 |
| FDE eval lifecycle | FDE Hub | <https://www.fdehub.org/p/the-eval-lifecycle> | [extracted.md](../raw/2026-07-04/rss-fulltext/fde-hub/fde-hub-the-eval-lifecycle-what-actually-happens-between-proof-of-concept-and-af0c7a85ff.extracted.md) | secondary-source | 企业 agent 生产化 gate。 |
| Market mechanisms for agents | Forward Deployed | <https://www.forwarddeployed.com/p/forward-deployed-episode-6-market> | [opencli.md](../raw/2026-07-04/rss-fulltext/forward-deployed/forward-deployed-forward-deployed-episode-6-market-mechanisms-for-agents-88f1c49929.opencli.md) | secondary-source | agent 生态机制讨论。 |
| ScarfBench | Hugging Face Blog | <https://huggingface.co/blog/ibm-research/scarfbench> | [opencli.md](../raw/2026-07-04/rss-fulltext/huggingface-blog/huggingface-blog-scarfbench-benchmarking-ai-agents-for-enterprise-java-framework-migrat-8654826289.opencli.md) | secondary-source | 企业 Java 迁移 agent benchmark。 |
| Codex plugin for Claude Code | GitHub Trending + README | <https://github.com/openai/codex-plugin-cc> | [README](../raw/2026-07-04/github-trending-readmes/openai__codex-plugin-cc.md) | secondary-source | Claude Code 内调用 Codex。 |
| Page Agent | GitHub Trending + README | <https://github.com/alibaba/page-agent> | [README](../raw/2026-07-04/github-trending-readmes/alibaba__page-agent.md) | secondary-source | 网页内 GUI agent。 |
| Strix | GitHub Trending + README | <https://github.com/usestrix/strix> | [README](../raw/2026-07-04/github-trending-readmes/usestrix__strix.md) | secondary-source | AI 渗透测试，高风险需复现。 |
| X/Twitter direct evidence | twitterapi.io | n/a | [twitterapi-io-results.json](../raw/2026-07-04/twitterapi-io-results.json) | direct-x | API 总体可用，保留 110 条 direct-X。 |

## 4. X/Twitter 覆盖说明

- 本日报通过 `twitterapi.io` 收集 X/Twitter 直接证据，不使用官方 X API，不使用 Exa MCP，不使用登录态浏览器。
- `twitterapi.io` 总体状态为 `ok`；27 个账号均返回 `ok`。其中 `rryssf_`、`Yangyixxxx`、`zhaogua61654931`、`lidang` 等账号本轮 `raw_count=0`，不能扩展解释为账号完整无更新。
- 当天保留 direct-X 110 条。高分内容主要集中在 Fable/Claude Code/Codex 使用实践、AI agent-first SaaS、subagent 成本控制、agent 端到端测试和独立开发/增长。
- [official-link-candidates.json](../raw/2026-07-04/official-link-candidates.json) 状态为 `empty`，没有可升级的一手官方链接候选。

## 5. 不确定性与待验证项

- RSS 失败来源：`dwarkesh-patel`。这不是“无更新”，只是本轮源级失败。
- GitHub API release path 为 `skipped`，release 证据来自 Atom feed；OpenAI/Codex 5 条 release fulltext 和 Claude Code `v2.1.201` 为 `limited`，不能写具体 release body 机制结论。
- GitHub Trending 是 discovery signal。`codex-plugin-cc`、`page-agent`、`Strix`、`chrome-devtools-mcp`、`herdr` 的 README 已归档，但未本地安装、运行或安全验证。
- direct-X 只证明 API 返回了公开推文文本和链接；模型能力、销售效果、治理判断或产品可用性仍需要官方材料、代码运行或独立评测补证。

## 6. 运行统计

- 新增条目：`seen_added=58`，`seen_total=2744`。
- 高信号条目：10 条。
- 稳定来源：RSS 31/32 成功，RSS fulltext 54/54 ok；GitHub release sources 7/7 成功，release fulltext 4/10 ok、6/10 limited；GitHub Trending 1/1 成功，10 个 README 文件归档；官方页面 4/4 ok。
- X/Twitter：`twitterapi.io` 成功，direct-X 110 条，27 个账号级状态均为 `ok`。
- official-link candidates：0 条。
- candidate audit：[reviews/2026-07-04-candidate-audit.md](../reviews/2026-07-04-candidate-audit.md)，将在日报写入后生成并按 missed 候选复核。

### Candidate audit 处理记录

以下条目被 audit 识别为候选时的处理原则：一手全文、agent 工作流、coding agent、企业交付、安全高风险和官方 release 优先；`limited` 全文、历史窗口、泛工程教程、弱相关产品/独立开发社交内容、转推或无官方原文的 direct-X 只记录边界。

- 一手重点源：OpenAI `GeneBench-Pro`、OpenAI Signals、`Core dump epidemiology`、`Mapping Europe’s AI Workforce Opportunity` 已按官方可读正文处理；OpenAI/Codex release limited，仅保留 release 边界；Claude Code 可读 release 只作为版本跟踪。
- Claude / Fable / Codex 使用策略：Simon Willison 的 `Fable's judgement` 和相关 direct-X 已进入高信号、AI Coding 与 X/Twitter 摘要；个人经验不升级为官方能力声明。
- FDE / 企业交付：`The Eval Lifecycle`、`Forward Deployed Episode 6`、`ScarfBench` 已进入高信号或主题摘要；其它 FDE 背景文只作为趋势背景。
- GitHub Trending：`openai/codex-plugin-cc`、`alibaba/page-agent`、`usestrix/strix`、`ChromeDevTools/chrome-devtools-mcp`、`ogulcancelik/herdr` 已按 README 归档处理；`meetily`、`system_prompts_leaks`、`cs249r_book`、`romm`、`caveman` 按边界处理。
- top direct-X：Fable/Claude Code/Codex/subagent/workflow/agent-first SaaS 已通过 X 摘要或本地正文处理；泛增长收入、生活内容、传闻、纯转推或无可读官方原文的产品夸赞不进入高信号。

#### audit 候选逐项覆盖

- OpenAI / Google 官方与准官方 RSS：`Core dump epidemiology: fixing an 18-year-old bug` 作为 OpenAI 数据基础设施事故复盘处理；`Start building with Nano Banana 2 Lite and Gemini Omni Flash`、`Introducing computer use in Gemini 3.5 Flash`、`Unlocking UK house-building with AI-accelerated planning` 是可读官方材料，但今天主线优先级低于 `GeneBench-Pro` 和 OpenAI Signals，分别作为多媒体模型、computer use 和公共部门 AI 背景；`Featuring Every Eval Ever Results on Hugging Face Model Pages` 作为 eval 展示/模型页背景，弱于 `ScarfBench` 与 FDE eval lifecycle。
- Simon Willison / 工具背景 RSS：`Open Source AI Gap Map`、`Quoting Josh W. Comeau`、`June 2026 newsletter`、`llm-coding-agent 0.1a0` 都已归入 LLM / AI Coding 背景；只有 `Fable's judgement` 同时有正文和 direct-X 呼应，进入今日高信号。
- 长期 LLM / infra 背景：`Extrinsic Hallucinations in LLMs`、`AI inference is obviously profitable`、`AI GPUs probably live longer than three years`、`Why are cached input tokens cheaper with AI services?`、`The mysterious Hy3 LLM is topping OpenRouter Model Rankings by a large margin`、`Claude Haiku 4.5 does not appreciate my attempts to jailbreak it`、`Liminality`、`AI will be massively deflationary` 是可读背景，但不是今天新增发布或工作流主信号。
- Antirez / Lucumr / Geohot 技术文章：`A new era for software testing`、`Distributing LLM inference in DwarfStar`、`Alternatives for the EDIT tool of LLM agents`、`A few words on DS4`、`Redis array type: short story of a long development`、`The Coming Loop`、`Dangerous Technology For Americans Only`、`Gaslighting Openness`、`Communities of Not`、`Clanker: A Word For The Machine`、`Summoning the Demon` 作为 AI coding、infra、开放性和社会叙事背景，不升级为今日高信号。
- 产品 / 工程 / 创业 RSS：`Quickly apply LUTs (color grading) with ffmpeg`、`Lean Launch Pad 2026 @ Stanford - Lessons Learned Presentations`、`AI and Teaching - The Brave New World`、`How to Build a Webhook System in Rails Using Sidekiq`、`How to License and Distribute a Private Node Module`、`Great Products, Bad Companies`、`Build To Learn FAQ`、`Build to Learn vs Build to Earn`、`Commercial vs Internal Products`、`Product Coaching and AI`、`Charts of the Week: Cycles, different but the same` 是可读但弱相关的产品/工程材料。
- FDE / 运营 RSS：`Forward Deployed, Episode 5: Aligning Agents`、`Sorry, that isn't an FDE`、`DIY, Context layers and the curious growth of the FDE.`、`Agentic Risk Operations`、`We Tested Marketing Incentives to AI Agents. Here's What Happened.`、`Managing Elasticsearch Reindex at Scale: Performance, Reliability, and Observability` 作为企业交付或运营背景；今天主信号仍是 `The Eval Lifecycle: What Actually Happens Between "Proof of Concept" and "Production"`、`Forward Deployed, Episode 6: Market Mechanisms for Agents` 与 `ScarfBench`。
- 高分 direct-X 已处理为 field note：`> pick commodity SaaS > make it AI agent first > sell the value, not the product...`、`everyone clipped Karpathy talking about vibe coding... and slept on the BIGGEST thing he...`、`If you think codex sucks at design, try "use imagegen to re-imagine this design and imple...`、`Fable x Obsidian inside Claude Code is literally insane... and there will never be a bett...`、`Give your agent its own computer to REALLY end to end test stuff. https://t.co/kvaA8guwXL`、`The most interesting Fable tip I've heard so far is to let the model use its own judgemen...`、`when a researcher from OpenAI, DeepMind, and Stanford drops an article like this, you kno...`、`Quick PSA for anyone using Claude: Fable 5 is back, but it's ONLY included through July 7...`、`this is the ultimate Fable Cheat Sheet... literally EVERYTHING you need to know about: -...`、`RT @theo: Just put together this guide for maximizing your Fable usage https://t.co/YiFFS...`、`RT @anshnanda: This skill can help you cut your Fable token usage by 90%. First, add this...` 均已归入 Fable/Claude Code/Codex 使用策略，不作为官方能力声明。
- 高分 direct-X 只保留边界：`I remember when I was making $50K/mo with ShipFast in 2024, some people said, "Yeah, but...`、`Highest payout on X so far. That's 1.2X more of what I should have earned per month as an...`、`I made a live stock market bubble detector that shows bubble indicators updated multiple...`、`3 new sponsors overnight on TrustMRR`、`I juste went on the biggest French tech podcast with my startup mentor`、`interesting, solo founder, and currently have over 50,000 users on Thumio pretty cool.`、`Get acquired: @trust_mrr https://t.co/zUen0Aohr2`、`Very interesting story about Southern Europe's wild fires There's a whole private industr...` 属于增长、个人产品或市场情绪，不进入高信号。
- 弱相关、转推或不可验证 direct-X：`Great night hanging with the Claude Code folks.`、`Shoutout to @vhbrzezowski for is rad CodexBar website redesign!`、`I fed Fable 80.000 of my tweets so it could roast me even more.`、`https://t.co/zXM38P3HGs`、`RT @MitcheIl: "Honey, why don't you come downstairs and show everyone what you built with...`、`I just started reading this book and the whole premise was like "omg Apple is so dependen...`、`RT @EXM7777: Fable x Obsidian inside Claude Code is literally insane...`、`people have their opinions. but Cursor is still number 1 to me.`、`第一批Vibe Coding 的受害者出现了~`、`RT @MiTypeScript: ~60% Fable cost cut by transparently turning the code into an image and...`、`RT @jeremy_daly: "Half of the companies here at @aiDotEngineer could be a markdown file!"...`、`Some days I feel like a double agent, sitting at the OpenAI office, making sure Fable 5 w...`、`I fucking love prototyping Wayfinder killing it again with a modal I can open anywhere to...`、`Feels like categorising models got harder recently I used to put models in the bucket of...`、`"Evals on skills are hard" is the understatement of the year`、`AI inference engineering is one of the most critical skills AI labs are looking for to ma...`、`Fable 5 is NOT NERFED after the ban, per Arena.`、`RT @robertskmiles: If your software product doesn't have a text box where I can write a f...`、`嗯嗯 Codex 应该已经这么做了`、`补一个：通过 SSH 控制 这样，服务器也可以交给 Codex 打理了`、`my cloud agent ran for 107 hours straight.` 可作为 field note，但缺少可读一手材料或实测闭环。
- 明确剔除的 weak direct-X：`Fuck. I did my 6-month blood test`、`RT @garyvee: The American Dream is not big houses and cars.`、`RT @gokhanamal: Adana'da yillarden beri klimalı duraklar var`、`RT @naval: Happy Birthday America`、`RT @rainisto: AI video - 3 years ago.`、`RT @0xSero: In 12 hours we've had 323 people sign our petition to protect local AI.`、`Yes @Waymo`、`RT @SIGKITTEN: Better call Sol`、`RT @daedalium: I raised $3.5M to build the AI lab`、`The "European AC civil war of 2026" will be studied`、`I'm crying`、`https://t.co/s5DIOHCdxc`、`RT @visakanv: Ok I'm starting a thread of examples of AI copywriting`、`RT @MapleShadow: 博客更新: 为什么我用mattpocock/skills替代了superpowers`、`RT @cellinlab: 最最重要的！别只把 https://t.co/OX3INQZN1a 理解成一个 Agent 商店。`、`RT @vasuman: A thought piece on why private equity is misunderstanding the value add of A...` 不进入日报正文判断。
