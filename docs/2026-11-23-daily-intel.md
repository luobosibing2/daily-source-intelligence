# 每日情报｜2026-11-23

## 直接答案

本轮有 **1 条高信号**：Sam Altman 在北京时间 11 月 23 日发布的 X 帖子，谈到 OpenAI 公开更多预训练进展，并支持围绕共同测量和安全门槛开展讨论。帖子链接到前一日发布的《Perplexity and Intelligence》；本地已归档并读取正文，但 RSS 发布时间为 11 月 22 日 08:00（北京时间），正文页眉却标为 11 月 20 日，因此不把文章本身算作 11 月 23 日新发布。当天帖子保留为 `direct-x`，文章正文保留为 `official-source`，两者的日期与证据边界分开处理。

统一采集与状态准备新增 41 条去重记录。正文阅读清单有 9 条，全部是 `direct-x` 结构化记录，没有本地正文；没有把 X 文本伪装成已读取的网页正文。播客本轮 `partial`：follow-builders offered 1 集，窗口内 0 集；transcript 和单集链接各成功 1 个，另有 1 个上游转写错误。详细范围见[采集清单](../raw/2026-11-23/manifest.json)、[运行摘要](../raw/2026-11-23/run-summary.json)、[信号索引](../raw/2026-11-23/signals.json)和[正文阅读清单](../raw/2026-11-23/report-reading-list.json)。

## 采集范围

- 运行日期为 `2026-11-23`（Asia/Shanghai）。统一入口 `DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-11-23` 完成；原始数据及窗口按各来源时间处理。`update-state.py` 新增 41 条，去重状态总计 8,535 条。
- 普通 RSS/Atom：33 个源中 32 个成功。主题匹配或一手重点正文尝试 45 条，45 条可读；另外 160 条按匹配规则跳过。`dwarkesh-patel` 返回 `curl: (52) Empty reply from server`。[RSS 条目](../raw/2026-11-23/rss-items.json)
- AIHOT 精选：从当前 feed 读取 50 条；北京时间本日内 0 条、窗口外 50 条、发布时间未知 0 条。50 条均有 GUID 和站内链接，原文链接状态均为可用；本轮没有主题命中，依窗口规则未读取任何链接原文。AIHOT 只作为二手发现源，标题和摘要不当作原文或 `official-source`。[条目记录](../raw/2026-11-23/rss-items.json) · [feed 原始快照](../raw/2026-11-23/rss-feeds/aihot-selected.xml)
- GitHub Releases：7/7 个 Atom 源成功。Codex 与 Claude Code 一手重点正文尝试 10 条，其中 5 条可读、5 条受限；受限项均为 Codex Atom 正文只有版本标签。[发布记录](../raw/2026-11-23/github-items.json)
- GitHub Trending：当日解析 10 个仓库，10/10 项目描述与 README 均已归档并可读。榜单仅作发现线索，不代表项目质量、实际采用或当日发布。[Trending 记录](../raw/2026-11-23/github-trending.json) · [README 归档](../raw/2026-11-23/github-trending-readmes/)
- 官方页面：5 个源中 4 个成功、1 个受限。Anthropic Engineering 索引归档成功但解析出 0 张文章卡片，状态为 `limited`，不能据此判断当日没有文章。OpenAI News 页通过 `opencli-read` 保存了索引内容，但没有解析出可计入本日的官方文章记录。[页面记录](../raw/2026-11-23/official-pages.json) · [Anthropic Engineering 索引快照](../raw/2026-11-23/official-page-text/anthropic-engineering/anthropic-engineering-anthropic-engineering-9bba7c6d8f.index.html)
- X/Twitter：`twitterapi.io` 配置的 50 个账号均成功请求；共返回 798 条原始帖子，按既有筛选保留 135 条 `direct-x`。主题 brief 中有 9 条进入当日阅读清单。[API 结果](../raw/2026-11-23/twitterapi-io-results.json) · [推主主题摘要](../raw/2026-11-23/twitter-topic-brief.json)
- 播客 / 长对话：follow-builders 状态 `partial`，上游 offered 1 集，窗口内/窗口外/未知为 0/1/0；transcript 成功/受限为 1/0，单集链接成功/受限为 1/0，上游错误 1 个。[podcast-items.json](../raw/2026-11-23/podcast-items.json) · [上游 feed 快照](../raw/2026-11-23/podcasts/follow-builders/feed-podcasts.json)。这些数量只描述中央 feed 本轮实际提供的内容，不代表逐一检查全部配置节目。

## 今日高信号

1. **OpenAI 公开预训练进展与共同安全门槛的讨论进入当日 X 信息流。** Sam Altman 的帖子发布时间为北京时间 11 月 23 日 01:12；他表示 OpenAI 正提高预训练进展透明度，并希望围绕共同限制形成共识。帖子引用 OpenAI 首席科学家 Jakub Pachocki 关于共同测量指标与安全门槛的说明。[Sam Altman 帖子](https://x.com/sama/status/2124551594691932405) · [Jakub Pachocki 帖子](https://x.com/merettm/status/2124549218995949967)。这是 `direct-x` 证据，支撑“实验室公开讨论测量与安全门槛”这一判断，不等同于独立验证政策效果。同一北京时间日，`swyx` 也引用该文讨论以困惑度衡量训练进展和安排研发节奏；这是对同一篇文章的评论，不是第二条独立研究证据。[swyx 帖子](https://x.com/swyx/status/2124583459356373052)。

   相关一手文章《Perplexity and Intelligence》提出以困惑度等测量比较训练进展，并公开部分预训练测量数据；正文还讨论跨模型可比性、下游能力、思维链与安全边界。该文章正文由 `opencli-read` 归档为 10,542 字符的可读材料，但 RSS 发布时间与正文页眉日期冲突，且对应 11 月 22 日而非本日，不把它算作本日新文章。[OpenAI 原文](https://openai.com/index/perplexity-and-intelligence) · [本地归档正文](../raw/2026-11-23/rss-fulltext/openai-blog/openai-blog-perplexity-and-intelligence-de5cd1a6d5.opencli.md)。

<!-- dsi-candidate-audit: covered=8 missed=64 -->

## 按主题分组摘要

### 一手重点源 / OpenAI 与 Claude Code

- **OpenAI：**RSS 最近条目中有《Perplexity and Intelligence》，正文已通过 `opencli-read` 完整归档；RSS 标注时间为 11 月 22 日 08:00（北京时间），而正文页眉显示 11 月 20 日。文章本身不计入 11 月 23 日新发布；当天 Sam Altman 的 X 帖子按 `direct-x` 单独列入高信号。[RSS 记录](../raw/2026-11-23/rss-items.json) · [正文归档](../raw/2026-11-23/rss-fulltext/openai-blog/openai-blog-perplexity-and-intelligence-de5cd1a6d5.opencli.md)
- **Codex：**5 条 release Atom 记录均为受限正文，内容只有版本标签，不能据版本号推断功能变化。最近版本 `0.173.0-alpha.4` 的更新时间为 11 月 21 日 08:40（北京时间），不属于本日窗口。[release 记录](../raw/2026-11-23/github-items.json) · [受限正文示例](../raw/2026-11-23/github-release-fulltext/openai-codex/openai-codex-0.173.0-alpha.4-c89ec8c212.atom.md)
- **Claude Code：**5 条正文均可读；最近的 `v2.1.330` 更新时间为 11 月 21 日 06:32（北京时间），早于本日窗口。可读 release notes 描述企业管理员登录、自托管 runner 启动目录、任务视图与循环任务，以及工具钩子、托管设置和会话恢复等功能或修复。这些是版本说明，不能替代本日新增或运行时验证。[release 记录](../raw/2026-11-23/github-items.json) · [v2.1.330 正文](../raw/2026-11-23/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.330-7ce40af713.atom.md)

### 大模型、智能体与开发工具

- **OpenAI 训练评测讨论：**Sam Altman 的当日帖子，以及 `swyx` 对同一文章的评论，都围绕预训练进展透明度、共同测量与安全门槛；后者强调以困惑度比较进展。[Sam Altman 帖子](https://x.com/sama/status/2124551594691932405) · [swyx 帖子](https://x.com/swyx/status/2124583459356373052)。两条均为 `direct-x`，但后者是评论，不构成独立验证；相关官方正文日期边界见[高信号说明](#今日高信号)。
- **T3Code 多模型创作流程：**Riley Brown 描述自己试用 T3Code 的经历，包括用手机控制浏览器、让 Claude 调用 Gemini 子代理分析视频，再由 Claude 编写编辑代码，并比较多个模型在同一上下文下处理视频的结果。[帖子](https://x.com/rileybrown/status/2124581053314850904)。这是个人体验，不是对产品稳定性、模型能力或效果的独立测评；帖子还提到价格顾虑。
- **视频工作流话题：**Riley Brown 另发帖征集讨论视频与图像模型工作流的嘉宾。[帖子](https://x.com/rileybrown/status/2124601107716739581)。它是节目邀约，没有新技术细节，不作为高信号。

### AI 治理与基础设施

- **共同评测与安全门槛：**本日主题 brief 没有单独标记 `ai-governance` 类别的 X 条目；Sam Altman 与 Jakub Pachocki 的帖子按内容放在上方，保留其原始 `direct-x` 等级。OpenAI 文章是前一北京时间日的官方材料，发布时间仍有冲突。
- **推理服务数据风险观点：**Vercel CEO Guillermo Rauch 警告免费、“隐形”及零数据留存（ZDR）推理服务可能带来数据外泄风险，并提及其公司 AI Gateway 的信任与隐私工作。[帖子](https://x.com/rauchg/status/2124595496849445079)。把风险推断与国家级项目联系起来是作者的猜测；作者也有商业利益，未提供本地归档的独立调查正文，不能当作已证实的数据泄露事件。

### 产品、增长与个人开发

- `levelsio` 对 X 上 AI 回复刷屏、屏蔽名单效果发表个人观察。[帖子一](https://x.com/levelsio/status/2124586276489695710) · [帖子二](https://x.com/levelsio/status/2124560949059240002)。帖子没有平台级数据，不能据此推断整体趋势。
- `nikunj` 转述 SaaS 业务可用“外包风险”理解客户购买结果的观点。[帖子](https://x.com/nikunj/status/2124569093806428308)。帖子指向另一篇文章，但本轮没有归档该文章正文，因此仅记录为观点线索。
- 其余当日 X 条目包括对触觉触控板发声的转发和对独立产品的评价，未作为 AI 行业信号展开。[主题摘要](../raw/2026-11-23/twitter-topic-brief.json)。

### GitHub Trending 项目

今日 10 个项目的榜单描述和 README 均已读取。以下只概括 README 能支持的用途；趋势榜单是发现来源，不表示质量背书、实际采用或运行验证。本轮没有安装或运行这些项目。

- [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) 面向希望让桌面软件接受智能体调用的开发者。README 描述一个七阶段流程，用来分析软件、生成命令行工具并附带测试与文档；README 自报覆盖 18 个应用、2,461 项通过测试。今天上榜使它成为桌面软件工具化的发现候选；这些覆盖与测试数字尚未独立核验。[README](../raw/2026-11-23/github-trending-readmes/HKUDS__CLI-Anything.md)
- [obra/superpowers](https://github.com/obra/superpowers) 为编码智能体组织软件开发步骤。README 将需求澄清、方案说明、实现计划、测试驱动开发、子代理协作和评审组合为技能流程；今天的榜单热度让这类可组合开发流程值得留意，但 README 不证明不同宿主会一致执行。[README](../raw/2026-11-23/github-trending-readmes/obra__superpowers.md)
- [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) 提供面向 Claude Code 等智能体的安全测试技能包，覆盖侦察、Web/API 检查、验证与报告，也提到 Burp MCP。README 自称包含 83 项技能、15 个命令和 681 种公开漏洞模式；今天上榜使它成为安全测试工具的发现候选。仅可在自有或明确授权的系统上使用，项目数字和检测效果未独立核实。[README](../raw/2026-11-23/github-trending-readmes/elementalsouls__Claude-BugHunter.md)
- [cursor/plugins](https://github.com/cursor/plugins) 是 Cursor 的官方插件规范与插件仓库，按目录和清单组织开发工具、生产力和 SaaS 集成。今天上榜反映插件分发与集成机制的发现价值；仓库级说明不能确认每个插件的权限、数据访问或副作用。[README](../raw/2026-11-23/github-trending-readmes/cursor__plugins.md)
- [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) 提供可用于 Claude Code、Codex 等工具的图表设计技能，生成 HTML/SVG 图表并适配品牌样式。README 列出 51 种图表类型；今天上榜使其成为智能体生成图表的候选，尚未验证输出质量或外部字体与样式获取行为。[README](../raw/2026-11-23/github-trending-readmes/cathrynlavery__diagram-design.md)
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) 用多来源材料为指定主题生成近期研究摘要，README 提到 Reddit、X、YouTube、Hacker News、Polymarket 和网页等来源。今天上榜提供一个多来源研究流程的发现线索；来源覆盖依赖外部工具或凭据，互动量和预测市场赔率不等于事实核验。本轮只读 README，没有运行该技能。[README](../raw/2026-11-23/github-trending-readmes/mvanhorn__last30days-skill.md)
- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) 提供网页搜索、抓取、遍历和映射接口，可经 API、MCP 或自托管方式使用。README 宣称支持 550 多个数据来源，并说明某些本地抓取场景会回退到云服务；今天上榜使它成为网页采集基础设施的候选，部署前应核实数据是否离开本地环境。[README](../raw/2026-11-23/github-trending-readmes/firecrawl__firecrawl.md)
- [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 用小型模型示例讲解从头训练语言模型。README 以 64M 参数模型和“两小时训练”为演示目标，覆盖预训练、微调、LoRA 与偏好优化等步骤；今天上榜使其成为中文入门材料候选，耗时、成本和训练效果是项目自述，不代表一般情况。[README](../raw/2026-11-23/github-trending-readmes/jingyaogong__minimind.md)
- [nginx/nginx](https://github.com/nginx/nginx) 是开源 Web 服务器，也常用于反向代理、负载均衡、网关和缓存。它今天进入榜单，可作为基础设施项目的发现记录；README 本身是简短介绍，完整配置和安全运维仍需查官方资料，上榜不表示当天发布。[README](../raw/2026-11-23/github-trending-readmes/nginx__nginx.md)
- [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) 是用于模型转换、推理优化和部署的工具包，README 列出 CPU、GPU、NPU 等目标设备与多种模型格式。今天上榜使其成为边缘与异构推理工具的发现候选；设备支持和性能要按具体模型、硬件与版本核验。[README](../raw/2026-11-23/github-trending-readmes/openvinotoolkit__openvino.md)

### X/Twitter 推主主题摘要

下表只选本日窗口内进入主题 brief 的帖子；每条保留 `direct-x` 边界。主题分类来自 [`config/topics.yaml`](../config/topics.yaml)，不代表帖子的说法已独立验证。

| 主题 | 本日帖子 | 证据边界 |
|---|---|---|
| 大模型 / 前沿模型 | [Riley Brown：T3Code 的多模型视频流程](https://x.com/rileybrown/status/2124581053314850904) · [Sam Altman：预训练进展透明度](https://x.com/sama/status/2124551594691932405) · [swyx：困惑度与训练节奏评论](https://x.com/swyx/status/2124583459356373052) | 均为 `direct-x`；Sam 与 swyx 指向同一篇官方文章，评论不构成独立核验。 |
| 智能体 / 智能体工作流 | [Riley Brown：T3Code 中组合 Claude 与 Gemini 处理视频的个人流程](https://x.com/rileybrown/status/2124581053314850904) | `direct-x`；个人使用报告，未经独立评测。 |
| AI 编码 / 开发工具 | [Riley Brown：T3Code 与多模型视频编辑工作流](https://x.com/rileybrown/status/2124581053314850904) | `direct-x`；帖子中的产品能力未经独立复现。 |
| AI 治理 / 公共合法性 | 本日 brief 没有单独标记该分类；[Sam Altman](https://x.com/sama/status/2124551594691932405) 与 [swyx](https://x.com/swyx/status/2124583459356373052) 的帖子按 brief 归在大模型主题，但内容涉及共同测量和安全门槛。 | 此处是编辑归组；原始分类和 `direct-x` 等级保持不变。 |
| AI 基础设施 / 开源 | [Guillermo Rauch：对免费及 ZDR 推理服务的数据风险看法](https://x.com/rauchg/status/2124595496849445079) | `direct-x`；风险推断未经独立调查，作者有商业利益。 |
| 独立开发 / 单人创业 | [nikunj：SaaS 客户购买结果中的外包风险观点](https://x.com/nikunj/status/2124569093806428308) | `direct-x`；被转述的原文未在本地归档。 |
| 产品 / 增长 / 市场进入 | [levelsio：AI 回复刷屏与屏蔽名单的个人观察](https://x.com/levelsio/status/2124586276489695710) | `direct-x`；无平台级数据。 |
| AI 系统 / 自动化 | [Riley Brown：让 Claude 调用 Gemini 子代理分析视频，再由 Claude 编写编辑流程](https://x.com/rileybrown/status/2124581053314850904) | `direct-x`；个人体验，未复现，帖子将其归入多模型工作流。 |

### 播客 / 长对话

follow-builders 本轮上游 offered 1 集：No Priors 的《Powering AI-Driven Drug Discovery with President of Isomorphic Labs Max Jaderberg》，GUID `c9a0c39e-de2a-11f1-9237-d39059052d4c`。发布时间为 `2026-11-12T11:00:00Z`，处于本轮窗口外；因此不写当日洞察卡。聚合 transcript 状态 `ok`，47,939 字符，speaker/timestamp 覆盖均为真；canonical 单集链接状态 `ok`。它属于 `secondary-source`，没有音频复核。另有一条针对 “⚡️Anthropic: Know Before You IPO — Tanay Jaipuria, Wing VC” 的上游转写提交错误（HTTP 502，`transcription_submit_failed`）；该错误不表示 offered 单集缺失或本日播客为零。[单集链接](https://www.youtube.com/watch?v=IiKf3BgBezE) · [播客状态文件](../raw/2026-11-23/podcast-items.json) · [feed 快照](../raw/2026-11-23/podcasts/follow-builders/feed-podcasts.json) · [窗外 transcript](../raw/2026-11-23/podcasts/follow-builders/transcripts/powering-ai-driven-drug-discovery-with-president-of-isomorphic-labs-max-jaderber-2ac097442ec4.md)

## 来源证据表

| 来源 | 本轮状态与数量 | 证据与限制 | 本地材料 |
|---|---|---|---|
| 普通 RSS/Atom | 33 源中 32 成功；45/45 匹配或重点正文可读；160 条按规则跳过 | `dwarkesh-patel` 抓取失败；未用其他来源替代。 | [RSS 记录](../raw/2026-11-23/rss-items.json) |
| AIHOT 精选 | 50 条；本日内/窗外/未知 0/50/0；主题命中 0；原文读取 0 | 二手发现源；GUID、站内 URL 与原文链接保存在记录和 feed 快照。当前 feed 的最新 50 条不代表完整 AI 新闻覆盖。 | [RSS 记录](../raw/2026-11-23/rss-items.json) · [feed XML](../raw/2026-11-23/rss-feeds/aihot-selected.xml) |
| GitHub Releases | Atom 7/7；重点正文 5/10 可读 | Claude Code 5/5 `ok`；Codex 5/5 `limited`；本日没有更新时间落在 11 月 23 日的重点 release。 | [发布记录](../raw/2026-11-23/github-items.json) · [正文目录](../raw/2026-11-23/github-release-fulltext/) |
| GitHub Trending | 10 个项目；描述与 README 10/10 可读 | `secondary-source` / discovery signal；没有安装、运行或核实 README 自述数字。 | [Trending 记录](../raw/2026-11-23/github-trending.json) · [README 目录](../raw/2026-11-23/github-trending-readmes/) |
| 官方页面 | 4/5 成功；Anthropic Engineering `limited`，0 张卡片 | OpenAI News 通过 `opencli-read` 获取索引，但没有解析出官方页面文章正文；索引链接不替代文章正文。 | [页面记录](../raw/2026-11-23/official-pages.json) · [Anthropic Engineering 索引](../raw/2026-11-23/official-page-text/anthropic-engineering/anthropic-engineering-anthropic-engineering-9bba7c6d8f.index.html) |
| X 官方链接候选 | 本轮 `official-link-candidates.json` 为空 | 没有将 X 帖子中的猜测提升为官方原文。 | [候选记录](../raw/2026-11-23/official-link-candidates.json) |
| X/Twitter API | `twitterapi.io` 50/50 账号成功；798 条原始、135 条保留 | 保留项为 `direct-x`；不等于账号完整时间线。 | [API 结果](../raw/2026-11-23/twitterapi-io-results.json) · [主题摘要](../raw/2026-11-23/twitter-topic-brief.json) |
| follow-builders 播客 | `partial`；offered/inside/outside/unknown 1/0/1/0；transcript/link ok/limited 各 1/0；上游错误 1 | 聚合转录为 `secondary-source`，本日窗口内没有可读单集。 | [podcast-items.json](../raw/2026-11-23/podcast-items.json) · [feed 快照](../raw/2026-11-23/podcasts/follow-builders/feed-podcasts.json) · [窗外 transcript](../raw/2026-11-23/podcasts/follow-builders/transcripts/powering-ai-driven-drug-discovery-with-president-of-isomorphic-labs-max-jaderber-2ac097442ec4.md) |

## X/Twitter 覆盖说明

`twitterapi.io` 按配置请求 50 个账号，全部成功，返回 798 条原始帖子，经过窗口、关键词和去重筛选后保留 135 条 `direct-x`；主题 brief 为当日阅读清单列出 9 条。接口的 36 小时抓取范围、内容过滤、窗口规则和 `seen.json` 去重都会影响保留数量，不能把未保留帖子解释为账号没有更新，也不承诺完整时间线覆盖。本轮只使用公开只读数据，没有用登录态浏览器、Exa 搜索或 X 写入接口。[API 结果](../raw/2026-11-23/twitterapi-io-results.json) · [主题 brief](../raw/2026-11-23/twitter-topic-brief.json)

## 不确定性与待验证项

- `dwarkesh-patel` RSS 返回空响应，缺少该源本轮覆盖；其它来源的成功不能补足该源内容。[RSS 记录](../raw/2026-11-23/rss-items.json)
- AIHOT 当前精选 feed 的 50 条全部处于 11 月 23 日北京时间窗口外，本轮按规则未读取原文；其最新 50 条是有界发现源，不代表完整覆盖。记录中的站内 URL/GUID 与原文 URL 应分别解释，摘要仍是 `secondary-source`。[feed 快照](../raw/2026-11-23/rss-feeds/aihot-selected.xml) · [条目记录](../raw/2026-11-23/rss-items.json)
- OpenAI《Perplexity and Intelligence》的 RSS 发布时间为 11 月 22 日 00:00 UTC（北京时间 08:00），正文页眉标为 11 月 20 日；文章不计入 11 月 23 日新发布。正文可读，但索引页解析出的官方文章卡片为 0。Sam Altman 帖子是当日 `direct-x` 证据，不替代对日期冲突的解决。[RSS 原文记录](../raw/2026-11-23/rss-items.json) · [本地正文](../raw/2026-11-23/rss-fulltext/openai-blog/openai-blog-perplexity-and-intelligence-de5cd1a6d5.opencli.md) · [官方页面索引记录](../raw/2026-11-23/official-pages.json)
- Codex 最近 release Atom 正文只有版本标签；Claude Code 的最近可读 release 更新时间在 11 月 21 日。不能从版本标签或窗口外的 release notes 推断本日产品变化。[GitHub release 记录](../raw/2026-11-23/github-items.json)
- Anthropic Engineering 抓到索引 HTML，但没有解析出文章卡片，页面状态 `limited`；当天是否有该站新文章仍未知。[索引快照](../raw/2026-11-23/official-page-text/anthropic-engineering/anthropic-engineering-anthropic-engineering-9bba7c6d8f.index.html)
- follow-builders 只 offered 1 集，窗口内 0 集；不能据此判断全部配置节目没有更新。唯一单集的 transcript 虽可读且含 speaker/timestamp，但在窗口外。上游另报告 1 个转写错误，标题为 “⚡️Anthropic: Know Before You IPO — Tanay Jaipuria, Wing VC”。[podcast-items.json](../raw/2026-11-23/podcast-items.json) · [feed 快照](../raw/2026-11-23/podcasts/follow-builders/feed-podcasts.json) · [窗外 transcript](../raw/2026-11-23/podcasts/follow-builders/transcripts/powering-ai-driven-drug-discovery-with-president-of-isomorphic-labs-max-jaderber-2ac097442ec4.md)
- Trending README 与帖子中的使用、覆盖、性能和安全声明均未在本轮运行验证；安全测试项目必须限定在获授权目标上。

## 当天产物

- 原始采集、状态和阅读清单：[manifest](../raw/2026-11-23/manifest.json) · [run summary](../raw/2026-11-23/run-summary.json) · [signals](../raw/2026-11-23/signals.json) · [report-reading-list](../raw/2026-11-23/report-reading-list.json)
- 播客覆盖材料：[podcast-items.json](../raw/2026-11-23/podcast-items.json) · [follow-builders feed snapshot](../raw/2026-11-23/podcasts/follow-builders/feed-podcasts.json) · [outside-window transcript](../raw/2026-11-23/podcasts/follow-builders/transcripts/powering-ai-driven-drug-discovery-with-president-of-isomorphic-labs-max-jaderber-2ac097442ec4.md)
- 候选审计：[candidate audit JSON](../reviews/2026-11-23-candidate-audit.json) · [candidate audit Markdown](../reviews/2026-11-23-candidate-audit.md)
- 趋势报告：[2026-11-23 trend report](../trend/reports/2026-11-23-trend-report.md)
- 派生日报包：[JSON index](2026-11-23-daily-intel.index.json) · [HTML view](2026-11-23-daily-intel.html) · [docs index](index.html)

## 边界与验证

本日报覆盖 2026-11-23 Asia/Shanghai 的日期窗口和各来源自身抓取上限。对于 X、AIHOT 与 follow-builders，正文没有超出各自原始证据等级；所有本地正文和状态链接均指向本轮归档。AIHOT 的 50 条均在窗口外，播客窗口内条目为 0；二者都不能解释为上游无更新。当天 X 的 9 条阅读清单项没有本地全文，按结构化直接帖子记录。候选审计、日报严格校验、bundle、trend Phase 1/2、trend check 与 `dsi.py check` 的实际结果以各自输出和当天趋势报告为准。
