## 直接答案

2026-11-15 北京时间日窗内最值得关注的三类线索是：Riley Brown 对 Fable 5.2 驱动 Blender 制作短片的个人演示、Simon Willison 对 Claude 自动模式权限行为的使用观察，以及 AIHOT 转引 TechCrunch 关于亚洲政府回应 Nvidia 算力供给变化的报道。前两项是 `direct-x`，属于个人帖子；AIHOT 线索及其 TechCrunch 原文为 `secondary-source`。今天没有发布时间落在 11 月 15 日的 OpenAI 或 Claude Code 一手发布。

GitHub Trending 收录的 10 个项目提供了可进一步核验的开发工具线索，其中 Google Chrome 的 Modern Web Guidance README 报告了带指南与不带指南的智能体编码评测结果。该结果来自项目自身记录，不能视为独立复现或当天发布。

## 采集范围

- 目标窗口：2026-11-15，北京时间。采集使用统一入口 `DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-11-15`；最终成功运行使用系统/TUN 网络路径。状态准备后 `seen_added=44`，`seen_total=8105`。阅读清单有 16 项：7 项有本地可读正文，9 项只有结构化 `direct-x` 证据或明确覆盖边界。
- RSS/Atom：33 个源中 32 个成功；47 个命中正文读取 47/47 成功。唯一失败源为 `dwarkesh-patel`，错误是 `curl: (52) Empty reply from server`。
- AIHOT 精选摘要 RSS：读取当轮最新 50 条；50 条均保留了 feed 发布时间、GUID、聚合站页面和原文链接。48 条在日窗外；1 条在窗内但未命中主题，原文读取按规则跳过；1 条命中 `infra`，其 TechCrunch 原文通过 `opencli-read` 成功归档。AIHOT 标题与摘要仍标记为 `secondary-source`，最新 50 条只是有界发现范围。
- GitHub Releases：7/7 个 Atom 源成功；10 条一手重点发布项均尝试读取正文，其中 5 条 `ok`、5 条 `limited`。GitHub Trending：10 个项目，10/10 有页面描述和 README 归档。
- 官方页面：4/5 成功；`anthropic-engineering` 的索引 HTML 已抓取，但有效文章卡片为 0，因此状态为 `limited`，不能据此断言当天没有文章。
- `twitterapi.io`：50/50 账号请求成功；保留 169 条 `direct-x` 推文。覆盖受服务返回条数与本轮账号范围限制，不代表完整时间线。
- follow-builders 播客 feed：`podcast-items.json` 状态为 `ok`，上游 offered 1 集，inside/outside/unknown 为 0/1/0；transcript ok/limited 为 1/0，单集链接 ok/limited 为 0/1，上游错误 0。该 offered 数只表示中央 feed 本轮给出的单集数。

## 今日高信号

1. **Fable 5.2 的长链路制作演示**：Riley Brown 声称 Claude 用 Python 在 Blender 中生成短片所需角色、场景、镜头和动画，随后并行启动多个副本并租用 RunPod GPU 渲染。帖子报告约 4.5 小时、3,220 帧和约 20 美元成本；这些数字是作者自述，未独立复现。证据：[`direct-x`](https://x.com/rileybrown/status/2121642720045261185)。
2. **自动模式的权限反馈**：Simon Willison 记录 Claude 普通聊天中的自动模式有时会拒绝操作，并称明确说明本次会话授权后似乎解除了一次阻挡。这是单个用户的行为观察，不是官方规则说明。证据：[`direct-x`](https://x.com/simonw/status/2121695097674981849)。
3. **亚洲 GPU 供给与政策回应**：AIHOT 当日摘要命中基础设施主题，并将原文明确链接到 TechCrunch。原文概述了中国、韩国、台湾和日本政府对相关 Nvidia 供给、项目及调查的回应；其中韩国 260,000 张 GPU 供给计划等信息均按 TechCrunch 报道转述，未在本轮逐一打开其所引政府材料。证据：[`secondary-source` 原文](https://techcrunch.com/2026/11/14/asian-governments-react-to-nvidia-ceo-jensen-huangs-exit/)及[本地 OpenCLI 正文](../raw/2026-11-15/rss-fulltext/aihot-selected/aihot-selected-nvidia-075bbfb634.opencli.md)。
4. **基于评测维护的网页开发指南**：今日热门项目 Modern Web Guidance 提供可检索、可取回的现代网页 API 指南，并在 README 中报告 Codex 在 215 项任务上的通过率由 54% 升至 82%。该数字来自项目自己的评测仪表板记录，属于 `secondary-source`，并非独立验证或 11 月 15 日发布。证据：[仓库 README 归档](../raw/2026-11-15/github-trending-readmes/GoogleChrome__modern-web-guidance-src.md)。
5. **数学研究中的文献辅助**：Hesamation 在 X 上称 Claude 协助研究者整理 Gödel 笔记，提出 663 个潜在定理，其中 400 个通过形式化验证。帖子没有附原始研究链接；本条只记录该用户报告，不把数字当作已核实研究结果。证据：[`direct-x`](https://x.com/Hesamation/status/2121700858647978340)。
6. **智能体软件工厂的运维负担**：Matt Pocock 转发 Steve Yegge 的个人复盘，称智能体过快产出曾压垮功能审阅、邮件处理和合并队列，并指出软件工厂需要持续维护和人的管理投入。该帖子来自个人项目经验，不能推广为所有团队的普遍结果。证据：[`direct-x` 转发帖](https://x.com/mattpocockuk/status/2121706650780442735)。

## 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

截至 11 月 15 日北京时间日窗，没有新的 OpenAI 博客或 OpenAI Codex / Claude Code 发布项。OpenAI 博客 feed 返回 5 条，正文均为 `ok`，最新条目 `Introducing ChatGPT Wallet` 的 feed 时间为 11 月 13 日；Codex 与 Claude Code 各返回 5 条发布项，最新 Codex `0.171.0-alpha.5` 的更新时间为 11 月 14 日 09:25，北京时间，最新 Claude Code `v2.1.325` 为 11 月 14 日 04:40，北京时间，均在本日日窗外。10 条发布正文中，5 条可读、5 条 `limited`；受限项是 Codex `0.171.0-alpha.2` 至 `alpha.5` 和 Claude Code `v2.1.322`。一手重点源仍保留在本节，未因主题关键词过滤。

### AI 基础设施与供给链

AIHOT 站内条目标题为“黄仁勋离开 Nvidia 后，亚洲各国政府如何回应”，GUID 为 `ni18shok3lh70l1e49nazmgdc`，feed 发布时间为 `Sat, 14 Nov 2026 16:34:15 GMT`，换算后落在 11 月 15 日北京时间。AIHOT 聚合页为 [https://aihot.news/items/ni18shok3lh70l1e49nazmgdc](https://aihot.news/items/ni18shok3lh70l1e49nazmgdc)，原文为 [TechCrunch](https://techcrunch.com/2026/11/14/asian-governments-react-to-nvidia-ceo-jensen-huangs-exit/)。本次读取的原文提到中国外交部对出口限制的表态、韩国政府称 Nvidia 重申 GPU 供给计划、台湾继续推进总部项目以及日本将密切关注等内容；这些是 TechCrunch 的报道内容，AIHOT 仅为发现入口。

同一 50 条快照中，另一条窗内条目“Anthropic CEO Amodei 在 IPO 前承认明年存在巨大不确定性，算力是公司最深的商业两难”未命中配置关键词，`fulltext_status=skipped`，按 `read_not_relevant` 处理，没有把 AIHOT 摘要当作原文。

### GitHub Trending 每日热门项目

本轮 Trending 页面解析 10 个仓库，10/10 有页面描述，10/10 README 通过 `curl` 归档。以下介绍将 Trending 描述与 README 合并；当天上榜仅是发现线索，不代表当天发布、质量背书或长期采用。

- [backnotprop/plannotator](https://github.com/backnotprop/plannotator)：本地浏览器审阅界面通过插件、hooks 和 MCP 接入多个编码智能体，让人批注计划、规格、HTML 成品、代码差异和 PR，再把反馈送回对应会话；Inbox 可让智能体继续工作并等待人工回复。README 说明内容默认本地保存，但 Ask AI 会把选中内容发给配置的模型，分享链接也可能让持有完整链接的人读取内容。证据：[README 归档](../raw/2026-11-15/github-trending-readmes/backnotprop__plannotator.md)，`secondary-source`。
- [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)：项目维护网页平台技能，提供 `search`、`retrieve` 和旧式代码扫描，把精选 API 用法、兼容性、无障碍注意点与回退方式加入智能体上下文；README 称本地检索使用离线语义匹配和 BM25，也提供用真实网页应用与 Playwright 检查器构成的评测流程。README 报告的提升来自项目自身评测；工具另会收集匿名安装、调用方、指南 ID 和搜索查询，可用 `DISABLE_TELEMETRY=1` 退出。证据：[README 归档](../raw/2026-11-15/github-trending-readmes/GoogleChrome__modern-web-guidance-src.md)，`secondary-source`。
- [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)：这是面向个人投资者的 Claude Skills 工作流集合，使用 workflow manifest 串联市场状态、风险评估、候选筛选、仓位计算、交易日志和复盘；README 明确保留人工决策，不下单，也不提供信号服务。它是个人项目的自述材料，不是金融建议或收益证据。证据：[README 归档](../raw/2026-11-15/github-trending-readmes/tradermonty__claude-trading-skills.md)，`secondary-source`。
- [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)：MCP 服务和 CLI 通过 Puppeteer 控制、检查 Chrome，可记录性能轨迹、读取网络请求与控制台、截屏并等待交互结果，适用于浏览器测试和调试。README 警告 MCP 客户端能访问和修改浏览器数据，工具使用统计默认开启。证据：[README 归档](../raw/2026-11-15/github-trending-readmes/ChromeDevTools__chrome-devtools-mcp.md)，`secondary-source`。
- [alibaba/open-code-review](https://github.com/alibaba/open-code-review)：代码审查 CLI 先确定文件范围、组合相关文件并套用规则，再让工具型智能体读取完整文件、搜索代码并输出行级意见；README 还描述了独立的意见定位和复核模块，以及全文件扫描。其大规模内部使用和评测结果是仓库自述，README 也说明精确率和召回率之间有取舍，不能当成独立验证。证据：[README 归档](../raw/2026-11-15/github-trending-readmes/alibaba__open-code-review.md)，`secondary-source`。
- [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)：开源编码智能体覆盖终端、桌面、网页、编辑器和聊天接口，可切换多种模型服务，并内置记忆、技能、子智能体与 MCP；团队、竞技场和动态工作流标为实验或可选能力。README 还说明其 daemon 默认只监听本机回环地址但没有 bearer token，能访问它的本机进程可使用代码执行 API。证据：[README 归档](../raw/2026-11-15/github-trending-readmes/QwenLM__qwen-code.md)，`secondary-source`。
- [dream-num/univer](https://github.com/dream-num/univer)：嵌入式表格与文档 SDK 让应用和智能体操作同一份工作簿，Facade API、命令和类型化事件连接编辑器、公式计算、Headless 任务及应用逻辑；应用方负责持久化。此仓库只含 Apache-2.0 Web SDK 核心，协作服务、文件格式转换和部分 AI SDK 能力另行分发或收费。证据：[README 归档](../raw/2026-11-15/github-trending-readmes/dream-num__univer.md)，`secondary-source`。
- [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui)：AG-UI 将智能体执行事件连接到面向用户的应用，README 描述约 16 种标准事件、SSE/WebSocket/webhook 等传输，以及让前端状态与实时上下文同步的中间层和 HTTP 参考实现；项目列出多种框架集成。集成状态来自项目 README，仍需按具体实现核对。证据：[README 归档](../raw/2026-11-15/github-trending-readmes/ag-ui-protocol__ag-ui.md)，`secondary-source`。
- [ashhart/TensorFold](https://github.com/ashhart/TensorFold)：本地推理引擎用 Zig 直接在 Apple Silicon Metal 或 Nvidia CUDA 上加载模型，不需 Python/MLX；README 还描述企业版 Starlight 的身份接入、模型策略和节点管理。其 Living Weights 会尝试把新事实写进模型权重，项目明确标为实验功能，并披露相关事实互扰、几十条后回忆下降和解码变慢等限制。证据：[README 归档](../raw/2026-11-15/github-trending-readmes/ashhart__TensorFold.md)，`secondary-source`。
- [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)：该工具组合简短输出、日志/JSON 压缩、模型路由和可复用脚本，以减少智能体读取与生成的 token；README 自报多项节省比例，同时说明一组会话测试来自旧版引擎、HTML 压缩曾更差，Auto 评测尚未跑完且误差范围较大。CLI 默认会发送使用统计；选择云端 Auto 后，用户请求及智能体附带的上下文可能发往 Caveman Cloud。证据：[README 归档](../raw/2026-11-15/github-trending-readmes/JuliusBrussee__caveman.md)，`secondary-source`。

### X/Twitter 推主主题摘要

下表只列北京时间 11 月 15 日窗口内的主题项。每条均为 `direct-x`；同一帖子会在多个主题重复出现，因为主题 brief 会多主题归类。

| 主题 | 当日高分帖子 |
| --- | --- |
| 前沿模型 | Riley Brown 称其用 Fable 5.2 和 Blender 生成 2 分钟短片；[原帖](https://x.com/rileybrown/status/2121642720045261185)（`direct-x`）。 |
| 智能体与工作流 | Riley Brown 的短片制作案例提到代码生成、并行副本和云端渲染；[原帖](https://x.com/rileybrown/status/2121642720045261185)（`direct-x`）。另有 Kloss 转发的观点，认为只要求快速小修可能固化临时补丁；[转发帖](https://x.com/kloss_xyz/status/2121652754674557332)（`direct-x`）。 |
| 编程智能体与开发工具 | Riley Brown 的 Fable 5.2 制作案例；[原帖](https://x.com/rileybrown/status/2121642720045261185)（`direct-x`）。Levels.io 讨论个人项目可用性；[原帖](https://x.com/levelsio/status/2121658404850872676)（`direct-x`）。Peter Yang 分享 `/doctor prompt-audit` 检查 Claude Code 配置、技能和命令，以及按技能名深入检查的提示；[原帖](https://x.com/petergyang/status/2121649295950762363)（`direct-x`）。 |
| 治理与公共信任 | Simon Willison 对自动模式拒绝及会话授权提示的个人观察；[原帖](https://x.com/simonw/status/2121695097674981849)（`direct-x`）。这条分类实际涉及产品权限行为，不足以说明公共治理变化。 |
| 基础设施与开源 | 本轮窗口内没有符合主题的推主帖子。 |
| 独立开发与个人创业 | Levels.io 以大型服务商故障为例讨论个人项目的可用性；[原帖](https://x.com/levelsio/status/2121658404850872676)（`direct-x`）。Marc Lou 转发个人生产环境迭代做法，包含仅自己可见的功能、日志和数据库检查；[转发帖](https://x.com/marclou/status/2121707439007662371)（`direct-x`）。 |
| 产品增长与市场进入 | Riley Brown 的短片制作案例；[原帖](https://x.com/rileybrown/status/2121642720045261185)（`direct-x`）。Levels.io 的可用性观点；[原帖](https://x.com/levelsio/status/2121658404850872676)（`direct-x`）。Marc Lou 的生产环境迭代自述；[转发帖](https://x.com/marclou/status/2121707439007662371)（`direct-x`）。 |
| 智能体系统与自动化 | Kloss 转发“quick fix”观点；[转发帖](https://x.com/kloss_xyz/status/2121652754674557332)（`direct-x`）。Kloss 另建议请求根因修复与验证；[原帖](https://x.com/kloss_xyz/status/2121671581013553475)（`direct-x`）。Matt Turck 发布一个 12 步自动发邮件工作流的短视频标题；[原帖](https://x.com/mattturck/status/2121714325295386984)（`direct-x`），本次只按帖文文字记录，未读取视频内容。 |

此外，Levels.io 分享 Claude 用 OBS 圆形遮罩处理摄像头画面的做法；[原帖](https://x.com/levelsio/status/2121686411900551270)（`direct-x`）。

### 播客 / 长对话

follow-builders 本轮 offered 1 集：Training Data 的《A Model For Everyone: How Ronak From Trajectory Is Building Products For Continual Learning》，GUID `eed8f8c6-d88e-11f1-8b73-637e085f73d5`，发布时间为 2026-11-05T10:00:00Z，落在 11 月 15 日日窗外。因此本节报告实际窗口边界，不把它写成当天洞察。聚合 transcript 状态 `ok`，35,530 字符且包含 speaker/timestamp 覆盖；canonical episode URL 为空，节目 RSS 未找到 GUID 精确匹配。feed 提供的 YouTube playlist 是别名，不是单集链接。

产物：[podcast-items.json](../raw/2026-11-15/podcast-items.json)、[feed-podcasts.json](../raw/2026-11-15/podcasts/follow-builders/feed-podcasts.json)、[本地 transcript](../raw/2026-11-15/podcasts/follow-builders/transcripts/a-model-for-everyone-how-ronak-from-trajectory-is-building-products-for-continua-9c6b2d4e1195.md)。

## 来源证据表

| 来源 | 本轮状态与覆盖 | 证据等级与本地入口 |
| --- | --- | --- |
| RSS/Atom | 32/33 成功；47/47 命中正文可读；`dwarkesh-patel` 失败 | 按各条目保留来源等级；[rss-items.json](../raw/2026-11-15/rss-items.json) |
| AIHOT 精选 RSS | 最新 50 条；48 条窗外、1 条窗内未匹配、1 条窗内匹配并读取原文；本轮元数据字段完整 | 始终为 `secondary-source`；[XML 快照](../raw/2026-11-15/rss-feeds/aihot-selected.xml)、[匹配原文](../raw/2026-11-15/rss-fulltext/aihot-selected/aihot-selected-nvidia-075bbfb634.opencli.md) |
| GitHub Releases | 7/7 Atom 源；10 条一手正文 5 `ok`、5 `limited` | 按来源条目标记；[github-items.json](../raw/2026-11-15/github-items.json) |
| GitHub Trending | 10 个项目、10/10 页面描述、10/10 README 归档；仅发现线索 | `secondary-source`；[github-trending.json](../raw/2026-11-15/github-trending.json) |
| 官方页面 | 4 成功、1 `limited`；Anthropic Engineering 索引解析 0 卡片 | [official-pages.json](../raw/2026-11-15/official-pages.json)；OpenAI News 归档方法为 `opencli-read` |
| X/Twitter | 50/50 账号成功；920 原始推文、169 条保留 | 每条 `direct-x`；[twitterapi-io-results.json](../raw/2026-11-15/twitterapi-io-results.json)、[twitter-topic-brief.json](../raw/2026-11-15/twitter-topic-brief.json) |
| follow-builders 播客 | status `ok`；offered/inside/outside/unknown `1/0/1/0`；transcript `1/0`；link `0/1` | 聚合转录为 `secondary-source`；[podcast-items.json](../raw/2026-11-15/podcast-items.json) |

## X/Twitter 覆盖说明

`twitterapi.io` 请求覆盖配置中的 50 个账号，50/50 返回成功，收到 920 条原始推文并保留 169 条匹配内容。该结果窗口为近 36 小时的有限账号采样，不保证账号全量时间线。主题 brief 的分组统计为：前沿模型 43、智能体与工作流 72、编程工具 64、治理 5、基础设施 1、独立创业 27、产品增长 42、系统与自动化 37；这些计数来自主题归类，可重复计入同一条推文。主题摘要只选用本日日窗内的条目。

所有 X 内容均以 `direct-x` 标记。AIHOT 的标题或摘要即使指向 X 也不会升级为 `direct-x`；本轮 AIHOT 匹配原文是 TechCrunch 页面。没有使用登录态浏览器、Exa 或 X 写操作。

## 不确定性与待验证项

- `dwarkesh-patel` feed 返回 `curl: (52) Empty reply from server`；该来源当日覆盖缺失。
- Anthropic Engineering 索引虽已抓取，但解析出 0 个有效文章卡片，因此该源是 `limited`；不能把它记作“当天无文章”。
- 5 条一手发布正文为 `limited`：Codex `0.171.0-alpha.2`、`alpha.3`、`alpha.4`、`alpha.5` 及 Claude Code `v2.1.322`。无法据这些受限正文总结完整变更。
- AIHOT 精选只覆盖 feed 当前返回的 50 条；聚合时间、GUID 和站内页面保留为来源线索，不能证明全量 AI 新闻覆盖。唯一命中原文由 TechCrunch 报道；文章所引政府材料未在本轮逐条复读。
- X 覆盖是 `twitterapi.io` 本轮返回值，不代表完整账号历史。Fable 5.2、自动模式、生产部署等条目为个人帖子或转发；缺少独立产品文档或复现。
- 本日日窗另有 3 条高分 X 候选未纳入主题摘要，均保留为 `direct-x` 并在候选审计中标记 `insufficient_evidence`：一条对编程能力的泛化预测、一条缺少语境的开源宣传图文、一条只有讲座预告而无机制细节的转发。
- GitHub Trending 的 10 项是当日发现排序。各项目功能、评测和使用范围主要依据 README 自述；Caveman、Open Code Review、Modern Web Guidance 的测量结果不应当作独立验证。多个项目涉及浏览器数据、交易工作流、代码执行或外部云服务，采用前应逐项核对其权限、数据路径和许可证。
- 播客 feed 的 `lookback_hours=336` 只代表 follow-builders 上游提供范围；本轮 1 集并不表示所有配置节目均无更新。该集 transcript 由聚合站提供、未做音频复核；episode 链接仅有 playlist alias，canonical link 受限。

## 当天产物

- 日报：[2026-11-15-daily-intel.md](2026-11-15-daily-intel.md)
- 原始清单与状态：[report-reading-list.json](../raw/2026-11-15/report-reading-list.json)、[run-summary.json](../raw/2026-11-15/run-summary.json)、[manifest.json](../raw/2026-11-15/manifest.json)、[signals.json](../raw/2026-11-15/signals.json)
- 播客：[podcast-items.json](../raw/2026-11-15/podcast-items.json)、[feed snapshot](../raw/2026-11-15/podcasts/follow-builders/feed-podcasts.json)、[transcript](../raw/2026-11-15/podcasts/follow-builders/transcripts/a-model-for-everyone-how-ronak-from-trajectory-is-building-products-for-continua-9c6b2d4e1195.md)
- 候选审计：[JSON](../reviews/2026-11-15-candidate-audit.json)；[Markdown](../reviews/2026-11-15-candidate-audit.md)

## 边界与验证

本日报以 `raw/2026-11-15/` 中的采集归档为证据入口，目标窗口按北京时间计算。AIHOT 与 follow-builders 维持各自的聚合来源边界；X 条目保留 `direct-x`；GitHub Trending 只作为 `secondary-source` 发现材料。日报不声称覆盖全部 AI 新闻、完整 X 时间线或 follow-builders 配置的所有节目。涉及外部运行结果的数字均按来源自述或单用户观察标注，不把发现信号提升为已独立验证的结论。

<!-- dsi-candidate-audit: covered=12 missed=66 -->
