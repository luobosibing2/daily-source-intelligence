## 直接答案

2026-11-21 北京时间运行新增入库 52 条，去重状态总数为 8,457。阅读清单有 20 项：7 项指向可读本地正文，13 项保留结构化帖子、受限正文或时间边界。本日报整理 5 条高信号：OpenAI 官方账号分享反蒸馏防护研究和 MedChemBench 基准、ChatGPT Space 更新、一则 AIHOT 收录的黎曼猜想 Lean 证明主张，以及一条关于 ArcFront 的未核验创业线索。两篇 OpenAI 文章原文日期为 11 月 20 日，11 月 21 日的新信号是官方账号当天分享；黎曼猜想主张与 ArcFront 经营数据都待独立核实。所有来源按北京时间自然日统计。

## 采集范围

- 统一采集命令：`DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-11-21`。本轮于 2026-11-21 05:24（北京时间）完成；后续为记录 Anthropic Engineering 的 OpenCLI fallback 重新运行了状态准备，未再新增 seen 记录。运行计数与证据路径见[run-summary.json](../raw/2026-11-21/run-summary.json)、[manifest.json](../raw/2026-11-21/manifest.json)、[signals.json](../raw/2026-11-21/signals.json)和[report-reading-list.json](../raw/2026-11-21/report-reading-list.json)。
- RSS/Atom：33 个源中 32 个成功；48/48 条命中主题或一手重点的正文读取成功，另有 157 条未触发正文读取。`dwarkesh-patel` 返回 `curl: (52) Empty reply from server`。[采集记录](../raw/2026-11-21/rss-items.json)。
- AIHOT 精选 RSS：读取最新 50 条，其中 4 条落在北京时间 11 月 21 日，46 条在窗口外，0 条时间未知；4 条窗口内记录中 3 条命中主题并读取链接正文，1 条不相关而跳过。50 条均保留 GUID、站内条目链接、发布时间和描述中的原文链接；匹配正文 3/3 可读。[XML 快照](../raw/2026-11-21/rss-feeds/aihot-selected.xml) · [采集记录](../raw/2026-11-21/rss-items.json)。AIHOT 是有边界的二手发现源，不代表完整 AI 新闻覆盖。
- GitHub Releases：7/7 个 Atom 源成功。Codex 与 Claude Code 的一手重点源共尝试读取 10 条正文，6 条可读、4 条受限。北京时间 11 月 21 日仅看到 Codex `0.173.0-alpha.2` 与 `alpha.3` 两条新标签；正文只有版本名，不能据此推断功能变化。[发布记录](../raw/2026-11-21/github-items.json)。
- GitHub Trending：解析 10 个项目，描述和 README 均为 10/10 可读。以下介绍结合榜单描述与本地 README；本轮没有安装或运行项目。上榜只作为发现信号。[Trending 记录](../raw/2026-11-21/github-trending.json)。
- 官方页面：4/5 个源成功。Anthropic Engineering 的 curl HTML 未解析出文章卡片；按 runbook 以 OpenCLI 读取后得到 29 个文章链接，但没有发布时间，因此仍标记 `limited`，不能断言当天没有文章。[页面状态](../raw/2026-11-21/official-pages.json) · [curl 索引快照](../raw/2026-11-21/official-page-text/anthropic-engineering/anthropic-engineering-anthropic-engineering-9bba7c6d8f.index.html) · [OpenCLI 可读快照](../raw/2026-11-21/official-page-text/anthropic-engineering/anthropic-engineering-index.opencli.md)。
- X/Twitter：`twitterapi.io` 配置的 50/50 个账号请求成功，共取得 920 条原始帖子，保留 229 条 `direct-x` 记录。API 返回不代表完整账号时间线。[API 结果](../raw/2026-11-21/twitterapi-io-results.json) · [主题 brief](../raw/2026-11-21/twitter-topic-brief.json)。
- priority X 链接候选：4/4 个候选有可读正文，方法包括 `opencli-read` 与本地提取；其中 3 个进入本轮阅读清单。[候选采集记录](../raw/2026-11-21/official-link-candidates.json)。链接候选的页面日期与 X 帖子时间分别记录，不把页面发布日期未知改成窗口内。
- 播客：follow-builders 状态 `ok`，上游本轮 offered 1 集；inside/outside/unknown 为 0/1/0，transcript ok/limited 为 1/0，canonical link ok/limited 为 1/0，上游错误 0。[podcast-items.json](../raw/2026-11-21/podcast-items.json) · [原始 feed 快照](../raw/2026-11-21/podcasts/follow-builders/feed-podcasts.json)。本轮没有窗口内 transcript；offered 1 集不等于逐节目或完整单集覆盖。

## 今日高信号

1. **OpenAI 官方账号分享其反蒸馏防护研究。** 文章描述请求级模型训练、输入与输出分类器、API 限制，以及针对协同提取活动的调查和处置；OpenAI 报告称，GPT-6.2 Astra 的自适应黑盒测试中，提取先前请求受保护推理的攻击成功率从 GPT-6 Astra 原防护下的 54.0% 降至 0.2%，提取当前请求的成功率从 22.9% 降至 0.9%。这些是公司内部评测与执法统计，不能当作独立审计结果。文章发表于 11 月 20 日；11 月 21 日官方 X 分享为本日 direct-x 信号。[官方文章](https://openai.com/index/combatting-adversarial-distillation/) · [本地正文](../raw/2026-11-21/rss-fulltext/openai-blog/openai-blog-combatting-adversarial-distillation-3ea993db7e.opencli.md) · [官方帖子](https://x.com/OpenAI/status/2123862344422088794)（`direct-x`）。
2. **OpenAI 官方账号分享 MedChemBench。** 基准以 99 道题评估分子结构还原、实验结果解释、候选排序与性质预测，材料来自 117 篇论文和专利、761 个分子结构。OpenAI 报告 GPT-6.2 Astra 在 xhigh 设置下取得 84.5%；但单题只尝试一次、没有工具或反馈，也不能排除模型预先接触过公开材料，因此不能据此推断真实药物发现能力。文章页面写 11 月 20 日，RSS 正文的提取元数据却写 11 月 18 日；官方新闻索引显示 11 月 20 日。11 月 21 日官方 X 分享是本日 direct-x 信号，文章本身不是当日新发布。[官方文章](https://openai.com/index/introducing-medchembench/) · [本地 RSS 正文](../raw/2026-11-21/rss-fulltext/openai-blog/openai-blog-can-ai-help-scientists-identify-promising-drug-candidates-f4784c3040.opencli.md) · [官方新闻索引](../raw/2026-11-21/official-page-text/openai-news-openai-news-openai-cd4de9e9e7.opencli.md) · [官方帖子](https://x.com/OpenAI/status/2123856316187975756)（`direct-x`）。
3. **ChatGPT Space 增加协作页面与幻灯片工作区。** 当天 X 页面称，用户可在 Space 中整理页面、幻灯片、图片和文件，与他人协作，并让页面或幻灯片从连接的工具自动更新。原帖作者为 ChatGPT 官方账号，但本轮发现入口是 AIHOT 精选 feed，故本条证据保持 `secondary-source`，不标为 `direct-x` 或独立官方页面采集。[AIHOT 站内条目](https://aihot.news/items/ekf0so0xitc52thkrxx3mwax1) · [所链接帖子](https://x.com/ChatGPT/status/2123850915061104735) · [本地正文](../raw/2026-11-21/rss-fulltext/aihot-selected/aihot-selected-chatgpt-space-2bce2d8b99.extracted.md)。
4. **Levent Alpöge 宣称与 Claude 合作完成黎曼猜想 Lean 形式化证明。** AIHOT 收录的中文文章称，代码约有 1,737 万行；TechCrunch 报道说数学界仍在检查证明，作者本人也表示希望进一步理解和简化论证。当前归档没有原始论文 PDF、Lean 项目或编译日志，不能写成“证明已成立”；AIHOT、TechCrunch 与 Simon Willison 均属于二手报道或转述。[AIHOT 中文站内条目](https://aihot.news/items/vu6fw8wmrs3xcln4u9gwzf1f4) · [AIHOT 所链接文章](https://mp.weixin.qq.com/s/8Zi3nfwddzFy6cZsK2_KxA) · [TechCrunch 报道](https://techcrunch.com/2026/11/20/ai-claimed-a-solution-to-the-167-year-old-riemann-hypothesis-and-a-human-did-too/) · [Simon Willison 转述](https://simonwillison.net/2026/Nov/20/levent-alpoge/) · [本地 AIHOT 正文](../raw/2026-11-21/rss-fulltext/aihot-selected/aihot-selected-anthropic-levent-alp-ge-claude-1737-lean-a6e23c88dc.opencli.md) · [本地 TechCrunch 正文](../raw/2026-11-21/rss-fulltext/aihot-selected/aihot-selected-anthropic-levent-alp-ge-lean-d6bff5841b.opencli.md)。
5. **一条 direct-x 帖子称 ArcFront 已达到约 10 亿美元年化收入。** 帖子称这家不到一年的公司从专家处获取领域判断，服务芯片设计、工厂运营等真实任务，并称其客户包含五家前沿模型实验室中的四家。这是单一用户帖，未见公司公告、客户证言或独立收入材料；只作为待核验线索，不当作市场事实。[帖子](https://x.com/kloss_xyz/status/2123855459149086979)（`direct-x`）。

## 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- **OpenAI Blog：5/5 正文可读，0/5 是 11 月 21 日发布。** 反蒸馏文章、Hebbia 金融研究案例和 MedChemBench 页面日期为 11 月 20 日；Performance Factory 与 Codex Security Plugin 页面日期为 11 月 19 日。当天的 OpenAI 新信号来自官方账号对反蒸馏和 MedChemBench 的 X 分享，不能将链接文章的旧发布时间改成当日。Hebbia 案例为厂商客户自述；它不在本日窗口内，不作为本日新信号。[RSS 条目](../raw/2026-11-21/rss-items.json) · [OpenAI 正文目录](../raw/2026-11-21/rss-fulltext/openai-blog/)。
- **Codex：**`openai/codex` 的 `0.173.0-alpha.2` 与 `0.173.0-alpha.3` 更新于北京时间 11 月 21 日，Atom 正文均只有版本名，状态 `limited`；`alpha.1`、`0.172.0-alpha.2` 与 `0.171.0` 不属于本日窗口。今天能确认两条 alpha 标签出现，不能确认功能差异。[GitHub 记录](../raw/2026-11-21/github-items.json) · [Codex release 正文目录](../raw/2026-11-21/github-release-fulltext/openai-codex/)。
- **Claude Code：**最新归档 `v2.1.329` 的更新时间折算为北京时间 11 月 20 日 06:14，位于本日窗口外；更早的 `v2.1.328` 至 `v2.1.325` 也不在 11 月 21 日。本轮 5/5 条 release 正文可读，但没有 Claude Code 当日新 release。[GitHub 记录](../raw/2026-11-21/github-items.json) · [Claude Code release 正文目录](../raw/2026-11-21/github-release-fulltext/anthropics-claude-code/)。

### 智能体、工具与工程实践

- Matt Pocock 分享为非开发者制作的 `/vector` skill，强调用清晰步骤委派日常 AI 任务。[帖子](https://x.com/mattpocockuk/status/2123810087361810663)（`direct-x`）。这是个人实践分享，没有本轮可复现的使用评估。
- `kloss_xyz` 转发 `pstack v0.15.46` 更新：帖子称该版缩短 skills，并把 Gemini 4 Neon 加入 panel reviewer。内容是转帖及发布者自述，不能当作独立的模型效果验证。[帖子](https://x.com/kloss_xyz/status/2123833336548487628)（`direct-x`）。
- Riley Brown 预测按需租用 GPU 可能成为 Claude 与 Codex 的新方向并推高算力成本；这是观点，不是市场数据。[帖子](https://x.com/rileybrown/status/2123884789413683638)（`direct-x`）。
- Anthropic 官方账号发布创始团队回顾内容，列出 Dario Amodei、Daniela Amodei、Tom Brown、Jack Clark、Jared Kaplan、Sam McCandlish 与 Chris Olah；该帖是公司叙事材料，没有新增产品或独立治理证据。[帖子](https://x.com/AnthropicAI/status/2123822989154369958)（`direct-x`）。

### GitHub Trending 项目

以下说明依据榜单描述和 10 份本地 README；属于项目方自述及发现信号，不表示采用规模、质量、安全性或生产效果。

- [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) 是面向 Claude Code 的授权漏洞测试技能包。README 称含 83 项技能、15 个命令和漏洞报告模式，按范围检查、侦察、测试、验证和报告组织工作；项目描述与榜单对技能数量分别写 83 和 82。它涉及双重用途安全知识，只能在自有或书面授权范围内使用。[README](../raw/2026-11-21/github-trending-readmes/elementalsouls__Claude-BugHunter.md)。
- [obra/superpowers](https://github.com/obra/superpowers) 把需求澄清、分段设计、用户确认、计划、子代理实施、测试驱动开发、代码审查和分支收尾组织成可供多种编码 Agent 使用的技能流程。README 描述的是项目预期流程，不证明每个宿主都能一致触发。[README](../raw/2026-11-21/github-trending-readmes/obra__superpowers.md)。
- [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) 提供 CLI-Hub 浏览和安装已有命令行工具，并以七阶段生成流程为软件创建带结构化输出的 CLI。README 还描述可连接真实软件后端与制造设备控制示例；高影响命令和设备操作需要额外核验权限与副作用。[README](../raw/2026-11-21/github-trending-readmes/HKUDS__CLI-Anything.md)。
- [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 提供轻量 PyTorch 训练链路，覆盖预训练、SFT、LoRA、蒸馏、强化学习和工具调用。README 中单卡 RTX 3090 的时间和成本是项目自报的小模型实验值，不能代表训练通用高能力模型的成本或效果。[README](../raw/2026-11-21/github-trending-readmes/jingyaogong__minimind.md)。
- [cursor/plugins](https://github.com/cursor/plugins) 是由多个独立目录组成的插件市场，清单可包含技能、规则、MCP 配置及外部服务集成。部分插件会发送消息、改记录、购买或交易；安装前应核对各插件的授权范围和写入权限。[README](../raw/2026-11-21/github-trending-readmes/cursor__plugins.md)。
- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) 提供网页搜索、抓取、遍历和 URL 映射；本地工具可用 MCP 接入 Agent，自托管版另有队列、worker 和数据库。README 提醒本地功能在特定情形下可能回退至云服务，需核对数据路径并按需关闭云端回退。[README](../raw/2026-11-21/github-trending-readmes/firecrawl__firecrawl.md)。
- [nginx/nginx](https://github.com/nginx/nginx) 是 Web 服务器、反向代理、负载均衡器、API 网关和缓存。README 描述 master/worker 进程、模块和文本配置；Windows 版本标明用于开发和测试，不是本日 AI 专项变化。[README](../raw/2026-11-21/github-trending-readmes/nginx__nginx.md)。
- [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) 为 PyTorch、TensorFlow、ONNX 等模型提供转换与推理优化，可面向 CPU、GPU、NPU 和边缘环境部署。README 列出的性能与设备支持需按具体模型和硬件验证；项目提供关闭遥测的方式。[README](../raw/2026-11-21/github-trending-readmes/openvinotoolkit__openvino.md)。
- [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) 是生成自包含 HTML/SVG 图表的 Agent skill，可导入多种图表格式并保留组件关系后重排布局；README 还说明品牌适配和字体选择。Trending 描述列 45 种图，README 列 51 种；数字差异未独立核验。[README](../raw/2026-11-21/github-trending-readmes/cathrynlavery__diagram-design.md)。
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) 并行检索多个社区和平台，按相关性、互动与新鲜度评分，再合并事件生成带引用的摘要。可用来源取决于凭据与已启用工具，部分路径会读取登录态账户数据或产生费用；互动分数不能单独证明内容准确。[README](../raw/2026-11-21/github-trending-readmes/mvanhorn__last30days-skill.md)。

### X/Twitter 推主主题摘要

下表只列 11 月 21 日北京时间窗口内的代表帖子。帖子会因多主题匹配而重复进入 topic brief；此处按链接去重。内容来自 `twitterapi.io`，均为 `direct-x`；转帖和个人推断按其原有性质说明。

| 主题 | 窗口内代表帖子 |
| --- | --- |
| LLM / Frontier Models | OpenAI 分享 MedChemBench 与反蒸馏防护文章，见[MedChemBench 帖](https://x.com/OpenAI/status/2123856316187975756)和[反蒸馏帖](https://x.com/OpenAI/status/2123862344422088794)；两篇被链接的文章日期为 11 月 20 日。 |
| AI Agent / Agentic Workflow | Matt Pocock 分享为非开发者制作 `/vector` skill 的委派方式，[帖子](https://x.com/mattpocockuk/status/2123810087361810663)；没有当日跨场景使用评估。 |
| AI Coding / Developer Tools | `/vector` 为非开发者委派任务提供步骤化 skill 入口，[帖子](https://x.com/mattpocockuk/status/2123810087361810663)；`pstack v0.15.46` 的技能精简是转帖信息，[帖子](https://x.com/kloss_xyz/status/2123833336548487628)。 |
| AI Governance / Public Legitimacy | OpenAI 官方账号分享反蒸馏防护研究，[帖子](https://x.com/OpenAI/status/2123862344422088794)；这是厂商披露，效果数据未独立审计。 |
| AI Infrastructure / Open Source | Riley Brown 预测智能体按需租用算力可能影响 GPU 价格，[帖子](https://x.com/rileybrown/status/2123884789413683638)；属于个人观点，不是价格或需求数据。 |
| Indie Hacking / Solo Founder | Kloss 称 ArcFront 年化收入约 10 亿美元、客户包括五家前沿模型实验室中的四家；公司和客户数据未核实。[帖子](https://x.com/kloss_xyz/status/2123855459149086979)（`direct-x`）。 |
| Product / Growth / GTM | Matt Pocock 的 `/vector` 面向非开发者委派日常任务；Marc Lou 当天转发赛事资格处置，[帖子](https://x.com/mattpocockuk/status/2123810087361810663) · [转发帖](https://x.com/marclou/status/2123835858289631609)。 |
| AI Systems / Automation | `pstack v0.15.46` 转帖提到技能精简与 reviewer 组合变化，[帖子](https://x.com/kloss_xyz/status/2123833336548487628)；ArcFront 的帖子描述以专家知识支持真实工业任务，但收入与客户数字未独立核实。[帖子](https://x.com/kloss_xyz/status/2123855459149086979)。 |

### 播客 / 长对话

follow-builders 本轮 `status=ok`，中央 feed offered 1 集；inside/outside/unknown 为 0/1/0，transcript ok/limited 为 1/0，canonical link ok/limited 为 1/0，上游错误 0。单集为 No Priors 的《Superintelligence Needs the Physical World with CEO and Co-Founder of Arda Bob McGrew》，GUID 为 `8fd14988-e40e-11f1-99ee-ebfb28833f04`，发布时间 `2026-11-19T11:44:00Z`，在 11 月 21 日窗口外。官方单集链接状态 `ok`，transcript 有 speaker/timestamp 覆盖，但本轮没有窗口内单集，因此不写洞察卡，也未复核音频。聚合 transcript 的证据等级为 `secondary-source`。[canonical 单集链接](https://www.youtube.com/watch?v=_wLzJINt9iQ) · [podcast-items.json](../raw/2026-11-21/podcast-items.json) · [follow-builders 原始 feed](../raw/2026-11-21/podcasts/follow-builders/feed-podcasts.json) · [窗外 transcript](../raw/2026-11-21/podcasts/follow-builders/transcripts/superintelligence-needs-the-physical-world-with-ceo-and-co-founder-of-arda-bob-m-c269dff631d6.md)。这是中央 feed 实际提供的 1 集，不能解释为六个节目均无更新。

## 来源证据表

| 来源 | 本轮状态与覆盖 | 证据等级与本地入口 |
| --- | --- | --- |
| RSS/Atom | 32/33 源成功；命中或一手重点正文 48/48 可读；157 条跳过正文；`dwarkesh-patel` 返回空响应 | [rss-items.json](../raw/2026-11-21/rss-items.json) |
| AIHOT 精选 RSS | 最新 50 条；4 条窗内、46 条窗外、0 条时间未知；3 条匹配、1 条不相关；匹配原文 3/3 可读，50/50 条均有 GUID、站内 URL、发布时间和描述中的原文链接 | `secondary-source`；[XML 快照](../raw/2026-11-21/rss-feeds/aihot-selected.xml) · [采集记录](../raw/2026-11-21/rss-items.json) · [3 条已读正文](../raw/2026-11-21/rss-fulltext/aihot-selected/) |
| GitHub Releases | 7/7 Atom 源成功；一手重点正文 6 ok、4 limited；11 月 21 日 Codex 仅有两条 limited alpha 标签 | `official-source`；[github-items.json](../raw/2026-11-21/github-items.json) |
| GitHub Trending | 10 项目；描述和 README 均 10/10 可读 | 项目方 README 自述，仅为发现信号；[Trending 记录](../raw/2026-11-21/github-trending.json) |
| 官方页面 | 4 个成功、1 个 limited；Anthropic Engineering 的 OpenCLI fallback 可读 29 条链接但缺发布时间 | [official-pages.json](../raw/2026-11-21/official-pages.json) · [OpenCLI 快照](../raw/2026-11-21/official-page-text/anthropic-engineering/anthropic-engineering-index.opencli.md) |
| OpenAI Blog 一手 RSS | 5 篇正文 5/5 可读，全部早于 11 月 21 日；当日相关信号来自官方 X 分享 | `official-source`；[RSS 状态](../raw/2026-11-21/rss-items.json) · [正文目录](../raw/2026-11-21/rss-fulltext/openai-blog/) |
| X/Twitter | 50/50 账号成功；920 条原始、229 条保留；API 覆盖不是完整时间线 | `direct-x`；[API 结果](../raw/2026-11-21/twitterapi-io-results.json) · [主题 brief](../raw/2026-11-21/twitter-topic-brief.json) |
| follow-builders 播客 | `status=ok`；offered/inside/outside/unknown 为 1/0/1/0；transcript 与链接各 1/0 ok/limited；上游错误 0 | 聚合 transcript 为 `secondary-source`；[podcast-items.json](../raw/2026-11-21/podcast-items.json) · [feed 快照](../raw/2026-11-21/podcasts/follow-builders/feed-podcasts.json) · [窗外 transcript](../raw/2026-11-21/podcasts/follow-builders/transcripts/superintelligence-needs-the-physical-world-with-ceo-and-co-founder-of-arda-bob-m-c269dff631d6.md) |

## X/Twitter 覆盖说明

`twitterapi.io` 本轮对配置中的 50 个账号全部请求成功，取得 920 条原始记录，按采集规则保留 229 条 `direct-x`。按多个主题标签归类可能重复；表格按帖子链接去重。OpenAI 对反蒸馏和 MedChemBench 的两条官方帖属于 11 月 21 日 direct-x 证据，链接文章分别发表于 11 月 20 日；AIHOT 转述的 ChatGPT Space 帖子仍标为 `secondary-source`。转帖、个人观点和项目方说法不能替代独立测试。没有使用登录态浏览器、Exa、X 写操作或账号凭据。

## 不确定性与待验证项

- `dwarkesh-patel` RSS 返回 `curl: (52) Empty reply from server`，本轮缺少该来源 feed 覆盖。
- Anthropic Engineering curl HTML 没有解析出有效文章卡片；OpenCLI fallback 返回 29 个链接但无发布日期，无法确定哪些文章落入本日窗口，状态维持 `limited`。
- AIHOT 只覆盖其站点最新 50 条。50 条均保留 GUID、站内 URL、北京时间窗口判断和描述中的外部原文链接；4 条窗内，3 条主题匹配并读取原文，1 条不相关跳过；46 条窗外。AIHOT 标题与摘要始终是二手发现证据，匹配正文可读也不把 AIHOT 站内内容升级为官方或 direct-x。该来源不代表完整新闻覆盖。
- 本轮 `signals.json` 有 20 条信号：17 条窗口内，3 条发布时间未知。官方链接候选的页面发布时间未知时保留 unknown；LinkedIn/X 分享时间不能替代原文发布时间。MedChemBench 正文提取的时间与页面和索引日期不一致，且模型得分属于 OpenAI 自报基准。
- 黎曼猜想主张的本地材料为 AIHOT、TechCrunch 与 Simon Willison 的二手报道或转述；原始 PDF、Lean 代码仓、完整编译记录和独立数学审查结论没有归档。文章内关于广义黎曼猜想的另一项人类证明是不同主张，未与 AI 合作证明混为一谈。
- Codex `0.173.0-alpha.2` 与 `alpha.3` 的 release Atom 正文只有版本名；不能据此推断功能、修复或兼容性。Claude Code 当前最新归档版本的更新时间在 11 月 20 日，不是当日新 release。
- DuskBot、CLI-Anything、Claude-BugHunter、last30days-skill、Cursor plugins 和其他 Trending 项目的能力及安全说明来自 README 自述。本轮未运行代码；设备控制、外部服务、登录态数据、写操作、凭据和交易等权限需在采用前核对。
- 播客上游只提供 1 集，且它位于窗口外。transcript 和 canonical link 可读，但没有本日窗口内 transcript；speaker/timestamp 覆盖存在不改变窗口状态。中央 feed 结果不能解释为所有节目无更新。[podcast-items.json](../raw/2026-11-21/podcast-items.json) · [feed 快照](../raw/2026-11-21/podcasts/follow-builders/feed-podcasts.json) · [窗外 transcript](../raw/2026-11-21/podcasts/follow-builders/transcripts/superintelligence-needs-the-physical-world-with-ceo-and-co-founder-of-arda-bob-m-c269dff631d6.md)。
- 候选审计共 104 项：14 项正文覆盖、90 项未覆盖。90 项未覆盖均已处置：66 项 `outside_window`、13 项 `not_selected`、6 项 `read_not_relevant`、3 项 `duplicate`、2 项 `insufficient_evidence`。[审计 JSON](../reviews/2026-11-21-candidate-audit.json) · [审计 Markdown](../reviews/2026-11-21-candidate-audit.md)。

## 当天产物

- 日报：[2026-11-21-daily-intel.md](2026-11-21-daily-intel.md)
- 流程和阅读证据：[run-summary.json](../raw/2026-11-21/run-summary.json) · [manifest.json](../raw/2026-11-21/manifest.json) · [signals.json](../raw/2026-11-21/signals.json) · [report-reading-list.json](../raw/2026-11-21/report-reading-list.json)
- 候选审计：[JSON](../reviews/2026-11-21-candidate-audit.json) · [Markdown](../reviews/2026-11-21-candidate-audit.md)
- AIHOT：[XML feed 快照](../raw/2026-11-21/rss-feeds/aihot-selected.xml) · [采集记录](../raw/2026-11-21/rss-items.json) · [已读原文目录](../raw/2026-11-21/rss-fulltext/aihot-selected/)
- 播客：[podcast-items.json](../raw/2026-11-21/podcast-items.json) · [feed 快照](../raw/2026-11-21/podcasts/follow-builders/feed-podcasts.json) · [窗外 transcript](../raw/2026-11-21/podcasts/follow-builders/transcripts/superintelligence-needs-the-physical-world-with-ceo-and-co-founder-of-arda-bob-m-c269dff631d6.md)
- 派生展示：[日报索引 JSON](2026-11-21-daily-intel.index.json) · [日报 HTML](2026-11-21-daily-intel.html) · [总索引页](index.html)
- 趋势分析：[trend report](../trend/reports/2026-11-21-trend-report.md)

## 边界与验证

本日报依据 2026-11-21 北京时间自然日窗口的统一采集与本地正文归档整理。官方 X 帖子按 `direct-x`，AIHOT 和 follow-builders 按 `secondary-source`，Trending 项目按 README 自述处理。发布时间未知、limited 页面、未复核的数学主张和厂商自报评测均保留各自边界。候选审计、严格校验、日期 bundle、趋势 Phase 1/2、趋势检查与 `dsi.py check` 的最终状态以本轮闭环命令结果为准。

<!-- dsi-candidate-audit: covered=14 missed=90 -->
