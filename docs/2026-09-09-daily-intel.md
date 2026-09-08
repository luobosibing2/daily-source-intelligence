# 每日源情报（2026-09-09）

<!-- dsi-candidate-audit: covered=12 missed=91 -->

## 直接答案

今天最值得关注的是四条彼此独立、证据等级不同的信号：

1. **Codex 与 Claude Code 都有窗口内版本变化，但证据不对称。** Codex `0.154.0-alpha.7` 的 release body 只有标题，不能从版本号推断功能；Claude Code `v2.1.265` 的一手 Atom body 则列出插件目录热加载、工具结果 1 GB 磁盘上限、提示缓存恢复、MCP SSE 回退、后台会话和远程控制等大量修复/改进，属于可读的官方 release 证据。
2. **OpenAI 把 Codex/Agent 连接到真实科研仪器，显示“定义清楚的实验闭环”已成为可自动运行的对象。** OpenAI 的量子计算案例说明 GPT‑5.6 Sol 通过 Codex 运行测量、分析结果并决定下一步；弱信号和新实验仍需要研究者介入，因此不能写成通用科研自主化证明。
3. **OpenAI 的产品与公共叙事在同一窗口集中出现。** 官方正文确认 ChatGPT Images 2.5 的更快生成、精细编辑、多轮一致性和可用范围；OpenAI 的 `direct-x` 帖子还宣布 Astra 面向 Plus、Pro、Business、Enterprise 用户全面推出，并提到由 Agent 组解决 Navier–Stokes 问题。后者仍应以官方论文/证明材料复核，不能只凭 X 帖文断言数学结果。
4. **Trending 项目把“技能、记忆、图表、浏览器和文档转换”包装成可安装的 Agent 工具链。** 10 个 README 全部可读，但上榜只是 `secondary-source` discovery signal；README 的性能、兼容性、绕检测和安装影响均未在本机验证。

## 采集范围

- 主窗口按北京时间 **2026-09-09 00:00 至 2026-09-10 00:00** 解释；采集时间为 `2026-09-09T05:21:29+08:00`，派生阅读清单生成于 `05:22:40+08:00`。原始归档是证据真相源，`signals.json`、`report-reading-list.json` 和 `run-summary.json` 只负责去重、路由和流程索引，不能替代正文。
- RSS/Atom 共 32 个启用源，30 个成功、2 个失败，失败为 `dwarkesh-patel`（`curl: (52) Empty reply from server`）和 `steve-blank`（`feed parse failed: syntax error: line 1, column 0`）。46 条命中主题或一手 `always_read` 策略的正文全部尝试且 `fulltext_status=ok`，104 条被过滤或跳过。失败是覆盖边界，不表示源没有更新。入口见 [`rss-items.json`](../raw/2026-09-09/rss-items.json)。
- GitHub release 共 7/7 个 Atom 源成功、35 条记录，REST API 为 `skipped`。OpenAI Codex 与 Claude Code 一手 release 共尝试 10 条，5 条 `ok`、5 条 `limited`；最新 Codex `0.154.0-alpha.7` 在窗口内但正文仅为 `Release 0.154.0-alpha.7`，Claude Code `v2.1.265` 的正文可读。入口见 [`github-items.json`](../raw/2026-09-09/github-items.json) 和 [`github-release-fulltext/`](../raw/2026-09-09/github-release-fulltext/)。
- GitHub Trending 1/1 源成功，解析 10 个 repo；10/10 有 Trending description，10/10 README 归档为 `ok`。Trending 项目时间、stars、性能和安全能力没有在本轮独立复测，全部按 `secondary-source` discovery signal 处理。入口见 [`github-trending.json`](../raw/2026-09-09/github-trending.json) 与 [`github-trending-readmes/`](../raw/2026-09-09/github-trending-readmes/)。
- 官方页面 4/4 成功；OpenAI News 的 `curl` 页面受限后用 `opencli-read` 保存了索引正文，Anthropic News、Claude Docs Release Notes 和 Claude Blog 也已写入 raw。priority X 官方链接候选 2 条，均由 `opencli-read` 归档正文：GPT TV 与 ChatGPT Images 2.5，见 [`official-link-candidates.json`](../raw/2026-09-09/official-link-candidates.json)。
- `twitterapi.io` 只读接口 27/27 个账号请求 `ok`，返回 509 条原始 tweet，保留 149 条 `direct-x`；使用 `includeReplies=false` 和有限滚动窗口。`rryssf_`、`Yangyixxxx`、`zhaogua61654931`、`lidang` 返回 raw=0；这不是“没有更新”的证明。原始数据和主题摘要见 [`twitterapi-io-results.json`](../raw/2026-09-09/twitterapi-io-results.json) 与 [`twitter-topic-brief.json`](../raw/2026-09-09/twitter-topic-brief.json)。
- [`report-reading-list.json`](../raw/2026-09-09/report-reading-list.json) 共 14 条：2 条官方链接正文、1 条 RSS 正文、2 条 GitHub release 条目、9 条结构化 X 条目。所有带 `local_body_path` 的正文/README 已逐项读取；没有本地正文的 X 条目只按结构化 `direct-x` 证据处理。

## 今日高信号

1. **Claude Code `v2.1.265` 把运行时治理和长会话可靠性继续产品化。** [一手 release Atom 正文](../raw/2026-09-09/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.265-e40558a093.atom.md)明确写出 `--plugin-dir` 子目录 manifest 自动加载与运行中增删发现、工具结果保存 1 GB 上限、插件路径 symlink containment 修复、MCP 旧 HTTP/SSE 回退、后台 `--bg` 会话不再中途退休、远程控制结束信号时序修复、长会话 resume 加速等。证据等级为 `official-source`；这是 release notes 的能力声明，不等于本机已升级或所有宿主默认启用。
2. **Codex `0.154.0-alpha.7` 是窗口内一手新版本，但正文受限。** [Atom 归档](../raw/2026-09-09/github-release-fulltext/openai-codex/openai-codex-0.154.0-alpha.7-5e39acf2b7.atom.md)显示更新时间为 2026-09-09 01:47 北京时间，正文只有标题，`fulltext_status=limited`；只能确认 release 条目出现，不能补写功能、默认模型、权限、MCP 或本机状态。
3. **OpenAI 的量子计算案例显示 Agent 能处理“测量—分析—下一步”闭环。** [《How GPT‑5.6 Sol helps run quantum computing experiments》](../raw/2026-09-09/rss-fulltext/openai-blog/openai-blog-how-gpt-5.6-sol-helps-run-quantum-computing-experiments-167bce5d47.opencli.md)说明 GPT‑5.6 Sol 经 Codex 连接实验室软件，运行超导量子比特测量、分析结果并调整后续参数；清晰信号下可少量干预，弱/噪声信号和新实验仍需研究者指导。它是一个 OpenAI 发布的单案例，未提供独立对照、可重复性或跨实验室采用率。
4. **ChatGPT Images 2.5 将图像模型升级与工作流控制一起发布。** [官方正文](../raw/2026-09-09/official-link-candidates/sama-2097410967978324010-introducing-chatgpt-images-2-5.opencli.md)描述更快生成、参考图保真、精细编辑、多轮一致性、Sketch、模板和图像评论，并称已向 ChatGPT、ChatGPT Work 和 Codex 用户开放；文章还给出“延迟最多降低 50%”和每周 30 亿张图的厂商自述数字，不能当成独立基准。
5. **OpenAI 的 X 帖子把 Astra 的可用范围与数学 Agent 叙事推到公共窗口。** [@OpenAI 的 2097431322117476423](https://x.com/OpenAI/status/2097431322117476423)（`direct-x`）称 Astra 已向 Plus、Pro、Business、Enterprise 的 Codex 和 ChatGPT Work 全面推出；[@OpenAI 的 2097374640582668336](https://x.com/OpenAI/status/2097374640582668336)（`direct-x`）称由一组 Agent 产生 Navier–Stokes 问题的解。前者需要账户/地区实际回读，后者需要论文、证明和独立数学核验；帖子不是完整产品文档或学术证明。
6. **X 上的 Agent 讨论出现“数据集即 Agent 接口”的商业假设。** [@gregisenberg 的 2097048828826275988](https://x.com/gregisenberg/status/2097048828826275988)（`direct-x`）提出由用户贡献细分数据、向专业用户收费，并按 Agent 查询收费的三层模式；它是创业者观点，没有样本、客户、支付或复购证据，不能写成市场已验证。

## 一手重点源 / First-party OpenAI & Claude Code

### OpenAI

- [GPT‑5.6 Sol 量子计算案例](../raw/2026-09-09/rss-fulltext/openai-blog/openai-blog-how-gpt-5.6-sol-helps-run-quantum-computing-experiments-167bce5d47.opencli.md)（`official-source`，`fulltext_status=ok`）：说明 Codex Agent 在定义清晰的量子比特校准测量中可连续运行并让研究者转向实验设计；弱信号仍需要人类指导。
- [ChatGPT Images 2.5](../raw/2026-09-09/official-link-candidates/sama-2097410967978324010-introducing-chatgpt-images-2-5.opencli.md)（`official-source` 与 `direct-x` 组合，`fulltext_status=ok`）：正文包含产品功能和厂商自述性能/使用量数字；这些数字尚未独立复测。
- [GPT TV](../raw/2026-09-09/official-link-candidates/openai-2097431322117476423-gpt-tv.opencli.md)（`official-source` 与 `direct-x` 组合，`fulltext_status=ok`）：页面能确认由 GPT‑6 Astra 驱动的 ChatGPT TV/直播入口，但正文主要是媒体页面和加载状态，不能据此推断产品稳定性或长期形态。
- [Codex `0.154.0-alpha.7`](../raw/2026-09-09/github-release-fulltext/openai-codex/openai-codex-0.154.0-alpha.7-5e39acf2b7.atom.md)（`official-source`，`fulltext_status=limited`）：只确认版本条目和时间，未知 changelog。
- `openai-blog` 其余 4 条 `always_read` 正文也均为 `ok`，包括 *The Work Now Within Reach*、*Introducing ChatGPT Images 2.5*、*On the Navier–Stokes Millennium Prize Problem*、*Funding grants for new research into AI and teen development*；本报告只把有可读正文且与窗口/主题直接相关的材料提升为高信号。

### Anthropic 与 Claude Code

- [Claude Code `v2.1.265`](../raw/2026-09-09/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.265-e40558a093.atom.md)（`official-source`，`fulltext_status=ok`）：可读变更列表覆盖插件目录发现、工具结果落盘上限、提示缓存、SubagentStart/skills、MCP SSE、远程控制、后台会话、工作树并行 checkout 等。
- `v2.1.263` 的 Atom body 仍为 `limited`，只能看到 bug-fix 摘要；`v2.1.261`、`v2.1.260`、`v2.1.259` 正文可读，但不把历史版本混写成 9 月 9 日新功能。对应归档见 [`anthropics-claude-code/`](../raw/2026-09-09/github-release-fulltext/anthropics-claude-code/)。

## 按主题分组摘要

### LLM / Frontier Models

- OpenAI 的 Astra、GPT‑5.6 Sol 和 ChatGPT Images 2.5 在本窗口形成产品、科研和图像工作流的多面信号；X 中 [@sama 的 2097404861642137851](https://x.com/sama/status/2097404861642137851)（`direct-x`）还预告 9 月 16 日在旧金山与 GPT‑6 用户交流。用户可用性与模型能力仍需产品界面、版本日志和独立测试复核。

### AI Agent / Agentic Workflow

- 量子实验案例展示 Agent 依据测量结果选择下一步，Claude Code release 则展示插件、后台会话、MCP 和子 Agent 可靠性继续被工程化；[@OpenAI 的数学问题帖子](https://x.com/OpenAI/status/2097374640582668336)（`direct-x`）是更高风险的能力叙事，仍缺外部证明。

### AI Coding / Developer Tools

- Claude Code `v2.1.265` 的可读 release notes 是今日最实的 coding-agent 变化；Trending 的 [`obra/superpowers`](https://github.com/obra/superpowers) 与 [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) README 则分别把开发方法论和“减少错误假设、要求澄清”的操作规则打包成可安装材料，但未验证宿主兼容性。

### AI Governance / Public Legitimacy

- X brief 的治理主题只有 OpenAI 的 Astra 与数学 Agent 叙事；这类公开能力声明会影响公共信任，但本轮没有新的监管文本、标准、政府文件或独立治理结果，不能把产品宣传当治理证据。

### AI Infrastructure / Open Source

- Trending 的 `microsoft/markitdown`、`cathrynlavery/diagram-design` 和 `heygen-com/hyperframes` 说明 Agent 输入转换、图表生成和视频渲染正在被拆成可复用组件；项目自述的兼容性、确定性和性能尚未在本机复测。

### Indie Hacking / Solo Founder

- [@gregisenberg 的 2097048828826275988](https://x.com/gregisenberg/status/2097048828826275988)（`direct-x`）提出细分数据集按查询向 Agent 收费；[@marclou 的 2096911867516252385](https://x.com/marclou/status/2096911867516252385)（`direct-x`）讲述个人创业收入与项目数量。二者都是个人叙事，没有账本、合同或可复制性材料。

### Product / Growth / GTM

- `coreyhaines31/marketingskills` README 将 CRO、文案、SEO、分析、定价和增长工程拆成跨宿主技能；[@rileybrown 的 2097080191163998488](https://x.com/rileybrown/status/2097080191163998488)（`direct-x`）分享 Astra 体验，但帖子不构成产品转化或生产率的独立测量。

### AI Systems / Automation

- Claude Code release 的后台 `--bg`、远程控制、MCP SSE 和长会话恢复修复，与 `openai/skills`、ECC 的技能/记忆/安全目录共同指向 Agent 运行时系统化；README 和 release notes 不等于本机启用或跨平台可靠性。

### X/Twitter 推主主题摘要

主题 brief 共保留 149 条 `direct-x`，主题计数相互重叠，不能相加。以下每个主题只列 1 条代表性帖子；没有本地正文、媒体转录或完整 thread 上下文，帖子中的数字与能力描述均需后续核验。

#### LLM / Frontier Models

- [@OpenAI 的 2097431322117476423](https://x.com/OpenAI/status/2097431322117476423)（`direct-x`）：宣布 Astra 面向 Plus、Pro、Business、Enterprise 的 Codex/ChatGPT Work 全面推出；实际账户可用性需回读。

#### AI Agent / Agentic Workflow

- [@gregisenberg 的 2097048828826275988](https://x.com/gregisenberg/status/2097048828826275988)（`direct-x`）：把细分数据集描述为可向 Agent 按查询计费的接口；是商业假设。

#### AI Coding / Developer Tools

- [@OpenAI 的 2097431322117476423](https://x.com/OpenAI/status/2097431322117476423)（`direct-x`）：与 Codex 可用范围相关，但没有 CLI/SDK 版本、权限或配额细节。

#### AI Governance / Public Legitimacy

- [@OpenAI 的 2097374640582668336](https://x.com/OpenAI/status/2097374640582668336)（`direct-x`）：把 Agent 与 Navier–Stokes 证明联系起来；需要论文、证明和独立数学核验。

#### AI Infrastructure / Open Source

- [@gregisenberg 的 2097381384608166057](https://x.com/gregisenberg/status/2097381384608166057)（`direct-x`）：推荐关于开源模型、Hugging Face 与云端 AI 商业的课程线索；不等于课程或产业数据已验证。

#### Indie Hacking / Solo Founder

- [@marclou 的 2096911867516252385](https://x.com/marclou/status/2096911867516252385)（`direct-x`）：个人创业收入/项目数量自述；没有财务凭证。

#### Product / Growth / GTM

- [@rileybrown 的 2097080191163998488](https://x.com/rileybrown/status/2097080191163998488)（`direct-x`）：分享 Astra 将整份地产 PDF 转为 Blender 等个人体验；未提供输入、提示、失败率或复现记录。

#### AI Systems / Automation

- [@steipete 的 2097091456234111377](https://x.com/steipete/status/2097091456234111377)（`direct-x`）：谈到 Agent coding PR 的上游评审反馈；没有完整仓库、变更或生产指标。

## GitHub Trending 项目说明

本节把 Trending description 与已读 README 合成项目介绍。10 个项目的上榜时间未知，全部是 `secondary-source` discovery signal；没有安装、部署或安全复测。

1. **`ayghri/i-have-adhd`：面向注意力负担的编码 Agent 输出规则。** README 以“ADHD-friendly outputs”为目标，提供中英文等多语言说明和更易扫描的回答格式；它解决的是输出组织与可读性，不是医学诊断或治疗。规则是否改善任务完成率需受控对照，不能因项目名推断用户健康状况。
2. **`cathrynlavery/diagram-design`：面向 Claude Code、Codex 和 Pi 的编辑图表目录。** README 列出架构、循环等多种 editorial diagram 类型，并用 HTML/SVG 与共享记忆中心表达自我改进循环；这是设计模板与生成约束，未证明图表准确性或生产可用性。
3. **`openai/skills`：Codex Agent Skills 目录，但 README 明确标注已弃用。** README 将 Skill 定义为可发现的指令、脚本和资源文件，并把当前示例指向 OpenAI Plugins 仓库和插件构建文档；它可作为历史目录线索，不能当作当前 Codex 安装源或已加载技能证明。
4. **`affaan-m/ECC`：把计划、测试、实现、评审、验证、记忆和安全扫描组织成多宿主 Agent harness。** README 覆盖 Claude Code、Codex、Cursor、OpenCode 等适配与 hooks/skills/memory；安装可能写入宿主配置和记忆，需先隔离审计权限与文件影响。
5. **`heygen-com/hyperframes`：用 HTML、CLI 和 skills 生成视频。** README 强调 composition 是 HTML、支持产品介绍/代码 diff/数据可视化/文档视频，并主张相同输入产生相同帧、可用于 CI；渲染质量、许可证和 Agent 成功率未验证。
6. **`coreyhaines31/marketingskills`：可安装的营销 Agent 技能集合。** README 覆盖 CRO、文案、SEO/AEO、分析、launch、pricing 和 revops，支持 Claude Code、Codex、Cursor、Windsurf 及 Agent Skills spec；技能安装与营销效果不是同一件事，不能把作者/合作方描述当转化证据。
7. **`obra/superpowers`：面向 coding agent 的可组合技能与软件开发方法论。** README 提供多宿主安装入口、技能/计划/评审工作流；方法论是否改善交付质量需按具体宿主、权限和仓库验证，本轮没有安装。
8. **`multica-ai/andrej-karpathy-skills`：用单个 `CLAUDE.md` 约束错误假设和澄清行为。** README 从 Karpathy 公开观察出发，要求 Agent 管理不确定性、不要未经确认地一路执行；这是提示与流程建议，不能冒充 Karpathy 官方规则或效果研究。
9. **`microsoft/markitdown`：把 PDF、Office、图片、音频、HTML、CSV/JSON/XML 等转成 Markdown 的 Python 工具。** README 明确警告 I/O 使用当前进程权限，服务端需清洗不可信输入并调用最窄的 `convert_*` 接口；它适合作为模型输入预处理，但不等于保真排版转换。
10. **`jo-inc/camofox-browser`：面向 Agent 的反检测浏览器服务。** README 描述 Camoufox、会话隔离、cookie 导入、代理/GeoIP、VNC、下载捕获和 JSON tracing，并明确把绕过 Cloudflare/bot detection 当卖点；这是安全与合规敏感能力，本轮没有运行、导入 cookie 或审计数据流。

## 来源证据表

| 来源组 | 本轮结果 | 证据与边界 |
| --- | --- | --- |
| RSS/Atom | 32 个源；30 成功、2 失败；46 条命中/一手正文尝试且 46 条 `ok` | [`rss-items.json`](../raw/2026-09-09/rss-items.json)。`dwarkesh-patel`、`steve-blank` 失败是覆盖边界；其余历史 feed 条目不能自动视为今日事件。 |
| GitHub release | 7/7 Atom 成功；35 条记录；一手 release 10 条尝试，5 `ok`、5 `limited` | [`github-items.json`](../raw/2026-09-09/github-items.json) 与 [`github-release-fulltext/`](../raw/2026-09-09/github-release-fulltext/)。REST API 为 `skipped`。 |
| GitHub Trending | 1/1 成功；10 个 repo；10/10 description、10/10 README `ok` | [`github-trending.json`](../raw/2026-09-09/github-trending.json) 与 [`github-trending-readmes/`](../raw/2026-09-09/github-trending-readmes/)。全部是 `secondary-source` discovery signal。 |
| 官方页面 | 4/4 成功；OpenAI News 使用 `opencli-read` | [`official-pages.json`](../raw/2026-09-09/official-pages.json)。索引页/卡片不能替代单篇正文。 |
| 官方链接候选 | 2 条；GPT TV 与 ChatGPT Images 2.5 均 `fulltext_status=ok` | [`official-link-candidates.json`](../raw/2026-09-09/official-link-candidates.json) 与两个 `opencli.md` 归档；组合证据仍不能替代账户或实验复核。 |
| X/Twitter | 27/27 账号请求 `ok`；509 条原始、149 条保留 `direct-x` | [`twitterapi-io-results.json`](../raw/2026-09-09/twitterapi-io-results.json) 与 [`twitter-topic-brief.json`](../raw/2026-09-09/twitter-topic-brief.json)。是有限窗口和相关性筛选，不是完整时间线。 |
| 日报阅读清单 | 14 条；4 条有本地正文，10 条为结构化 X 或受限 release | [`report-reading-list.json`](../raw/2026-09-09/report-reading-list.json)。本地正文/README 均已逐项读取。 |

## X/Twitter 覆盖说明

本轮 X 由 `twitterapi.io` 的 `GET /twitter/user/last_tweets` 只读接口采集，27 个账号请求均为 `ok`，原始 509 条，保留 149 条 `direct-x`。主题 brief 的计数为 `llm=55`、`ai-agent=122`、`ai-coding=99`、`ai-governance=4`、`infra=3`、`indie-founder=41`、`product-growth=74`、`ai-systems=40`，主题相互重叠，不能相加成 149；当前 brief 没有独立 `fde` 条目。

账号级边界必须与“无更新”分开：`rryssf_`、`Yangyixxxx`、`zhaogua61654931`、`lidang` raw=0；`karpathy`、`AnthropicAI`、`simonw`、`oviswang`、`_LuoFuli` 有请求但 kept=0。它们可能是有限窗口、筛选或相关性过滤结果，不构成账号没有更新的证明。本轮没有使用登录态 X 浏览器、官方 X API、发帖/点赞/关注/私信或 Exa MCP，也没有用其它发现层补漏。

下列窗口内或 36 小时内的高分候选未全部进入“今日高信号”，原因是观点、转发、主窗口外、没有原始材料或与关注方向弱相关：[@rileybrown 的 2096969016136908860](https://x.com/rileybrown/status/2096969016136908860)、[@mattpocockuk 的 2096906181121818702](https://x.com/mattpocockuk/status/2096906181121818702)、[@levelsio 的 2096916717955903539](https://x.com/levelsio/status/2096916717955903539)、[@jackfriks 的 2096985034041221240](https://x.com/jackfriks/status/2096980473754866081)、[@genspark_ai 的 2096921237973037417](https://x.com/genspark_ai/status/2096921237973037417)、[@frxiaobei 的 2096946066885419489](https://x.com/frxiaobei/status/2096946066885419489)。这些链接作为 candidate audit 的可追溯入口，不改变 `direct-x` 证据等级。

## 不确定性与待验证项

- `dwarkesh-patel` RSS 与 `steve-blank` RSS 分别因空响应和 feed 解析失败而缺失覆盖；没有用 Exa 或其它发现层替代。
- RSS/Atom 命中正文虽然 46/46 可读，但多条是历史文章；主窗口内可直接支撑的稳定新增主要是 OpenAI 量子计算案例与 Claude Code `v2.1.265`/Codex `0.154.0-alpha.7` release。不能把历史博客、feed summary 或版本相邻条目写成今日新增。
- Codex `0.154.0-alpha.7` 以及同批次其他 Codex/Claude release 中 5 条 body 为 `limited`；不能从版本号、标题或邻近版本补写具体功能、默认开关、MCP/插件行为、本机升级或 Marketplace 状态。
- `direct-x` 的 149 条保留项来自有限账号、滚动窗口和相关性筛选；主题计数重叠，转发、截断文本、未展开媒体和帖子中的数字不构成独立确认。Astra 可用范围、Navier–Stokes 解、个人收入、模型 benchmark 和“Agent 替代 IDE”等主张都需要原始材料、账户回读或复现实验。
- Trending README 全部可读，但项目自述的性能、stars、兼容性、确定性、跨平台支持和安全能力没有本机验证。`camofox-browser` 的绕检测/cookie/代理功能、`ECC`/`superpowers` 的安装写入、`markitdown` 的进程权限，以及 `openai/skills` 已弃用状态，均应先做隔离和许可/数据流审计。
- 官方页面 4/4 成功，OpenAI News 使用 `opencli-read`；页面索引和候选正文可以支持“页面存在/内容可读”，不能支持组织采用、账户资格、数学证明或产品稳定性结论。

## 当天产物

- 原始与派生状态：[`manifest.json`](../raw/2026-09-09/manifest.json)、[`signals.json`](../raw/2026-09-09/signals.json)、[`report-reading-list.json`](../raw/2026-09-09/report-reading-list.json)、[`run-summary.json`](../raw/2026-09-09/run-summary.json)。
- 稳定来源：[`rss-items.json`](../raw/2026-09-09/rss-items.json)、[`github-items.json`](../raw/2026-09-09/github-items.json)、[`github-trending.json`](../raw/2026-09-09/github-trending.json)、[`official-pages.json`](../raw/2026-09-09/official-pages.json)。
- X 与官方候选：[`twitterapi-io-results.json`](../raw/2026-09-09/twitterapi-io-results.json)、[`twitter-topic-brief.json`](../raw/2026-09-09/twitter-topic-brief.json)、[`official-link-candidates.json`](../raw/2026-09-09/official-link-candidates.json)。
- 正文归档：[`rss-fulltext/`](../raw/2026-09-09/rss-fulltext/)、[`github-release-fulltext/`](../raw/2026-09-09/github-release-fulltext/)、[`github-trending-readmes/`](../raw/2026-09-09/github-trending-readmes/)、[`official-page-text/`](../raw/2026-09-09/official-page-text/)、[`official-link-candidates/`](../raw/2026-09-09/official-link-candidates/)。
- 本文件：[`docs/2026-09-09-daily-intel.md`](2026-09-09-daily-intel.md)。candidate audit、严格日报校验、bundle、trend、main worktree 发布和 email 属于本初稿之后的闭环步骤，完成前不预填成功状态。

## 边界与验证

- **已确认：** 当日稳定来源 raw、X raw/brief、官方链接正文、GitHub Trending README、`manifest.json`、`signals.json`、`report-reading-list.json` 和 `run-summary.json` 均已生成；采集失败源、limited release 和 raw=0 账号均保留了覆盖边界。
- **已确认：** 阅读清单中的本地正文/README 已逐项读取；无 `local_body_path` 的条目只按受限 release 或结构化 `direct-x` 证据处理，未把帖子摘要写成已读原文。
- **未覆盖：** 两个失败 RSS；X 完整时间线、媒体、回复上下文和未展开链接；受限 release body；Trending 项目的安装、部署、性能、安全、许可证、真实资金或实际采用；帖子背后的论文、实验和财务原始数据。
- **运行时可能变化：** X API 返回、GitHub Trending、RSS/官方页面内容、产品/插件版本、组织权限、`origin/main` 和 Gmail 认证状态只能以后续独立回读为准。下一步是运行 candidate audit 并回填 marker，再做严格日报校验与 bundle；随后为 9 个 enabled trend 准备唯一 marker、执行 Phase 1/Phase 2 与 trend check，最后才发布到 dedicated main worktree 并发送/回读 Gmail。
