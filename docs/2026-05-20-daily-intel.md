# 2026-05-20 Daily Source Intelligence

## 采集范围

- 运行时间：2026-05-20 Asia/Shanghai，本轮写入 [`../raw/2026-05-20/`](../raw/2026-05-20/)。
- 稳定来源：RSS/Atom 31 个源，30 个成功、1 个失败；相关全文 48 条尝试，48 条 ok、0 条 limited、0 条 failed；GitHub releases 7 个源成功；GitHub Trending 1 个源成功，解析 10 个每日热门 repo；official pages 4 个源成功、0 个 limited。
- X/Twitter：通过 `twitterapi.io` read endpoint 采集，顶层状态 `ok`；27 个账号全部 ok，保留 144 条 direct-x 原始条目。
- 状态更新：[`../raw/2026-05-20/manifest.json`](../raw/2026-05-20/manifest.json)、[`../state/source-health.json`](../state/source-health.json)、[`../state/seen.json`](../state/seen.json) 已由 `update-state.py` 更新；本轮 `seen_added=46`，累计 892 条。
- 本次没有使用 Exa MCP、登录态浏览器、X/Twitter 账号凭证、写操作 endpoint、posting、liking、following 或 DM。
- 本地归档：[`../raw/2026-05-20/rss-items.json`](../raw/2026-05-20/rss-items.json)、[`../raw/2026-05-20/github-items.json`](../raw/2026-05-20/github-items.json)、[`../raw/2026-05-20/github-trending.json`](../raw/2026-05-20/github-trending.json)、[`../raw/2026-05-20/github-trending-readmes/`](../raw/2026-05-20/github-trending-readmes/)、[`../raw/2026-05-20/official-pages.json`](../raw/2026-05-20/official-pages.json)、[`../raw/2026-05-20/twitterapi-io-results.json`](../raw/2026-05-20/twitterapi-io-results.json)。

## 今日高信号

1. OpenAI for Singapore 是今天最强 FDE / enterprise AI 一手信号：OpenAI 与 MDDI 合作，承诺超过 S$300M，建立美国以外首个 Applied AI Lab，并明确把 Singapore 做成 Forward-Deployed Engineers global hub。【有明确证据支撑 / official-source / fulltext-ok】证据见 [`openai-singapore`](../raw/2026-05-20/rss-fulltext/openai-blog/openai-blog-introducing-openai-for-singapore-e0640ad032.autocli.md#L12)、[`#L24`](../raw/2026-05-20/rss-fulltext/openai-blog/openai-blog-introducing-openai-for-singapore-e0640ad032.autocli.md#L24) 和 [`#L44`](../raw/2026-05-20/rss-fulltext/openai-blog/openai-blog-introducing-openai-for-singapore-e0640ad032.autocli.md#L44)。
2. OpenAI provenance 更新把 C2PA、Google SynthID 和 public verifier 组合起来：重点不是单个水印，而是标准元数据、鲁棒水印和公众验证三层互补。【有明确证据支撑 / official-source / fulltext-ok】证据见 [`content provenance`](../raw/2026-05-20/rss-fulltext/openai-blog/openai-blog-advancing-content-provenance-for-a-safer-more-transparent-ai-ecosystem-4f14311644.autocli.md#L10)、[`#L24`](../raw/2026-05-20/rss-fulltext/openai-blog/openai-blog-advancing-content-provenance-for-a-safer-more-transparent-ai-ecosystem-4f14311644.autocli.md#L24) 和 [`#L28`](../raw/2026-05-20/rss-fulltext/openai-blog/openai-blog-advancing-content-provenance-for-a-safer-more-transparent-ai-ecosystem-4f14311644.autocli.md#L28)。
3. OpenAI Codex `0.132.0` 是 today first-party coding-agent runtime release：Python SDK first-class auth、text-only turn API、`codex exec resume --output-schema`、remote executor auth-backed registration、websocket keepalive、multi-session TUI fixes 和 versioned memory summaries 都在同一 release body 中出现。【有明确证据支撑 / first-party-openai / release-fulltext-ok】证据见 [`openai-codex-0.132.0`](../raw/2026-05-20/github-release-fulltext/openai-codex/openai-codex-0.132.0-df87a5dff8.atom.md#L7)。
4. Claude Code `v2.1.145` 继续把 long-running agent runtime 做得更可观测、可脚本化、可诊断：`claude agents --json`、OTEL `agent_id`/`parent_agent_id`、plugin pre-install surface、background task fields、permission-prompt bypass fix、skill fork infinite-loop fix 和 Read partial view 都值得记录。【有明确证据支撑 / first-party-claude-code / release-fulltext-ok】证据见 [`claude-code-v2.1.145`](../raw/2026-05-20/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.145-5eddeb758d.atom.md#L7)。
5. Google Gemini Omni 是 multimodal generation 的一手 release：Google 把 Gemini reasoning 与 video generation/editing 合在一起，首个模型 Gemini Omni Flash 进入 Gemini app、Google Flow 和 YouTube Shorts，并计划后续 API / enterprise rollout。【有明确证据支撑 / official-source / fulltext-ok】证据见 [`gemini-omni`](../raw/2026-05-20/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-gemini-omni-6ff85c3103.extracted.md#L1)。
6. Gemini for Science 把 agentic science workflow 产品化：Hypothesis Generation、Computational Discovery、Literature Insights 和 Science Skills 连接 Co-Scientist、AlphaEvolve、ERA、NotebookLM、Google Antigravity 与 30+ life science databases。【有明确证据支撑 / official-source / fulltext-ok】证据见 [`gemini-for-science`](../raw/2026-05-20/rss-fulltext/google-deepmind-blog/google-deepmind-blog-gemini-for-science-ai-experiments-and-tools-for-a-new-era-of-discovery-548bdf100a.extracted.md#L1)。
7. direct-x 中 `@karpathy` 宣布加入 Anthropic，`@OpenAI` 发布 Guaranteed Capacity 和 content provenance，`@sama` 解释 capacity certainty 与 YC token credits。这些是高价值实时线索，但 release/spec 仍要回到官方页面或后续文档确认。【有明确证据支撑 / direct-x】证据见 [`twitterapi-io-results.json`](../raw/2026-05-20/twitterapi-io-results.json)。
8. GitHub Trending 仍集中在 agent runtime substrate：`agentmemory`、`CodeGraph`、`rtk`、`Superpowers`、`claude-plugins-official`、`OpenHuman` 连续出现。今天不是新项目首发，但它强化了 memory server、local code graph、tool-output compression、methodology skills、plugin supply chain 的同一条主线。【有明确证据支撑 / secondary-source】

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS 今天 5/5 条按 `fulltext_policy: always` 读取并归档成功：OpenAI for Singapore、content provenance、Dell/Codex、Malta partnership、Databricks GPT-5.5。归档见 [`../raw/2026-05-20/rss-fulltext/openai-blog/`](../raw/2026-05-20/rss-fulltext/openai-blog/)。
- OpenAI for Singapore 是今天新增最强一手主线：它把 national AI strategy、Applied AI Lab、本地 FDE roles、FDE training、public service / finance / healthcare / digital infrastructure 和 SME/startup adoption 放在同一 deployment package 中。
- Content provenance 是安全与平台信任主线：C2PA metadata 负责携带上下文，SynthID 负责更耐受的图像水印，public verifier 负责帮助用户检测 OpenAI 生成内容；边界是工具初期只覆盖 OpenAI 生成内容，并且检测不到特征时不会断言非 AI。
- OpenAI Codex GitHub release Atom 读取 5 条，其中 `0.132.0` 与 `0.131.0` fulltext ok，三个 alpha release limited；本日报只细写 `0.132.0` 的新增 runtime 能力。
- Claude Code GitHub release Atom 读取 `v2.1.145` 到 `v2.1.141`，5/5 release fulltext ok；今天高价值集中在 `v2.1.145` 的 live session JSON、OTEL agent spans、plugin pre-install visibility、hook input、security fix 和 token-limit Read 行为。

## 按主题分组摘要

### AI Coding / Developer Tools

- Codex `0.132.0` 把 automation/session continuity 和 SDK 可用性往前推：Python SDK auth、plain-string turn input、handle `TurnResult`、`exec resume --output-schema`、remote executor registration、websocket keepalive 和 versioned memory summaries 都是长任务自动化会用到的底层能力。
- Claude Code `v2.1.145` 更像 operational hardening：`claude agents --json` 让 live sessions 可被 tmux/status bars/session pickers 消费；OTEL agent span parent 修复让 background subagent tracing 更可信；plugin browse 前显示 commands/agents/skills/hooks/MCP/LSP servers 能降低安装前盲区。
- Google Gemini 3.5 Flash 由 Simon Willison 细读后指出：Google 计划把它用于 Gemini app、Search AI Mode、Antigravity、Gemini API、Android Studio 和 enterprise agent platforms，但价格相比前代 Flash 明显上升。这是 secondary analysis，不替代官方 spec。证据见 [`simonwillison-gemini-3.5-flash`](../raw/2026-05-20/rss-fulltext/simonwillison/simonwillison-gemini-3.5-flash-more-expensive-but-google-plan-to-use-it-for-everythi-b49356edd1.extracted.md#L1)。

### AI Agent / Agentic Workflow

- Gemini Omni 和 Gemini for Science 分别代表生成侧与科研 workflow 侧的 agentic expansion：前者把多模态输入、视频生成、对话式编辑和 digital avatar 放进一个 Omni family；后者把假设生成、并行计算实验、文献结构化、Science Skills 和 Antigravity 连接起来。
- GitHub Trending 延续昨天的 agent runtime set：`agentmemory` 作为 shared memory server，`CodeGraph` 作为 local semantic code index，`rtk` 作为 command-output compression，`Superpowers` 作为 methodology skills，`claude-plugins-official` 作为官方 plugin directory。它们都是 discovery signal，不是质量背书。
- direct-x 中 `@mattpocockuk` 继续围绕 `/grill-with-docs`、agent adversarial review 和 skill workflow 发声，说明 skills/rules 正在被当成 agent 质量控制界面；这仍是个人使用线索，不是标准 API。

### LLM / Frontier Models

- Gemini Omni 与 Gemini for Science 是今天 Google 官方侧最强 LLM/product signal。Omni 关注 video creation/editing，Science 关注 research-agent workflow；二者共同指向“model capability + tool/workflow surface”合并。
- `@karpathy` 加入 Anthropic 是 direct-x 高信号，影响更多在人才与研究方向观察上；它不能单独说明 Anthropic 产品路线变化。
- OpenAI Guaranteed Capacity 在 X 上由 `@OpenAI` 与 `@sama` 同日说明，是 capacity certainty / long-term token commit 的实时线索；日报标为 direct-x，后续应等官方商业文档或 API/contract 页面确认细节。

### Forward Deployed Engineering / Enterprise AI

- OpenAI for Singapore 是今天 FDE 主线：Applied AI Lab、200+ Singapore-based technical roles、Forward-Deployed Engineers hub、FDE training programme、public service / finance / healthcare / digital infrastructure 都在官方正文中出现。
- Dell/Codex partnership 继续强化昨天判断：Codex 的 enterprise path 正围绕 governed data、hybrid/on-prem infrastructure、business systems、systems of record 和 repeatable workflows 展开。
- Guaranteed Capacity 与 YC token credits 是 capacity-market 线索：如果 models 继续变好且需求受限于 compute，enterprise adoption 会越来越依赖容量确定性、长期承诺和成本治理；但今天只有 direct-x 证据。

### Financial Agents

- 今天没有新的 financial agent action surface。OpenAI for Singapore 提到 finance 是 Applied AI Lab 支持方向之一，但没有给出金融 workflow、connector、approval、交易、账务或 advice 边界细节。
- 因此 Financial Agents trend 今天只记录 checked：无新 trading、payment、ledger、Treasury、investment-advice execution 或 human approval 新证据。

### Product / Growth / Indie Founder

- `@sama` 的 tokenmaxxing startups / YC token credits 是创业成本结构线索：token budget 可能从 API 成本变成 founder workflow 和 product design 的显性资源。
- `@levelsio`、`@marclou`、`@jackfriks`、`@gregisenberg` 继续提供 bootstrapped distribution、startup acquisition、outage handling 和 AI product ideation 的 direct-x pulse；本日报只保留为 product/indie 线索，不上升为可验证市场结论。

## GitHub Trending / Daily Repos

本轮 GitHub Trending Daily 成功解析 10 个 repo，10/10 README 文件已写入目录。索引见 [`../raw/2026-05-20/github-trending.json`](../raw/2026-05-20/github-trending.json)，README 原文见 [`../raw/2026-05-20/github-trending-readmes/`](../raw/2026-05-20/github-trending-readmes/)。证据等级统一按 `secondary-source` 处理：它只能说明项目当天在 GitHub Trending 页面可见，不代表官方发布、质量背书或长期趋势。

- [`tinyhumansai/openhuman`](https://github.com/tinyhumansai/openhuman)：personal AI assistant / desktop agent。README 能确认 UI-first desktop assistant、Google Meet 参与、跨周记忆、118+ integrations、Memory Tree、SQLite 和 optional `agentmemory` backend。今天值得记录，因为它继续代表 personal context auto-fetch 与本地 memory vault；风险是 OAuth scope、后台同步、删除治理和敏感数据长期记忆。归档：[`../raw/2026-05-20/github-trending-readmes/tinyhumansai__openhuman.md`](../raw/2026-05-20/github-trending-readmes/tinyhumansai__openhuman.md)。
- [`HKUDS/CLI-Anything`](https://github.com/HKUDS/CLI-Anything)：把软件包装成 agent-native CLI harness。README 记录 CLI-Hub、generated CLIs、preview/live preview/trajectory loops 和多类软件 demo。它解决的是 agent 如何稳定操作原本面向人的软件；边界是 side effect、sandbox、credential、真实软件版本兼容性和测试覆盖。归档：[`../raw/2026-05-20/github-trending-readmes/HKUDS__CLI-Anything.md`](../raw/2026-05-20/github-trending-readmes/HKUDS__CLI-Anything.md)。
- [`Imbad0202/academic-research-skills`](https://github.com/Imbad0202/academic-research-skills)：Claude Code academic research skills，面向 research、write、review、revise、finalize。它把文献查找、引用格式、数据验证和逻辑一致性做成 workflow skills；风险是 citation accuracy、academic integrity 和 provenance。归档：[`../raw/2026-05-20/github-trending-readmes/Imbad0202__academic-research-skills.md`](../raw/2026-05-20/github-trending-readmes/Imbad0202__academic-research-skills.md)。
- [`obra/superpowers`](https://github.com/obra/superpowers)：agentic skills framework 与 software development methodology。README 能确认它把需求澄清、design approval、implementation plan、subagent-driven development、TDD、review 和 branch finish 做成 skills workflow，并支持 Claude Code、Codex CLI/App、Gemini、OpenCode、Cursor 等 harness。边界是 README 不能证明 runtime 强制执行。归档：[`../raw/2026-05-20/github-trending-readmes/obra__superpowers.md`](../raw/2026-05-20/github-trending-readmes/obra__superpowers.md)。
- [`anthropics/claude-plugins-official`](https://github.com/anthropics/claude-plugins-official)：Anthropic-managed Claude Code plugin directory。README 确认 internal/external plugin structure、plugin install command、Discover UI、plugin metadata、MCP config、commands、agents、skills，并明确提示插件信任风险。它是 plugin supply chain 进入官方 distribution surface 的延续信号。归档：[`../raw/2026-05-20/github-trending-readmes/anthropics__claude-plugins-official.md`](../raw/2026-05-20/github-trending-readmes/anthropics__claude-plugins-official.md)。
- [`rohitg00/agentmemory`](https://github.com/rohitg00/agentmemory)：persistent memory for AI coding agents。README 记录 Claude Code、Codex CLI、Cursor、Gemini CLI、OpenCode 等支持 hooks/MCP/REST/API，共享同一 memory server，并宣称 confidence scoring、lifecycle、knowledge graphs、hybrid search。它是 Memory & Dream 主线，但需要复现权限、删除、污染和跨项目隔离。归档：[`../raw/2026-05-20/github-trending-readmes/rohitg00__agentmemory.md`](../raw/2026-05-20/github-trending-readmes/rohitg00__agentmemory.md)。
- [`CloakHQ/CloakBrowser`](https://github.com/CloakHQ/CloakBrowser)：stealth Chromium / Playwright replacement。README 声称 source-level fingerprint patches、humanize behavior 和 bot detection tests；这是浏览器自动化与反检测高风险信号，必须标注 ToS、平台反滥用、凭据和安全边界，不进入正常 agent tooling 推荐。归档：[`../raw/2026-05-20/github-trending-readmes/CloakHQ__CloakBrowser.md`](../raw/2026-05-20/github-trending-readmes/CloakHQ__CloakBrowser.md)。
- [`rtk-ai/rtk`](https://github.com/rtk-ai/rtk)：Rust Token Killer，CLI proxy / hook layer，压缩 shell command output 后再给 agent。README 记录 60-90% token reduction claims、100+ commands、Bash hook rewrite、Claude Code/Codex/Gemini/Cursor 等 target。它解决的是 tool output hygiene；风险是压缩是否隐藏关键错误、hook 是否改变命令语义。归档：[`../raw/2026-05-20/github-trending-readmes/rtk-ai__rtk.md`](../raw/2026-05-20/github-trending-readmes/rtk-ai__rtk.md)。
- [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents)：把 frontend、Reddit/community、reality check、content/marketing 等角色打包成 specialized agent personalities。它是 agency-style agent pack 的 discovery signal；README 不能证明实际交付质量或账号/平台安全。归档：[`../raw/2026-05-20/github-trending-readmes/msitarzewski__agency-agents.md`](../raw/2026-05-20/github-trending-readmes/msitarzewski__agency-agents.md)。
- [`colbymchenry/codegraph`](https://github.com/colbymchenry/codegraph)：local semantic code graph for Claude Code、Cursor、Codex、OpenCode。README 记录 pre-indexed knowledge graph、symbol/call graph、FTS5、impact analysis、file watcher、framework-aware routes、100% local SQLite。它是 coding-agent context index 的强 discovery signal；边界是 benchmark/quality claims 需复现，源码变化后 freshness 也要验证。归档：[`../raw/2026-05-20/github-trending-readmes/colbymchenry__codegraph.md`](../raw/2026-05-20/github-trending-readmes/colbymchenry__codegraph.md)。

## 来源证据表

| 信号 | 证据等级 | 来源 | URL | 本地归档 |
| --- | --- | --- | --- | --- |
| OpenAI for Singapore / FDE hub | official-source | OpenAI Blog RSS/fulltext | https://openai.com/index/introducing-openai-for-singapore | [`../raw/2026-05-20/rss-fulltext/openai-blog/openai-blog-introducing-openai-for-singapore-e0640ad032.autocli.md`](../raw/2026-05-20/rss-fulltext/openai-blog/openai-blog-introducing-openai-for-singapore-e0640ad032.autocli.md) |
| Content provenance / C2PA / SynthID | official-source | OpenAI Blog RSS/fulltext | https://openai.com/index/advancing-content-provenance | [`../raw/2026-05-20/rss-fulltext/openai-blog/openai-blog-advancing-content-provenance-for-a-safer-more-transparent-ai-ecosystem-4f14311644.autocli.md`](../raw/2026-05-20/rss-fulltext/openai-blog/openai-blog-advancing-content-provenance-for-a-safer-more-transparent-ai-ecosystem-4f14311644.autocli.md) |
| OpenAI Codex 0.132.0 | official-source | GitHub release Atom | https://github.com/openai/codex/releases/tag/rust-v0.132.0 | [`../raw/2026-05-20/github-release-fulltext/openai-codex/openai-codex-0.132.0-df87a5dff8.atom.md`](../raw/2026-05-20/github-release-fulltext/openai-codex/openai-codex-0.132.0-df87a5dff8.atom.md) |
| Claude Code v2.1.145 | official-source | GitHub release Atom | https://github.com/anthropics/claude-code/releases/tag/v2.1.145 | [`../raw/2026-05-20/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.145-5eddeb758d.atom.md`](../raw/2026-05-20/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.145-5eddeb758d.atom.md) |
| Gemini Omni | official-source | Google DeepMind RSS/fulltext | https://deepmind.google/blog/introducing-gemini-omni/ | [`../raw/2026-05-20/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-gemini-omni-6ff85c3103.extracted.md`](../raw/2026-05-20/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-gemini-omni-6ff85c3103.extracted.md) |
| Gemini for Science | official-source | Google DeepMind RSS/fulltext | https://deepmind.google/blog/gemini-for-science-ai-experiments-and-tools-for-a-new-era-of-discovery/ | [`../raw/2026-05-20/rss-fulltext/google-deepmind-blog/google-deepmind-blog-gemini-for-science-ai-experiments-and-tools-for-a-new-era-of-discovery-548bdf100a.extracted.md`](../raw/2026-05-20/rss-fulltext/google-deepmind-blog/google-deepmind-blog-gemini-for-science-ai-experiments-and-tools-for-a-new-era-of-discovery-548bdf100a.extracted.md) |
| Direct X product/personnel signals | direct-x | `twitterapi.io` | multiple X URLs | [`../raw/2026-05-20/twitterapi-io-results.json`](../raw/2026-05-20/twitterapi-io-results.json) |
| Agent runtime Trending set | secondary-source | GitHub Trending / README | multiple GitHub URLs | [`../raw/2026-05-20/github-trending-readmes/`](../raw/2026-05-20/github-trending-readmes/) |

## X/Twitter 覆盖说明

- 本次 X/Twitter 只使用 `twitterapi.io` 的 `GET https://api.twitterapi.io/twitter/user/last_tweets` read endpoint，`includeReplies=false`。
- `twitterapi.io` 顶层采集成功：27 个账号均 `ok`，没有 failed accounts。
- 本轮共保留 144 条 direct-x 原始条目。保留数较高的账号包括 `levelsio` 20 条、`cellinlab` 17 条、`Hesamation` 16 条、`rileybrown` 15 条、`marclou` 12 条、`steipete` 9 条、`frxiaobei` 8 条、`kloss_xyz` 7 条。
- `rryssf_`、`oviswang`、`Yangyixxxx`、`lidang`、`cnyzgkc`、`_LuoFuli` 请求成功但 kept_count 为 0；这表示 36 小时窗口和脚本过滤下没有保留条目，不等于账号没有更新。
- direct-x 内容包含个人观点、短评论、转发、产品线索和活动宣传；日报只把它们作为直接来源线索，不把个人观点写成官方事实。

## 运行结果与失败源

- RSS：30/31 成功；失败源为 `sean-goedecke`，`source-health.json` 记录 `curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to www.seangoedecke.com:443`。
- RSS fulltext：相关全文 48 条尝试，48 条 ok、0 条 limited、0 条 failed。
- GitHub releases：7/7 release Atom feed 成功；GitHub REST API 状态为 `skipped`，脚本按设计使用 Atom feed。
- GitHub release fulltext：OpenAI Codex 2/5 ok、3/5 limited；Claude Code 5/5 ok。
- GitHub Trending：1/1 成功，解析 10 个每日热门 repo，10 个 README 文件已归档。
- 官方页面：4/4 ok，0 limited，0 failed。
- X/Twitter：`twitterapi.io` 顶层采集成功，27/27 accounts ok；没有使用 Exa fallback。

## 不确定性与待验证项

- 已确认边界：本日报覆盖 2026-05-20 raw 输出、[`../raw/2026-05-20/manifest.json`](../raw/2026-05-20/manifest.json)、[`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)；GitHub Trending 只覆盖 `https://github.com/trending?since=daily` 当前 HTML 中解析到的 10 个 repo，以及脚本归档的 README；X/Twitter 只覆盖 `twitterapi.io` 返回并被 36 小时窗口保留的 direct-x 条目。
- 未覆盖范围：没有抓取登录态网页、没有补采 X thread/context、没有复现 GitHub Trending repo、没有运行 OpenHuman/agentmemory/CodeGraph/rtk/Superpowers、没有验证 Codex/Claude Code release 的运行行为、没有检查 OpenAI Guaranteed Capacity 的商业合同或 API 文档。
- 推断项：【推断得出】本日报把“FDE national deployment package、agent runtime observability/continuity、multimodal generation、scientific agent workflow、capacity certainty”作为今天主线。依据是 OpenAI/Google/Codex/Claude 一手材料与 direct-x 同日出现；失效条件是后续官方 docs 显示这些只是 marketing framing、region-limited launch 或未开放能力。
- 待验证项：查 OpenAI for Singapore 的 Applied AI Lab hiring、FDE training、public service/finance/healthcare pilots 和数据治理边界；查 Guaranteed Capacity 的官方商业文档、commitment、discount、availability 和 quota semantics；复现 Codex `0.132.0` 的 Python SDK auth、`exec resume --output-schema` 和 remote executor registration；检查 Claude Code `v2.1.145` 的 `claude agents --json`、OTEL spans、permission fix 和 Read partial view；等待 Gemini Omni API/enterprise docs。

## 运行统计

- 新增条目：`seen_added=46`。
- 高信号条目：8 条。
- 失败来源：RSS failed 1 个；official page failed 0 个；twitterapi.io failed accounts 0 个。
- limited 来源：OpenAI Codex release fulltext limited 3 条；RSS fulltext limited 0 条。

## 完成审计

- 用户目标拆解：稳定来源采集、twitterapi.io direct-x 采集、状态更新、日报生成、enabled trends 检查、失败/limited 来源说明、输出路径汇总。
- 证据对应：raw JSON 写入 [`../raw/2026-05-20/`](../raw/2026-05-20/)，状态文件写入 [`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)，日报为当前文件。
- 状态同步：`update-state.py` 已生成 [`../raw/2026-05-20/manifest.json`](../raw/2026-05-20/manifest.json)，并更新 source health 与 seen。
- 来源边界：所有 X/Twitter 内容标为 `direct-x`，GitHub Trending 标为 `secondary-source`，官方 RSS/GitHub release/official pages 标为 `official-source`、official metadata 或 limited；未用 Exa fallback。
- Trend 检查：`memory-dream`、`financial-agents`、`forward-deployed-engineering` 均已检查；trend raw 归档见 [`../trend/raw/2026-05-20/`](../trend/raw/2026-05-20/)。
