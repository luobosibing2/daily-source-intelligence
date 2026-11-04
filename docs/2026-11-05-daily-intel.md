# 每日情报｜2026-11-05

## 直接答案

今天可确认的高信号有 1 条：Anthropic 称 Claude 协助其生物研究团队找到并解析一种噬菌体 vault-like 颗粒的三维结构。公司报告称，Claude 帮助筛查约 150 亿条蛋白质序列、改进实验构建与纯化流程；研究团队仍需验证结构与实验结果，功能尚未确定，预印本也未发布。

本轮采集在 2026-11-05 北京时间窗口内新增 55 条去重状态记录，阅读清单有 27 项，其中 15 项有可读正文、12 项属于结构化证据或边界。follow-builders 播客只提供 1 集，发布时间在窗口外；没有窗口内 transcript 洞察卡。

## 采集范围

本轮运行统一入口 DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-11-05。采集窗口按北京时间 2026-11-05 计算。

- RSS/Atom：33/33 个源成功；47/47 个命中或优先正文读取成功。
- AIHOT 精选 RSS：读取 feed 最新 50 条；50/50 有发布时间、GUID 和原文链接，2 条在窗口内但未命中配置主题，48 条在窗口外。原文全文均未抓取，状态是 skipped，不是正文失败。
- GitHub Releases：7/7 个 Atom 源成功；10 篇优先正文中 5 篇可读、5 篇 limited。
- GitHub Trending：10 个仓库，描述 10/10，README 10/10 已归档并阅读。
- 官方页面：4 个 ok、1 个 limited、0 个 failed。Anthropic Engineering 未解析出有效文章卡，不能据此推断当天没有文章。
- X/Twitter：twitterapi.io 50/50 个账号成功，保留 211 条帖子。
- follow-builders：状态 partial，feed 实际 offered 1 集；窗口内 0、窗口外 1、未知 0；transcript 1 条 ok、0 条 limited，单集链接 1 条 ok、0 条 limited，另有 1 个上游转录错误。[podcast-items.json](../raw/2026-11-05/podcast-items.json)、[feed snapshot](../raw/2026-11-05/podcasts/follow-builders/feed-podcasts.json)。

## 今日高信号

### Anthropic 研究团队用 Claude 协助解析噬菌体 vault 颗粒

Anthropic 的生物研究文章介绍，团队发现与细菌噬菌体有关的 vault-like 颗粒，并解析了 L05 噬菌体颗粒结构。Anthropic 称 Claude 帮助搜索约 150 亿条蛋白质序列、设计构建体、优化分离流程并处理冷冻电镜数据；团队称纯化时间从约 3 天降至 90 分钟，首个结构模型在 34 小时内完成。研究显示模型可参与实验科学工作流，但这些数字来自 Anthropic 自述，尚无预印本供外部复核；颗粒功能仍未知，团队也记录了培养方案和电镜图像处理方面的实验失误。

[Anthropic 研究文章](https://www.anthropic.com/research/investigating-vault-particles-with-claude)（[本地正文](../raw/2026-11-05/official-link-candidates/anthropicai-2118073665296228863-investigating-vault-particles-with-claude.extracted.md)；Anthropic 官方账号的 [direct-x 帖子](https://x.com/AnthropicAI/status/2118073665296228863)，北京时间 04:11）。

## 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- **Codex：** 北京时间当日记录到 0.167.0-alpha.3.1、0.167.0-alpha.5 和 0.168.0-alpha.2。三条 GitHub release Atom 正文都只有版本标签，状态为 limited；本轮没有足够信息判断功能变化，不能从版本号推断行为。[GitHub 采集记录](../raw/2026-11-05/github-items.json)。
- **Claude Code：** 最新读取到 v2.1.318，正文可读，但更新时间换算为北京时间 11 月 4 日；本轮 5 篇 Claude Code 正文均可读，没有一篇是 11 月 5 日新发布。[GitHub 采集记录](../raw/2026-11-05/github-items.json)。
- Anthropic 的 FlashProve 与 Provable Inference 页面属于 11 月 2 日的背景材料，不是今日发布。文章讨论用密码学证明实际服务的模型与输出之间的关系；FlashProve 仓库注明它是研究原型，未维护、暂不接受贡献。完整正文见 [FlashProve](../raw/2026-11-05/official-link-candidates/anthropicai-2117710942826123294-flashprove.extracted.md) 与 [Provable Inference](../raw/2026-11-05/official-link-candidates/anthropicai-2117710942826123294-provable-inference.extracted.md)。

### RSS/Atom 与日期窗口

本轮候选审计识别出 13 条此前未记录的主题匹配 RSS 项目；正文均可读，但发布时间都早于 11 月 5 日北京窗口，因此没有列为今日信号。两条 OpenAI 页面在 RSS 与页面中都显示 11 月 4 日；OpenCLI 抽取头部的日期与页面日期不一致，但不改变它们早于本次窗口的判断。逐项日期和处置见候选审计 JSON。

### AIHOT 精选 RSS 发现线索

AIHOT 的来源抓取状态为 ok，但它是最多取 50 条的二手发现源，站内标题和摘要不是原文。两条窗口内记录分别是：

- “Moonshot AI 在 HuggingFace 开放 2.8T 参数 Kimi K3.1 Pro 权重”，GUID se9yjzn1asv817vcahsxd5zpw；[AIHOT station item](https://aihot.news/items/se9yjzn1asv817vcahsxd5zpw)，feed 中的原始链接指向 [X 帖子](https://x.com/rohanpaul_ai/status/2118059884055024027)。采集器按配置主题判定为 not_relevant，没有读取原文。
- “美国中期选举中选民在 13 州否决数据中心相关提案”，GUID rt92cw12z1dsqozka4y4wzl2v；[AIHOT station item](https://aihot.news/items/rt92cw12z1dsqozka4y4wzl2v)，feed 中的原始链接指向 [404 Media 原文](https://www.404media.co/american-voters-overwhelmingly-reject-ai-data-centers/)。采集器判定为 not_relevant，没有读取原文。

48 条记录在窗口外。50 条都有 feed 发布时刻、GUID、station URL 和原文链接；50 条全文状态都是 skipped，本轮没有 AIHOT 原文抓取失败。feed 快照：[rss-feeds/aihot-selected.xml](../raw/2026-11-05/rss-feeds/aihot-selected.xml)；完整来源和 GUID/原文对应关系：[rss-items.json](../raw/2026-11-05/rss-items.json)。

### Anthropic 研究链接与 DSH 社区项目

Anthropic 官方账号的另一条较早帖子同时指向 [FlashProve](https://github.com/anthropics/FlashProve) 和 [Provable Inference](https://www.anthropic.com/research/provable-inference)，属于 11 月 2 日背景，不作为今日新发布。

X 帖子 [@cnyzgkc 的 DSH 项目汇总](https://x.com/cnyzgkc/status/2117938659169386640)链接到以下第三方社区仓库。它们来自同一条发现帖，不代表 DSH 官方发布；README 描述是项目方自述，本轮没有运行这些项目。

- [dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter)：记录会话与每日成本、token 使用量、账户余额和编码套餐额度；README 标注需要 DSH 0.2.0 以上，并说明针对 0.2.2-alpha.3 调整。
- [dsh-bili-humanism](https://github.com/InariNGT-Ofiicial/dsh-bili-humanism)：从视频文本与画面生成日志、可编辑记忆；README 表示评论接口未开放，账号写操作开关默认关闭，但未用真实账号验证写操作。项目也说明这不是模型微调，长期人格效果尚未证实。
- [dsh-nekowhale-stickers](https://github.com/Loping151/dsh-nekowhale-stickers)：本地可搜索的表情包知识库与模板，提供 Cordis、MCP 和 CLI 接口。
- [universal-plugin-hub](https://github.com/Ultmebius/universal-plugin-hub)：导入 Claude/Codex 插件市场，并管理 Skills、Commands、Agents、MCP、Hooks 和 LSP。
- [dsh-reasoning-only-guard](https://github.com/apex-mochen/dsh-reasoning-only-guard)：声称阻止仅含推理内容的空回合破坏后续会话回放；它是预防工具，不能修复已经损坏的会话，效果未经独立复现。
- [dsh-context](https://github.com/bowenliang123/dsh-context)：查看跨会话 token、成本、上下文、事件、文件和命令，并显示父子代理关系。
- [dsh-bili-scroll](https://github.com/c1overzz/dsh-bili-scroll)：搜索 B 站视频、读取字幕或抽取画面并生成摘要；自动评论和 @ 是可选项，README 称 npm 包当前版本滞后。
- [dsh-Go](https://github.com/ccch1mneyyy/dsh-Go)：Android 端连接本地 Linux/DSH 运行环境或远程主机；README 标注 Android 8 以上、外部模型请求和默认启用的分析数据，并提示权限及破坏性操作风险。
- [dsh-memory-palace](https://github.com/lovezi0/dsh-memory-palace)：用 Markdown、钩子、快照和记忆工具管理用户或工作区记忆；删除或重组操作设有确认门槛。
- [DSH-Pal](https://github.com/yiheng-zyh/DSH-Pal)：Android 远程控制配套端，需要主机侧 DSH 与远程插件；多种隧道方式仍处于 alpha 验证边界，并非手机本地模型执行。

各项目的本地正文和采集状态见 [official-link-candidates.json](../raw/2026-11-05/official-link-candidates.json)。

### GitHub Trending 每日热门项目

本轮 10 个仓库的 README 均已读取。Trending 描述和 README 用于发现和了解项目，不证明采用情况、质量或性能；以下功能来自 README，自述指标未独立复核。

- [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) 从数据库元数据构建企业语义目录和图层，将自然语言查询落到经过认证的定义、数据血缘与 SQL；README 描述了 Postgres 后端、NVIDIA NIM，以及 MCP、CLI、REST 接口，可用 Docker Compose 或 Helm 部署。它补充既有语义模型，不等同于自动保证正确查询。[本地 README](../raw/2026-11-05/github-trending-readmes/NVIDIA__auto-ontology.md)。
- [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) 是管理 Git worktree 的命令行工具，可用 wt switch/list/merge/remove 管理并行分支，另有钩子、独立端口、CI/PR 预览和构建缓存。它提供工作区管理，不负责运行或验证代理。[本地 README](../raw/2026-11-05/github-trending-readmes/max-sixty__worktrunk.md)。
- [mattpocock/skills](https://github.com/mattpocock/skills) 收录可在 Claude、Codex、Copilot、Gemini 等工具中调整使用的工程提示模板，重点包括先澄清需求、简洁沟通、测试与架构。README 是作者的实践集合，没有衡量这些模板效果的数据。[本地 README](../raw/2026-11-05/github-trending-readmes/mattpocock__skills.md)。
- [floci-io/floci](https://github.com/floci-io/floci) 提供本地 AWS API 模拟器，面向 SDK、CLI 和 Terraform 开发；部分服务由进程内实现，另一些需要 Docker 容器。README 明确说明它不等同于完整 AWS，部分 API 只是 stub/mock；运行真实容器服务还需要 Docker socket。[本地 README](../raw/2026-11-05/github-trending-readmes/floci-io__floci.md)。
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) 用会话生命周期钩子记录工具活动，由本地 Bun worker、SQLite 和 Chroma 支持语义与关键词检索，再通过 MCP 分层取回时间线和观察记录；也提供托管观察器。跨工具数据源选项默认关闭，用户需要核对数据同步、密钥和排除设置。[本地 README](../raw/2026-11-05/github-trending-readmes/thedotmack__claude-mem.md)。
- [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) 将 macOS AX、Windows UIA、Linux AT-SPI 辅助功能树转成可操作引用，代理按“观察—操作—复查”循环工作；提供 CLI、MCP stdio 和 C 库，不含模型。截图、剪贴板和日志可能含私人 UI 内容。[本地 README](../raw/2026-11-05/github-trending-readmes/vercel-labs__agent-desktop.md)。
- [github/spec-kit](https://github.com/github/spec-kit) 通过 specify 命令行和编码代理技能生成规格驱动开发、修复缺陷或评估想法的材料，也支持扩展和预设。README 要求用户审阅生成物，并说明缺陷修复和想法评估不必强制走完整 SDD 流程。[本地 README](../raw/2026-11-05/github-trending-readmes/github__spec-kit.md)。
- [The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent) 提供 PR 描述、审查、改进和问答命令，可通过 CLI 或 PR 评论使用。README 将其称为社区维护的旧版项目；help_docs 因曾有凭据暴露问题而在 v0.36.1 后关闭，部署前应核对当前维护和供应商配置。[本地 README](../raw/2026-11-05/github-trending-readmes/The-PR-Agent__pr-agent.md)。
- [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) 把主题转成脚本，再生成或选择画面、配音、字幕和音乐，输出短视频；支持 WebUI、API、CLI 和批量任务。运行常需外部服务密钥，重型本地转录可能需要 GPU。[本地 README](../raw/2026-11-05/github-trending-readmes/harry0703__MoneyPrinterTurbo.md)。
- [garrytan/gstack](https://github.com/garrytan/gstack) 是一组面向 Claude Code 的开发角色与工具，覆盖思考、规划、构建、审查、测试和发布，也提供持久化知识。README 称其他代理环境仍属实验；部分安全技能只是建议，完整阻断钩子仅在 Claude Code 高配形态工作。外部代码审查会把代码发送给 Codex/Claude，需按 README 的运行方式确认授权。[本地 README](../raw/2026-11-05/github-trending-readmes/garrytan__gstack.md)。

### X/Twitter 推主主题摘要

本节只总结北京时间 11 月 5 日的帖子。同一帖子可命中多个配置主题；retweet 仍是所采集账户发布的 direct-x 记录，不是对原作者主张的独立核验。

- **LLM / 前沿模型：** @EXM7777 转发 @ladyxtel 关于跨 ChatGPT、Claude、Cursor、Codex 共享“Living Brain”记忆的说法；帖子被截断，没有实现、评估或原始产品资料，作为发现线索处理。[帖子](https://x.com/EXM7777/status/2118050958282539139)（direct-x）。
- **AI Agent：** @genspark_ai 链接 Forbes 对 SecondBrain Note 的报道，但帖子本身没有说明记忆能力如何实现或评估；不据此判断产品效果。[帖子](https://x.com/genspark_ai/status/2118043860517671134)（direct-x）。Living Brain 转帖也被自动分到本主题，仍是同一条未经验证的线索。
- **AI Coding / Developer Tools：** @thsottiaux 对 Pierre 收购的短评指向 11 月 4 日公告，不构成新的收购事实或产品细节。[帖子](https://x.com/thsottiaux/status/2118024169762029594)（direct-x）；对应官方消息正文在本轮窗口外。
- **AI Governance / Public Legitimacy：** 一条转帖指称 AI 公司侵犯版权，但没有附可核验材料；本报告不将其当作事实。[帖子](https://x.com/Hesamation/status/2118036710785183900)（direct-x，证据不足）。
- **Product / Growth / GTM 与 AI Systems：** @EXM7777 转发一条关于 AI 新界面的创业想法，未提供产品或实现信息。[帖子](https://x.com/EXM7777/status/2118050920378589616)（direct-x，证据不足）。
- **其他窗口内帖子：** @Hesamation 猜测下一代模型发布时间但未给来源；另一条转发 Anthropic vault 研究，内容重复上方官方文章；关于科幻叙事与 AI 写作的两条转帖没有可复用的工程细节。[模型猜测](https://x.com/Hesamation/status/2118016901188301136)、[重复转述](https://x.com/Hesamation/status/2118084410121592953)、[科幻评论](https://x.com/Hesamation/status/2118048771867119812)、[AI 写作泛谈](https://x.com/kloss_xyz/status/2118036107690696796)（均为 direct-x）。
- **AI Infrastructure / Open Source、Indie Hacking、Forward Deployed Engineering：** 本轮没有其他窗口内高信号直帖。

### 播客 / 长对话

follow-builders 的 podcast-items.json 状态是 partial，实际 offered 1 集：Unsupervised Learning 的《Ep 96: Nebius CTO on Racing the Hyperscalers Before AWS Wakes Up》，GUID 4248d1df-1156-4e68-b67a-5f3cfd063aea，身份键 podcast:unsupervised-learning:4248d1df-1156-4e68-b67a-5f3cfd063aea。发布时间为 2026-11-02 13:54:35 UTC，窗口外；因此没有可用于今日的洞察卡。

- [规范单集页面](https://unsupervised-learning.simplecast.com/episodes/ep-96-nebius-cto-on-racing-the-hyperscalers-before-aws-wakes-up-AZ_eCjjr)；feed alias 指向[节目 YouTube 页面](https://www.youtube.com/@RedpointAI)，不是单集链接。
- [本地 transcript](../raw/2026-11-05/podcasts/follow-builders/transcripts/ep-96-nebius-cto-on-racing-the-hyperscalers-before-aws-wakes-up-c63553190136.md)，62,067 字符，包含 speaker/timestamp；它是 follow-builders 聚合转录，未做音频复核，证据等级为 secondary-source。
- [podcast-items.json](../raw/2026-11-05/podcast-items.json) 与 [feed snapshot](../raw/2026-11-05/podcasts/follow-builders/feed-podcasts.json) 保留完整状态。另一个标题为 “⚡️ The 2026 Software Factory Standard — Zach Lloyd, Warp.dev” 的上游 transcript 请求返回 HTTP 502；该错误不能解释为节目没有更新，也不能把中央 feed 的 1 集等同于全部配置节目覆盖。

## 来源证据表

| 来源 | 本轮覆盖 | 证据与边界 |
| --- | --- | --- |
| RSS/Atom | 33/33 源成功；47/47 个匹配或优先正文读取成功 | [rss-items.json](../raw/2026-11-05/rss-items.json) 与 [run-summary.json](../raw/2026-11-05/run-summary.json)；13 条新候选的正文可读，但发布日期在 11 月 5 日前，审计中逐项标为 outside_window。 |
| AIHOT 精选 RSS | 最新 50 条；日期/GUID/原文链接 50/50；窗口内 2 条，均为 not_relevant；窗口外 48 条；全文 0 次读取 | [feed snapshot](../raw/2026-11-05/rss-feeds/aihot-selected.xml) 与 [条目归档](../raw/2026-11-05/rss-items.json)；二手发现源，站内摘要不作原文。 |
| GitHub Releases | 7/7 源成功；10 篇优先正文 5 ok、5 limited | [github-items.json](../raw/2026-11-05/github-items.json)；Codex 五条 Atom 正文只有版本标签，Claude Code 五条正文可读但无 11 月 5 日新发布。 |
| GitHub Trending | 10 个仓库；描述 10/10；README 10/10 已归档并阅读 | [github-trending.json](../raw/2026-11-05/github-trending.json)；仅作为发现线索，README 功能描述和项目指标没有独立验证。 |
| 官方页面 | 4 ok、1 limited、0 failed | [official-pages.json](../raw/2026-11-05/official-pages.json)；Anthropic Engineering 解析到 0 个有效卡片，状态 limited。 |
| X/Twitter | 50/50 账号读取成功；保留 211 条帖子；候选审计采样 69 条，其中 9 条在窗口内、60 条早于窗口 | [twitterapi-io-results.json](../raw/2026-11-05/twitterapi-io-results.json)、[twitter-topic-brief.json](../raw/2026-11-05/twitter-topic-brief.json)；帖子为 direct-x，不证明帖子中的主张已核实。 |
| follow-builders 播客 | partial；offered/allowed/inside/outside/unknown = 1/1/0/1/0；transcript ok/limited = 1/0；link ok/limited = 1/0；上游错误 1 | [podcast-items.json](../raw/2026-11-05/podcast-items.json)、[feed snapshot](../raw/2026-11-05/podcasts/follow-builders/feed-podcasts.json) 和 [本地 transcript](../raw/2026-11-05/podcasts/follow-builders/transcripts/ep-96-nebius-cto-on-racing-the-hyperscalers-before-aws-wakes-up-c63553190136.md)；只表示中央 feed 实际提供量。 |

## X/Twitter 覆盖说明

twitterapi.io 本轮配置的 50 个账号均返回成功，共保留 211 条公开帖子。采集结果不代表完整时间线，账号清单、接口返回量和约 36 小时查询窗口都会限制覆盖；没有使用登录态浏览器补抓 X。候选审计工具不按日期筛选帖子：69 条高分候选中，9 条按发布时间换算为北京时间 11 月 5 日，另外 60 条来自 11 月 3 日或 11 月 4 日，逐项按 outside_window 处理。

## 不确定性与待验证项

- AIHOT 仅代表 https://aihot.news/feed.xml 当前最新 50 条。Kimi K3.1 Pro 记录在窗口内，但采集器按配置主题判为 not_relevant，所以未读取原文；AIHOT 的标题、摘要及站内链接不能替代原文证据。
- OpenAI 收购与 Daybreak Red 两项 RSS 原文的 feed/页面日期均显示 11 月 4 日，而 OpenCLI 抽取头部存在不同的日期；两项均不属于 11 月 5 日窗口，保留在候选审计的 outside_window 处置中。
- Anthropic vault 文章没有预印本；研究结果、15B 序列搜索和实验耗时来自公司自述，颗粒功能仍未知。
- Codex 三条窗口内预发布记录的 Atom 正文只有版本标签；Anthropic Engineering 页面状态 limited，0 个文章卡不代表 0 篇新文章。
- 本轮唯一 offered 的播客在窗口外，但 transcript 和规范链接可读；另有一个上游 HTTP 502。中央 feed 不承诺覆盖所有节目或完整单集目录。[podcast-items.json](../raw/2026-11-05/podcast-items.json)、[feed snapshot](../raw/2026-11-05/podcasts/follow-builders/feed-podcasts.json)。
- GitHub Trending 反映当天热度，不证明项目可靠、成熟或被实际采用。Agent Desktop 的桌面快照可能含私人数据；claude-mem 和 gstack 需按安装配置检查同步和代码外发；MoneyPrinterTurbo 依赖外部服务时需核对密钥与数据流向；PR Agent README 说明了维护与凭据风险。
- 所有转帖保持其直接采集身份；原作者主张、产品效果、账号增长数据和性能数字没有在本轮独立验证。

## 当天产物

- 原始采集：[manifest.json](../raw/2026-11-05/manifest.json)、[signals.json](../raw/2026-11-05/signals.json)、[report-reading-list.json](../raw/2026-11-05/report-reading-list.json)、[run-summary.json](../raw/2026-11-05/run-summary.json)。
- 播客：[podcast-items.json](../raw/2026-11-05/podcast-items.json)、[feed snapshot](../raw/2026-11-05/podcasts/follow-builders/feed-podcasts.json)、[窗口外 transcript](../raw/2026-11-05/podcasts/follow-builders/transcripts/ep-96-nebius-cto-on-racing-the-hyperscalers-before-aws-wakes-up-c63553190136.md)。
- AIHOT：[feed snapshot](../raw/2026-11-05/rss-feeds/aihot-selected.xml)、[RSS 条目](../raw/2026-11-05/rss-items.json)。
- 候选审计：共 93 条，covered=20、missed=73；73 条 missed 均逐项处置为窗口外（13 条 matched RSS、60 条 X 帖子）。[候选审计 JSON](../reviews/2026-11-05-candidate-audit.json)；[审计表](../reviews/2026-11-05-candidate-audit.md)。趋势报告：[2026-11-05-trend-report.md](../trend/reports/2026-11-05-trend-report.md)；9 个启用专题均已检查并记录 no-new-signal，未重写专题正文。不生成已退役的 translations/2026-11-05。

<!-- dsi-candidate-audit: covered=20 missed=73 -->

## 边界与验证

今天只有 Anthropic vault 研究达到高信号标准。窗口外的 RSS、此前发布的 Anthropic 链接和未验证社交帖只用于背景或审计处置。播客 transcript 虽可读，但发布时间窗口外；partial 状态与上游错误仍是本轮覆盖边界。
