# 2026-05-15 Daily Source Intelligence

## 采集范围

- 运行时间：2026-05-15 Asia/Shanghai，本轮按 `RUN_DATE=2026-05-15` 写入当天 raw 目录。
- 稳定来源：RSS/Atom 31 个源，31 个成功；GitHub releases 6 个源，6 个通过 Atom feed 成功；GitHub Trending 1 个源成功，解析 10 个每日热门 repo；official pages 4 个源，2 个成功、2 个 limited、0 个 failed。
- X/Twitter：通过 `twitterapi.io` read endpoint 成功读取 credential，顶层状态 `ok`；26 个账号均返回 `ok`，保留 145 条 direct-x 原始条目。
- 状态更新：[`../raw/2026-05-15/manifest.json`](../raw/2026-05-15/manifest.json)、[`../state/source-health.json`](../state/source-health.json)、[`../state/seen.json`](../state/seen.json) 已由 `update-state.py` 更新；本轮 `seen_added=46`，累计 675 条。
- 本次没有使用 Exa MCP、登录态浏览器、X/Twitter 账号凭证、写操作 endpoint、posting、liking、following 或 DM。
- 本地归档：
  - [`../raw/2026-05-15/rss-items.json`](../raw/2026-05-15/rss-items.json)
  - [`../raw/2026-05-15/github-items.json`](../raw/2026-05-15/github-items.json)
  - [`../raw/2026-05-15/github-trending.json`](../raw/2026-05-15/github-trending.json)
  - [`../raw/2026-05-15/github-trending-readmes/`](../raw/2026-05-15/github-trending-readmes/)
  - [`../raw/2026-05-15/official-pages.json`](../raw/2026-05-15/official-pages.json)
  - [`../raw/2026-05-15/twitterapi-io-results.json`](../raw/2026-05-15/twitterapi-io-results.json)

## 今日高信号

1. OpenAI Blog RSS 新增 `Work with Codex from anywhere`，并且 `@OpenAI` direct-x 同步宣布 Codex in ChatGPT mobile app preview。它把 Codex 从本机桌面任务推进到移动端监控、steer 和 approve 的跨设备工作流，但具体功能边界仍以官方文档为准。【有明确证据支撑 / official-source + direct-x】
2. OpenAI Blog RSS 新增 `Building a safe, effective sandbox to enable Codex on Windows`。这不是普通产品文案，而是 Codex 在 Windows/enterprise developer environment 中运行所需的 isolation 机制信号，和 coding-agent 安全落地直接相关。【有明确证据支撑 / official-source】
3. OpenAI Blog RSS 新增 `Our response to the TanStack npm supply chain attack`。它把 AI/coding-tool 生态的供应链风险拉回到包管理、token、CI/CD 与维护者安全这一层；对 agent 自动改代码/自动装包的边界很有提示价值。【有明确证据支撑 / official-source】
4. Hugging Face Blog 新增 `Unlocking asynchronicity in continuous batching`。这是 inference serving 的工程信号：连续 batching 不只是吞吐优化，还会影响长请求、异步调度和多用户负载下的延迟/资源权衡。【有明确证据支撑 / official-source】
5. a16z `From "System of Record" to "System of Intelligence"` 已补全文阅读，OpenAI Codex Windows sandbox / TanStack supply-chain response 已补官方可读抽取；它们共同把 FDE 观察从“岗位回温”推进到 enterprise intelligence layer、OS-level sandbox 和 developer supply-chain controls。【有明确证据支撑 / official-source + secondary-source】
6. GitHub Trending Daily 中 `rohitg00/agentmemory`、`obra/superpowers`、`K-Dense-AI/scientific-agent-skills` 同日上榜。共同点是把 agent 长期能力做成外部 memory server、可安装 methodology/skills 和专业领域技能包，而不是只靠一次 prompt。【有明确证据支撑 / secondary-source】
7. GitHub Trending Daily 中 `shiyu-coder/Kronos` 上榜，README 把它定位为金融 K-line/candlestick 的 foundation model，并给出 tokenizer、decoder-only model 和 forecasting 使用路径。这是 Financial Agents 的高风险 discovery signal，需要严格区分研究模型、预测 demo 和可交易系统。【有明确证据支撑 / secondary-source】
8. `@sama` direct-x 提到 Codex 企业试用优惠，并讨论 `price/speed` 相对 `price/intelligence` 的权衡。这是 Codex go-to-market 和 model UX tradeoff 的 direct-x 线索，但不是正式产品规格。【有明确证据支撑 / direct-x】
9. `@AnthropicAI` direct-x 宣布与 Gates Foundation 合作，投入 grants、Claude credits 和 technical support 到 global health、life sciences、education、agriculture、economic mobility。这是 philanthropic/sector deployment 线索，需等官方长文确认项目治理和交付边界。【有明确证据支撑 / direct-x】

## 按主题分组摘要

### LLM / Frontier Models

- OpenAI 今天的新增 RSS 重点偏工程落地：Codex mobile preview、Windows sandbox 与 TanStack npm supply-chain response 分别覆盖跨设备 agent 操作、OS-level isolation 和 developer supply-chain controls。
- Hugging Face `continuous_async` 是 serving 层信号，和 agent runtime 的并发、多租户、长请求调度有关；它不是模型发布，但会影响 LLM 应用的实际成本和延迟。
- Google DeepMind RSS 仍保留 `AlphaEvolve`、AI co-clinician、distributed training 等近期条目；本轮没有新增到高信号，因为今天更强的变化来自 OpenAI/Hugging Face/FDE/Trending。

### AI Agent / Agentic Workflow

- `agentmemory` 继续是 Memory & Dream 的强 discovery signal：README 说它支持 Claude Code、Cursor、Gemini CLI、Codex CLI、OpenCode 和任意 MCP client，并通过 hooks、MCP 或 REST API 共享同一个 memory server。
- `obra/superpowers` 把 software development methodology 做成 agent skills/插件，README 描述从需求澄清、spec、implementation plan 到 subagent-driven-development 的流程。它的价值是把 agent 工作流状态“安装”到 harness 里；边界是 README 不能证明流程一定被强制执行。
- `K-Dense-AI/scientific-agent-skills` 把 135 个 scientific/research skills、100+ databases、优化 Python package skills 和多步科研 workflow 包装给 Cursor、Claude Code、Codex 等 agent。它说明 skills 正从 coding best practices 扩展到垂直专业工作流。
- `OpenHuman` 再次上榜，继续代表 personal-agent connector、后台思考、长期记忆和本地 vault 方向；今天不重复扩写旧结论，只记录持续热度。

### AI Coding / Developer Tools

- OpenAI Codex release Atom feed 今天可见 `0.131.0-alpha.18`、`rust-v0.131.0-alpha.17`、`.16`、`.15`、`.14`；Atom 摘要不足以判断用户可见变化，需后续打开 release body 或 diff。
- LangChain releases 仍可见 `langchain==1.3.0`、`langchain-core==1.4.0`；LlamaIndex releases 新增到 `v0.14.22`；vLLM releases 继续有近期 RC surface。日报只记录 release surface，不从 Atom 摘要推断 breaking change。
- `@sama` direct-x 的 Codex 试用优惠、`@OpenAI` 的 mobile preview 和 “Another reason to switch to Codex” 是 go-to-market / workflow 线索；它们证明今天 X 侧 Codex 传播活跃，但不能替代正式 pricing、terms 或 product docs。

### Forward Deployed Engineering / Enterprise AI

- `The Pulse: Forward deployed engineering heats up again` 明确把 FDE 放回工程组织/市场讨论里；这是 FDE trend 的新增强信号，但当前只有 RSS 摘要，不能直接断言具体 operating model。
- a16z `System of Record` 到 `System of Intelligence` 已补全文阅读：它把 CRM/database 降为 intelligence layer 的输入之一，强调 agent/orchestration layer 会跨 CRM、calendar、inbox、call recording、Slack、billing、product telemetry 拉上下文、写回数据并处理权限/合规/企业 IT 环境。
- OpenAI Codex Windows sandbox 与 TanStack supply-chain response 也属于 enterprise deployment 的底层条件：如果 coding agent 要进入受控开发环境，OS-level sandbox、网络隔离、workspace 写权限、dependency provenance、credential rotation、code-signing 和 CI/CD guardrail 会比 demo 能力更重要。

### Financial Agents

- `shiyu-coder/Kronos` 是今天 financial-agents 的新增 high-risk discovery signal。README 把 Kronos 描述为金融 candlesticks/K-lines 的 decoder-only foundation model，使用 tokenizer 量化 OHLCV 数据，并提供预测 demo 和 Hugging Face model zoo。
- 这条信号不能写成“可用于交易”。更稳妥的解释是：金融 agent/模型正在从 analyst workflow 扩展到 market-sequence foundation model；但预测质量、交易适用性、风险控制、数据泄漏、回测边界和合规都需要更高证据。
- `@cnyzgkc` direct-x 出现基金收益、awesome-mac 等内容，但与 Financial Agents 主线弱相关；不提升为高信号。

### Product / Growth / Indie Founder

- direct-x 中 `rileybrown` 提到 agent-native apps、SaaS “plug-in or die” 和 Codex/Claude Code/Cursor 连接到视频编辑器这类 super app 设想。这些是产品方向线索，不是技术事实。
- `EXM7777` 讨论 AI 内容写作的“screen time / taste / rewrite”经验，`kloss_xyz` 讨论 AI 与个人创作/品味的边界；它们适合作为 product/content craft 观察，不进入技术高信号。
- `genspark_ai` 宣传 Boston/NYC Roast Nights，属于活动/社区线索，本轮不进入高信号。

## GitHub Trending / Daily Repos

本轮 GitHub Trending Daily 成功解析 10 个 repo，10/10 README 文件已写入目录。索引见 [`../raw/2026-05-15/github-trending.json`](../raw/2026-05-15/github-trending.json)，README 原文见 [`../raw/2026-05-15/github-trending-readmes/`](../raw/2026-05-15/github-trending-readmes/)。证据等级统一按 `secondary-source` 处理：它只能说明项目当天在 GitHub Trending 页面可见，不代表官方发布、质量背书或长期趋势。

- [`ruvnet/RuView`](https://github.com/ruvnet/RuView)：这是把 commodity WiFi/ESP32 CSI 信号用于空间感知、presence detection、呼吸/心率监测和 through-wall sensing 的项目。README 明确写着 beta、API/firmware 可能变化、ESP32-C3/original ESP32 不支持，且 camera-ground-truth PCK 训练/评估仍未完成。它值得记录是因为 camera-free sensing 与 edge AI/隐私设备交叉，但证据边界很重：不能把 README claim 当作实测医疗或安防能力。归档：[`../raw/2026-05-15/github-trending-readmes/ruvnet__RuView.md`](../raw/2026-05-15/github-trending-readmes/ruvnet__RuView.md)。
- [`tinyhumansai/openhuman`](https://github.com/tinyhumansai/openhuman)：这是 personal AI assistant / desktop agent，README 继续强调 UI-first、daily-life integrations、Google Meet participant、background thinking、Memory Tree、本地 vault 和长期记忆。它解决的是个人 agent 如何持续获得上下文，而不是每次冷启动；风险仍是 OAuth 权限、后台同步、隐私、删除治理和记忆污染。归档：[`../raw/2026-05-15/github-trending-readmes/tinyhumansai__openhuman.md`](../raw/2026-05-15/github-trending-readmes/tinyhumansai__openhuman.md)。
- [`rohitg00/agentmemory`](https://github.com/rohitg00/agentmemory)：这是给 coding agents 用的 persistent memory server，README 声称支持 Claude Code、Cursor、Gemini CLI、Codex CLI、OpenCode 等，通过 hooks、MCP 或 REST API 共享同一个 memory server，并加入 confidence scoring、lifecycle、knowledge graph 和 hybrid search。它值得记录是因为 memory 变成跨 harness 的外部状态层。待验证点是权限隔离、删除治理、confidence decay、hooks 安全和 benchmark 真实性。归档：[`../raw/2026-05-15/github-trending-readmes/rohitg00__agentmemory.md`](../raw/2026-05-15/github-trending-readmes/rohitg00__agentmemory.md)。
- [`obra/superpowers`](https://github.com/obra/superpowers)：这是 agentic skills framework / software development methodology。README 描述它让 agent 先澄清意图、形成 spec、拿到 design sign-off、生成 implementation plan，再进入 subagent-driven-development；支持 Claude Code、Codex CLI、Codex App、Gemini CLI、OpenCode、Cursor 等 harness。它是 skills/workflow 状态化的强 discovery signal；风险是 workflow 是否被 runtime 强制执行、与 repo-local rules 冲突时谁优先。归档：[`../raw/2026-05-15/github-trending-readmes/obra__superpowers.md`](../raw/2026-05-15/github-trending-readmes/obra__superpowers.md)。
- [`K-Dense-AI/scientific-agent-skills`](https://github.com/K-Dense-AI/scientific-agent-skills)：这是 scientific/research agent skills 集合，README 写到 135 ready-to-use skills、100+ scientific/financial databases、70+ optimized Python package skills，并支持 Cursor、Claude Code、Codex 等 agent。它值得记录是因为 agent skills 正从通用 coding workflow 扩展到科研、临床、材料、金融数据库和多步分析；边界是专业领域输出需要事实校验、数据许可和人工 review。归档：[`../raw/2026-05-15/github-trending-readmes/K-Dense-AI__scientific-agent-skills.md`](../raw/2026-05-15/github-trending-readmes/K-Dense-AI__scientific-agent-skills.md)。
- [`shiyu-coder/Kronos`](https://github.com/shiyu-coder/Kronos)：这是金融 candlestick/K-line foundation model 项目，README 称它用 45+ global exchanges 数据训练，通过 specialized tokenizer 把 OHLCV quantize 成 discrete tokens，再用 autoregressive Transformer 做多种 quantitative tasks。它今天值得记录是因为金融模型开始采用 foundation-model 叙事；风险是 forecast demo 不等于 trading edge，也不证明回测、风控、执行和合规可用。归档：[`../raw/2026-05-15/github-trending-readmes/shiyu-coder__Kronos.md`](../raw/2026-05-15/github-trending-readmes/shiyu-coder__Kronos.md)。
- [`roboflow/supervision`](https://github.com/roboflow/supervision)：这是 computer vision toolkit，README 强调 model-agnostic detections、connectors、zone counting、annotation/dataset utilities 和 inference integration。它和本 watch 的交集在 AI systems / vision tooling，不是 agent 主线。归档：[`../raw/2026-05-15/github-trending-readmes/roboflow__supervision.md`](../raw/2026-05-15/github-trending-readmes/roboflow__supervision.md)。
- [`influxdata/telegraf`](https://github.com/influxdata/telegraf)：这是 metrics/logs/arbitrary data collection agent，README 记录 300+ plugins、TOML config、standalone static binary 和多种 monitoring/messaging integrations。它与 AI 主线弱相关，但对 observability/agent telemetry 有类比价值。归档：[`../raw/2026-05-15/github-trending-readmes/influxdata__telegraf.md`](../raw/2026-05-15/github-trending-readmes/influxdata__telegraf.md)。
- [`supertone-inc/supertonic`](https://github.com/supertone-inc/supertonic)：这是 on-device multilingual TTS，README 写到 ONNX Runtime、本地推理、31-language support、public ONNX assets 和 PyPI package。它是 local inference / voice interface discovery signal，和 agent 主线的交集在端侧语音输出。归档：[`../raw/2026-05-15/github-trending-readmes/supertone-inc__supertonic.md`](../raw/2026-05-15/github-trending-readmes/supertone-inc__supertonic.md)。
- [`Genymobile/scrcpy`](https://github.com/Genymobile/scrcpy)：这是 Android device mirror/control 工具，README 强调 USB/TCP/IP 控制、低延迟、无 root、无账号、无广告、无网络需求。它不是 AI 项目，但与 GUI/mobile automation 的操作面有关；若进入 agent 工具链，需要额外看权限和设备控制边界。归档：[`../raw/2026-05-15/github-trending-readmes/Genymobile__scrcpy.md`](../raw/2026-05-15/github-trending-readmes/Genymobile__scrcpy.md)。

## 来源证据表

| 信号 | 证据等级 | 来源 | URL | 本地归档 |
| --- | --- | --- | --- | --- |
| Codex in ChatGPT mobile app | official-source / direct-x | OpenAI Blog RSS + `@OpenAI` | https://openai.com/index/work-with-codex-from-anywhere | [`../raw/2026-05-15/rss-items.json`](../raw/2026-05-15/rss-items.json), [`../raw/2026-05-15/twitterapi-io-results.json`](../raw/2026-05-15/twitterapi-io-results.json) |
| Codex Windows sandbox | official-source | OpenAI Blog RSS / official readable extract | https://openai.com/index/building-codex-windows-sandbox | [`../trend/raw/2026-05-15/forward-deployed-engineering/fulltext/openai-codex-windows-sandbox.extracted.md`](../trend/raw/2026-05-15/forward-deployed-engineering/fulltext/openai-codex-windows-sandbox.extracted.md) |
| TanStack npm supply-chain response | official-source | OpenAI Blog RSS / official readable extract | https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack | [`../trend/raw/2026-05-15/forward-deployed-engineering/fulltext/openai-tanstack-supply-chain.extracted.md`](../trend/raw/2026-05-15/forward-deployed-engineering/fulltext/openai-tanstack-supply-chain.extracted.md) |
| Continuous batching asynchronicity | official-source | Hugging Face Blog RSS | https://huggingface.co/blog/continuous_async | [`../raw/2026-05-15/rss-items.json`](../raw/2026-05-15/rss-items.json) |
| Forward deployed engineering heats up again | secondary-source / limited-paid | The Pragmatic Engineer RSS | https://newsletter.pragmaticengineer.com/p/the-pulse-forward-deployed-engineering | [`../trend/raw/2026-05-15/forward-deployed-engineering/fulltext/pragmatic-fde.extracted.md`](../trend/raw/2026-05-15/forward-deployed-engineering/fulltext/pragmatic-fde.extracted.md) |
| System of Record to System of Intelligence | secondary-source | a16z News RSS / fulltext archive | https://www.a16z.news/p/from-system-of-record-to-system-of | [`../trend/raw/2026-05-15/forward-deployed-engineering/fulltext/a16z-system-of-intelligence.extracted.md`](../trend/raw/2026-05-15/forward-deployed-engineering/fulltext/a16z-system-of-intelligence.extracted.md) |
| agentmemory persistent memory | secondary-source | GitHub Trending / repo README | https://github.com/rohitg00/agentmemory | [`../raw/2026-05-15/github-trending-readmes/rohitg00__agentmemory.md`](../raw/2026-05-15/github-trending-readmes/rohitg00__agentmemory.md) |
| Superpowers agentic methodology | secondary-source | GitHub Trending / repo README | https://github.com/obra/superpowers | [`../raw/2026-05-15/github-trending-readmes/obra__superpowers.md`](../raw/2026-05-15/github-trending-readmes/obra__superpowers.md) |
| Scientific Agent Skills | secondary-source | GitHub Trending / repo README | https://github.com/K-Dense-AI/scientific-agent-skills | [`../raw/2026-05-15/github-trending-readmes/K-Dense-AI__scientific-agent-skills.md`](../raw/2026-05-15/github-trending-readmes/K-Dense-AI__scientific-agent-skills.md) |
| Kronos financial-market model | secondary-source | GitHub Trending / repo README | https://github.com/shiyu-coder/Kronos | [`../raw/2026-05-15/github-trending-readmes/shiyu-coder__Kronos.md`](../raw/2026-05-15/github-trending-readmes/shiyu-coder__Kronos.md) |
| Codex enterprise trial / speed-intelligence tradeoff | direct-x | `@sama` | https://x.com/sama/status/2054626219858293128 | [`../raw/2026-05-15/twitterapi-io-results.json`](../raw/2026-05-15/twitterapi-io-results.json) |
| Gates Foundation partnership | direct-x | `@AnthropicAI` | https://x.com/AnthropicAI/status/2054941901900611787 | [`../raw/2026-05-15/twitterapi-io-results.json`](../raw/2026-05-15/twitterapi-io-results.json) |

## X/Twitter 覆盖说明

- 本次 X/Twitter 只使用 `twitterapi.io` 的 `GET https://api.twitterapi.io/twitter/user/last_tweets` read endpoint，`includeReplies=false`。
- `twitterapi.io` 顶层状态为 `ok`，26 个账号均返回 `status=ok`；没有把任何 credential/API 异常当作“无推文”。
- 本轮共保留 145 条 direct-x 原始条目。保留数较高的账号包括 `corbin_braun` 20 条、`cellinlab` 15 条、`steipete` 14 条、`Hesamation` 13 条、`levelsio` 11 条、`cnyzgkc` 11 条、`kloss_xyz` 10 条。
- `karpathy`、`rryssf_`、`oviswang`、`Yangyixxxx`、`zhaogua61654931`、`lidang`、`_LuoFuli` 请求成功但 kept_count 为 0；这表示 36 小时窗口和脚本过滤下没有保留条目，不等于账号没有更新。
- direct-x 内容包含个人观点、短评论、转发、产品线索和活动宣传；日报只把它们作为直接来源线索，不把个人观点写成官方事实。

## 运行结果与失败源

- RSS：31/31 成功；本轮没有 RSS failed source。
- GitHub releases：6/6 release Atom feed 成功；GitHub REST API 状态为 `skipped`，脚本按设计使用 Atom feed。
- GitHub Trending：1/1 成功，解析 10 个每日热门 repo，10 个 README 文件已归档。
- 官方页面：`anthropic-news-page`、`claude-blog` 成功；`openai-news` limited，原因是 HTML 页面未返回可用 title/content snapshot，但 OpenAI RSS 成功；`claude-docs-release-notes` limited，原因是跳转到 `platform.claude.com` 后返回 region-unavailable HTML。
- X/Twitter：`twitterapi.io` 顶层 `ok`，26 个账号请求成功；没有 failed accounts，没有 Exa fallback。

## 不确定性与待验证项

- 已确认边界：本日报覆盖 2026-05-15 raw 输出、[`../raw/2026-05-15/manifest.json`](../raw/2026-05-15/manifest.json)、[`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)；GitHub Trending 只覆盖 `https://github.com/trending?since=daily` 当前 HTML 中解析到的前 10 个 repo，以及脚本归档的 README；X/Twitter 只覆盖 `twitterapi.io` 返回并被 36 小时窗口保留的 direct-x 条目。
- 未覆盖范围：没有抓取登录态网页、没有补采 X thread/context、没有打开每个 GitHub release 的完整正文、没有浏览器渲染 OpenAI/Anthropic official pages、没有验证 Trending repo 的源码质量或运行效果。
- 推断项：【推断得出】本日报把“coding-agent 安全落地 + skills/memory 产品化 + FDE 部署 substrate + 金融模型 discovery”作为今天主线。依据是 OpenAI RSS/官方可读抽取、Hugging Face RSS、a16z 全文、GitHub Trending README 和 direct-x 同日出现；失效条件是后续源码、产品文档或客户案例显示这些只是 marketing framing、demo 项目或不可复现实现。
- 待验证项：细读 Hugging Face continuous batching 技术正文；若有订阅权限，打开 Pragmatic Engineer FDE 全文确认 operating model；审计 `agentmemory` hooks/delete/audit；检查 `superpowers` 与 Codex/Claude plugin runtime 的 enforcement；审计 Kronos 数据、回测、预测边界和是否触达交易动作；继续观察 `openai-news` 与 `claude-docs-release-notes` official page limited 是否为环境问题。

## 运行统计

- 新增条目：`seen_added=46`。
- 高信号条目：9 条。
- 失败来源：official page failed 0 个；twitterapi.io failed accounts 0 个。
- limited 来源：official page limited 2 个：`openai-news`、`claude-docs-release-notes`。

## 完成审计

- 用户目标拆解：稳定来源采集、twitterapi.io direct-x 采集、状态更新、日报生成、trend report 生成、enabled trends 检查、失败/limited 来源说明、输出路径汇总。
- 证据对应：raw JSON 写入 [`../raw/2026-05-15/`](../raw/2026-05-15/)，状态文件写入 [`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)，日报为当前文件。
- 状态同步：`update-state.py` 已生成 [`../raw/2026-05-15/manifest.json`](../raw/2026-05-15/manifest.json)，并更新 source health 与 seen。
- 来源边界：所有 X/Twitter 内容标为 `direct-x`，GitHub Trending 标为 `secondary-source`，官方 RSS/GitHub release/official pages 标为 `official-source` 或 official metadata；未用 Exa fallback。
- Trend 检查：`memory-dream`、`financial-agents` 有新增趋势信号并更新专题；`forward-deployed-engineering` 已补全文/可读抽取并更新专题。Pragmatic Engineer 正文仍受 paid gate 限制，未用于强结论。
