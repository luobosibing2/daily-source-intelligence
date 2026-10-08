# 2026-07-02 Daily Source Intelligence

## 0. 采集范围

- 时间窗口：2026-07-02 日跑；RSS/Atom、GitHub release、GitHub Trending、官方页面按各源最近窗口采集，X/Twitter 使用 `twitterapi.io` 的 24-36 小时窗口。
- 配置来源：[config/watch.md](../config/watch.md)、[config/topics.yaml](../config/topics.yaml)、[config/sources.yaml](../config/sources.yaml)、[config/trends.yaml](../config/trends.yaml)。
- 生成时间：2026-07-02T03:07:56+08:00。
- 原始归档目录：[raw/2026-07-02/](../raw/2026-07-02/)。
- 阅读清单：[report-reading-list.json](../raw/2026-07-02/report-reading-list.json)，共 499 条，其中 50 条有本地正文，449 条为结构化或边界条目。
- GitHub Trending：1 个 daily trending 源成功，解析 10 个 repo，10 个 Trending description 均保留，10 个 README 均写入本地归档；Trending 只作为 discovery signal，不作为质量、采用、安全或投资收益背书。

## 1. 今日高信号

| 等级 | 主题 | 标题/信号 | 来源 | 证据等级 | 链接 | 为什么重要 |
| --- | --- | --- | --- | --- | --- | --- |
| 高 | Claude Code / 默认模型 | `v2.1.197` 把 Claude Sonnet 5 设为 Claude Code 默认模型，并写明原生 1M token context 与限时价格 | Claude Code release Atom | official-source | [release](https://github.com/anthropics/claude-code/releases/tag/v2.1.197) / [归档](../raw/2026-07-02/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.197-c9b523c535.atom.md) | 这是今天最明确的一手 coding-agent 产品信号：默认模型、长上下文和价格同时进入 Claude Code release。边界是 release body 很短，真实性能、延迟和工具调用表现仍需实测。 |
| 高 | AI 治理 / 模型发布 | Anthropic 重新部署 Fable 5，并说明出口管制解除、网络安全分类器、安全余量、jailbreak 严重度框架和政府协作机制 | Anthropic official link candidate | official-source + direct-x | [原文](https://www.anthropic.com/news/redeploying-fable-5) / [归档](../raw/2026-07-02/official-link-candidates/anthropicai-2072163884430229756-redeploying-fable-5.extracted.md) | 这不是普通模型公告，而是“前沿能力发布如何被政府、安全评测和行业框架共同约束”的一手材料，适合进入 AI 治理与合法性趋势。 |
| 高 | Computer Use / Enterprise Agent | Google 把 computer use 做成 Gemini 3.5 Flash 内置工具，并强调浏览器、移动、桌面环境中的长任务和企业自动化 | Google DeepMind Blog | official-source | [原文](https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/) / [归档](../raw/2026-07-02/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-computer-use-in-gemini-3.5-flash-0ce8c6adc2.extracted.md) | 这是 agent 从工具调用走向真实界面操作的官方信号；Google 同时给出敏感操作确认、间接 prompt injection 停止任务、沙箱和人工核验等安全边界。 |
| 中高 | 多媒体生成 / 开发者 API | Google 发布 Nano Banana 2 Lite 与 Gemini Omni Flash 的开发者入口，强调低延迟图像生成、视频生成/编辑和串联工作流 | Google DeepMind Blog | official-source | [原文](https://deepmind.google/blog/start-building-with-nano-banana-2-lite-and-gemini-omni-flash/) / [归档](../raw/2026-07-02/rss-fulltext/google-deepmind-blog/google-deepmind-blog-start-building-with-nano-banana-2-lite-and-gemini-omni-flash-adbaffb551.extracted.md) | 生成式媒体正在从单点模型变成“图像草稿 -> 视频生成/编辑 -> 多轮交互历史”的开发者管线。边界是速度、价格和 benchmark 来自厂商自述。 |
| 中高 | 公共部门 AI / 企业交付 | Google DeepMind 与英国政府规划工具项目强调数据抽取、政策引用、反馈总结、报告草稿、人工最终决策和审计轨迹 | Google DeepMind Blog | official-source | [原文](https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/) / [归档](../raw/2026-07-02/rss-fulltext/google-deepmind-blog/google-deepmind-blog-unlocking-uk-house-building-with-ai-accelerated-planning-12ceb5f0dc.extracted.md) | 这条线索说明 AI 落地正在进入真实审批流程：工具承担重体力的信息处理，规划官保留最终决定，审计轨迹成为部署条件。 |
| 中高 | Agent 评测 / 生产化 | FDE Hub 的 eval lifecycle 强调从 PoC 到生产之间的检索评测、忠实性、引用准确率、guardrail 和上线 gate | RSS fulltext | secondary-source | [原文](https://www.fdehub.org/p/the-eval-lifecycle) / [归档](../raw/2026-07-02/rss-fulltext/fde-hub/fde-hub-the-eval-lifecycle-what-actually-happens-between-proof-of-concept-and-af0c7a85ff.extracted.md) | 它把企业 AI demo 到生产的差距拆成可测 gate，补强“企业交付系统”趋势：瓶颈不是模型能不能回答，而是能不能被评测、批准、监控和复盘。 |
| 中高 | Agent 安全测试 | `usestrix/strix` 把多 agent 渗透测试、动态运行、PoC 验证、CI/CD 阻断和修复建议写进开源安全工具 README | GitHub Trending | secondary-source | [repo](https://github.com/usestrix/strix) / [README](../raw/2026-07-02/github-trending-readmes/usestrix__strix.md) | 这是 agent 从编码助手进入发布门禁和安全验证的强 discovery signal；高风险边界是 README 自述不能替代靶场复现或安全效果证明。 |
| 中高 | Agent 工具分发 | `msitarzewski/agency-agents` 把面向 Claude Code、Cursor、Codex、Gemini 等工具的专家 agent 角色包和桌面安装器打包分发 | GitHub Trending | secondary-source | [repo](https://github.com/msitarzewski/agency-agents) / [README](../raw/2026-07-02/github-trending-readmes/msitarzewski__agency-agents.md) | 这说明“agent 角色/流程资产”正在像插件一样跨工具传播；边界是 role prompt 质量和实际交付能力未验证。 |
| 中 | 金融 Agent / 高风险垂直 | `HKUDS/Vibe-Trading` 上榜，README 描述个人交易 agent、影子账户、API/MCP、IM 研究投递和安全清理 | GitHub Trending | secondary-source | [repo](https://github.com/HKUDS/Vibe-Trading) / [README](../raw/2026-07-02/github-trending-readmes/HKUDS__Vibe-Trading.md) | 金融 agent 的信号价值在于高约束场景把 agent runtime、研究分发、影子账户和安全默认值绑定到一起；不能当作投资建议、收益证明或风控证明。 |
| 中 | AI 基础设施 / 成本路由 | `diegosouzapw/OmniRoute` 主张一个 endpoint 连接多 provider、多 coding tool、自动 fallback、压缩和 MCP/A2A | GitHub Trending | secondary-source | [repo](https://github.com/diegosouzapw/OmniRoute) / [README](../raw/2026-07-02/github-trending-readmes/diegosouzapw__OmniRoute.md) | coding agent 用户对多供应商路由、免费额度和成本控制的需求继续增强；README 的 provider 数量、免费 token 和压缩收益需要独立验证。 |

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- Claude Code release Atom 今天可读且高信号集中：`v2.1.197` 宣布 Claude Sonnet 5 成为默认模型；`v2.1.196` 加入组织默认模型、可读 session 名、文件附件点击、MCP 自批准安全修复、后台任务恢复、streaming idle watchdog 和远程会话恢复；`v2.1.195`、`v2.1.193`、`v2.1.191` 继续围绕后台 agent、MCP、插件、权限、语音、hook 和长会话稳定性修补。
- OpenAI Blog / OpenAI News 今天仍出现多条官方线索，但 `rss-items.json` 中一批 OpenAI 正文为 `fulltext_status=limited`；日报只记录为官方发布线索，不把 metadata 或 feed 摘要升级为已读全文结论。
- Anthropic 的 `Redeploying Fable 5` 通过 OpenAI/Anthropic priority X 链接候选抓到可读官方全文，证据等级按 official-source + direct-X 处理；它比普通推文更适合进入治理趋势。

### X/Twitter 推主主题摘要

- AI Agent / Agentic Workflow：`rileybrown`、`steipete`、`kloss_xyz`、`mattpocockuk` 等账号继续提供 agent workflow、tooling 和产品使用侧观察；这些是 `direct-x` field note，只能说明公开推文内容和扩散，不代表行业统计。
- AI Coding / Developer Tools：`AnthropicAI`、`simonw`、`mattpocockuk` 与 `steipete` 的高分项集中在 Claude Sonnet 5、Claude Code、skills、个人工作流和 coding agent 实践。事实判断仍优先使用 Claude Code release Atom 与可读官方链接。
- AI Governance / Public Legitimacy：`AnthropicAI` 的 Fable 5 重新部署和 `OpenAI` 的官方链接候选进入 topic brief；Anthropic 链接可读，OpenAI 相关链接有 limited 边界，治理结论不混用。
- AI Systems / Automation：`kloss_xyz`、`steipete`、`cellinlab` 等账号出现法律团队知识可查询、构建循环、自动化系统等 field note，适合后续和企业交付趋势互证。
- Product / Growth / GTM 与 Indie Hacking：今天有大量产品发布、增长经验、转推和市场情绪；日报只保留与 agent 工具、分发、成本路由和工作流有关的部分。

### LLM / Frontier Models

- Claude Sonnet 5 进入 Claude Code 默认模型是今天最强 LLM 使用面信号；Simon Willison 的可读文章补充了开发者视角：1M token context、128k 最大输出、adaptive thinking、采样参数变化、tokenizer 变化和真实成本感知，但它是二手解读，事实优先级低于官方 release 与模型页。
- Google 的 Nano Banana 2 Lite / Gemini Omni Flash 是可读官方多媒体模型信号，重点是速度、成本、低延迟草稿、视频编辑和 API/平台可用性。
- Computer use 进入 Gemini 3.5 Flash 说明基础模型正在把“看屏幕、推理、执行动作”纳入内置能力，而不是单独模型或外置 browser bot。

### AI Agent / Agentic Workflow

- Gemini 3.5 Flash computer use、`Strix`、`agency-agents` 和 Claude Code 的后台任务修复共同指向一个方向：agent 产品竞争点正在从单轮生成转向长任务、可安装流程、跨应用执行和安全边界。
- `msitarzewski/agency-agents` 代表 agent 角色资产的跨工具分发：它不是一个单独 app，而是一组可装进 Claude Code、Cursor、Codex、Gemini 等环境的专家角色和流程。
- `OmniRoute` 代表另一类工具层：用户不只想要模型，还想要 provider 路由、fallback、压缩、统一 endpoint 和 MCP/A2A 连接。

### AI Coding / Developer Tools

- Claude Code `v2.1.196` 的组织默认模型、MCP 自批准限制、后台任务恢复、远程会话自动恢复、streaming idle watchdog 和 `/code-review` token 优化，说明 coding agent 的工程重点转向组织治理、长任务可靠性、安全默认值和运行时成本。
- `facebook/astryx` README 说明它是 Meta 内部长大的开源设计系统，提供 150+ 组件、主题、模板和 CLI，并强调人和 agent 使用同一套工具；这是设计系统进入 agent-ready 开发流程的 discovery signal。
- `logto-io/logto` 的 README 强调面向 SaaS 和 AI app 的 OIDC/OAuth 2.1、多租户、企业 SSO、RBAC 和 MCP/agent 架构支持，适合记录为 agent 产品化所需的身份与权限基础设施。

### AI Infrastructure / Open Source

- `Strix` 是今天 GitHub Trending 中最贴近 agent 与工程 infra 的 repo：README 自述动态运行应用、多 agent 渗透测试、验证 PoC、报告、自动修复和 CI/CD 阻断。
- `OmniRoute` 聚焦 AI gateway 与成本路由，但高收益数字必须保留为 README 自述；下一步最小验证是本地跑通 endpoint、provider fallback 和 token 压缩前后成本。
- `allenai/olmocr` 是 PDF/图片文档线性化工具，可把复杂版面转成 Markdown，适合 LLM 训练或数据处理；今天只作为文档处理 infra discovery signal。

### Forward Deployed Engineering / Enterprise AI Deployment

- Google DeepMind 的英国规划工具把数据抽取、政策引用、公众反馈总结、报告草稿、人工最终决策和审计轨迹放在同一条部署链路里；这是公共部门 AI 落地的强样本。
- FDE Hub 的 eval lifecycle 给出另一侧机制：demo 之后必须有检索、忠实性、引用准确率、guardrail、adversarial test、SLO 和持续监控，否则 PoC 很难进入生产。
- Claude Code 的组织默认模型、MCP 安全和 background session 修复属于企业交付系统底层条件：组织需要可治理、可恢复、可审计的 agent 工具，而不是单人本地助手。

### AI Governance / Public Legitimacy

- Anthropic Fable 5 事件的关键不是“模型重新上线”本身，而是模型能力、出口管制、网络安全 safeguard、jailbreak 分级、政府测试和行业标准开始绑定到发布流程。
- 官方材料明确区分 Fable 5 与 Mythos 5 的能力/用途边界，并说明对 cybersecurity classifier 进行了更新；同时承认更强安全余量会带来更多 benign false positive。
- 这条信号适合进入 `ai-governance-legitimacy`：它提供的是制度化发布机制、分类器治理和政府协作框架，而不是单个模型能力 benchmark。

### Financial Agents

- `HKUDS/Vibe-Trading` 是今天最明确的金融 agent discovery signal。README 写到个人交易 agent、影子账户、API/MCP、IM channel runtime、paper-trading tracker 和安全清理。
- 金融方向必须保持高风险边界：GitHub Trending 和 README 只能证明项目上榜与自述能力，不能证明交易收益、合规性、回测质量或生产可用性。

### GitHub Trending / Daily Repos

- `msitarzewski/agency-agents`：跨 Claude Code、Cursor、Codex、Gemini 等工具安装的专家 agent 角色包，价值在“角色/流程资产分发”，不是质量背书。
- `usestrix/strix`：开源 AI 渗透测试工具，README 确认多 agent 编排、动态测试、PoC 验证、报告、自动修复和 CI/CD 集成；安全效果需靶场复现。
- `HKUDS/Vibe-Trading`：个人交易 agent，README 强调交易能力、影子账户、API/MCP、IM 研究投递和近期安全清理；金融风险和合规边界必须单独验证。
- `hasaneyldrm/exercises-dataset`：健身动作结构化数据集/开发者 wizard，和 AI 主线弱相关，只作为数据集上榜记录。
- `facebook/astryx`：Meta 开源设计系统，强调 React/StyleX、150+ 组件、主题、模板、CLI 和 agent-ready 开发方式。
- `diegosouzapw/OmniRoute`：AI gateway，主张统一 endpoint、多 provider、fallback、压缩和 MCP/A2A；成本与 provider 覆盖需实测。
- `allenai/olmocr`：PDF/图片文档转 Markdown 的 OCR/线性化工具，适合作为 LLM 数据处理 infra。
- `logto-io/logto`：面向 SaaS 和 AI app 的认证授权基础设施，覆盖 OIDC/OAuth 2.1、多租户、SSO、RBAC 和 MCP/agent 架构。
- `togatoga/karukan`：Linux/macOS 日语输入法系统，含 llama.cpp 神经假名汉字转换引擎；与本仓主线较弱。
- `Mebus/cupp`：密码画像工具，适合合法渗透测试或取证场景；自动化使用存在滥用风险。

## 3. 来源证据表

| 来源 | 类型 | 原文链接 | 本地归档 | 证据等级 | 备注 |
| --- | --- | --- | --- | --- | --- |
| Claude Code `v2.1.197` | GitHub release Atom | <https://github.com/anthropics/claude-code/releases/tag/v2.1.197> | [atom.md](../raw/2026-07-02/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.197-c9b523c535.atom.md) | official-source | 默认 Claude Sonnet 5，release body 可读但较短。 |
| Claude Code `v2.1.196` | GitHub release Atom | <https://github.com/anthropics/claude-code/releases/tag/v2.1.196> | [atom.md](../raw/2026-07-02/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.196-e8f3ca338f.atom.md) | official-source | 组织默认模型、MCP 安全、后台任务、streaming watchdog 和远程会话修复。 |
| Anthropic Fable 5 redeploy | Official link candidate | <https://www.anthropic.com/news/redeploying-fable-5> | [extracted.md](../raw/2026-07-02/official-link-candidates/anthropicai-2072163884430229756-redeploying-fable-5.extracted.md) | official-source + direct-x | 通过 priority X 链接候选抓取，全文可读。 |
| Gemini computer use | Google DeepMind Blog | <https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/> | [extracted.md](../raw/2026-07-02/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-computer-use-in-gemini-3.5-flash-0ce8c6adc2.extracted.md) | official-source | 内置 computer use 与企业安全边界。 |
| Nano Banana 2 Lite / Gemini Omni Flash | Google DeepMind Blog | <https://deepmind.google/blog/start-building-with-nano-banana-2-lite-and-gemini-omni-flash/> | [extracted.md](../raw/2026-07-02/rss-fulltext/google-deepmind-blog/google-deepmind-blog-start-building-with-nano-banana-2-lite-and-gemini-omni-flash-adbaffb551.extracted.md) | official-source | 多媒体模型开发者入口，厂商 benchmark 边界。 |
| UK planning prototype | Google DeepMind Blog | <https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/> | [extracted.md](../raw/2026-07-02/rss-fulltext/google-deepmind-blog/google-deepmind-blog-unlocking-uk-house-building-with-ai-accelerated-planning-12ceb5f0dc.extracted.md) | official-source | 公共部门 AI 原型，人工最终决策和审计轨迹明确。 |
| FDE eval lifecycle | FDE Hub | <https://www.fdehub.org/p/the-eval-lifecycle> | [extracted.md](../raw/2026-07-02/rss-fulltext/fde-hub/fde-hub-the-eval-lifecycle-what-actually-happens-between-proof-of-concept-and-af0c7a85ff.extracted.md) | secondary-source | 企业交付与生产化评测背景。 |
| Strix | GitHub Trending + README | <https://github.com/usestrix/strix> | [README](../raw/2026-07-02/github-trending-readmes/usestrix__strix.md) | secondary-source | 安全工具高风险，需靶场复现。 |
| Vibe-Trading | GitHub Trending + README | <https://github.com/HKUDS/Vibe-Trading> | [README](../raw/2026-07-02/github-trending-readmes/HKUDS__Vibe-Trading.md) | secondary-source | 金融 agent，非投资建议或效果证明。 |
| X/Twitter direct evidence | twitterapi.io | n/a | [twitterapi-io-results.json](../raw/2026-07-02/twitterapi-io-results.json) | direct-x | API 总体可用，保留 140 条 direct-X。 |

## 4. X/Twitter 覆盖说明

- 本日报通过 `twitterapi.io` 收集 X/Twitter 直接证据，不使用官方 X API，不使用 Exa MCP，不使用登录态浏览器。
- `twitterapi.io` 总体状态为 `ok`；27 个账号均返回 `ok`。其中 `karpathy`、`rryssf_`、`Yangyixxxx`、`zhaogua61654931`、`lidang` 的 `raw_count=0`，不能扩展解释为账号完整无更新。
- 当天保留 direct-X 140 条。高分内容主要集中在 Claude Sonnet 5 / Claude Code、Anthropic Fable 5、agent workflow、AI coding、产品增长、独立开发和中文 AI 产品体验。
- [official-link-candidates.json](../raw/2026-07-02/official-link-candidates.json) 候选数为 4：Anthropic Fable 5 和两个 Matt Pocock GitHub PR 候选可读；OpenAI 相关候选为 `limited`，不写成已读官方正文。

## 5. 不确定性与待验证项

- OpenAI 官方页面今天有 `limited` 边界；只能作为官方发布线索或 direct-X 候选，不能从 metadata 推出机制结论。
- GitHub API release path 为 `skipped`，release 证据来自 Atom feed；Claude Code release body 可读，OpenAI/Codex 等部分 release body 仍为 `limited` 或过短。
- GitHub Trending 是发现线索，不是质量背书。`Strix` 的漏洞验证、`Vibe-Trading` 的交易能力、`OmniRoute` 的 provider/免费 token/压缩收益、`agency-agents` 的角色质量、`Astryx` 的 agent-ready 体验都未本地运行验证。
- direct-X 只证明 API 返回了公开推文文本和链接；模型能力、销售效果、治理判断或产品可用性仍需要官方材料、代码运行或独立评测补证。

## 6. 运行统计

- 新增条目：`seen_added=31`，`seen_total=2686`。
- 高信号条目：10 条。
- 稳定来源：RSS 31/32 成功，RSS fulltext 32/54 ok、22/54 limited；GitHub release sources 7/7 成功，release fulltext 5/10 ok、5/10 limited；GitHub Trending 1/1 成功，10 个 README 文件归档；官方页面 2 ok、2 limited。
- X/Twitter：`twitterapi.io` 成功，direct-X 140 条，27 个账号级状态均为 `ok`。
- official-link candidates：4 条，3 条可读、1 条 limited。
- candidate audit：[reviews/2026-07-02-candidate-audit.md](../reviews/2026-07-02-candidate-audit.md)，将在日报写入后生成并按 missed 候选复核。

### Candidate audit 处理记录

以下条目被 audit 识别为候选时的处理原则：一手全文、agent 工作流、coding agent、企业交付、安全/金融高风险和官方 release 优先；`limited` 全文、历史窗口、泛工程教程、弱相关产品/独立开发社交内容、转推或无官方原文的 direct-X 只记录边界。

- 一手重点源：Claude Code `v2.1.197`、`v2.1.196`、`v2.1.195`、`v2.1.193`、`v2.1.191` 均已在一手重点源和证据表处理；OpenAI 官方线索受 `limited` 边界限制，不写机制结论。
- Anthropic：`Redeploying Fable 5` 已进入今日高信号、治理摘要和证据表；`Claude Sonnet 5` 的事实以 Claude Code release 为主，Simon Willison 文章作为开发者二手解读处理。
- Google DeepMind：`Introducing computer use in Gemini 3.5 Flash`、`Start building with Nano Banana 2 Lite and Gemini Omni Flash`、`Unlocking UK house-building with AI-accelerated planning` 均为可读官方材料，已进入高信号和相关主题摘要。
- FDE / 企业交付：`The Eval Lifecycle: What Actually Happens Between “Proof of Concept” and “Production”` 已进入高信号；其它 FDE 背景文若只提供历史或弱新增，不升级为今日主信号。
- GitHub Trending：`usestrix/strix`、`HKUDS/Vibe-Trading`、`msitarzewski/agency-agents`、`diegosouzapw/OmniRoute`、`facebook/astryx`、`logto-io/logto`、`allenai/olmocr` 已按 README 归档处理；`hasaneyldrm/exercises-dataset`、`togatoga/karukan`、`Mebus/cupp` 弱相关或高风险，保留边界。
- top direct-X：Anthropic / OpenAI / Claude / agent workflow / coding tool 相关 direct-X 已通过 X 摘要或官方候选处理；生活、比赛、健身、泛市场情绪、单纯转推、无可读官方原文的产品夸赞不进入高信号。
- 金融和安全：`Vibe-Trading`、`Strix`、`CUPP` 均明确保留风险边界；任何交易收益、安全效果或漏洞修复能力都需要独立复现。

#### audit 候选逐类覆盖

- OpenAI limited 官方线索：`How ChatGPT adoption has expanded`、`Inside Genebench-Pro`、`Introducing GeneBench-Pro`、`Core dump epidemiology: fixing an 18-year-old bug`、`Mapping Europe’s AI Workforce Opportunity`、`https://openai.com/index/introducing-genebench-pro/` 均已记录为 OpenAI 官方线索，但正文为 `limited`，不写机制结论。
- Hugging Face / eval limited 线索：`ScarfBench: Benchmarking AI Agents for Enterprise Java Framework Migration`、`Featuring Every Eval Ever Results on Hugging Face Model Pages` 为 `limited`，只作为 agent/eval 候选，不高于今天可读的 FDE eval lifecycle。
- Simon Willison / 模型与工具：`Quoting Anthropic`、`What's new in Claude Sonnet 5`、`The AI Compass`、`Have your agent record video demos of its work with shot-scraper video`、`Nano Banana 2 Lite` 已分别作为 Anthropic/Claude 二手解读、AI ethics 背景、agent 可视化交付物或 Google 官方模型发布的补充处理。
- 长期背景 RSS：`Extrinsic Hallucinations in LLMs`、`AI inference is obviously profitable`、`AI GPUs probably live longer than three years`、`Why are cached input tokens cheaper with AI services?`、`The mysterious Hy3 LLM is topping OpenRouter Model Rankings by a large margin`、`An AI agent coding skeptic tries AI agent coding, in excessive detail`、`Claude Haiku 4.5 does not appreciate my attempts to jailbreak it` 是可读背景，但不是今天新增产品/发布主线。
- Antirez / Lucumr / Geohot 背景：`A new era for software testing`、`Distributing LLM inference in DwarfStar`、`Alternatives for the EDIT tool of LLM agents`、`A few words on DS4`、`Redis array type: short story of a long development` 为 limited 或历史背景；`The Coming Loop`、`Dangerous Technology For Americans Only`、`Gaslighting Openness`、`Communities of Not`、`Clanker: A Word For The Machine`、`Liminality`、`Summoning the Demon`、`AI will be massively deflationary` 作为 AI coding、开放性或社会叙事背景处理。
- 产品和工程背景：`Quickly apply LUTs (color grading) with ffmpeg`、`Lean Launch Pad 2026 @ Stanford – Lessons Learned Presentations`、`AI and Teaching – The Brave New World`、`How to Build a Webhook System in Rails Using Sidekiq`、`How to License and Distribute a Private Node Module`、`Build To Learn FAQ`、`Build to Learn vs Build to Earn`、`Commercial vs Internal Products`、`Product Coaching and AI`、`Great Products, Bad Companies`、`Charts of the Week: Cycles, different but the same` 是弱相关产品/工程/创业材料。
- FDE / 运营背景：`Forward Deployed, Episode 6: Market Mechanisms for Agents`、`Forward Deployed, Episode 5: Aligning Agents`、`Sorry, that isn't an FDE`、`DIY, Context layers and the curious growth of the FDE.`、`Agentic Risk Operations`、`We Tested Marketing Incentives to AI Agents. Here's What Happened.`、`Managing Elasticsearch Reindex at Scale: Performance, Reliability, and Observability` 作为趋势背景或 limited 线索处理，今天主信号仍是可读的 `The Eval Lifecycle: What Actually Happens Between “Proof of Concept” and “Production”` 与 Google 规划工具。
- Matt Pocock 候选：`https://github.com/mattpocock/skills/pull/394`、`https://github.com/mattpocock/skills/pull/409`、`One unexpected outcome of this is that I'm now using the wiki as the ONLY place I run Claude Code...`、`/writing-great-skills is quickly becoming my most often-invoked skill`、`Getting sick of setting up third-party services So I built a skill for it /wizard builds...`、`This is just outrageously useful It just had me set up the infra for my personal podcast...`、`I'm working on a new skill which helps you plan enormous chunks of work...`、`I feel like I've developed a clear rationale for when to /compact, when to /clear...`、`Next plan is to make a daily podcast of all the relevant stuff that came in to the wiki...` 均作为个人 wiki、skills 和 workflow direct-X 处理，不代表通用产品能力。
- Claude / Anthropic direct-X：`We’ve received notice that the Department of Commerce has lifted export controls on Claud...`、`RT @claudeai: Introducing Claude Sonnet 5, our most agentic Sonnet yet...`、`RT @AnthropicAI: Claude Fable 5 will be available again globally tomorrow...`、`RT @AnthropicAI: We’ve received notice that the Department of Commerce has lifted export...`、`18 days without Fable felt like a decade...`、`Fable 5 is officially back...`、`🚀Claude Sonnet 5 is now live in Genspark AI Chat Agent, Code Agent and Claw...` 均已由 Anthropic 官方全文或 Claude Code release 覆盖。
- 模型评论 direct-X：`bro GPT-5.6 Sol and GPT-5.5 aren't even comparable...`、`Claude Sonnet 5 is said to be released today...`、`actually worse than Opus 4.8 on benchmarks`、`Notes (and a Pelican) on Claude Sonnet 5 - the new tokenizer makes it ~1.4x more expensiv...`、`Sonnet 5 is the first model to criticize a rule in Claude’s Constitution...`、`UMMMM... so Sonnet 5 has a HIGHER misalignment score than Mythos preview...`、`heavy backend work. go with GPT 5.5` 保留为 direct-X 观点，不作为事实来源。
- Google / computer-use direct-X：`🔥 Google: Gemini Omni Flash is out...`、`Google 昨天发布了Nano Banana 2 lite 的新模型...`、`RT @mayfer: gpt 5.6 at 750 tok/s doing computer use is going to be a little scary` 由 Google 官方全文覆盖。
- agent 落地 direct-X：`You can build your own custom Jarvis, using Cursor, Claude Code or Codex...`、`Most companies are implementing AI agents RANDOMLY for non-coding use cases...`、`RT @rileybrown: Most companies are implementing AI agents RANDOMLY...`、`做 agent 自动化系统时，一个很容易踩的坑...`、`刚下飞机，就迫不及待打开看了一眼项目进度...AI native 的组织...`、`对普通人，飞书 aily 已经足够好了...`、`做了一个探索类小游戏的新实验...Agent 插入到游戏体验里...` 是 direct-X field note，可支撑趋势观察但不能升级为统计结论。
- X MCP / 抓取 / 浏览器自动化：`RT @XDevelopers: Announcing the hosted X MCP...`、`this is a GAME CHANGER for scraping with ai agents...`、`Cloudflare 全家桶又添 Browser Rendering...`、`I built a bot traffic tracker for @DataFast_...` 是工具层 field note；今天没有完整官方原文或实测。
- coding / workflow direct-X：`Was thinking if I should highlight this tweet or not...`、`RT @ajambrosino: what’s a little funny about the “GPT weak on frontend” discourse...`、`看到小耳老师这个skill...ai-website-cloner-template...`、`用Codex + @xiaoerzhan 的claude-skill-web-clone skill 10min 复刻...`、`最近 @Saccc_c 分享了他做个人网站的经历...Hallmark...`、`I've added video support to my "shot-scraper"...`、`RT @thorstenball: There's a lesson here for everybody who thinks that "I'll just use a ch...` 均作为使用侧观察处理。
- 产品增长 / 独立开发 direct-X：`I made $83,701 in June 2026...`、`Monthly reminder: remove your free plan.`、`Can confirm that this is the best decision for my business...`、`A little thread about product life cycles...`、`I built a bot traffic tracker for @DataFast_...`、`What people suspect is indeed true Negative content performs much better...` 只保留为市场和增长情绪，不进入高信号。
- 弱相关或剔除 direct-X：`Stanford dropped their latest course on Parallel Programming, GPU, and CUDA.`、`I think in a few years we'll discover the same foreign funding...`、`As someone who lives in Portugal...`、`Folks I found the reset button.`、`三大运营商如果能有 Anthropic 封号的决心...`、`So the copyright claims around 2013...`、`mental performance has higher throughput...`、`我的 Claude Code 账号也于6 月 29 日寿终正寝了...`、`Today's gym...`、`读张忠谋自传下册...`、`20 day workout streak...`、`字节员工靠炒美股财务自由...`、`啊？！这是真的吗？有杭州推友被封吗？`、`claude 软件里藏了太多秘密了`、`收到 claude 邮件...` 等内容弱相关、不可验证或仅为生活/情绪/传闻。
