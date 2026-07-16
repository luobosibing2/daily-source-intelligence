# 2026-06-29 Daily Source Intelligence

## 0. 采集范围

- 时间窗口：2026-06-29 日跑；RSS/Atom、GitHub release、GitHub Trending、官方页面按各源最近窗口采集，X/Twitter 使用 `twitterapi.io` 的 24-36 小时窗口。
- 配置来源：[config/watch.md](../config/watch.md)、[config/topics.yaml](../config/topics.yaml)、[config/sources.yaml](../config/sources.yaml)、[config/trends.yaml](../config/trends.yaml)。
- 生成时间：2026-06-29T03:05:31+08:00。
- 原始归档目录：[raw/2026-06-29/](../raw/2026-06-29/)。
- GitHub Trending：1 个 daily trending 源成功，解析 10 个 repo，10 个 Trending description 均保留，10 个 README 均写入本地归档；Trending 只作为 discovery signal，不作为质量、采用或安全背书。

## 1. 今日高信号

| 等级 | 主题 | 标题/信号 | 来源 | 证据等级 | 链接 | 为什么重要 |
| --- | --- | --- | --- | --- | --- | --- |
| 高 | AI Coding / 代码记忆 | `DeusData/codebase-memory-mcp` 把代码库索引成持久知识图谱，作为 MCP 工具提供毫秒级结构查询 | GitHub Trending | secondary-source | [repo](https://github.com/DeusData/codebase-memory-mcp) / [README 归档](../raw/2026-06-29/github-trending-readmes/DeusData__codebase-memory-mcp.md) | 这是今天最贴近 agent 长任务可靠性的新增线索：它把“少读文件、少耗 token、保留调用图”包装成独立 MCP server。边界是 README 自述性能未在本地复测。 |
| 高 | Financial Agents | `HKUDS/Vibe-Trading` 把交易能力包装成个人交易 agent，并提供 API/MCP、shadow account 和跨平台运行更新 | GitHub Trending | secondary-source | [repo](https://github.com/HKUDS/Vibe-Trading) / [README 归档](../raw/2026-06-29/github-trending-readmes/HKUDS__Vibe-Trading.md) | 金融 agent 正从投研 checklist 走向可执行交易工具；这类项目必须额外保留风险边界：README 上榜和更新记录不等于收益、合规或风控已验证。 |
| 中高 | 文档到 Agent 工作流 | `opendatalab/MinerU` 把 PDF、Office、图片和网页转换成 LLM/RAG/agent 可用的 Markdown/JSON | GitHub Trending | secondary-source | [repo](https://github.com/opendatalab/MinerU) / [README 归档](../raw/2026-06-29/github-trending-readmes/opendatalab__MinerU.md) | 它代表“复杂文档进入 agent 工作流”的基础设施化：多格式解析、OCR/VLM、MCP server 和 LangChain/Dify/FastGPT 集成都指向企业知识流转的输入层。 |
| 中高 | 语音输入 / 本地 AI | `altic-dev/FluidVoice` 提供 macOS 离线语音转文字，并强调本地 AI 增强和低延迟 dictation | GitHub Trending | secondary-source | [repo](https://github.com/altic-dev/FluidVoice) / [README 归档](../raw/2026-06-29/github-trending-readmes/altic-dev__FluidVoice.md) | 语音输入正在成为个人 agent/coding workflow 的前端入口；本地运行降低隐私暴露，但准确率、资源占用和许可仍需实测。 |
| 中高 | AI Coding / 使用方式 | Pieter Levels 继续强调把 Claude Code 放在 VPS 上长期编码，作为独立开发工作流的 direct-X field note | X/Twitter | direct-x | [tweet](https://x.com/levelsio/status/2071162399864889705) / [raw](../raw/2026-06-29/twitterapi-io-results.json) | 这不是官方发布，但说明 coding agent 的使用场景从本机 IDE 扩展到远端常驻环境：电量、会话连续性、服务器上下文和部署路径成为体验的一部分。 |
| 中高 | Computer Use / Agent 安全 | `Introducing computer use in Gemini 3.5 Flash` 说明 Google DeepMind 把 computer use 并入主力模型，并强调敏感动作确认与注入防护 | RSS fulltext | official-source | [原文](https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/) / [归档](../raw/2026-06-29/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-computer-use-in-gemini-3.5-flash-0ce8c6adc2.extracted.md) | 这条仍是今天可读的一手材料：真实界面操作能力进入模型产品后，安全边界必须落到系统、权限和人工确认，而不是只靠提示词。 |
| 中 | Agent 记忆 / 上下文压缩 | Matt Pocock 用 `/rewind` 和 `/compact` 观察长上下文后模型表现改善，提示“上下文新鲜度”仍是 coding agent 质量变量 | X/Twitter | direct-x | [tweet](https://x.com/mattpocockuk/status/2071288332642812229) / [raw](../raw/2026-06-29/twitterapi-io-results.json) | 这条适合放入 Memory & Dream 的使用侧证据：不是新产品能力，而是用户通过重跑和压缩体验到 agent 行为变化。 |
| 中 | AI Coding / 官方运行时 | Claude Code `v2.1.195`、`v2.1.193`、`v2.1.191`、`v2.1.187` release Atom 可读，继续集中在插件、hook、后台任务和远程会话 | GitHub release Atom | official-source | [v2.1.195](https://github.com/anthropics/claude-code/releases/tag/v2.1.195) / [归档](../raw/2026-06-29/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.195-ce628ff665.atom.md) | 这些不是 6 月 29 日新 release，但在今天窗口内仍构成一手重点源材料；它们显示 coding agent 运行时竞争继续落在权限、恢复、插件和远程执行可靠性。 |
| 中 | AI Agent 安全 | Simon Willison 的 OpenClaw prompt injection 复盘仍是今天可读全文候选，约束是二手复盘而非生产安全证明 | RSS fulltext | secondary-source | [原文](https://simonwillison.net/2026/Jun/26/hack-my-ai-assistant/#atom-everything) / [归档](../raw/2026-06-29/rss-fulltext/simonwillison/simonwillison-what-happened-after-2-000-people-tried-to-hack-my-ai-assistant-20e226947a.extracted.md) | 它继续提供 agent 安全攻防样本：模型抗注入能力增强不等于权限隔离、不可逆动作确认和工具边界可以省略。 |
| 中 | 企业 AI 交付 | FDE Hub 的 eval lifecycle 文章把 POC 到生产的差距拆成真实输入、错误观测、门槛和上线 gate | RSS fulltext | secondary-source | [原文](https://www.fdehub.org/p/the-eval-lifecycle-what-actually) / [归档](../raw/2026-06-29/rss-fulltext/fde-hub/fde-hub-the-eval-lifecycle-what-actually-happens-between-proof-of-concept-and-af0c7a85ff.extracted.md) | 这条延续企业 AI 落地判断：demo 后真正稀缺的是评估生命周期和生产反馈闭环，而不是一次性 prompt 或模型调用。 |
| 中 | 代码外层控制循环 | Armin Ronacher 的 `The Coming Loop` 继续把 coding agent 外层 harness 描述为队列、重试、继续会话和终止判断 | RSS fulltext | secondary-source | [原文](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/) / [归档](../raw/2026-06-29/rss-fulltext/lucumr/lucumr-the-coming-loop-387584b75f.extracted.md) | 对长期趋势来说，这条帮助解释为什么 agent 产品开始强调状态、验证、恢复和跨机器执行，而不是只强调单轮模型能力。 |

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS 今日仍抓到 `Previewing GPT-5.6 Sol: a next-generation model`、`How agents are transforming work`、`OpenAI and Broadcom unveil LLM-optimized inference chip`、`Helping build shared standards for advanced AI`、`How GPT-5 helped immunologist Derya Unutmaz solve a 3-year-old mystery` 等 always-read 条目，但 `rss-items.json` 标记为 `fulltext_status=limited`，OpenAI 官方新闻页也为 `limited`。因此今天只把它们当作官方发布线索和连续窗口背景，不新增未归档机制细节。
- OpenAI Codex release Atom 抓到 `0.143.0-alpha.29`、`0.143.0-alpha.28`、`0.143.0-alpha.27`、`0.143.0-alpha.26`、`0.142.3`，但 release body 均为 `limited`；今天只能记录版本节奏，不能写具体功能判断。
- Claude Code release Atom 可读度更好：`v2.1.195`、`v2.1.193`、`v2.1.191`、`v2.1.187` 为 `fulltext_status=ok`，`v2.1.190` 为 `limited`。今天的 Claude Code 判断继续来自这些一手 release body，而不是受限的 Claude docs release notes 页面。
- Anthropic News 和 Claude Blog 官方页面 fetch 为 `ok`，但今天没有形成比 Claude Code release 更强的新一手信号。

### X/Twitter 推主主题摘要

- AI Coding / Developer Tools：`levelsio` 记录把 Claude Code 放在 VPS 上长期编码的体验，`marclou`、`steipete` 等围绕独立开发和 coding agent 使用给出 field note；全部为 `direct-x`，只能说明使用扩散和主观体验。
- AI Agent / Agentic Workflow：`gregisenberg`、`steipete`、`marclou` 等讨论 agent/自动化产品使用；今天没有官方链接候选，因此不把这些社交讨论升级成官方事实。
- Memory / 上下文：`mattpocockuk` 关于 `/rewind`、`/compact` 和长上下文“变笨区”的观察，是上下文新鲜度与压缩策略的 direct-X 使用证据。
- Product / Growth / Indie：`levelsio`、`marclou`、`gregisenberg` 的高分 tweet 多数是独立开发工作方式、收入或产品体验讨论，适合作为市场感知，不作为技术发布。
- AI Governance / Public Legitimacy：`EXM7777`、`levelsio`、`Hesamation` 等被 topic brief 归类为 governance 相关，但今天没有官方长文候选；只保留在覆盖说明中。

### LLM / Frontier Models

- GPT-5.6 Sol、OpenAI/Broadcom 推理芯片、agents transforming work 等 OpenAI 条目都在一手重点源中出现，但正文受限。今天可确认的是“官方源仍在发布/扩散这些主题”，不可确认的是它们的具体技术、访问层级或指标细节。
- Google DeepMind 的 computer use 与 AI planning 旧窗口条目仍为可读全文，今天作为背景保留；没有比 GitHub Trending 中代码记忆、文档解析和金融 agent 更明确的新信号。
- Xe Iaso 的 cached token 成本解释、minimaxir 的 OpenRouter Hy3 观察、Lilian Weng 的 hallucination 文章可作为模型/推理背景，但不进入今天高信号。

### AI Governance / Public Legitimacy

- 官方治理线今天主要是受限的 OpenAI `Helping build shared standards for advanced AI` 与若干 direct-X field note；由于没有可读官方全文，不新增强治理结论。
- Google DeepMind 的 AI planning 条目可读，说明公共部门规划和 AI 加速流程仍是治理/公共服务应用方向；但它不是今天最核心新增。
- Simon Willison 的 OpenClaw 复盘继续支持 agent 安全边界判断：产品侧权限、隔离和人工确认是治理与安全交叉点。

### AI Agent / Agentic Workflow

- `The Coming Loop` 与 `The Eval Lifecycle` 仍是今天最清楚的机制解释材料：agent 价值越来越依赖外层控制循环、任务状态、验证、恢复和生产门禁。
- `MinerU`、`FluidVoice`、`codebase-memory-mcp` 展示了 agent 工作流输入层和上下文层的三个方向：文档结构化、语音输入、本地代码知识图谱。
- direct-X 中的使用侧内容可以帮助解释扩散，但不能替代 README、release body 或官方文档。

### AI Coding / Developer Tools

- `DeusData/codebase-memory-mcp` 是今天最贴近 coding agent 基础设施的 GitHub Trending 项：README 声称用 tree-sitter AST、Hybrid LSP 和持久知识图谱回答函数、类、调用链、HTTP route 等结构查询，并作为 MCP 工具暴露。
- Claude Code release Atom 继续提供一手运行时证据：插件同意、hook matcher、后台任务恢复、远程容器启动检查等问题，说明 agent 工具链正在补企业化运行和可恢复性。
- `levelsio` 的 VPS Claude Code 工作流、`mattpocockuk` 的 `/compact` 体验和 `The Coming Loop` 的 harness 叙述共同指向一个使用模式：coding agent 不是一次性聊天，而是长任务、长会话和可恢复环境。

### AI Infrastructure / Open Source

- `MinerU` 面向文档解析和 agent/RAG 输入层，README 确认可输出 Markdown/JSON，覆盖 PDF、DOCX、PPTX、XLSX、图片、网页，并提供 MCP server 和常见 AI 工具集成。
- `CuPy` 是成熟 GPU 数组计算库，今天上榜更像基础设施背景；它不是 agent 新能力，但对本地/服务端高性能推理和数据处理有间接意义。
- `free-for-dev` 是免费 tier 列表，服务 devops/infra discovery；与 AI 主线弱相关。

### Forward Deployed Engineering / Enterprise AI Deployment

- FDE Hub 的 eval lifecycle 仍是今天企业交付最相关材料：从 POC 到生产需要真实用户输入、静默错误观测、指标门槛和上线 gate。
- `MinerU` 也能进入企业交付背景：大量企业 agent 的前置瓶颈是把 PDF、Office、扫描件和网页转成可审计、可检索、可调用的结构化输入。
- Forward Deployed 系列、Ted Mabrey、Thomas Otter 等条目今天多为 `limited`，不能新增强判断。

### GitHub Trending / Daily Repos

- `simplex-chat/simplex-chat` 是无用户标识符的隐私通信网络，README 确认可用于移动端、桌面和 CLI，并强调双棘轮端到端加密和元数据保护；它不是 AI 项目，但对 agent 身份、私密通信和元数据边界有背景价值。
- `ripienaar/free-for-dev` 是面向 devops/infra 开发者的免费服务清单，靠社区 PR 维护；今天只作为开发者基础设施 discovery signal。
- `commaai/openpilot` 是面向 300+ 车型的驾驶辅助/机器人操作系统，README 说明需要支持设备、支持车型和车载 harness；上榜不是自动驾驶安全背书。
- `xbtlin/ai-berkshire` 继续上榜，是兼容 Claude Code/Codex 的价值投资研究 skill 集；它的收益展示不能作为投资建议、可复现绩效或风控证明。
- `Robbyant/lingbot-map` 是流式 3D 重建基础模型，README 描述几何上下文、轨迹记忆和约 20 FPS 推理；今天作为空间感知/机器人背景，不直接进入 agent 工作流主线。
- `DeusData/codebase-memory-mcp` 是代码智能 MCP server，最值得进入 Memory & Dream / AI Coding 趋势观察；性能、语言覆盖和查询效果需要本地验证。
- `cupy/cupy` 是 NumPy/SciPy 兼容的 GPU 数组计算库，支持 CUDA/ROCm；今天是基础设施背景。
- `altic-dev/FluidVoice` 是 macOS 本地语音转文字 app，强调 on-device AI enhancement 和低延迟；可作为个人 agent 输入层信号。
- `opendatalab/MinerU` 是高准确文档解析引擎，面向 LLM/RAG/agent 工作流输出 Markdown/JSON；与企业知识输入和 agent 数据准备高度相关。
- `HKUDS/Vibe-Trading` 是个人交易 agent，README 提到 API/MCP、shadow account、quick start 和近期运行更新；金融、交易、自动执行都属于高风险场景，必须单独验证合规、真实收益、风控和人工确认边界。

## 3. 来源证据表

| 来源 | 类型 | 原文链接 | 本地归档 | 证据等级 | 备注 |
| --- | --- | --- | --- | --- | --- |
| DeusData/codebase-memory-mcp | GitHub Trending + README | <https://github.com/DeusData/codebase-memory-mcp> | [README](../raw/2026-06-29/github-trending-readmes/DeusData__codebase-memory-mcp.md) | secondary-source | 高相关 discovery signal；README 自述未本地复测。 |
| HKUDS/Vibe-Trading | GitHub Trending + README | <https://github.com/HKUDS/Vibe-Trading> | [README](../raw/2026-06-29/github-trending-readmes/HKUDS__Vibe-Trading.md) | secondary-source | 金融/交易高风险项目，不能把上榜写成收益或合规证明。 |
| opendatalab/MinerU | GitHub Trending + README | <https://github.com/opendatalab/MinerU> | [README](../raw/2026-06-29/github-trending-readmes/opendatalab__MinerU.md) | secondary-source | 文档到 LLM/RAG/agent 输入层。 |
| altic-dev/FluidVoice | GitHub Trending + README | <https://github.com/altic-dev/FluidVoice> | [README](../raw/2026-06-29/github-trending-readmes/altic-dev__FluidVoice.md) | secondary-source | 本地语音输入和个人工作流信号。 |
| Claude Code v2.1.195 | GitHub release Atom | <https://github.com/anthropics/claude-code/releases/tag/v2.1.195> | [atom.md](../raw/2026-06-29/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.195-ce628ff665.atom.md) | official-source | `fulltext_status=ok`；同日归档还包括 v2.1.193、v2.1.191、v2.1.187。 |
| OpenAI Blog always-read 条目 | RSS/官方发布线索 | <https://openai.com/index/previewing-gpt-5-6-sol> | n/a | official-source / limited | `fulltext_status=limited`，不能写成已读正文。 |
| OpenAI Codex releases | GitHub release Atom | <https://github.com/openai/codex/releases> | [release dir](../raw/2026-06-29/github-release-fulltext/openai-codex/) | official-source / limited | 5 条 release Atom body 均为 limited。 |
| The Coming Loop | 博客/机制分析 | <https://lucumr.pocoo.org/2026/6/23/the-coming-loop/> | [extracted.md](../raw/2026-06-29/rss-fulltext/lucumr/lucumr-the-coming-loop-387584b75f.extracted.md) | secondary-source | agent harness / loop 趋势判断。 |
| The Eval Lifecycle | FDE Hub / 交付机制 | <https://www.fdehub.org/p/the-eval-lifecycle-what-actually> | [extracted.md](../raw/2026-06-29/rss-fulltext/fde-hub/fde-hub-the-eval-lifecycle-what-actually-happens-between-proof-of-concept-and-af0c7a85ff.extracted.md) | secondary-source | 企业 AI 交付与 eval gate。 |
| Introducing computer use in Gemini 3.5 Flash | Google DeepMind 官方博客 | <https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/> | [extracted.md](../raw/2026-06-29/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-computer-use-in-gemini-3.5-flash-0ce8c6adc2.extracted.md) | official-source | 可读全文；用于 computer use 与 agent 安全边界。 |
| X/Twitter direct evidence | twitterapi.io | n/a | [twitterapi-io-results.json](../raw/2026-06-29/twitterapi-io-results.json) | direct-x | API 总体可用，保留 100 条 direct-X。 |

## 4. X/Twitter 覆盖说明

- 本日报通过 `twitterapi.io` 收集 X/Twitter 直接证据，不使用官方 X API，不使用 Exa MCP，不使用登录态浏览器。
- `twitterapi.io` 总体状态为 `ok`；27 个账号采集均返回 `ok`，其中部分账号 raw_count 为 0，不能扩展解释为该账号完整无更新。
- 当天保留 direct-X 100 条。高分内容主要集中在独立开发、Claude Code/VPS 工作流、上下文压缩、AI coding 使用体验和产品增长讨论。
- [official-link-candidates.json](../raw/2026-06-29/official-link-candidates.json) 状态为 `ok`，候选数为 0；今天没有由 priority X account 触发的官方长文候选。

## 5. 不确定性与待验证项

- OpenAI 官方页面 `openai-news`、Claude docs release notes、OpenAI Blog always-read 条目和 OpenAI Codex release body 多数为 `limited`；不能把这些写成已读正文或新增机制细节。
- GitHub Trending 是发现线索，不是质量背书。`codebase-memory-mcp` 的性能、`MinerU` 的解析准确率、`FluidVoice` 的延迟/准确率、`Vibe-Trading` 的交易效果和风险控制都未在本地验证。
- RSS 中 Hugging Face、Antirez、Forward Deployed、SVPG、Ramp Builders、Palantir、Ted Mabrey、Thomas Otter 等来源存在 `limited` 条目；日报只保留边界，不升级为强结论。
- direct-X 只证明 API 返回了公开推文文本和链接；主观体验、收益、交易、模型能力或安全效果都需要官方材料、代码运行或独立评测补证。

## 6. 运行统计

- 新增条目：`seen_added=36`，`seen_total=2568`。
- 高信号条目：10 条。
- 稳定来源：RSS 32/32 成功，RSS fulltext 31/53 ok、22/53 limited；GitHub release sources 7/7 成功，release fulltext 4/10 ok、6/10 limited；GitHub Trending 1/1 成功，10 个 README 文件归档；官方页面 2 ok、2 limited。
- X/Twitter：`twitterapi.io` 成功，direct-X 100 条，账号级状态均为 `ok`。
- official-link candidates：0 条。
- candidate audit：[reviews/2026-06-29-candidate-audit.md](../reviews/2026-06-29-candidate-audit.md)，`covered=16`、`missed=90`；missed 已按下方处理记录降级、补入正文或保留待验证。

### Candidate audit 处理记录

以下条目被 audit 识别为候选但没有全部进入“今日高信号”。处理原则：一手重点源、agent 运行时、代码记忆、金融 agent、文档输入层、computer use、安全边界、FDE/eval 生命周期优先；`limited` 全文、历史窗口、泛工程教程、弱相关产品/独立开发社交内容或没有官方原文的 direct-X 只记录边界。

- Google DeepMind：`Introducing computer use in Gemini 3.5 Flash` 已补入高信号；`Unlocking UK house-building with AI-accelerated planning` 可读但今天作为公共部门应用背景处理，不高于 computer use 主线。
- OpenAI / Codex：5 条 OpenAI Blog always-read 均已在一手重点源处理为 `limited`；OpenAI Codex release body 也为 `limited`，不写机制判断。
- Simon Willison / agent 安全：OpenClaw 复盘已进入高信号；`Incident Report: CVE-2026-LGTM`、`Quoting Dean W. Ball`、`Quoting Timothy B. Lee`、`Quoting OpenAI` 是相关评论或背景，已降级到安全/治理背景。
- 模型、推理和基础设施：Hugging Face、Antirez、Sean Goedecke、Xe Iaso、minimaxir、Lilian Weng、geohot 等条目多数是旧窗口、背景解释或 `limited`；今天只作为模型市场、缓存成本、推理经济和 coding-agent 背景。
- 产品、FDE 和企业交付：FDE Hub 已进入高信号；Forward Deployed、SVPG、Ramp Builders、Palantir、Ted Mabrey、Thomas Otter 等条目多为 `limited` 或泛产品/工程背景，供 trend 阶段参考。
- top direct-X：`levelsio` VPS Claude Code 与 `mattpocockuk` compact/rewind 已进入高信号；`marclou`、`gregisenberg`、`EXM7777`、`Hesamation`、`frxiaobei`、`cnyzgkc` 等高分社交项多数是市场情绪、独立开发经验、转推或弱相关生活内容，不作为官方事实。

## 7. 完成审计

- 日报已写入：本文件。
- candidate audit：已写入 [reviews/2026-06-29-candidate-audit.md](../reviews/2026-06-29-candidate-audit.md)，`covered=16`、`missed=90`；missed 候选已按受限全文、历史窗口、弱相关或 direct-X field note 处理。
- trend report：已写入 [trend/reports/2026-06-29-trend-report.md](../trend/reports/2026-06-29-trend-report.md)。
- enabled trends：9 个 enabled trend 均已检查；8 个写入 `manifest.json`，`claude-tag-identity` 写入 [no-new-signal.json](../trend/raw/2026-06-29/claude-tag-identity/no-new-signal.json)。
- 更新过的 trend topic 文件：[trend/memory-dream.md](../trend/memory-dream.md)、[trend/financial-agents.md](../trend/financial-agents.md)、[trend/forward-deployed-engineering.md](../trend/forward-deployed-engineering.md)、[trend/enterprise-delivery-system.md](../trend/enterprise-delivery-system.md)、[trend/codex-feature-watch.md](../trend/codex-feature-watch.md)、[trend/ai-governance-legitimacy.md](../trend/ai-governance-legitimacy.md)、[trend/claude-code-feature-watch.md](../trend/claude-code-feature-watch.md)、[trend/codex-claude-usage-tactics.md](../trend/codex-claude-usage-tactics.md)、[trend/claude-tag-identity.md](../trend/claude-tag-identity.md)。
- trend raw marker：[memory-dream](../trend/raw/2026-06-29/memory-dream/manifest.json)、[financial-agents](../trend/raw/2026-06-29/financial-agents/manifest.json)、[forward-deployed-engineering](../trend/raw/2026-06-29/forward-deployed-engineering/manifest.json)、[enterprise-delivery-system](../trend/raw/2026-06-29/enterprise-delivery-system/manifest.json)、[codex-feature-watch](../trend/raw/2026-06-29/codex-feature-watch/manifest.json)、[ai-governance-legitimacy](../trend/raw/2026-06-29/ai-governance-legitimacy/manifest.json)、[claude-code-feature-watch](../trend/raw/2026-06-29/claude-code-feature-watch/manifest.json)、[codex-claude-usage-tactics](../trend/raw/2026-06-29/codex-claude-usage-tactics/manifest.json)、[claude-tag-identity no-new-signal](../trend/raw/2026-06-29/claude-tag-identity/no-new-signal.json)。
- trend check：`python3 scripts/run-trend-stage.py --date 2026-06-29 --check` 返回 `ok=true`。
