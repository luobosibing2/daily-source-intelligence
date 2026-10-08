# 2026-09-27 Daily Source Intelligence

> 本日报按北京时间目标日归档。GitHub Trending 是二手发现线索；项目机制只有在本轮 README 可读时才总结。follow-builders 播客 transcript 属于聚合方二手材料，不能替代节目音频或节目官方页面。

## 0. 采集范围

- 运行日期：2026-09-27，`Asia/Shanghai`；信号窗口为 2026-09-27 00:00 至 2026-09-28 00:00。统一入口按 `DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-09-27` 执行；网络使用系统/TUN 或已有代理路径。未使用 Exa、登录态 X/Twitter、账号密码或任何 X 写操作。
- 配置范围：RSS/Atom、GitHub Releases、GitHub Trending、官方页面、follow-builders 公共 transcript feed、`twitterapi.io`；关注方向来自 [config/watch.md](../config/watch.md) 和 [config/topics.yaml](../config/topics.yaml)。
- RSS/Atom：32 个来源中 31 个成功、1 个失败；49 条匹配或一手必读正文尝试中 47 条可读、2 条 `limited`，另有 106 条按主题过滤跳过。按北京时间目标窗口过滤，本轮没有匹配的 RSS/Atom 新条目；raw 中的可读历史条目保留供追溯，不能当作 9 月 27 日新信号。
- GitHub Releases：7/7 个 Atom 来源成功，共 35 条记录；10 条一手必读正文尝试中 5 条可读、5 条 `limited`。目标窗口内有 OpenAI Codex `0.159.0-alpha.5` 与 `0.159.0-alpha.6` 两条发布活动，但 Atom 正文只有版本短句，功能变化不可确认。
- GitHub Trending：1/1 来源成功，解析 10 个仓库；榜单描述 10/10、README 10/10 可读。榜单星数与 `stars_today` 是约 05:21 的单次快照，不证明目标日发布、代码变化、项目质量或厂商背书。
- 官方页面：4 个来源成功、1 个 `limited`。Anthropic Engineering 索引成功解析 25 张卡片，但目标窗口 article 数为 0；OpenAI News 返回 challenge/limited HTML 且 OpenCLI fallback 被拒；Claude Blog 与 Claude Docs 只有页面级 metadata，本轮没有目标日可读文章正文。
- 播客：[`podcast-items.json`](../raw/2026-09-27/podcast-items.json) 存在，状态为 `partial`。follow-builders 本轮 offered/configured/allowed/inside/outside/unknown=`1/1/1/0/1/0`，transcript ok/limited=`1/0`，link ok/limited=`0/1`，upstream errors=`1`。唯一允许单集是 No Priors 的 “Re-Founding Incumbents for the AI Era with Sequence Holdings Co-Founder and CEO Michael Lee”，发布时间为 2026-09-24 10:00 UTC（北京时间 9 月 24 日 18:00），在目标窗口外；transcript 虽可读，但不能进入本日报的当日洞察卡。另一个 OpenRouter 单集 transcript 返回 HTTP 404，已保留为上游错误。未运行 pod2txt、Supadata、音频下载或 ASR。
- X/Twitter：请求 50 个已配置账号，0 个成功、50 个失败；每个账号返回 `Credits is not enough.Please recharge`。没有 `direct-x` 证据，失败不等于账号没有更新。
- 原始归档入口：[`raw/2026-09-27/`](../raw/2026-09-27/)、[`manifest.json`](../raw/2026-09-27/manifest.json)、[`run-summary.json`](../raw/2026-09-27/run-summary.json)、[`report-reading-list.json`](../raw/2026-09-27/report-reading-list.json)。

## 1. 今日高信号

- **OpenAI Codex 在目标窗口连续出现两个 alpha 版本。** `0.159.0-alpha.5`（北京时间 01:42）与 `0.159.0-alpha.6`（04:19）均来自 OpenAI Codex GitHub Releases，证据等级为 `official-source`。两个 release Atom body 都只有版本短句（`limited`），因此今天只能确认发布活动、时间和链接，不能从版本号推断功能、稳定性或 breaking change。[alpha.5](https://github.com/openai/codex/releases/tag/rust-v0.159.0-alpha.5) · [alpha.6](https://github.com/openai/codex/releases/tag/rust-v0.159.0-alpha.6) · [本地 release 归档](../raw/2026-09-27/github-release-fulltext/openai-codex/)。
- **Agent 控制面与长期记忆仍是 Trending 的强发现线索。** `paperclipai/paperclip`（今日 +2,589 stars）把多 agent 协作包装为带组织结构、预算、审批、心跳和审计的控制面；`vectorize-io/hindsight`（今日 +2,152 stars）把记忆拆成 retain/recall/reflect、事实、经验、观察和 mental models。两者的机制可由本轮 README 确认，但热榜本身是 `secondary-source` 快照，不代表采用率、生产成熟度或独立 benchmark 结论。[Paperclip README](../raw/2026-09-27/github-trending-readmes/paperclipai__paperclip.md) · [Hindsight README](../raw/2026-09-27/github-trending-readmes/vectorize-io__hindsight.md)。

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

**OpenAI Codex alpha：** 目标窗口内仅确认 `0.159.0-alpha.5` 和 `0.159.0-alpha.6` 两次发布。对应 Atom 全文分别只有短句 `Release 0.159.0-alpha.5` 与 `Release 0.159.0-alpha.6`，被标为 `fulltext_status=limited`；不能把版本号写成具体功能或质量变化。[`github-items.json`](../raw/2026-09-27/github-items.json) · [alpha.5 Atom 归档](../raw/2026-09-27/github-release-fulltext/openai-codex/openai-codex-0.159.0-alpha.5-72017f696f.atom.md) · [alpha.6 Atom 归档](../raw/2026-09-27/github-release-fulltext/openai-codex/openai-codex-0.159.0-alpha.6-90a8cbc1a5.atom.md)。

**Anthropic：** Engineering 索引可读并解析出 25 张卡片，但目标窗口 article 为 0；这只能支持“本轮索引检查完成、没有目标日 article”的边界。Claude Blog 页面显示近几日文章卡片，但没有目标日正文进入阅读清单，不能仅凭标题下结论。[`official-pages.json`](../raw/2026-09-27/official-pages.json) · [Anthropic Engineering index](../raw/2026-09-27/official-page-text/anthropic-engineering/anthropic-engineering-anthropic-engineering-9bba7c6d8f.index.html)。

### 模型、代理与工程效率

本轮没有目标日 RSS 正文新信号；以下结论来自 GitHub Trending README，证据等级固定为 `secondary-source`：

- **Paperclip** 是 Node.js server + React UI 的多 agent 组织控制面。README 明确写到目标、组织结构、角色和权限、预算、审批、心跳、工作区、MCP/插件、成本记录和不可变审计；它把“管理 pull request”上移为“管理业务目标”。这些是仓库自述，尚未做运行时验证。
- **Hindsight** 面向“会学习而不只是回忆”的 agent memory，提供 server、Python/Node.js/Go/CLI/REST 客户端和 MCP；核心操作是 `retain`、`recall`、`reflect`，并区分事实、经验、观察、mental models 与 knowledge pages。README 的 LongMemEval 性能宣称是项目方材料，不能当成独立评测结论。
- **Univer** 把表格、文档、演示、看板、关系表和 PDF 组合为可嵌入的 Office SDK；README 描述 plugin-first、浏览器/Node.js 同构、Facade API、Canvas 渲染，并为 agent 提供结构化编辑、结果检查、截图/布局诊断和隔离草稿流程。适合作为“agent 操作办公文档”的工程候选，不等于已经具备生产级权限隔离。[Univer README](../raw/2026-09-27/github-trending-readmes/dream-num__univer.md)
- **From the creator of Agent Memory / AI Engineering from Scratch** 是一套长课程型仓库。README 自述包含 523 lessons、20 phases、约 342 小时，覆盖 Python、TypeScript、Rust、Julia；每课产出 prompt、skill、agent 或 MCP 等可复用 artifact。课程规模与读者统计均为 README 自报，不代表学习效果。[课程 README](../raw/2026-09-27/github-trending-readmes/rohitg00__ai-engineering-from-scratch.md)

### AI 基础设施 / 开源组件

- **NVIDIA Model Optimizer** 提供量化、剪枝、NAS、蒸馏、稀疏化和 speculative decoding，输入支持 Hugging Face、PyTorch、ONNX，输出可部署到 TensorRT-LLM、TensorRT、vLLM、SGLang。README 还列出 NVFP4/W4A4 示例与吞吐/模型体积改善数字；这些数字需要按官方 benchmark 和具体硬件复核。[README](../raw/2026-09-27/github-trending-readmes/NVIDIA__Model-Optimizer.md)
- **TensorFlow** 是成熟的端到端机器学习平台，README 明确提供 Python/C++ API、pip 与 CPU/GPU 安装路径、源码构建与测试指引。它今天上榜更适合作为基础设施发现线索，而不是新的发布日期或能力变化。[README](../raw/2026-09-27/github-trending-readmes/tensorflow__tensorflow.md)
- **OpenBao** 是社区治理的开源 secrets/certificates/keys 管理系统。README 描述加密存储、动态凭据、租约续期、撤销和 transit encryption，并支持磁盘、PostgreSQL 等后端；涉及密钥和生产权限，必须先看正式文档、版本和部署配置，不能因上榜就直接接入。[README](../raw/2026-09-27/github-trending-readmes/openbao__openbao.md)
- **Visual Studio Code / Code - OSS** 是 Microsoft 与社区共同开发的开源代码编辑器仓库，README 区分 MIT 许可的 Code - OSS 与带 Microsoft 定制的 VS Code 产品，并保留 roadmap、monthly iteration 与 endgame 计划。今天的榜单位置不是新版本证据。[README](../raw/2026-09-27/github-trending-readmes/microsoft__vscode.md)

### 安全、治理与协作边界

- **Buzz** 是 Block 的 Rust/Nostr relay 工作区：人、agent、workflow、Git 事件和项目记忆在同一 relay 中以签名事件、审计链和可搜索记录协作；README 还描述 `buzz-cli`、ACP/MCP、分支变房间、CI/审批和自托管部署。项目明确写着“Not finished”，因此只能视作架构线索；Nostr 身份、relay 运维、密钥和多租户边界都需独立验证。[README](../raw/2026-09-27/github-trending-readmes/block__buzz.md)
- **reverse-skill** 是面向 APK/ELF/JS/PCAP/CTF/授权渗透测试的技能路由包，README 的流程先过 `RULES.md`、scope/auth gate 和 `case-init`，再按场景选择 jadx、Frida、IDA、Burp 等工具，并保留时间线、证据链和报告。它只适用于明确授权的目标；本日报没有运行其中任何工具，也不把其自述的回归数量、工具链或 sponsor 信息当作安全保证。[README](../raw/2026-09-27/github-trending-readmes/zhaoxuya520__reverse-skill.md)

### GitHub Trending / Daily Repos

本轮 10/10 项目均取得榜单描述与 README；以下是把两者合并后的读者向摘要。星数为单次快照，所有条目均为 `secondary-source` discovery signal：

- [paperclipai/paperclip](https://github.com/paperclipai/paperclip)（87,035 stars，今日 +2,589，TypeScript）：Node.js + React 的 agent 组织控制面；README 描述目标、org chart、预算、审批、心跳、插件、工作区和审计，把多种 agent 运行时放进同一家公司式治理模型。下一步应验证权限模型、预算 hard-stop、持久化状态和真实 adapter 行为。[README](../raw/2026-09-27/github-trending-readmes/paperclipai__paperclip.md)
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)（32,002，今日 +2,152，Python）：长期记忆服务，提供 server/SDK/MCP 与 `retain`/`recall`/`reflect`，并区分事实、经验、观察和 mental models；README 声称在 LongMemEval 上表现领先，但仍需独立复测延迟、成本、删除和隔离语义。[README](../raw/2026-09-27/github-trending-readmes/vectorize-io__hindsight.md)
- [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer)（4,709，今日 +354，Python）：把量化、剪枝、蒸馏、NAS、稀疏化和 speculative decoding 组合成可导出 checkpoint，并对接 TensorRT-LLM、TensorRT、vLLM、SGLang；实际收益依赖模型、硬件和 benchmark 设定。[README](../raw/2026-09-27/github-trending-readmes/NVIDIA__Model-Optimizer.md)
- [dream-num/univer](https://github.com/dream-num/univer)（19,155，今日 +845，TypeScript）：可嵌入的 Office SDK，覆盖表格、文档、演示、看板和关系表；plugin-first、Facade API、Canvas 渲染与浏览器/Node.js 同构让 agent 可以通过结构化 API 修改内容，再用渲染/布局诊断做结果检查。[README](../raw/2026-09-27/github-trending-readmes/dream-num__univer.md)
- [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow)（200,423，今日 +31，C++）：端到端机器学习平台，提供 Python/C++ API、pip/CPU/GPU 安装、源码构建和测试；今天的上榜只说明快照热度，不表示新发布或新 benchmark。[README](../raw/2026-09-27/github-trending-readmes/tensorflow__tensorflow.md)
- [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)（58,287，今日 +828，Python）：以大量 lesson、phase 和可复用 prompt/skill/agent/MCP artifact 组织 AI 工程学习路径；课程数量、时长和读者数是 README 自报，适合当教育资源候选，不等价于课程质量验证。[README](../raw/2026-09-27/github-trending-readmes/rohitg00__ai-engineering-from-scratch.md)
- [openbao/openbao](https://github.com/openbao/openbao)（7,969，今日 +360，Go）：社区治理的 secrets、证书与密钥服务，提供加密存储、动态 secrets、租约和撤销；生产使用前必须核对后端、密钥轮换、审计和升级策略。[README](../raw/2026-09-27/github-trending-readmes/openbao__openbao.md)
- [block/buzz](https://github.com/block/buzz)（34,797，今日 +367，Rust）：自托管的人机协作 workspace，relay 以 Nostr 签名事件承载消息、workflow、Git、审核和审计，并提供 agent-first CLI 与 ACP/MCP 表面；README 明确项目未完成，不能直接视为生产系统。[README](../raw/2026-09-27/github-trending-readmes/block__buzz.md)
- [microsoft/vscode](https://github.com/microsoft/vscode)（193,055，今日 +78，TypeScript）：Code - OSS 的开发仓库，覆盖代码编辑、导航、调试、扩展、roadmap 和迭代计划；榜单位置不是版本发布证据。[README](../raw/2026-09-27/github-trending-readmes/microsoft__vscode.md)
- [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)（37,949，今日 +409，PowerShell）：为授权逆向、渗透测试和安全研究按目标类型路由方法、工具和证据报告；scope/auth gate 是其关键边界，未经明确授权不得对任何目标执行扫描、利用或数据获取。[README](../raw/2026-09-27/github-trending-readmes/zhaoxuya520__reverse-skill.md)

### X/Twitter 推主主题摘要

本轮没有可归入主题的推文：[`twitter-topic-brief.json`](../raw/2026-09-27/twitter-topic-brief.json) 为 `partial`，50 个账号成功 0、失败 50、tweet 数 0。全部账号均报 `Credits is not enough.Please recharge`；空结果不是账号无更新的证据。

### 播客 / 长对话

follow-builders 工件为 `partial`，不是合法空 feed：中央 feed 实际 offered 1 集、允许节目 1 个、窗口内 0 集、窗口外 1 集、未知 0 集；transcript 1/1 可读，canonical link 0/1（`link_status=limited`），上游错误 1。唯一归档单集是 No Priors 的 [Re-Founding Incumbents for the AI Era with Sequence Holdings Co-Founder and CEO Michael Lee](https://www.youtube.com/@NoPriorsPodcast)，GUID 为 `e2eb4b88-b7c1-11f1-a5c5-4b2557d321bc`，发布时间在目标窗口外；聚合 transcript 位于 [本地 transcript](../raw/2026-09-27/podcasts/follow-builders/transcripts/re-founding-incumbents-for-the-ai-era-with-sequence-holdings-co-founder-and-ceo-8ab8e2776d59.md)，feed snapshot 位于 [feed-podcasts.json](../raw/2026-09-27/podcasts/follow-builders/feed-podcasts.json)。由于没有 inside-window transcript，本轮不写洞察卡、不把节目观点升级为当日事实；证据等级仍固定为 `secondary-source`，且 canonical 单集链接未由 RSS GUID 精确修复。另一个 OpenRouter 单集返回 HTTP 404，已在 [`podcast-items.json`](../raw/2026-09-27/podcast-items.json) 的 `errors` 中保留。

## 3. 来源证据表

| 来源 | 类型与覆盖 | 原始记录 / 正文归档 | 证据等级与边界 |
| --- | --- | --- | --- |
| RSS/Atom | 32 来源：31 ok、1 failed；49 条匹配/一手必读正文，47 ok、2 limited；目标窗口匹配新条目 0 | [`rss-items.json`](../raw/2026-09-27/rss-items.json)；正文索引见 [`report-reading-list.json`](../raw/2026-09-27/report-reading-list.json) | 一手源仍需按发布时间落入目标窗口；历史正文不升级为今日新信号 |
| GitHub Releases | 7/7 Atom 成功、35 条；10 条一手正文 5 ok、5 limited；目标窗口 2 条 Codex alpha | [`github-items.json`](../raw/2026-09-27/github-items.json)；[release body 归档目录](../raw/2026-09-27/github-release-fulltext/) | `official-source`；两条目标日 Atom body 只有版本短句 |
| GitHub Trending | 1/1 成功、10 个仓库；榜单描述 10/10、README 10/10 | [`github-trending.json`](../raw/2026-09-27/github-trending.json)；[README 归档目录](../raw/2026-09-27/github-trending-readmes/) | `secondary-source` discovery snapshot，不代表发布、质量或采用率 |
| 官方页面 | 4 ok、1 limited；Anthropic Engineering 索引 25 卡片、目标日 article 0；OpenAI News challenge | [`official-pages.json`](../raw/2026-09-27/official-pages.json)；[Anthropic index](../raw/2026-09-27/official-page-text/anthropic-engineering/anthropic-engineering-anthropic-engineering-9bba7c6d8f.index.html) | index/metadata 不等于 article 正文；limited 只作覆盖边界 |
| `twitterapi.io` | 50 个账号 0 ok、50 failed；0 条 direct-x | [`twitterapi-io-results.json`](../raw/2026-09-27/twitterapi-io-results.json)；[`twitter-topic-brief.json`](../raw/2026-09-27/twitter-topic-brief.json) | 额度不足导致失败，不代表无更新；未使用 Exa 或登录态浏览器 |
| follow-builders | `partial`；offered/configured/allowed/inside/outside/unknown=`1/1/1/0/1/0`；transcript ok/limited=`1/0`；link ok/limited=`0/1`；upstream errors=`1` | [`podcast-items.json`](../raw/2026-09-27/podcast-items.json)；[feed snapshot](../raw/2026-09-27/podcasts/follow-builders/feed-podcasts.json)；[transcript](../raw/2026-09-27/podcasts/follow-builders/transcripts/re-founding-incumbents-for-the-ai-era-with-sequence-holdings-co-founder-and-ceo-8ab8e2776d59.md) | 聚合 transcript `secondary-source`；单集窗口外且 canonical link limited |
| 正文阅读清单 | 5 项：2 条 Codex release limited、3 个 Trending README 可读 | [`report-reading-list.json`](../raw/2026-09-27/report-reading-list.json) | 派生阅读控制，不替代 raw 原文；limited 项只能写边界 |

## 4. X/Twitter 覆盖说明

本轮 `twitterapi.io` 请求 50 个已配置账号，成功 0、失败 50，全部返回 `Credits is not enough.Please recharge`。`twitter-topic-brief` 为 `partial`，当前没有直接 X 证据；不得把失败结果解释为“没有更新”。未使用 Exa、登录态浏览器、账号密码或任何发帖、点赞、关注、私信等写操作。

## 5. 不确定性与待验证项

- 目标日 RSS/Atom 没有匹配新条目；raw 中 49 条匹配/一手必读正文主要是历史窗口材料，不能借其可读状态制造目标日信号。
- 两条 Codex alpha release 的时间、版本和链接可确认，但 Atom body 仅 23 字符左右；不得从版本号推断功能、稳定性、兼容性或 breaking change。若要判断变化，下一步应取得对应 GitHub release body 或 changelog 的可读正文。
- `dwarkesh-patel` RSS 源失败；OpenAI News 是 limited/challenge，OpenCLI fallback 也被导航拒绝。Anthropic Engineering 仅确认索引卡片，没有目标日 article 正文；Claude Blog/Docs 页面 metadata 不能代替全文。
- GitHub Trending 的 10 个 README 本轮均可读，但榜单是二手快照。Paperclip、Hindsight、Univer、Buzz、OpenBao 和 reverse-skill 的权限、成本、数据隔离、部署安全或生产成熟度均未做运行时验证；reverse-skill 涉及逆向/渗透工具，必须先确认书面授权与隔离环境。
- `twitterapi.io` 额度不足导致 50 个账号全部失败，当前无 `direct-x`，不能代表账号没有更新；没有用 Exa 或登录态浏览器补漏。
- follow-builders 只反映中央 feed 本轮 offered 的内容，不承诺六个节目的完整覆盖。唯一允许单集在窗口外、canonical link limited；另有一个 transcript HTTP 404。没有 inside-window podcast candidate，故无播客候选需要进入正文审计，但工件与错误已保留。
- 候选审计中保留的 11 条 matched-RSS 行均为早于目标窗口的历史条目（其中 1 条正文 limited）；本轮逐条以 `outside_window` 处置并保留来源，不把它们伪装成当日新信号。
- 不把任何 README 自报 benchmark、star 增长、客户案例数字或项目宣传语写成独立实验、行业共识或官方保证。

## 6. 运行统计

- 新增 seen 记录：9；seen 总数：5,915。流程索引与状态见 [`run-summary.json`](../raw/2026-09-27/run-summary.json) 和 [`manifest.json`](../raw/2026-09-27/manifest.json)。
- 信号索引：5 项，其中 2 项落在目标窗口（Codex alpha.5/alpha.6），3 项为发布时间 unknown 的 Trending README 边界；详见 [`signals.json`](../raw/2026-09-27/signals.json)。
- 今日高信号：1 组官方发布活动（两条 Codex alpha）与 1 组二手发现线索（Paperclip/Hindsight）；均已明确正文或来源边界。
- RSS/Atom：32 来源，31 ok、1 failed；49 条匹配/一手必读正文 47 ok、2 limited。
- GitHub Releases：7/7 Atom，35 条；一手正文 5 ok、5 limited。
- GitHub Trending：10 个仓库，10/10 榜单描述，10/10 README。
- 官方页面：4 ok、1 limited；Anthropic Engineering 索引 25 张卡片、目标日 article 0。
- 播客：`partial`；offered 1 / configured 1 / allowed 1 / inside 0 / outside 1 / unknown 0；transcript ok 1 / limited 0；link ok 0 / limited 1；upstream errors 1。
- X/Twitter：0/50 成功、50/50 failed；不能解释为无更新。
- Candidate audit：11 条历史 matched-RSS 候选均为 `outside_window`，当前 covered=0、missed=11；审计明细见 [Markdown](../reviews/2026-09-27-candidate-audit.md) 和 [JSON](../reviews/2026-09-27-candidate-audit.json)。

<!-- dsi-candidate-audit: covered=0 missed=11 -->

## 7. 当天产物

- [`manifest.json`](../raw/2026-09-27/manifest.json)、[`run-summary.json`](../raw/2026-09-27/run-summary.json)、[`signals.json`](../raw/2026-09-27/signals.json)、[`report-reading-list.json`](../raw/2026-09-27/report-reading-list.json)。
- 播客覆盖工件：[`podcast-items.json`](../raw/2026-09-27/podcast-items.json)、[feed snapshot](../raw/2026-09-27/podcasts/follow-builders/feed-podcasts.json)、[本地 transcript](../raw/2026-09-27/podcasts/follow-builders/transcripts/re-founding-incumbents-for-the-ai-era-with-sequence-holdings-co-founder-and-ceo-8ab8e2776d59.md)。
- RSS / GitHub / 官方页面来源：[`rss-items.json`](../raw/2026-09-27/rss-items.json)、[`github-items.json`](../raw/2026-09-27/github-items.json)、[`github-trending.json`](../raw/2026-09-27/github-trending.json)、[`official-pages.json`](../raw/2026-09-27/official-pages.json)、[`official-link-candidates.json`](../raw/2026-09-27/official-link-candidates.json)。
- X/Twitter 状态工件：[`twitterapi-io-results.json`](../raw/2026-09-27/twitterapi-io-results.json)、[`twitter-topic-brief.json`](../raw/2026-09-27/twitter-topic-brief.json)。
- 候选审计：[`2026-09-27-candidate-audit.md`](../reviews/2026-09-27-candidate-audit.md)、[`2026-09-27-candidate-audit.json`](../reviews/2026-09-27-candidate-audit.json)；11 条历史 RSS 候选均有 `outside_window` disposition。
- 本日报写作依据：[`report-reading-list.json`](../raw/2026-09-27/report-reading-list.json) 及其列出的本地正文；未生成 `translations/2026-09-27/`。

## 边界与验证

- 本文把 `official-source`、`secondary-source`、`limited`、窗口外和失败状态分开记录；后续候选审计、strict report validation、日期 bundle、trend marker/Phase 1/Phase 2、trend check、`dsi.py check` 和 main 发布状态以对应产物与命令输出为准。
