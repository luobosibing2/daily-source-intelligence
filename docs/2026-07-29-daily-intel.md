# 2026-07-29 每日源情报

## 直接答案

今天最值得跟进的是：模型已经进入科学计算、密码分析和企业部署等真实工作流，但验证、长期维护和治理仍是主要瓶颈。

1. OpenAI 的科学计算现场报告归档了 8 个 agent 辅助项目：研究人员从实现者转向目标定义、验收与长期维护者；代理能快速完成迁移和优化，却不能可靠判断科学正确性。
2. Anthropic 报告 Claude Mythos Preview 改进了 HAWK 和七轮 AES 的攻击，但明确表示当前不影响生产系统。这个信号说明“发现能力”在前移，不能写成现有加密系统已被攻破。
3. Anthropic 的公开权重立场、Microsoft 的 Agent Governance Toolkit 和 FDE 定价分析共同指向同一控制面：模型能力之外，芯片、身份、沙箱、审计、部署成本和续约责任正在成为产品边界。
4. OpenAI Codex `rust-v0.146.0-alpha.15` 确认有新 release，但 Atom 正文为 `limited`；Claude Code `v2.1.219` 的 release body 可读、`v2.1.220` 只有“Bug fixes and reliability improvements”。版本存在不等于今天能确认具体功能。

## 0. 采集范围

- 运行日：北京时间 2026-07-29；原始入口和窗口见 [`manifest.json`](../raw/2026-07-29/manifest.json)，派生阅读清单见 [`report-reading-list.json`](../raw/2026-07-29/report-reading-list.json)。
- RSS/Atom：32 个源中 31 个成功、1 个失败；共 155 条条目，56 条命中关注方向或一手重点源并尝试全文，56/56 归档成功。`nabeel-qureshi` 因 feed XML 解析错误失败，不能解释为该源没有更新。
- GitHub release：7/7 个 Atom 源成功。OpenAI Codex 的 5 条 release 与 Claude Code 的 1 条 release 属于一手重点源；10 条一手 release 正文中 4 条可读、6 条 `limited`。本轮 GitHub REST API 为 `skipped`，Atom 是证据来源。
- GitHub Trending：1 个每日页面成功解析 10 个 repo-card，10/10 README 归档成功；上榜是 `secondary-source` 发现信号，不是质量、采用率或安全背书。
- 官方页面：4/4 成功；OpenAI News 页面因 `curl` 返回 challenge/有限内容，使用 `opencli-read` 归档，其余页面抓到公开页面内容或列表。
- X/Twitter：`twitterapi.io` 处理 27 个账号，27/27 返回成功，保留 128 条 `direct-x`；主题摘要覆盖 8 个有内容主题。部分账号返回 0 条原始结果或被窗口/关键词过滤，这不是“账号没有更新”的证明。

## 1. 今日高信号

- **科学计算从写代码转向验收和维护**：OpenAI 的 [`Scientific computing in the age of agentic AI`](../raw/2026-07-29/rss-fulltext/openai-blog/openai-blog-scientific-computing-in-the-age-of-agentic-ai-df22037e3e.opencli.md) 现场报告回顾 8 个生命科学等项目，涵盖维护、优化、语言迁移和 GPU 原生重写。案例共同指出代理降低实现成本，却不能判断科学有效性；可复现输出、统计行为和既有工具一致性仍需人类验收，项目还必须有明确维护者（官方全文，`fulltext_status=ok`）。
- **AI 找到密码学设计弱点，但没有生产影响**：Anthropic 的 [`Discovering cryptographic weaknesses with Claude`](../raw/2026-07-29/official-link-candidates/anthropicai-2082153297670992134-discovering-cryptographic-weaknesses.extracted.md) 称 Mythos 用约 60 小时改进 HAWK 攻击、把小型 HAWK-256 的估计成本从 `2^64` 降到 `2^38`，并把七轮 AES 的既有攻击提速约 200–800 倍；文章同时说明 HAWK 尚未部署、AES 只攻击减轮版本，当前生产系统无需改变。证据是 Anthropic 自述的官方原文，由 `AnthropicAI` 的 [`direct-x` 链接](https://x.com/AnthropicAI/status/2082153297670992134)发现，需等待论文和独立复核。
- **公开权重争论转向有针对性的治理措施**：Anthropic CEO 在 [`Our position on open-weights models`](../raw/2026-07-29/official-link-candidates/anthropicai-2081864750296658008-position-open-weights-models.extracted.md) 中否认主张全面禁止公开权重模型，主张限制高端芯片流向威权政府、打击工业规模蒸馏，并要求足够强的开放或闭源模型在发布前接受安全测试。它是公司政策立场，不是政府规则；`AnthropicAI` 的 [`direct-x` 原帖](https://x.com/AnthropicAI/status/2081864750296658008)只证明该立场被发布。
- **agent 工具链把发现、复现和修复串成可审阅记录**：`steipete` 的 [`direct-x` 原帖](https://x.com/steipete/status/2081767828278170002)称一个 agent 发现 Bun bug、另一个 agent 当夜修复；链接的 [`oven-sh/bun#36049`](http://github.com/oven-sh/bun/issues/36049) 已归档全文，给出 `child_process.spawn` 对 `encoding: "buffer"` 抛出 `ERR_UNKNOWN_ENCODING` 的复现、根因和两个修复方向，并标注为 AI 生成、人工复核的问题。issue 是官方问题记录，不等于修复已合入或发布。
- **FDE 的定价方式决定团队到底是产品、服务还是续约保险**：FDE Hub 的 [`Your Pricing Model Decides What Your FDE Team Is For`](../raw/2026-07-29/rss-fulltext/fde-hub/fde-hub-your-pricing-model-decides-what-your-fde-team-is-for-ba1a6e234a.extracted.md) 把部署付费归纳为计量消费、客户显式付费、几乎没有部署、以及费用藏在订阅毛利四类，并指出复杂度和 outcome 往往在信息最少时被写入合同。文章是行业分析而非客户侧审计，但对企业 AI 部署的成本、采用和续约责任有直接研究价值。
- **地理空间模型的瓶颈是数据和调度，不只是 GPU**：Ai2/Hugging Face 的 [`OlmoEarth Platform`](../raw/2026-07-29/rss-fulltext/huggingface-blog/huggingface-blog-the-olmoearth-platform-geospatial-inference-at-planetary-scale-92e866603d.opencli.md) 采用 CPU 数据获取与预处理、GPU 推理、CPU 后处理的三段式流水线，维护跨卫星供应商的 STAC 元数据索引，以可重入、幂等任务应对失败。文章自报一次北美野火风险运行使用约 19,600 CPU、994 GPU，约 30.5 小时完成；这些数字仍需外部复测。
- **Codex 新版本已发布，但功能不可判读**：[`rust-v0.146.0-alpha.15`](https://github.com/openai/codex/releases/tag/rust-v0.146.0-alpha.15) 是本轮最新 OpenAI Codex release，Atom 全文状态 `limited`，归档入口见 [`github-release-fulltext/openai-codex`](../raw/2026-07-29/github-release-fulltext/openai-codex/)。不能从版本号推断功能，也不能把 `alpha.14`、`alpha.13` 等近期条目重复算成今日功能更新。
- **Claude Code 的控制面继续变细**：可读的 [`v2.1.219 release body`](../raw/2026-07-29/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.219-0be0b416a3.atom.md) 提到 Claude Opus 5 默认模型与 1M 上下文、严格网络 allowlist、MCP 配置错误可见性、动态工作流大小指引、嵌套 subagent 转发和结构化 runner/session 失败分类；最新 [`v2.1.220`](../raw/2026-07-29/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.220-65266a9cdd.atom.md) 只有简短的可靠性说明，不能写成具体变更。
- **治理组件从提示语移到执行前控制**：GitHub Trending 的 [`microsoft/agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit) README 说明其公共预览版把策略、身份、沙箱和可观测性放在工具调用、消息发送和 agent 委派之前；它仍是项目自述，需检查实际拒绝路径、日志完整性和框架兼容性。
- **本地语音 agent 已有可替换的端到端接口**：[`huggingface/speech-to-speech`](https://github.com/huggingface/speech-to-speech) README 归档了 VAD→STT→LLM→TTS 四段流水线，提供 OpenAI Realtime 兼容 WebSocket，并可把 LLM 指向本机 vLLM、llama.cpp 或云端兼容端点。README 还说明组件和硬件依赖可切换；“数千个机器人生产使用”是项目自述，需要独立验证延迟、稳定性和数据边界。
- **知识库被编译为按需加载的 agent skill**：[`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) 把书籍或文档拆成 `SKILL.md`、章节、词汇表和决策规则，主张比整本塞进上下文少 24–51 倍 token。README 的性能数字是项目自测，需在真实文档和任务上复现，尤其验证是否保留原文证据而非只生成摘要。
- **跨提供商与企业部署的接缝成为产品层**：`andrewyng/aisuite` 的 README 说明统一 Chat Completions API、Agents API 和工具策略；其 OpenWorker 桌面协作者已迁移到独立仓库，当前仓库只保留快照。它适合作为接口抽象线索，不证明跨提供商行为完全一致。

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

OpenAI 的科学计算报告是本轮最完整的一手正文：8 个案例都把“谁定义正确性、谁负责维护”放在代理速度之上；同一报告还提醒，降低实现成本会增加重复重写和维护碎片化。OpenAI News 页面本轮使用 `opencli-read`，归档在 [`official-page-text`](../raw/2026-07-29/official-page-text/)。Codex 最新 `alpha.15` 及前几条 release 均为 `limited`，只能确认发布存在。

Claude Code `v2.1.219` 是近期背景而非今日新发布，重点是模型默认值、网络 allowlist、MCP 错误、动态 workflow 大小和 subagent 转发；`v2.1.220` 只写可靠性修复，不能补写功能。Claude Code 相关 release 索引见 [`github-items.json`](../raw/2026-07-29/github-items.json)。

### LLM / Frontier Models

Anthropic 的密码分析报告把 frontier 模型能力推到研究级密码学，但官方同时把 HAWK 和减轮 AES 的现实影响限定为“当前没有生产影响”。OpenAI 账号的 [`direct-x` 使命表述](https://x.com/OpenAI/status/2082208694142730340)与 [`科学计算帖](https://x.com/OpenAI/status/2082152074071228702) 支持其产品叙事，但不提供独立效果评估。`mattpocockuk` 的 [`Claude Code plugin` 说明](https://x.com/mattpocockuk/status/2082028549125624164) 是工具分发线索，不等于插件质量审计。

### AI Agent / Agentic Workflow

科学计算报告、Bun issue 和 FDE Hub 分别展示了“代理实现—人类验收”“代理发现—官方 issue”“部署—商业 outcome”三条链。`gregisenberg` 的 [`marketing agents` 描述](https://x.com/gregisenberg/status/2081814601851900221) 把营销 agent 描述成读取实时业务数据、执行、读结果再改进的循环；这属于个人方案叙事，尚无成本、权限、转化和失败率证据。

### AI Coding / Developer Tools

Codex release 当前只有版本存在证据；Claude Code `v2.1.219` 的可读正文则显示，后台 review、MCP 错误、网络 allowlist、工作流大小与嵌套 subagent 都在产品控制面内化。`mattpocockuk` 的插件帖和 `rileybrown` 的 [`Codex Buzz 配置多个模型个案`](https://x.com/rileybrown/status/2082202895508775070) 是 `direct-x` 个案，不能推出普遍的多模型编排可靠性。

### AI Governance / Public Legitimacy

Anthropic 的公开权重文章提供了明确公司立场：不主张全面禁用公开权重，优先芯片管制、打击工业规模蒸馏、对足够强的开放或闭源模型做发布前安全测试。Microsoft Agent Governance Toolkit 则把策略、身份、沙箱、审计写进执行层。二者都是公司/项目材料，本轮没有新的政府法规或监管原文；OpenAI 的 [`direct-x 治理表述`](https://x.com/OpenAI/status/2082208694142730340) 只作为覆盖线索。

### AI Infrastructure / Open Source

OlmoEarth 把跨供应商卫星数据、元数据索引、CPU/GPU 分工、自动重试和地图拼接组合成可运营平台；`huggingface/speech-to-speech` 则把本地语音 agent 组件化并暴露 Realtime 兼容接口。GitHub Trending 还出现 `aisuite`、GeoLibre 和本地语音项目，但热门度不等于采用或生产可靠性。`EXM7777` 的 [`Fish Audio S2.1 Pro` 说法](https://x.com/EXM7777/status/2082180140780650647) 是未经独立验证的 `direct-x` 市场叙事，不作为基础设施结论。

### Forward Deployed Engineering / Enterprise AI Deployment

FDE Hub 的全文把固定 outcome、setup fee、隐藏在订阅里的实施成本和续约采用放到同一张商业图上。它提示企业 AI 的关键验收不只是“上线”，还包括复杂度估计、真实运营者参与、采用率和续约；文章属于二手行业分析，不替代合同、客户数据或财务披露。

### Indie Hacking / Solo Founder 与 Product / Growth / GTM

`marclou` 发布的 [`1,127 家创业公司 B2B/B2C 对比`](https://x.com/marclou/status/2082085413091700934) 与 [`AI 视频剪辑插件收入个案`](https://x.com/marclou/status/2081890388298874880) 是自报或转发数据；`gregisenberg` 的营销 agent 是产品叙事。它们可作为分发、定价和小团队自动化的候选线索，但不能升级为市场规模、收入中位数或替代率。

### AI Systems / Automation

Bun issue 是本轮最可审阅的自动化证据：短帖、可复现代码、根因和官方问题正文形成闭环，但修复状态仍待合并验证。`marclou` 的创业公司数据与 `steipete` 的 [`Codex/网络安全转发`](https://x.com/steipete/status/2082071399691399472) 只能证明账号发布了这些说法；不把转发或商业数字写成系统性能事实。

### X/Twitter 推主主题摘要

以下按 [`twitter-topic-brief.json`](../raw/2026-07-29/twitter-topic-brief.json) 为每个有内容主题选取 1–3 条最高分条目。所有条目均为 `direct-x`，只证明 `twitterapi.io` 返回了账号发布内容；同一 tweet 可被多个主题路由，不能替代原文或独立验证。

- **LLM / Frontier Models（43 条）**：`mattpocockuk` 的 [Claude Code plugin](https://x.com/mattpocockuk/status/2082028549125624164)、`OpenAI` 的 [使命表述](https://x.com/OpenAI/status/2082208694142730340)、`AnthropicAI` 的 [密码学研究链接](https://x.com/AnthropicAI/status/2082153297670992134)；分别是工具分发、公司叙事和研究发布线索。
- **AI Agent / Agentic Workflow（95 条）**：`gregisenberg` 的 [marketing agent 循环](https://x.com/gregisenberg/status/2081814601851900221)、`OpenAI` 的 [科学计算帖](https://x.com/OpenAI/status/2082152074071228702)、`steipete` 的 [agent 修复 Bun](https://x.com/steipete/status/2081767828278170002)；只有 Bun 链接叠加可读官方 issue。
- **AI Coding / Developer Tools（85 条）**：`marclou` 的 [创业公司数据](https://x.com/marclou/status/2082085413091700934)、`mattpocockuk` 的 [插件说明](https://x.com/mattpocockuk/status/2082028549125624164)、`rileybrown` 的 [Buzz 多模型配置个案](https://x.com/rileybrown/status/2082202895508775070)；均需真实项目复测。
- **AI Governance / Public Legitimacy（11 条）**：`OpenAI` 的 [frontier AI 使命帖](https://x.com/OpenAI/status/2082208694142730340)、`OpenAI` 的 [GPT-Live 计划可用性帖](https://x.com/OpenAI/status/2081794871795589485)、`AnthropicAI` 的 [公开权重立场帖](https://x.com/AnthropicAI/status/2081864750296658008)；本主题仍没有监管原文。
- **AI Infrastructure / Open Source（1 条）**：`EXM7777` 的 [Fish Audio S2.1 Pro 说法](https://x.com/EXM7777/status/2082180140780650647) 是单条、未经独立核验的市场线索。
- **Indie Hacking / Solo Founder（42 条）**：`marclou` 的 [B2B/B2C 数据](https://x.com/marclou/status/2082085413091700934)、`gregisenberg` 的 [营销 agent](https://x.com/gregisenberg/status/2081814601851900221)、`marclou` 的 [AI 视频插件收入个案](https://x.com/marclou/status/2081890388298874880)；均为个案或自报数据。
- **Product / Growth / GTM（81 条）**：`marclou` 的 [B2B/B2C 对比](https://x.com/marclou/status/2082085413091700934)、`mattpocockuk` 的 [插件分发](https://x.com/mattpocockuk/status/2082028549125624164)、`marclou` 的 [创业产品增长个案](https://x.com/marclou/status/2081890388298874880)；没有独立收入或留存审计。
- **AI Systems / Automation（37 条）**：`marclou` 的 [创业公司自动化数据](https://x.com/marclou/status/2082085413091700934)、`steipete` 的 [Bun agent 链](https://x.com/steipete/status/2081767828278170002)、`steipete` 的 [Codex 网络安全转发](https://x.com/steipete/status/2082071399691399472)；转发和短帖不等于运行时证明。
- 本轮没有 `fde` 主题条目；这是摘要路由覆盖边界，不能解释为 FDE 方向没有更新。

### GitHub Trending 每日发现

本轮解析 10/10 个 repo-card、归档 10/10 README。每个项目下面同时使用 Trending description 与 README 归纳；它们都是 `secondary-source` 发现线索，不是发布、质量或安全背书。

- [`pascalorg/editor`](https://github.com/pascalorg/editor)：面向建筑项目的 3D 编辑器，用 React Three Fiber、WebGPU 和 Next.js/Turborepo 组织 viewer、编辑器、节点与核心状态；README 说明 Zustand 场景状态、IndexedDB 持久化、撤销/重做和插件注册，适合需要可扩展建筑场景编辑的使用者。今天值得记录在于它把 3D 场景编辑拆成可替换运行时与工具层；仍需实测 WebGPU 兼容、插件权限和生产部署。
- [`jenkinsci/jenkins`](https://github.com/jenkinsci/jenkins)：成熟的 Java 自动化服务器，用 2,000+ 插件编排构建、测试、静态分析和部署，并提供 Weekly 与 LTS 两条发布线。上榜反映发现热度，不是今天发布或质量变化；生产使用仍需审阅插件供应链、权限和升级策略。
- [`moeru-ai/airi`](https://github.com/moeru-ai/airi)：可自托管的 AI 虚拟角色/数字陪伴体，README 描述实时语音、Minecraft/Factorio 交互以及 Web、macOS、Windows 运行，并列出 RAG、memory、嵌入式数据库和 Live2D 子项目。项目明确警告没有官方代币；需验证模型调用、数据留存、第三方连接和账号权限。
- [`andrewyng/aisuite`](https://github.com/andrewyng/aisuite)：Python 库提供跨 OpenAI、Anthropic、Google、Mistral、Hugging Face、Ollama 等提供商的统一 Chat Completions API，并在 Agents API 中加入工具、MCP 和策略；README 说明 OpenWorker 已迁移到独立仓库。它解决的是提供商切换和工具调用接口收敛问题，仍需测参数语义、错误处理和密钥边界。
- [`affaan-m/ECC`](https://github.com/affaan-m/ECC)：面向 Claude Code、Codex、Cursor 等 harness 的工程工具箱，把计划、测试验证、审查、记忆、技能和 hooks 组合成可复用工作流。README 要求只从官方仓库/npm/插件渠道安装并警告第三方镜像风险；这是项目自述，需逐项审阅权限、脚本和跨 harness 差异。
- [`huggingface/speech-to-speech`](https://github.com/huggingface/speech-to-speech)：本地语音 agent 管线将 VAD、STT、LLM、TTS 通过队列连接，提供 OpenAI Realtime 兼容 WebSocket，可选本地 Transformers、MLX、vLLM 或 llama.cpp。它解决低延迟语音交互的组件替换和部署问题；要验证设备依赖、延迟、音频留存和工具调用权限。
- [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill)：把 PDF、文档目录或资料集合编译成核心 `SKILL.md`、按章文件、词汇表、模式和速查表，agent 按需读取章节而不是每次把整本书塞进上下文。它适合反复查阅的知识库，但 README 的 24–51 倍 token 节省是自测声明，需复现召回、引用和版权边界。
- [`opengeos/GeoLibre`](https://github.com/opengeos/GeoLibre)：轻量云原生 GIS，使用 Tauri v2、React/TypeScript、MapLibre GL JS、DuckDB-WASM Spatial 和 deck.gl，在浏览器、桌面、移动端和 Jupyter 中共享工作区。README 声称本地化数据并支持 SQL、插件和嵌入；需验证离线/云端数据流、插件权限和大数据量性能。
- [`paperswithbacktest/awesome-systematic-trading`](https://github.com/paperswithbacktest/awesome-systematic-trading)：策展型量化交易资源表，按回测、实盘、策略、风险、经纪商 API 和数据源整理 97 个库、40+ 策略、书籍和教程。它是索引而非交易系统或收益证据；金融使用必须独立检查维护状态、数据许可、回测偏差和交易成本。
- [`microsoft/agent-governance-toolkit`](https://github.com/microsoft/agent-governance-toolkit)：公共预览工具包把策略执行、零信任身份、沙箱、可靠性工程和审计放进 agent 工具调用之前，README 覆盖 Python、npm、NuGet、Claude Code 插件和 OWASP Agentic Top 10 映射。它直接对应企业上线的控制面，但“生产级公共预览”是项目自述，需验证拒绝不可绕过、身份追踪、日志防篡改和破坏性操作边界。

## 3. 来源证据表

| 来源组 | 本轮结果 | 代表证据与边界 |
| --- | --- | --- |
| RSS/Atom | 32 源，31 成功；56 条关注/一手正文 56/56 可读 | OpenAI 科学计算全文见 [`rss-fulltext/openai-blog`](../raw/2026-07-29/rss-fulltext/openai-blog/)；`nabeel-qureshi` feed 解析失败，不能写成无更新。 |
| GitHub release | 7/7 Atom 成功；4 条一手全文可读、6 条 `limited` | Codex 与 Claude Code 状态见 [`github-items.json`](../raw/2026-07-29/github-items.json)；Atom 正文不足时只保留发布存在边界。 |
| GitHub Trending | 10/10 repo-card；10/10 README | 统一 `secondary-source`，字段和归档路径见 [`github-trending.json`](../raw/2026-07-29/github-trending.json)。 |
| 官方页面 | 4/4 成功 | OpenAI News 使用 `opencli-read`，归档见 [`official-page-text`](../raw/2026-07-29/official-page-text/)。 |
| X/Twitter | 27 个账号均返回；128 条 `direct-x` | 结构化结果见 [`twitterapi-io-results.json`](../raw/2026-07-29/twitterapi-io-results.json)，主题聚合见 [`twitter-topic-brief.json`](../raw/2026-07-29/twitter-topic-brief.json)。 |

## 4. X/Twitter 覆盖说明

- 本轮 `twitterapi.io` 为 `ok`：27 个账号均返回，保留 128 条 direct-x；`rryssf_`、`Yangyixxxx`、`zhaogua61654931`、`lidang` 等账号返回 0 条原始结果，另有账号因窗口、关键词或去重保留 0 条。它们都是覆盖边界，不是账号没有更新的结论。
- 接口使用最近约 24–36 小时上下文，默认 `includeReplies=false`；主题摘要中部分条目来自 7 月 27 日晚或 7 月 28 日，已按 `window_status` 和边界说明处理，不伪装成全部是 7 月 29 日新事件。
- 所有 X/Twitter 内容均标注 `direct-x`。转发、短句、个人体验、收入数字和高收益叙事只证明账号发布了该说法；只有 Bun issue、Anthropic 密码学文章和公开权重文章成功归档了链接正文，才可叠加官方正文证据。
- 本轮未使用 Exa MCP、登录态 X/Twitter 浏览器、账号密码、官方 X API 或任何发帖、点赞、关注、私信和其它 action endpoint。

## 5. 候选审计与处置

<!-- dsi-candidate-audit: covered=14 missed=76 -->

初稿后由 [`candidate-audit.py`](../scripts/candidate-audit.py) 根据当天 raw 生成稳定 candidate id。审计会覆盖当日未在 `state/seen.json` 中出现过的匹配 RSS、官方链接候选和主题 direct-x；未逐条展开的 direct-x 多为重复路由、转发、短句或缺乏上下文的个案，未被写成事实。三个 official-link candidate（Bun issue、Anthropic 密码学、Anthropic 公开权重）均已在“今日高信号”和主题摘要中给出 tweet 与正文链接；最终 covered/missed 数字以 [`candidate-audit.json`](../reviews/2026-07-29-candidate-audit.json) 为准。

## 6. 不确定性与待验证项

- `nabeel-qureshi` RSS 仍是 XML parse failed；下一轮重试同一 URL，不能把失败写成无更新。
- Codex `alpha.15`、`alpha.14`、`alpha.13`、`alpha.12`、`alpha.11` 与 Claude Code `v2.1.220` 的 release body 为 `limited`；最小验证是打开对应 release 页面补全文本，不能从版本号推断功能。
- Anthropic 密码分析结果、HAWK/AES 影响范围、OlmoEarth 的吞吐/成本和 `book-to-skill` 的 token 节省都是官方或项目自述；需论文、代码、独立复测和生产日志验证。
- FDE Hub 的定价四分法是行业文章，不是客户合同或财务审计；下一步应收集真实部署周期、setup fee、采用率、续约和毛利数据。
- GitHub Trending 的十个项目 README 全部归档成功，但热度只说明今日被发现；涉及 agent 执行、凭据、插件、交易、浏览器、隐私或安全的项目必须先做权限、供应链、数据流和合规检查。
- X/Twitter 只提供结构化 direct-x 证据，未承诺完整时间线覆盖；`direct-x` 不等于事实核验，也不能替代原帖链接指向的官方正文。
- 本轮 `run-summary.json` 与 `signals.json` 是流程派生物，原始 JSON、HTML/Markdown 正文和 README 归档仍是证据真相源。

## 7. 当天产物

- 运行摘要：[`raw/2026-07-29/run-summary.json`](../raw/2026-07-29/run-summary.json)
- 报告阅读清单：[`raw/2026-07-29/report-reading-list.json`](../raw/2026-07-29/report-reading-list.json)
- 信号派生：[`raw/2026-07-29/signals.json`](../raw/2026-07-29/signals.json)
- 原始状态清单：[`raw/2026-07-29/manifest.json`](../raw/2026-07-29/manifest.json)
- 候选审计：[`reviews/2026-07-29-candidate-audit.json`](../reviews/2026-07-29-candidate-audit.json)
- 日报 Markdown 是本报告；通过严格校验后再派生日期化 HTML、索引 JSON 和 `docs/index.html`。
