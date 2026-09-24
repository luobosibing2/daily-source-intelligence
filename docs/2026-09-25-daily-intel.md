# 2026-09-25 Daily Source Intelligence

> 本日报按北京时间目标日归档。GitHub Trending 是二手发现线索，项目功能来自各仓库 README 自述；follow-builders 播客若出现，只代表聚合方 transcript 材料。

## 0. 采集范围

- 运行日期：2026-09-25，Asia/Shanghai；信号窗口为 2026-09-25 00:00 至 2026-09-26 00:00。统一入口在 05:21 完成，命令为 `DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-09-25`。
- 配置范围：RSS/Atom、GitHub Releases、GitHub Trending、官方页面、follow-builders 公共播客 transcript feed、`twitterapi.io`；关注方向来自 [config/watch.md](../config/watch.md) 和 [config/topics.yaml](../config/topics.yaml)。
- RSS/Atom：32 个来源中 31 个成功、1 个失败（`dwarkesh-patel`，`curl: (52) Empty reply from server`）；155 条 feed 记录中 48 条匹配或一手必读正文尝试，45 条可读、3 条 limited、0 条 failed，另有 107 条按主题过滤跳过。可读当前窗口 RSS 正文为 Google DeepMind 的 Gemini 3.8 Live with Live Avatar；limited 条目仍只作覆盖边界。
- GitHub Releases：7/7 个 Atom 来源成功，共 35 条记录；一手必读正文尝试 10 条，5 条可读、5 条 limited。目标窗口可进入信号索引的是 OpenAI Codex 的 3 个 alpha 条目和 Claude Code `v2.1.282`；Codex 三条仅有 limited Atom 占位，不能由版本号推断功能。
- GitHub Trending：1/1 来源成功，解析 10 个仓库；榜单描述 10/10、README 10/10。星数和 `stars_today` 是约 05:20 的单次快照，不证明目标日发布、代码变化、项目质量或厂商背书。
- 官方页面：5 个来源中 4 个成功、1 个 limited（OpenAI News 返回 challenge，OpenCLI fallback 也未产生可读正文）；Anthropic Engineering 索引解析出 25 张卡片，但目标窗口没有 article。
- 播客：follow-builders 完整 feed 快照成功保存，但 `podcast-items.json` 为 `status=partial`；本轮规范化 `offered=0`、`configured=0`、`inside=0`、`outside=0`、`unknown=0`，transcript ok/limited 为 0/0、canonical link ok/limited 为 0/0，`upstream_error_count=3`。3 个 transcript 请求返回 HTTP 404（Episode not found）。`offered=0` 只表示本轮没有可规范化的上游单集，且本轮有上游错误，不等于逐一检查了所有节目或确认没有节目更新；未运行 pod2txt、音频下载或 ASR。
- X/Twitter：请求 `x_accounts` 的 50 个账号，0 个成功、50 个失败；绝大多数错误为 `Credits is not enough.Please recharge`，`mattturck` 为 TLS 连接失败。没有 `direct-x` 证据，不能据此解释为账号没有更新。
- 原始归档：[raw/2026-09-25](../raw/2026-09-25/)；流程索引 [run-summary.json](../raw/2026-09-25/run-summary.json)、[manifest.json](../raw/2026-09-25/manifest.json) 与 [report-reading-list.json](../raw/2026-09-25/report-reading-list.json)。

## 1. 今日高信号

- **Claude Code 把治理可见性、网关就绪和长会话恢复继续做成运行时能力。** `v2.1.282` 的可读 release body 新增 `maxProseWidth`，让宽终端中的 prose 受控而表格/代码保持全宽；启动提示、`/status` 和 `claude doctor` 会列出项目设置中被忽略或关闭 telemetry 的变量；新增 `allowClaudeInChromeWithManagedMcp`，并为 Claude apps gateway 增加 `store.readiness_grace_seconds`。同时修复恢复会话重发消息、extended thinking 丢失、不可解密 web-search 结果、redacted thinking 错误和压缩失败等路径。这是官方发布说明中的变更声明，不等于本地运行时验证。[v2.1.282 release](https://github.com/anthropics/claude-code/releases/tag/v2.1.282)（`official-source`，正文已归档）。
- **实时对话开始把“可见化身＋持续工具执行”作为企业产品形态。** Google DeepMind 页面称 Gemini 3.8 Live with Live Avatar 将近实时视频、语音和视觉输入组合成带口型同步、表情与轮次控制的对话；异步工具调用可在对话继续时后台取数；页面还声称支持 97 种语言切换、参考图定制化身（当前需企业 allowlisting）和 SynthID 水印。这些是页面自述，流水线对该 RSS 正文标为 `secondary-source`，不应升级为独立性能验证。[Introducing Gemini 3.8 Live with Live Avatar](https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/)（正文已归档）。

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

**Claude Code `v2.1.282`：** 当前窗口唯一进入可读正文清单的 Claude Code release。除上面的治理与网关变化外，release body 还写到：managed permissions、`autoMode`、`worktree`、attribution 等设置在嵌套值部分无效时仍尽量应用；项目/本地 settings 中会忽略开启遥测导出的 OpenTelemetry 变量；server-side classifier 默认用于 direct Anthropic API 的 auto mode（telemetry 关闭时可退出）；长会话恢复、slash command 期间 thinking、插件/skills、Windows/WSL 管理设置和 VSCode/Cloud sessions 有大量边界修复。[release body](../raw/2026-09-25/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.282-cd3a2bc67e.atom.md)

**OpenAI Codex alpha：** `rust-v0.158.0-alpha.10`、`rust-v0.158.0-alpha.9` 与 `rust-v0.157.0-alpha.11.1` 在窗口内出现，但 release Atom 正文均为 `limited`；版本、时间与链接可确认，功能变化不可确认。[github-items.json](../raw/2026-09-25/github-items.json)

### 模型、代理与工程效率

Gemini 3.8 Live with Live Avatar 把实时音视频、异步工具执行、多语言口型同步和可定制角色放到同一企业对话界面；页面还强调 SynthID 透明标记。这说明产品化重点从“模型能否回答”延伸到持续对话中的视觉存在、工具编排和身份/溯源，但 97 语言、低延迟和视频保真等数字均是厂商页面自述。[原文归档](../raw/2026-09-25/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-gemini-3.8-live-with-live-avatar-e7107d9a76.extracted.md)

### GitHub Trending / Daily Repos

本次 10 个仓库的 README 均已归档，榜单描述覆盖 10/10；以下星数与今日增量来自单次榜单快照，功能和限制来自 README，证据等级均为 `secondary-source`，不表示目标日发布或稳定性背书。

- [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)（56,439 stars，今日 +310）：面向从零学习 AI 工程的开源课程，README 自述包含 523 节课、20 个阶段、约 342 小时，覆盖 Python、TypeScript、Rust、Julia；每课产出 prompt、skill、agent 或 MCP server 等可复用工件。它更像完整学习路径而非单一运行时，课程统计和学习效果仍需独立核验。[README](../raw/2026-09-25/github-trending-readmes/rohitg00__ai-engineering-from-scratch.md)
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)（27,685 stars，今日 +1,607）：面向长期记忆的 agent memory 系统，把 retain、recall、reflect、观察和 mental model 组合起来，支持 Docker、嵌入式运行、PostgreSQL/pgvector、Oracle、MCP 与多种 coding-agent 集成。README 提到 LongMemEval 等基准和生产使用，但这些数字主要是项目方自述；多租户隔离、PII 防御与云服务成本需实测。[README](../raw/2026-09-25/github-trending-readmes/vectorize-io__hindsight.md)
- [dream-num/univer](https://github.com/dream-num/univer)（17,485 stars，今日 +1,060）：可嵌入产品的 Office SDK，覆盖表格、文档、演示、Bases、Boards 和开发中的 PDF；通过插件架构、Canvas 渲染、公式引擎和浏览器/Node.js 统一 Facade API，面向 SaaS、内部工具、BI 与 AI 应用。权限隔离、公式兼容性和服务端处理边界不能只凭 README 推断。[README](../raw/2026-09-25/github-trending-readmes/dream-num__univer.md)
- [google/ax](https://github.com/google/ax)（10,248 stars，今日 +1,376）：声明式 agent 编排器，以 `Workspace`、`Task`、gateway、网络围栏和沙箱运行自主任务，CLI 类似 Kubernetes 的 apply/watch/ssh；README 明确警告协议与核心概念仍在快速变化、稳定前可能有重大破坏性变更。大规模吞吐和隔离强度仍需独立验证。[README](../raw/2026-09-25/github-trending-readmes/google__ax.md)
- [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer)（4,033 stars，今日 +22）：把量化、剪枝、NAS、蒸馏、投机解码和稀疏化组合成 Python 优化库，输入可来自 Hugging Face、PyTorch 或 ONNX，输出可部署到 TensorRT-LLM、TensorRT、vLLM、SGLang 等框架。README 的吞吐/压缩倍数和 2026-09-16 Qwen3.6 教程数据是项目方材料，不替代目标硬件上的基准。[README](../raw/2026-09-25/github-trending-readmes/NVIDIA__Model-Optimizer.md)
- [FxEmbed/FxEmbed](https://github.com/FxEmbed/FxEmbed)（5,346 stars，今日 +165）：通过 `fx`/`fixup` 前缀修复 X/Twitter 和 Bluesky 的视频、投票、引用、翻译等嵌入，目标渠道包括 Discord 和 Telegram；README 说明它以 Cloudflare Worker 运行，可用 Docker/Wrangler 自托管并按 Host 路由。它依赖第三方平台公开接口与域名配置，稳定性、隐私和平台政策需另行检查。[README](../raw/2026-09-25/github-trending-readmes/FxEmbed__FxEmbed.md)
- [anthropics/financial-services](https://github.com/anthropics/financial-services)（37,326 stars，今日 +510；榜单描述缺失）：提供投资银行、股票研究、私募和财富管理工作流的 agents、skills 与数据连接器，可作为 Claude Cowork 插件或通过 Managed Agents API 部署。README 明确只起草模型、备忘录、研究笔记和对账材料，需专业人员审核，不做投资建议、交易执行、记账或开户审批；金融数据、权限和合规仍需独立核验。[README](../raw/2026-09-25/github-trending-readmes/anthropics__financial-services.md)
- [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)（50,290 stars，今日 +415）：通过 CLI-Hub 安装和管理社区生成的 CLI，把 CAD、3D、图表、游戏、字幕等软件包装成 agent 可调用命令，并展示 preview/trajectory 产物流程。它可能触达本机文件、外部服务和凭据；使用前应审查生成 CLI 的供应链、权限和执行隔离。[README](../raw/2026-09-25/github-trending-readmes/HKUDS__CLI-Anything.md)
- [mvt-project/mvt](https://github.com/mvt-project/mvt)（14,698 stars，今日 +275）：Amnesty International Security Lab 维护的移动设备取证工具集，用于收集 Android/iOS 痕迹、检查潜在入侵指标；README 警告 v3 带来破坏性变化，并明确这是面向技术人员和调查人员的取证工具，不是终端用户自测工具。调查授权、证据保全与解释能力需由专业人员负责。[README](../raw/2026-09-25/github-trending-readmes/mvt-project__mvt.md)
- [obra/superpowers](https://github.com/obra/superpowers)（291,183 stars，今日 +606）：把澄清需求、分段规格、实现计划、TDD、调试与验证组织成可组合的 coding-agent skills，并覆盖多个 agent CLI。README 描述的是工作方法和提示约束，不等于具体团队已建立审查、权限和测试门禁。[README](../raw/2026-09-25/github-trending-readmes/obra__superpowers.md)

### X/Twitter 推主主题摘要

本轮没有可归入主题的推文：`twitter-topic-brief.json` 为 `partial`，50 个账号成功 0、失败 50，tweet 数为 0。失败主要是 `Credits is not enough.Please recharge`，`mattturck` 另有 TLS 连接错误；空结果不是账号无更新的证据。详见 [twitter-topic-brief.json](../raw/2026-09-25/twitter-topic-brief.json) 与 [twitterapi-io-results.json](../raw/2026-09-25/twitterapi-io-results.json)。

### 播客 / 长对话

本轮 follow-builders 工件存在但为 `status=partial`：中央 feed 快照 HTTP 200，`offered=0`、`configured=0`、`inside=0`、`outside=0`、`unknown=0`，transcript/link 均为 0/0，同时有 3 个上游 transcript 404（Episode not found）。没有窗口内可读 transcript，因此没有洞察卡；不能把本轮结果写成六个节目逐一无更新，也不能把 offered 0 当作完整 show coverage。证据等级固定为 `secondary-source` 聚合方 transcript，本轮没有单集 canonical link 或本地 transcript 路径。

- 状态与覆盖：[podcast-items.json](../raw/2026-09-25/podcast-items.json)、[manifest.json](../raw/2026-09-25/manifest.json)
- 上游快照：[feed-podcasts.json](../raw/2026-09-25/podcasts/follow-builders/feed-podcasts.json)
- transcript 路径：本轮无可读 transcript；3 个失败标题和错误保存在 `podcast-items.json` 的 `errors` 中。

## 3. 来源证据表

| 来源 | 类型与覆盖 | 原始记录 / 正文归档 | 证据等级与边界 |
| --- | --- | --- | --- |
| RSS/Atom | 32 来源：31 ok、1 failed；48 条匹配或必读正文尝试，45 ok、3 limited | [rss-items.json](../raw/2026-09-25/rss-items.json)；可读正文索引见 [report-reading-list.json](../raw/2026-09-25/report-reading-list.json) | 一手 OpenAI 条目使用 `opencli-read`；limited 条目只能作摘要/覆盖边界 |
| GitHub Releases | 7/7 Atom 成功、35 条；10 条一手正文 5 ok、5 limited | [github-items.json](../raw/2026-09-25/github-items.json)；[Claude Code v2.1.282 body](../raw/2026-09-25/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.282-cd3a2bc67e.atom.md) | Codex 当前窗口 alpha release 仅有 limited Atom 占位，不能推断功能 |
| GitHub Trending | 1/1 成功、10 个仓库；榜单描述 10/10、README 10/10 | [github-trending.json](../raw/2026-09-25/github-trending.json)；[README 归档目录](../raw/2026-09-25/github-trending-readmes/) | `secondary-source` 榜单快照与仓库自述；不表示目标日更新或质量背书 |
| 官方页面 | 4/5 成功；Anthropic Engineering 25 张卡片，目标日 article 0；OpenAI News limited | [official-pages.json](../raw/2026-09-25/official-pages.json)；[Anthropic index](../raw/2026-09-25/official-page-text/anthropic-engineering/anthropic-engineering-anthropic-engineering-9bba7c6d8f.index.html) | 页面索引不等于文章正文；OpenAI News challenge 未升级为可读事实 |
| twitterapi.io | 50 个账号 0 ok、50 failed，0 条 direct-x | [twitterapi-io-results.json](../raw/2026-09-25/twitterapi-io-results.json)；[主题摘要状态](../raw/2026-09-25/twitter-topic-brief.json) | 额度不足/TLS 失败导致覆盖失败，不代表没有推文；未使用 Exa、登录态浏览器或 X 写操作 |
| follow-builders | `status=partial`；offered 0、inside/outside/unknown 0；transcript/link 0/0；上游错误 3 | [podcast-items.json](../raw/2026-09-25/podcast-items.json)；[feed snapshot](../raw/2026-09-25/podcasts/follow-builders/feed-podcasts.json) | 聚合方 transcript 的 `secondary-source` 边界；本轮没有单集可读正文，不能声称完整 show coverage |
| 正文阅读清单 | 8 项：4 条 GitHub release、1 条 RSS、3 份 Trending README；5 项有正文、3 项为边界 | [report-reading-list.json](../raw/2026-09-25/report-reading-list.json) | 派生阅读控制，不替代 raw 原文；limited 项只作覆盖边界 |

## 4. X/Twitter 覆盖说明

本轮 `twitterapi.io` 请求 50 个已配置账号，成功 0、失败 50；绝大多数返回额度不足，`mattturck` 为 TLS 连接失败。`twitter-topic-brief` 为 partial，当前没有直接 X 证据。未使用 Exa、登录态浏览器、账号密码或任何发帖、点赞、关注、私信等写操作；不得把失败结果解释为“没有更新”。

## 5. 不确定性与待验证项

- `dwarkesh-patel` RSS 源失败；若后续命中关注方向，应按 runbook 的 OpenCLI fallback 重新抓取。
- RSS 匹配/一手必读共 48 条，只有 Gemini 3.8 Live 的目标窗口正文在本日报展开；3 条 limited（`huggingface-blog`、`forward-deployed`、`ted-mabrey` 各一条）只能作覆盖边界，其他旧条目仍保留在 raw 供去重与追溯。
- 3 条窗口内 OpenAI Codex alpha release 的 Atom body 为 `limited`；版本、时间和链接可确认，功能变化不可确认。
- OpenAI News 页面为 challenge/limited，OpenCLI fallback 也导航失败；Anthropic Engineering 只确认索引 25 张卡片，没有目标日 article 正文。
- GitHub Trending 是单次排名快照；`google/ax` README 明确仍可能有破坏性协议变化，`NVIDIA/Model-Optimizer` 的性能数据、Hindsight 的基准/生产自述、金融连接器、CLI 执行和 FxEmbed 的平台接口都需独立验证。
- twitterapi.io 额度不足/TLS 失败导致 50 个账号全部失败，当前无 direct-x，不能代表账号无更新。
- follow-builders `podcast-items.json` 为 `partial` 而非合法空 feed：offered 0、configured 0，但有 3 个上游 transcript 404；本轮无窗口内 transcript，不能推出六个节目逐一没有新集，也没有完整 show coverage。
- 本轮没有 inside-window podcast candidate，因此没有需要单独处置的 podcast candidate audit 行；上游错误标题和状态已保留在 [podcast-items.json](../raw/2026-09-25/podcast-items.json)。

## 6. 运行统计

- 新增 seen 记录：20；seen 总数：5,888。
- 信号索引：8 项，其中 5 项在目标窗口内（3 条 Codex limited、1 条 Claude Code 正文、1 条 Gemini 正文），3 项为发布时间 unknown 的 Trending README。
- 达到日报高信号标准：2 项（Claude Code `v2.1.282`、Gemini 3.8 Live with Live Avatar）。
- RSS/Atom：32 个来源，155 条 feed 记录，48 条匹配或必读正文尝试，45 ok、3 limited、1 个源失败。
- GitHub Releases：35 条；7/7 Atom 来源；一手正文 5 ok、5 limited。
- GitHub Trending：10 个仓库，10/10 榜单描述，10/10 README。
- 官方页面：5 个来源，4 ok、1 limited；Anthropic Engineering 索引 25 张卡片、目标日 article 0。
- 播客状态：`partial`；offered 0 / configured 0 / inside 0 / outside 0 / unknown 0；transcript ok 0 / limited 0；link ok 0 / limited 0；upstream errors 3。
- X/Twitter：0/50 成功、50/50 failed；不能解释为无更新。
- Candidate audit：初稿运行后写入覆盖/未覆盖计数；逐条状态与原文入口见 [Markdown](../reviews/2026-09-25-candidate-audit.md) 和 [JSON](../reviews/2026-09-25-candidate-audit.json)。

<!-- dsi-candidate-audit: covered=1 missed=11 -->

## 当天产物

- [manifest.json](../raw/2026-09-25/manifest.json)、[run-summary.json](../raw/2026-09-25/run-summary.json)、[signals.json](../raw/2026-09-25/signals.json)、[report-reading-list.json](../raw/2026-09-25/report-reading-list.json)。
- 播客覆盖工件：[podcast-items.json](../raw/2026-09-25/podcast-items.json)、[feed snapshot](../raw/2026-09-25/podcasts/follow-builders/feed-podcasts.json)；本轮无 transcript 文件。
- RSS / GitHub / 官方页面来源：[rss-items.json](../raw/2026-09-25/rss-items.json)、[github-items.json](../raw/2026-09-25/github-items.json)、[github-trending.json](../raw/2026-09-25/github-trending.json)、[official-pages.json](../raw/2026-09-25/official-pages.json)。
- X/Twitter 状态工件：[twitterapi-io-results.json](../raw/2026-09-25/twitterapi-io-results.json)、[twitter-topic-brief.json](../raw/2026-09-25/twitter-topic-brief.json)。
- 候选审计：[Markdown](../reviews/2026-09-25-candidate-audit.md)、[JSON](../reviews/2026-09-25-candidate-audit.json)。
