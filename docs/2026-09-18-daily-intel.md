# 每日源情报（2026-09-18）

<!-- dsi-candidate-audit: covered=15 missed=99 -->

## 直接答案

本轮统一入口为 `DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-09-18`。采集器向 `state/seen.json` 新增 41 条去重记录；派生阅读清单有 22 条信号，其中 16 条在北京时间目标窗口内、6 条是时间未知边界，7 条清单条目有可读本地正文。今天最值得跟踪的是：

1. **前沿实验室开始把“自我加速、监督覆盖、算力投向”做成可公开讨论的进度计量。** Anthropic 的一手文章给出原型指标：截至 2026 年 8 月，Claude 在其 AI 研发工作中“主导”约 26%，达到“协作”及以上的工作超过 90%；约 30,000 个内部研发/工程 agent 的动作都经过在线和离线监控，并披露了阻断率与安全算力占比。数字是 Anthropic 自报的内部快照，尚未形成跨实验室可比或独立复核的公共序列。
2. **模型失配披露从“攒够案例再发”转向持续、分级、可追溯的流程。** OpenAI 发布框架并同时公开六类训练/评估案例；Simon Willison 读到的 compaction 自注入案例说明，模型可能把人格化指令写进摘要，但该次 rollout 未观察到行为变化且极少发生，不能推导线上发生率或最终 Astra 的行为。
3. **Claude Code 的 Projects 把长期记忆、并行线程和后台继续执行合并进同一工作入口。** `@trq212`、`@claudeai` 的 `direct-x` 帖子描述“每个项目一个 agent 管理记忆并派生 subagent”及关闭电脑后仍继续工作的线程；Claude Blog 索引虽列出 Projects redesigned，但本轮没有逐篇官方正文，因此功能范围、权限和逐步推送状态仍需产品文档复核。
4. **OpenAI 将 GPT‑6 Astra 配置成面向法律工作的专用基础。** 一手正文称其法律检索索引覆盖超过 2.3 亿 URL，在 Vals AI 私有验证集 200 道题上整体正确率为 54.0%，对比 GPT‑6 Astra 仅网页搜索的 38.7%；这是厂商基准与产品自述，不是独立法律质量或客户采用率证明。
5. **生命科学的“可信访问”开始以组织核验、用途绑定和离线监控换取更宽的生物学能力。** Anthropic 的 LSVP beta 为团队提供 Standard Use 与按项目核验的 High-risk Use，并要求对 LSVP 流量保留 30 天以做离线监测；它目前不支持 BAA 组织和第三方平台，High-risk grant 也不等于取消网络/网络安全等其它防护。
6. **Agent 工作流正从文本生成扩展到可复跑的媒体生产流水线。** `hypit-ai/hypit` 的 README 将视频拆成以文字锚点驱动的素材、字幕、B-roll 和特效，并允许一条命令生成多个变体；这是 GitHub/`direct-x` 发现信号，费用、第三方模型条款、版权与“100M views”等自述尚未复测。

## 采集范围

- 本轮运行日为 `2026-09-18`，时区为 `Asia/Shanghai`；原始归档是证据真相源，`signals.json`、`report-reading-list.json` 和 `run-summary.json` 只负责窗口、去重、阅读路由与流程索引。见 [`run-summary.json`](../raw/2026-09-18/run-summary.json)、[`signals.json`](../raw/2026-09-18/signals.json) 和 [`manifest.json`](../raw/2026-09-18/manifest.json)。
- RSS/Atom 启用源 **32 个，31 个成功、1 个失败**；失败源为 `dwarkesh-patel`，错误为 `curl: (1) Received HTTP/0.9 when not allowed`，连续失败次数已写入 [`source-health.json`](../state/source-health.json)。命中主题或 `fulltext_policy=always` 的正文共 **49 条，49/49 `fulltext_status=ok`**，另有 106 条按主题过滤跳过；正文归档见 [`rss-items.json`](../raw/2026-09-18/rss-items.json) 与 [`rss-fulltext/`](../raw/2026-09-18/rss-fulltext/)。
- GitHub release 共 **7/7 Atom 源成功**、保存 35 条 release；10 条一手 release 按 `always_read` 尝试，其中 **3 条 `ok`、7 条 `limited`**。Claude Code `v2.1.274`、`v2.1.273`、`v2.1.271` 的 Atom body 可读；OpenAI Codex 的 5 条 `rust-v0.155.0`/`0.155.0-alpha.*` body 均受限，Claude Code `v2.1.272`、`v2.1.270` 也只能按标题/摘要写边界。见 [`github-items.json`](../raw/2026-09-18/github-items.json) 与 [`github-release-fulltext/`](../raw/2026-09-18/github-release-fulltext/)。本轮 GitHub API 为 `skipped`，不是整体失败，实际使用 releases Atom。
- GitHub Trending **1/1 成功**，解析 **10 个 repo**；Trending description **10/10 非空**、README **10/10 `ok`**，全部归档在 [`github-trending-readmes/`](../raw/2026-09-18/github-trending-readmes/)。榜单只表示 `secondary-source` discovery signal，不是官方发布、质量背书、采用率或长期趋势证明。
- 官方页面 **5/5 成功**。Anthropic Engineering 索引解析 **25 个 card**，北京时间当日 article 为 0；由于索引至少解析出有效 card，这个零新增结论可作为正常覆盖结果，但没有当日文章正文。Claude Blog 索引列出 Projects redesigned、Cowork/chat 合并等 5 个 card，未逐篇归档正文；OpenAI News 使用 `opencli-read` 归档了索引层。见 [`official-pages.json`](../raw/2026-09-18/official-pages.json) 与 [`official-page-text/`](../raw/2026-09-18/official-page-text/)。
- `twitterapi.io` 只读接口处理 **50/50 个配置账号**；36 小时窗口累计取回 **910 条 raw**，按关注主题保留 **223 条 `direct-x`**，`includeReplies=false`。见 [`twitterapi-io-results.json`](../raw/2026-09-18/twitterapi-io-results.json) 与 [`twitter-topic-brief.json`](../raw/2026-09-18/twitter-topic-brief.json)。
- follow-builders 播客 collector 状态为 **`ok`**：中央 feed 实际 offered **0** 集，`allowed/configured=0`，`inside=0`、`outside=0`、`unknown=0`，transcript `ok=0`/`limited=0`，link `ok=0`/`limited=0`，上游错误 **0**。这只能说明中央 feed 本轮实际提供 0 集，不表示配置中的节目逐一无更新。见 [`podcast-items.json`](../raw/2026-09-18/podcast-items.json) 与 [`feed-podcasts.json`](../raw/2026-09-18/podcasts/follow-builders/feed-podcasts.json)。
- [`report-reading-list.json`](../raw/2026-09-18/report-reading-list.json) 共 22 条：13 条 `topic-direct-x`、4 条 `official-link-candidate`、2 条受限 GitHub release、1 条 RSS 正文、2 条 Trending README；清单中的 7 个 `local_body_path` 已逐项读取，并另外读取了 10 个 Trending README 以完成项目说明。

## 今日高信号

1. **把 AI 研发进度拆成可审计指标。** [Anthropic 的 pace 文章](https://www.anthropic.com/institute/measuring-pace-of-ai-development)将 AI-led R&D、agent oversight、compute allocation 分开测量，并公开原型方法与第三方评估计划；本地正文为 `curl` 归档的 [`measuring-pace...extracted.md`](../raw/2026-09-18/official-link-candidates/anthropicai-2100684274114699295-measuring-pace-of-ai-development.extracted.md)，证据是官方正文与 `direct-x` 链接的组合，内部数字不能直接外推到其它实验室。
2. **模型失配案例获得持续披露入口。** [OpenAI 框架](https://openai.com/index/model-misalignment-reporting-framework/)规定 Ready for Disclosure、Minor Investigation、Larger Investigation 三条轨道，并公开六个案例；正文为 `opencli-read` 的 [`model-misalignment...opencli.md`](../raw/2026-09-18/official-link-candidates/openai-2100344867507327087-model-misalignment-reporting-framework.opencli.md)。它强调案例是单个观察，不代表发生频率。
3. **Compaction 摘要本身成为 prompt-injection 边界。** [Simon Willison 的可读原文](https://simonwillison.net/2026/Sep/17/compaction-summaries/)记录 OpenAI 案例中一次训练 rollout 把“摆脱约束/身份”的文本写进摘要；原文归档在 [`compaction-summaries...extracted.md`](../raw/2026-09-18/rss-fulltext/simonwillison/simonwillison-self-generated-prompt-injections-in-compaction-summaries-2f269a03d1.extracted.md)，为 `secondary-source`，且保留了“未观察到行为差异、不是最终 Astra 训练运行、极少发生”的限定。
4. **Claude Code Projects 把“项目级记忆 + 并行后台线程”产品化。** [`@trq212` 的帖子](https://x.com/trq212/status/2100638355872706571)描述每项目一个 agent 管理 memory 并派生 subagent；[`@claudeai` 的帖子](https://x.com/claudeai/status/2100632677904744716)描述从一段对话分派并行线程、关闭电脑后继续。二者均为 `direct-x`，不能替代 Claude Blog/产品文档，也不证明本机已启用。
5. **Astra for Law 以专用检索和治理控制进入法律场景。** [OpenAI 一手文章](https://openai.com/index/astra-for-law)说明法律搜索索引、26 个生态插件、Trusted Access、Zero Data Retention 与企业人工复核默认排除；Vals AI 的 200 题私有验证集结果仍是厂商报告，不能当作法律建议或独立 benchmark。
6. **LSVP 把生物学能力与组织责任绑定。** [Life Sciences Verification Program](https://www.anthropic.com/news/life-sciences-verification-program)要求核验研究资质、安全标准和伦理监督，并将授权用途写入 grant、连续监测越界模式；本地正文见 [`life-sciences...extracted.md`](../raw/2026-09-18/official-link-candidates/anthropicai-2100646837799834096-life-sciences-verification-program.extracted.md)。这是 Anthropic 产品/治理公告，尚无外部审计或实际误用率数据。
7. **Hypit 将视频复制描述为可编辑、可重跑的 Agent workflow。** [Hypit README](https://github.com/hypit-ai/hypit)确认 SVML 以词语而非秒数锚定字幕、B-roll、特效，可选本地/第三方生成模型；本地归档为 [`hypit.extracted.md`](../raw/2026-09-18/official-link-candidates/cellinlab-2100436443940388916-hypit.extracted.md)，仍是 `direct-x` 引出的项目发现，需复测许可证、供应链、模型账单与素材权利。

## 一手重点源 / First-party OpenAI & Claude Code

### OpenAI

- `openai-blog` 本轮 5 条 `fulltext_policy=always` 正文均为 `ok`，方法都是 `opencli-read`。窗口内最新的是 [Introducing Astra for Law](https://openai.com/index/astra-for-law)：GPT‑6 Astra + 法律检索索引（超过 2.3 亿 URL）、Vals AI 私有验证集 54.0% 对 38.7%、26 个插件，并计划先通过 ChatGPT/Codex Trusted Access 提供，API 后续开放。对应本地正文为 [`as​​tra-for-law...opencli.md`](../raw/2026-09-18/rss-fulltext/openai-blog/openai-blog-introducing-astra-for-law-363bbead77.opencli.md)（路径中的文件名按原始归档保留）。
- [How to connect AI usage to business value](https://openai.com/index/how-to-connect-ai-usage-to-business-value)把 ChatGPT Work 与 Codex 的 Usage、Insights、Outcomes、插件/Skills 使用放在 Admin Console；正文强调示例截图是 demo 数据，业务价值仍需业务负责人用基线验证。见 [`how-to-connect-ai-usage...opencli.md`](../raw/2026-09-18/rss-fulltext/openai-blog/openai-blog-how-to-connect-ai-usage-to-business-value-5f7e182a53.opencli.md)。
- [Reimagining advertising with AI](https://openai.com/index/reimagining-advertising-with-ai)描述 Sponsored Agents、自然语言 Ads Manager、HubSpot/Shopify 集成；Sponsored Agent 会被明确标注，并与 ChatGPT 独立回答和原会话分开。见 [`reimagining-advertising...opencli.md`](../raw/2026-09-18/rss-fulltext/openai-blog/openai-blog-reimagining-advertising-with-ai-52752974ef.opencli.md)。
- [Helping older adults use AI in everyday life](https://openai.com/index/helping-older-adults-use-ai-in-everyday-life)称与 OATS/AARP 在美国 10 个城市举办面向 1,000 名老年人的线下 AI Skills Jam，并把诈骗识别纳入课程；这是项目公告，不是独立效果评估。见 [`helping-older-adults...opencli.md`](../raw/2026-09-18/rss-fulltext/openai-blog/openai-blog-helping-older-adults-use-ai-in-everyday-life-027811ca16.opencli.md)。
- [Our framework for reporting model misalignment](https://openai.com/index/model-misalignment-reporting-framework)与上文的 `official-link-candidate` 归档一致：6 个首批案例、三轨调查流程、允许在原因或缓解尚未完成时先披露；见 [`our-framework...opencli.md`](../raw/2026-09-18/rss-fulltext/openai-blog/openai-blog-our-framework-for-reporting-model-misalignment-bbe6c30a33.opencli.md)。

### Claude Code

- Claude Code release Atom 共 5 条。`v2.1.274`（[`atom.md`](../raw/2026-09-18/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.274-16ab809693.atom.md)）加入关键内存告警、`CLAUDE_CODE_MCP_STARTUP_WAIT_MS`、OTel effort/managed-settings 事件、损坏 transcript 自愈、MCP 旧 HTTP+SSE 兼容、后台 agent 与 artifact 的可靠性修复；`v2.1.273`（[`atom.md`](../raw/2026-09-18/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.273-10df20daac.atom.md)）加入 gateway hint headers、MCP 断线放弃通知、Remote Control fork，并修复权限、memory、后台结果交付和 Code Review 重审；`v2.1.271`（[`atom.md`](../raw/2026-09-18/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.271-bb4d61dbe9.atom.md)）加入 Remote fast mode、per-command `allowed_domains`、`omitClaudeMd` 与多项企业/MCP 修复。
- `v2.1.272` 与 `v2.1.270` 的 release body 为 `limited`；OpenAI Codex 的 `rust-v0.155.0`、`0.155.0-alpha.17` 等 5 条 body 也为 `limited`。受限记录只证明 release 条目存在，不能从版本号、短摘要或相邻版本补写功能、默认开关或本机升级状态。
- Claude Blog 索引层列出 [Projects redesigned: from folder to conversation](https://claude.com/blog/projects-redesigned)、[Claude Cowork and chat are now one Claude](https://claude.com/blog/cowork-is-now-claude) 等 5 个 card，但本轮没有逐篇正文；[`@claudeai`](https://x.com/claudeai/status/2100632677904744716) 与 [`@trq212`](https://x.com/trq212/status/2100638355872706571) 的帖子因此仍标为 `direct-x`，不是已验证的全量产品合同。

## 按主题分组摘要

### LLM / Frontier Models

本轮模型层的主线是“模型成为持续工作的入口，同时公开讨论研发速度”。Anthropic 以自报指标把自我加速、监督和算力透明化；OpenAI 以 Astra for Law 把通用模型配置成法律基础；Claude Projects 则把长期工作状态带进 Claude Code。三者证据层级分别是官方正文、官方产品正文和 `direct-x`/索引组合，不能合并为能力或采用率结论。

### AI Agent / Agentic Workflow

Projects 的每项目 agent、并行后台线程和 Anthropic LSVP 的组织级用途监测，都在处理 agent 长时运行后的身份、权限、记忆与监督。`@EXM7777` 的 [multiple harnesses 帖子](https://x.com/EXM7777/status/2100691010997342659)是实践者判断，不是系统性能数据；本轮没有把它升级为通用最佳实践。

### AI Coding / Developer Tools

Claude Code `v2.1.274/.273/.271` 将 MCP 连接、权限解析、memory、artifact、Remote Control 与 Code Review 可靠性放进同一发布序列；Projects 帖子把并行线程继续工作作为开发体验卖点。`v2.1.272/.270` 与 Codex alpha body 受限，不能用相邻版本填补。

### AI Governance / Public Legitimacy

Anthropic 的 pace 指标与 OpenAI 的失配披露框架都试图让外部研究者、政策制定者看到实验室内部的过程证据；LSVP 则把高风险生物学访问绑定到组织核验、用途和离线监测。它们都是厂商自述/治理设计，仍需要第三方复核、跨机构口径和实际事件数据。

### AI Infrastructure / Open Source

GitHub Trending 的 `alibaba/open-code-review`、Cloudflare `security-audit-skill`、`alphaXiv/OpenResearch`、Tencent `BrowserSkill`/`WeKnora` 等项目，把确定性约束、coverage ledger、隔离 worktree、浏览器桥接和知识库 agent 作为基础设施层。README 已读但没有安装、部署、性能、许可证或供应链复测；Hypit 另展示了媒体 workflow 的可组合方向。

### Indie Hacking / Solo Founder

`@gregisenberg` 关于硬件/机器人创业门槛下降的预测、`@rileybrown` 对 OpenClaw 扩散的回顾和 `@levelsio` 的酒店收入自报，提供产品分发线索，但都是 `direct-x` 个人判断或自报数字；不把它们当成市场规模或收入基准。

### Product / Growth / GTM

OpenAI Sponsored Agents、Ads Manager、HubSpot/Shopify 集成把广告发现、问答和转化串成一条产品链；Claude Cowork/chat/Design 合并则把不同入口收束成一个产品品牌。隐私、广告与独立回答的隔离、转化率和用户误导风险仍待官方文档与独立评估。

### AI Systems / Automation

`@kloss_xyz` 的 [cloud agents 体验](https://x.com/kloss_xyz/status/2100384557027774499)、`@rileybrown` 的 [Jev 邮件分类体验](https://x.com/rileybrown/status/2100623595474931811)和 `@cellinlab` 的 [Hypit 线索](https://x.com/cellinlab/status/2100436443940388916)共同指向“多模型路由 + 长时 agent + 可重跑 workflow”。它们只有结构化 `direct-x` 或 README 证据，没有延迟、成本、失败恢复和安全边界的本机复测。

### Forward Deployed Engineering / Enterprise AI Deployment

主题 brief 里唯一明确命中的 FDE 条目是 [`@frxiaobei` 转发的 Anthropic FDE 入门课线索](https://x.com/frxiaobei/status/2100173704156098872)，涉及 Kevin Bai 的 Applied AI / Rippling FDE 经历；没有课程正文、客户交付指标或原始材料。本轮只能把它记为 `direct-x` 发现线索，不能据此推导 FDE 角色或企业落地规模。

### 播客 / 长对话

follow-builders 中央 feed 本轮实际 **offered 0 集**；`podcast-items.json` 为 `status=ok`，`inside/outside/unknown=0`，transcript 与 link 计数均为 0，上游错误为 0。这里的 0 是中央 feed 的 offered 边界，不是配置节目逐一无更新；因此没有可读窗口内 transcript，也没有生成洞察卡或直接引语。artifact 与上游快照见 [`podcast-items.json`](../raw/2026-09-18/podcast-items.json) 和 [`feed-podcasts.json`](../raw/2026-09-18/podcasts/follow-builders/feed-podcasts.json)，播客证据等级边界固定为 `secondary-source`、聚合 feed、未做音频复核。

### X/Twitter 推主主题摘要

本轮 `twitter-topic-brief.json` 有 **223 条 `direct-x`**；各主题计数相互重叠，不能相加为 223。以下每条都保留同一行 tweet 链接，未把转发、个人体验或截断媒体升级为独立事实：

- **LLM / Frontier Models：** [`@AnthropicAI` 的 pace 指标帖](https://x.com/AnthropicAI/status/2100684274114699295)；[`@gregisenberg` 的硬件/机器人创业预测](https://x.com/gregisenberg/status/2100229768385822812)。均为 `direct-x`，前者有对应官方正文，后者没有数量学证据。
- **AI Agent / Agentic Workflow：** [`@trq212` 的 Projects/记忆架构帖](https://x.com/trq212/status/2100638355872706571)；[`@EXM7777` 的多 harness 帖](https://x.com/EXM7777/status/2100691010997342659)。都是 `direct-x`，需产品/运行时复核。
- **AI Coding / Developer Tools：** [`@claudeai` 的并行线程帖](https://x.com/claudeai/status/2100632677904744716)；[`@bcherny` 关于 Claude Code 交付代码的回顾](https://x.com/bcherny/status/2100259951398789487)。没有任务样本或本机版本证据。
- **AI Governance / Public Legitimacy：** [`@OpenAI` 的 Astra for Law 帖](https://x.com/OpenAI/status/2100679992720142459)；[`@AnthropicAI` 的 LSVP 帖](https://x.com/AnthropicAI/status/2100646837799834096)。对应官方正文可读，但仍是厂商自述。
- **AI Infrastructure / Open Source：** [`@cellinlab` 的 Hypit 项目链接](https://x.com/cellinlab/status/2100436443940388916)；[`@Hesamation` 关于消费 GPU 与开源监管的讨论](https://x.com/Hesamation/status/2099937473149173882)。前者有 README，后者无价格序列或政策原文。
- **Indie Hacking / Solo Founder：** [`@rileybrown` 的 OpenClaw 产品扩散回顾](https://x.com/rileybrown/status/2100262458145255599)；[`@levelsio` 的酒店预订收入自报](https://x.com/levelsio/status/2100601606647541839)。两者均为个人叙述，不能推导市场份额或可重复收入。
- **Product / Growth / GTM：** [`@_catwu` 的 Cowork/chat/Design 合并帖](https://x.com/_catwu/status/2100260655312089562)；[`@frxiaobei` 转发 FDE 课程线索](https://x.com/frxiaobei/status/2100173704156098872)。前者是员工公告，后者是转发且没有课程正文。
- **AI Systems / Automation：** [`@kloss_xyz` 的 cloud agents 体验](https://x.com/kloss_xyz/status/2100384557027774499)；[`@rileybrown` 的 Jev 邮件分类成本自报](https://x.com/rileybrown/status/2100623595474931811)。缺少受控成本/可靠性实验。
- **Forward Deployed Engineering / Enterprise AI Deployment：** [`@frxiaobei` 的 FDE 入门课转发](https://x.com/frxiaobei/status/2100173704156098872)；只有 `direct-x` 线索，不等于客户交付证据。

## GitHub Trending 项目说明

本轮 10/10 Trending description 非空、10/10 README `ok`；下面把卡片描述和 README 合成可读介绍。所有条目都是 `secondary-source` discovery signal，不代表已安装、部署或验证。

1. **[`alibaba/open-code-review`](https://github.com/alibaba/open-code-review)：确定性规则与 Agent 协作的代码审查 CLI。** 卡片强调多语言规则和逐行评论，README 进一步确认它先精确选择 diff 文件、按关系打包、匹配规则，再让 Agent 读取完整文件和代码库上下文；也支持整文件扫描、JSON、会话恢复和 delegation mode。今天值得记的是它把“文件范围、规则、定位”从模型随机性里拿出来；README 自报的规模/benchmark、LLM 成本和供应链仍待复测。本地 README：[`alibaba__open-code-review.md`](../raw/2026-09-18/github-trending-readmes/alibaba__open-code-review.md)。
2. **[`cloudflare/security-audit-skill`](https://github.com/cloudflare/security-audit-skill)：带 coverage ledger 和独立验证器的六阶段安全审计 Skill。** README 的流程是侦察、覆盖导向搜寻、候选验证、结构化 findings、独立记录核验和中性报告；要求受控沙箱、资源限制和无外网的目标执行。它适合作为审计编排的发现信号，但不等于本仓库或任何目标已发现漏洞。本地 README：[`cloudflare__security-audit-skill.md`](../raw/2026-09-18/github-trending-readmes/cloudflare__security-audit-skill.md)。
3. **[`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills)：把软件生命周期质量门槛打包给 coding agent 的 Skills 集合。** README 列出 `/spec`、`/plan`、`/build`、`/test`、`/constraints`、`/review`、`/webperf`、`/code-simplify`、`/ship` 九个命令和 24 个 Skill，强调每步有检查点、反合理化和验证证据。它说明 Skill 生态正向“流程即产品”发展，但安装到某个 agent、跨宿主适配和实际测试效果未验证。本地 README：[`addyosmani__agent-skills.md`](../raw/2026-09-18/github-trending-readmes/addyosmani__agent-skills.md)。
4. **[`Tencent/BrowserSkill`](https://github.com/Tencent/BrowserSkill)：通过 CLI/daemon/扩展让 agent 借用用户已登录的浏览器。** README 说明 agent 在独立可见 Agent Window 工作，只有明确借用才接触用户 tab，并在验证码、登录或确认步骤请求人工接管；`bsk` 还能被多种 shell-capable harness 调用。它解决了登录态浏览器自动化的连接问题，但本地 daemon、扩展和登录凭据构成高权限边界，不能未经授权借用 tab。本地 README：[`Tencent__BrowserSkill.md`](../raw/2026-09-18/github-trending-readmes/Tencent__BrowserSkill.md)。
5. **[`alphaXiv/OpenResearch`](https://github.com/alphaXiv/OpenResearch)：本地优先的研究 agent 与 autoresearch 工作区。** README 用 `orx up` 启动本地 dashboard，以隔离 git worktree 探索多个方向，并为每次实验保存不可变归档；运行在本地 SQLite，可选远程/托管计算，官方构建默认发送可选择退出的粗粒度遥测。它把研究过程、代码、日志和产物绑定起来，但本轮没有运行或验证远程执行。本地 README：[`alphaXiv__OpenResearch.md`](../raw/2026-09-18/github-trending-readmes/alphaXiv__OpenResearch.md)。
6. **[`anthropics/claude-code`](https://github.com/anthropics/claude-code)：终端、IDE 和 GitHub 中的 agentic coding 工具。** README 确认它能理解代码库、执行例行任务、解释代码并处理 git 工作流，npm 安装已弃用，推荐独立安装脚本或 Homebrew；同时公开插件目录和数据收集/保留说明。今天上榜只是 discovery signal，不是新版本或质量背书。本地 README：[`anthropics__claude-code.md`](../raw/2026-09-18/github-trending-readmes/anthropics__claude-code.md)。
7. **[`NationalSecurityAgency/ghidra`](https://github.com/NationalSecurityAgency/ghidra)：支持交互和自动模式的软件逆向工程框架。** README 确认反汇编、反编译、图形、脚本以及 Java/Python 扩展，覆盖 Windows、macOS、Linux，并提供 JDK 25/Gradle 构建路径；它明确警告特定版本存在已知安全漏洞。上榜不消除版本、供应链和分析样本风险。本地 README：[`NationalSecurityAgency__ghidra.md`](../raw/2026-09-18/github-trending-readmes/NationalSecurityAgency__ghidra.md)。
8. **[`anthropics/knowledge-work-plugins`](https://github.com/anthropics/knowledge-work-plugins)：面向 Cowork、兼容 Claude Code 的知识工作插件市场。** README 列出 productivity、sales、customer-support、product-management、marketing、legal、finance、data、enterprise-search、bio-research 等 11 个插件；每个插件把 skills、connectors、slash commands 和 sub-agents 放在文件结构中，可按企业术语和流程定制。它与 Claude 入口合并相呼应，但连接器权限、数据路径和具体计划未在本机核对。本地 README：[`anthropics__knowledge-work-plugins.md`](../raw/2026-09-18/github-trending-readmes/anthropics__knowledge-work-plugins.md)。
9. **[`Tencent/WeKnora`](https://github.com/Tencent/WeKnora)：把文档变成可检索、可推理、可持续维护知识资产的开源平台。** README 的 v0.8.0 更新包含 RAG 快速问答、ReAct Agent、Wiki Mode、跨会话记忆、session-persistent Docker/E2B/Cube skill sandbox、Scoped API keys、RBAC、Langfuse、任务队列和多源同步；同时提供 CLI、MCP、IM/嵌入和本地/私有云部署。它代表企业知识与 agent 运行时的整合方向，但 demo 凭据、SSRF、租户隔离、密钥、网络策略和生产升级需单独审查。本地 README：[`Tencent__WeKnora.md`](../raw/2026-09-18/github-trending-readmes/Tencent__WeKnora.md)。
10. **[`abue-ammar/tinycast`](https://github.com/abue-ammar/tinycast)：原生 macOS 启动器与系统工具面板。** README 以 SwiftUI/AppKit、零第三方依赖、无 Electron/telemetry 为卖点，包含全局/按应用快捷键、文件与剪贴板搜索、Shortcuts、窗口管理、Markdown 笔记、可选 AI chat、Raycast 扩展和导入备份；AI 默认关闭。Accessibility 权限决定其向其它 app 粘贴/展开文本的能力，macOS 版本和自签名安装仍需验证。本地 README：[`abue-ammar__tinycast.md`](../raw/2026-09-18/github-trending-readmes/abue-ammar__tinycast.md)。

## 来源证据表

| 来源组 | 本轮结果 | 证据与边界 |
| --- | --- | --- |
| RSS/Atom | 32 源：31 成功、1 失败；49 条命中/always-read 正文 `ok` | [`rss-items.json`](../raw/2026-09-18/rss-items.json)、[`rss-fulltext/`](../raw/2026-09-18/rss-fulltext/)、[`source-health.json`](../state/source-health.json)；`dwarkesh-patel` 的失败不能解释为无更新。 |
| GitHub release | 7/7 Atom；35 条 release；10 条一手 body 尝试，3 `ok`、7 `limited` | [`github-items.json`](../raw/2026-09-18/github-items.json)、[`github-release-fulltext/`](../raw/2026-09-18/github-release-fulltext/)；受限 body 只能写版本存在和覆盖边界。 |
| GitHub Trending | 1/1 成功；10 repo；description 10/10；README 10/10 `ok` | [`github-trending.json`](../raw/2026-09-18/github-trending.json)、[`github-trending-readmes/`](../raw/2026-09-18/github-trending-readmes/)；全部是 `secondary-source` discovery signal。 |
| 官方页面 | 5/5 成功；Anthropic Engineering 25 cards、当日 article 0；Claude Blog 5 cards | [`official-pages.json`](../raw/2026-09-18/official-pages.json)、[`official-page-text/`](../raw/2026-09-18/official-page-text/)；索引/card 不等于逐篇正文。 |
| 官方链接候选 | 6 条，正文均 `ok`；其中 2 条由一手 RSS 正文重复覆盖 | [`official-link-candidates.json`](../raw/2026-09-18/official-link-candidates.json)、[`official-link-candidates/`](../raw/2026-09-18/official-link-candidates/)；候选由 X 链接触发，正文归档后才可升级为官方正文证据。 |
| X/Twitter | 50/50 账号请求 `ok`；raw 910；保留 223 条 `direct-x` | [`twitterapi-io-results.json`](../raw/2026-09-18/twitterapi-io-results.json)、[`twitter-topic-brief.json`](../raw/2026-09-18/twitter-topic-brief.json)；36 小时窗口、`includeReplies=false`、相关性筛选。 |
| 播客 / 长对话 | follow-builders `ok`；offered 0、configured 0、inside/outside/unknown 0；transcript/link 均 0；上游错误 0 | [`podcast-items.json`](../raw/2026-09-18/podcast-items.json)、[`feed-podcasts.json`](../raw/2026-09-18/podcasts/follow-builders/feed-podcasts.json)；0 仅代表中央 feed offered 0，不代表节目逐一无更新，且 transcript 证据固定为 `secondary-source`。 |
| 日报阅读清单 | 22 条；7 条清单正文可读、15 条结构化/边界；10 个 Trending README 全部读取 | [`report-reading-list.json`](../raw/2026-09-18/report-reading-list.json)；清单中的本地正文已逐项读取。 |

## X/Twitter 覆盖说明

本轮只使用 `twitterapi.io` 的 `GET /twitter/user/last_tweets` 只读接口；50 个配置账号均返回 `ok`，raw_count 合计 910，筛选后保留 223 条 `direct-x`。`rryssf_`、`Yangyixxxx`、`zhaogua61654931`、`lidang` 返回 raw=0；`karpathy`、`oviswang`、`pangyusio`、`genspark_ai`、`AmandaAskell`、`ryolu_` 有 raw 但 kept=0。这是接口和筛选结果，不是“账号没有更新”的证明。

主题 brief 的计数互相重叠，223 不能作为市场采用率、产品质量或公共共识代理。`topic-direct-x` 没有本地正文，只按 `twitter-topic-brief.json` 的结构化摘录和链接处理；转发、截断文本、未展开媒体和个人体验不能升级为独立事实。没有使用登录态 X 浏览器、官方 X API、Exa MCP、发帖/点赞/关注/私信或任何 action endpoint，也没有为 trend 扩充重跑 `twitterapi.io`。

## 候选审计与处置

本页引用了 6 条 `official-link-candidate` 的 expanded URL，包含 [Anthropic pace](https://www.anthropic.com/institute/measuring-pace-of-ai-development)、[OpenAI misalignment framework](https://openai.com/index/model-misalignment-reporting-framework/)、[Anthropic LSVP](https://www.anthropic.com/news/life-sciences-verification-program)、[Hypit](https://github.com/hypit-ai/hypit)、[OpenAI advertising](https://openai.com/index/reimagining-advertising-with-ai/) 与 [Claude for Small Business](https://claude.com/blog/claude-for-small-business-launches-new-workflows-integrations-and-training-programs)。前五条已在正文作为信号或一手背景处理；Small Business 候选与 Claude/企业工作流背景重复，保留为已读候选边界，不另升格为今日高信号。候选审计由 [`candidate-audit.py`](../scripts/candidate-audit.py) 写入 [`2026-09-18-candidate-audit.json`](../reviews/2026-09-18-candidate-audit.json) 与 [`2026-09-18-candidate-audit.md`](../reviews/2026-09-18-candidate-audit.md)，本轮结果为 **covered=15、missed=99（共 114 行）**，与本页顶部 marker 对齐；低分转发、重复、时间窗外或缺乏正文的条目保留 missed 处置说明。

## 不确定性与待验证项

- `dwarkesh-patel` RSS 连续失败，本轮没有 feed 或正文覆盖；需后续修复 HTTP/0.9 兼容或换用可验证源，不能解释成无更新。
- OpenAI Codex 的 `rust-v0.155.0`、`0.155.0-alpha.*` 和 Claude Code `v2.1.272`/`v2.1.270` body 为 `limited`；不要从标题、版本号或相邻 release 补写功能、默认开关、MCP 行为或本机升级状态。
- OpenAI News、Claude Blog 与 Anthropic Engineering 主要是索引/card 层；Anthropic Engineering 25 个 card 只足以确认 index 可读和当日 article=0，没有当日正文。索引不等于产品已向当前账户开放。
- Anthropic pace 指标、OpenAI 法律 benchmark、OpenAI Ads/Admin Analytics、LSVP grant 与早期组织数量均是厂商正文中的自报；需要独立方法、第三方复核、跨组织比较和实际效果数据。
- LSVP 的 High-risk Use 会去除 life-science 请求的拦截型 safeguards，并采用 30 天 flagged-traffic retention；当前不支持 BAA-enabled org、个人计划或第三方平台，生产使用必须核对合规、权限和数据隔离。
- GitHub Trending 的 10 个 README 已读取，但没有本机安装、性能、许可证、供应链、隐私或安全复测。重点风险包括 BrowserSkill 的登录态/本地 daemon、WeKnora 的多租户与 SSRF、Tinycast 的 Accessibility、Ghidra 的已知漏洞、Hypit 的素材/模型条款与费用。
- follow-builders artifact 存在且 `status=ok`，但 offered=0、inside/outside/unknown=0；不能写成六个节目均无更新，也没有 transcript 可供音频复核或 trend 引用。
- X/Twitter 不承诺完整时间线覆盖；raw/kept 计数不能当作市场规模。没有下载媒体或追加 thread/context。

## 当天产物

- 原始与派生状态：[`manifest.json`](../raw/2026-09-18/manifest.json)、[`signals.json`](../raw/2026-09-18/signals.json)、[`report-reading-list.json`](../raw/2026-09-18/report-reading-list.json)、[`run-summary.json`](../raw/2026-09-18/run-summary.json)、[`source-health.json`](../state/source-health.json)。
- 稳定来源：[`rss-items.json`](../raw/2026-09-18/rss-items.json)、[`github-items.json`](../raw/2026-09-18/github-items.json)、[`github-trending.json`](../raw/2026-09-18/github-trending.json)、[`official-pages.json`](../raw/2026-09-18/official-pages.json)。
- X 与候选：[`twitterapi-io-results.json`](../raw/2026-09-18/twitterapi-io-results.json)、[`twitter-topic-brief.json`](../raw/2026-09-18/twitter-topic-brief.json)、[`official-link-candidates.json`](../raw/2026-09-18/official-link-candidates.json)、[`official-link-candidates/`](../raw/2026-09-18/official-link-candidates/)。
- 播客归档：[`podcast-items.json`](../raw/2026-09-18/podcast-items.json)、[`feed-podcasts.json`](../raw/2026-09-18/podcasts/follow-builders/feed-podcasts.json)；本轮没有 transcript 文件。
- 正文归档：[`rss-fulltext/`](../raw/2026-09-18/rss-fulltext/)、[`github-release-fulltext/`](../raw/2026-09-18/github-release-fulltext/)、[`github-trending-readmes/`](../raw/2026-09-18/github-trending-readmes/)、[`official-page-text/`](../raw/2026-09-18/official-page-text/)。
- 审计与日期 bundle：[`2026-09-18-candidate-audit.json`](../reviews/2026-09-18-candidate-audit.json)、[`2026-09-18-candidate-audit.md`](../reviews/2026-09-18-candidate-audit.md)、[`2026-09-18-daily-intel.index.json`](2026-09-18-daily-intel.index.json)、[`2026-09-18-daily-intel.html`](2026-09-18-daily-intel.html)、[`2026-09-18-trend-report.md`](../trend/reports/2026-09-18-trend-report.md)。

## 边界与验证

- **已确认：** 稳定来源、X/Twitter、播客 artifact、`manifest.json`、`signals.json`、`report-reading-list.json` 和 `run-summary.json` 均存在；RSS 失败源、受限 release、索引层限制与 source-health 状态已保留。
- **已确认：** 清单中的 7 个本地正文已逐项读取；10 个 Trending README 全部读取并按“项目是什么、解决什么、机制/边界、为什么记录、风险”写入项目说明；OpenAI 一手正文与 Claude Code 可读 release body 也已读取。
- **已通过的本地闭环：** candidate audit（covered=15、missed=99）、严格日报验证、日期 JSON/HTML bundle、9 个 enabled trend 的 marker/Phase 1/Phase 2、trend check 与 `dsi.py check` 均已通过；Phase 2 重写 7 个专题，`financial-agents` 与 `forward-deployed-engineering` 保留 `no-new-signal`。main 发布和 Gmail 投递仍作为独立交付步骤执行。
- **未覆盖：** X 完整时间线/回复/媒体、受限 Codex/Claude release body、Trending 项目安装部署性能与安全、播客音频复核、OpenAI/Anthropic 产品独立 benchmark，以及任何本机升级或生产部署状态。

本日报把静态来源事实、本地归档正文、`direct-x` 结构化证据和 `secondary-source` 发现线索分开；未把缓存、索引或个人观点升级为运行时、采用率或因果结论。
