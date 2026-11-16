## 直接答案

2026-11-17 北京时间窗口新增入库 68 条，seen 总数为 8,209。阅读清单有 24 项：12 项有可读本地正文，12 项是结构化帖子或正文受限。日报整理出 6 条高信号，主要涉及 OpenAI 的科研访问、儿童安全、外部评估与医疗电脑操作代理，以及 Gemini 4 安全评估争议和智能体技能评估工具。

## 采集范围

- 最终统一采集命令为 DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-11-17，通过系统网络路径完成。随后用同一入口的 resume 模式重建派生状态；resume 没有新增 seen 条目。采集范围按 2026-11-17 北京时间计算；日期与流程索引见[run-summary.json](../raw/2026-11-17/run-summary.json)、[manifest.json](../raw/2026-11-17/manifest.json)和[report-reading-list.json](../raw/2026-11-17/report-reading-list.json)。
- RSS/Atom：33 个源中 32 个成功。44/44 个主题匹配或一手重点正文读取成功；dwarkesh-patel 返回 curl: (52) Empty reply from server。
- AIHOT 精选 RSS：读取最新 50 条，状态 ok。50 条均保留 feed 发布时间、GUID、AIHOT 站内链接和原文链接；7 条在北京时间窗口内、43 条在窗外、0 条时间未知。窗口内 3 条命中主题且原文均可读（2 条 curl、1 条 opencli-read），另有 4 条未命中配置并跳过原文。AIHOT 内容始终按 secondary-source 处理；最新 50 条只是有限发现范围。[AIHOT XML 快照](../raw/2026-11-17/rss-feeds/aihot-selected.xml)。
- GitHub Releases：7/7 个 Atom 源成功。10 条一手重点正文均已尝试，4 条 ok、6 条 limited；窗口内的 Codex 0.171.0-alpha.8 和 0.171.0-alpha.9 只有版本标题，无法确认具体改动。
- GitHub Trending：解析到 10 个项目，页面描述与 README 均为 10/10。榜单和 README 是发现线索及项目方自述，不是质量或部署验证。
- 官方页面：4/5 个源成功，anthropic-engineering 为 limited。它的索引虽抓取成功，但没有解析出有效文章卡片，因此不能据此断言当天没有文章。OpenAI News 使用 opencli-read。
- X/Twitter：twitterapi.io 的 50/50 个账号请求成功，返回 920 条原始帖子并保留 148 条 direct-x 记录。该结果不代表账号完整时间线。
- 播客：follow-builders 状态 ok，本轮 offered 1 集；inside/outside/unknown 为 0/1/0，transcript ok/limited 为 1/0，单集链接 ok/limited 为 0/1，上游错误 0。这个数字只表示中央 feed 本轮提供 1 集，不代表已逐一检查所有配置节目。[播客采集记录](../raw/2026-11-17/podcast-items.json)、[feed 快照](../raw/2026-11-17/podcasts/follow-builders/feed-podcasts.json)和[本地 transcript](../raw/2026-11-17/podcasts/follow-builders/transcripts/tokenization-agentic-trading-harmonic-robinhood-s-mission-to-expand-ownership-wi-177edd54d1f6.md)保留了 GUID、聚合来源和链接状态。

## 今日高信号

1. **OpenAI 扩大科学研究者的免费访问。** 官方文章称新一轮申请于 11 月 23 日开放，计划提供最多 5 万份 ChatGPT Plus 资助，每份可覆盖研究者和最多两名合作者；项目的整体目标是触达最多 20 万名科学家，默认不使用项目数据训练模型。这是科研场景产品访问范围的扩展，人数与数据处理承诺来自 OpenAI 自述。[官方文章](https://openai.com/index/expanding-chatgpt-for-academic-researchers) · [本地正文](../raw/2026-11-17/rss-fulltext/openai-blog/openai-blog-broadening-access-to-ai-for-scientists-f26f2a4dfd.opencli.md)（official-source）。
2. **OpenAI 更新儿童安全检测与干预措施。** 公司称其图像分类器可经免费 API 提供给通过审核的组织，帮助人工审核人员优先处理内容；ChatGPT 也增加风险警告、24 小时暂停和专业帮助入口。测试结果和适用效果仍是厂商披露，不能直接代表各组织上线后的表现。[官方文章](https://openai.com/index/strengthening-online-child-safety) · [本地正文](../raw/2026-11-17/rss-fulltext/openai-blog/openai-blog-strengthening-the-fight-against-online-child-sexual-abuse-with-new-too-b1c71d0787.opencli.md)（official-source）。AIHOT 同文发现的 GUID 为 cidgb5cgquwqxtiydrzykwc2p，站内项是[聚合站链接](https://aihot.news/items/cidgb5cgquwqxtiydrzykwc2p)，不替代官方原文。
3. **OpenAI 宣布由外部机构参与模型评估。** Apollo Research、METR、Transluce 和 Goodfire 将按约定范围检查模型、代码、训练与评估材料及监控。监督委员会会收到未删节报告，但公开披露仍可能删去保密内容或延迟；首阶段的评估结论尚未公布。X 公告在本日窗口内，配套官方正文已读，原文发布时间仍为未知。[X 公告](https://x.com/OpenAI/status/2122359930628063248) · [官方文章](https://openai.com/index/our-first-phase-of-embedded-assessments) · [正文归档](../raw/2026-11-17/official-link-candidates/openai-2122359930628063248-our-first-phase-of-embedded-assessments.opencli.md)（direct-x；配套正文为 official-source）。
4. **OpenAI 展示医疗团队的电脑操作代理。** 文章举例包括只生成待审批草稿、在病历含糊时询问人员，以及提交前等待确认；另有厂商转述的 CVS 生产场景和内部任务评测。这些材料混合了演示、合作方描述和公司评测，不足以证明通用临床安全。相关 X 帖在本日窗口内，但文章页日期只显示 11 月 16 日、没有时区，候选原文发布时间仍为未知。[X 帖](https://x.com/OpenAI/status/2122419941756531150) · [官方正文归档](../raw/2026-11-17/official-link-candidates/openai-2122419941756531150-advancing-computer-use-for-healthcare-teams.opencli.md)（direct-x；配套正文为 official-source）。
5. **Redwood Research 质疑 Gemini 4 安全报告的证据充分性。** 作者认为 Carbon 的告警减少可能来自监测覆盖、任务组合等变化，现有报告不足以单独证明失控风险已降到很低；文章也追问什么结果会改变发布判断。这是对公开安全论证的外部分析，不是独立事故率或真实部署风险估计。[Redwood 原文](https://blog.redwoodresearch.org/p/gemini-4-safety-reports-dont-demonstrate) · [本地正文](../raw/2026-11-17/rss-fulltext/aihot-selected/aihot-selected-redwood-research-gemini-4-f671840a04.extracted.md)（AIHOT 发现，secondary-source）。
6. **NVIDIA 发布智能体技能评估工具 SkillEvaluator。** README 描述了格式、安全与兼容性检查、语义重复检测，以及在沙箱中比较有无技能时的任务表现。项目自称仍处于实验阶段，本轮只读 README、未运行，因此不能把静态评分或合成任务当作技能真实效果。[GitHub 仓库](https://github.com/NVIDIA/SkillEvaluator) · [README](../raw/2026-11-17/github-trending-readmes/NVIDIA__SkillEvaluator.md)（secondary-source）。

## 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- OpenAI 的科研访问扩展和儿童安全更新都有窗口内 RSS 正文，正文均已归档；科研访问的 X 帖与 RSS 指向同一篇文章，合并为一个信号。儿童安全文章也由 AIHOT 发现；报告以独立 OpenAI RSS 正文为事实依据，同时在原始材料中保留 AIHOT GUID 与站内链接。
- OpenAI 外部评估公告和医疗电脑操作代理文章由窗口内 X 帖引出，官方正文均可读。X 帖时间落在窗口内，但两篇页面的发布时间字段并不都能确认落在本日，因此按“窗口内传播、原文发布时间未知”处理。
- Codex Atom 有 5 个标题型条目、Claude Code 有 5 条重点正文；合计 4 条可读、6 条受限。Codex 0.171.0-alpha.8 和 0.171.0-alpha.9 在窗口内，但归档只有版本标题；Claude Code 最新条目 v2.1.325 在窗口外且正文可读，不能当作今日更新。[GitHub 发布记录](../raw/2026-11-17/github-items.json)。

### 模型、评估与治理

- Philipp Schmid 建议用 Gemini 4 Carbon 处理高难设计、调试和推理，用 Hydrogen 处理日常编码、工具型智能体与并行执行，也提出由前者规划、后者执行的搭配。这是作者的工作负载建议，未做独立对比；AIHOT GUID 为 zo7ubny2zjk4qoqjdoiec91b8，原帖通过公开 HTTP 读取，但发现证据仍为 secondary-source。[AIHOT 条目](https://aihot.news/items/zo7ubny2zjk4qoqjdoiec91b8) · [原帖](https://x.com/_philschmid/status/2122359669909811362) · [本地正文](../raw/2026-11-17/rss-fulltext/aihot-selected/aihot-selected-gemini-4-hydrogen-carbon-d8c84ab768.extracted.md)。
- Redwood 对 Gemini 4 控制评估的批评侧重“告警更少”是否能区分模型行为变化与监测变弱。文章是作者对 Google DeepMind 安全报告的解读，不能单独确定部署风险。[AIHOT 条目](https://aihot.news/items/naql5xzzrykngxhvhd6vin5yn)保留 GUID 与聚合站 provenance；原文链接和本地正文见高信号条目。
- OpenAI 的 Science at the Frontier 研究文章分析 1,819 名科研项目参与者的 580,186 条分类消息，并调查 251 人；受访者估计同等质量的工作不用 AI 约需 1.9 倍时间。这个数字是自报估计，不是因果生产率评测。该文章的 RSS 发布时间为本日窗口外；X 研究结果帖在窗内。[官方文章](https://openai.com/index/science-at-the-frontier) · [本地正文](../raw/2026-11-17/rss-fulltext/openai-blog/openai-blog-science-at-the-frontier-how-scientists-use-chatgpt-f891bd93f3.opencli.md) · [X 帖](https://x.com/OpenAI/status/2122380010287960095)（RSS outside-window；X 为 direct-x）。
- X 主题摘要中另有 OpenAI 的外部评估合作和科研计划公告，均标记 direct-x；具体范围以已读官方正文为准，评估结果仍待公布。

### 企业应用与智能体工作流

- OpenAI 的医疗电脑操作文章展示了审批、暂停和补问等人为控制点；其临床场景仍属公司披露和合作方演示，不能推广为普适安全结论。
- GitHub Trending 的 NVIDIA SkillEvaluator 聚焦技能质量评估；AG-UI 描述智能体与前端间的事件和状态协议；Plannotator 提供计划、网页及代码差异的本地审阅界面。三者均来自 README 自述，尚未独立运行或验证兼容性、权限边界。
- forward-deployed 主题的窗口内 X 帖只有 rauchg 对 trace 作为软件与智能体协作原语的个人判断；它没有客户现场或企业部署证据。[帖子](https://x.com/rauchg/status/2122391135129858507)（direct-x）。

### GitHub Trending 项目

本轮 10 个项目均读到 README。以下介绍结合榜单描述和 README；上榜只说明本轮观察到其进入榜单，功能、评测与部署声明仍是项目方自述。

- [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) 用事件协议把不同框架的智能体接到网页或移动应用；协议消息包括文本、工具调用和运行状态，并描述了共享状态更新、人工审核后继续运行的机制。真实互通情况与工具调用权限本轮未验证。[README](../raw/2026-11-17/github-trending-readmes/ag-ui-protocol__ag-ui.md)（secondary-source）。
- [backnotprop/plannotator](https://github.com/backnotprop/plannotator) 在本地浏览器中审阅智能体计划、HTML 和代码差异，逐行批注可返回原会话；Inbox 汇总多个会话的问题和产物。README 提到远程模式会监听所有网络接口且不设登录，分享链接持有者也可访问内容，部署时应先核对网络暴露与分享范围。[README](../raw/2026-11-17/github-trending-readmes/backnotprop__plannotator.md)（secondary-source）。
- [dream-num/univer](https://github.com/dream-num/univer) 为产品嵌入表格、文档、公式计算和内容处理，编辑器与智能体可共用内容快照、命令和应用接口。README 区分 Apache-2.0 Web 核心与另行授权的实时协作、Office 文件转换及部分 AI 模块；身份验证由集成方负责。[README](../raw/2026-11-17/github-trending-readmes/dream-num__univer.md)（secondary-source）。
- [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) 用 YAML 流程组织市场观察、交易前风险检查、仓位计算和交易日志，面向个人投资者的研究与流程辅助。部分步骤连接行情或券商；README 未提供独立实盘收益证据，使用前需要核对持仓数据与券商凭据权限。[README](../raw/2026-11-17/github-trending-readmes/tradermonty__claude-trading-skills.md)（secondary-source）。
- [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) 汇集 Claude Code 安全评估技能、命令和报告流程，README 描述授权范围核对、证据处理与问题分级。主动测试能力带来权限风险，本轮未验证它能否强制阻止超出授权范围的操作。[README](../raw/2026-11-17/github-trending-readmes/elementalsouls__Claude-BugHunter.md)（secondary-source）。
- [getarcaneapp/arcane](https://github.com/getarcaneapp/arcane) 是带图形界面的 Docker 管理工具；README 区分 main 的 v3 与旧版本分支，另有部署、配置文档和软件物料清单。本轮只读文档，没有验证部署方式、权限隔离或安全性。[README](../raw/2026-11-17/github-trending-readmes/getarcaneapp__arcane.md)（secondary-source）。
- [DeanChensj/jiangshan-map](https://github.com/DeanChensj/jiangshan-map) 是中国历史地理学习用的交互地图，可按时期切换疆域、查询地点沿革，并展示人物与诗文路线。README 将古疆界标为示意；部分府州县边界受数据许可限制，GeoJSON 导出范围也有限，不能当作权威边界资料。[README](../raw/2026-11-17/github-trending-readmes/DeanChensj__jiangshan-map.md)（secondary-source）。
- [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) 将 Stitch 的界面生成、设计规范提取和 React/React Native 转换整理成可供智能体调用的技能。部分流程会上传 HTML、图像或设计资产；README 也声明该项目未获 Google 官方支持。[README](../raw/2026-11-17/github-trending-readmes/google-labs-code__stitch-skills.md)（secondary-source）。
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) 并行检索近期 Reddit、X、YouTube、Hacker News 等资料，按相关性、新鲜度和互动排序并合并成带出处的摘要。实际覆盖取决于凭据和启用项；部分来源使用登录会话，外部重排也可能收到检索片段，本轮没有运行此技能。[README](../raw/2026-11-17/github-trending-readmes/mvanhorn__last30days-skill.md)（secondary-source）。
- [NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) 先做技能格式、安全和兼容性检查，再检查语义重复，并可在沙箱中比较有无技能时的任务表现。项目称其仍属实验性；静态评分不等于真实发布证明，本轮没有运行自动评测。[README](../raw/2026-11-17/github-trending-readmes/NVIDIA__SkillEvaluator.md)（secondary-source）。

### X/Twitter 推主主题摘要

下表只列 2026-11-17 北京时间窗口内的主题帖子；同一帖子会匹配多个主题。推文和转帖中的观点代表发布者表达，不等于已核实的产品事实。每条均为 direct-x。

| 主题 | 窗口内帖子 |
| --- | --- |
| 前沿模型 | OpenAI 公告将扩大科学家免费使用前沿模型的范围；[帖子](https://x.com/OpenAI/status/2122377585523126615)。Hesamation 推测 GPT-6.2 延迟与安全债务有关；[帖子](https://x.com/Hesamation/status/2122390973141414280)，这是未经证实的个人判断。 |
| 智能体与工作流 | Greg Isenberg 提议把客户常用工作流整理成技能并开源；[帖子](https://x.com/gregisenberg/status/2122420795716653204)。OpenAI 也介绍了外部模型评估安排；[帖子](https://x.com/OpenAI/status/2122359930628063248)。前者是创业者观点，后者是公司公告。 |
| 编程智能体与开发工具 | Kloss 转发 Matt Pocock 对 AI 编程近一年的回顾；[转帖](https://x.com/kloss_xyz/status/2122372793513951581)。用户 Corbin Braun 称 Cursor 已允许为 Bugbot 代码审查选择模型；[帖子](https://x.com/corbin_braun/status/2122438627330555913)，本轮没有独立核实。Steipete 转发了 Codex 团队可能修复模型容量错误的说法；[转帖](https://x.com/steipete/status/2122411443576598944)，没有对应发布说明佐证。 |
| AI 治理与公共信任 | OpenAI 公布与 Apollo Research、METR、Transluce、Goodfire 开展外部评估；[帖子](https://x.com/OpenAI/status/2122359930628063248)。科学家访问扩展与研究结果也由 OpenAI 发布；[访问扩展](https://x.com/OpenAI/status/2122377585523126615) · [研究结果](https://x.com/OpenAI/status/2122380010287960095)。Hesamation 关于 GPT-6.2 延迟原因的说法没有证据支持；[帖子](https://x.com/Hesamation/status/2122390973141414280)。 |
| AI 基础设施与开源 | 本窗口没有高相关帖子；主题摘要里的 1 条记录位于本日窗口外。 |
| 独立开发与个人创业 | Greg Isenberg 认为 SaaS 团队可以把客户工作流整理为技能并开源；[帖子](https://x.com/gregisenberg/status/2122420795716653204)。这是市场观点，没有用户或收入数据佐证。 |
| 产品、增长与市场进入 | Greg Isenberg 分享开源工作流技能的产品思路；[帖子](https://x.com/gregisenberg/status/2122420795716653204)。Genspark 预告黑五折扣；[帖子](https://x.com/genspark_ai/status/2122419052379623702)，属于促销信息。 |
| 智能体系统与自动化 | Greg Isenberg 提出将客户工作流转为开源技能；[帖子](https://x.com/gregisenberg/status/2122420795716653204)。Rauch 认为软件会转向个性化、用户可控与开源；[帖子](https://x.com/rauchg/status/2122396034186014919)。EXM7777 转述 Nasiko Labs 的智能体运行平台介绍；[转帖](https://x.com/EXM7777/status/2122421709898915906)，功能仍是发布者描述。 |
| 企业部署与 FDE | rauchg 将 trace 描述为软件开发和智能体协作的新原语；[帖子](https://x.com/rauchg/status/2122391135129858507)。这是个人判断，不是客户现场或企业部署案例。 |

### 播客 / 长对话

follow-builders 本轮 offered 1 集，来自 No Priors：《Tokenization, Agentic Trading, Harmonic: Robinhood's Mission to Expand Ownership with CEO Vlad Tenev》，GUID 03f99d40-d8c2-11f1-9c96-7b13ace0b070，发布时间为 2026-11-05 11:00 UTC，位于本日窗口外，因此不写当天洞察。聚合 transcript 状态 ok，共 48,817 字符；元数据标记说话人与时间戳覆盖均为 true，但本轮未阅读窗外 transcript，也未复核音频。节目 RSS 未按 GUID 找到单集链接；上游 URL 只是 [No Priors YouTube 频道](https://www.youtube.com/@NoPriorsPodcast)，不能作为单集链接。该 transcript 仍是 secondary-source，不能据此说所有配置节目都没有更新。

## 来源证据表

| 来源 | 本轮状态与覆盖 | 证据等级与本地入口 |
| --- | --- | --- |
| RSS/Atom | 32/33 源成功；44/44 个匹配或一手重点正文读取成功；dwarkesh-patel 返回空响应 | [rss-items.json](../raw/2026-11-17/rss-items.json) |
| AIHOT 精选 RSS | 最新 50 条；7 条在窗内、43 条在窗外；3 条匹配并读取原文，4 条未命中而跳过；发布时间、GUID、聚合站及原文链接均完整 | 发现证据为 secondary-source；[XML 快照](../raw/2026-11-17/rss-feeds/aihot-selected.xml) · [采集记录](../raw/2026-11-17/rss-items.json) |
| GitHub Releases | 7/7 Atom 源成功；10 条一手重点正文 4 ok、6 limited | [github-items.json](../raw/2026-11-17/github-items.json)；受限条目的版本和本地路径在其中记录 |
| GitHub Trending | 10 个项目；描述与 README 10/10 可读 | README 自述、secondary-source；[Trending 记录](../raw/2026-11-17/github-trending.json) |
| 官方页面 | 4 个成功、1 个 limited；Anthropic Engineering 索引解析 0 个有效卡片 | [official-pages.json](../raw/2026-11-17/official-pages.json)；OpenAI News 使用 opencli-read |
| X/Twitter | twitterapi.io 50/50 账号请求成功，原始帖子 920 条，保留 148 条 | 帖子为 direct-x；[API 结果](../raw/2026-11-17/twitterapi-io-results.json) · [主题摘要](../raw/2026-11-17/twitter-topic-brief.json) |
| follow-builders 播客 | 状态 ok；offered/inside/outside/unknown 为 1/0/1/0；transcript 1/0；单集链接 0/1；上游错误 0 | transcript 为聚合 secondary-source；[podcast-items.json](../raw/2026-11-17/podcast-items.json) · [feed 快照](../raw/2026-11-17/podcasts/follow-builders/feed-podcasts.json) · [本地 transcript](../raw/2026-11-17/podcasts/follow-builders/transcripts/tokenization-agentic-trading-harmonic-robinhood-s-mission-to-expand-ownership-wi-177edd54d1f6.md) |

## X/Twitter 覆盖说明

twitterapi.io 本轮请求配置中的 50 个账号，50/50 返回成功，返回 920 条原始帖子并保留 148 条匹配记录。4 个账号本轮返回 0 条；这只表示服务本轮没有返回帖子，不说明账号没有更新。主题摘要存在跨主题重复，日报只列北京时间窗口内的帖子。帖子均标记 direct-x；转帖观点仍归属于原作者。未使用登录态浏览器、Exa 或 X 写操作。[API 原始结果](../raw/2026-11-17/twitterapi-io-results.json) · [主题 brief](../raw/2026-11-17/twitter-topic-brief.json)。

## 不确定性与待验证项

- dwarkesh-patel feed 返回 curl: (52) Empty reply from server，该来源覆盖缺失。
- Anthropic Engineering 索引抓取后没有解析出有效文章卡片，状态为 limited；不能据此推断当天没有文章。
- 6 条一手重点发布正文受限：Codex 0.171.0-alpha.5 至 0.171.0-alpha.9，以及 Claude Code v2.1.322。其中窗口内的 Codex alpha.8 与 alpha.9 只有版本标题，具体功能改动未知。
- AIHOT 只返回最新 50 条。窗口内 4 条匹配规则未命中，按配置跳过原文；其标题与摘要不能替代原文。另 3 条匹配原文均已读取；包括 Philipp Schmid 的公开 X 原帖也保持 secondary-source，没有升级为 direct-x。AIHOT 站内链接、GUID、feed 时间和原始链接保存在[采集记录](../raw/2026-11-17/rss-items.json)和[XML 快照](../raw/2026-11-17/rss-feeds/aihot-selected.xml)中。
- 5 个官方链接候选正文均成功读取，但页面发布时间有未知或冲突。科研访问扩展与官方 RSS 同文，合并计数；Science at the Frontier 对应的 X 帖在窗口内，但其 RSS 发布时间在窗外，文章讨论的生产率来自受访者自报。Standard Model 客座文的 X 帖在窗外，页面显示 11 月 15 日而抓取元数据时间不同，且内容指向十月预印本，因此不作为今日新进展。[OpenAI X 帖](https://x.com/OpenAI/status/2122123437141553630) · [正文归档](../raw/2026-11-17/official-link-candidates/openai-2122123437141553630-step-toward-defining-the-standard-model.opencli.md) · [候选记录](../raw/2026-11-17/official-link-candidates.json)。
- X/Twitter 的 920 条是 API 本轮返回量，148 条是筛选后的保留记录；它们不构成完整账号时间线。帖子中的市场观点、转帖和容量错误传闻尚未独立验证。
- GitHub Trending 的项目功能主要来自 README 自述，尚未逐项运行或复核。涉及交易技能、主动安全测试、远程管理及用户数据传输的项目，应先核对权限、凭据和数据路径。
- 播客本轮 offered 1 集，发布时间在窗口外；聚合 transcript 可读，但没有 canonical 单集链接，只有节目频道地址。尽管 transcript 元数据标记说话人与时间戳覆盖均为 true，本轮仍未阅读该窗外内容或复核音频。14 天 lookback 只代表上游本轮提供范围；不能将本轮 1 集或 inside=0 解释成所有配置节目均无更新。[采集记录](../raw/2026-11-17/podcast-items.json) · [feed 快照](../raw/2026-11-17/podcasts/follow-builders/feed-podcasts.json) · [本地 transcript](../raw/2026-11-17/podcasts/follow-builders/transcripts/tokenization-agentic-trading-harmonic-robinhood-s-mission-to-expand-ownership-wi-177edd54d1f6.md)。

## 当天产物

- 日报：[2026-11-17-daily-intel.md](2026-11-17-daily-intel.md)
- 流程与阅读输入：[run-summary.json](../raw/2026-11-17/run-summary.json) · [report-reading-list.json](../raw/2026-11-17/report-reading-list.json) · [manifest.json](../raw/2026-11-17/manifest.json) · [signals.json](../raw/2026-11-17/signals.json)
- 候选审计：[JSON](../reviews/2026-11-17-candidate-audit.json) · [Markdown](../reviews/2026-11-17-candidate-audit.md)
- AIHOT：[XML 快照](../raw/2026-11-17/rss-feeds/aihot-selected.xml) · [采集记录](../raw/2026-11-17/rss-items.json)
- 播客：[podcast-items.json](../raw/2026-11-17/podcast-items.json) · [follow-builders feed 快照](../raw/2026-11-17/podcasts/follow-builders/feed-podcasts.json) · [本地 transcript](../raw/2026-11-17/podcasts/follow-builders/transcripts/tokenization-agentic-trading-harmonic-robinhood-s-mission-to-expand-ownership-wi-177edd54d1f6.md)

## 边界与验证

本日报以 raw/2026-11-17/ 的采集归档为证据入口，日期窗口按北京时间计算。AIHOT 精选和 follow-builders transcript 维持聚合来源边界；X 帖子保留 direct-x；GitHub Trending 与 README 自述属于发现材料。报告不声称覆盖全部 AI 新闻、完整 X 时间线或 follow-builders 配置的全部节目，也不把受限正文、未知发布时间或未复核的评测结果写成已确认事实。

<!-- dsi-candidate-audit: covered=21 missed=61 -->
