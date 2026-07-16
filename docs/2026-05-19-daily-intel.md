# 2026-05-19 Daily Source Intelligence

## 采集范围

- 运行时间：2026-05-19 Asia/Shanghai，本轮写入 [`../raw/2026-05-19/`](../raw/2026-05-19/)。
- 稳定来源：RSS/Atom 31 个源，31 个成功；相关全文 47 条尝试，47 条 ok、0 条 limited、0 条 failed；GitHub releases 7 个源通过 Atom feed 成功；GitHub Trending 1 个源成功，解析 10 个每日热门 repo；official pages 4 个源成功、0 个 limited、0 个 failed。
- X/Twitter：通过 `twitterapi.io` read endpoint 采集，顶层状态进入 `partial`；27 个账号中 24 个 ok、3 个 failed，保留 125 条 direct-x 原始条目。
- 状态更新：[`../raw/2026-05-19/manifest.json`](../raw/2026-05-19/manifest.json)、[`../state/source-health.json`](../state/source-health.json)、[`../state/seen.json`](../state/seen.json) 已由 `update-state.py` 更新；本轮 `seen_added=50`，累计 846 条。
- 本次没有使用 Exa MCP、登录态浏览器、X/Twitter 账号凭证、写操作 endpoint、posting、liking、following 或 DM。
- 本地归档：[`../raw/2026-05-19/rss-items.json`](../raw/2026-05-19/rss-items.json)、[`../raw/2026-05-19/github-items.json`](../raw/2026-05-19/github-items.json)、[`../raw/2026-05-19/github-trending.json`](../raw/2026-05-19/github-trending.json)、[`../raw/2026-05-19/github-trending-readmes/`](../raw/2026-05-19/github-trending-readmes/)、[`../raw/2026-05-19/official-pages.json`](../raw/2026-05-19/official-pages.json)、[`../raw/2026-05-19/twitterapi-io-results.json`](../raw/2026-05-19/twitterapi-io-results.json)。

## 今日高信号

1. OpenAI 与 Dell 的 Codex enterprise partnership 是今天最强一手新增：Codex 要进入 hybrid/on-prem enterprise 环境，并连接 Dell AI Data Platform / Dell AI Factory，使 agent 更靠近企业内部 codebase、docs、business systems、operational knowledge 和 workflow。【有明确证据支撑 / official-source / fulltext-ok】证据见 [`openai-blog-openai-and-dell...autocli.md`](../raw/2026-05-19/rss-fulltext/openai-blog/openai-blog-openai-and-dell-partner-to-bring-codex-to-hybrid-and-on-premise-enterp-210c7a7c78.autocli.md#L8)、[`#L14`](../raw/2026-05-19/rss-fulltext/openai-blog/openai-blog-openai-and-dell-partner-to-bring-codex-to-hybrid-and-on-premise-enterp-210c7a7c78.autocli.md#L14) 和 [`#L16`](../raw/2026-05-19/rss-fulltext/openai-blog/openai-blog-openai-and-dell-partner-to-bring-codex-to-hybrid-and-on-premise-enterp-210c7a7c78.autocli.md#L16)。
2. Codex for business operations 把 coding-agent 形态继续推到 business artifacts：off-track brief、strategic initiative update、leadership decision packet、board/company progress update、scenario model。重点不是“写代码”，而是把 trackers、dashboards、docs、Slack、spreadsheets 和 executive asks 合成可 review 的工作草稿。【有明确证据支撑 / first-party-openai / fulltext-ok】证据见 [`openai-blog-how-business-operations...autocli.md`](../raw/2026-05-19/rss-fulltext/openai-blog/openai-blog-how-business-operations-teams-use-codex-b5b1610b25.autocli.md#L8) 到 [`#L12`](../raw/2026-05-19/rss-fulltext/openai-blog/openai-blog-how-business-operations-teams-use-codex-b5b1610b25.autocli.md#L12)。
3. OpenAI Codex `0.131.0` release 是今天 Codex repo 的 strongest first-party release body：TUI session controls、unified `@` mentions、plugin marketplace/share workflows、remote-control daemon/API、Python SDK、`codex doctor`、Windows sandbox hardening、permissions/root handling、app-server SQLite recovery、extension/tool internals 和 memories extension 都在同一 release body 里出现。【有明确证据支撑 / first-party-openai / release-fulltext-ok】证据见 [`openai-codex-0.131.0...atom.md`](../raw/2026-05-19/github-release-fulltext/openai-codex/openai-codex-0.131.0-46b684e571.atom.md#L7)。
4. Claude Code `v2.1.144` 是 runtime reliability / background agents / plugin supply-chain 的高密度修复：新增 `/resume` background sessions、plugin discover last-updated、session-local `/model`、API unreachable timeout、防 terminal corruption、macOS Full Disk Access background crash 修复、MCP paginated tools/list 修复、background/session/worktree/agent view 大量边界修复。【有明确证据支撑 / first-party-claude-code / release-fulltext-ok】证据见 [`anthropics-claude-code-v2.1.144...atom.md`](../raw/2026-05-19/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.144-d9e87694d0.atom.md#L7)。
5. Anthropic 官方 Claude Code plugin directory 上 GitHub Trending，README 明确它是 curated directory，并把 internal plugins、external plugins、`.claude-plugin/plugin.json`、`.mcp.json`、commands、agents、skills 作为标准结构；同时警告用户必须信任插件，因为 Anthropic 不能控制插件内 MCP servers、files 或 software 是否变化。【有明确证据支撑 / secondary-source + official repo README】证据见 [`anthropics__claude-plugins-official.md`](../raw/2026-05-19/github-trending-readmes/anthropics__claude-plugins-official.md#L1)、[`#L5`](../raw/2026-05-19/github-trending-readmes/anthropics__claude-plugins-official.md#L5) 和 [`#L30`](../raw/2026-05-19/github-trending-readmes/anthropics__claude-plugins-official.md#L30)。
6. `agentmemory`、`CodeGraph`、`rtk`、`Superpowers` 同日上榜，说明 coding agent 生态继续围绕 long-running state、code context index、token/tool-output compression、methodology plugins 聚合。它们都是 README/Trending discovery signal，价值在观察方向，不是质量证明。【有明确证据支撑 / secondary-source】
7. antirez 的 `Alternatives for the EDIT tool of LLM agents` 是今天最值得读的 agent-tool-design 文章：它把 current edit CAS、line number fragility、token-poor local inference、line tag/checksum edit 和 whole-file CRC32 tradeoff 讲清楚，正好击中 coding-agent edit tool 的可靠性与 token 成本问题。【有明确证据支撑 / secondary-source / fulltext-ok】证据见 [`antirez-alternatives...autocli.md`](../raw/2026-05-19/rss-fulltext/antirez/antirez-alternatives-for-the-edit-tool-of-llm-agents-a9be0014dd.autocli.md#L11) 到 [`#L13`](../raw/2026-05-19/rss-fulltext/antirez/antirez-alternatives-for-the-edit-tool-of-llm-agents-a9be0014dd.autocli.md#L13)，以及 [`#L41`](../raw/2026-05-19/rss-fulltext/antirez/antirez-alternatives-for-the-edit-tool-of-llm-agents-a9be0014dd.autocli.md#L41)。
8. direct-x 中 `@sama` 称 latest ChatGPT update 质量明显提升，`@AnthropicAI` 宣布收购 Stainless，`@mattpocockuk` 继续展示 `/grill-with-docs`、`/handoff`、feature-flag development with agents，`@rileybrown` 把 Codex/Claude Code 用在 marketing/content creation skills。它们是 direct-x 使用/发布线索，不是官方规格完整证据。【有明确证据支撑 / direct-x】

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS 今天 5/5 条按 `fulltext_policy: always` 读取并归档成功：Dell/Codex enterprise partnership、Malta ChatGPT Plus partnership、personal finance、Codex for sales teams、Codex for business operations。归档见 [`../raw/2026-05-19/rss-fulltext/openai-blog/`](../raw/2026-05-19/rss-fulltext/openai-blog/)。
- Dell/Codex enterprise partnership 是今天真正的新一手信号。它把 Codex 的部署面从 cloud SaaS/IDE 扩到 hybrid/on-prem enterprise environments，指向 governed data、business systems、internal context 和 repeatable enterprise agent workflows。
- Codex for business operations 与前几天的 finance/sales/data science materials 合起来，说明 OpenAI 正把 Codex 从 coding agent 包装成 cross-functional work artifact agent。今天的边界是：这些页面给出 use-case prompts 和 review workflow，不等于已经证明每个公司可生产部署。
- OpenAI Codex GitHub release Atom 读取 5 条，其中 `0.131.0` release fulltext ok，其余 4 条 alpha release fulltext limited；报告只对 `0.131.0` 的 release body 写具体变更。
- Claude Code GitHub release Atom 读取 `v2.1.144` 到 `v2.1.140`，5/5 release fulltext ok；今天高价值集中在 `v2.1.144` 的 background sessions、plugin browsing、MCP pagination、headless Skill、worktree/background guard 和 terminal reliability。

## 按主题分组摘要

### AI Coding / Developer Tools

- Codex + Dell 是今天的主线：coding agent 正在进入 hybrid/on-prem enterprise 环境，核心不是把模型搬进机房，而是让 agent 接近企业 data platform、codebase、docs、business systems 和 operational workflow。
- Codex `0.131.0` release body 表明 Codex 自身也在补 runtime 基础设施：plugin marketplace、remote-control daemon、Python SDK、doctor diagnostics、Windows sandbox、permissions、SQLite recovery、extension/tool internals 和 memory extension。
- Claude Code `v2.1.144` 把背景任务和 plugin runtime 的实际边界补得很密：background session resume、agent view、Full Disk Access、MCP pagination、headless Skill、plugin install hints、worktree isolation guard、terminal corruption。这些都说明 coding-agent 产品战线已经从“能写代码”转到“能长期跑、可恢复、可安装、可诊断”。
- antirez 的 edit-tool 文章是小而硬的机制信号：coding agent 的 patch primitive 仍在寻找 token 成本、并发编辑冲突、line drift 和 hallucinated old-text 之间的平衡。

### AI Agent / Agentic Workflow

- GitHub Trending 今日强烈偏 agent runtime / agent workflow：`agentmemory` 处理 persistent memory，`CodeGraph` 处理 local code knowledge graph，`rtk` 处理 command-output compression，`Superpowers` 把 workflow methodology 做成 skills/plugin，`claude-plugins-official` 把 Claude Code plugin directory 官方化。
- `agentmemory` README 记录 hooks/MCP/REST/API、多 agent 共享 server、confidence/lifecycle/knowledge graph/hybrid search 等主张；这是 Memory & Dream 的强 discovery signal，但仍要复现权限隔离、删除治理和污染防护。
- `CodeGraph` README 记录 pre-indexed knowledge graph、symbol relationships、call graphs、FTS5、impact analysis、file watcher、19+ languages、100% local SQLite；这是 coding-agent context layer，不是传统 memory item。
- `rtk` README 记录 hook/plugin rewrite Bash commands，把 `git status`、`cat`、`rg`、test output 等压缩后再给 agent；它对应的是 tool-result hygiene 和 token budget，不是模型能力更新。

### LLM / Frontier Models

- Simon Willison 的 PyCon 5-minute LLM recap 把过去半年总结为两条：coding agents got good，以及 laptop-available models 开始超出预期；这是 secondary/analysis source，但可作为 practitioner framing 线索。证据见 [`simonwillison-the-last-six-months...extracted.md`](../raw/2026-05-19/rss-fulltext/simonwillison/simonwillison-the-last-six-months-in-llms-in-five-minutes-1c555495cd.extracted.md#L1)。
- Hugging Face `Granite Embedding Multilingual R2` 与 DeepMind `AlphaEvolve` 今天都有 fulltext-ok 归档，但它们不是本轮最高优先级。日报只记录其存在，不把它们拔高为今天主线。
- direct-x 中 `@sama` 对 latest ChatGPT update 的评价和 Qwen3.7 Preview 转发都是实时线索；没有配套官方 release note 时，只能作为观察入口。

### Forward Deployed Engineering / Enterprise AI

- Dell/Codex partnership 是 FDE/enterprise AI 今日最强证据：Codex 要贴近 on-prem governed data、internal systems 和 existing workflows，这比“AI coding tool”更接近 enterprise deployment substrate。
- Codex for business operations 把 agent 放入 initiative health、decision packet、board/company update 和 scenario model 等运营工作流；这不是客户现场 FDE，但它回答同一个落地问题：企业里哪些 high-context artifacts 可以被 agent 先生成，再由人 review。
- Malta partnership 和 personal finance 是前几天延续信号；今天没有比 Dell/Codex 更强的新 public-sector/finance deployment fact。

### Financial Agents

- OpenAI personal finance 全文今天再次 fulltext-ok，但功能事实与 2026-05-17/18 基本一致：connected accounts、Plaid、Financial memories、temporary chat 不访问 connected financial accounts、disconnect 后 30 天删除同步账户数据、不是 professional financial advice replacement。
- 今天没有新的 trading、payment、ledger posting、broker execution 或 Treasury action surface 高信号；Financial Agents trend 只记录 checked，不强行提升新结论。

### Product / Growth / Indie Founder

- `@levelsio`、`@marclou`、`@gregisenberg`、`@jackfriks` 今天给出 bootstrapped ARR、startup opportunities、traffic source、solo founder workflow 等 direct-x 线索；保留为 product/indie pulse，不写成可验证市场结论。
- `@rileybrown` 的 Codex/Claude Code marketing/content skills 是更贴近本项目的线索：coding-agent harness 正被用于内容研究、second brain、diagrams、subagents、design、Remotion/media、email 和 social media workflows。

## GitHub Trending / Daily Repos

本轮 GitHub Trending Daily 成功解析 10 个 repo，10/10 README 文件已写入目录。索引见 [`../raw/2026-05-19/github-trending.json`](../raw/2026-05-19/github-trending.json)，README 原文见 [`../raw/2026-05-19/github-trending-readmes/`](../raw/2026-05-19/github-trending-readmes/)。证据等级统一按 `secondary-source` 处理：它只能说明项目当天在 GitHub Trending 页面可见，不代表官方发布、质量背书或长期趋势。

- [`tinyhumansai/openhuman`](https://github.com/tinyhumansai/openhuman)：personal AI assistant / desktop agent。README 能确认 118+ integrations、one-click OAuth、20 分钟 auto-fetch、Memory Tree、SQLite、Obsidian-compatible vault 和 optional `agentmemory` backend。今天值得记录，因为它继续代表 personal context auto-fetch 与本地 memory vault；风险是 OAuth scope、后台同步、删除治理和敏感数据进入长期记忆。归档：[`../raw/2026-05-19/github-trending-readmes/tinyhumansai__openhuman.md`](../raw/2026-05-19/github-trending-readmes/tinyhumansai__openhuman.md)。
- [`HKUDS/CLI-Anything`](https://github.com/HKUDS/CLI-Anything)：把软件包装成 agent-native CLI harness。README 记录 CLI-Hub、generated CLIs、preview/live preview/trajectory loops 和多类软件 demo。它解决的是 agent 如何稳定操作原本面向人的软件；边界是 side effect、sandbox、credential、真实软件版本兼容性和测试覆盖。归档：[`../raw/2026-05-19/github-trending-readmes/HKUDS__CLI-Anything.md`](../raw/2026-05-19/github-trending-readmes/HKUDS__CLI-Anything.md)。
- [`Imbad0202/academic-research-skills`](https://github.com/Imbad0202/academic-research-skills)：Claude Code academic research skills，面向 research、write、review、revise、finalize。它属于 domain workflow skills，价值在把研究流程包装成可安装技能；风险是引用准确性、学术诚信和 provenance。归档：[`../raw/2026-05-19/github-trending-readmes/Imbad0202__academic-research-skills.md`](../raw/2026-05-19/github-trending-readmes/Imbad0202__academic-research-skills.md)。
- [`obra/superpowers`](https://github.com/obra/superpowers)：agentic skills framework 与 software development methodology。README 能确认它把 brainstorming、design approval、implementation plan、subagent-driven development、TDD、review 和 finishing branch 做成自动触发 workflow，并支持 Claude Code、Codex CLI/App、Gemini、OpenCode、Cursor 等 harness。边界是 README 不能证明这些 rules 在所有 agent/runtime 中强制执行。归档：[`../raw/2026-05-19/github-trending-readmes/obra__superpowers.md`](../raw/2026-05-19/github-trending-readmes/obra__superpowers.md)。
- [`anthropics/claude-plugins-official`](https://github.com/anthropics/claude-plugins-official)：Anthropic-managed Claude Code plugin directory。README 确认 internal/external plugin structure、plugin install command、Discover UI、plugin metadata、MCP config、commands、agents、skills，也明确提示插件信任风险。它是 plugin supply chain 进入官方 distribution surface 的信号。归档：[`../raw/2026-05-19/github-trending-readmes/anthropics__claude-plugins-official.md`](../raw/2026-05-19/github-trending-readmes/anthropics__claude-plugins-official.md)。
- [`rohitg00/agentmemory`](https://github.com/rohitg00/agentmemory)：persistent memory for AI coding agents。README 记录 Claude Code、Codex CLI、Cursor、Gemini CLI、OpenCode 等支持 hooks/MCP/REST/API，共享同一 memory server，并宣称 confidence scoring、lifecycle、knowledge graphs、hybrid search。它是 Memory & Dream 主线，但需要复现权限、删除、污染和跨项目隔离。归档：[`../raw/2026-05-19/github-trending-readmes/rohitg00__agentmemory.md`](../raw/2026-05-19/github-trending-readmes/rohitg00__agentmemory.md)。
- [`CloakHQ/CloakBrowser`](https://github.com/CloakHQ/CloakBrowser)：stealth Chromium / Playwright replacement。README 声称 source-level fingerprint patches 和 bot detection tests；这是浏览器自动化与反检测高风险信号，必须标注 ToS、平台反滥用、凭据和安全边界，不进入正常 agent tooling 推荐。归档：[`../raw/2026-05-19/github-trending-readmes/CloakHQ__CloakBrowser.md`](../raw/2026-05-19/github-trending-readmes/CloakHQ__CloakBrowser.md)。
- [`rtk-ai/rtk`](https://github.com/rtk-ai/rtk)：Rust Token Killer，CLI proxy / hook layer，压缩 shell command output 后再给 agent。README 记录 60-90% token reduction claims、100+ commands、Bash hook rewrite、Claude Code/Codex/Gemini/Cursor 等 target。它解决的是 tool output hygiene；风险是压缩是否隐藏关键错误、hook 是否改变命令语义。归档：[`../raw/2026-05-19/github-trending-readmes/rtk-ai__rtk.md`](../raw/2026-05-19/github-trending-readmes/rtk-ai__rtk.md)。
- [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents)：把 frontend、Reddit/community、reality check、content/marketing 等角色打包成一组 specialized agents。它是 agency-style agent pack 的 discovery signal；README 不能证明实际交付质量或账号/平台安全。归档：[`../raw/2026-05-19/github-trending-readmes/msitarzewski__agency-agents.md`](../raw/2026-05-19/github-trending-readmes/msitarzewski__agency-agents.md)。
- [`colbymchenry/codegraph`](https://github.com/colbymchenry/codegraph)：local semantic code graph for Claude Code、Cursor、Codex、OpenCode。README 记录 pre-indexed knowledge graph、symbol/call graph、FTS5、impact analysis、file watcher、framework-aware routes、100% local SQLite。它是 coding-agent context index 的强 discovery signal；边界是 benchmark/quality claims 需复现，源码变化后 freshness 也要验证。归档：[`../raw/2026-05-19/github-trending-readmes/colbymchenry__codegraph.md`](../raw/2026-05-19/github-trending-readmes/colbymchenry__codegraph.md)。

## 来源证据表

| 信号 | 证据等级 | 来源 | URL | 本地归档 |
| --- | --- | --- | --- | --- |
| Dell/Codex enterprise partnership | official-source | OpenAI Blog RSS/fulltext | https://openai.com/index/dell-codex-enterprise-partnership | [`../raw/2026-05-19/rss-fulltext/openai-blog/openai-blog-openai-and-dell-partner-to-bring-codex-to-hybrid-and-on-premise-enterp-210c7a7c78.autocli.md`](../raw/2026-05-19/rss-fulltext/openai-blog/openai-blog-openai-and-dell-partner-to-bring-codex-to-hybrid-and-on-premise-enterp-210c7a7c78.autocli.md) |
| Codex for business operations | official-source | OpenAI Academy | https://openai.com/academy/codex-for-work/how-business-operations-teams-use-codex | [`../raw/2026-05-19/rss-fulltext/openai-blog/openai-blog-how-business-operations-teams-use-codex-b5b1610b25.autocli.md`](../raw/2026-05-19/rss-fulltext/openai-blog/openai-blog-how-business-operations-teams-use-codex-b5b1610b25.autocli.md) |
| OpenAI Codex 0.131.0 | official-source | GitHub release Atom | https://github.com/openai/codex/releases/tag/rust-v0.131.0 | [`../raw/2026-05-19/github-release-fulltext/openai-codex/openai-codex-0.131.0-46b684e571.atom.md`](../raw/2026-05-19/github-release-fulltext/openai-codex/openai-codex-0.131.0-46b684e571.atom.md) |
| Claude Code v2.1.144 | official-source | GitHub release Atom | https://github.com/anthropics/claude-code/releases/tag/v2.1.144 | [`../raw/2026-05-19/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.144-d9e87694d0.atom.md`](../raw/2026-05-19/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.144-d9e87694d0.atom.md) |
| Agent runtime Trending set | secondary-source | GitHub Trending / README | multiple GitHub URLs | [`../raw/2026-05-19/github-trending-readmes/`](../raw/2026-05-19/github-trending-readmes/) |
| EDIT tool alternatives | secondary-source | antirez RSS/fulltext | https://antirez.com/news/166 | [`../raw/2026-05-19/rss-fulltext/antirez/antirez-alternatives-for-the-edit-tool-of-llm-agents-a9be0014dd.autocli.md`](../raw/2026-05-19/rss-fulltext/antirez/antirez-alternatives-for-the-edit-tool-of-llm-agents-a9be0014dd.autocli.md) |
| Direct X usage and product signals | direct-x | `twitterapi.io` | multiple X URLs | [`../raw/2026-05-19/twitterapi-io-results.json`](../raw/2026-05-19/twitterapi-io-results.json) |

## X/Twitter 覆盖说明

- 本次 X/Twitter 只使用 `twitterapi.io` 的 `GET https://api.twitterapi.io/twitter/user/last_tweets` read endpoint，`includeReplies=false`。
- `twitterapi.io` 顶层采集成功，但 state 标为 `partial`：27 个账号处理完成，24 个账号 `ok`，`frxiaobei`、`oviswang`、`Yangyixxxx` 三个账号 `failed`。这些失败只表示 API 覆盖失败，不代表账号没有更新。
- 本轮共保留 125 条 direct-x 原始条目。保留数较高的账号包括 `levelsio` 20 条、`cellinlab` 19 条、`Hesamation` 14 条、`rileybrown` 12 条、`marclou` 10 条、`mattpocockuk` 8 条、`steipete` 8 条。
- `karpathy`、`OpenAI`、`simonw`、`rryssf_`、`genspark_ai`、`lidang`、`cnyzgkc`、`_LuoFuli` 请求成功但 kept_count 为 0；这表示 36 小时窗口和脚本过滤下没有保留条目，不等于账号没有更新。
- direct-x 内容包含个人观点、短评论、转发、产品线索和活动宣传；日报只把它们作为直接来源线索，不把个人观点写成官方事实。

## 运行结果与失败源

- RSS：31/31 成功；相关全文 47 条尝试，47 条 ok、0 条 limited、0 条 failed。
- GitHub releases：7/7 release Atom feed 成功；GitHub REST API 状态为 `skipped`，脚本按设计使用 Atom feed。
- GitHub release fulltext：Claude Code 5/5 ok；OpenAI Codex 1/5 ok、4/5 limited，因此只对 `0.131.0` 细写 release body。
- GitHub Trending：1/1 成功，解析 10 个每日热门 repo，10 个 README 文件已归档。
- 官方页面：4/4 ok，0 limited，0 failed；Claude Blog 返回 5 个近期 blog metadata。
- X/Twitter：`twitterapi.io` 顶层采集成功但覆盖 partial；failed accounts 为 `frxiaobei`、`oviswang`、`Yangyixxxx`；没有使用 Exa fallback。

## 不确定性与待验证项

- 已确认边界：本日报覆盖 2026-05-19 raw 输出、[`../raw/2026-05-19/manifest.json`](../raw/2026-05-19/manifest.json)、[`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)；GitHub Trending 只覆盖 `https://github.com/trending?since=daily` 当前 HTML 中解析到的 10 个 repo，以及脚本归档的 README；X/Twitter 只覆盖 `twitterapi.io` 返回并被 36 小时窗口保留的 direct-x 条目。
- 未覆盖范围：没有抓取登录态网页、没有补采 X thread/context、没有浏览器渲染 official pages、没有复现 GitHub Trending repo、没有运行 OpenHuman/agentmemory/CodeGraph/rtk/Superpowers、没有验证 Dell/Codex partnership 的实际部署形态、没有检查 Codex/Claude Code release 的运行行为。
- 推断项：【推断得出】本日报把“enterprise/on-prem Codex、agent runtime reliability、plugin/skills supply chain、memory/index/compression layer”作为今天主线。依据是 OpenAI/Dell fulltext、OpenAI Codex release body、Claude Code release body、GitHub Trending README 和 direct-x 同日出现；失效条件是后续产品文档、源码或真实运行显示这些只是 marketing framing、demo 项目或不可复现实现。
- 待验证项：查 Dell AI Data Platform / AI Factory 与 Codex 的实际部署文档、security boundary、data governance、customer availability；复现 Codex `0.131.0` 的 plugin/remote/Python SDK/doctor 功能；检查 Claude Code `v2.1.144` 的 background session resume、MCP pagination 和 Full Disk Access 修复；运行 agentmemory/CodeGraph/rtk/Superpowers 的最小样例，验证权限、删除、freshness、hook side effect 和压缩失真。

## 运行统计

- 新增条目：`seen_added=50`。
- 高信号条目：8 条。
- 失败来源：RSS failed 0 个；official page failed 0 个；twitterapi.io failed accounts 3 个。
- limited 来源：OpenAI Codex release fulltext limited 4 条；RSS fulltext limited 0 条。

## 完成审计

- 用户目标拆解：稳定来源采集、twitterapi.io direct-x 采集、状态更新、日报生成、enabled trends 检查、失败/limited 来源说明、输出路径汇总。
- 证据对应：raw JSON 写入 [`../raw/2026-05-19/`](../raw/2026-05-19/)，状态文件写入 [`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)，日报为当前文件。
- 状态同步：`update-state.py` 已生成 [`../raw/2026-05-19/manifest.json`](../raw/2026-05-19/manifest.json)，并更新 source health 与 seen。
- 来源边界：所有 X/Twitter 内容标为 `direct-x`，GitHub Trending 标为 `secondary-source`，官方 RSS/GitHub release/official pages 标为 `official-source`、official metadata 或 limited；未用 Exa fallback。
- Trend 检查：`memory-dream`、`financial-agents`、`forward-deployed-engineering` 均已检查；trend raw 归档见 [`../trend/raw/2026-05-19/`](../trend/raw/2026-05-19/)。
