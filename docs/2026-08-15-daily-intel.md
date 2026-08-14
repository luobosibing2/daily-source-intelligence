# 2026-08-15 每日源情报

## 直接答案

本轮按北京时间 2026-08-15 00:00 至 2026-08-16 00:00 的严格窗口派生出 13 条 inside 信号：3 条官方 Codex release、1 条已读 RSS 正文和 9 条 direct-x；另有 6 条 unknown 候选：1 条 X 引出的 GitHub 链接和 5 个 GitHub Trending README。正文阅读清单共 19 条，其中 7 条有本地正文、12 条只能作为受限证据或发现线索。

今天最值得跟进的是 Codex 0.148.0-alpha.16、0.148.0-alpha.17 和 rust-v0.148.0-alpha.18 在同一窗口连续出现，但 Atom release body 都只有版本级短内容，因此只能确认版本发布，不能据此推断功能、权限、模型或计费变化。另一个可读的一手材料是 The Pragmatic Engineer 对 Grok Bot 的体验：它把托管式通用智能体描述为面向知识工作的“Codex 式”入口；这仍是二手体验，不是产品方规格或采用率证据。X/Twitter 还出现了单卡 RTX 5090 的速度说法、本地 Qwen 27B 的低门槛说法和“AI coding 快到人看不懂代码”的风险讨论，均保留为 direct-x 线索，不能升级为性能、产品或安全结论。

## 采集范围

- 时间窗口：北京时间 2026-08-15 00:00 至 2026-08-16 00:00；采集在约 05:17–05:23 完成。窗口派生见 [signals.json](../raw/2026-08-15/signals.json)，原始证据仍以 [当天 raw 目录](../raw/2026-08-15/) 为准；没有发布时间的官方链接候选和 Trending 项目标为 unknown。
- RSS/Atom：32 个源中 31 个成功，dwarkesh-patel 因 curl: (52) Empty reply from server 失败。49 条命中关注方向或一手重点源的正文全部尝试且 49/49 为 ok；大多数是滚动背景，只有 The Pragmatic Engineer 的 The Pulse 进入严格窗口，见 [rss-items.json](../raw/2026-08-15/rss-items.json)、[RSS 正文归档](../raw/2026-08-15/rss-fulltext/) 和 [source-health.json](../state/source-health.json)。
- GitHub release：7/7 个 Atom 源成功，REST API 按设计为 skipped。一手重点 release body 共尝试 10 条，其中 4 条可读、6 条为 limited；严格窗口内的 3 个 Codex alpha 版本均为 limited，见 [github-items.json](../raw/2026-08-15/github-items.json) 和 [release 全文目录](../raw/2026-08-15/github-release-fulltext/)。
- GitHub Trending：榜单源 1/1 成功，10/10 个 repo 卡片和 10/10 个 README 均已归档，统一标为 secondary-source。Trending 只是发现/研究线索，不是官方发布、质量背书、采用率或长期趋势证明，见 [github-trending.json](../raw/2026-08-15/github-trending.json) 和 [README 归档](../raw/2026-08-15/github-trending-readmes/)。
- 官方页面：4/4 成功；OpenAI 新闻列表的 curl 响应受 challenge 影响，改用 opencli-read 读取，其他页面为页面级抓取，不把列表页升级成每篇文章的正文证据，见 [official-pages.json](../raw/2026-08-15/official-pages.json) 和 [官方页面归档](../raw/2026-08-15/official-page-text/)。
- X/Twitter：twitterapi.io provider 为 ok，27 个账号中 24 个请求成功、AnthropicAI、genspark_ai、cellinlab 3 个请求超时失败；滚动窗口保留 121 条 direct-x 记录。失败账号和返回零条的账号都只是 coverage boundary，不解释为“没有更新”，见 [twitterapi-io-results.json](../raw/2026-08-15/twitterapi-io-results.json) 和 [twitter-topic-brief.json](../raw/2026-08-15/twitter-topic-brief.json)。
- 官方链接候选：从 priority X 账号得到 1 条 GitHub 候选，正文抓取成功但仍只是 X 引出的仓库线索，见 [official-link-candidates.json](../raw/2026-08-15/official-link-candidates.json) 和 [候选归档](../raw/2026-08-15/official-link-candidates/)。

## 今日高信号

### 1. Codex 三个 alpha 版本连续进入窗口，但正文不足以说明功能

官方 [Codex 0.148.0-alpha.16](https://github.com/openai/codex/releases/tag/rust-v0.148.0-alpha.16)、[0.148.0-alpha.17](https://github.com/openai/codex/releases/tag/rust-v0.148.0-alpha.17) 和 [rust-v0.148.0-alpha.18](https://github.com/openai/codex/releases/tag/rust-v0.148.0-alpha.18) 在严格窗口内出现；对应本地 Atom 归档分别为 [alpha.16](../raw/2026-08-15/github-release-fulltext/openai-codex/openai-codex-0.148.0-alpha.16-86d15057ce.atom.md)、[alpha.17](../raw/2026-08-15/github-release-fulltext/openai-codex/openai-codex-0.148.0-alpha.17-b0530974f4.atom.md) 和 [alpha.18](../raw/2026-08-15/github-release-fulltext/openai-codex/openai-codex-rust-v0.148.0-alpha.18-bddbdb8632.atom.md)。三份正文均为 limited，它们只证明版本存在，不证明 CLI、TUI、权限、模型、沙箱或计费变化；证据等级为 official-source，最小验证路径是补抓对应 release 页面正文。

### 2. Grok Bot 被描述为托管式知识工作入口

已读的 [The Pulse: Meta’s self-inflicted resignation-wave](https://newsletter.pragmaticengineer.com/p/the-pulse-metas-self-inflicted-resignation) 认为 Cursor 团队发布的 Grok Bot 把通用 AI harness 做成了类似“知识工作的 Codex 体验”，作者还描述了自动化日常流程的个人体验。正文归档在 [本地全文](../raw/2026-08-15/rss-fulltext/pragmatic-engineer/pragmatic-engineer-the-pulse-meta-s-self-inflicted-resignation-wave-68c233597f.extracted.md)，证据等级为 secondary-source；它不提供权限模型、运行成本、稳定性、客户规模或可复现实验。

### 3. 单卡本地推理速度说法值得核对，但目前只有个人帖子

Hesamation 的 [帖子](https://x.com/Hesamation/status/2088299258613055580) 称单张 RTX 5090 可以以约每秒 200 token 运行接近 Opus-4.6 的模型。它是严格窗口内的 direct-x，只证明 twitterapi.io 返回了该帖子；没有模型名称、量化设置、上下文长度、温度、端到端延迟或独立基准，因此不能写成硬件性能结论。

### 4. 本地 Qwen 27B 的硬件门槛叙事正在扩散

frxiaobei 的 [中文帖子](https://x.com/frxiaobei/status/2088302915266236743) 称 Qwen3.8-27B 可在约 17GB 内存上本地运行，并把隐私、内网隔离和低成本部署联系起来。它是 direct-x 个人观察；版本、GGUF 参数、速度、质量、许可证和实际内存占用都未由官方材料确认。

### 5. AI coding 的主要风险被表述为“快到失去可解释进度”

frxiaobei 的 [帖子](https://x.com/frxiaobei/status/2088299848722424197) 讨论 AI Coding 让代码产出速度超过人对阶段目标和实现内容的理解；gregisenberg 的 [帖子](https://x.com/gregisenberg/status/2088369650065089018) 则建议先检查重复触发、稳定输入、工具清晰度和可测完成线。两者都是 direct-x，适合作为工作流设计问题的提醒，不是成功率、缺陷率或治理效果的测量。

### 6. X 引出的 DeepSeek Harness Desktop 仓库可读，但仍是待验证候选

cnyzgkc 的 [帖子](https://x.com/cnyzgkc/status/2088140505972666491) 链接到 [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop)。候选正文已抓取到 [本地归档](../raw/2026-08-15/official-link-candidates/cnyzgkc-2088140505972666491-deepseek-harness-desktop.extracted.md)，证据等级是 direct-x + GitHub 页面；在确认维护者、安装包、权限、许可证和可重复运行前，不把它写成已验证产品。

## 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- OpenAI/Codex 一手 Atom 在窗口内给出 3 个连续 alpha 版本，但三份 release body 都为 limited，因此只保留版本存在性。
- Claude Code 最新可读 release v2.1.232 的更新时间早于本次严格窗口，虽然它的 [本地 Atom 正文](../raw/2026-08-15/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.232-32d43bc3ba.atom.md)可读，本日报不把它写成 2026-08-15 新发布。
- OpenAI 新闻页通过 opencli-read 读取到 GPT‑5.6 开发者指南、Ultrafast 模式预览和企业使用 AI 等列表信息；这是页面级正文，不能替代逐篇文章正文。

### LLM / Frontier Models

Codex alpha 连续发布是唯一可由一手材料确认的窗口内版本信号，但功能正文不足。Qwen 本地运行、单卡速度和“SpaceXAI 加入前沿竞争”的帖子都是 direct-x 个人/转发叙事；需要官方模型卡、配置和独立评测后再比较。

### AI Agent / Agentic Workflow

The Pragmatic Engineer 将 Grok Bot 视为托管式通用 harness 的产品化尝试；gregisenberg 的重复触发/稳定输入/工具/完成线四问则提供了判断 agent 是否值得自动化的实用框架。两者共同指向从聊天到长流程执行的迁移，但取消、回滚、凭据隔离和失败恢复没有被本轮证据确认。

### AI Coding / Developer Tools

Codex alpha 版本只能作为 release 节奏信号。frxiaobei 关于“代码写得太快而人不再知道自己写了什么”的帖子，和 levelsio 关于把 Claude Code 接到路由器的 [实践帖](https://x.com/levelsio/status/2087903666158162214)，说明工具正在从编辑代码扩展到环境操作；这些都是个人经验，不能替代权限、审计和回滚测试。

### AI Governance / Public Legitimacy

本轮没有进入严格窗口、且能同时满足“AI lab/核心人物 + 公共权威或高影响治理文本”的新材料。OpenAI 新闻列表、Qwen 隐私叙事和 AI coding 可解释性讨论仍不足以支持政策、合法性或公共信任判断。

### AI Infrastructure / Open Source

Hesamation 转述的模型成本/效果比较和 Trending 中的 Needle 2、RAGFlow、SpiderFoot 都是发现线索。需要区分“可在小设备运行”“提供 RAG/OSINT 功能”和实际吞吐、数据隔离、误报率及生产部署效果。

### Indie Hacking / Solo Founder

levelsio 的 Claude Code 路由器实践、mattpocockuk 关于技能产品发布的 [帖子](https://x.com/mattpocockuk/status/2088272462618247478)，以及 marclou 关于 AI bot 抓取行为的 [观察](https://x.com/marclou/status/2087872366898827510) 都反映个人开发者围绕 agent 工具、分发和可发现性做产品化实验；没有收入、留存或转化证据。

### Product / Growth / GTM

Grok Bot 的托管入口、OpenAI Ultrafast 的限量开放说法和 agent-native 产品更新帖共同构成产品线索。direct-x 与 newsletter 体验不能证明市场规模、价格、客户留存或企业采购。

### AI Systems / Automation

cnyzgkc 的 DeepSeek Harness Desktop 链接、EXM7777 的 Seedance 2.5 [帖子](https://x.com/EXM7777/status/2088352573782978843) 和 steipete 关于把内部知识库检索做成 MCP 调用的 [转发](https://x.com/steipete/status/2088253401213911432) 都把 agent 从聊天界面推向可执行系统；证据仍是仓库候选或转发，必须补权限、凭据和恢复边界。

### Forward Deployed Engineering / Enterprise AI Deployment

严格窗口没有可独立验证的客户嵌入工程、现场数据整合、产品反馈闭环或 FDE 经济学新材料。direct-x 的工作流帖子最多说明需求叙事，不代表客户部署或服务化模型已成立。

### GitHub Trending 每日发现

榜单和 README 均已读取，证据等级统一为 secondary-source；上榜不等于官方发布、质量背书或长期趋势。以下把 Trending description 与 README 合并为可读介绍，并保留安全和验证边界。

- **[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)：给 Claude Code、Codex 和 Pi 使用的编辑式图示技能。** README 说明它提供多种架构、队列、策略追踪和共享记忆图示，默认生成自包含 HTML/SVG，也能重绘 draw.io 或 Mermaid；它试图解决 AI 图示模板化和品牌不一致问题。生成质量、外部网页取色、技能脚本权限和许可证仍需审查。
- **[cactus-compute/needle](https://github.com/cactus-compute/needle)：面向手机、穿戴设备、智能家居和机器人的超小模型。** README 称 Needle 2 是 4500 万参数、单个约 14MB 的工具调用/设备操作/结构化抽取模型，可在约 28MB RAM 的会话中运行，并提供 Python 推理、LoRA 微调和离线安装。模型效果、量化损失、设备兼容和授权需独立复现。
- **[megadose/holehe](https://github.com/megadose/holehe)：从邮箱判断其是否注册过多个网站账号的 OSINT 工具。** README 说明它通过忘记密码流程检查 Twitter、Instagram 等 120 多个站点，并提供 CLI、Python 模块和 Docker；这类枚举会触及隐私、误报、平台条款和滥用风险，不能把“能查询”写成授权或准确率保证。
- **[macro-inc/macro](https://github.com/macro-inc/macro)：把邮件、聊天、文档、任务、agent、通话和 CRM 放进带共享记忆的统一工作区。** README 的核心机制是统一界面、@ 链接和团队级记忆，目标是减少 Slack、Linear、Notion、HubSpot 之间的 MCP/Zapier 胶水；权限继承、记忆删除、数据迁移和商业可用性仍未验证。
- **[smicallef/spiderfoot](https://github.com/smicallef/spiderfoot)：用于威胁情报和攻击面测绘的 OSINT 自动化平台。** README 提供 Web UI/CLI、200 多个模块、YAML 关联规则、SQLite、CSV/JSON/GEXF 导出、Docker 和 Tor 集成；它适合安全研究和资产盘点，但外部数据合规、扫描授权、凭据保护和误报率需要严格边界。
- **[citrolabs/ego-lite](https://github.com/citrolabs/ego-lite)：让人和 AI agent 并行使用同一登录态浏览器的桌面浏览器。** README 称 agent 在独立 Space 中运行，用户的标签页保持不变，并通过 ego-browser 访问真实登录态；当前以 macOS 为主。共享登录态、跨任务隔离、网站条款、凭据泄露和远程控制风险必须先验证。
- **[holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS)：本地优先的多 agent 工作区。** README 称 Claude Code、Codex 和 holaOS 可在同一工具、文件、技能和共享记忆中并行运行，支持 100 多个集成、MCP、内置模型或 BYOK；“共享一套上下文”是设计描述，不证明权限分区、记忆删除、密钥托管或恢复能力。
- **[github/spec-kit](https://github.com/github/spec-kit)：面向任意 AI coding agent 的规格驱动开发工具包。** README 把“先定义要构建什么”组织成 CLI、阶段和可扩展 preset，目标是让规格成为软件交付的一部分而不是一次性脚手架；它值得记录，因为它把 agent coding 的控制点前移，但并不证明规格能自动保证实现质量。
- **[lightningpixel/modly](https://github.com/lightningpixel/modly)：完全在本地 GPU 上从图像或提示生成 3D 网格的桌面应用。** README 覆盖 Windows、Linux 和 Apple Silicon macOS，提供本地开源模型、安装包、Python 后端、工作流校验和错误提示；模型下载、显存需求、输入隐私、生成质量和平台差异需实际测试。
- **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)：融合 RAG 与 agent 模板的开源上下文引擎。** README 提供云服务、自托管、Docker/源码启动和面向企业的检索流程，强调复杂资料解析、上下文引擎和预置 agent 模板；“高保真、生产就绪”是项目自述，解析质量、权限隔离、成本和幻觉率没有由 Trending 证明。

### X/Twitter 推主主题摘要

以下来自 [twitter-topic-brief.json](../raw/2026-08-15/twitter-topic-brief.json)。这是滚动窗口的结构化摘要，不是完整账号时间线；每项保留 direct-x 和边界说明。严格窗口外的滚动帖子只作背景。

- **LLM / Frontier Models：** levelsio 的 [Claude Code 连接路由器实践](https://x.com/levelsio/status/2087903666158162214)、rileybrown 关于 [GLM 5.3、GrokBot 和 Claude Code 更新](https://x.com/rileybrown/status/2088137061312127008)、OpenAI 的 [GPT‑5.6 Sol Ultrafast 预览](https://x.com/OpenAI/status/2087947721936359705) 均为 direct-x；前两条是个人/社区摘要，最后一条是官方账号声明但没有逐篇产品正文。
- **AI Agent / Agentic Workflow：** rileybrown 的 [agent-native 周报预告](https://x.com/rileybrown/status/2088137061312127008)、OpenAI 的 [Ultrafast 预览](https://x.com/OpenAI/status/2087947721936359705) 和 mattpocockuk 的 [技能产品发布帖](https://x.com/mattpocockuk/status/2088272462618247478) 指向模型、技能和 agent 入口的组合，但没有统一成功率或安全测试。
- **AI Coding / Developer Tools：** levelsio 的 [Claude Code 路由器实践](https://x.com/levelsio/status/2087903666158162214)、rileybrown 的 [工具更新汇总](https://x.com/rileybrown/status/2088137061312127008) 和 OpenAI 的 [Ultrafast 预览](https://x.com/OpenAI/status/2087947721936359705) 是工具入口/速度线索，不是可复现实验。
- **AI Governance / Public Legitimacy：** OpenAI 的 [Ultrafast 开放范围说明](https://x.com/OpenAI/status/2087947721936359705)、OpenAI 的 [企业技能/插件使用观察](https://x.com/OpenAI/status/2087912623883051300) 和 simonw 对 [模型定价变化的观察](https://x.com/simonw/status/2087964264275587565) 仍不足以形成政策或公共权威结论。
- **AI Infrastructure / Open Source：** Hesamation 的 [Grok 4.6 与 DeepSeek 比较](https://x.com/Hesamation/status/2087940614142759228) 只有个人转述，缺少评测方法和基础设施成本数据。
- **Indie Hacking / Solo Founder：** levelsio 的 [Claude Code 实践](https://x.com/levelsio/status/2087903666158162214)、mattpocockuk 的 [技能发布帖](https://x.com/mattpocockuk/status/2088272462618247478) 和 marclou 的 [AI bot 抓取观察](https://x.com/marclou/status/2087872366898827510) 反映个人产品化路径，但没有收入或留存证据。
- **Product / Growth / GTM：** levelsio 的 [实践帖](https://x.com/levelsio/status/2087903666158162214)、rileybrown 的 [工具更新帖](https://x.com/rileybrown/status/2088137061312127008) 和 mattpocockuk 的 [发布帖](https://x.com/mattpocockuk/status/2088272462618247478) 是产品假设或个人体验，不是市场规模证据。
- **AI Systems / Automation：** cnyzgkc 的 [DeepSeek Harness Desktop 链接](https://x.com/cnyzgkc/status/2088140505972666491)、EXM7777 的 [Seedance 2.5 教程线索](https://x.com/EXM7777/status/2088260693451768232) 和 steipete 的 [MCP 内部知识检索转发](https://x.com/steipete/status/2088253401213911432) 指向可执行系统，但权限、凭据、版权和恢复边界未验证。
- **Forward Deployed Engineering / Enterprise AI Deployment：** EXM7777 的 [Seedance 2.5 业务制作线索](https://x.com/EXM7777/status/2088260693451768232) 只说明自动化内容制作叙事，不能证明客户嵌入工程、部署经济学或产品反馈闭环。

## 来源证据表

| 来源组 | 本轮结果 | 证据与边界 |
| --- | --- | --- |
| RSS/Atom | 32 源，31 成功、1 失败；49 条匹配正文，49 条 ok | [rss-items.json](../raw/2026-08-15/rss-items.json)；dwarkesh-patel 空回复失败；The Pulse 是本轮唯一进入严格窗口的已读 RSS 正文。 |
| GitHub release | 7/7 Atom；一手 release 10 条中 4 条 ok、6 条 limited | [github-items.json](../raw/2026-08-15/github-items.json)；REST API skipped；Codex 三个 alpha body 只支持版本存在性。 |
| GitHub Trending | 10/10 repo 卡、10/10 README | [github-trending.json](../raw/2026-08-15/github-trending.json)、[README 归档](../raw/2026-08-15/github-trending-readmes/)；统一为 secondary-source discovery signal。 |
| 官方页面 | 4/4 成功；OpenAI 新闻页使用 opencli-read | [official-pages.json](../raw/2026-08-15/official-pages.json)、[官方页归档](../raw/2026-08-15/official-page-text/)；列表页不等于逐篇正文。 |
| X/Twitter | provider ok；24/27 账号成功，3 个请求超时；121 条 direct-x | [twitterapi-io-results.json](../raw/2026-08-15/twitterapi-io-results.json)、[主题摘要](../raw/2026-08-15/twitter-topic-brief.json)；失败/零条账号只是覆盖边界。 |
| 官方链接候选 | 1 条候选，GitHub 正文抓取 ok | [official-link-candidates.json](../raw/2026-08-15/official-link-candidates.json)、[候选正文](../raw/2026-08-15/official-link-candidates/)；保留 direct-x + GitHub 双重边界，不能当作产品验证。 |

## X/Twitter 覆盖说明

本轮只使用 twitterapi.io 的读取端点，所有保留帖子标记为 direct-x；没有使用官方 X API、Exa MCP、登录态 X 浏览器、账号密码或写入/发帖/点赞/关注/私信端点。provider 整体为 ok，但 AnthropicAI、genspark_ai、cellinlab 的请求因超时失败，karpathy、kloss_xyz、rryssf_、Yangyixxxx、zhaogua61654931、lidang 等账号出现零条或零保留结果。它们都只能写成 coverage boundary；121 条滚动记录也不是完整时间线保证。

## 候选审计与处置

初稿后运行 [candidate-audit.py](../scripts/candidate-audit.py) 生成 [JSON 审计](../reviews/2026-08-15-candidate-audit.json) 与 [Markdown 审计](../reviews/2026-08-15-candidate-audit.md)。严格窗口内的 Codex release、The Pulse、9 条 direct-x 和 DeepSeek Harness Desktop 候选已在高信号、主题摘要或边界段落中处理；其余匹配 RSS、滚动 X 和 Trending 项目保留为已读候选或发现线索，不静默升级为今日发布。

<!-- dsi-candidate-audit: covered=15 missed=82 -->

## 不确定性与待验证项

- dwarkesh-patel RSS 本轮因 curl: (52) Empty reply from server 失败；失败不表示作者没有更新，下一轮继续重试。GitHub REST API 本轮按设计 skipped，Atom 是稳定读取路径。
- Codex 三个严格窗口 alpha release body 均为 limited；一手重点源中另有受限 release。最小验证路径是补抓对应 release 页面正文，不能从版本号或标题补写机制。
- Grok Bot 的“知识工作 Codex 体验”来自 newsletter 付费文章可读摘录和第三方帖子；它没有给出产品方权限、计费、客户量或恢复模型。
- Hesamation 的单卡速度、frxiaobei 的 Qwen 本地内存和 EXM7777 的 frontier 比较都缺少模型配置、硬件条件和独立评测；direct-x 只证明 API 返回帖子。
- X 主题摘要中的许多条目来自滚动 36 小时，严格窗口外的滚动帖子只作背景；转发、个人体验和社区周报不等于官方 release。
- DeepSeek Harness Desktop 的候选全文虽抓取成功，仍需要确认仓库维护、安装包来源、权限、许可证和可重复演示；在此之前只能是待验证候选。
- Trending 项目的浏览器共享登录态、邮箱枚举、OSINT 扫描、共享记忆、代码执行、本地模型、金融/内容自动化和外部 API 都可能有供应链、隐私、合规、凭据或回滚风险；榜单和 README 不构成安全或准确率证明。
- twitterapi.io 本轮有 3 个账号请求失败、多个账号返回零条或零保留结果；这些是覆盖边界，不使用 Exa 或登录态浏览器补漏。
- [signals.json](../raw/2026-08-15/signals.json)、[report-reading-list.json](../raw/2026-08-15/report-reading-list.json)、[run-summary.json](../raw/2026-08-15/run-summary.json) 和 bundle 都是派生控制物；原始 JSON、正文/README 归档与 [source-health.json](../state/source-health.json) 才是证据真相源。
- 中文阅读翻译阶段按当前合同退役，本轮没有创建 translations/2026-08-15/、.zh.md 或其它翻译派生产物。

## 当天产物

- 原始状态与窗口派生：[manifest.json](../raw/2026-08-15/manifest.json)、[signals.json](../raw/2026-08-15/signals.json)、[report-reading-list.json](../raw/2026-08-15/report-reading-list.json)、[run-summary.json](../raw/2026-08-15/run-summary.json)
- 稳定来源：[rss-items.json](../raw/2026-08-15/rss-items.json)、[github-items.json](../raw/2026-08-15/github-items.json)、[github-trending.json](../raw/2026-08-15/github-trending.json)、[official-pages.json](../raw/2026-08-15/official-pages.json)
- X/Twitter：[twitterapi-io-results.json](../raw/2026-08-15/twitterapi-io-results.json)、[twitter-topic-brief.json](../raw/2026-08-15/twitter-topic-brief.json)、[official-link-candidates.json](../raw/2026-08-15/official-link-candidates.json)
- 候选审计：由 [candidate-audit.py](../scripts/candidate-audit.py) 生成 [JSON](../reviews/2026-08-15-candidate-audit.json) 与 [Markdown](../reviews/2026-08-15-candidate-audit.md)。
- 趋势闭环：trend/reports/2026-08-15-trend-report.md；9 个 enabled trend 必须各自写入当天 manifest.json 或 no-new-signal.json marker。

## 边界与验证

- 已确认：稳定来源、只读 twitterapi.io、官方链接候选、X 主题摘要、update-state.py、run-dsi-pipeline.py --skip-collection、正文/README 归档均已按 2026-08-15 写入；[signals.json](../raw/2026-08-15/signals.json) 的 13 条 inside 与 6 条 unknown 可复核。
- 待完成的工作流闭环：candidate audit marker、严格日报校验、bundle、9 个 enabled trend 的 marker/Phase 1/Phase 2/check，以及 dedicated main 发布和 Gmail 独立发送，均须以本日报存在为前提继续执行。
- 运行时可能变化：RSS/XML、官方页面、GitHub release、Trending 排名、twitterapi.io 覆盖、远端 origin/main 和 Gmail 认证状态只以本轮命令输出与后续独立回读为准。
