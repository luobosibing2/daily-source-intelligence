# 每日情报：2026-11-27

> 运行日期：2026-11-27（Asia/Shanghai）。采集窗口按北京时间自然日；来源对时间字段和回看范围的支持不同，具体边界见下文。

## 采集范围

- 新增去重状态记录 `seen_added=40`；统一入口派生 16 条阅读清单候选，其中 4 条有可读正文、12 条为正文受限或结构化 X 证据。统一入口、状态和路径摘要见[运行摘要](../raw/2026-11-27/run-summary.json)、[manifest](../raw/2026-11-27/manifest.json)和[阅读清单](../raw/2026-11-27/report-reading-list.json)。
- RSS/Atom 33 个来源中 32 个成功；51/51 条命中或一手重点正文读取成功，154 条按规则未尝试全文。`dwarkesh-patel` 返回 `curl: (52) Empty reply from server`。AIHOT 精选源读取最新 50 条，feed 状态 `ok`；1 条在窗口内且命中主题，49 条窗口外，0 条时间未知。50 条均保留原文链接；唯一追读的原文 `fulltext_status=ok`、方法为 `curl`，其余 49 条因窗口外未尝试全文。
- GitHub Releases 7/7 个 Atom 来源成功；10 条一手重点版本正文中 5 条可读、5 条只有版本标签而受限。GitHub Trending 解析 10 个项目，项目描述和 README 均为 10/10 可读。
- 官方页面 4/5 个来源成功。`OpenAI News` 通过 `opencli-read` 读取，但未解析出当日文章；`Anthropic Engineering` 索引由 `curl` 读取却解析出 0 张有效文章卡，按受限覆盖处理，不能据此判断当日无文章。
- `twitterapi.io` 的 50/50 个账号请求成功，保留 215 条 `direct-x`；这是有限时间线采样，不是完整账号历史。播客使用已配置的 follow-builders 公共 feed，状态、窗口和 transcript 覆盖见[播客产物](../raw/2026-11-27/podcast-items.json)。

## 今日高信号

1. **FDE 的工作重心开始从写代码转向设计客户反馈如何进入产品和交付循环。** FDE Hub 一周年文章描述了同一职位名称下的客户嵌入工程师、售前、多人交付小组和初创公司首位 FDE 等不同岗位，也指出代码生成加快后，系统设计、验证、CI/CD 和部署成为更多工作。文章所引调查只有 24 份答复；17 位为客户写生产代码的人中，4 人说代码回并入核心产品、9 人说留在客户专用实现，作者观点和小样本不能代表整个行业。[文章原文](https://www.fdehub.org/p/fde-hub-one-year-in) · [本地全文](../raw/2026-11-27/rss-fulltext/fde-hub/fde-hub-fde-hub-one-year-in-85cf13810c.extracted.md)（`secondary-source`）。
2. **一条 AIHOT 收录的 X 案例称 Claude Code 与 Opus 5.5 用公开数据搭建了美国文明风格地图。** 聚合摘要称项目用了 31 个数据源，耗时约 7 小时并生成约 45,000 行代码；可读 X 页面显示这是 Ado 转述 Andrej Karpathy 的项目描述。它提供了多源数据整合和长任务编码的探索线索，但成果与数字没有独立复核，证据仍为 `secondary-source`。[原帖页面](https://x.com/adocomplete/status/2125994186252161315) · [AIHOT 站内条目](https://aihot.news/items/gc4qp85ij5qzhu53qzkg8quqj) · [本地正文](../raw/2026-11-27/rss-fulltext/aihot-selected/aihot-selected-karpathy-claude-code-opus-5.5-399e1c4b0d.extracted.md)。

## 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Codex Atom 返回 `rust-v0.174.0-alpha.8` 及此前四个 alpha 版本。最新条目更新时间为 `2026-11-26T20:53:08Z`（北京时间 11 月 27 日 04:53）；其余四条早于本次窗口。五条 release body 都只有版本标签，均为 `limited`，因此只能报告版本，不能推断功能变化。[alpha.8 release](https://github.com/openai/codex/releases/tag/rust-v0.174.0-alpha.8) · [本地受限正文](../raw/2026-11-27/github-release-fulltext/openai-codex/openai-codex-rust-v0.174.0-alpha.8-8b54564126.atom.md)。
- Claude Code Atom 返回最近五个版本 `v2.1.328`–`v2.1.332`，正文均可读；最新 `v2.1.332` 更新时间是 `2026-11-25T01:32:14Z`，早于本次窗口，本轮没有当日 Claude Code release。其正文包含 MCP server skills（beta）、`PreSkillShellCommand` hook 和多项会话保存、挂起及运行可靠性修复，但不作为今日新增。[v2.1.332 release](https://github.com/anthropics/claude-code/releases/tag/v2.1.332) · [本地正文](../raw/2026-11-27/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.332-15aa96a954.atom.md)。

### Forward Deployed Engineering / Enterprise AI Deployment

- FDE Hub 文章认为，FDE 的价值取决于能否把客户现场学到的需求反馈回产品，而不只是完成单客户实现；在代理能写更多代码时，工作也转向设计系统、验证和交付循环。小样本调查显示回并核心产品的比例有限，但该结果仅能作为待跟踪线索，不能外推为行业统计。[文章](https://www.fdehub.org/p/fde-hub-one-year-in) · [全文归档](../raw/2026-11-27/rss-fulltext/fde-hub/fde-hub-fde-hub-one-year-in-85cf13810c.extracted.md)。

### LLM / Agent / AI Coding

- AIHOT 当天唯一命中的条目是上述 Karpathy 地图案例。feed 的标题、摘要和 GUID `gc4qp85ij5qzhu53qzkg8quqj` 保留为聚合来源；公开 X 原文页面通过 `curl` 读取，采集器标记全文 `ok`，但聚合来源等级仍为 `secondary-source`，没有升级为 `direct-x`。[AIHOT feed](https://aihot.news/feed.xml) · [站内条目](https://aihot.news/items/gc4qp85ij5qzhu53qzkg8quqj) · [X 原文页面](https://x.com/adocomplete/status/2125994186252161315)。
- 窗口内 X 主题摘要还有两条低强度案例线索：`gregisenberg` 转述有人用 Claude 和低成本芯片读取旧 Jeep 车载电脑，帖子未提供可复核项目或测量；`kloss_xyz` 转推 Meng To 的 Three.js 摩托场景，称用了 GPT-6.2 Astra、视差和鱼眼效果并分享 Skills。两条都是 `direct-x` 帖文证据，不代表项目效果已独立核实。[Jeep 诊断转述](https://x.com/gregisenberg/status/2126004403052445733) · [Three.js 场景转推](https://x.com/kloss_xyz/status/2126000587292672378)。

### GitHub Trending 项目发现

以下十项依据当天 GitHub Trending 项目卡和各自 README 归纳；上榜仅是发现信号，不能证明项目质量、普及程度或使用效果。全部 README 均已归档且状态为 `ok`，见[项目记录](../raw/2026-11-27/github-trending.json)和[README 目录](../raw/2026-11-27/github-trending-readmes/)。

- [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)：用七阶段流程分析桌面软件、生成带 JSON 输出和测试的命令行接口，并用 CLI-Hub 管理已有 CLI。它面向希望让代理调用专业软件的开发者；README 也指出包装后的命令仍可能依赖原软件安装，不能据此认为可控制所有软件。
- [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)：把自然语言需求转成独立 HTML 与内嵌 SVG 图表，可从多种图表格式导入，并用 fidelity ledger 记录内容取舍。它适合较稳定的说明图；频繁变化的图表不如可 diff 的 Mermaid，默认字体还会联网请求。
- [cursor/plugins](https://github.com/cursor/plugins)：Cursor 插件市场目录，通过 marketplace 与单插件清单组织 Skills、规则、MCP 配置及 SaaS 集成。README 证明的是目录结构，不是各插件的运行效果或权限范围；涉及企业系统读写时应逐项检查授权。
- [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter)：面向 Claude Code 的安全测试 Skill 包，README 描述从侦察、排序、验证到报告的流程，并限定在自有或书面授权资产。它具有双用途，README 自述的技能数与报告数没有独立验证。
- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)：提供网页抓取、爬取、映射的本地 Rust 工具、MCP 与本地 API；本地读取失败时可回退 Firecrawl Cloud。完整自托管不含云端 Alexandria 数据源，使用本地模式也需核查云回退设置和数据外发边界。
- [jingyaogong/minimind](https://github.com/jingyaogong/minimind)：用原生 PyTorch 教学展示小型 Dense/MoE 模型的预训练、微调、偏好优化、工具调用和 Agent 强化学习。README 报告的时间与费用是特定硬件上的估算；64M 参数教学模型不能视作前沿或生产能力证明。
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)：把 Reddit、X、YouTube、GitHub 等来源汇总为带引用的研究简报，可按新鲜度和相关性排序并合并重复故事。实际覆盖依赖 API 凭据、浏览器会话和可选工具；主题与片段可能发给自动选择的推理服务。
- [nginx/nginx](https://github.com/nginx/nginx)：成熟的 Web 服务器、反向代理、负载均衡和缓存项目；README 说明主进程管理工作进程、工作进程处理流量，并以共享内存传递部分状态。它是本日榜单发现，不是新发布或 AI 领域趋势信号。
- [obra/superpowers](https://github.com/obra/superpowers)：面向编程代理的流程 Skills，覆盖需求澄清、计划、隔离 worktree、任务委派、测试和审查。README 描述的是预期工作流，实际触发和宿主兼容性仍须按版本验证。
- [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino)：把 PyTorch、TensorFlow、ONNX 等模型转换并优化到 Intel CPU、GPU、NPU 推理，Python 示例通过 `convert_model` 和 `compile_model` 完成部署。性能取决于设备与模型，README 提及的遥测可选择退出。

### X/Twitter 推主主题摘要

按北京时间目标日筛选 [twitter-topic-brief.json](../raw/2026-11-27/twitter-topic-brief.json) 中的推文；所有链接均为 `direct-x`。其中部分帖子是转推或个人叙述，不能据此推断普遍产品表现。

- **LLM / Frontier Models：** Sam Altman 发帖谈到一位早期相信当时模型可解决千禧年难题的同事；这是个人回忆，没有提供新的模型结果或验证。[direct-x](https://x.com/sama/status/2125990371897557278)
- **AI Agent / Agentic Workflow：** Greg Isenberg 转述 Claude 辅助读取旧车 ECU 的个案；来源帖子没有可复核仓库或测量数据。[direct-x](https://x.com/gregisenberg/status/2126004403052445733)
- **AI Coding / Developer Tools：** Meng To 的 Three.js 视觉演示由 `kloss_xyz` 转推，提到 GPT-6.2 Astra、视差和鱼眼技巧；属于创作者案例，不是独立代码评测。[direct-x 转推](https://x.com/kloss_xyz/status/2126000587292672378)
- **AI Governance / Public Legitimacy：** Simon Willison 评论有人收到以 AI 套话开头的求职邮件，并引用 Kenton Varda 的观察；这是个人体验，不代表招聘数据。[direct-x](https://x.com/simonw/status/2125998873252605954)
- **AI Infrastructure / Open Source：** Garry Tan 转推 DHH 关于 Inkling2 Mini 与 Qwen3.8 27B 在特定 48–64GB RTX Spark 环境中的夜间比较；未经独立复测，不能写成通用模型排名。[direct-x 转推](https://x.com/garrytan/status/2126060072128184750)
- **Indie Hacking / Solo Founder 与 Product / Growth / GTM：** 当天入选的主要相关帖子是上述 Jeep 诊断个案（`direct-x`）；它同时匹配多个主题，不构成第二份独立证据。[原帖](https://x.com/gregisenberg/status/2126004403052445733)
- **AI Systems / Automation：** 当天较具体的内容是上述 Three.js 演示（`direct-x` 转推），未显示新的自动化运行机制或生产部署证据。[转推](https://x.com/kloss_xyz/status/2126000587292672378)
- **Forward Deployed Engineering / Enterprise AI Deployment：** 本日 X 样本没有明确的 FDE 专属内容；FDE 观察来自上方 FDE Hub 文章。

### 播客 / 长对话

follow-builders 本轮状态 `ok`，上游 offered 1 集：inside/outside/unknown = 0/1/0；transcript ok/limited = 1/0；canonical episode link ok/limited = 1/0；上游错误 0。唯一节目是 Training Data 的《OpenAI’s Noam Brown: Why Game Theory Didn’t Lead to General Intelligence》，GUID `fa4bc7f0-e514-11f1-8a20-23a2aece5414`，发布时间为 2026-11-24 10:00 UTC，早于本次北京时间窗口。transcript 可读，speaker 和 timestamp 覆盖均为 true，但没有窗口内 transcript，因此不写当天洞察卡。上游中央 feed 提供 1 集，不等于逐一确认所有配置节目均无更新；transcript 是聚合站材料，未做音频复核。

- 单集链接：[YouTube](https://www.youtube.com/watch?v=tRaFbDFBl_A)
- follow-builders feed 快照：[feed-podcasts.json](../raw/2026-11-27/podcasts/follow-builders/feed-podcasts.json)
- 规范化覆盖记录：[podcast-items.json](../raw/2026-11-27/podcast-items.json)
- 窗口外本地 transcript：[Markdown](../raw/2026-11-27/podcasts/follow-builders/transcripts/openai-s-noam-brown-why-game-theory-didn-t-lead-to-general-intelligence-live-at-07e49c53be04.md)

## 来源证据表

| 来源 | 实际状态 | 证据与边界 |
| --- | --- | --- |
| RSS/Atom | 32/33 来源成功；51/51 命中全文可读；1 源连接失败。 | [rss-items.json](../raw/2026-11-27/rss-items.json)。`dwarkesh-patel` 为 `curl: (52) Empty reply from server`；其他源成功。 |
| AIHOT 精选 RSS | 抓取状态 `ok`；最新 50 条中 inside/outside/unknown = 1/49/0；原始链接 50 条均有效；唯一窗口内相关原文读取 `ok`（`curl`），其他 49 条按窗口规则跳过。 | feed 保留 GUID、站内链接和原始链接；[原始 feed 快照](../raw/2026-11-27/rss-feeds/aihot-selected.xml)、[RSS 条目快照](../raw/2026-11-27/rss-items.json)、[站内条目](https://aihot.news/items/gc4qp85ij5qzhu53qzkg8quqj)、[原始 X 页面归档](../raw/2026-11-27/rss-fulltext/aihot-selected/aihot-selected-karpathy-claude-code-opus-5.5-399e1c4b0d.extracted.md)。feed 标题/摘要和条目证据等级始终为 `secondary-source`。 |
| GitHub Releases | 7/7 Atom 来源成功；一手重点正文 5 ok、5 limited。 | [github-items.json](../raw/2026-11-27/github-items.json)。Codex 五个 alpha 正文都只有版本标签；Claude Code 五个版本正文可读，最新一个早于本轮窗口。 |
| GitHub Trending | 10 个项目，项目描述 10/10、README 10/10。 | [github-trending.json](../raw/2026-11-27/github-trending.json)及[README 快照](../raw/2026-11-27/github-trending-readmes/)；均按 `secondary-source` 发现线索处理。 |
| 官方页面 | 4/5 成功，Anthropic Engineering 受限。 | [official-pages.json](../raw/2026-11-27/official-pages.json)。OpenAI News 使用 `opencli-read`，当日文章 0；Anthropic Engineering `curl` 成功但解析 0 卡片，不能当作零新增。 |
| X/Twitter | `twitterapi.io` 50/50 账号成功；215 条保留 `direct-x`。 | [API 结果](../raw/2026-11-27/twitterapi-io-results.json)和[主题摘要](../raw/2026-11-27/twitter-topic-brief.json)。使用公开 HTTP 证据；没有登录态回退，也不代表完整时间线。 |
| 播客 / 长对话 | follow-builders `ok`；offered/inside/outside/unknown = 1/0/1/0；transcript ok/limited = 1/0；link ok/limited = 1/0；错误 0。 | [podcast-items.json](../raw/2026-11-27/podcast-items.json)、[feed 快照](../raw/2026-11-27/podcasts/follow-builders/feed-podcasts.json)、[窗口外 transcript](../raw/2026-11-27/podcasts/follow-builders/transcripts/openai-s-noam-brown-why-game-theory-didn-t-lead-to-general-intelligence-live-at-07e49c53be04.md)。证据等级固定为 `secondary-source`。 |

## X/Twitter 覆盖说明

本轮从 `twitterapi.io` 读取配置中的 50 个账号，50/50 成功，保留 215 条近期直接帖子并标为 `direct-x`。主题摘要按发布时间换算成北京时间后再筛选；一条帖子可以匹配多个主题，不能按主题重复计作多个独立信号。X 原文和链接候选均使用公开 HTTP，没有使用登录浏览器、Exa 或写操作。

两个官方链接候选来自 `direct-x` 帖子，发布时间都早于 11 月 27 日目标日：Anthropic 的迁移文章链接来自 11 月 25 日 16:26 UTC 的帖子，Cookout 链接来自 11 月 25 日 10:41 UTC 的帖子。两个目标网页都成功归档，但不作为本日新增；候选审计会记录其日期处置。[Anthropic 正文](../raw/2026-11-27/official-link-candidates/anthropicai-2125627317263466739-migrating-api-to-rust.extracted.md) · [Cookout README 页面](../raw/2026-11-27/official-link-candidates/mattpocockuk-2125540436483711074-cookout.extracted.md)。

## 不确定性与待验证项

- `dwarkesh-patel` RSS 的 `Empty reply from server` 是单一 feed 失败；其余独立来源运行成功，因此本轮没有因跨源连接故障重跑统一命令。该 feed 当日覆盖仍缺失。
- AIHOT 只覆盖当时返回的最新 50 条。本轮 1 条窗口内匹配并读取原文、49 条窗口外；摘要、feed GUID 和站内链接保留在快照中。AIHOT 是有限发现源，不是全量 AI 新闻目录；窗口外、时间未知或缺少原文的条目不升级为已读原文。
- Anthropic Engineering 索引解析 0 张卡片，状态为 `limited`；这不是当日无文章的证据。Codex `v0.174.0-alpha.8` 的正文只含版本字符串，功能变更待正式 release body 或其他一手材料核实。
- X 只读取近期有限样本。帖子、转推和个人轶事都只支持“该账号发布了此说法”，不证明帖子中的产品效果、模型能力、价格或使用规模；超出目标日的官方链接候选已按日期排除。
- 播客 offered 1 集且发布时间窗口外；transcript 虽可读、speaker/timestamp 覆盖为 true，仍是聚合 transcript，未与音频复核。offered 1 不表示所有配置节目都已检查或均无更新。
- Trending 项目的机制、数量、性能、定价和安全信息来自各自 README；此榜单不代表项目质量、真实使用效果或当天发布。具体限制已在各项目摘要中标出。

## 当天产物

- 原始状态和派生索引：[manifest.json](../raw/2026-11-27/manifest.json)、[run-summary.json](../raw/2026-11-27/run-summary.json)、[report-reading-list.json](../raw/2026-11-27/report-reading-list.json)、[signals.json](../raw/2026-11-27/signals.json)
- 播客覆盖材料：[podcast-items.json](../raw/2026-11-27/podcast-items.json)、[上游 feed 快照](../raw/2026-11-27/podcasts/follow-builders/feed-podcasts.json)、[窗口外 transcript](../raw/2026-11-27/podcasts/follow-builders/transcripts/openai-s-noam-brown-why-game-theory-didn-t-lead-to-general-intelligence-live-at-07e49c53be04.md)
- AIHOT 原始 feed 和窗口内原文：[rss-items.json](../raw/2026-11-27/rss-items.json)、[HTML](../raw/2026-11-27/rss-fulltext/aihot-selected/aihot-selected-karpathy-claude-code-opus-5.5-399e1c4b0d.html)、[提取正文](../raw/2026-11-27/rss-fulltext/aihot-selected/aihot-selected-karpathy-claude-code-opus-5.5-399e1c4b0d.extracted.md)
- GitHub Trending 发现材料：[github-trending.json](../raw/2026-11-27/github-trending.json)、[README 归档目录](../raw/2026-11-27/github-trending-readmes/)
- 日报：[2026-11-27-daily-intel.md](2026-11-27-daily-intel.md)
- 候选审计：[Markdown](../reviews/2026-11-27-candidate-audit.md) · [JSON](../reviews/2026-11-27-candidate-audit.json)

<!-- dsi-candidate-audit: covered=8 missed=88 -->
