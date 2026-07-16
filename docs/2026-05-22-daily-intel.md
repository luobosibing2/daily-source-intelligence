# 2026-05-22 Daily Source Intelligence

## 采集范围

- 运行时间：2026-05-22 Asia/Shanghai，本轮写入 [`../raw/2026-05-22/`](../raw/2026-05-22/)。
- 稳定来源：RSS/Atom 31 个源全部成功；相关全文 43 条尝试，43 条 ok、0 条 limited、0 条 failed；GitHub releases 7 个源成功；GitHub Trending 1 个源成功，解析 10 个每日热门 repo；official pages 4 个源成功、0 个 failed。
- X/Twitter：通过 `twitterapi.io` read endpoint 采集，顶层状态 `ok`；27 个账号全部 ok，保留 147 条 direct-x 原始条目。
- 状态更新：[`../raw/2026-05-22/manifest.json`](../raw/2026-05-22/manifest.json)、[`../state/source-health.json`](../state/source-health.json)、[`../state/seen.json`](../state/seen.json) 已由 `update-state.py` 更新；本轮 `seen_added=35`，累计 991 条。
- 本次没有使用 Exa MCP、登录态浏览器、X/Twitter 账号凭证、写操作 endpoint、posting、liking、following 或 DM。
- 本地归档：[`../raw/2026-05-22/rss-items.json`](../raw/2026-05-22/rss-items.json)、[`../raw/2026-05-22/github-items.json`](../raw/2026-05-22/github-items.json)、[`../raw/2026-05-22/github-trending.json`](../raw/2026-05-22/github-trending.json)、[`../raw/2026-05-22/github-trending-readmes/`](../raw/2026-05-22/github-trending-readmes/)、[`../raw/2026-05-22/official-pages.json`](../raw/2026-05-22/official-pages.json)、[`../raw/2026-05-22/twitterapi-io-results.json`](../raw/2026-05-22/twitterapi-io-results.json)。

## 今日高信号

1. OpenAI Codex `0.133.0` 是今天最强 first-party coding-agent runtime 信号：Goals 默认启用并进入 dedicated storage，remote-control、permission profiles、plugin discovery、extension lifecycle hooks 和 packaged runtime/release pipeline 同时推进。【有明确证据支撑 / first-party-openai / release-fulltext-ok】证据见 [`openai-codex-0.133.0.atom.md`](../raw/2026-05-22/github-release-fulltext/openai-codex/openai-codex-0.133.0-e5c3c75b2a.atom.md#L7)。
2. Claude Code `v2.1.147` 和 `v2.1.148` 是 runtime hardening 信号：`v2.1.147` 修复 pinned background sessions、`/code-review`、auto-updater、managed login、MCP pagination、AskUserQuestion、background permission、subagent model forwarding 等长任务边界；`v2.1.148` 又修复 `2.1.147` 引入的 Bash tool exit code 127 regression。【有明确证据支撑 / first-party-claude-code / release-fulltext-ok/limited】证据见 [`v2.1.147`](../raw/2026-05-22/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.147-949492598a.atom.md#L7) 与 [`v2.1.148`](../raw/2026-05-22/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.148-1360a65d32.atom.md#L7)。
3. OpenAI/AdventHealth 是今天最强 enterprise AI deployment / healthcare adoption 信号：材料把 `ChatGPT for Healthcare` 放进 utilization management、文档/总结、跨部门 workflow、privacy/governance、EHR timestamp metrics、daily usage KPI 和 change leadership，而不是只讲单点 pilot。【有明确证据支撑 / official-source / fulltext-ok】证据见 [`openai-adventhealth`](../raw/2026-05-22/rss-fulltext/openai-blog/openai-blog-adventhealth-advances-whole-person-care-with-openai-85a3fdb43c.autocli.md#L24)、[`#L38`](../raw/2026-05-22/rss-fulltext/openai-blog/openai-blog-adventhealth-advances-whole-person-care-with-openai-85a3fdb43c.autocli.md#L38)、[`#L52`](../raw/2026-05-22/rss-fulltext/openai-blog/openai-blog-adventhealth-advances-whole-person-care-with-openai-85a3fdb43c.autocli.md#L52) 和 [`#L99`](../raw/2026-05-22/rss-fulltext/openai-blog/openai-blog-adventhealth-advances-whole-person-care-with-openai-85a3fdb43c.autocli.md#L99)。
4. Datasette Agent 是 developer-data agent 的 practical release：Simon Willison 发布 extensible AI assistant for Datasette，支持对 SQLite 数据问答、插件扩展、charts、imagegen、Fly Sprites sandbox，并能跑 local models；边界是这是项目 alpha/生态 release，不是 benchmark。【有明确证据支撑 / official-blog / fulltext-ok】证据见 [`simonwillison-datasette-agent`](../raw/2026-05-22/rss-fulltext/simonwillison/simonwillison-datasette-agent-1116f836bd.extracted.md#L1)。
5. antirez 的 LLM agent EDIT tool 讨论是 agent tooling 设计信号：他把传统 `old/new` CAS edit 与 line tag / file CRC tradeoff 对比，重点是 token-poor local inference、colliding edits、hallucinated line content 和 edit reliability。【有明确证据支撑 / official-blog / fulltext-ok】证据见 [`antirez-edit-tool`](../raw/2026-05-22/rss-fulltext/antirez/antirez-alternatives-for-the-edit-tool-of-llm-agents-a9be0014dd.autocli.md#L11) 到 [`#L45`](../raw/2026-05-22/rss-fulltext/antirez/antirez-alternatives-for-the-edit-tool-of-llm-agents-a9be0014dd.autocli.md#L45)。
6. GitHub Trending 继续集中在 coding-agent substrate：`claude-plugins-official`、`CodeGraph`、Karpathy-inspired guidelines、`.NET Agent Skills`、`Superpowers`、`CLI-Anything`、`ChromeDevTools MCP` 和 `notebooklm-py` 仍在榜，10/10 README 已归档。【有明确证据支撑 / secondary-source】它是 discovery signal，不是质量背书。
7. direct-x 中 `@OpenAI` 和 `@sama` 提到 Codex Thursday / new Codex ships，`@simonw` 发布 Datasette Agent，`@mattpocockuk` 讨论 `/handoff`、TDD skill 和战略编程。这些是实时线索，产品事实仍应回到 official pages、release body 或项目 README。【有明确证据支撑 / direct-x】证据见 [`twitterapi-io-results.json`](../raw/2026-05-22/twitterapi-io-results.json)。

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS 今天 5/5 条按 `fulltext_policy: always` 读取并归档成功：AdventHealth、Ramp/Codex、Education for Countries、OpenAI 数学突破、OpenAI for Singapore。归档见 [`../raw/2026-05-22/rss-fulltext/openai-blog/`](../raw/2026-05-22/rss-fulltext/openai-blog/)。
- OpenAI Codex release Atom 读取 5 条，其中 `0.133.0` fulltext ok，四个 `0.133.0-alpha.*` / `rust-v0.133.0-alpha.2` limited；今天只把 `0.133.0` 写成完整 release body 已读。
- Claude Code release Atom 读取 5 条，其中 `v2.1.147` 到 `v2.1.144` fulltext ok，`v2.1.148` 内容很短但可读；重点是 `v2.1.147` 的 background session、`/code-review`、MCP pagination、AskUserQuestion、permission、managed login 和 Windows/PowerShell 修复，以及 `v2.1.148` 对 Bash tool regression 的补丁。
- OpenAI official news page 通过 `autocli-read` 归档，但它只是 news index；Claude docs release notes 页面返回 region/cookie 限制页，不作为 Claude docs 更新事实来源。证据见 [`openai-news`](../raw/2026-05-22/official-page-text/openai-news-openai-news-cd4de9e9e7.autocli.md#L16) 与 [`claude-docs-region-limit`](../raw/2026-05-22/official-page-text/claude-docs-release-notes-app-unavailable-in-region-claude-5092885c3d.autocli.md#L1)。

## 按主题分组摘要

### AI Coding / Developer Tools

- Codex `0.133.0` 的主线是把 app/runtime/control surface 做厚：Goals 默认启用、remote-control 可报告机器状态、permission profile 可列出/继承/刷新、plugin discovery 可 inspect，extensions 可观察 subagent/tool/turn lifecycle。
- Claude Code `v2.1.147/148` 继续处理长任务可靠性：pinned background sessions、slash command error、MCP pagination、managed login、permission rule、subagent model forwarding、Windows/PowerShell 和 Bash regression 都是 coding agent 在真实机器上跑久之后才会暴露的问题。
- antirez 的 EDIT tool 讨论值得记录，因为它不是泛 prompt tip，而是围绕 edit CAS、line tags、CRC、token budget、并发编辑和 hallucinated context 设计 agent tool contract。

### AI Agent / Agentic Workflow

- Datasette Agent 把 agent 放到具体数据工具里：自然语言问 SQLite、生成 SQL、插件化扩展 charts/imagegen/sandbox，并把 local model tool-call 能力当成可跑路径。这是 agent 从 generic chat 进入 domain app 的清晰例子。
- GitHub Trending 的 skills/plugins/codegraph/devtools set 延续昨天主线：agent 行为约束、上下文索引、浏览器调试和软件 harness 正在被打包成可安装资产。
- direct-x 中 `/handoff`、TDD skill、Codex mobile/remote-control 线索继续说明：agent workflow 的竞争面正在从“写代码快”转向“长上下文交接、审查、工具远程操作和人类监督”。

### LLM / Frontier Models

- OpenAI 数学突破和 Gemini Omni 仍在 RSS 窗口内出现，但它们是前几日报告已读的一手信号；今天不重复扩写。
- 今天 LLM 主线更偏应用和 runtime：医疗系统 adoption、coding-agent runtime、data-agent release 和 edit-tool contract，而不是新模型权重或 benchmark。

### Forward Deployed Engineering / Enterprise AI

- AdventHealth 是今天 FDE/enterprise AI 核心新增。材料强调 adoption is the product、domain peer groups、governance controls、healthcare safeguards、system-level EHR timestamps 和 change leadership，说明落地难点是组织行为、度量和信任，而不只是模型能力。
- 这条 healthcare case 与前几天 Dell/Codex、Singapore Applied AI Lab、Ramp/Codex 形成连续线：enterprise AI last mile 正在按基础设施位置、行业合规、工作流重设计、现场 adoption 和供应商协作来包装。

### Financial Agents

- 今天没有新的 financial-agent action surface。OpenAI news index 仍包含 2026-05-15 的 ChatGPT personal finance 入口，但这已在 2026-05-17 专题里按 fulltext confirmed 处理。
- 本轮未发现新的 trading、payment、ledger、Treasury、banking connector、regulated advice、investment execution 或 human sign-off 新证据。

### Product / Growth / Indie Founder

- direct-x 中 `@marclou` 的 TrustMRR payment provider / marketing channel 更新、`@levelsio` 的 product/data side project chatter、`@mattpocockuk` 的 junior developer training 讨论有 pulse 价值，但不提升为市场事实。
- 对 product/growth 的主要启发仍来自 AdventHealth：把 adoption 当作可度量产品、用同行 domain groups 做 change management，比一次性 prompt training 更接近可复制落地机制。

## GitHub Trending / Daily Repos

本轮 GitHub Trending Daily 成功解析 10 个 repo，10/10 README 文件已写入目录。索引见 [`../raw/2026-05-22/github-trending.json`](../raw/2026-05-22/github-trending.json)，README 原文见 [`../raw/2026-05-22/github-trending-readmes/`](../raw/2026-05-22/github-trending-readmes/)。证据等级统一按 `secondary-source` 处理：它只能说明项目当天在 GitHub Trending 页面可见，不代表官方发布、质量背书或长期趋势。

- [`anthropics/claude-plugins-official`](https://github.com/anthropics/claude-plugins-official)：Anthropic-managed Claude Code plugin directory。README 能确认 internal/external plugin structure、install command、Discover UI、plugin metadata、MCP config、commands、agents、skills 和 trust warning；边界是每个插件仍需单独审计。归档：[`../raw/2026-05-22/github-trending-readmes/anthropics__claude-plugins-official.md`](../raw/2026-05-22/github-trending-readmes/anthropics__claude-plugins-official.md)。
- [`colbymchenry/codegraph`](https://github.com/colbymchenry/codegraph)：local semantic code graph for Claude Code、Cursor、Codex 和 OpenCode。README 能确认 installer、project init、symbol/call graph 和 benchmark claims；它解决 coding agent 反复 grep/read 带来的 token/tool-call 成本，边界是 freshness 和 benchmark 需要复现。归档：[`../raw/2026-05-22/github-trending-readmes/colbymchenry__codegraph.md`](../raw/2026-05-22/github-trending-readmes/colbymchenry__codegraph.md)。
- [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills)：一个 `CLAUDE.md` guidance file，把 coding-agent 常见失败压成 think/simplicity/surgical/goal-driven rules。它值得记录是因为 behavior spec 正被当成 agent quality layer；边界是它本身不是 runtime enforcement。归档：[`../raw/2026-05-22/github-trending-readmes/multica-ai__andrej-karpathy-skills.md`](../raw/2026-05-22/github-trending-readmes/multica-ai__andrej-karpathy-skills.md)。
- [`dotnet/skills`](https://github.com/dotnet/skills)：Microsoft/.NET team 的 curated agent skills 与 custom agents，覆盖 .NET build、data、diagnostics、upgrade、MAUI、AI、tests、ASP.NET 等方向，并支持多个 coding-agent harness。归档：[`../raw/2026-05-22/github-trending-readmes/dotnet__skills.md`](../raw/2026-05-22/github-trending-readmes/dotnet__skills.md)。
- [`obra/superpowers`](https://github.com/obra/superpowers)：agentic software development methodology。README 能确认它用 skills 强制澄清、设计、计划、TDD、subagent-driven-development、review 和 finish workflow；边界是 README 不能证明运行时强制执行。归档：[`../raw/2026-05-22/github-trending-readmes/obra__superpowers.md`](../raw/2026-05-22/github-trending-readmes/obra__superpowers.md)。
- [`HKUDS/CLI-Anything`](https://github.com/HKUDS/CLI-Anything)：把软件包装成 agent-native CLI harness。它解决 agent 操作复杂软件的接口层问题；风险是自动写入、credential、sandbox 和版本兼容性。归档：[`../raw/2026-05-22/github-trending-readmes/HKUDS__CLI-Anything.md`](../raw/2026-05-22/github-trending-readmes/HKUDS__CLI-Anything.md)。
- [`rmyndharis/OpenWA`](https://github.com/rmyndharis/OpenWA)：self-hosted WhatsApp API Gateway，含 dashboard、多 session、webhooks、API key auth、bulk messaging、proxy、rate limiting 和 audit logging；涉及平台政策、账号安全、bulk messaging 滥用和隐私风险。归档：[`../raw/2026-05-22/github-trending-readmes/rmyndharis__OpenWA.md`](../raw/2026-05-22/github-trending-readmes/rmyndharis__OpenWA.md)。
- [`ChromeDevTools/chrome-devtools-mcp`](https://github.com/ChromeDevTools/chrome-devtools-mcp)：Chrome DevTools for coding agents，提供 MCP server、Chrome/Puppeteer automation、network/console/screenshot/performance trace；风险是浏览器内容暴露、usage statistics 和 session 隔离。归档：[`../raw/2026-05-22/github-trending-readmes/ChromeDevTools__chrome-devtools-mcp.md`](../raw/2026-05-22/github-trending-readmes/ChromeDevTools__chrome-devtools-mcp.md)。
- [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch)：AI engineering curriculum，435 lessons、20 phases、四种语言、每课生成 prompt/skill/agent/MCP artifact；这是 education / skill-building discovery signal，不是 agent runtime release。归档：[`../raw/2026-05-22/github-trending-readmes/rohitg00__ai-engineering-from-scratch.md`](../raw/2026-05-22/github-trending-readmes/rohitg00__ai-engineering-from-scratch.md)。
- [`teng-lin/notebooklm-py`](https://github.com/teng-lin/notebooklm-py)：NotebookLM unofficial Python API、CLI 和 agent skill，支持 source import、research queries、artifact generation/download、Google Docs/Sheets export；README 明确使用 undocumented Google APIs，不能当稳定官方 API。归档：[`../raw/2026-05-22/github-trending-readmes/teng-lin__notebooklm-py.md`](../raw/2026-05-22/github-trending-readmes/teng-lin__notebooklm-py.md)。

## 来源证据表

| 信号 | 证据等级 | 来源 | URL | 本地归档 |
| --- | --- | --- | --- | --- |
| Codex `0.133.0` | official-source | GitHub release Atom | https://github.com/openai/codex/releases/tag/rust-v0.133.0 | [`../raw/2026-05-22/github-release-fulltext/openai-codex/openai-codex-0.133.0-e5c3c75b2a.atom.md`](../raw/2026-05-22/github-release-fulltext/openai-codex/openai-codex-0.133.0-e5c3c75b2a.atom.md) |
| Claude Code `v2.1.147/148` | official-source | GitHub release Atom | https://github.com/anthropics/claude-code/releases | [`../raw/2026-05-22/github-release-fulltext/anthropics-claude-code/`](../raw/2026-05-22/github-release-fulltext/anthropics-claude-code/) |
| AdventHealth with OpenAI | official-source | OpenAI Blog RSS/fulltext | https://openai.com/index/adventhealth | [`../raw/2026-05-22/rss-fulltext/openai-blog/openai-blog-adventhealth-advances-whole-person-care-with-openai-85a3fdb43c.autocli.md`](../raw/2026-05-22/rss-fulltext/openai-blog/openai-blog-adventhealth-advances-whole-person-care-with-openai-85a3fdb43c.autocli.md) |
| Datasette Agent | official-blog | Simon Willison RSS/fulltext | https://simonwillison.net/2026/May/21/datasette-agent/ | [`../raw/2026-05-22/rss-fulltext/simonwillison/simonwillison-datasette-agent-1116f836bd.extracted.md`](../raw/2026-05-22/rss-fulltext/simonwillison/simonwillison-datasette-agent-1116f836bd.extracted.md) |
| LLM agent EDIT tool | official-blog | antirez RSS/fulltext | https://antirez.com/news/166 | [`../raw/2026-05-22/rss-fulltext/antirez/antirez-alternatives-for-the-edit-tool-of-llm-agents-a9be0014dd.autocli.md`](../raw/2026-05-22/rss-fulltext/antirez/antirez-alternatives-for-the-edit-tool-of-llm-agents-a9be0014dd.autocli.md) |
| Direct X product/runtime signals | direct-x | `twitterapi.io` | multiple X URLs | [`../raw/2026-05-22/twitterapi-io-results.json`](../raw/2026-05-22/twitterapi-io-results.json) |
| Coding-agent substrate Trending set | secondary-source | GitHub Trending / README | multiple GitHub URLs | [`../raw/2026-05-22/github-trending-readmes/`](../raw/2026-05-22/github-trending-readmes/) |

## X/Twitter 覆盖说明

- 本次 X/Twitter 只使用 `twitterapi.io` 的 `GET https://api.twitterapi.io/twitter/user/last_tweets` read endpoint，`includeReplies=false`。
- `twitterapi.io` 顶层采集成功：27 个账号均 `ok`，没有 failed accounts。
- 本轮共保留 147 条 direct-x 原始条目。保留数较高的账号包括 `levelsio` 20 条、`corbin_braun` 20 条、`cellinlab` 19 条、`Hesamation` 15 条、`rileybrown` 14 条、`marclou` 9 条、`sama` 8 条、`frxiaobei` 8 条。
- `karpathy`、`AnthropicAI`、`gregisenberg`、`rryssf_`、`oviswang`、`Yangyixxxx`、`lidang`、`cnyzgkc`、`_LuoFuli` 请求成功但 kept_count 为 0；这表示 36 小时窗口和脚本过滤下没有保留条目，不等于账号没有更新。
- direct-x 内容包含个人观点、短评论、转发、产品线索和活动宣传；日报只把它们作为直接来源线索，不把个人观点写成官方事实。

## 运行结果与失败源

- RSS：31/31 成功；RSS fulltext 43 条尝试，43 条 ok、0 条 limited、0 条 failed。
- GitHub releases：7/7 release Atom feed 成功；GitHub REST API 状态为 `skipped`，脚本按设计使用 Atom feed。
- GitHub release fulltext：OpenAI Codex 1/5 ok、4/5 limited；Claude Code 4/5 ok、`v2.1.148` 内容很短但可读，manifest 标记 first-party limited 1 条。
- GitHub Trending：1/1 成功，解析 10 个每日热门 repo，10 个 README 文件已归档。
- 官方页面：4/4 ok，0 failed；Claude Docs Release Notes 返回 region/cookie 限制页，不用于实质更新判断。
- X/Twitter：`twitterapi.io` 顶层采集成功，27/27 accounts ok；没有使用 Exa fallback。

## 不确定性与待验证项

- 已确认边界：本日报覆盖 2026-05-22 raw 输出、[`../raw/2026-05-22/manifest.json`](../raw/2026-05-22/manifest.json)、[`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)；GitHub Trending 只覆盖 `https://github.com/trending?since=daily` 当前 HTML 中解析到的 10 个 repo，以及脚本归档的 README；X/Twitter 只覆盖 `twitterapi.io` 返回并被 36 小时窗口保留的 direct-x 条目。
- 未覆盖范围：没有抓取登录态网页、没有补采 X thread/context、没有复现 GitHub Trending repo、没有运行 Codex `0.133.0`、Claude Code `v2.1.147/148`、Datasette Agent 或 antirez 的 edit tool variants，也没有验证 AdventHealth 的内部 rollout metrics。
- 推断项：【推断得出】本日报把 “agent runtime control plane + enterprise adoption as change management + domain app agentization” 作为今天主线。依据是 Codex/Claude 一手 release、OpenAI/AdventHealth 一手案例、Datasette Agent/antirez 原文和 GitHub Trending 同日出现；失效条件是后续使用显示这些 release/regression、案例或 README 只是短期宣传或未成熟实验。
- 待验证项：运行 Codex `0.133.0` 的 Goals、remote-control、permission profiles、plugin discovery 和 extension hooks；复现 Claude Code `v2.1.147/148` 的 Bash regression fix、MCP pagination、AskUserQuestion、background permission 和 subagent model forwarding；试跑 Datasette Agent 的 SQLite tool call / plugin path / local model path；比较 antirez line-tag edit 与 whole-file CRC edit 的 collision、token 和并发编辑表现；继续查 AdventHealth 是否公开 privacy、clinical safety、quality measurement、human review 和 deployment governance 细节。

## 运行统计

- 新增条目：`seen_added=35`。
- 高信号条目：7 条。
- 失败来源：RSS failed 0 个；official page failed 0 个；twitterapi.io failed accounts 0 个。
- limited 来源：OpenAI Codex release fulltext limited 4 条；Claude Code release fulltext limited 1 条；RSS fulltext limited 0 条。

## 完成审计

- 用户目标拆解：稳定来源采集、twitterapi.io direct-x 采集、状态更新、日报生成、enabled trends 检查、失败/limited 来源说明、输出路径汇总。
- 证据对应：raw JSON 写入 [`../raw/2026-05-22/`](../raw/2026-05-22/)，状态文件写入 [`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)，日报为当前文件。
- 状态同步：`update-state.py` 已生成 [`../raw/2026-05-22/manifest.json`](../raw/2026-05-22/manifest.json)，并更新 source health 与 seen。
- 来源边界：所有 X/Twitter 内容标为 `direct-x`，GitHub Trending 标为 `secondary-source`，官方 RSS/GitHub release/official pages 标为 `official-source`、official metadata 或 limited；未用 Exa fallback。
- Trend 检查：`memory-dream`、`financial-agents`、`forward-deployed-engineering` 均已检查；trend raw 归档见 [`../trend/raw/2026-05-22/`](../trend/raw/2026-05-22/)。
