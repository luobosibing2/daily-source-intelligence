# 2026-09-28 Daily Source Intelligence

> 本日报按北京时间目标日归档。GitHub Trending 是二手发现线索；项目机制只有在本轮 README 可读时才总结。follow-builders 播客 transcript 属于聚合方二手材料，不能替代节目音频或节目官方页面。

## 直接答案

目标窗口内确认了 2 条 OpenAI Codex alpha 发布活动：`0.158.0-alpha.15.3`（03:30）和 `0.159.0-alpha.10`（05:18）。两条 GitHub Release Atom 正文都只有版本短句，今天只能确认版本、时间与发布链接，不能据此推断功能或稳定性。RSS/Atom 没有新的目标日匹配条目；GitHub Trending 解析到 9 个仓库，9/9 描述和 README 可读，属于二手发现信号。follow-builders 播客工件有效，但实际 offered 1 集在窗口外；没有可写入当日洞察卡的 inside-window transcript。X/Twitter 的 50 个账号全部因 `Credits is not enough.Please recharge` 失败，不能解释为账号没有更新。

## 0. 采集范围

- 运行日期：2026-09-28，`Asia/Shanghai`；信号窗口为 2026-09-28 00:00 至 2026-09-29 00:00。统一入口按 `DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-09-28` 执行；首轮在 follow-builders RSS 补链时遇到 `http.client.IncompleteRead`，重跑同一统一入口后成功完成。网络使用系统/TUN 或已有代理路径，未使用 Exa、登录态 X/Twitter、账号密码或任何 X 写操作。
- 配置范围：RSS/Atom、GitHub Releases、GitHub Trending、官方页面、follow-builders 公共 transcript feed、`twitterapi.io`；关注方向来自 [config/watch.md](../config/watch.md) 和 [config/topics.yaml](../config/topics.yaml)。
- RSS/Atom：32 个来源中 31 个成功、1 个失败（`dwarkesh-patel`，`curl: (52) Empty reply from server`）。50 条匹配或一手必读正文尝试中 44 条可读、6 条 `limited`，另有 105 条按主题过滤跳过。按北京时间目标窗口过滤，本轮没有 RSS/Atom 新条目；raw 中的可读历史条目保留供追溯，不能当作 9 月 28 日新信号。
- GitHub Releases：7/7 个 Atom 来源成功，共 35 条记录；10 条一手必读正文尝试中 5 条可读、5 条 `limited`。目标窗口内有 OpenAI Codex `0.158.0-alpha.15.3` 与 `0.159.0-alpha.10` 两条发布活动，但 Atom 正文只有版本短句，功能变化不可确认。
- GitHub Trending：1/1 来源成功，解析 9 个仓库；榜单描述 9/9、README 9/9 可读。星数与 `stars_today` 是单次榜单快照，不证明目标日发布、代码变化、项目质量或厂商背书。
- 官方页面：4 个来源成功、1 个 `limited`。Anthropic Engineering 索引成功解析 25 张卡片，但目标窗口 article 数为 0；OpenAI News 返回 challenge/limited HTML 且 OpenCLI fallback 未产出可读正文；Claude Blog/Docs 只有页面级 metadata，本轮没有目标日可读 article 正文。
- 播客：[`podcast-items.json`](../raw/2026-09-28/podcast-items.json) 存在且状态为 `ok`。follow-builders 本轮 offered/configured/allowed/inside/outside/unknown=`1/1/1/0/1/0`，transcript ok/limited=`1/0`，link ok/limited=`0/1`，upstream errors=`0`。唯一允许单集是 No Priors 的 “Why Diffusion Will Win AI Inference with Inception Co-Founder and CEO Stefano Ermon”，发布时间为 2026-09-18 18:00（北京时间），在目标窗口外；transcript 可读但不能进入当日洞察卡。未运行 pod2txt、Supadata、音频下载或 ASR。
- X/Twitter：请求 50 个已配置账号，0 个成功、50 个失败；每个账号返回 `Credits is not enough.Please recharge`。没有 `direct-x` 证据，失败不等于账号没有更新。
- 原始归档入口：[`raw/2026-09-28/`](../raw/2026-09-28/)、[`manifest.json`](../raw/2026-09-28/manifest.json)、[`run-summary.json`](../raw/2026-09-28/run-summary.json)、[`report-reading-list.json`](../raw/2026-09-28/report-reading-list.json)。

## 1. 今日高信号

- **OpenAI Codex 在目标窗口出现两次 alpha 发布。** `0.158.0-alpha.15.3`（北京时间 03:30）与 `0.159.0-alpha.10`（05:18）均来自 OpenAI Codex GitHub Releases，证据等级为 `official-source`。两个 release Atom body 都只有版本短句（`limited`），因此今天只能确认发布活动、时间和链接，不能从版本号推断功能、稳定性、兼容性或 breaking change。[0.158.0-alpha.15.3](https://github.com/openai/codex/releases/tag/rust-v0.158.0-alpha.15.3) · [0.159.0-alpha.10](https://github.com/openai/codex/releases/tag/rust-v0.159.0-alpha.10) · [本地 release 归档](../raw/2026-09-28/github-release-fulltext/openai-codex/)。
- **多 agent 控制面、记忆与本地编译工具继续出现在 Trending。** `paperclipai/paperclip`、`vectorize-io/hindsight`、`mvschwarz/openrig` 与 `vercel-labs/scriptc` 的 README 可读，分别提供 agent 组织治理、长期记忆、跨 Claude Code/Codex 的团队 harness、以及 TypeScript/JavaScript 到原生与 WebAssembly 的实验性编译路径。它们是 `secondary-source` discovery signal；README 自报的 benchmark、生产使用、热度和成熟度尚未做独立验证。[README 归档目录](../raw/2026-09-28/github-trending-readmes/)。

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

**OpenAI Codex alpha：** 目标窗口内确认 `0.158.0-alpha.15.3` 与 `0.159.0-alpha.10`。对应 Atom 全文分别只有短句 `Release 0.158.0-alpha.15.3` 与 `Release 0.159.0-alpha.10`，被标为 `fulltext_status=limited`；不能把版本号写成具体功能或质量变化。[`github-items.json`](../raw/2026-09-28/github-items.json) · [release Atom 归档](../raw/2026-09-28/github-release-fulltext/openai-codex/)。

**Claude Code：** 采集器取得 5 条一手 release Atom 正文，5/5 可读，但它们的 Atom 更新时间均早于本次目标窗口；本日报不把这些历史 release 的功能列表伪装成 9 月 28 日新信号。其正文仍作为一手来源覆盖保留在 [`github-release-fulltext/anthropics-claude-code/`](../raw/2026-09-28/github-release-fulltext/anthropics-claude-code/) 供后续专题核验。

**Anthropic 页面：** Engineering 索引可读并解析出 25 张卡片，但目标窗口 article 为 0；这只能支持“本轮索引检查完成、没有目标日 article”的边界。Claude Blog 页面显示近几日文章卡片，但没有目标日正文进入阅读清单。[`official-pages.json`](../raw/2026-09-28/official-pages.json) · [Anthropic Engineering index](../raw/2026-09-28/official-page-text/anthropic-engineering/anthropic-engineering-anthropic-engineering-9bba7c6d8f.index.html)。

### 模型、代理与工程效率

本轮没有目标日 RSS 正文新信号；以下结论来自可读的 GitHub Trending README，证据等级固定为 `secondary-source`：

- **Paperclip** 是 Node.js server + React UI 的多 agent 组织控制面。README 描述目标、组织图、角色和权限、预算、审批、心跳、插件、工作区与审计，把多种 agent 运行时放进同一套公司式治理模型；下一步应验证权限边界、预算 hard-stop、持久化状态和真实 adapter 行为。[Paperclip README](../raw/2026-09-28/github-trending-readmes/paperclipai__paperclip.md)
- **Hindsight** 面向“会学习而不只是回忆”的 agent memory，提供 server、Python/Node.js/Go/CLI/REST 客户端和 MCP；核心操作是 `retain`、`recall`、`reflect`，并区分事实、经验、观察、mental models 与 knowledge pages。README 的 LongMemEval 与生产使用表述属于项目方材料，不能当成独立评测结论。[Hindsight README](../raw/2026-09-28/github-trending-readmes/vectorize-io__hindsight.md)
- **OpenRig** 把多个 Claude Code/Codex 会话组织成由 YAML 定义的持久团队，依赖 Node.js 与 tmux，提供 lead agent、specialist、共享 dashboard、队列和恢复路径。README 明确提示 `rig setup` 会写 provider hooks、workspace trust 和本地配置，因此任何安装或运行都应先审阅 dry-run、备份相关文件并验证权限范围；本轮没有运行它。[OpenRig README](../raw/2026-09-28/github-trending-readmes/mvschwarz__openrig.md)
- **Univer** 是可嵌入的 Office SDK，覆盖表格、文档、演示、看板和关系表；README 描述 plugin-first、Canvas 渲染、公式引擎、浏览器/Node.js 同构和 Facade API，可让人和 agent 在同一文件上协作。它适合作为“agent 操作办公文档”的工程候选，但权限隔离、商业版边界和生产行为需单独验证。[Univer README](../raw/2026-09-28/github-trending-readmes/dream-num__univer.md)
- **AI Engineering from Scratch** 是以 lesson、phase 和可复用 prompt/skill/agent/MCP artifact 组织的 AI 工程课程。README 自述 523 lessons、20 phases、约 342 小时，并要求学习者保留命令、退出码和产物证据；数量、读者统计和学习效果均为项目方材料。[课程 README](../raw/2026-09-28/github-trending-readmes/rohitg00__ai-engineering-from-scratch.md)

### AI 基础设施、编译与媒体工具

- **scriptc** 是 Vercel Labs 的实验性 TypeScript/JavaScript 编译器，README 描述可输出 typed IR、C、LLVM IR、汇编、对象文件、原生可执行文件和 WASI WebAssembly；静态路径带小型 runtime，npm 包与 `any` 类型需要显式 `--dynamic` 嵌入 quickjs-ng。它要求 Node.js 24+，WASI 仍受网络、子进程、信号和文件监视能力边界约束；本轮只读 README，未做编译复现。[scriptc README](../raw/2026-09-28/github-trending-readmes/vercel-labs__scriptc.md)
- **VoiceStudio** 是 Electron 本地优先的语音工作台，README 把 voice cloning、voice design、视频配音、听写、转录和有声书批处理放在同一工作流，并提供本地 API/MCP 与可选远程 worker；默认引擎为 `k2-fsa/OmniVoice`，远程服务和使用分析可选。语音克隆必须取得本人许可，模型许可证、硬件需求和安装脚本需要单独审查。[VoiceStudio README](../raw/2026-09-28/github-trending-readmes/debpalash__VoiceStudio.md)
- **PipePipe** 是 NewPipe 的独立 Android fork，提供 YouTube/BiliBili SponsorBlock、恢复 dislike、原始标题、登录访问受限内容、AV1/VP9 播放、后台音乐、过滤与批量 playlist 操作。README 说明它自 2022 年独立开发，不再接收或推送 NewPipe 更新；cookie 只用于用户选择的播放流场景。涉及登录 cookie、第三方服务兼容性和分发渠道，需在隔离设备验证。[PipePipe README](../raw/2026-09-28/github-trending-readmes/InfinityLoop1308__PipePipe.md)

### 安全、治理与部署边界

- **Madeira** 把 Wine（ARM64EC）、FEX-Emu（x86-64→ARM64）与 DXMT（D3D11→Metal）组合成单一 Mach 进程，在非越狱 iPhone 上运行 Windows PC 游戏。README 明确这是研究项目，游戏兼容性、控制和稳定性都不可靠；需要 JIT 调试器附加、Apple ID 侧载以及每 7 天重签，依赖的 Wine/FEX/DXMT 是包含 iOS 改动的 fork。[Madeira README](../raw/2026-09-28/github-trending-readmes/willfaust__Madeira.md)
- **GitHub Trending 快照的统一边界：** 9/9 项目取得榜单描述与 README，本文把两份材料合并为读者向摘要；星数和 `stars_today` 只反映单次发现快照，不是发布、质量背书、采用率或独立 benchmark。涉及登录 cookie、JIT/侧载、语音身份、tmux hooks、代理/模型凭据和自动执行的项目，均未在本轮运行。

### GitHub Trending / Daily Repos

本轮 9/9 项目均取得榜单描述与 README；以下是把两者合并后的项目介绍，证据等级均为 `secondary-source` discovery signal：

- [paperclipai/paperclip](https://github.com/paperclipai/paperclip)（89,581 stars，今日 +2,527，TypeScript）：Node.js + React 的 agent 组织控制面，把目标、org chart、预算、审批、心跳、插件、成本与审计放进同一 dashboard；适合研究多 agent 组织治理，但权限、预算 hard-stop 与持久化仍需验证。[README](../raw/2026-09-28/github-trending-readmes/paperclipai__paperclip.md)
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)（37,080，今日 +4,463，Python）：长期记忆服务，提供 server/SDK/MCP 与 `retain`/`recall`/`reflect`，并区分事实、经验、观察和 mental models；README 的 benchmark 与生产宣称需要独立复测延迟、成本、删除和隔离语义。[README](../raw/2026-09-28/github-trending-readmes/vectorize-io__hindsight.md)
- [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)（39,827，今日 +3,060，Python）：本地优先的 Electron 语音工作台，把克隆/设计、配音、听写、转录和有声书批处理接到本地 API/MCP；语音许可、模型许可证、硬件和远程 worker 的数据边界需要验证。[README](../raw/2026-09-28/github-trending-readmes/debpalash__VoiceStudio.md)
- [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)（59,172，今日 +848，Python）：以 523 lessons、20 phases 和多条学习路径教授 Python、TypeScript、Rust、Julia、LLM、agent、MCP 与 Agent Skills，每课要求留下运行证据；规模与读者数字是 README 自报，不等价于学习质量验证。[README](../raw/2026-09-28/github-trending-readmes/rohitg00__ai-engineering-from-scratch.md)
- [InfinityLoop1308/PipePipe](https://github.com/InfinityLoop1308/PipePipe)（6,532，今日 +139，Shell）：独立于 NewPipe 的 Android 媒体客户端 fork，加入 SponsorBlock、dislike、原始标题、过滤、后台播放和 playlist 工具；登录 cookie 只用于用户指定的播放流，第三方服务兼容性与分发风险需隔离验证。[README](../raw/2026-09-28/github-trending-readmes/InfinityLoop1308__PipePipe.md)
- [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc)（5,355，今日 +186，TypeScript）：将 TS/JS 编译为 IR、C、LLVM、原生可执行文件与 WASI，使用 TypeScript 做解析和类型检查，npm/`any` 代码需显式 `--dynamic`；项目仍是实验性工具，平台、动态代码与 linker 边界需复现。[README](../raw/2026-09-28/github-trending-readmes/vercel-labs__scriptc.md)
- [mvschwarz/openrig](https://github.com/mvschwarz/openrig)（887，今日 +114，TypeScript）：用 YAML 定义 agent team，把 Claude Code、Codex 和其他 seat 组织成持久团队，通过 tmux、lead/specialist 协作、队列和共享 dashboard 管理工作；安装会写 hooks、trust 与实例状态，须先审阅 `rig setup --dry-run` 和权限影响。[README](../raw/2026-09-28/github-trending-readmes/mvschwarz__openrig.md)
- [dream-num/univer](https://github.com/dream-num/univer)（20,104，今日 +920，TypeScript）：可嵌入的 Office SDK，覆盖表格、文档、演示、看板和关系表，用插件架构、Canvas、公式引擎和 Facade API 支持浏览器/Node.js 与 headless agent 工作流；商业版、权限和协作状态需核对。[README](../raw/2026-09-28/github-trending-readmes/dream-num__univer.md)
- [willfaust/Madeira](https://github.com/willfaust/Madeira)（782，今日 +117，C）：在非越狱 iPhone 上用 Wine/FEX-Emu/DXMT 跑 Windows PC 游戏，单 Mach 进程加 wineserver thread；项目自称研究性质，依赖 JIT、侧载和每周重签，游戏兼容性和 fork 许可证需要逐项验证。[README](../raw/2026-09-28/github-trending-readmes/willfaust__Madeira.md)

### X/Twitter 推主主题摘要

本轮没有可归入主题的推文：[`twitter-topic-brief.json`](../raw/2026-09-28/twitter-topic-brief.json) 为 `partial`，50 个账号成功 0、失败 50、tweet 数 0。全部账号均报 `Credits is not enough.Please recharge`；空结果不是账号无更新的证据。

### 播客 / 长对话

follow-builders 工件为 `ok`，不是合法空 feed：中央 feed 实际 offered 1 集、允许/配置命中 1 集、窗口内 0 集、窗口外 1 集、未知 0 集；transcript ok/limited=`1/0`，canonical link ok/limited=`0/1`，上游错误 0。唯一归档单集是 No Priors 的 [Why Diffusion Will Win AI Inference with Inception Co-Founder and CEO Stefano Ermon](https://www.youtube.com/@NoPriorsPodcast)，GUID 为 `51c4092c-b309-11f1-8603-fb8d30e1277f`，发布时间为 2026-09-18 18:00（北京时间），明确在目标窗口外；本地聚合 transcript [可读 transcript](../raw/2026-09-28/podcasts/follow-builders/transcripts/why-diffusion-will-win-ai-inference-with-inception-co-founder-and-ceo-stefano-er-3b3fbf039413.md) 含 speaker/timestamp，但 RSS 未按 GUID 找到 canonical 单集链接，频道页不能冒充单集 URL。因没有 inside-window transcript，本轮不写洞察卡、不把节目观点升级为当日事实；证据等级固定为 `secondary-source`。feed snapshot 见 [`feed-podcasts.json`](../raw/2026-09-28/podcasts/follow-builders/feed-podcasts.json)。`offered=1` 只表示中央 feed 本轮实际提供 1 集，不表示 6 个配置节目均已完整检查或均无更新。

## 3. 来源证据表

| 来源 | 类型与覆盖 | 原始记录 / 正文归档 | 证据等级与边界 |
| --- | --- | --- | --- |
| RSS/Atom | 32 来源：31 ok、1 failed；50 条匹配/一手必读正文，44 ok、6 limited；目标窗口匹配新条目 0 | [`rss-items.json`](../raw/2026-09-28/rss-items.json)；正文索引见 [`report-reading-list.json`](../raw/2026-09-28/report-reading-list.json) | 一手源仍需按发布时间落入目标窗口；历史正文不升级为今日新信号 |
| GitHub Releases | 7/7 Atom 成功、35 条；10 条一手正文 5 ok、5 limited；目标窗口 2 条 Codex alpha | [`github-items.json`](../raw/2026-09-28/github-items.json)；[release body 归档目录](../raw/2026-09-28/github-release-fulltext/) | `official-source`；两条目标日 Codex Atom body 只有版本短句 |
| GitHub Trending | 1/1 成功、9 个仓库；榜单描述 9/9、README 9/9 | [`github-trending.json`](../raw/2026-09-28/github-trending.json)；[README 归档目录](../raw/2026-09-28/github-trending-readmes/) | `secondary-source` discovery snapshot，不代表发布、质量或采用率 |
| 官方页面 | 4 ok、1 limited；Anthropic Engineering 索引 25 卡片、目标日 article 0；OpenAI News challenge | [`official-pages.json`](../raw/2026-09-28/official-pages.json)；[Anthropic index](../raw/2026-09-28/official-page-text/anthropic-engineering/anthropic-engineering-anthropic-engineering-9bba7c6d8f.index.html) | index/metadata 不等于 article 正文；limited 只作覆盖边界 |
| `twitterapi.io` | 50 个账号 0 ok、50 failed；0 条 direct-x | [`twitterapi-io-results.json`](../raw/2026-09-28/twitterapi-io-results.json)；[`twitter-topic-brief.json`](../raw/2026-09-28/twitter-topic-brief.json) | 额度不足导致失败，不代表无更新；未使用 Exa 或登录态浏览器 |
| follow-builders | `ok`；offered/configured/allowed/inside/outside/unknown=`1/1/1/0/1/0`；transcript ok/limited=`1/0`；link ok/limited=`0/1`；upstream errors=`0` | [`podcast-items.json`](../raw/2026-09-28/podcast-items.json)；[feed snapshot](../raw/2026-09-28/podcasts/follow-builders/feed-podcasts.json)；[transcript](../raw/2026-09-28/podcasts/follow-builders/transcripts/why-diffusion-will-win-ai-inference-with-inception-co-founder-and-ceo-stefano-er-3b3fbf039413.md) | 聚合 transcript `secondary-source`；单集窗口外且 canonical link limited |
| 正文阅读清单 | 6 项：2 条 Codex release limited、4 个 Trending README 可读 | [`report-reading-list.json`](../raw/2026-09-28/report-reading-list.json) | 派生阅读控制，不替代 raw 原文；limited 项只能写边界 |

## 4. X/Twitter 覆盖说明

本轮 `twitterapi.io` 请求 50 个已配置账号，成功 0、失败 50，全部返回 `Credits is not enough.Please recharge`。`twitter-topic-brief` 为 `partial`，当前没有直接 X 证据；不得把失败结果解释为“没有更新”。未使用 Exa、登录态浏览器、账号密码或任何发帖、点赞、关注、私信等写操作。

## 5. 不确定性与待验证项

- 目标日 RSS/Atom 没有匹配新条目；raw 中 50 条匹配/一手必读正文主要是历史窗口材料，不能借其可读状态制造目标日信号。
- 两条 Codex alpha 的版本、时间和链接可确认，但 Atom body 仅有版本短句；不得从版本号推断功能、稳定性、兼容性或 breaking change。若要判断变化，下一步应取得对应 GitHub release body 或 changelog 的可读正文。
- `dwarkesh-patel` RSS 源失败；OpenAI News 是 limited/challenge，OpenCLI fallback 也未产出可读正文。Anthropic Engineering 仅确认索引卡片，没有目标日 article 正文；Claude Blog/Docs 页面 metadata 不能代替全文。
- GitHub Trending 的 9 个 README 本轮均可读，但榜单是二手快照。Paperclip、Hindsight、OpenRig、Univer、VoiceStudio、PipePipe、Madeira 和 scriptc 的权限、成本、凭据/cookie、安装脚本、数据隔离、部署安全或生产成熟度均未做运行时验证；Madeira 还涉及 JIT/侧载，VoiceStudio 涉及语音身份，PipePipe 涉及登录 cookie，OpenRig 涉及 hooks/trust 写入。
- `twitterapi.io` 额度不足导致 50 个账号全部失败，当前无 `direct-x`，不能代表账号没有更新；没有用 Exa 或登录态浏览器补漏。
- follow-builders 只反映中央 feed 本轮 offered 的内容，不承诺六个配置节目的逐节目或完整单集覆盖。唯一允许单集在窗口外、transcript 可读但 canonical link limited；没有 inside-window podcast candidate，故无被省略的当日 podcast candidate，但工件和链路边界已保留。
- 不把任何 README 自报 benchmark、star 增长、读者/客户数字或项目宣传语写成独立实验、行业共识或官方保证。

## 6. 运行统计

- 新增 seen 记录：10（首轮统一采集状态更新；补全播客的重跑未新增），seen 总数：5,925；流程索引与状态见 [`run-summary.json`](../raw/2026-09-28/run-summary.json) 和 [`manifest.json`](../raw/2026-09-28/manifest.json)。
- 信号索引：6 项，其中 2 项落在目标窗口（Codex alpha.15.3/alpha.10），4 项为发布时间 unknown 的 Trending README 边界；详见 [`signals.json`](../raw/2026-09-28/signals.json)。
- 今日高信号：2 条官方 Codex 发布活动；Trending 作为 4 条进入阅读清单的二手发现边界，完整 9 项榜单覆盖另见上文。
- RSS/Atom：32 来源，31 ok、1 failed；50 条匹配/一手必读正文 44 ok、6 limited。
- GitHub Releases：7/7 Atom，35 条；一手正文 5 ok、5 limited。
- GitHub Trending：9 个仓库，9/9 榜单描述，9/9 README。
- 官方页面：4 ok、1 limited；Anthropic Engineering 索引 25 张卡片、目标日 article 0。
- 播客：`ok`；offered 1 / configured 1 / allowed 1 / inside 0 / outside 1 / unknown 0；transcript ok 1 / limited 0；link ok 0 / limited 1；upstream errors 0。
- X/Twitter：0/50 成功、50/50 failed；不能解释为无更新。
- Candidate audit：12 条 matched-RSS 候选均为目标窗口外的历史/非窗口条目，统一以 `outside_window` 处置；审计明细见 [Markdown](../reviews/2026-09-28-candidate-audit.md) 和 [JSON](../reviews/2026-09-28-candidate-audit.json)。

<!-- dsi-candidate-audit: covered=0 missed=12 -->

## 7. 当天产物

- [`manifest.json`](../raw/2026-09-28/manifest.json)、[`run-summary.json`](../raw/2026-09-28/run-summary.json)、[`signals.json`](../raw/2026-09-28/signals.json)、[`report-reading-list.json`](../raw/2026-09-28/report-reading-list.json)。
- 播客覆盖工件：[`podcast-items.json`](../raw/2026-09-28/podcast-items.json)、[feed snapshot](../raw/2026-09-28/podcasts/follow-builders/feed-podcasts.json)、[本地 transcript](../raw/2026-09-28/podcasts/follow-builders/transcripts/why-diffusion-will-win-ai-inference-with-inception-co-founder-and-ceo-stefano-er-3b3fbf039413.md)。
- RSS / GitHub / 官方页面来源：[`rss-items.json`](../raw/2026-09-28/rss-items.json)、[`github-items.json`](../raw/2026-09-28/github-items.json)、[`github-trending.json`](../raw/2026-09-28/github-trending.json)、[`official-pages.json`](../raw/2026-09-28/official-pages.json)、[`official-link-candidates.json`](../raw/2026-09-28/official-link-candidates.json)。
- X/Twitter 状态工件：[`twitterapi-io-results.json`](../raw/2026-09-28/twitterapi-io-results.json)、[`twitter-topic-brief.json`](../raw/2026-09-28/twitter-topic-brief.json)。
- 候选审计：[`2026-09-28-candidate-audit.md`](../reviews/2026-09-28-candidate-audit.md) 和 [`2026-09-28-candidate-audit.json`](../reviews/2026-09-28-candidate-audit.json)；12 条 matched-RSS 候选均有 `outside_window` disposition。
- 本日报写作依据：[`report-reading-list.json`](../raw/2026-09-28/report-reading-list.json) 及其列出的本地正文；未生成 `translations/2026-09-28/`。

## 边界与验证

- 本文把 `official-source`、`secondary-source`、`limited`、窗口外和失败状态分开记录；后续 candidate audit、strict report validation、日期 bundle、trend marker/Phase 1/Phase 2、trend check、`dsi.py check` 和 main 发布状态以对应产物与命令输出为准。
