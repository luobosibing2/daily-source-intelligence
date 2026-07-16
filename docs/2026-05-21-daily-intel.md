# 2026-05-21 Daily Source Intelligence

## 采集范围

- 运行时间：2026-05-21 Asia/Shanghai，本轮写入 [`../raw/2026-05-21/`](../raw/2026-05-21/)。
- 稳定来源：RSS/Atom 31 个源全部成功；相关全文 47 条尝试，47 条 ok、0 条 limited、0 条 failed；GitHub releases 7 个源成功；GitHub Trending 1 个源成功，解析 10 个每日热门 repo；official pages 4 个源成功、0 个 limited。
- X/Twitter：通过 `twitterapi.io` read endpoint 采集，顶层状态 `ok`；27 个账号全部 ok，保留 134 条 direct-x 原始条目。
- 状态更新：[`../raw/2026-05-21/manifest.json`](../raw/2026-05-21/manifest.json)、[`../state/source-health.json`](../state/source-health.json)、[`../state/seen.json`](../state/seen.json) 已由 `update-state.py` 更新；本轮 `seen_added=64`，累计 956 条。
- 本次没有使用 Exa MCP、登录态浏览器、X/Twitter 账号凭证、写操作 endpoint、posting、liking、following 或 DM。
- 本地归档：[`../raw/2026-05-21/rss-items.json`](../raw/2026-05-21/rss-items.json)、[`../raw/2026-05-21/github-items.json`](../raw/2026-05-21/github-items.json)、[`../raw/2026-05-21/github-trending.json`](../raw/2026-05-21/github-trending.json)、[`../raw/2026-05-21/github-trending-readmes/`](../raw/2026-05-21/github-trending-readmes/)、[`../raw/2026-05-21/official-pages.json`](../raw/2026-05-21/official-pages.json)、[`../raw/2026-05-21/twitterapi-io-results.json`](../raw/2026-05-21/twitterapi-io-results.json)。

## 今日高信号

1. OpenAI 发布数学研究突破：一个内部通用推理模型推翻 planar unit distance problem 中长期被相信的 square-grid 最优猜想，并由外部数学家检查证明。【有明确证据支撑 / official-source / fulltext-ok】证据见 [`openai-model-discrete-geometry`](../raw/2026-05-21/rss-fulltext/openai-blog/openai-blog-an-openai-model-has-disproved-a-central-conjecture-in-discrete-geometr-7f625f6663.autocli.md#L12) 与 [`#L14`](../raw/2026-05-21/rss-fulltext/openai-blog/openai-blog-an-openai-model-has-disproved-a-central-conjecture-in-discrete-geometr-7f625f6663.autocli.md#L14)。
2. Ramp/Codex 是今天最强 enterprise coding-agent 落地信号：Ramp 把 Codex with GPT-5.5 用于 PR review 和 On-Call Assistant，强调从小时级 review 等待降到分钟级反馈，并且对复杂业务逻辑和 incident context 有用。【有明确证据支撑 / official-source / fulltext-ok】证据见 [`openai-ramp-codex`](../raw/2026-05-21/rss-fulltext/openai-blog/openai-blog-how-ramp-engineers-accelerate-code-review-with-codex-cb920945cf.autocli.md#L8)、[`#L20`](../raw/2026-05-21/rss-fulltext/openai-blog/openai-blog-how-ramp-engineers-accelerate-code-review-with-codex-cb920945cf.autocli.md#L20) 和 [`#L30`](../raw/2026-05-21/rss-fulltext/openai-blog/openai-blog-how-ramp-engineers-accelerate-code-review-with-codex-cb920945cf.autocli.md#L30)。
3. Claude Code `v2.1.146` 是 first-party runtime hardening 信号：`/simplify` 改名为 `/code-review`，Auto mode 不再压制显式依赖的 `AskUserQuestion`，并修复 Windows、MCP pagination、background session、managed settings、Agent SDK streaming 和 subagent model forwarding 等问题。【有明确证据支撑 / first-party-claude-code / release-fulltext-ok】证据见 [`claude-code-v2.1.146`](../raw/2026-05-21/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.146-06b1d30886.atom.md#L7)。
4. OpenAI Codex `0.133.0-alpha.*` 连续出现，但 release Atom 正文为 limited；本日报只把它记为 first-party release watch，不把 alpha 内容写成已读完整 release body。【有明确证据支撑 / first-party-openai / release-fulltext-limited】证据见 [`../raw/2026-05-21/manifest.json`](../raw/2026-05-21/manifest.json)。
5. Google Gemini Omni 继续是 multimodal generation 一手信号：它把 Gemini reasoning 与视频生成/编辑、图像/音频/视频/文本输入和 conversational editing 合在一起，并计划后续 API / enterprise rollout。【有明确证据支撑 / official-source / fulltext-ok】证据见 [`gemini-omni`](../raw/2026-05-21/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-gemini-omni-6ff85c3103.extracted.md#L1)。
6. GitHub Trending 继续集中在 coding-agent substrate：Claude plugins directory、CodeGraph、Karpathy-inspired guidelines、.NET Agent Skills、Superpowers、CLI-Anything、Chrome DevTools MCP 和 NotebookLM unofficial API/skill 同日上榜。【有明确证据支撑 / secondary-source】它是 discovery signal，不是质量背书。
7. direct-x 中 `@OpenAI`、`@sama` 围绕 OpenAI 数学突破发声，`@mattpocockuk` 讨论 tactical vs strategic programming，`@steipete` 转发 Codex compaction UX 与 coding-agent 工具反馈。这些是实时线索，但产品/论文判断仍应回到官方页面或 release body。【有明确证据支撑 / direct-x】证据见 [`twitterapi-io-results.json`](../raw/2026-05-21/twitterapi-io-results.json)。

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS 今天 5/5 条按 `fulltext_policy: always` 读取并归档成功：数学研究突破、Ramp/Codex、Education for Countries、OpenAI for Singapore、content provenance。归档见 [`../raw/2026-05-21/rss-fulltext/openai-blog/`](../raw/2026-05-21/rss-fulltext/openai-blog/)。
- 数学研究突破是今天最强 research-capability 信号：它不是专门数学系统或定向 proof search，而是通用推理模型在 Erdős problem collection 中产出证明，并由外部数学家检查；边界是原文没有给出可复现实验脚本或模型发布方式。
- Ramp/Codex 是今天最强 enterprise adoption 信号：材料把代码审查、incident/on-call 工具、复杂业务逻辑、CLI/App 体验和 vendor feedback loop 放在一起，比单纯“用了 AI code review”更接近真实组织落地。
- OpenAI Codex GitHub release Atom 读取 5 条，其中 `0.132.0` fulltext ok，四个 `0.133.0-alpha.*` / `rust-v0.133.0-alpha.2` limited；本日报不细写 limited release body。
- Claude Code GitHub release Atom 读取 `v2.1.146` 到 `v2.1.142`，5/5 release fulltext ok；今天高价值集中在 `v2.1.146` 的 code-review command、AskUserQuestion 行为、MCP pagination、background/session、managed policy 和 multi-agent fixes。

## 按主题分组摘要

### AI Coding / Developer Tools

- Ramp/Codex 把 coding agent 从 individual coding assistance 推到 platform-engineering adoption：code review 成为团队期待的 PR flow 一部分，On-Call Assistant 则把 agentic tooling 放进 incident/on-call 场景。
- Claude Code `v2.1.146` 是 operational hardening：`/code-review` 命名更贴近实际任务，`AskUserQuestion` 修复保护显式交互流程，MCP pagination 修复避免 resources/templates/prompts 丢 page 1 之后的数据。
- GitHub Trending 中 `dotnet/skills`、`multica-ai/andrej-karpathy-skills`、`obra/superpowers` 都在把 agent 行为约束做成 skills / instructions / methodology。这说明 coding-agent 质量控制面继续从 prompt advice 变成可安装、可复用的流程资产。

### AI Agent / Agentic Workflow

- `anthropics/claude-plugins-official` 上榜，说明 Claude Code plugin marketplace 的 supply-chain surface 仍是核心观察点：README 同时给出 internal/external plugin structure、install command、plugin metadata 和 trust warning。
- `CodeGraph` 与 `ChromeDevTools MCP` 分别代表两类 agent substrate：前者把代码库变成 100% local semantic code graph，后者把 live Chrome DevTools 暴露给 coding agents。一个解决代码上下文成本，一个解决浏览器调试/自动化证据面。
- `CLI-Anything`、`notebooklm-py` 和 `OpenWA` 都涉及把原本面向人的软件或服务包装成 agent 可调用接口；风险点分别是 side effect、安全边界、未公开 API 稳定性、消息/账号权限和平台 ToS。

### LLM / Frontier Models

- OpenAI 数学突破是今天最强 frontier reasoning signal：官方材料强调通用推理模型、非专门数学系统、外部数学家检查和 autonomously resolved prominent open problem。它应被记录为 research-capability 观察，不应直接推断为可用产品能力。
- Gemini Omni / Gemini for Science 仍然构成 Google 的 “model capability + workflow surface” 线索。今天日报不重复展开昨天结论，只保留为持续 official-source 背景。
- direct-x 中 `@sama` 对数学突破的解读强化了 “AI accelerating research” 叙事，但 direct-x 不能替代论文、模型卡、评测或可复现材料。

### Forward Deployed Engineering / Enterprise AI

- Ramp/Codex 是今天 FDE/enterprise AI 的核心新增：AI DevEx 不只是采购工具，而是把 Codex 嵌入 PR review、on-call tooling、first session enablement、trust-building 和 direct vendor feedback loop。
- OpenAI for Singapore、Dell/Codex 和 Ramp/Codex 连续出现，说明 Codex 的 enterprise path 正围绕三件事变清楚：客户现场数据/系统位置、复杂工程 workflow、以及需要贴近用户的启用与反馈循环。
- 今天没有新的 public-sector / national deployment official source；Singapore 信号沿用昨天归档，不新增重复判断。

### Financial Agents

- 今天没有新的 financial agent action surface。OpenAI for Singapore 仍然只把 finance 作为支持方向之一，Ramp/Codex 是企业工程案例而不是金融 agent workflow。
- 因此 Financial Agents trend 今天只记录 checked：无新 trading、payment、ledger、Treasury、investment-advice execution、banking connector 或 human approval 新证据。

### Product / Growth / Indie Founder

- `@mattpocockuk` 的 tactical vs strategic programming 是 AI coding 对 junior engineer skill formation 的 direct-x 线索；它有观察价值，但不等同于课程、公司政策或行业数据。
- `@marclou`、`@levelsio`、`@corbin_braun`、`@Hesamation` 等继续提供 indie/product/job-market pulse；本日报只保留为 product/indie 背景，不上升为可验证市场结论。

## GitHub Trending / Daily Repos

本轮 GitHub Trending Daily 成功解析 10 个 repo，10/10 README 文件已写入目录。索引见 [`../raw/2026-05-21/github-trending.json`](../raw/2026-05-21/github-trending.json)，README 原文见 [`../raw/2026-05-21/github-trending-readmes/`](../raw/2026-05-21/github-trending-readmes/)。证据等级统一按 `secondary-source` 处理：它只能说明项目当天在 GitHub Trending 页面可见，不代表官方发布、质量背书或长期趋势。

- [`anthropics/claude-plugins-official`](https://github.com/anthropics/claude-plugins-official)：Anthropic-managed Claude Code plugin directory。README 能确认 internal/external plugin folders、`/plugin install {plugin-name}@claude-plugins-official`、Discover UI、plugin metadata、MCP config、commands、agents、skills 和 trust warning。今天值得记录，因为 plugin supply chain 进入 official distribution surface；边界是每个插件仍需单独审计。归档：[`../raw/2026-05-21/github-trending-readmes/anthropics__claude-plugins-official.md`](../raw/2026-05-21/github-trending-readmes/anthropics__claude-plugins-official.md)。
- [`colbymchenry/codegraph`](https://github.com/colbymchenry/codegraph)：local semantic code graph for Claude Code、Cursor、Codex 和 OpenCode。README 能确认 interactive installer、project init、pre-indexed symbol/call graph 和 benchmark claims；它解决的是 coding agent 反复 grep/read 带来的 token/tool-call 成本。边界是 savings claim 需要独立复现，索引 freshness 和 framework coverage 也要验证。归档：[`../raw/2026-05-21/github-trending-readmes/colbymchenry__codegraph.md`](../raw/2026-05-21/github-trending-readmes/colbymchenry__codegraph.md)。
- [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills)：一个 `CLAUDE.md` guidance file，把 coding-agent 常见失败压成 four principles：Think Before Coding、Simplicity First、Surgical Changes、Goal-Driven Execution。它值得记录是因为这类 behavior spec 正在被当成 agent quality layer；边界是它本身不是 runtime enforcement。归档：[`../raw/2026-05-21/github-trending-readmes/multica-ai__andrej-karpathy-skills.md`](../raw/2026-05-21/github-trending-readmes/multica-ai__andrej-karpathy-skills.md)。
- [`dotnet/skills`](https://github.com/dotnet/skills)：Microsoft/.NET team 的 curated agent skills 与 custom agents，覆盖 .NET build、data、diagnostics、upgrade、MAUI、AI、tests、ASP.NET 等方向，并支持 Copilot CLI、Claude Code、VS Code preview、Cursor。归档：[`../raw/2026-05-21/github-trending-readmes/dotnet__skills.md`](../raw/2026-05-21/github-trending-readmes/dotnet__skills.md)。
- [`obra/superpowers`](https://github.com/obra/superpowers)：agentic software development methodology。README 能确认它用 skills 强制需求澄清、design approval、implementation plan、TDD、subagent-driven-development、review 和 finish workflow；边界是 README 不能证明 runtime 强制执行。归档：[`../raw/2026-05-21/github-trending-readmes/obra__superpowers.md`](../raw/2026-05-21/github-trending-readmes/obra__superpowers.md)。
- [`HKUDS/CLI-Anything`](https://github.com/HKUDS/CLI-Anything)：把各类软件包装成 agent-native CLI harness。它解决 agent 操作复杂软件的接口层问题；风险是自动写入、credential、sandbox 和软件版本兼容性。归档：[`../raw/2026-05-21/github-trending-readmes/HKUDS__CLI-Anything.md`](../raw/2026-05-21/github-trending-readmes/HKUDS__CLI-Anything.md)。
- [`rmyndharis/OpenWA`](https://github.com/rmyndharis/OpenWA)：self-hosted WhatsApp API Gateway，含 REST API、多 session、webhooks、dashboard、API key auth、Swagger、bulk messaging、groups/channels、proxy、rate limiting、CIDR whitelist 和 audit logging；涉及平台政策、账号安全、bulk messaging 滥用和隐私风险。归档：[`../raw/2026-05-21/github-trending-readmes/rmyndharis__OpenWA.md`](../raw/2026-05-21/github-trending-readmes/rmyndharis__OpenWA.md)。
- [`ChromeDevTools/chrome-devtools-mcp`](https://github.com/ChromeDevTools/chrome-devtools-mcp)：Chrome DevTools for coding agents，提供 MCP server、Chrome/Puppeteer automation、network/console/screenshot/performance trace；风险是浏览器内容暴露、usage statistics 和 session 隔离。归档：[`../raw/2026-05-21/github-trending-readmes/ChromeDevTools__chrome-devtools-mcp.md`](../raw/2026-05-21/github-trending-readmes/ChromeDevTools__chrome-devtools-mcp.md)。
- [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch)：AI engineering curriculum，435 lessons、20 phases、四种语言、每课生成 prompt/skill/agent/MCP artifact；这是 education / skill-building discovery signal，不是 agent runtime release。归档：[`../raw/2026-05-21/github-trending-readmes/rohitg00__ai-engineering-from-scratch.md`](../raw/2026-05-21/github-trending-readmes/rohitg00__ai-engineering-from-scratch.md)。
- [`teng-lin/notebooklm-py`](https://github.com/teng-lin/notebooklm-py)：NotebookLM unofficial Python API、CLI 和 agent skill，支持 source import、research queries、artifact generation/download、Google Docs/Sheets export；README 明确使用 undocumented Google APIs，不能当稳定官方 API。归档：[`../raw/2026-05-21/github-trending-readmes/teng-lin__notebooklm-py.md`](../raw/2026-05-21/github-trending-readmes/teng-lin__notebooklm-py.md)。

## 来源证据表

| 信号 | 证据等级 | 来源 | URL | 本地归档 |
| --- | --- | --- | --- | --- |
| OpenAI 数学研究突破 | official-source | OpenAI Blog RSS/fulltext | https://openai.com/index/model-disproves-discrete-geometry-conjecture | [`../raw/2026-05-21/rss-fulltext/openai-blog/openai-blog-an-openai-model-has-disproved-a-central-conjecture-in-discrete-geometr-7f625f6663.autocli.md`](../raw/2026-05-21/rss-fulltext/openai-blog/openai-blog-an-openai-model-has-disproved-a-central-conjecture-in-discrete-geometr-7f625f6663.autocli.md) |
| Ramp engineers use Codex | official-source | OpenAI Blog RSS/fulltext | https://openai.com/index/ramp | [`../raw/2026-05-21/rss-fulltext/openai-blog/openai-blog-how-ramp-engineers-accelerate-code-review-with-codex-cb920945cf.autocli.md`](../raw/2026-05-21/rss-fulltext/openai-blog/openai-blog-how-ramp-engineers-accelerate-code-review-with-codex-cb920945cf.autocli.md) |
| Claude Code v2.1.146 | official-source | GitHub release Atom | https://github.com/anthropics/claude-code/releases/tag/v2.1.146 | [`../raw/2026-05-21/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.146-06b1d30886.atom.md`](../raw/2026-05-21/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.146-06b1d30886.atom.md) |
| Gemini Omni | official-source | Google DeepMind RSS/fulltext | https://deepmind.google/blog/introducing-gemini-omni/ | [`../raw/2026-05-21/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-gemini-omni-6ff85c3103.extracted.md`](../raw/2026-05-21/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-gemini-omni-6ff85c3103.extracted.md) |
| Direct X product/research signals | direct-x | `twitterapi.io` | multiple X URLs | [`../raw/2026-05-21/twitterapi-io-results.json`](../raw/2026-05-21/twitterapi-io-results.json) |
| Coding-agent substrate Trending set | secondary-source | GitHub Trending / README | multiple GitHub URLs | [`../raw/2026-05-21/github-trending-readmes/`](../raw/2026-05-21/github-trending-readmes/) |

## X/Twitter 覆盖说明

- 本次 X/Twitter 只使用 `twitterapi.io` 的 `GET https://api.twitterapi.io/twitter/user/last_tweets` read endpoint，`includeReplies=false`。
- `twitterapi.io` 顶层采集成功：27 个账号均 `ok`，没有 failed accounts。
- 本轮共保留 134 条 direct-x 原始条目。保留数较高的账号包括 `cellinlab` 20 条、`corbin_braun` 16 条、`levelsio` 14 条、`frxiaobei` 12 条、`Hesamation` 10 条、`marclou` 10 条、`rileybrown` 10 条、`steipete` 8 条。
- `karpathy`、`AnthropicAI`、`rryssf_`、`oviswang`、`Yangyixxxx`、`lidang`、`cnyzgkc`、`_LuoFuli` 请求成功但 kept_count 为 0；这表示 36 小时窗口和脚本过滤下没有保留条目，不等于账号没有更新。
- direct-x 内容包含个人观点、短评论、转发、产品线索和活动宣传；日报只把它们作为直接来源线索，不把个人观点写成官方事实。

## 运行结果与失败源

- RSS：31/31 成功；RSS fulltext 47 条尝试，47 条 ok、0 条 limited、0 条 failed。
- GitHub releases：7/7 release Atom feed 成功；GitHub REST API 状态为 `skipped`，脚本按设计使用 Atom feed。
- GitHub release fulltext：OpenAI Codex 1/5 ok、4/5 limited；Claude Code 5/5 ok。
- GitHub Trending：1/1 成功，解析 10 个每日热门 repo，10 个 README 文件已归档。
- 官方页面：4/4 ok，0 limited，0 failed。
- X/Twitter：`twitterapi.io` 顶层采集成功，27/27 accounts ok；没有使用 Exa fallback。

## 不确定性与待验证项

- 已确认边界：本日报覆盖 2026-05-21 raw 输出、[`../raw/2026-05-21/manifest.json`](../raw/2026-05-21/manifest.json)、[`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)；GitHub Trending 只覆盖 `https://github.com/trending?since=daily` 当前 HTML 中解析到的 10 个 repo，以及脚本归档的 README；X/Twitter 只覆盖 `twitterapi.io` 返回并被 36 小时窗口保留的 direct-x 条目。
- 未覆盖范围：没有抓取登录态网页、没有补采 X thread/context、没有复现 GitHub Trending repo、没有运行 `CodeGraph` / `Superpowers` / `CLI-Anything` / `OpenWA` / `notebooklm-py`，没有验证 OpenAI 数学证明细节，没有复现 Ramp 的 Codex workflow，也没有运行 Claude Code `v2.1.146`。
- 推断项：【推断得出】本日报把“frontier reasoning research、enterprise coding-agent adoption、agent skills/plugin supply chain、local code context index、browser/debugging tool surface”作为今天主线。依据是 OpenAI/Claude 一手材料与 GitHub Trending 同日出现；失效条件是后续可复现材料、release notes 或实际使用显示这些只是宣传、样例或不稳定 alpha。
- 待验证项：阅读 OpenAI 数学 companion paper 和外部数学家说明；复现 Claude Code `v2.1.146` 的 `/code-review`、AskUserQuestion、MCP pagination 和 background permission fixes；调研 Ramp/Codex 是否有更具体的权限、audit、PR comment quality、human review gate 和 incident safety 边界；复现 `CodeGraph` freshness 与 benchmark；审计 `ChromeDevTools MCP` 的 browser data exposure 和 usage-statistics defaults。

## 运行统计

- 新增条目：`seen_added=64`。
- 高信号条目：7 条。
- 失败来源：RSS failed 0 个；official page failed 0 个；twitterapi.io failed accounts 0 个。
- limited 来源：OpenAI Codex release fulltext limited 4 条；RSS fulltext limited 0 条。

## 完成审计

- 用户目标拆解：稳定来源采集、twitterapi.io direct-x 采集、状态更新、日报生成、enabled trends 检查、失败/limited 来源说明、输出路径汇总。
- 证据对应：raw JSON 写入 [`../raw/2026-05-21/`](../raw/2026-05-21/)，状态文件写入 [`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)，日报为当前文件。
- 状态同步：`update-state.py` 已生成 [`../raw/2026-05-21/manifest.json`](../raw/2026-05-21/manifest.json)，并更新 source health 与 seen。
- 来源边界：所有 X/Twitter 内容标为 `direct-x`，GitHub Trending 标为 `secondary-source`，官方 RSS/GitHub release/official pages 标为 `official-source`、official metadata 或 limited；未用 Exa fallback。
- Trend 检查：`memory-dream`、`financial-agents`、`forward-deployed-engineering` 均已检查；trend raw 归档见 [`../trend/raw/2026-05-21/`](../trend/raw/2026-05-21/)。
