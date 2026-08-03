# 2026-08-04 每日源情报

## 直接答案

按北京时间 2026-08-04 的日历窗口，本轮确认了 4 个可进入信号清单的条目：OpenAI Codex 的 3 个 alpha release 只确认版本条目存在，正文均为 `limited`；Simon Willison 对 David Crawshaw 自动更新提示词的转述有可读正文。另有 4 个 GitHub Trending README 被纳入正文阅读清单，作为 `secondary-source` 发现线索而不是发布或质量证明。

今天最值得保留的观察是：

1. **实时智能体的瓶颈正在从模型响应转向全链路状态管理。** OpenAI 对 GPT-Live 的工程文章（本窗口之前发布）描述了全双工语音、异步深度推理、上下文压缩和会话实例切换；这是厂商一手背景，不计作今天的新发布，但为长期观察实时 agent 系统的状态迁移和恢复边界提供了可读证据。
2. **本轮发现流同时出现了“把复杂能力压缩到本地”的两条路线。** `airllm` 以专家逐层流式加载降低大模型显存门槛，`antirez/ds4` 则把少数模型、KV 状态、工具调用、HTTP 服务和编码 agent 组合成面向本地硬件的窄型推理引擎；两者都只有 README/Trending 证据，性能、兼容性和安全边界需要固定环境复测。
3. **共享记忆与工具治理开始成为团队级产品形态。** `TencentCloud/TencentDB-Agent-Memory` 把对话记忆、技能、文档知识图谱和代码图谱做成可共享资产，并提供团队 ACL；`esengine/DeepSeek-Reasonix` 把模型、工具、插件和上下文维护写入配置驱动的单一二进制。它们值得跟踪，但不能从上榜或 README 自述推断生产采用、权限正确性或长期可靠性。
4. **本轮没有新的 X/Twitter 直接证据。** `twitterapi.io` 处理的 27 个账号均返回 `status=ok`，但每个账号在本次 API、时间窗和保留规则下都是 0 条；这只是覆盖边界，不是账号没有发帖的证明。

## 0. 采集范围

- 运行日为北京时间 **2026-08-04**。原始状态见 [`manifest.json`](../raw/2026-08-04/manifest.json)，派生信号见 [`signals.json`](../raw/2026-08-04/signals.json)，正文阅读路由见 [`report-reading-list.json`](../raw/2026-08-04/report-reading-list.json)，流程索引见 [`run-summary.json`](../raw/2026-08-04/run-summary.json)。`signals.json` 共 8 条，其中 4 条发布时间在当天窗口内，4 条 Trending 项目发布时间未知；原始归档仍是证据真相源。
- RSS/Atom：32 个源中 **31 个成功、1 个失败**；失败源为 `nabeel-qureshi`。54 条命中关注方向或一手重点源的条目全部尝试正文，**54/54 为 `fulltext_status=ok`**；多数条目的发布时间早于当天，不能因采集到而升级成当天发布。
- GitHub release：7/7 个 Atom 源成功，REST API 为 `skipped`。10 条一手重点 release 均尝试正文，**4 条可读、6 条 `limited`**；其中 Codex `rust-v0.147.0-alpha.6`、`rust-v0.147.0-alpha.5`、`0.147.0-alpha.1.2` 落在当天窗口，但正文受限，只能确认版本存在，不能从版本号推断功能。
- GitHub Trending：每日页面解析 **10/10 个 repo-card、10/10 README**。Trending description 与 README 均保存在 [`github-trending.json`](../raw/2026-08-04/github-trending.json) 和 [`github-trending-readmes/`](../raw/2026-08-04/github-trending-readmes/)。证据等级统一为 `secondary-source`，只表示当天发现线索，不表示质量、采用率或官方支持。
- 官方页面：4/4 个配置源成功；OpenAI News 列表在 `curl` challenge 后使用 `opencli-read` 归档，详细判断仍以 RSS/Atom 正文为准。官方页面归档见 [`official-page-text/`](../raw/2026-08-04/official-page-text/)。
- X/Twitter：`twitterapi.io` 处理 27 个启用账号，27/27 请求返回 `status=ok`，保留 **0 条 `direct-x`**；`official-link-candidates.json` 为 `ok`、候选数为 0，主题摘要的 `tweet_count=0`。没有使用 Exa MCP、登录态 X/Twitter 浏览器、账号密码、官方 X API 或任何写操作。

## 1. 今日高信号

- **Codex alpha 版本线继续推进，但正文不可读**：`openai/codex` 的 `rust-v0.147.0-alpha.6`、`rust-v0.147.0-alpha.5` 与 `0.147.0-alpha.1.2` 在北京时间当天发布窗口内出现。Atom 内容被归档为 `limited`，所以今天的确定判断只有“官方 release 条目存在”，不能写成新增功能、修复或行为变化。证据：[`alpha.6 Atom`](../raw/2026-08-04/github-release-fulltext/openai-codex/openai-codex-rust-v0.147.0-alpha.6-34ee3c44c2.atom.md)、[`alpha.5 Atom`](../raw/2026-08-04/github-release-fulltext/openai-codex/openai-codex-rust-v0.147.0-alpha.5-6e97a70003.atom.md)、[`alpha.1.2 Atom`](../raw/2026-08-04/github-release-fulltext/openai-codex/openai-codex-0.147.0-alpha.1.2-ddb3dcd4d7.atom.md)；等级 `official-source`，正文边界 `limited`。
- **可重复的“自动更新并验证软件”提示词**：Simon Willison 归档 David Crawshaw 的提示词，要求定时拉取上游、在本地变更之上 rebase、检查软件是否按预期工作并替换当前版本。原文是可读的二手转述，能说明一种把依赖更新、回归检查和替换动作串起来的工作流想法，但不能证明已有无人值守生产部署。证据：[`Quoting David Crawshaw's prompt`](../raw/2026-08-04/rss-fulltext/simonwillison/simonwillison-quoting-david-crawshaw-s-prompt-765bf45633.extracted.md)；等级 `secondary-source`。

以下十个项目是本轮 GitHub Trending **发现信号**，不是“今日发布”或质量背书。每段把 Trending description 与 README 合并说明，并保留必要的验证边界：

- **`lyogavin/airllm`：低显存大模型推理。** README 说明它通过按专家逐层流式加载，让 70B 模型在单张 4GB GPU 上运行，并给出 405B、DeepSeek-V3 和 Kimi K3 的更低显存示例；Quickstart 以 Python 包和 Hugging Face 模型为入口。它解决的是模型权重无法整体放入显存时的本地推理门槛，今天上榜说明“用内存/磁盘换显存”的工具仍有发现热度；吞吐、首 token 延迟、上下文长度、显存峰值和特定模型兼容性必须在固定 GPU、CUDA 与依赖版本下复测。证据：[`README`](../raw/2026-08-04/github-trending-readmes/lyogavin__airllm.md)；等级 `secondary-source`。
- **`zhaoxuya520/reverse-skill`：面向授权安全研究的技能路由包。** README 将 APK、ELF、前端 JS、PCAP、CTF 和渗透目标按场景路由到 jadx、Frida、IDA、BurpSuite 等工具，要求先建立授权范围、网络配置和证据链，再执行具体技能。它解决 agent 在逆向任务中选错方法、工具分散和经验不复用的问题；由于涉及凭据、样本和扫描，必须在明确授权、隔离网络、最小权限和人工复核下验证，不能把自动路由等同于安全。证据：[`README`](../raw/2026-08-04/github-trending-readmes/zhaoxuya520__reverse-skill.md)；等级 `secondary-source`。
- **`firecrawl/pdf-inspector`：本地 PDF 分类与结构化抽取。** 这是 Rust 库，先判断 PDF 是文本、扫描、图像或混合类型，再按坐标和多栏顺序提取文本并转为 Markdown，同时提供 Python、Node.js 和浏览器 WebAssembly 绑定；README 还给出本地基准和表格检测实现。它解决的是研究报告、发票和法律文档在 OCR 前的路由与结构保真问题；README 的 200 文档基准需按同一 corpus、版本和硬件复测，扫描件仍可能需要 OCR，不能把自报分数当成普遍优势。证据：[`README`](../raw/2026-08-04/github-trending-readmes/firecrawl__pdf-inspector.md)；等级 `secondary-source`。
- **`esengine/DeepSeek-Reasonix`：围绕前缀缓存的终端编码 agent。** README 把 provider、模型、工具和插件写入 `reasonix.toml`，用单一静态 Go 二进制运行，可在 executor 与 planner 间组合多模型，外部工具通过 stdio JSON-RPC/MCP 兼容接口接入；它还会在压缩前裁剪过期工具输出并维护稳定环境摘要。它解决的是把模型切换、插件和长会话上下文维护做成可配置本地工作台的问题；社区项目的缓存收益、工具权限、插件供应链和恢复行为仍需源码与隔离运行验证。证据：[`README`](../raw/2026-08-04/github-trending-readmes/esengine__DeepSeek-Reasonix.md)；等级 `secondary-source`。
- **`TencentCloud/TencentDB-Agent-Memory`：团队级 agent 记忆中枢。** README 将对话、文档和代码转换为 Chat Memory、Skill、LLM-Wiki、Code-Graph 四类可复用资产，安装时启动 `memory-core`、`memory-hub` 和 `proxy` 三个服务，并在面板中管理团队、版本、可见性和 User/Role/Agent ACL。它把“下一次少重复解释”扩展为可审查、可共享和跨框架迁移的团队资产；Beta 状态、默认端口、LLM 参数、数据迁移和权限隔离需要实际部署测试，不能仅凭 Trending 星数判断成熟度。证据：[`README`](../raw/2026-08-04/github-trending-readmes/TencentCloud__TencentDB-Agent-Memory.md)；等级 `secondary-source`。
- **`microsoft/AI-For-Beginners`：带实验和多语言维护的 AI 入门课程。** README 提供 12 周、24 节课、测验和实验，覆盖符号 AI、神经网络、视觉、文本、多 agent 与伦理，并通过 GitHub Action 持续生成 50 多种语言翻译。它解决的是从概念到可运行练习的系统入门和培训问题；课程版本、框架依赖和实验可复现性需按当前提交检查，不能把教学仓库的热度解释为前沿能力或真实采用。证据：[`README`](../raw/2026-08-04/github-trending-readmes/microsoft__AI-For-Beginners.md)；等级 `secondary-source`。
- **`microsoft/generative-ai-for-beginners`：面向应用构建的生成式 AI 课程。** 21 节课覆盖模型选择、提示、RAG、函数调用、聊天、向量搜索、图像、应用安全、生命周期、agent 和微调，并提供 Python/TypeScript 示例和多语言版本。它为初学者提供从 API 调用到应用交付的学习路径；示例所依赖的模型、API 和云服务会变动，不能直接当成生产架构或安全评估。证据：[`README`](../raw/2026-08-04/github-trending-readmes/microsoft__generative-ai-for-beginners.md)；等级 `secondary-source`。
- **`donnemartin/system-design-primer`：大规模系统设计学习与面试资料库。** README 把可扩展性、延迟/吞吐、可用性/一致性、缓存、数据库和消息系统等主题组织成教程、练习题、样例解答和 Anki 卡片，目标是帮助读者设计大规模系统并准备系统设计面试。它是长期维护的知识索引而不是 agent 产品；内容与架构取舍适合学习起点，但示例、云服务行为和面试标准需结合当前环境验证。证据：[`README`](../raw/2026-08-04/github-trending-readmes/donnemartin__system-design-primer.md)；等级 `secondary-source`。
- **`antirez/ds4`：面向特定模型和本地硬件的原生推理引擎。** README 将 DeepSeek V4 Flash、GLM 5.2 及部分 DeepSeek V4 PRO 支持、模型加载、提示渲染、工具调用、KV 状态、HTTP 服务和编码 agent 组合起来，后端覆盖 Metal、CUDA、ROCm，也提供 SSD 流式和多 GPU 运行路径。它解决的是在高端 Mac、DGX Spark 或多卡机器上以窄模型集合运行本地 agent；项目自称 beta 且快速变化，硬件要求、量化质量、工具调用可靠性和 120 tokens/s 等性能数字必须按其 QA 矩阵复测。证据：[`README`](../raw/2026-08-04/github-trending-readmes/antirez__ds4.md)；等级 `secondary-source`。
- **`shiyu-coder/Kronos`：面向金融 K 线的基础模型。** README 介绍一种先把 OHLCV 连续数据量化成分层离散 token、再用 decoder-only Transformer 预训练的两阶段方案，提供不同规模模型、Hugging Face 权重和 BTC/USDT 预测 demo。它解决的是把金融市场序列作为专门“语言”建模并用于预测的研究问题；金融数据噪声、回测泄漏、交易成本、漂移和监管责任都未由 Trending 或 README 证明，不能据此给出投资建议或执行交易。证据：[`README`](../raw/2026-08-04/github-trending-readmes/shiyu-coder__Kronos.md)；等级 `secondary-source`。

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

OpenAI feed 的五条一手文章均完成正文归档，其中《How we built a realtime system for responsive voice AI in six months》在 2026-08-03 发布，早于本日窗口。文章描述 GPT-Live 的全双工语音、独立媒体快路径、异步 frontier model/tool delegation、状态化推理、上下文压缩时的实例热切换、WARP/Instant Connect 以及生产 shadow test；这些是 OpenAI 自述的系统设计背景，不应写成 2026-08-04 新发布。正文见 [`GPT-Live 工程文章`](../raw/2026-08-04/rss-fulltext/openai-blog/openai-blog-how-we-built-a-realtime-system-for-responsive-voice-ai-in-six-months-d04cc35bd3.opencli.md)。

Codex release Atom 的 3 个当天条目均为 `limited`，另外两条旧 alpha 也受限；Claude Code `v2.1.220` 的 release body 同样 `limited`，`v2.1.216`–`v2.1.219` 可读但早于本日。版本号或 “Bug fixes and reliability improvements” 不能支撑功能判断；完整状态见 [`github-items.json`](../raw/2026-08-04/github-items.json) 与 [`github-release-fulltext/`](../raw/2026-08-04/github-release-fulltext/)。

### LLM / 前沿模型

本轮没有可读的当天模型发布正文。AirLLM 的专家流式加载、DeepSeek-Reasonix 的前缀缓存维护和 `ds4` 的特定模型本地推理属于 Trending/README 发现线索；需要固定硬件、模型、上下文和量化配置复测，不能把 README 的显存或吞吐数字升级为基准结论。

### AI Agent / 智能体工作流

`TencentDB-Agent-Memory` 把记忆、技能、文档知识图谱和代码图谱做成团队资产，`DeepSeek-Reasonix` 把 provider、规划/执行模型、工具和插件写入配置文件。两者共同指向“agent 工作流的可复用状态和工具边界”成为独立基础设施；权限、凭据代理、版本迁移、审计和失败恢复仍需源码与隔离部署验证。

### AI Coding / 开发者工具

当天 Codex alpha 只给出有限 release 证据，不能推断功能。Simon Willison 转述的 Crawshaw 提示词则展示了一个可重复的更新—rebase—测试—替换循环；它更像自动化协议的想法，尚无运行日志、回滚策略或生产安全证据。DeepSeek-Reasonix 的终端、桌面和 VS Code 入口是发现型补充，不能与官方编码工具能力直接比较。

### AI Governance / 公共合法性

本轮没有新的政府规则、监管决定或公共授权原文。`reverse-skill` README 把授权范围、网络配置、证据链和“目标 ACT 前置检查”写入安全研究路由，说明 agent 工具链开始显式声明权限门槛；这只是项目方自述，不替代安全评估或法律授权。

### AI Infrastructure / Open Source

`pdf-inspector` 以本地 Rust 解析、类型分类、多栏顺序和表格结构处理 PDF；AirLLM、`ds4` 则分别以专家流式加载和原生窄型引擎降低本地推理资源门槛。共同方向是把模型/文档基础设施的成本与延迟控制下沉到本地，但 benchmark、硬件支持和上游模型变化都必须独立复测。

### Indie Hacking / Solo Founder

当天没有新的独立开发者原始文章或 `direct-x`。课程、学习资料和 Trending star 增长不能被解释成收入、留存或市场需求信号。

### Product / Growth / GTM

当天没有可验证的产品发布、客户采用或转化数据。`TencentDB-Agent-Memory` 的团队面板和 `DeepSeek-Reasonix` 的多入口分发可作为产品化形态观察，但没有定价、留存、部署规模或客户证据。

### AI Systems / Automation

本轮的系统型线索集中在三个边界：GPT-Live 背景中的实时媒体路径与异步推理隔离、DeepSeek-Reasonix 的插件/缓存/压缩策略、TencentDB Agent Memory 的服务拆分与 ACL。下一步应验证状态迁移、工具调用隔离、凭据代理、长任务恢复和审计日志，而不是只看安装是否成功。

### Forward Deployed Engineering / Enterprise AI Deployment

当天没有新的客户嵌入工程、数据整合瓶颈或产品反馈闭环原始材料。FDE feed 的旧条目已完成采集和正文归档，但不属于当天新增；本轮不把它们写成新趋势判断。

### X/Twitter 推主主题摘要

[`twitter-topic-brief.json`](../raw/2026-08-04/twitter-topic-brief.json) 状态为 `ok`，27 个账号均成功返回，但 `tweet_count=0`，没有可按主题选取的推文。因此本节没有 tweet 链接；这表示本次 API、时间窗和保留过滤没有输出，不表示账号没有更新。没有 `direct-x` 或 X 链接候选可升级为今日判断。

### GitHub Trending 每日发现

本轮解析 10/10 repo-card、归档 10/10 README。上文十段介绍已把 Trending description 与 README 合并，证据等级统一为 `secondary-source`；上榜只表示当天发现，不表示质量、采用率、官方支持或长期趋势。涉及 agent 执行、MCP/插件、凭据、金融预测、网络访问或安全研究的项目，必须在授权、隔离环境和可回滚条件下验证。

## 3. 来源证据表

| 来源组 | 本轮结果 | 代表证据与边界 |
| --- | --- | --- |
| RSS/Atom | 32 源，31 成功、1 失败；54 条命中/一手正文 54/54 可读 | [`rss-items.json`](../raw/2026-08-04/rss-items.json)；`nabeel-qureshi` 解析失败。 |
| GitHub release | 7/7 Atom 成功；一手正文 10 条中 4 条 `ok`、6 条 `limited` | [`github-items.json`](../raw/2026-08-04/github-items.json)；REST API 为 `skipped`。 |
| GitHub Trending | 10/10 repo-card；10/10 README | [`github-trending.json`](../raw/2026-08-04/github-trending.json) 与 [`github-trending-readmes/`](../raw/2026-08-04/github-trending-readmes/)，统一 `secondary-source`。 |
| 官方页面 | 4/4 成功；OpenAI News fallback 使用 `opencli-read` | [`official-pages.json`](../raw/2026-08-04/official-pages.json) 与 [`official-page-text/`](../raw/2026-08-04/official-page-text/)。 |
| X/Twitter | 27/27 请求成功；0 条保留 `direct-x` | [`twitterapi-io-results.json`](../raw/2026-08-04/twitterapi-io-results.json)、[`twitter-topic-brief.json`](../raw/2026-08-04/twitter-topic-brief.json)。 |

## 4. X/Twitter 覆盖说明

- `twitterapi.io` 状态为 `ok`，27 个账号均返回成功，但所有账号 `raw_count=0`、`kept_count=0`。这是 API 结果、过去 36 小时窗口和保留过滤共同形成的覆盖边界，不是“账号没有更新”的证明。
- `official-link-candidates.json` 为 `ok`、候选数 0；没有可升级为 `official-source/direct-x` 组合证据的链接。本轮没有使用 Exa MCP、登录态 X/Twitter 浏览器、账号密码、官方 X API、发帖、点赞、关注、私信或其它 action endpoint。
- Trend 阶段不会重跑 `twitterapi.io`；任何未来补抓都必须继续标为 `direct-x`，并单独归档原始响应和覆盖失败原因。

## 5. 候选审计与处置

初稿后运行 [`candidate-audit.py`](../scripts/candidate-audit.py) 生成 JSON 与 Markdown 审计。审计会把当天 raw 中仍可见但属于旧日期、已见 URL、重复主题路由或发现型 Trending 的候选列出；报告只把当天窗口内的 3 个受限 Codex release 和 1 篇可读 Simon Willison 转述提升为信号，其余按日期窗口、`state/seen.json`、受限正文或 `secondary-source` 边界解释。最终计数以 [`2026-08-04-candidate-audit.json`](../reviews/2026-08-04-candidate-audit.json) 为准。

<!-- dsi-candidate-audit: covered=2 missed=18 -->

## 6. 不确定性与待验证项

- `nabeel-qureshi` feed 仍然 XML 解析失败；下一轮应重试同一 feed，不能解释成无更新。
- 54 条 RSS 命中正文虽然全部 `ok`，但大多数发布时间早于北京时间 2026-08-04；当天信号以 `signals.json` 的 4 条 inside 为准，不能把滚动抓取的旧文章当成今日发布。
- Codex `rust-v0.147.0-alpha.6`、`rust-v0.147.0-alpha.5`、`0.147.0-alpha.1.2` 与 Claude Code `v2.1.220` 的 release body 为 `limited`；最小验证路径是打开对应 release 页面补正文，不能从版本号或短摘要推断功能。
- OpenAI GPT-Live 工程文章中的全双工、上下文压缩、shadow test、WARP 和性能数字来自厂商自述；需要公开实现、协议草案、完整实验记录或独立复测后才能判断外部可迁移性。
- Trending 十个 README 全部归档，但热度只表示当天发现；`airllm`/`ds4` 的硬件性能、`pdf-inspector` 的 benchmark、`Kronos` 的金融预测和安全研究路由都不能只凭 README 作采用、准确性或安全结论。
- `twitterapi.io` 0 条保留结果未覆盖完整账号时间线；没有 direct-X 证据，不能把空结果写成账号无更新。
- [`signals.json`](../raw/2026-08-04/signals.json)、[`report-reading-list.json`](../raw/2026-08-04/report-reading-list.json)、[`run-summary.json`](../raw/2026-08-04/run-summary.json) 与 HTML/dashboard 是派生控制物；raw JSON、正文/README 归档和 [`source-health.json`](../state/source-health.json) 才是证据真相源。中文阅读翻译阶段已退休，本轮不生成 `translations/` 输出。

## 7. 当天产物

- 原始状态清单：[`manifest.json`](../raw/2026-08-04/manifest.json)
- 信号派生：[`signals.json`](../raw/2026-08-04/signals.json)
- 报告阅读清单：[`report-reading-list.json`](../raw/2026-08-04/report-reading-list.json)
- 流程摘要：[`run-summary.json`](../raw/2026-08-04/run-summary.json)
- 候选审计：[`2026-08-04-candidate-audit.json`](../reviews/2026-08-04-candidate-audit.json) 与 [`2026-08-04-candidate-audit.md`](../reviews/2026-08-04-candidate-audit.md)
- 主题摘要：[`twitter-topic-brief.json`](../raw/2026-08-04/twitter-topic-brief.json)
- 趋势报告：[`2026-08-04-trend-report.md`](../trend/reports/2026-08-04-trend-report.md)；9 个 enabled trend 的 marker 和专题文件已由趋势阶段完成。

## 边界与验证

- 已确认：稳定采集、`twitterapi.io` 只读采集、官方链接候选、主题摘要、`update-state.py` 和 `dsi.py prepare` 均以运行日期 2026-08-04 完成；原始文件位于 `raw/2026-08-04/`。
- 待完成的闭环验证：初稿后需运行候选审计、严格日报校验和 bundle；随后为所有 enabled trend 建立唯一 marker，执行 Phase 1、Phase 2、`run-trend-stage.py --check` 与 `dsi.py check`。趋势正文与报告尚未在本初稿阶段生成。
- 运行时可能变化：源正文、Trending 排名、GitHub release、`twitterapi.io` 覆盖、远端 `origin/main` 和 Gmail 认证状态都只以本次命令输出和后续独立回读为准。
