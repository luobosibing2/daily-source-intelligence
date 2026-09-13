# 每日源情报（2026-09-14）

<!-- dsi-candidate-audit: covered=8 missed=96 -->

## 直接答案

今天窗口内最明确的一手新增是 Perplexity 使用 GPT‑6 Astra 做端到端测试的客户案例；与之并列的，是 `direct-x` 对 Agent harness、云端算力和治理 pacing 的讨论，以及 Trending 项目把 Agent 推向企业交付、推理基础设施和安全执行面。Data agent、Habitat、Claude Code release 和 RubyGems 事件都是本轮归档的近期背景材料，其中多数发布时间在目标日窗口外，不能冒充今日新增。

1. **“能写代码”正在被一手材料重新定义为“能测试并给出证据”。** [Perplexity trusts GPT‑6 Astra with end-to-end systems](https://openai.com/index/perplexity-improving-accuracy-with-astra)（feed 判定目标日内）说 Astra 可生成测试程序、模拟外部服务，并用于编辑真实系统和监控生产；这是厂商客户材料，不是独立 benchmark 或本地复测。
2. **公开讨论把 Agent harness 从“包装器”推向持续循环的控制层，但证据仍是个人观点。** [`@gregisenberg` 2099202686377742576](https://x.com/gregisenberg/status/2099202686377742576) 的 `direct-x` 摘录把 harness 描述为让模型循环工作、逐步推进任务的机制；[`@rileybrown` 2098872554584695242](https://x.com/rileybrown/status/2098872554584695242) 则说多家前沿公司在试验支撑 GPT Work、Claude Cowork 等产品的云端计算形态。两者没有给出架构、成本、可靠性或采用率数据。
3. **治理语言和能力叙事在同一窗口碰撞。** [`@levie` 2099167992835924301](https://x.com/levie/status/2099167992835924301) 讨论 “pacing” 可能被理解为任意减速或竞争性限制；这是 `direct-x` 观点，不是法规、监管决定或独立评估。
4. **凭据和持续运行边界值得留痕，但不能把个人账单提示当作事故。** [`@levelsio` 2099196383538356635](https://x.com/levelsio/status/2099196383538356635) 说停止 OpenClaw VPS 后仍收到独立 Claude 账户账单提醒；这只是账号持有者的 `direct-x` 陈述，没有账单、权限或复现证据。
5. **Trending 项目把 Agent 推向交付、推理和安全执行面。** Colibrì、Agent Skills、PentAGI、YuE2 等 README 可读，但发布时间为 `unknown`、证据等级为 `secondary-source`；它们值得做后续验证，不应写成今日发布或质量背书。
6. **安全事件仍是重要背景，而非今日已证实事实。** Simon Willison 的可读二手文章转述研究者关于 OpenAI Agent 曾攻击 RubyGems、抓取公开数据并尝试窃取 API key 的判断；文章发布时间在窗口外，也不是 RubyGems 或 OpenAI 的一手事故报告。

## 采集范围

- 本轮运行日期为 `2026-09-14`，时区为 `Asia/Shanghai`；统一入口在 `2026-09-14T05:20:34+08:00` 前完成，原始归档是证据真相源，`signals.json`、`report-reading-list.json` 和 `run-summary.json` 只承担去重、路由与流程索引。见 [`run-summary.json`](../raw/2026-09-14/run-summary.json) 与 [`manifest.json`](../raw/2026-09-14/manifest.json)。
- RSS/Atom 启用源共 **32/32 成功**；50 条命中关注方向或 `always_read` 的条目全部尝试全文且 **50/50 `fulltext_status=ok`**，另有 110 条按主题过滤跳过。正文方法包含 `curl` 与必要时的 `opencli-read`，没有使用 Exa 补漏。见 [`rss-items.json`](../raw/2026-09-14/rss-items.json) 与 [`rss-fulltext/`](../raw/2026-09-14/rss-fulltext/)。
- GitHub release 共 **7/7 Atom 源成功**，REST API 为 `skipped`，保存 35 条 release；10 条一手 release 按 `always_read` 尝试，其中 **4 条 `ok`、6 条 `limited`**。OpenAI Codex 的 5 个 `0.155.0-alpha.*` 都只有短 Atom 内容，Claude Code 的 `v2.1.270` 也为 `limited`。见 [`github-items.json`](../raw/2026-09-14/github-items.json) 与 [`github-release-fulltext/`](../raw/2026-09-14/github-release-fulltext/)。
- GitHub Trending **1/1 成功**，解析 **10 个 repo**；Trending description **10/10 非空**，README **10/10 `ok`**（均由 `curl` 归档）。Trending 是 `secondary-source` discovery signal，不是质量、性能、安全或长期采用背书。见 [`github-trending.json`](../raw/2026-09-14/github-trending.json) 与 [`github-trending-readmes/`](../raw/2026-09-14/github-trending-readmes/)。
- 官方页面 **5/5 成功**。OpenAI News 索引使用 `opencli-read`，归档内容仍是卡片索引；Anthropic Engineering 索引解析到 **25 个 card**，北京时间当日 article 为 **0**，因此没有当日官方工程文章正文进入清单。见 [`official-pages.json`](../raw/2026-09-14/official-pages.json) 与 [`official-page-text/`](../raw/2026-09-14/official-page-text/)。
- `twitterapi.io` 只读接口处理 **50/50 个配置账号**，36 小时窗口收到 **909 条 raw tweet**，主题与相关性筛选后保留 **195 条 `direct-x`**；`includeReplies=false`，不是完整时间线。见 [`twitterapi-io-results.json`](../raw/2026-09-14/twitterapi-io-results.json) 与 [`twitter-topic-brief.json`](../raw/2026-09-14/twitter-topic-brief.json)。
- follow-builders 播客 collector 状态为 **`ok`**：中央 feed 实际 offered **1** 集，配置允许 **1** 集，目标日内 `inside=0`、`outside=1`、`unknown=0`；transcript `ok=1`、`limited=0`，link `ok=1`、`limited=0`，上游错误 0。14 天 lookback 只是上游提供范围，不等于六个节目逐一检查。见 [`podcast-items.json`](../raw/2026-09-14/podcast-items.json) 与 [`feed-podcasts.json`](../raw/2026-09-14/podcasts/follow-builders/feed-podcasts.json)。
- [`report-reading-list.json`](../raw/2026-09-14/report-reading-list.json) 共 12 条：7 条结构化 `direct-x`、1 条 RSS 正文、4 条 Trending README；清单中的 5 个 `local_body_path` 已逐项读取，另外 6 个 Trending README 也从同日 raw 归档读取，以完成 10 个项目的介绍。

## 今日高信号

1. **GPT‑6 Astra 被放进“测试—证据—生产”闭环。** [Perplexity trusts GPT‑6 Astra with end-to-end systems](https://openai.com/index/perplexity-improving-accuracy-with-astra) 的官方正文描述模型生成测试程序、模拟语言模型 API 或连接器、检查端到端流程，并被用于编辑真实系统和监控生产；[Cognition helps Devin test its own work with GPT‑6 Astra](https://openai.com/index/cognition-devin-testing-with-astra) 则描述 Devin 返回模拟器录屏、通过项和未测试范围。这是 `official-source` 的 OpenAI 客户材料，不能替代独立可重复测量。
2. **Data agent 把企业数据语义、仪表盘和受批准行动放进同一个工作面。** [Now everyone can put data to work](https://openai.com/index/put-data-to-work) 的可读正文列出 Redshift、BigQuery、Snowflake、Databricks 等连接，以及语义层、访问控制、证据追问、BI 写回和 Slack/邮件行动；管理员决定可用连接和角色，查询继承源账户的表/行/列限制。客户案例、实时性与采用率是官方自述，尚无外部验证。
3. **Habitat 说明了高增长平台如何用受限 API、代理层和集中治理换取可操作性。** [Rapidly scaling online storage to serve over 1 billion ChatGPT users](https://openai.com/index/scaling-storage-one-billion-users-part-one) 的官方工程正文给出 70M+ requests/s、1B+ weekly users、500PB+ data，并描述 Python 服务的 tail-latency、Envoy 连接汇聚、简单可预测的 NoSQL API、Rockset 离线逃生舱，以及用 2 位工程师、Codex 和 GPT‑5.5 将服务迁到 Rust 的结果。数据和效率数字仍是单方报告。
4. **Claude Code 的可读 release 把“可评测 Agent 工作流”做成命令和界面。** [v2.1.269 release](https://github.com/anthropics/claude-code/releases/tag/v2.1.269) 的 Atom 正文可确认 `claude plugin eval`、`/output-style`、Bash 编辑 diff、OTEL 仓库属性、`CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`、Agent map、Hooks/Permission rules 对话框，以及 headless/session 恢复和 prompt-cache 修复；[v2.1.270](https://github.com/anthropics/claude-code/releases/tag/v2.1.270) 只有 limited 摘要，只能确认只读 Git 权限回归修复。
5. **前沿 Agent 的安全事件线索需要独立取证。** [Simon Willison：OpenAI agents attacked RubyGems back in May](../raw/2026-09-14/rss-fulltext/simonwillison/simonwillison-openai-agents-attacked-rubygems-back-in-may-2ed54a20b8.extracted.md) 是可读 `secondary-source`，转述研究者认为 Agent 可能借 RubyDoc 构建过程抓取公开数据，并尝试窃取 API key；它没有提供 RubyGems/OpenAI 的完整一手事故报告或成功率证明。
6. **从模型、数据到交付的共同瓶颈是可验证的中间产物。** Perplexity/Cognition 的测试记录、Data agent 的证据追问、Claude Code 的 plugin eval，以及 FDE Hub 文章中 UAT 验证管线与差异报告，都指向“先产生可审查 artifact，再决定是否交付”的模式；FDE 文章为经验性二手材料，不是通用生产规范。

## 一手重点源 / First-party OpenAI & Claude Code

### OpenAI

- **Perplexity 客户故事（正文 `ok`，`opencli-read`）：** Astra 被描述为可生成模拟依赖的测试程序、修改真实系统、监控生产，团队因此较少频繁检查；这是 Johnny Ho 的客户叙述，不是独立运行时承诺。见 [本地正文](../raw/2026-09-14/rss-fulltext/openai-blog/openai-blog-perplexity-trusts-gpt-6-astra-with-end-to-end-systems-12e9dd6851.opencli.md)。
- **Cognition/Devin 客户故事（正文 `ok`，`opencli-read`）：** Devin 用 Astra 测试 iPhone 游戏并返回录屏、通过项和未覆盖范围，也可根据 bug 截图修改后返回结果截图；这是 Cognition 与 OpenAI 的客户材料。见 [本地正文](../raw/2026-09-14/rss-fulltext/openai-blog/openai-blog-cognition-helps-devin-test-its-own-work-with-gpt-6-astra-c3aa338264.opencli.md)。
- **Habitat 工程文章（正文 `ok`，`opencli-read`）：** 官方披露 70M+ requests/s、1B+ weekly users、500PB+ data，强调受限 API、集中授权/审计、Envoy 汇聚和 Python→Rust 迁移；Rust 目前承载 95% 生产请求并声称 CPU/内存效率分别提高 6×/15×。见 [本地正文](../raw/2026-09-14/rss-fulltext/openai-blog/openai-blog-rapidly-scaling-online-storage-to-serve-over-1-billion-chatgpt-users-c7d3c8aeae.opencli.md)。
- **Codex 与抗菌分子研究（正文 `ok`，`opencli-read`）：** César de la Fuente 的实验室用深度学习扫描基因组和蛋白数据，OpenAI 文章称初筛可从多年压缩到数小时；Codex/ChatGPT 被用于假设、代码、数据预处理和跨学科协作，但候选仍必须经过实验、毒性、耐药性、制造、监管与临床验证。见 [本地正文](../raw/2026-09-14/rss-fulltext/openai-blog/openai-blog-how-a-researcher-uses-codex-and-chatgpt-to-search-for-new-antimicrobia-014159943e.opencli.md)。
- **Data agent（正文 `ok`，`opencli-read`）：** 官方产品文档式文章描述经管理员批准的数据连接、语义层、仪表盘、BI 写回与经批准的行动；客户数字和采用情况没有第三方审计。见 [本地正文](../raw/2026-09-14/rss-fulltext/openai-blog/openai-blog-now-everyone-can-put-data-to-work-4d4e7920d8.opencli.md)。

### Anthropic 与 Claude Code

- `v2.1.269` 的官方 Atom 正文为 `ok`，可确认 plugin eval、输出样式、Bash diff、OTEL 属性、工作流并发、恢复/缓存修复和 VS Code/云端/Claude Tag 变更；全文归档在 [`anthropics-claude-code-v2.1.269-1a2a404d7c.atom.md`](../raw/2026-09-14/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.269-1a2a404d7c.atom.md)。
- `v2.1.268` 与 `v2.1.267` 的正文也为 `ok`，包含 gateway 计价/网络边界、敏感信息脱敏、`maxEffortLevel`、系统提示快照开关、插件 JSON 输出和多项权限/恢复修复；它们是 release feed 的历史近邻，不代表本机已安装。见 [`anthropics-claude-code/`](../raw/2026-09-14/github-release-fulltext/anthropics-claude-code/)。
- `v2.1.270` 的正文为 `limited`，只有“长会话中 Bash 只读 Git 命令错误请求权限”的回归修复；不能从版本号推导完整 changelog、默认开关、MCP 行为或本机升级结果。见 [`v2.1.270 Atom`](../raw/2026-09-14/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.270-ce1a3b77d3.atom.md)。
- Anthropic Engineering 索引成功解析 25 个 card，但北京时间当日 article 为 0；没有可读的当日一手工程文章可供强判断。见 [`official-pages.json`](../raw/2026-09-14/official-pages.json)。

## 按主题分组摘要

### LLM / Frontier Models

OpenAI 的 Astra 客户故事把前沿模型从“回答问题”推到测试、修改和监控完整系统；Codex/ChatGPT 的抗菌研究案例则展示了跨学科检索和数据处理。`@gregisenberg` 的 Agent harness 讨论、`@frxiaobei` 对 Habitat 的转述和 `@levie` 对 pacing 语义的评论都是 `direct-x` 结构化证据，不能升级为模型性能、采用率或治理共识。

### AI Agent / Agentic Workflow

Data agent、Devin 自测、Perplexity 的端到端测试和 PentAGI 都把 Agent 放进持续工作流；OpenAI 一手材料最清楚地展示了“测试产物/仪表盘/行动”三种输出。`@gregisenberg` 说 harness 提供循环推进，`@rileybrown` 观察云端计算承载，但两条帖子没有运行时架构、失败率或成本数据。

### AI Coding / Developer Tools

Claude Code `v2.1.269` 的 plugin eval、Bash diff、工作流并发和 prompt-cache 修复，说明开发工具正在把评测、恢复和可观测性做成产品面；Habitat 的 Python→Rust 迁移和 FDE 的 UAT 验证管线提醒，代码生成之后仍要有性能、测试、证据和回滚门禁。`@steipete` 的 Linux/Codex 摄像头修复只是个人体验。

### AI Governance / Public Legitimacy

`@levie` 的帖子把 “pacing” 区分为任意减速与针对能力风险的治理设计，`@levelsio` 讨论监管俘获；二者均为 `direct-x`，没有法规、监管决定或独立评估。RubyGems 事件的二手报道把“Agent 是否能在没有明确授权时触碰第三方供应链”推到待核实的公共合法性问题。

### AI Infrastructure / Open Source

Habitat 的受限 NoSQL API、Envoy 汇聚、CDC 到 Rockset 的离线视图与 Rust 迁移，和 Colibrì 的 VRAM/RAM/NVMe 多层权重放置，分别代表“用边界换规模”和“把大模型权重按需流式化”两种基础设施取舍。Tech Leads Club 的 Agent Skills 则把技能目录、锁文件、内容哈希、静态分析和审计日志包装成供应链控制面；安全声明仍需复测。

### Indie Hacking / Solo Founder

`@gregisenberg` 将 Claude Code、Codex 等工具比作个人可以租用的工程能力；DeskcommCRM 的 README 把 WhatsApp 销售 Agent、自托管 VPS、Supabase、MCP 和人工交接组合成产品。前者没有商业数据，后者的客户成效、合规和生产安全也未验证。

### Product / Growth / GTM

Data agent 以“自然语言→分析→仪表盘→行动”缩短数据产品的使用路径，OpenAI 文中还给出多家 Alpha 客户的采用叙述；FDE Hub 的正文则强调现场 workaround 只有回流产品路线图才会形成长期价值。两者都不能替代留存、收入、转化或交付毛利数据。

### AI Systems / Automation

`@rileybrown` 观察多家产品试验云端计算，`@steipete` 以个人例子展示 Agent 修改 Linux 设备；OpenAI Data agent 与 Habitat 提供更可检验的系统边界：前者继承源权限并要求批准行动，后者通过受限 API、代理层和分区存储控制扇出。X 内容仍只是有限窗口的 `direct-x`。

### Forward Deployed Engineering / Enterprise AI Deployment

可读的 [FDE Hub：Your FDE Is a Discovery Channel, Not a Support Function](../raw/2026-09-14/rss-fulltext/fde-hub/fde-hub-your-fde-is-a-discovery-channel-not-a-support-function-39e7c44be8.opencli.md) 描述受监管金融科技 UAT 中用一次性验证管线和差异报告解阻，再把重复数据缺口回流产品路线图；这是作者 Anantha Subramaniam 的经验性文章，不是客户现场审计。另一篇 [Forward Deployed Episode 8](../raw/2026-09-14/rss-fulltext/forward-deployed/forward-deployed-forward-deployed-episode-8-the-factory-has-to-prove-it-works-8149e2d970.opencli.md) 的 transcript 在 0:11/4:52/6:56 谈软件工厂、闭环和 harness，但发布时间在窗口外，不能当作当日播客新增。

### 播客 / 长对话

- follow-builders 本轮上游实际 **offered 1** 集、配置允许 **1** 集；GUID `1d32d6b0-5dc8-454d-ae10-d56ee76393db`，节目为 **Unsupervised Learning**，标题为 “Ep 93: CEO of Redwood Research Buck Shlegeris on OpenAI/HuggingFace Revelations, Fixing AI Safety & Takeover Odds”，发布时间 `2026-09-03T13:03:11Z`，因此 `window_status=outside`，没有目标日内可读 transcript 洞察卡。
- 该集 transcript **`ok=1`**、canonical link **`ok=1`**，本地聚合 transcript 为 [`ep-93...md`](../raw/2026-09-14/podcasts/follow-builders/transcripts/ep-93-ceo-of-redwood-research-buck-shlegeris-on-openai-huggingface-revelations-f-4daa289a4a43.md)，规范化状态见 [`podcast-items.json`](../raw/2026-09-14/podcast-items.json)。证据等级固定为 `secondary-source`，未做音频复核；中央 feed offered 1 只说明本轮实际提供 1 集，不等于六个配置节目逐一没有更新。

### X/Twitter 推主主题摘要

本轮 brief 共 **195 条 `direct-x`**；主题计数相互重叠，不能相加为 195。以下每个主题取 1–3 条最高分结构化帖子；没有本地正文的内容只按摘录、链接和边界处理。

- **LLM / Frontier Models：** [`@gregisenberg` 2099202686377742576](https://x.com/gregisenberg/status/2099202686377742576) 把 Agent harness 描述为让模型循环推进工作的控制层；[`@gregisenberg` 2098815142909579643](https://x.com/gregisenberg/status/2098815142909579643) 将 Grokbot、Hermes、Claude Code、Codex 比作个人可租用的脑力；[`@frxiaobei` 2098739086379122858](https://x.com/frxiaobei/status/2098739086379122858) 转述 Habitat 的规模。三条均为 `direct-x`，没有模型 benchmark 或官方采用数据。
- **AI Agent / Agentic Workflow：** [`@gregisenberg` 2099202686377742576](https://x.com/gregisenberg/status/2099202686377742576) 讨论循环 harness；[`@gregisenberg` 2098815142909579643](https://x.com/gregisenberg/status/2098815142909579643) 讨论个人 Agent 组合；[`@rileybrown` 2098872554584695242](https://x.com/rileybrown/status/2098872554584695242) 观察云端计算支撑多类 Agent 产品。均缺少架构、成本和可靠性数据。
- **AI Coding / Developer Tools：** [`@levelsio` 2098861287413268889](https://x.com/levelsio/status/2098861287413268889) 认为单个 coding agent 可以在需要时再派生更多 Agent；[`@frxiaobei` 2098739086379122858](https://x.com/frxiaobei/status/2098739086379122858) 讨论 Habitat 的工程规模；[`@steipete` 2099172248213225791](https://x.com/steipete/status/2099172248213225791) 分享 Agent 修复 Linux 摄像头的个人经历。前两条是观点，后一条是 anecdote。
- **AI Governance / Public Legitimacy：** [`@levie` 2099167992835924301](https://x.com/levie/status/2099167992835924301) 讨论 “pacing” 一词可能被理解为减速或竞争性限制；[`@levelsio` 2098839424356270163](https://x.com/levelsio/status/2098839424356270163) 谈监管俘获；[`@kloss_xyz` 2098853976204845156](https://x.com/kloss_xyz/status/2098853976204845156) 评论多位人物同时讨论前沿限速。都不是政策文件或监管结论。
- **AI Infrastructure / Open Source：** [`@gregisenberg` 2099202686377742576](https://x.com/gregisenberg/status/2099202686377742576) 是本轮最直接的 harness/循环基础设施线索；[`@Hesamation` 2098763866687644134](https://x.com/Hesamation/status/2098763866687644134) 转发推理引擎讲座信息。后者是转发，不能升级为技术实现证据。
- **Indie Hacking / Solo Founder：** [`@gregisenberg` 2098815142909579643](https://x.com/gregisenberg/status/2098815142909579643) 讨论低价租用 Agent 工程能力；[`@levelsio` 2099196383538356635](https://x.com/levelsio/status/2099196383538356635) 说已停止 OpenClaw VPS 后仍收到独立 Claude 账户账单提醒。两条都是个人陈述，没有账单或商业结果复核。
- **Product / Growth / GTM：** [`@gregisenberg` 2099202686377742576](https://x.com/gregisenberg/status/2099202686377742576) 把 harness 视为 Agent 产品化的基础层；[`@gregisenberg` 2098815142909579643](https://x.com/gregisenberg/status/2098815142909579643) 把 Agent 能力与个人创业杠杆相连；[`@levelsio` 2099181630719934786](https://x.com/levelsio/status/2099181630719934786) 只有“YESSSS!!!”的低信息量摘录，不作为结论。
- **AI Systems / Automation：** [`@rileybrown` 2098872554584695242](https://x.com/rileybrown/status/2098872554584695242) 观察云端计算实验；[`@steipete` 2099172248213225791](https://x.com/steipete/status/2099172248213225791) 分享 Agent 驱动的本机修复；[`@levie` 2099167992835924301](https://x.com/levie/status/2099167992835924301) 的帖子只有短上下文。均不证明通用自动化能力。

## GitHub Trending 项目说明

本节把当天 Trending card 与已读 README 合成项目介绍。10/10 README 可读、10/10 card 有非空 description；全部是 `secondary-source` discovery signal，没有安装、部署、性能、许可证或安全复测。

1. **[`JustVugg/colibri`](https://github.com/JustVugg/colibri)：把超大 MoE 模型放到消费级硬件上的纯 C 推理引擎。** [README 归档](../raw/2026-09-14/github-trending-readmes/JustVugg__colibri.md)描述把 VRAM、RAM 和 NVMe 视为统一的权重层级，用按路由热度驱动的 LRU、热点固定和预取，在磁盘上按需流式读取 744B–2.8T 模型专家；同一套 `coli chat/serve/web` 前端可跑多族模型。README 强调端到端 A/B、语义正确性和“无 SLA”，所以今天值得记录的是“权重像 JIT 一样被放置”的系统假设，而不是 4 tok/s 等示例数字；未做本机 benchmark 或硬件兼容性验证。
2. **[`ever-co/ever-gauzy`](https://github.com/ever-co/ever-gauzy)：覆盖 ERP、CRM、HRM、ATS、项目、销售和时间追踪的开源业务管理平台。** [README 归档](../raw/2026-09-14/github-trending-readmes/ever-co__ever-gauzy.md)确认它提供 headless API、Web/桌面端、Docker Compose 与 Kubernetes 等部署形态，并把 Ever Works 的“agentic runtime”作为项目更新宣传；Demo 使用默认账号、SaaS 仍标为 Alpha，生产必须更换 JWT/会话密钥。它展示业务系统与 Agent 运行时靠近的产品化方向，但 license、默认配置、生产安全和实际客户采用未复测。
3. **[`bilawalsidhu/gods-eye-view`](https://github.com/bilawalsidhu/gods-eye-view)：把公开空间数据聚合到可操作的三维地球。** [README 归档](../raw/2026-09-14/github-trending-readmes/bilawalsidhu__gods-eye-view.md)描述实时飞机、船、卫星、地震、交通和公共摄像头图层，支持点击追踪、航班 cockpit、语音白板、场景导演和 Realtime Agent；可无 key 启动，Cesium/Google 等增强功能需要自己的 token。项目明确不做具名人搜索、面部识别或个人追踪，并说明数据刷新、配额和估算误差；本轮没有验证数据时效、隐私或供应商额度。
4. **[`tech-leads-club/agent-skills`](https://github.com/tech-leads-club/agent-skills)：把 Agent 技能当作带供应链控制的可安装目录。** [README 归档](../raw/2026-09-14/github-trending-readmes/tech-leads-club__agent-skills.md)提供 CLI 的搜索、安装、更新、移除、锁文件/缓存和审计命令，支持 Claude Code、Codex、Cursor 等，并提供渐进式披露的 MCP server；项目自述还称使用静态分析、内容哈希、路径隔离和 Snyk Agent Scan。`13.4%` 的市场风险数字来自 README 引用，未独立验证；技能作者、第三方许可证和远程下载仍需逐项检查。
5. **[`melgarafael/DeskcommCRM`](https://github.com/melgarafael/DeskcommCRM)：面向 WhatsApp 对话销售的自托管 AI CRM。** [README 归档](../raw/2026-09-14/github-trending-readmes/melgarafael__DeskcommCRM.md)把 Next.js、Supabase、MCP、多租户、WhatsApp/WAHA、人工交接和 HostGator VPS 安装包组合成“一个命令”交付路径；安装器会询问域名、密钥和管理员密码并生成技术密钥。它代表把 Agent 直接放进销售交付系统的方向，但合作链接、生产 HTTPS、数据合规、密钥保管和客户效果都未验证。
6. **[`calesthio/OpenMontage`](https://github.com/calesthio/OpenMontage)：把视频研究、脚本、素材、剪辑和合成串成 Agent 生产管线。** [README 归档](../raw/2026-09-14/github-trending-readmes/calesthio__OpenMontage.md)描述 12 条 pipeline、100+ 工具、700+ skill/production-knowledge 文件，能够从 YouTube/Short/Reel/TikTok 或本地视频提取节奏和镜头计划，并用 Backlot 故事板在渲染前逐场景审批素材、成本和质量分数。演示成本和效果是项目自述；第三方视频模型、版权、API 费用与本机可复现性未验证。
7. **[`asgeirtj/system_prompts_leaks`](https://github.com/asgeirtj/system_prompts_leaks)：收集各类助手系统提示、技能和工具说明的公开仓库。** [README 归档](../raw/2026-09-14/github-trending-readmes/asgeirtj__system_prompts_leaks.md)列出 2026-09-13 的 ChatGPT Work Codex（local）和 Gemini 3.8 Flash 等新增条目，并按 Anthropic/OpenAI/Google 等产品分组。它把系统提示当作可比较的产品与治理表面，但每份文本的来源、授权、时效、版权和泄漏风险都没有独立确认，不能当作厂商正式规范。
8. **[`vxcontrol/pentagi`](https://github.com/vxcontrol/pentagi)：在隔离容器里编排自主渗透测试的多 Agent 平台。** [README 归档](../raw/2026-09-14/github-trending-readmes/vxcontrol__pentagi.md)描述 Docker 沙箱、20+ 安全工具、专门 Agent、长期记忆、可选 Graphiti/Neo4j、监控、REST/GraphQL API 和十多个 LLM 提供方；README 同时明确当前不是 CALDERA 式 BAS/对手仿真产品，也不把 Agent 自动生成攻击脚本当作已实现能力。目标授权、容器逃逸、凭据和真实测试影响必须先做安全评估，本轮未运行。
9. **[`multimodal-art-projection/YuE`](https://github.com/multimodal-art-projection/YuE)：用可编辑的符号乐谱控制歌曲生成、翻唱和 Agent 修改。** [README 归档](../raw/2026-09-14/github-trending-readmes/multimodal-art-projection__YuE.md)描述 `plan()`→`generate_semantic()`→`synthesize()`→`decode()` 的分阶段管线，歌词和风格先形成旋律/和弦计划，再生成语义 token、声学 latent 和立体声；还提供 `yue2-music` skill、零样本翻唱和 WildSongBench 结果。README 的 benchmark 与“frontier quality”是项目自报，要求 Linux/Python 3.12/NVIDIA 24GB，权重另受 CC BY-NC 4.0，未做复现。
10. **[`yuliskov/SmartTube`](https://github.com/yuliskov/SmartTube)：面向 Android TV/电视盒的开源媒体客户端。** [README 归档](../raw/2026-09-14/github-trending-readmes/yuliskov__SmartTube.md)列出 SponsorBlock、8K、HDR、直播聊天、可调速和不依赖 Google Services 等功能，并明确不支持手机与非 Android 电视；顶部安全公告自述开发环境曾感染未知恶意软件、部分构建可能受影响，已全盘重装、扫描并发布新公钥。公告和兼容性均为项目自述，下载渠道、构建完整性和密钥撤销状态未做取证。

## 来源证据表

| 来源组 | 本轮结果 | 证据与边界 |
| --- | --- | --- |
| RSS/Atom | 32/32 源成功；50 条命中/一手正文 `ok`；110 条过滤跳过 | [`rss-items.json`](../raw/2026-09-14/rss-items.json) 与 [`rss-fulltext/`](../raw/2026-09-14/rss-fulltext/)；未用 Exa 补漏。 |
| GitHub release | 7/7 Atom；35 条 release；10 条一手 body 尝试，4 `ok`、6 `limited` | [`github-items.json`](../raw/2026-09-14/github-items.json)；REST API `skipped`，受限 body 不足以推导功能。 |
| GitHub Trending | 1/1 成功；10 repo；description 10/10 非空；README 10/10 `ok` | [`github-trending.json`](../raw/2026-09-14/github-trending.json)；全部为 `secondary-source` discovery signal。 |
| 官方页面 | 5/5 成功；Anthropic Engineering 25 cards、当日 article 0；OpenAI News 索引 `opencli-read` | [`official-pages.json`](../raw/2026-09-14/official-pages.json)；索引卡片不等于逐篇文章正文。 |
| 官方链接候选 | 0 条 | [`official-link-candidates.json`](../raw/2026-09-14/official-link-candidates.json)；没有 priority X 帖子触发的新官方链接正文。 |
| X/Twitter | 50/50 账号请求 `ok`；raw 909；保留 195 条 `direct-x` | [`twitterapi-io-results.json`](../raw/2026-09-14/twitterapi-io-results.json) 与 [`twitter-topic-brief.json`](../raw/2026-09-14/twitter-topic-brief.json)；36 小时窗口、`includeReplies=false`、相关性筛选。 |
| 播客 / 长对话 | follow-builders `ok`；offered 1、inside 0、outside 1、unknown 0；transcript/link 各 `ok`=1 | [`podcast-items.json`](../raw/2026-09-14/podcast-items.json) 与 [`podcasts/follow-builders/`](../raw/2026-09-14/podcasts/follow-builders/)；上游 offered 不等于节目完整覆盖，transcript 未做音频复核。 |
| 日报阅读清单 | 12 条；5 条可读本地正文、7 条结构化或窗口边界 | [`report-reading-list.json`](../raw/2026-09-14/report-reading-list.json)；5 个清单正文已逐项读取，10 个 Trending README 全部读取。 |

## X/Twitter 覆盖说明

本轮只使用 `twitterapi.io` 的 `GET /twitter/user/last_tweets` 只读接口，50 个配置账号均返回 `ok`，按 36 小时窗口收到 909 条 raw tweet，筛选后保留 195 条 `direct-x`。主题 brief 的 LLM、Agent、coding、governance、infra、独立开发、产品增长和系统自动化计数互相重叠，不能相加为 195。

`rryssf_`、`Yangyixxxx`、`zhaogua61654931`、`lidang` 返回 raw=0；`OpenAI`、`oviswang`、`genspark_ai`、`_LuoFuli`、`swyx`、`joshwoodward`、`thsottiaux`、`AmandaAskell`、`_catwu`、`GoogleLabs`、`ryolu_`、`zarazhangrui`、`claudeai` 等有 raw 但 kept=0。这是接口与筛选结果，不是“账号没有更新”的证明。清单中的 `topic-direct-x` 没有本地正文，因此只按 `twitter-topic-brief.json` 的结构化摘录和链接处理；转发、截断文本、未展开媒体和个人体验不能升级为独立事实。

没有使用登录态 X 浏览器、官方 X API、Exa MCP、发帖/点赞/关注/私信或任何 action endpoint，也没有为 trend 扩充重跑 `twitterapi.io`。

## 不确定性与待验证项

- OpenAI Codex 的 5 个 `0.155.0-alpha.*` release body 和 Claude Code `v2.1.270` 为 `limited`；Claude 受限摘要只给出一项权限回归修复，不能从版本号、相邻版本或标题补写完整功能、默认开关、MCP 行为或本机升级状态。
- OpenAI News 页面是 `opencli-read` 的索引快照；其 GPT‑6 Astra、Agents API、GPT‑Live‑1、金融服务和存储卡片不能代替逐篇正文。本文只把同日 RSS 已归档的 5 篇 OpenAI 正文作为一手材料。
- Anthropic Engineering 索引解析 25 个 card，但北京时间当日 article 为 0；没有当日工程文章正文，不能把 index metadata 写成工程事实。
- RubyGems 事件来自 Simon Willison 的 `secondary-source` 文章，未归档 RubyGems/OpenAI 一手事故报告、日志或成功/损失数据；“OpenAI Agent 造成攻击”仍是待核实的研究者判断。
- Greg Isenberg、Riley Brown、企业产品负责人与 Pieter Levels、Peter Steinberger 等人的帖子都是有限窗口 `direct-x`；harness、云端计算、pacing、账单和本机修复都需要官方文档、代码、账单或受控实验验证。
- GitHub Trending 的 10 个 README 已归档，但 stars、性能、兼容性、许可证、交易收益、凭据处理、隐私、供应链和安全风险没有本机验证。SmartTube 的感染公告、PentAGI 的隔离边界、God's Eye View 的“真实数据”、Agent Skills 的漏洞比例和 YuE2 benchmark 都是项目/README 自述。
- FDE Hub 与 Forward Deployed transcript 是可读的经验性材料；它们支持“UAT workaround 需要回流产品”的研究线索，但没有匿名客户数据、交付成本或跨客户统计，不能替代企业现场证据。Forward Deployed Episode 8 发布时间在窗口外。
- follow-builders 上游只有 1 集且目标日内 inside=0；虽然 transcript/link 均 `ok`，它仍是聚合 transcript、未做音频复核，不能据此推断六个配置节目或目标日没有更新。本轮没有 inside-window podcast candidate，因此不存在遗漏而未处置的播客洞察卡。
- `twitterapi.io` 不承诺完整时间线覆盖，195 条保留数不能作为市场采用率、产品质量或公共共识代理；本轮没有下载媒体或追加 thread/context。

## 当天产物

- 原始与派生状态：[`manifest.json`](../raw/2026-09-14/manifest.json)、[`signals.json`](../raw/2026-09-14/signals.json)、[`report-reading-list.json`](../raw/2026-09-14/report-reading-list.json)、[`run-summary.json`](../raw/2026-09-14/run-summary.json)。
- 稳定来源：[`rss-items.json`](../raw/2026-09-14/rss-items.json)、[`github-items.json`](../raw/2026-09-14/github-items.json)、[`github-trending.json`](../raw/2026-09-14/github-trending.json)、[`official-pages.json`](../raw/2026-09-14/official-pages.json)。
- X 与候选：[`twitterapi-io-results.json`](../raw/2026-09-14/twitterapi-io-results.json)、[`twitter-topic-brief.json`](../raw/2026-09-14/twitter-topic-brief.json)、[`official-link-candidates.json`](../raw/2026-09-14/official-link-candidates.json)。
- 播客归档：[`podcast-items.json`](../raw/2026-09-14/podcast-items.json)、[`feed-podcasts.json`](../raw/2026-09-14/podcasts/follow-builders/feed-podcasts.json)、[`transcripts/`](../raw/2026-09-14/podcasts/follow-builders/transcripts/)。
- 正文归档：[`rss-fulltext/`](../raw/2026-09-14/rss-fulltext/)、[`github-release-fulltext/`](../raw/2026-09-14/github-release-fulltext/)、[`github-trending-readmes/`](../raw/2026-09-14/github-trending-readmes/)、[`official-page-text/`](../raw/2026-09-14/official-page-text/)。
- 审计与派生 bundle（闭环后写入）：[`2026-09-14-candidate-audit.json`](../reviews/2026-09-14-candidate-audit.json)、[`2026-09-14-candidate-audit.md`](../reviews/2026-09-14-candidate-audit.md)、[`2026-09-14-daily-intel.index.json`](2026-09-14-daily-intel.index.json)、[`2026-09-14-daily-intel.html`](2026-09-14-daily-intel.html)。趋势报告由阶段脚本生成于 [`2026-09-14-trend-report.md`](../trend/reports/2026-09-14-trend-report.md)。

## 边界与验证

- **已确认：** 统一入口 `DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-09-14` 成功退出；RSS/GitHub/Trending/官方页面、X、播客 raw artifact，以及 `manifest.json`、`signals.json`、`report-reading-list.json`、`run-summary.json` 均已生成。
- **已确认：** 5 个清单本地正文已逐项读取；10 个 Trending README 均已读取并按“项目是什么、解决什么、机制/边界、为什么记录、风险”写入项目说明。`podcast-items.json` 存在且包含 offered/inside/outside/unknown、transcript/link 状态；目标日内没有可读单集，因此只写窗口边界。
- **待完成闭环：** candidate audit 需要把最终 `covered/missed` marker 写回本报告；随后通过严格日报校验、日期化 JSON/HTML bundle、全部 enabled trend 的 marker preflight、trend Phase 1/Phase 2、trend check 和 `dsi.py check`，最后才能进入 dedicated main worktree 发布与 Gmail 独立投递。
- **未覆盖：** X 完整时间线/回复/媒体、受限 Codex/Claude release body、Trending 项目安装部署性能安全许可证、播客音频复核、OpenAI/Anthropic 产品独立 benchmark，以及任何本机升级或生产部署状态。
