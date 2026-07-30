# 2026-07-31 每日源情报

## 直接答案

今天最值得跟进的是三条相互连接的线：

1. 模型竞争继续从“能力”转向“单位结果的成本、速度和工作流配置”。OpenAI 的 GPT‑5.6 Luna/Terra 降价、Sol 的 Fast mode，以及 Responses API 的 reasoning 保留和 compaction，都把模型、推理服务和 agent harness 放在同一个效率问题里。
2. 评测分数越来越像“模型 + API 设置 + harness + 上下文管理”的联合产物。OpenAI 的 ARC‑AGI‑3 原文给出可读的对照实验；这支持重新审查评测 runner，而不是把低分或高分直接归因给裸模型。
3. agent 的下一步瓶颈是长期运维和责任边界：科研软件案例把瓶颈移到验证与 stewardship，Riley Brown 的 `direct-x` 经验提到权限、成员 onboarding、eval、技能、连接和版本维护，Word 提示注入案例则提醒“能执行”不等于“安全执行”。

## 0. 采集范围

- 运行日为北京时间 2026-07-31。权威原始状态见 [`manifest.json`](../raw/2026-07-31/manifest.json)，统一评分后的派生信号见 [`signals.json`](../raw/2026-07-31/signals.json)，正文阅读清单见 [`report-reading-list.json`](../raw/2026-07-31/report-reading-list.json)。阅读清单有 17 项，其中 12 项在北京时间当日日窗口内、5 项时间为 `unknown`；它是阅读路由，不是原始证据全集。
- RSS/Atom：32 个源中 31 个成功；54 条命中关注方向或一手重点源的条目全部尝试正文，54/54 的 `fulltext_status=ok`。`nabeel-qureshi` 连续失败，解析错误为 `not well-formed (invalid token): line 1, column 54`，不能解释成该源没有更新。
- GitHub release：7/7 个 Atom 源成功，REST API 为 `skipped`。一手重点 release 共 10 条，5 条正文可读、5 条 `limited`；其中 OpenAI Codex 4 条、Claude Code `v2.1.220` 1 条受限。
- GitHub Trending：每日页面成功解析 10 个 repo-card，10/10 README 已归档；Trending description 与 README 均保存在 [`github-trending.json`](../raw/2026-07-31/github-trending.json) 和 [`github-trending-readmes/`](../raw/2026-07-31/github-trending-readmes/)。证据等级统一为 `secondary-source`，只表示发现线索，不表示质量、采用率或长期趋势。
- 官方页面：4/4 成功。OpenAI News 列表在 `curl` challenge 后由 OpenCLI 读取，正文只有 510 字符的卡片列表；它不能替代 RSS 文章全文。归档见 [`official-pages.json`](../raw/2026-07-31/official-pages.json)。
- X/Twitter：`twitterapi.io` 处理 27 个账号，27/27 请求成功，保留 152 条 `direct-x`，覆盖窗口为接口返回的约 36 小时。raw 结果、主题摘要和官方链接候选分别见 [`twitterapi-io-results.json`](../raw/2026-07-31/twitterapi-io-results.json)、[`twitter-topic-brief.json`](../raw/2026-07-31/twitter-topic-brief.json) 和 [`official-link-candidates.json`](../raw/2026-07-31/official-link-candidates.json)。

## 1. 今日高信号

- **模型成本与速度一起下探（官方原文 + `direct-x`）**：OpenAI 的 [`Advancing the price-performance frontier with GPT‑5.6`](../raw/2026-07-31/rss-fulltext/openai-blog/openai-blog-advancing-the-price-performance-frontier-with-gpt-5.6-fc362ba711.opencli.md) 说明 GPT‑5.6 Luna 价格下降 80%，Terra 下降 20%；API 价格为 Luna 每百万输入/输出 token `$0.20/$1.20`、Terra `$2/$12`，Sol 新增 Fast mode，最高约 2.5 倍速度、价格约为标准模式 2 倍。Codex 与 ChatGPT Work 的用量计数也随之降低。`OpenAI` 的 [价格说明](https://x.com/OpenAI/status/2082878156483219672) 和 `sama` 的 [价格帖](https://x.com/sama/status/2082880720989532597) 是同日 `direct-x` 发布证据；价格以官方全文为准，企业案例中的成本/质量数字仍是公司自报。
- **评测结果高度依赖 harness（官方原文 + official-link candidate + `direct-x`）**：OpenAI 的 [`How enabling two settings tripled our scores on the ARC‑AGI‑3 benchmark`](../raw/2026-07-31/official-link-candidates/steipete-2082617409408762124-how-two-settings-tripled-our-arc-agi-3-scores.opencli.md) 比较通用 harness 与 Responses API。保留 reasoning、启用 compaction 后，公开任务集的 RHAE 得分从官方 harness 的 13.3% 升至 38.3%，输出 token 约减少 6 倍；文章还解释了滚动截断和丢弃私有推理如何破坏跨动作学习。这是本轮唯一的官方链接候选，来自 `steipete` 的 [原帖](https://x.com/steipete/status/2082617409408762124)，但仍是 OpenAI 自己的实验，不是独立 benchmark 复核。
- **科研 agent 的瓶颈转向验证与长期 stewardship（官方原文）**：OpenAI 的 [`Scientific computing in the age of agentic AI`](../raw/2026-07-31/rss-fulltext/openai-blog/openai-blog-scientific-computing-in-the-age-of-agentic-ai-df22037e3e.opencli.md) 回顾 8 个科研软件项目（5 个只用 Codex、3 个结合 Codex 与 Claude Code）。案例显示 agent 能加速迁移、维护、优化和 GPU 重写，但科学正确性仍需外部参照、可测验收目标、分阶段反馈和明确维护者；“最后一公里”与长期责任没有被自动化消除。
- **科研工具分发开始制度化（官方原文）**：[`ChatGPT for Academic Researchers`](../raw/2026-07-31/rss-fulltext/openai-blog/openai-blog-accelerating-scientific-discovery-with-chatgpt-for-academic-researcher-14fd05ad34.opencli.md) 宣布先向 10,000 名研究者开放，计划到 2027 年覆盖 100,000 名科学家、数学家和工程师，并提供 ChatGPT、ChatGPT Work、Codex、研究技能和连接器。原文强调机构资格、身份验证、默认不用于训练和研究者保持控制；参与规模、资格和成效仍应以实际申请与机构反馈复核。
- **物理 agent 把视频进度、工具编排和多机器人协作放进同一模型（官方 DeepMind 原文）**：[`Gemini Robotics ER 2`](../raw/2026-07-31/rss-fulltext/google-deepmind-blog/google-deepmind-blog-gemini-robotics-er-2-powering-robotics-with-video-understanding-task-o-06b8d0ad6f.extracted.md) 作为高层“机器人大脑”，接收连续视频并调用 VLA、导航等工具，支持任务进度分类、关键时刻定位和多机器人交接；文章报告进度分类 57.4%、关键时刻定位 91.3%、平均误差 0.96 秒，并称已通过 Gemini API、AI Studio 公开给开发者。指标和安全表现是官方评测，尚未有本地机器人、延迟、故障恢复或第三方复测证据。
- **基础设施的约束从“买到 GPU”转向“持续用对 GPU”（二手全文）**：Hugging Face 上的 [`GPU Management`](../raw/2026-07-31/rss-fulltext/huggingface-blog/huggingface-blog-gpu-management-why-idle-gpus-are-the-new-grounded-aircraft-f684c3a66a.opencli.md) 将 GPU 利用率、训练/推理/批处理的形状错配和持续调度视为下一阶段约束，并主张专用小模型与 GPU 编排互相补足。文章是作者团队的战略论述，不是生产集群审计；它与 OpenAI 的 routing、kernel、speculative decoding 和 KV cache 效率叙述构成同方向但非独立证实。
- **跨 harness 的共享工作区成为产品叙事（`direct-x` + README discovery）**：`rileybrown` 说 [Buzz iOS](https://x.com/rileybrown/status/2082871456875139403) 可在手机群聊中同时使用 Codex、Claude Code、Cursor 并让 agent 协作；另一条 [团队 agent 经验](https://x.com/rileybrown/status/2082906576147370164) 把权限、成员 onboarding、eval、模型、技能、连接、频道、内部文档、版本和 bug 维护列为真正成本。这是实践者的结构化 X 证据，未提供生产权限、审计、故障恢复或成本数据；[`different-ai/openwork`](../raw/2026-07-31/github-trending-readmes/different-ai__openwork.md) README 则给出跨 Codex、Claude Code、Cursor 的 MCP 连接复用和组织管理方式，同样需要安全审查。
- **输入文档可以成为提示注入的自传播载体（二手全文）**：Simon Willison 的 [`AI Worming through Word`](../raw/2026-07-31/rss-fulltext/simonwillison/simonwillison-ai-worming-through-word-f34faab803.extracted.md) 转述隐藏指令进入 Copilot for Word、被复制到生成文档并在下一次工作流再次触发的路径。它是二手安全分析，不等于 Microsoft 的正式修复公告；最小验证路径是隔离文档、权限和连接器后复现“隐藏指令复制—再次触发”，并检查文档清洗和下游工具边界。

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

OpenAI RSS 的 5 条一手文章全部完成正文归档：价格/速度、ARC‑AGI‑3 harness、学术研究者计划、GPT‑5.6 效率栈和科研软件 field report。效率文章进一步写到 routing、scheduling、kernel、speculative decoding、KV cache、延迟发现、工具输出默认 10,000 token 上限和 append-only history 以维持 prompt caching；这些是官方工程叙述，不能替代外部成本或性能审计。OpenAI News 列表只读到卡片索引，不能将其当成文章全文。

Codex `0.146.0` release body 可读，列出会话命名/固定、Agent Plugins manifests、workspace plugin publishing、分页与临时 fork、remote Code Mode、web search、executor skills、MCP 重连和代理/沙箱修复；`0.147.0-alpha.1/.2` 与 `0.146.0-alpha.9.x` 仅有标题或短内容，不能从版本号推断功能。Claude Code `v2.1.219` release body 可读，包含 Claude Opus 5 默认模型、1M context、sandbox network strict allowlist、`DirectoryAdded` hook 和 `mcp_server_errors`；`v2.1.220` 只有 “Bug fixes and reliability improvements”，因此本轮不为它补写功能。

### LLM / Frontier Models

GPT‑5.6 的核心信号是单位结果的成本、速度和上下文配置一起优化；ARC‑AGI‑3 则提醒评测 runner 会改变模型表现。Google DeepMind 的 Gemini Robotics ER 2 将视频进度理解、工具编排和多机器人协作推进到物理 agent，但数值仍是官方自报。`levelsio` 的 [indie hacker 与开发者角色讨论](https://x.com/levelsio/status/2082795824258359493) 为 `direct-x` 观点，不作为模型能力证据。

### AI Agent / Agentic Workflow

Buzz、OpenWork 和 OpenAI 科研案例都把 agent 从单会话工具移向共享工作区或长期项目：共享 skills/MCP/连接、成员与权限、研究执行和验证成为一组新控制面。`rileybrown` 的 [维护清单](https://x.com/rileybrown/status/2082906576147370164) 是实践者线索，OpenWork README 的 `search_capabilities`/`execute_capability` 与远程 OAuth 则需要凭据、越权、审计和策略绕过测试。

### AI Coding / Developer Tools

Codex `0.146.0` 和 Claude Code `v2.1.219` 显示线程、插件、MCP、沙箱网络、hook 和审计信息正在成为 coding agent 的运行时控制面。`mattpocockuk` 的 [代码审查观点](https://x.com/mattpocockuk/status/2082886149333258415) 认为 code review 能把“不要做什么”的负向指令变成可检查的正向任务；这是 `direct-x` 使用战术，不是评测结果。Simon Willison 的 [自定义 MCP 服务器记录](../raw/2026-07-31/rss-fulltext/simonwillison/simonwillison-adding-a-custom-mcp-server-to-claude-and-chatgpt-90749d7606.extracted.md) 说明在 Claude/ChatGPT 网页端接入 MCP 仍需多步配置，适合做安装复测，不等于默认可用。

### AI Governance / Public Legitimacy

本轮没有新增政府规则、监管决定或公共授权原文。学术研究者计划包含隐私、机构资格和研究者控制，Gemini Robotics ER 2 包含人体接近与安全指令评测，但都属于公司产品/研究叙述；Word 提示注入案例反而显示，治理需要落到文档输入隔离、连接器权限和事故响应。不能把公司安全声明升级为公共合法性已形成。

### AI Infrastructure / Open Source

OpenAI 效率文章把服务成本下降归因于负载均衡、kernel、speculative decoding、KV 管理和 harness；Hugging Face 的 LFM2.5 Encoders 文章则报告 230M/350M 编码器支持 8,192 token context、CPU 长文本处理约比 ModernBERT-base 快 3.7 倍，并适合路由、策略检查和 PII 检测。后者的 benchmark 和性能为项目方报告，需在目标 CPU/任务上复测。Trending 的 `speech-to-speech` README 提供可替换的 VAD→STT→LLM→TTS 组件链和 OpenAI Realtime 兼容 WebSocket，但默认代理无认证/限流，部署前必须加网关。

### Indie Hacking / Solo Founder

`levelsio` 的 [开发门槛与分发竞争观点](https://x.com/levelsio/status/2082437553030901814) 认为非技术创始人也能构建产品，竞争将更多转向分发和注意力；这是个人观察，不是市场中位数或收入数据。`mvanhorn/last30days-skill` 的 README 把跨 Reddit、X、YouTube、HN、Polymarket 和 Web 的 agent 汇总包装成研究产品，但它要求自带 key 或浏览器会话，来源评分和身份验证仍需逐站检查。

### Product / Growth / GTM

Buzz 的手机群聊叙事与 OpenWork 的跨工具连接复用，都把“分发上下文和协作入口”作为产品卖点；OpenAI 的 GPT‑5.6 降价则把高频工作流的单位成本作为 GTM 杠杆。两者都缺少留存、转化、权限事故和长期成本数据，不能直接推出市场规模。

### AI Systems / Automation

科研 field report 的结论最具体：agent 可以快速写代码和迁移，但必须由人定义验收目标、做数值/科学验证并承担长期维护。Ansible Trending README 以 agentless SSH 做配置管理、部署、网络自动化和多节点编排，适合作为传统自动化对照；它上榜只是 discovery signal。Word worm 与 OpenWork 的远程 `execute_capability` 共同说明输入、工具和连接器边界是自动化系统的安全核心。

### Forward Deployed Engineering / Enterprise AI Deployment

本轮没有新的客户嵌入工程、部署经济学或产品反馈闭环原始证据。OpenAI 的科研软件案例有“谁维护、怎样接入上游、如何长期 steward”的相邻信号，但它是科研软件场景，不能直接升级为 FDE 业务模型；FDE 方向保留为已检查、无新增。

### X/Twitter 推主主题摘要

以下按 [`twitter-topic-brief.json`](../raw/2026-07-31/twitter-topic-brief.json) 为每个有内容主题保留高分条目。所有 X 条目均为 `direct-x`，只证明 `twitterapi.io` 返回了该账号内容；重复路由不等于多份独立证据。

- **LLM / Frontier Models**：`OpenAI` 的 [GPT‑5.6 效率说明](https://x.com/OpenAI/status/2082577277246972300)（`direct-x`）、`OpenAI` 的 [价格调整](https://x.com/OpenAI/status/2082878156483219672)（`direct-x`）、`rileybrown` 的 [Buzz agent team](https://x.com/rileybrown/status/2082569013280796930)（`direct-x`）。前两条可由官方正文交叉读取，Buzz 仍是个人演示。
- **AI Agent / Agentic Workflow**：`rileybrown` 的 [Buzz 团队工作流](https://x.com/rileybrown/status/2082569013280796930)（`direct-x`）、`OpenAI` 的 [服务效率](https://x.com/OpenAI/status/2082577277246972300)（`direct-x`）、`steipete` 的 [ARC‑AGI‑3 链接](https://x.com/steipete/status/2082617409408762124)（`direct-x`）。ARC 链接已经升级为官方全文候选；其它内容仍需边界说明。
- **AI Coding / Developer Tools**：`OpenAI` 的 [GPT‑5.6 效率说明](https://x.com/OpenAI/status/2082577277246972300)（`direct-x`）、`rileybrown` 的 [手机端 Codex/Claude Code/Cursor](https://x.com/rileybrown/status/2082871456875139403)（`direct-x`）、`mattpocockuk` 的 [代码审查战术](https://x.com/mattpocockuk/status/2082886149333258415)（`direct-x`）。均不能替代安装或独立评测。
- **AI Governance / Public Legitimacy**：`OpenAI` 的 [效率发布](https://x.com/OpenAI/status/2082577277246972300)（`direct-x`）、[价格发布](https://x.com/OpenAI/status/2082878156483219672)（`direct-x`）和 [ARC‑AGI‑3 说明](https://x.com/OpenAI/status/2082616636989952217)（`direct-x`）是公司叙述，不是政策或监管证据；本轮无新增公共授权。
- **AI Infrastructure / Open Source**：`OpenAI` 的 [服务成本优化](https://x.com/OpenAI/status/2082577277246972300)（`direct-x`）与 `simonw` 的 [成本评论](https://x.com/simonw/status/2082641030093127768)（`direct-x`）；后者是推测性评论，不作为成本事实。
- **Indie Hacking / Solo Founder**：`levelsio` 的 [开发门槛观点](https://x.com/levelsio/status/2082437553030901814)（`direct-x`）与 [分发竞争观点](https://x.com/levelsio/status/2082396401095315571)（`direct-x`）；个人观察，不推导市场规模。
- **Product / Growth / GTM**：`levelsio` 的 [indie hacker 讨论](https://x.com/levelsio/status/2082795824258359493)（`direct-x`）、`rileybrown` 的 [Buzz agent team](https://x.com/rileybrown/status/2082569013280796930)（`direct-x`）和 [Buzz iOS](https://x.com/rileybrown/status/2082871456875139403)（`direct-x`）。没有留存、转化或组织采购证据。
- **AI Systems / Automation**：`rileybrown` 的 [团队 agent 维护清单](https://x.com/rileybrown/status/2082906576147370164)（`direct-x`）、`steipete` 的 [ARC‑AGI‑3 质疑/链接](https://x.com/steipete/status/2082617409408762124)（`direct-x`）、`cnyzgkc` 的 [上下文型助手观点](https://x.com/cnyzgkc/status/2082746826386714634)（`direct-x`）。前两条有原文或正文入口，最后一条只是个人产品观点。
- **Forward Deployed Engineering**：本轮摘要没有 FDE 主题条目；这是主题路由和去重边界，不是指定账号没有更新的证明。

### GitHub Trending 每日发现

本轮解析 10/10 repo-card、归档 10/10 README。以下每项把 Trending description 与 README 合成一段可读介绍；全部是 `secondary-source` discovery signal，不是官方发布、质量背书或采用率证明。

- [`huggingface/speech-to-speech`](https://github.com/huggingface/speech-to-speech)：面向本地或云端语音 agent 的模块化后端，把 VAD、STT、LLM、TTS 串成低延迟流水线，提供 OpenAI Realtime 兼容 WebSocket，并可接 vLLM、llama.cpp、MLX 等后端。README 给出 `pip install`、Realtime/TCP/Docker 和本地运行方式；LLM proxy 默认没有认证和限流，语音质量、延迟和生产规模需独立验证。归档：[`speech-to-speech README`](../raw/2026-07-31/github-trending-readmes/huggingface__speech-to-speech.md)。
- [`microsoft/AI-For-Beginners`](https://github.com/microsoft/AI-For-Beginners)：面向入门者的 12 周、24 课 AI 课程，包含神经网络、计算机视觉、自然语言、多智能体和多模态等 notebook/lab，并通过 GitHub Action 维护多语言版本。它解决的是教学入门问题，不是前沿 agent 工具；上榜只说明当天被发现。归档：[`AI-For-Beginners README`](../raw/2026-07-31/github-trending-readmes/microsoft__AI-For-Beginners.md)。
- [`paperswithbacktest/awesome-systematic-trading`](https://github.com/paperswithbacktest/awesome-systematic-trading)：量化研究与实盘资源索引，收集回测/实盘框架、交易 API、指标、风险、数据源、策略、书籍和课程。README 能确认它是目录而非执行系统，也没有 agent 审批或交易安全证据；金融使用者仍需单独验证数据、券商接口和策略风险。归档：[`awesome-systematic-trading README`](../raw/2026-07-31/github-trending-readmes/paperswithbacktest__awesome-systematic-trading.md)。
- [`different-ai/openwork`](https://github.com/different-ai/openwork)：开源桌面工作区，通过一个 OpenWork MCP 把 skills、plugins、MCP 连接、Google Workspace 和 Microsoft 365 能力复用到 Codex、Claude Code、Cursor 等 agent，并提供成员、能力发布和共享/个人连接管理。README 明确包含浏览器登录、远程 OAuth 和 `execute_capability`；凭据范围、权限绕过、审计和服务可用性必须先做安全评估。归档：[`OpenWork README`](../raw/2026-07-31/github-trending-readmes/different-ai__openwork.md)。
- [`WhiskeySockets/Baileys`](https://github.com/WhiskeySockets/Baileys)：通过 WebSocket 直接连接 WhatsApp Web 的 TypeScript 库，支持多设备、QR/配对码登录、事件处理、媒体流和会话存储。README 标出 7.0 breaking change、非官方关联和 WhatsApp 服务条款边界；账号登录、隐私、封禁与合规风险不能被“上榜”掩盖。归档：[`Baileys README`](../raw/2026-07-31/github-trending-readmes/WhiskeySockets__Baileys.md)。
- [`pascalorg/editor`](https://github.com/pascalorg/editor)：基于 React Three Fiber 与 WebGPU 的 3D 建筑编辑器，把 core/viewer/editor/nodes 拆成可发布包，用 Zustand 场景状态、节点注册表、空间查询、事件总线和统一 plugin manifest 支持扩展。它适合研究浏览器端 3D 编辑器和插件边界，但 README 没有性能、安全或商业采用数据。归档：[`Pascal Editor README`](../raw/2026-07-31/github-trending-readmes/pascalorg__editor.md)。
- [`mvanhorn/last30days-skill`](https://github.com/mvanhorn/last30days-skill)：让 agent 并行研究 Reddit、X、YouTube、HN、Polymarket、GitHub 等来源，再按互动信号打分并生成摘要，支持 Codex、Claude Code、Cursor 等多个宿主。README 也要求自带 API key 或浏览器会话，且跨站身份、来源真实性、Polymarket/X 访问和隐私边界需要逐项核验；它是研究工具候选而非可信情报证明。归档：[`last30days README`](../raw/2026-07-31/github-trending-readmes/mvanhorn__last30days-skill.md)。
- [`dotnet/aspnetcore`](https://github.com/dotnet/aspnetcore)：跨平台 .NET Web、IoT 和移动后端框架，模块化组件支持 Windows、macOS、Linux、云端或本地部署。README 可确认安装/贡献/安全报告入口，但本轮没有新的 release 证据；上榜只是一条通用开发基础设施发现线索。归档：[`ASP.NET Core README`](../raw/2026-07-31/github-trending-readmes/dotnet__aspnetcore.md)。
- [`microsoft/PowerToys`](https://github.com/microsoft/PowerToys)：Windows 生产力和定制工具集合，包含窗口布局、文本提取、PowerToys Run、文件工具、键盘和屏幕工具等 30 多个实用程序。它解决的是桌面效率问题，与 AI 主题的直接关系有限；需按具体版本和权限验证，不把 Trending 当作产品更新。归档：[`PowerToys README`](../raw/2026-07-31/github-trending-readmes/microsoft__PowerToys.md)。
- [`ansible/ansible`](https://github.com/ansible/ansible)：无需在远端安装 agent、通过 SSH 做配置管理、应用部署、云资源、网络自动化和多节点编排的平台；README 强调简单 YAML、并行执行、安全审计和可重写内容。它是传统自动化的成熟参照，今天值得记录在于与 agent 工具形成执行层对照，但没有本轮新发布或采用率证据。归档：[`Ansible README`](../raw/2026-07-31/github-trending-readmes/ansible__ansible.md)。

## 3. 来源证据表

| 来源组 | 本轮结果 | 代表证据与边界 |
| --- | --- | --- |
| RSS/Atom | 32 源，31 成功；54 条匹配/一手全文 54/54 可读 | 全部状态见 [`rss-items.json`](../raw/2026-07-31/rss-items.json)；`nabeel-qureshi` XML 解析失败。 |
| GitHub release | 7/7 Atom 成功；一手全文 10 条中 5 条 `ok`、5 条 `limited` | Codex/Claude Code release 归档见 [`github-release-fulltext/`](../raw/2026-07-31/github-release-fulltext/)，REST API 为 `skipped`。 |
| GitHub Trending | 10/10 repo-card；10/10 README | [`github-trending.json`](../raw/2026-07-31/github-trending.json) 与 [`github-trending-readmes/`](../raw/2026-07-31/github-trending-readmes/)，统一 `secondary-source`。 |
| 官方页面 | 4/4 成功 | OpenAI News challenge 后使用 `opencli-read`，只读到列表卡片；详情以 RSS 全文为准。 |
| X/Twitter | 27 个账号均返回；152 条 `direct-x` | 结构化结果见 [`twitterapi-io-results.json`](../raw/2026-07-31/twitterapi-io-results.json)；主题聚合见 [`twitter-topic-brief.json`](../raw/2026-07-31/twitter-topic-brief.json)。 |

## 4. X/Twitter 覆盖说明

- 本轮 `twitterapi.io` 状态为 `ok`：27/27 账号请求成功，保留 152 条 `direct-x`。`karpathy`、`AnthropicAI`、`kloss_xyz`、`frxiaobei`、`oviswang`、`pangyusio` 等账号本轮 raw 有返回但主题过滤后为 0；`rryssf_`、`Yangyixxxx`、`zhaogua61654931`、`lidang` 等返回 0 条原始结果。这些是接口、时间窗和关键词覆盖边界，不是“账号没有更新”的证明。
- 接口默认 `includeReplies=false`，使用账号近期结果，再按窗口、主题关键词和去重保留；本日报不声称完整覆盖指定账号过去 24 小时全部原帖。所有 X 内容都保留 `direct-x` 标签；转发、短句、个人体验、价格帖和市场叙事只证明账号发布了该说法。
- `official-link-candidates.json` 唯一候选是 `steipete` 指向 OpenAI ARC‑AGI‑3 的链接；该候选已在“今日高信号”同时给出 tweet 和 OpenCLI 归档正文，因此不是未处理候选。
- 本轮未使用 Exa MCP、登录态 X/Twitter 浏览器、账号密码、官方 X API，也未使用发帖、点赞、关注、私信或其它 action endpoint。Trend 阶段不会重跑 `twitterapi.io`。

## 5. 候选审计与处置

初稿后由 [`candidate-audit.py`](../scripts/candidate-audit.py) 根据当天 raw 生成稳定 candidate id；最终 covered/missed 计数以 [`2026-07-31-candidate-audit.json`](../reviews/2026-07-31-candidate-audit.json) 为准。未进入“今日高信号”的 missed 多为重复路由、转发、短句、历史窗口或只有结构化 X metadata 的发现线索；对高分 direct-x/RSS 的处理边界已在“今日高信号”“主题摘要”或“不确定性与待验证项”中说明。

<!-- dsi-candidate-audit: covered=16 missed=91 -->

## 6. 不确定性与待验证项

- `nabeel-qureshi` feed 仍为 XML parse failed（line 1, column 54），下一轮应重试同一 feed；不能把连续失败解释成无更新。
- OpenAI Codex `0.147.0-alpha.1/.2`、`0.146.0-alpha.9.x` 与 Claude Code `v2.1.220` release body 为 `limited`；最小验证路径是打开对应 release 页面补正文，不能从版本号或“Bug fixes”推断功能。
- OpenAI News 只有 510 字符的列表卡片；本轮已优先使用 OpenAI RSS 全文。学术项目资格、隐私、免费额度、GPT‑5.6 价格和 Fast mode 仍应以产品/开发者文档和实际账户为准。
- ARC‑AGI‑3 的 13.3%→38.3%、6 倍 token 下降、Gemini Robotics ER 2 的 57.4%/91.3% 指标、OpenAI 的 serving cost -20% 和 token generation +15% 都是发布方或项目方报告，尚未独立复测；评测必须固定模型、API 设置、harness、提示、随机种子和成本口径。
- Word worm 的完整影响范围、Microsoft 缓解状态、OpenWork 的远程能力与凭据边界、`speech-to-speech` 的 proxy 防护、Baileys 的账号合规和 `last30days-skill` 的跨站授权都需要隔离环境与最小权限复核。
- Trending 的十个 README 全部归档成功，但热度只表示当天发现；涉及 agent 执行、MCP/凭据、交易、浏览器、隐私或深伪的项目不能只凭上榜或 README 自述作采用结论。
- `signals.json`、`report-reading-list.json`、`run-summary.json` 与 HTML/dashboard 是派生控制物；原始 JSON、正文/README 归档和 source-health 才是证据真相源。

## 7. 当天产物

- 运行摘要：[`run-summary.json`](../raw/2026-07-31/run-summary.json)
- 报告阅读清单：[`report-reading-list.json`](../raw/2026-07-31/report-reading-list.json)
- 信号派生：[`signals.json`](../raw/2026-07-31/signals.json)
- 原始状态清单：[`manifest.json`](../raw/2026-07-31/manifest.json)
- 候选审计：[`2026-07-31-candidate-audit.json`](../reviews/2026-07-31-candidate-audit.json) 与 [`2026-07-31-candidate-audit.md`](../reviews/2026-07-31-candidate-audit.md)
- 主题摘要：[`twitter-topic-brief.json`](../raw/2026-07-31/twitter-topic-brief.json)
- Trend report：在趋势阶段完成后写入 `trend/reports/2026-07-31-trend-report.md`。

本 Markdown 是日报内容真相源；严格校验通过后才派生日期化 HTML、索引 JSON 和 `docs/index.html`。
