# 2026-07-28 每日源情报

## 直接答案

今天最值得跟进的是“模型能力进入真实工作流后，控制面和边界一起前移”：

1. OpenAI Codex `0.146.0-alpha.13` 确认有新发布，但 release Atom 正文只有 24 个字符，当前只能确认“发布存在”，不能从版本号推断功能。
2. `steipete` 报告 agent 发现 Bun 兼容性缺陷、另一 agent 当夜修复；随后归档的 Bun issue #36049 给出了可复现代码、根因和两个修复方向。这是今天最完整的“agent 产出工程证据”链路，但 issue 仍是待合并的官方问题记录，不等于修复已发布。
3. OpenAI 账号宣布 GPT-Live 已向 Edu、Business、Enterprise 计划全球可用；`gregisenberg` 把营销 agent 描述为“基于实时业务数据循环研究、执行、读结果、改进”。两者都是直接 X 证据：前者是产品可用性公告，后者是个人方案描述，不能直接推出普遍效果或市场规模。

## 0. 采集范围

- 运行日：北京时间 2026-07-28；稳定来源采用各源可提供的近期窗口，原始入口为 [`manifest.json`](../raw/2026-07-28/manifest.json)。
- RSS/Atom：32 个源中 31 个成功、1 个失败（`nabeel-qureshi` feed 解析错误）；155 条条目中 53 条命中或一手重点条目尝试全文，53/53 可读。失败不能解释为该源没有更新。
- GitHub release：7/7 个 Atom 源成功；10 条一手 release 全文中 4 条可读、6 条 `limited`。GitHub REST API 未启用，Atom 是本轮证据来源。
- GitHub Trending：1 个页面成功解析 10 个仓库，10/10 README 归档成功；全部是 `secondary-source` 发现信号，不是质量、采用或安全背书。
- 官方页面：4/4 成功；OpenAI News 页面使用 `opencli-read` 归档，其余页面主要作为发现列表。
- X/Twitter：`twitterapi.io` 处理 27 个账号，25 个成功、`karpathy` 与 `genspark_ai` 超时失败，保留 125 条 `direct-x`。主题摘要是最近约 36 小时上下文，不保证严格只含 7 月 28 日，也不代表账号没有发帖；未使用 Exa、登录态浏览器、官方 X API 或写操作。

## 1. 今日高信号

- **Codex 新版本但功能不可判读**：OpenAI Codex 的 [`0.146.0-alpha.13`](https://github.com/openai/codex/releases/tag/rust-v0.146.0-alpha.13) 在北京时间 00:08 发布，Atom 中的 release body 仅为“Release 0.146.0-alpha.13”，状态为 `official-source`、`limited`。正文归档见 [`github-release-fulltext`](../raw/2026-07-28/github-release-fulltext/openai-codex/)，下一步只能打开 release 页面补全文本，不能把版本号当作变更说明。
- **Agent 发现并推动修复 Bun 兼容性问题**：`steipete` 的 [原帖](https://x.com/steipete/status/2081767828278170002)（`direct-x`，7 月 27 日深夜，属于 24–36 小时上下文）称“我的 agent 报告 bug，另一个 agent 当夜修复”。它链接的 [`oven-sh/bun#36049`](http://github.com/oven-sh/bun/issues/36049) 已归档全文：`child_process.spawn` 错误处理 `encoding: "buffer"`，导致 execa/OpenClaw 调用抛 `ERR_UNKNOWN_ENCODING`；issue 标注由 Claude agent 生成并经人工复核。它证明的是发现、复现和提交问题的链路，不证明修复已经合入或发布。
- **GPT-Live 扩大到企业和教育计划**：OpenAI 账号宣布 [GPT-Live in ChatGPT Voice](https://x.com/OpenAI/status/2081794871795589485) 已向 Edu、Business、Enterprise 全球可用，证据等级 `direct-x`。本轮没有归档产品文档或独立可用性测试，不能补写具体能力、地区例外或性能承诺。
- **营销 agent 的循环式工作流成为产品线索**：`gregisenberg` 描述 [marketing agents](https://x.com/gregisenberg/status/2081814601851900221) 以实时业务数据为输入，循环进行研究、执行、读取结果和改进，属于 `direct-x` 的个人方案/推广信号。需要用真实系统日志、成本和转化数据验证，不能当作独立效果结论。
- **独立开发者的“对话式造应用”个案继续出现**：`levelsio` 描述非技术用户用 Claude/Codex 在本地生成并部署应用，[原帖](https://x.com/levelsio/status/2081454749237256564) 为 `direct-x`；`jackfriks` 也称使用 Claude 与 post bridge connector 发帖，[原帖](https://x.com/jackfriks/status/2081780537555910757) 只有短句。它们支持“入口成本下降”的观察，不支持普遍成功率、留存或替代率。
- **高收益/漏洞叙事降级为待核验线索**：`EXM7777` 称利用“系统漏洞”从 Claude Code 产生超过 25 万美元，[原帖](https://x.com/EXM7777/status/2081396624992219647) 是高分 `direct-x`，但没有可读教程、财务证明或复现材料；本日报不提供操作步骤，也不把它写成事实。

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

OpenAI RSS 的 [`How AI is expanding what people do at work`](../raw/2026-07-28/rss-fulltext/openai-blog/openai-blog-how-ai-is-expanding-what-people-do-at-work-f143efbfe2.opencli.md) 全文通过 `opencli-read` 归档，基于超过 80 万条美国 ChatGPT 用户消息提出“任务跨界”：16.8% 的工作相关消息、43.5% 的非通用职业特定消息涉及另一职业的任务。它发表于 7 月 27 日，是近期背景而非 7 月 28 日新发布；数据来自厂商研究，不能直接推出劳动市场因果。OpenAI Codex alpha13 的正文仍 `limited`。

Claude Code `v2.1.219` 的 [`release body`](../raw/2026-07-28/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.219-0be0b416a3.atom.md) 可读，包含 Claude Opus 5 默认模型与 1M 上下文、严格网络 allowlist、MCP 配置错误可见性、动态工作流大小指引、嵌套 subagent 转发和结构化 runner/session 失败分类；`v2.1.220` 只有 53 字、状态 `limited`。这些是 7 月 20–25 日的近期背景，不应伪装成今日新发布。

### LLM / Frontier Models

今日直接证据是 GPT-Live 的企业/教育可用性公告（`direct-x`）和 OpenAI 的“任务跨界”研究（官方全文、但非今日窗口）。`sama` 的 [“wrong”](https://x.com/sama/status/2081832600591892712) 没有上下文，标为 `indeterminate`，不作模型或产品判断。`Hesamation` 关于 Anthropic、开源和监管的长评论是立场性 `direct-x`，没有独立材料支持。

### AI Agent / Agentic Workflow

最完整的工程链是 Bun issue：agent 发现、复现并形成可审阅的问题记录；其中 [issue #36049](http://github.com/oven-sh/bun/issues/36049) 还说明 `spawnSync` 已对 `buffer` 特殊处理，而 `spawn` 路径不一致。营销 agent 的“研究—执行—反馈—改进”循环和 OpenAI 小企业帖子的“离工作边界最近的人直接处理问题”都只能作为方案/产品叙事，尚未有独立评测。

### AI Coding / Developer Tools

Codex alpha13 只确认发布存在、正文 `limited`；Claude Code v2.1.219 的后台 code review、MCP 错误可见性、网络 allowlist 与嵌套 subagent 能力是近期背景。Trending 中的 [`alibaba/open-code-review`](https://github.com/alibaba/open-code-review) README 描述“确定性流水线 + LLM agent”混合审查、逐行评论、规则匹配和低 token 消耗，但效果与“阿里内部识别大量缺陷”均是项目自述；需在目标代码库上复测精度、召回和数据边界。

### AI Governance / Public Legitimacy

本轮没有新的政策或监管原文。OpenAI 的小企业 direct-x 只说明其研究叙事，不能扩写成治理结论；Hesamation 的 Anthropic 评论是立场表达。最小验证路径是补充政策主体原文、监管文件或独立社会影响研究。

### AI Infrastructure / Open Source

RSS 与 release 采集到的高优先内容没有形成新的 infra 主题 direct-x；不能据此宣称“无基础设施更新”。GitHub Trending 的 [`opengeos/GeoLibre`](https://github.com/opengeos/GeoLibre) README 提供了可读的工程线索：Tauri v2、React/TypeScript、MapLibre GL JS、DuckDB-WASM Spatial 与 deck.gl 组合成浏览器、桌面、移动和 Jupyter 统一 GIS 工作区，并声称数据本地化；仍需自行验证部署、数据流和插件权限。

### Forward Deployed Engineering / Enterprise AI Deployment

当天 `twitter-topic-brief.json` 没有产出 `fde` 主题条目，这只是摘要路由结果，不是该方向无更新的证明。FDE/企业落地的最小验证仍应回到原始客户案例、数据接入、上线观测和反馈回流材料。

### Indie Hacking / Solo Founder 与 Product / Growth / GTM

`gregisenberg` 的营销 agent、`levelsio` 的非技术用户造应用，以及 `marclou` 转发的 [TrustMRR 991 家创业公司收入趋势](https://x.com/marclou/status/2081804323638698144)（称 AI 工具类收入下滑）共同构成分发与产品边界线索。后者是转发/自报数据，未独立核验；不把它们升级为市场规模、收入中位数或替代率结论。

### AI Systems / Automation

`steipete` 的 agent-to-agent Bun 修复链和营销 agent 循环是本日系统自动化信号。Trending 的 [`moeru-ai/airi`](https://github.com/moeru-ai/airi) README 描述可自托管的 AI 虚拟角色，支持实时语音、多端运行、游戏交互，并列出 RAG、memory、嵌入式数据库等子项目；README 另有“无官方代币”警告。它是项目自述，需验证模型调用、数据留存和第三方连接。

### X/Twitter 推主主题摘要

以下按 [`twitter-topic-brief.json`](../raw/2026-07-28/twitter-topic-brief.json) 选取每个有内容主题的高分条目。主题摘要使用最近约 36 小时上下文，同一 tweet 可重复归入多个主题；每条只证明账号通过 `twitterapi.io` 发布了相应内容，`direct-x` 不等于事实核验。

- **LLM / Frontier Models（43 条）**：`EXM7777` 的 [收益/漏洞叙事](https://x.com/EXM7777/status/2081396624992219647)、`Hesamation` 的 [Anthropic/开源评论](https://x.com/Hesamation/status/2081668231706611767)、`levelsio` 的 [Claude Cowork 造应用个案](https://x.com/levelsio/status/2081454749237256564)，均为 `direct-x`，前两项尤其需要外部证据。
- **AI Agent / Agentic Workflow（81 条）**：`EXM7777` 的 [工作流收益叙事](https://x.com/EXM7777/status/2081396624992219647)、`gregisenberg` 的 [marketing agent 循环](https://x.com/gregisenberg/status/2081814601851900221)、`steipete` 的 [agent 修复 Bun](https://x.com/steipete/status/2081767828278170002)，均为 `direct-x`；Bun 链接已叠加可读官方 issue。
- **AI Coding / Developer Tools（81 条）**：`EXM7777` 的 [收益叙事](https://x.com/EXM7777/status/2081396624992219647)、`levelsio` 的 [非技术用户造应用](https://x.com/levelsio/status/2081454749237256564)、`steipete` 的 [Bun 修复链](https://x.com/steipete/status/2081767828278170002)，均为 `direct-x`，不等于生产质量保证。
- **AI Governance / Public Legitimacy（3 条）**：`Hesamation` 的 [Anthropic/监管评论](https://x.com/Hesamation/status/2081668231706611767)、OpenAI 的 [GPT-Live 公告](https://x.com/OpenAI/status/2081794871795589485) 和 [小企业研究帖](https://x.com/OpenAI/status/2081833350323720219)，均为 `direct-x`；本主题没有政策原文。
- **Indie Hacking / Solo Founder（55 条）**：`gregisenberg` 的 [AI 吃掉独立软件的反向解读](https://x.com/gregisenberg/status/2081433961113481369)、`levelsio` 的 [进入门槛观察](https://x.com/levelsio/status/2081441046844657787)、[非技术用户造应用](https://x.com/levelsio/status/2081454749237256564)，均为 `direct-x` 个案。
- **Product / Growth / GTM（80 条）**：`EXM7777` 的 [收益叙事](https://x.com/EXM7777/status/2081396624992219647)、`gregisenberg` 的 [分发变化](https://x.com/gregisenberg/status/2081433961113481369)、`levelsio` 的 [进入门槛观察](https://x.com/levelsio/status/2081441046844657787)，均未提供独立收入或留存数据。
- **AI Systems / Automation（31 条）**：`EXM7777` 的 [while loop/graph 观点](https://x.com/EXM7777/status/2081440162316439809)、`steipete` 的 [agent 修复 Bun](https://x.com/steipete/status/2081767828278170002)、`gregisenberg` 的 [marketing agent](https://x.com/gregisenberg/status/2081814601851900221)，均为 `direct-x` 发现线索。
- `infra` 与 `fde` 在本次主题摘要没有条目；这是路由覆盖边界，不能解释为对应账号没有更新。

### GitHub Trending 每日发现

本轮解析 10/10 个 repo-card，10/10 README 通过 `curl` 归档；上榜只是今日发现信号。以下把 Trending description 与 README 能确认的项目机制合成说明：

- [`permissionlesstech/bitchat`](https://github.com/permissionlesstech/bitchat)：Swift 去中心化消息应用，用 Bluetooth mesh 做离线点对点通信，再以 Nostr relay 连接互联网；没有账号、手机号或中心服务器，并使用 Noise/私有信封加密。README 要求从 App Store 或可验证源码构建，并提醒设备标识和元数据边界；不能把 Trending 当作加密安全审计。
- [`amnezia-vpn/amnezia-client`](https://github.com/amnezia-vpn/amnezia-client)：桌面/移动端自托管 VPN 客户端，输入 IP、SSH 登录和密码后自动在服务器部署 Docker 容器；支持 OpenVPN、WireGuard、IKEv2、混淆协议和分流。涉及凭据、代理和绕过检测的安全边界，README 不是安全审计。
- [`moeru-ai/airi`](https://github.com/moeru-ai/airi)：可自托管的 AI 虚拟角色/陪伴体，README 描述实时语音、Minecraft/Factorio 交互和 Web/桌面/移动端，并列出 RAG、memory、嵌入式数据库与 Live2D 子项目。它是项目自述，需验证模型、数据留存、第三方连接和“无官方代币”警告。
- [`opengeos/GeoLibre`](https://github.com/opengeos/GeoLibre)：轻量云原生 GIS，把 Tauri v2、React/TypeScript、MapLibre GL JS、DuckDB-WASM Spatial 和 deck.gl 组合成浏览器、桌面、移动与 Jupyter 统一工作区；README 声称数据本地化，并提供 SQL、插件和嵌入能力。需要自行验证离线/云端数据流与插件权限。
- [`yorukot/superfile`](https://github.com/yorukot/superfile)：Go 终端文件管理器，README 覆盖 macOS/Linux/Windows 安装、插件、主题和快捷键；解决终端文件浏览与批量操作问题，但不是 AI 信号，安装脚本和插件仍需审阅。
- [`NanmiCoder/MediaCrawler`](https://github.com/NanmiCoder/MediaCrawler)：Python 多平台自媒体数据采集工具，支持小红书、抖音、快手、B 站、微博、贴吧、知乎；README 描述 Playwright 保留登录态、通过 JavaScript 获取签名、IP 代理池和评论抓取。项目同时明确学习用途和合规免责声明，涉及凭据、隐私、平台条款与法律风险，不能作为使用建议。
- [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable)：面向 AI coding agent 的前端设计技能，提供 1 个 skill、23 个命令、浏览器迭代和 60 条确定性检测规则；用 `npx impeccable install` 与 `/impeccable init` 接入项目。效果仍是项目自述，需用真实界面回归验证。
- [`shiyu-coder/Kronos`](https://github.com/shiyu-coder/Kronos)：面向金融 K 线的 decoder-only 基础模型，README 称用 45 个交易所数据、专用 tokenizer 和两阶段训练，可通过 Hugging Face 与微调/回测脚本使用。README 明确示例不是生产交易系统；数据漂移、交易成本和真实收益未验证。
- [`alibaba/open-code-review`](https://github.com/alibaba/open-code-review)：AI 代码审查 CLI，以确定性文件分组/规则匹配约束 LLM agent，输出逐行评论，也支持全文件扫描；兼容 OpenAI/Anthropic。项目关于内部规模、精度和低 token 消耗的说法需要在目标代码库复测，尤其要测召回、误报和源码外传边界。
- [`jenkinsci/jenkins`](https://github.com/jenkinsci/jenkins)：Java 自动化服务器，README 描述构建、测试、静态分析和部署，并拥有 2,000+ 插件及 Weekly/LTS 发布线；今天上榜只是成熟基础设施的热度，不是新版本发布或质量背书。

## 3. 来源证据表

| 来源组 | 本轮结果 | 代表证据与边界 |
| --- | --- | --- |
| RSS/Atom | 32 源，31 成功；命中/一手全文 53/53 可读 | 一手 OpenAI 全文见 [`rss-fulltext/openai-blog`](../raw/2026-07-28/rss-fulltext/openai-blog/)；`nabeel-qureshi` 失败，不能写成无更新。 |
| GitHub release | 7/7 Atom 成功；4 条一手全文可读、6 条受限 | Codex alpha13 与 Claude Code v2.1.220 的受限状态见 [`github-items.json`](../raw/2026-07-28/github-items.json)。 |
| GitHub Trending | 10/10 repo-card；10/10 README | 统一 `secondary-source`，字段见 [`github-trending.json`](../raw/2026-07-28/github-trending.json)。 |
| 官方页面 | 4/4 成功 | OpenAI News 的 `opencli-read` 归档见 [`official-page-text`](../raw/2026-07-28/official-page-text/)。 |
| X/Twitter | 27 个账号，25 成功、2 失败；125 条 `direct-x` | 结构化结果见 [`twitterapi-io-results.json`](../raw/2026-07-28/twitterapi-io-results.json)；主题聚合见 [`twitter-topic-brief.json`](../raw/2026-07-28/twitter-topic-brief.json)。 |

## 4. X/Twitter 覆盖说明

- 本轮 `twitterapi.io` 状态为 `partial`：`karpathy`、`genspark_ai` 请求在约 30 秒超时；这是失败覆盖，不能解释为两个账号没有更新。
- 采集接口使用最近约 24–36 小时窗口，默认 `includeReplies=false`；主题摘要中的部分高分条目来自 7 月 26 日或 7 月 27 日深夜，只作为上下文，不伪装成 7 月 28 日新事件。
- 所有 X/Twitter 相关内容均标记 `direct-x`。转发、短句、个人体验和高收益叙事只证明“账号发布了该说法”；只有 Bun issue 正文成功归档后，才叠加 `official-link-candidate`/官方正文边界，仍不等于修复合入。
- 没有使用 Exa MCP、登录态 X/Twitter 浏览器、账号密码、发帖、点赞、关注、私信或其它 action endpoint。

## 5. 候选审计与处置

<!-- dsi-candidate-audit: covered=13 missed=60 -->

初稿后由 [`candidate-audit.py`](../scripts/candidate-audit.py) 根据当天 raw 生成稳定 candidate id。高分但未逐条展开的 `direct-x`、RSS 命中条目和历史窗口条目保留在 [`candidate-audit.json`](../reviews/2026-07-28-candidate-audit.json)。其中 missed RSS 主要是 feed 最近条目的历史补抓（如 Gemini、Ruff、Claude Opus 5、FDE 和产品文章），不是 7 月 28 日新发布；missed direct-x 主要是转发、重复主题或低上下文短句。仍需留边界的高分例子包括 `marclou` 的 [TrustMRR 数据](https://x.com/marclou/status/2081666022223020540)、[Codex 提交 iOS app 个案](https://x.com/marclou/status/2081721767366967757)、`rileybrown` 的 [skills 成本观察](https://x.com/rileybrown/status/2081505696651034850) 和 `gregisenberg` 的 [AI 创业收购贴](https://x.com/gregisenberg/status/2081761054128816414)：它们只作为待核验线索，不被写成效果或市场结论。官方链接候选 Bun issue 已在“今日高信号”和主题摘要中给出 tweet 与正文链接，处置为“已读正文、保留待合并边界”。严格计数以 audit JSON 为准。

## 6. 不确定性与待验证项

- `nabeel-qureshi` feed 连续解析失败；最小验证是下一轮重试同一 URL，不能写成无更新。
- Codex alpha13 等 5 条 OpenAI release body 与 Claude Code v2.1.220 为 `limited`；最小验证是打开对应 release 页面补全文本，不从版本号推断功能。
- OpenAI “任务跨界”数据、Claude Code release、Bun issue 和所有 Trending README 各自有官方/项目自述边界；需要独立复测、客户侧基线、权限/沙箱检查和后续合并记录。
- MediaCrawler 的登录态、代理池和多平台抓取涉及隐私、凭据、合规和平台规则；Amnezia 涉及服务器密码与网络混淆；Kronos 涉及金融预测；本日报没有安装、登录、交易或远程暴露这些项目。
- X/Twitter 失败账号、空返回账号和未覆盖回复不构成“没有信号”证明；`infra`、`fde` 没有主题摘要条目也不构成对应方向无更新。

## 边界与验证

已确认：稳定来源 raw、X/Twitter 结构化结果、5 条可读正文、10 份 Trending README、日报草稿和候选审计均写入仓库；证据等级与失败边界已标注。未确认：受限 release body、失败 RSS 的实际更新、个人/厂商自述的外部效果、任何需要登录或动作权限的安全属性。剩余最小闭环是运行 candidate audit 与严格日报校验、构建 bundle、执行所有 enabled trend 的 marker/Phase 1/Phase 2/check，再用 dedicated main publisher 发布并单独发送 Gmail；在这些步骤完成前不把日报视为闭环。
