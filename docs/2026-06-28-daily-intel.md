# 2026-06-28 Daily Source Intelligence

## 0. 采集范围

- 时间窗口：2026-06-28 日跑；RSS/Atom、GitHub release、GitHub Trending、官方页面按各源最近窗口采集，X/Twitter 使用 `twitterapi.io` 的 24-36 小时窗口。
- 配置来源：[config/watch.md](../config/watch.md)、[config/topics.yaml](../config/topics.yaml)、[config/sources.yaml](../config/sources.yaml)、[config/trends.yaml](../config/trends.yaml)。
- 生成时间：2026-06-28T10:00:00+08:00。
- 原始归档目录：[raw/2026-06-28/](../raw/2026-06-28/)。
- GitHub Trending：1 个 daily trending 源成功，解析 10 个 repo，10 个 Trending description 均保留，10 个 README 文件均写入本地归档；其中 `garrytan/gstack` 的 README 归档内容为 `400: Invalid request`，只能作为 discovery signal。

## 1. 今日高信号

| 等级 | 主题 | 标题/信号 | 来源 | 证据等级 | 链接 | 为什么重要 |
| --- | --- | --- | --- | --- | --- | --- |
| 高 | AI 经济影响 / 工作形态 | Anthropic Economic Index June 2026 继续把 Claude 使用从聊天转向“产出物、节律、自动化程度”衡量 | Anthropic official-link candidate | official-source / fulltext-ok / direct-x | [原文](https://www.anthropic.com/research/economic-index-june-2026-report) / [归档](../raw/2026-06-28/official-link-candidates/anthropicai-2070528961235575278-economic-index-june-2026-report.extracted.md) | 这份报告把 Claude Code、Cowork、chat 和 1P API 拆开看，并增加小时级采样、产出物分类和调查结果；长期看，它把 AI 工作影响的讨论从“谁会被替代”推进到“哪些工作产物正在被委派”。 |
| 高 | Claude Code / 企业运行时 | Claude Code `v2.1.195` 修复插件同意路径、hook matcher、后台任务恢复和远程会话启动检查 | GitHub release Atom | official-source / fulltext-ok | [release](https://github.com/anthropics/claude-code/releases/tag/v2.1.195) / [归档](../raw/2026-06-28/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.195-ce628ff665.atom.md) | 更新集中在权限、插件、后台 agent、daemon socket 和远程容器启动可观测性，说明 coding agent 的竞争继续从“能不能写代码”转向“能不能被企业安全地恢复、授权和审计”。 |
| 中高 | Computer Use / Agent 安全 | Google DeepMind 把 computer use 内置进 `Gemini 3.5 Flash`，并强调敏感动作确认与间接 prompt injection 防护 | Google DeepMind Blog | official-source / fulltext-ok | [原文](https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/) / [归档](../raw/2026-06-28/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-computer-use-in-gemini-3.5-flash-0ce8c6adc2.extracted.md) | computer use 正在从专用能力并入主力模型，面向浏览器、移动端、桌面和企业自动化；安全边界也更像产品系统设计，而不是单纯提示词约束。 |
| 中高 | Agent 安全 / Prompt Injection | Simon Willison 复盘 OpenClaw 邮件注入挑战：约 6,000 次尝试未泄露 secret，但仍不能证明生产安全 | Simon Willison | secondary-source / fulltext-ok | [原文](https://simonwillison.net/2026/Jun/26/hack-my-ai-assistant/#atom-everything) / [归档](../raw/2026-06-28/rss-fulltext/simonwillison/simonwillison-what-happened-after-2-000-people-tried-to-hack-my-ai-assistant-20e226947a.extracted.md) | 这条给 agent 安全提供了真实攻防样本：模型训练可能让注入攻击更难，但不可逆动作仍需要系统级隔离、人工确认和权限边界。 |
| 中高 | Agent Harness / 使用方式 | Armin Ronacher 的 `The Coming Loop` 把 coding agent 外层 harness 描述成“队列、重试、继续会话、换上下文、派给别的机器”的控制循环 | RSS fulltext | secondary-source / fulltext-ok | [原文](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/) / [归档](../raw/2026-06-28/rss-fulltext/lucumr/lucumr-the-coming-loop-387584b75f.extracted.md) | 这不是产品发布，但解释了近期 agent 工程讨论的核心变化：价值不只在单个模型回合，而在模型外部的任务生命周期、验证、继续和终止控制。 |
| 中 | AI 交付 / Eval 生命周期 | FDE Hub 的 eval lifecycle 文章把 POC 到生产的差距描述为类别转换，而不是简单优化 | RSS fulltext | secondary-source / fulltext-ok | [原文](https://www.fdehub.org/p/the-eval-lifecycle-what-actually) / [归档](../raw/2026-06-28/rss-fulltext/fde-hub/fde-hub-the-eval-lifecycle-what-actually-happens-between-proof-of-concept-and-af0c7a85ff.extracted.md) | 它补充了企业 AI 落地趋势：demo 可行之后，真正难点转到真实用户输入、静默错误、指标门槛、评估 harness 和上线 gate。 |
| 中 | Financial Agents / 投研自动化 | `xbtlin/ai-berkshire` 继续在 GitHub Trending 上榜，把价值投资研究做成 Claude Code/Codex skill 集 | GitHub Trending | secondary-source | [repo](https://github.com/xbtlin/ai-berkshire) / [README 归档](../raw/2026-06-28/github-trending-readmes/xbtlin__ai-berkshire.md) | 它把金融投研包装成多 agent checklist、对抗分析和计算校验 workflow，是 Financial Agents 的高相关 discovery signal；README 中的收益展示不能作为投资建议或可复现绩效证据。 |
| 中 | AI Coding / 视觉上下文 | `google-labs-code/design.md` 用 YAML token 和 Markdown rationale 给 coding agent 读取视觉身份 | GitHub Trending | secondary-source | [repo](https://github.com/google-labs-code/design.md) / [README 归档](../raw/2026-06-28/github-trending-readmes/google-labs-code__design.md.md) | 设计规范被改造成 agent 可读、可 diff、可 lint 的上下文格式，说明 AI coding 的输入层正在产品化。 |
| 中 | 文档到 PPT / Agentic 文档流水线 | `hugohe3/ppt-master` 把文档转换为可编辑 PPTX，强调原生形状、动画、讲稿音频和模板跟随 | GitHub Trending | secondary-source | [repo](https://github.com/hugohe3/ppt-master) / [README 归档](../raw/2026-06-28/github-trending-readmes/hugohe3__ppt-master.md) | 它代表“文档到交付物”的 agent workflow：目标不是生成图片，而是生成可继续编辑、可套模板、可演示的办公产物。 |
| 中 | 网站克隆 / Agent 编排模板 | `JCodesMore/ai-website-cloner-template` 把网站逆向、设计 token 抽取、组件规格和并行 builder 包成一套 AI coding agent 模板 | GitHub Trending | secondary-source | [repo](https://github.com/JCodesMore/ai-website-cloner-template) / [README 归档](../raw/2026-06-28/github-trending-readmes/JCodesMore__ai-website-cloner-template.md) | 它显示 AI coding agent 的应用正在从“写一个页面”转向“先抽取规格，再分派并行实现”的流程模板；合规、版权和还原质量需要单独验证。 |

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS 今日仍出现 `Previewing GPT-5.6 Sol: a next-generation model`、`How agents are transforming work`、`OpenAI and Broadcom unveil LLM-optimized inference chip` 等 always-read 条目，但 `rss-items.json` 中 OpenAI Blog fulltext 多数为 `limited`；`OpenAI` 官方 X 链接候选 [https://openai.com/index/previewing-gpt-5-6-sol/](https://openai.com/index/previewing-gpt-5-6-sol/) 也只保存到 challenge HTML。因此今天不能把 GPT-5.6 的细节当作本日新读全文，只能作为连续窗口中的官方发布线索和社交扩散信号。
- Claude Code release Atom 可读度更好：`v2.1.195`、`v2.1.193`、`v2.1.191`、`v2.1.187` 为 `fulltext_status=ok`，`v2.1.190` 为 `limited`。今天最强新增仍是 `v2.1.195`，因为它同时覆盖插件授权、hook matcher、后台任务恢复、daemon socket 和远程会话启动。
- OpenAI Codex release Atom 采到 `0.143.0-alpha.27`、`0.143.0-alpha.26`、`0.142.3`、`0.143.0-alpha.25`、`rust-v0.143.0-alpha.24`，但 release body 均为 `limited`，只能记录版本节奏，不能写功能判断。

### LLM / Frontier Models

- GPT-5.6 相关材料今天的证据边界较弱：本地有 OpenAI 官方社交入口和 RSS 条目，但官方正文归档未达到可读全文状态。可保留的判断是：这条仍是 frontier model、访问层级和治理叙事的核心线索；不能在今天日报里新增未归档细节。
- Google 的 computer use 条目是更可靠的一手全文材料。它说明模型能力进入真实操作环境后，安全策略必须覆盖敏感动作、间接注入、sandbox、访问控制和人工确认。
- Hugging Face、minimaxir、Xe Iaso 等模型/推理成本条目提供背景：vLLM on HF Jobs、ASR leaderboard、OpenRouter Hy3、cached tokens 定价等均有归档或 limited 标记；它们今天不高于 Google/Anthropic/Claude Code 一手材料。

### AI Governance / Public Legitimacy

- Anthropic Economic Index 是今天最清晰的治理/经济影响一手材料：它强调 Claude 使用正在从 chat transcript 转到长时 agentic task、产出物、小时节律和调查感知。边界是它来自 Anthropic 自有产品数据与调查，不等于独立宏观就业因果证明。
- `AnthropicAI` 的 direct-x 还提到美国政府恢复 `Claude Mythos 5` / `Fable 5` 访问；今天没有抓到对应长文，因此只记录为治理/模型访问 field note，不升级为强结论。
- Simon Willison 的 prompt injection 复盘和 Google computer use 安全说明共同指向同一趋势：模型训练变强并不取消产品侧权限、隔离、审计和人工确认。

### AI Agent / Agentic Workflow

- `The Coming Loop` 把近期 agent 工程讨论讲清楚：外层 harness 接管任务生命周期，负责排队、复跑、继续会话、改上下文、转交机器和判断是否真的完成。这对 Memory & Dream、Codex/Claude 使用策略和企业交付系统都相关。
- `The Eval Lifecycle` 补充了交付端的同一件事：demo 到 production 不是修修补补，而是从受控输入进入真实用户输入、错误监测、指标门槛和上线门禁。
- X/Twitter direct-x 中，`sama`、`OpenAI`、`AnthropicAI`、`simonw`、`mattpocockuk`、`gregisenberg`、`EXM7777`、`frxiaobei`、`oviswang` 等都有 agent/模型/工作流相关 field note。它们用于解释扩散和用户关注，不替代官方正文。

### AI Coding / Developer Tools

- Claude Code `v2.1.195` 的 hook matcher 修复尤其具体：带 hyphen 的 matcher 不再误做 substring match，需要 `mcp__brave-search__.*` 才匹配整个 server。这是工具权限字符串规则进入安全面的例子。
- `JCodesMore/ai-website-cloner-template`、`google-labs-code/design.md`、`hugohe3/ppt-master`、`garrytan/gstack` 都是 GitHub Trending 中的 AI coding / agent workflow 信号：一个做网站克隆流程模板，一个做 agent 可读设计规范，一个做文档到 PPT 交付物，一个声称打包 Garry Tan 的 Claude Code 工具栈。`gstack` 的 README 本地内容为 `400: Invalid request`，只能保留为待读候选。
- `levelsio` 关于 Cloudflare 自动化、Claude Code country selector block、IBKR day trading 玩笑，`marclou` 和 `jackfriks` 的 30 天 ship / revenue 结果，都属于独立开发和工具使用观察；不写成官方产品事实。

### Financial Agents

- `xbtlin/ai-berkshire` 是今天 Financial Agents 最相关的 discovery signal：README 明确写到 Claude Code/Codex、四位价值投资方法论、多 agent 并行研究、反偏见机制和 Python 精确计算。
- 关键边界：README 自述的实盘收益图和指数对比不能作为投资建议、可复现回测或风控证明；后续若要进入长期趋势，只能写“金融投研工作流 skill 化”，不能写“投资效果已验证”。
- `levelsio` 的 IBKR day trading tweet 是风险/玩笑，不是金融 agent workflow 证据。

### Forward Deployed Engineering / Enterprise AI Deployment

- FDE Hub 的 eval lifecycle 文章适合更新 FDE/企业交付趋势：真实问题在 demo 之后出现，评估体系、错误分类、门槛和生产反馈才是落地能力。
- Anthropic Economic Index 也能补企业交付趋势：AI 使用的衡量单位从对话变成产出物、自动化程度和工作节律，企业评估 agent 不应只看对话量或 demo 效果。
- 今天没有新的明确 FDE 客户案例；Forward Deployed 系列部分条目为 `limited`，不把它们升级为新一手事实。

### GitHub Trending / Daily Repos

- `simplex-chat/simplex-chat` 是无用户标识符的隐私通信网络，README 确认有移动端、桌面/CLI、群组和开发者集成；它不是 AI 项目，今天只作为隐私通信/身份边界背景。
- `xbtlin/ai-berkshire` 是面向 Claude Code/Codex 的价值投资研究 skill 集，最相关但风险也最高；需要单独验证数据源、计算、回测和合规边界。
- `commaai/openpilot` 是面向 300+ 支持车型的驾驶辅助/机器人操作系统；上榜不是安全背书。
- `IceWhaleTech/CasaOS` 是个人云系统，README 关联 personalized copilot 叙事，但今天更像 self-hosting / personal cloud 背景。
- `ripienaar/free-for-dev` 是开发者免费 tier 列表，服务 devops 和 infra discovery，与 AI 主线弱相关。
- `google-labs-code/design.md` 是 coding agent 可读设计规范，高相关。
- `microsoft/PowerToys` 是 Windows 工具集合，上榜只代表成熟开发者工具关注。
- `hugohe3/ppt-master` 是文档到可编辑 PPTX 的 AI 交付物流水线，高相关。
- `JCodesMore/ai-website-cloner-template` 是 AI agent 网站克隆模板，高相关但有版权/合规边界。
- `garrytan/gstack` 的 Trending description 高相关，但 README 归档内容不可读；只能列为待读候选。

## 3. 来源证据表

| 来源 | 类型 | 原文链接 | 本地归档 | 证据等级 | 备注 |
| --- | --- | --- | --- | --- | --- |
| Anthropic Economic Index report: Cadences | 官方研究报告 | <https://www.anthropic.com/research/economic-index-june-2026-report> | [extracted.md](../raw/2026-06-28/official-link-candidates/anthropicai-2070528961235575278-economic-index-june-2026-report.extracted.md) | official-source / direct-x | 由 `AnthropicAI` tweet 触发官方链接候选，全文可读。 |
| Claude Code v2.1.195 | GitHub release Atom | <https://github.com/anthropics/claude-code/releases/tag/v2.1.195> | [atom.md](../raw/2026-06-28/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.195-ce628ff665.atom.md) | official-source | `fulltext_status=ok`。 |
| Introducing computer use in Gemini 3.5 Flash | 官方博客 | <https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/> | [extracted.md](../raw/2026-06-28/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-computer-use-in-gemini-3.5-flash-0ce8c6adc2.extracted.md) | official-source | `fulltext_status=ok`。 |
| What happened after 2,000 people tried to hack my AI assistant | 博客/二手复盘 | <https://simonwillison.net/2026/Jun/26/hack-my-ai-assistant/#atom-everything> | [extracted.md](../raw/2026-06-28/rss-fulltext/simonwillison/simonwillison-what-happened-after-2-000-people-tried-to-hack-my-ai-assistant-20e226947a.extracted.md) | secondary-source | 有真实挑战边界，不是安全证明。 |
| The Coming Loop | 博客/机制分析 | <https://lucumr.pocoo.org/2026/6/23/the-coming-loop/> | [extracted.md](../raw/2026-06-28/rss-fulltext/lucumr/lucumr-the-coming-loop-387584b75f.extracted.md) | secondary-source | 用于 agent harness / loop 趋势判断。 |
| The Eval Lifecycle | FDE Hub / 交付机制 | <https://www.fdehub.org/p/the-eval-lifecycle-what-actually> | [extracted.md](../raw/2026-06-28/rss-fulltext/fde-hub/fde-hub-the-eval-lifecycle-what-actually-happens-between-proof-of-concept-and-af0c7a85ff.extracted.md) | secondary-source | 用于企业 AI 落地和 eval gate 判断。 |
| GitHub Trending repos | GitHub Trending + README | <https://github.com/trending?since=daily> | [README dir](../raw/2026-06-28/github-trending-readmes/) | secondary-source | 10/10 README 文件写入本地；`gstack` 内容不可读。 |
| X/Twitter direct evidence | twitterapi.io | n/a | [twitterapi-io-results.json](../raw/2026-06-28/twitterapi-io-results.json) | direct-x | API 总体可用，但 `kloss_xyz` failed。 |

## 4. X/Twitter 覆盖说明

- 本日报通过 `twitterapi.io` 收集 X/Twitter 直接证据，不使用官方 X API，不使用 Exa MCP，不使用登录态浏览器。
- `twitterapi.io` 总体状态为 `ok`，但 `manifest.json` 汇总为 `partial`：27 个账号中 `kloss_xyz` 失败；保留 direct-x 113 条。失败账号不能解释为“没有发推”。
- [official-link-candidates.json](../raw/2026-06-28/official-link-candidates.json) 状态为 `ok`，候选数为 2：Anthropic Economic Index 抓取全文成功；OpenAI GPT-5.6 Sol 候选只保存到 HTML challenge，标为受限。
- 高分 direct-x 处理边界：`OpenAI` 与 `sama` 的 GPT-5.6/Sol/Terra 发言保留为官方社交入口和连续窗口信号；`AnthropicAI` Economic Index 由官方正文覆盖；`AnthropicAI` 关于 `Claude Mythos 5` / `Fable 5` 政府访问恢复的 tweet 缺少对应长文，只作治理 field note；`simonw`、`mattpocockuk`、`gregisenberg`、`EXM7777`、`frxiaobei`、`oviswang` 等作为使用方式和市场感知材料，不替代官方证据。

## 5. 不确定性与待验证项

- RSS `dwarkesh-patel` 失败；今天不能据此判断该源无新增。
- OpenAI 官方页面 `openai-news` 和 Claude docs release notes 均为 `limited`；OpenAI Blog 中 GPT-5.6、agents work、Broadcom inference chip 等 always-read 条目也为 `limited`，不能新增强机制判断。
- OpenAI Codex release Atom 5 条均为 `limited`，只能记录版本节奏。
- Claude Code `v2.1.190` 为 `limited`；今天 Claude Code 机制判断来自 `v2.1.195`、`v2.1.193`、`v2.1.191`、`v2.1.187`。
- GitHub Trending 是发现线索，不是质量背书；金融投研、网站克隆、驾驶辅助、PPT 生成、个人云和工具栈项目都需要许可证、可运行性、风险和效果复核。
- `garrytan/gstack` README 本地归档内容为 `400: Invalid request`；后续若要写机制判断，需重新读取 README 或 release/docs。

## 6. 运行统计

- 新增条目：`seen_added=27`，`seen_total=2532`。
- 高信号条目：10 条。
- 稳定来源：RSS 31/32 成功，RSS fulltext 31/53 ok、22/53 limited；GitHub release sources 7/7 成功，release fulltext 4/10 ok、6/10 limited；GitHub Trending 1/1 成功，10 个 README 文件归档；官方页面 2 ok、2 limited。
- X/Twitter：`twitterapi.io` 使用成功但 partial，direct-x 113 条，失败账号 `kloss_xyz`。
- official-link candidates：2 条，Anthropic 成功全文，OpenAI GPT-5.6 Sol 受限。
- candidate audit：[reviews/2026-06-28-candidate-audit.md](../reviews/2026-06-28-candidate-audit.md)，`covered=16`、`missed=49`，missed 已按受限全文、连续窗口背景、弱相关工程/产品材料或 direct-x field note 处理。

### Candidate audit 处理记录

以下条目被 audit 识别为候选但没有全部进入“今日高信号”。处理原则：一手全文、agent 安全、Claude Code 运行时、agent harness、eval/交付控制面和高相关 Trending 项优先；`limited` 全文、重复窗口、泛工程教程、泛产品管理、弱相关独立开发社交内容或没有官方原文的 X 讨论，只记录边界，不提升为高信号。

- official-link-candidate：Anthropic Economic Index 已进入高信号；OpenAI GPT-5.6 Sol 官方链接候选命中 [https://openai.com/index/previewing-gpt-5-6-sol/](https://openai.com/index/previewing-gpt-5-6-sol/)，但本日归档只有 challenge HTML，按受限证据处理。
- OpenAI matched RSS：`Previewing GPT-5.6 Sol`、`How agents are transforming work`、`OpenAI and Broadcom unveil LLM-optimized inference chip` 已在一手重点源边界中处理；`Helping build shared standards for advanced AI`、`How GPT-5 helped immunologist Derya Unutmaz solve a 3-year-old mystery` 为 `limited`，今天不新增机制判断。
- Google DeepMind：`Introducing computer use in Gemini 3.5 Flash` 已进入高信号；`Unlocking UK house-building with AI-accelerated planning` 是公共部门规划应用案例，全文可读但今天不高于 computer use 主线。
- Simon Willison / prompt injection / governance 背景：OpenClaw 复盘已进入高信号；`Quoting Dean W. Ball`、`Quoting Timothy B. Lee`、`Quoting OpenAI`、`Incident Report: CVE-2026-LGTM` 是相关评论或背景，已降级到治理、安全和 coding-agent 背景。
- 模型、推理和 infra 背景：Hugging Face、antirez、Xe Iaso、minimaxir、Sean Goedecke、geohot、Lilian Weng 等条目已归档或标为 limited；今天只作为模型市场、推理成本、编辑工具和 hallucination 背景，不升级为高信号。
- FDE / product / enterprise 背景：`The Eval Lifecycle` 已进入高信号；Forward Deployed 系列、Ted Mabrey、Thomas Otter、SVPG、Ramp Builders、Steve Blank、Keygen、a16z、Palantir 等条目多为 limited、旧窗口或泛产品/工程背景，供 trend 阶段参考。
- top direct-x：`AnthropicAI` 政府访问恢复 tweet 已作为治理 field note；`sama` Sol/Terra tweet 已由 GPT-5.6 边界覆盖；`Hesamation`、`levelsio`、`marclou`、`steipete` 等高分社交项多数是市场情绪、转推、独立开发或弱相关生活内容，不作为官方事实。

## 7. 完成审计

- 日报已写入：本文件。
- candidate audit：已写入 [reviews/2026-06-28-candidate-audit.md](../reviews/2026-06-28-candidate-audit.md)，`covered=16`、`missed=49`；missed 候选已按受限全文、重复窗口、弱相关或 direct-x field note 处理。
- trend report：已写入 [trend/reports/2026-06-28-trend-report.md](../trend/reports/2026-06-28-trend-report.md)。
- enabled trends：9 个 enabled trend 均已检查；8 个写入 `manifest.json`，`claude-tag-identity` 写入 [no-new-signal.json](../trend/raw/2026-06-28/claude-tag-identity/no-new-signal.json)。
- trend check：`python3 scripts/run-trend-stage.py --date 2026-06-28 --check` 返回 `ok=true`。
- trend Phase 2 备注：原始 `codex exec` topic consolidation 在 `claude-tag-identity` 的 no-new-signal 子任务上长时间不返回；本次清理 2026-06-28 date-scoped stale skipped rows 后，使用脚本自身 `run_phase2` 渲染/校验流程和本地确定性 topic body consolidation 完成落盘，最终仍通过非破坏性 verifier。
