# 2026-05-18 Daily Source Intelligence

## 采集范围

- 运行时间：2026-05-18 Asia/Shanghai，本轮写入 [`../raw/2026-05-18/`](../raw/2026-05-18/)。
- 稳定来源：RSS/Atom 31 个源，31 个成功；相关全文 49 条尝试，38 条 ok、11 条 limited、0 条 failed；GitHub releases 7 个源通过 Atom feed 成功；GitHub Trending 1 个源成功，解析 10 个每日热门 repo；official pages 4 个源成功、0 个 limited、0 个 failed。
- X/Twitter：通过 `twitterapi.io` read endpoint 成功采集，顶层状态 `ok`；27 个账号均返回 `ok`，保留 88 条 direct-x 原始条目。
- 状态更新：[`../raw/2026-05-18/manifest.json`](../raw/2026-05-18/manifest.json)、[`../state/source-health.json`](../state/source-health.json)、[`../state/seen.json`](../state/seen.json) 已由 `update-state.py` 更新；本轮 `seen_added=35`，累计 796 条。
- 本次没有使用 Exa MCP、登录态浏览器、X/Twitter 账号凭证、写操作 endpoint、posting、liking、following 或 DM。
- 本地归档：[`../raw/2026-05-18/rss-items.json`](../raw/2026-05-18/rss-items.json)、[`../raw/2026-05-18/github-items.json`](../raw/2026-05-18/github-items.json)、[`../raw/2026-05-18/github-trending.json`](../raw/2026-05-18/github-trending.json)、[`../raw/2026-05-18/github-trending-readmes/`](../raw/2026-05-18/github-trending-readmes/)、[`../raw/2026-05-18/official-pages.json`](../raw/2026-05-18/official-pages.json)、[`../raw/2026-05-18/twitterapi-io-results.json`](../raw/2026-05-18/twitterapi-io-results.json)。

## 今日高信号

1. OpenAI Malta partnership 是今天最清晰的一手新增：OpenAI 与 Malta 政府宣布向所有 Maltese citizens 提供完成 AI literacy course 后一年免费 ChatGPT Plus，且把它放在 `OpenAI for Countries` 的国家级采用框架里。【有明确证据支撑 / official-source / fulltext-ok】证据见 [`openai-blog-openai-and-malta...autocli.md`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-openai-and-malta-partner-to-bring-chatgpt-plus-to-all-citizens-f0106247de.autocli.md#L10) 和 [`#L14`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-openai-and-malta-partner-to-bring-chatgpt-plus-to-all-citizens-f0106247de.autocli.md#L14)。
2. OpenAI personal finance 原文再次完整归档。它确认 ChatGPT Pro U.S. 用户可连接 12,000+ 金融机构，通过 Plaid 连接、Intuit support coming soon；ChatGPT 可读 balances、transactions、investments、liabilities，但不能看到完整账号，也不能修改账户。【有明确证据支撑 / official-source / fulltext-ok】证据见 [`openai-blog-a-new-personal-finance...autocli.md`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-a-new-personal-finance-experience-in-chatgpt-ada6c14251.autocli.md#L18)、[`#L26`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-a-new-personal-finance-experience-in-chatgpt-ada6c14251.autocli.md#L26)、[`#L116`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-a-new-personal-finance-experience-in-chatgpt-ada6c14251.autocli.md#L116)。
3. personal finance 的高风险边界仍然清楚：它不是 professional financial advice replacement；断开账户后同步账户数据 30 天内删除；Financial memories 可查看/删除；temporary chats 不访问连接的金融账户。【有明确证据支撑 / official-source / fulltext-ok】证据见 [`openai-blog-a-new-personal-finance...autocli.md`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-a-new-personal-finance-experience-in-chatgpt-ada6c14251.autocli.md#L16)、[`#L122`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-a-new-personal-finance-experience-in-chatgpt-ada6c14251.autocli.md#L122)、[`#L123`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-a-new-personal-finance-experience-in-chatgpt-ada6c14251.autocli.md#L123)、[`#L124`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-a-new-personal-finance-experience-in-chatgpt-ada6c14251.autocli.md#L124)。
4. Databricks/GPT-5.5 enterprise agent workflow 继续是 FDE 强信号。原文把 OfficeQA Pro 的失败面具体化为 scanned PDFs、legacy files、long-context documents、parsing、retrieval、grounded reasoning，并把生产路径指向 AI Unity Gateway、AgentBricks、Agent Supervisor API。【有明确证据支撑 / official-source / fulltext-ok】证据见 [`openai-blog-databricks...autocli.md`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-databricks-brings-gpt-5.5-to-enterprise-agent-workflows-c64312c312.autocli.md#L34) 到 [`#L38`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-databricks-brings-gpt-5.5-to-enterprise-agent-workflows-c64312c312.autocli.md#L38)，以及 [`#L56`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-databricks-brings-gpt-5.5-to-enterprise-agent-workflows-c64312c312.autocli.md#L56)。
5. OpenAI Academy 新增 `How sales teams use Codex`，把 Codex 放进 CRM、call notes、email threads、Slack、decks、customer docs 和 account signals，输出 account brief、meeting prep、forecast risk review、account strategy pack 和 stalled-deal diagnosis。【有明确证据支撑 / first-party-openai / fulltext-ok】证据见 [`openai-blog-how-sales-teams-use-codex...autocli.md`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-how-sales-teams-use-codex-248b5ff069.autocli.md#L8)。
6. Claude Code release Atom 今日 5/5 fulltext ok，`v2.1.143` 的高价值变更集中在 plugin dependency enforcement、projected context cost、background session model/effort preservation、`worktree.bgIsolation: "none"`、以及多项 background/agent view 修复；OpenAI Codex release Atom 5/5 limited，只能记录 release surface。【有明确证据支撑 / first-party-claude-code / first-party-openai-limited】证据见 [`anthropics-claude-code-v2.1.143...atom.md`](../raw/2026-05-18/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.143-cf9984cc93.atom.md#L7)。
7. GitHub Trending Daily 继续高密度命中 agent runtime：`tinyhumansai/openhuman`、`Imbad0202/academic-research-skills`、`HKUDS/CLI-Anything`、`K-Dense-AI/scientific-agent-skills`、`tech-leads-club/agent-skills` 均进入榜单。它们共同指向 agent skills、personal memory tree、CLI harness 和安全 skill registry，但证据等级只是 secondary-source。【有明确证据支撑 / secondary-source】
8. direct-x 中 `@sama` 报告 ChatGPT Images 在 India 已创建 10 亿+ images；`@mattpocockuk` 讨论 `/grill-with-docs`、`/handoff`、feature-flag development with agents；`@rileybrown` 给出 Codex 分析本地短信的个人使用信号；`@cellinlab` 记录 Codex runner / remote Mac 控制体验。它们是 direct-x 使用者线索，不是官方规格。【有明确证据支撑 / direct-x】

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS 今天 5/5 条按 `fulltext_policy: always` 读取并归档成功：Malta ChatGPT Plus partnership、personal finance、Codex for data science、Databricks/GPT-5.5、Codex for sales teams。归档见 [`../raw/2026-05-18/rss-fulltext/openai-blog/`](../raw/2026-05-18/rss-fulltext/openai-blog/)。
- Malta partnership 是今天新增的一手政策/分发信号。它不是模型能力更新，而是国家级 AI literacy + ChatGPT Plus access 的 adoption programme；可跟踪点是 `OpenAI for Countries` 是否形成可复制的政府 adoption playbook。
- personal finance 是金融 agent 高风险信号的延续。今天没有比 2026-05-17 更多的功能细节，但全文归档再次成功，证据等级稳定在 official-source/fulltext-ok。
- Databricks/GPT-5.5 是 enterprise-agent benchmark / production workflow 延续信号。今天的价值是继续把 FDE 失败面固定到 enterprise document parsing、retrieval detours 和 supervisor/orchestration。
- Claude Code GitHub release Atom 读取 `v2.1.143` 到 `v2.1.139`，release fulltext 5/5 ok；OpenAI Codex release Atom 读取 `0.131.0-alpha.22` 到 `.18`，但 release fulltext 5/5 limited，不能推断具体变更。

## 按主题分组摘要

### LLM / Frontier Models

- OpenAI Malta partnership 把 ChatGPT Plus 分发与 AI literacy course 绑定，这是模型供应商进入国家 adoption / workforce education 的一手信号。它不提供新模型能力，但改变了 adoption surface：政府课程、资格分发、公共技能建设和 OpenAI for Countries。
- personal finance 继续说明 GPT-5.5 Thinking 正在被用于高上下文、高风险的 consumer guidance。日报只写官方页面确认的账户读取、记忆、删除和非专业建议边界，不把它写成投资顾问或交易执行。
- a16z `Memory to the Moon` 把 AI infrastructure bottleneck 从 power/chips 扩展到 DRAM/NAND/HBM memory，并引用 Affirm software engineering AI-first retooling 与 agentic PR output 作为 productivity signal；这是 secondary/analysis source，不是官方 benchmark。

### AI Agent / Agentic Workflow

- OpenHuman 今天继续上榜，是 Memory & Dream 主线。README 记录 118+ integrations、one-click OAuth、20 分钟 auto-fetch、Memory Tree、Obsidian-compatible vault、SQLite、本地 compression 和 optional `agentmemory` backend。它解决的是 personal agent 如何持续吸收用户工作系统上下文；风险是 OAuth、后台同步、删除治理和记忆污染。
- `CLI-Anything` 把更多软件包装成 agent-usable CLI harness，README 记录 CLI-Hub、generated CLIs、preview/live preview/trajectory loops、以及技能目录统一。它是 agent 操作面 productization 的 discovery signal；不能把上榜或 README claim 当成可生产质量证明。
- `Academic Research Skills`、`Scientific Agent Skills` 和 `Agent Skills` 共同说明 skills 正在从单点 prompt 走向可安装、可复用、带安全/验证叙事的 workflow unit。

### AI Coding / Developer Tools

- Codex for sales teams 和 data science teams 把 coding agent 的模式继续扩到 business artifacts：读散落上下文、生成 first usable draft、分离 sourced facts 和 inferred risk、交给人 review。
- Claude Code `v2.1.143` 的高信号是 background agents / plugin / context-cost 管理继续变重：plugin dependency enforcement、projected context cost、background session defaults、`/bg` 参数保存、stop-hook block cap 和 worktree cleanup 防数据丢失都说明 agent runtime 正在补长期任务边界。
- direct-x 中 `@mattpocockuk` 的 `/grill-with-docs` 与 feature flag development with agents，是真实使用者对 agent workflow 的小样本信号；它适合形成问题线索，不适合直接写成最佳实践。

### Forward Deployed Engineering / Enterprise AI

- Databricks/GPT-5.5 仍是今天最强 FDE 相关材料：企业 document-agent 的失败面、benchmark 和 production supervisor path 都有官方全文支撑。
- Malta partnership 是另一种 enterprise/public-sector adoption 信号：不是客户现场 engineering，但它说明 AI lab 正在把 access + literacy + government distribution 做成国家 adoption package。
- a16z 的 Affirm 段落提示 software engineering AI-first retooling 可能提升 PR output 且没有立即替代工程团队；因为它来自分析文章转述，应作为 secondary-source 线索，下一步需要找 Affirm 原始材料。

### Financial Agents

- OpenAI personal finance 继续是 Financial Agents 主线。fulltext-ok 支持的结论仍是 connected-data guidance：账户连接、dashboard、Financial memories、Plaid、Intuit coming soon、temporary chat 不访问账户、断开后 30 天删除同步账户数据。
- 它仍不是交易执行、payment、ledger posting 或 investment advisor action surface；但文中 `answers to action` 提到 credit card recommendation → approval odds/application、stock sale tax estimate → local tax expert scheduling，所以后续一旦出现 partner action/API/tool schema，必须提高证据门槛。
- 今天没有新的 trading/copy-trading repo 进入高信号；Financial Agents trend 不强行新增结论，只保留 personal finance 的 fulltext-confirmed 状态。

### Product / Growth / Indie Founder

- `@marclou` 的 micro-acquisition / affiliate program、`@jackfriks` 的流量来源经验、`@levelsio` 的 Hoodmaps/crime-data shipping、`@cellinlab` 的 Codex runner 使用体验属于 product/indie/direct-x 线索。
- 这些线索更适合保留方向感：AI 工具正在降低小团队出货、分析和分发的边际成本；但具体收入、转化、增长结论需要原始 dashboard 或产品数据。

## GitHub Trending / Daily Repos

本轮 GitHub Trending Daily 成功解析 10 个 repo，10/10 README 文件已写入目录。索引见 [`../raw/2026-05-18/github-trending.json`](../raw/2026-05-18/github-trending.json)，README 原文见 [`../raw/2026-05-18/github-trending-readmes/`](../raw/2026-05-18/github-trending-readmes/)。证据等级统一按 `secondary-source` 处理：它只能说明项目当天在 GitHub Trending 页面可见，不代表官方发布、质量背书或长期趋势。

- [`tinyhumansai/openhuman`](https://github.com/tinyhumansai/openhuman)：personal AI assistant / desktop agent。README 能确认它强调 118+ integrations、typed tools、20 分钟 auto-fetch、Memory Tree、Obsidian-compatible vault、SQLite 和 local-first workflow。今天值得记录，因为它把 personal agent memory 从 chat history 推到用户工作系统；风险是 OAuth 最小授权、后台同步、删除治理和敏感数据进入长期记忆。归档：[`../raw/2026-05-18/github-trending-readmes/tinyhumansai__openhuman.md`](../raw/2026-05-18/github-trending-readmes/tinyhumansai__openhuman.md)。
- [`Imbad0202/academic-research-skills`](https://github.com/Imbad0202/academic-research-skills)：Claude Code academic research skills，面向 research → write → review → revise → finalize。README 把它定位为帮研究者做引用、格式、数据验证和逻辑一致性检查，而不是替用户写论文或隐藏 AI 使用。今天价值在 skills-as-domain-workflow，风险是学术诚信、引用准确性和人工判断边界。归档：[`../raw/2026-05-18/github-trending-readmes/Imbad0202__academic-research-skills.md`](../raw/2026-05-18/github-trending-readmes/Imbad0202__academic-research-skills.md)。
- [`HKUDS/CLI-Anything`](https://github.com/HKUDS/CLI-Anything)：把软件做成 agent-native CLI harness 的项目。README 记录 CLI-Hub 安装/管理、generated CLIs、preview/live preview/trajectory loops，以及 CAD、3D、diagram、gameplay、subtitle 等 demo 面。它解决的是 agent 如何稳定操作原本面向人的软件；边界是 harness 安全、side effect、凭据、真实软件版本兼容性和测试覆盖需逐项验证。归档：[`../raw/2026-05-18/github-trending-readmes/HKUDS__CLI-Anything.md`](../raw/2026-05-18/github-trending-readmes/HKUDS__CLI-Anything.md)。
- [`K-Dense-AI/scientific-agent-skills`](https://github.com/K-Dense-AI/scientific-agent-skills)：scientific/research skills 集合，README 记录 135 ready-to-use skills、100+ scientific databases、open Agent Skills standard、BYOK desktop co-scientist。它解决的是科研/工程/分析技能如何包装给不同 agent 使用；风险是专业数据库 provenance、模型输出可验证性、临床/金融边界和 license。归档：[`../raw/2026-05-18/github-trending-readmes/K-Dense-AI__scientific-agent-skills.md`](../raw/2026-05-18/github-trending-readmes/K-Dense-AI__scientific-agent-skills.md)。
- [`supertone-inc/supertonic`](https://github.com/supertone-inc/supertonic)：on-device multilingual TTS，README 记录 ONNX Runtime、本地推理、31 languages 和 99M-parameter open-weight model。它和 agent 主线的交集在本地 voice interface 和隐私友好语音层，但不是今天的强 agent workflow 信号。归档：[`../raw/2026-05-18/github-trending-readmes/supertone-inc__supertonic.md`](../raw/2026-05-18/github-trending-readmes/supertone-inc__supertonic.md)。
- [`ggml-org/llama.cpp`](https://github.com/ggml-org/llama.cpp)：LLM inference in C/C++，README 记录 `libllama`/`llama-server` API 变化、HF cache migration、gpt-oss native MXFP4、multimodal support、FIM completions 等。它是本地推理基础设施常青信号，不是新 agent 产品。归档：[`../raw/2026-05-18/github-trending-readmes/ggml-org__llama.cpp.md`](../raw/2026-05-18/github-trending-readmes/ggml-org__llama.cpp.md)。
- [`ruvnet/RuView`](https://github.com/ruvnet/RuView)：用 commodity WiFi/ESP32 CSI 做 spatial intelligence、vital sign monitoring 和 presence detection。README 也写了 beta、硬件限制和 pose accuracy 待验证，不能把它当成医疗或安防可部署结论。归档：[`../raw/2026-05-18/github-trending-readmes/ruvnet__RuView.md`](../raw/2026-05-18/github-trending-readmes/ruvnet__RuView.md)。
- [`CloakHQ/CloakBrowser`](https://github.com/CloakHQ/CloakBrowser)：stealth Chromium / Playwright replacement，README 声称 source-level fingerprint patches、通过 bot detection tests、humanize 行为模拟。它是浏览器自动化与反检测高风险信号；必须标出风险：可能触达反滥用、平台 ToS、凭据和自动化规避边界，不进入正常 agent tooling 推荐。归档：[`../raw/2026-05-18/github-trending-readmes/CloakHQ__CloakBrowser.md`](../raw/2026-05-18/github-trending-readmes/CloakHQ__CloakBrowser.md)。
- [`tech-leads-club/agent-skills`](https://github.com/tech-leads-club/agent-skills)：secure, validated skill registry for professional AI coding agents。README 强调 skill registry、安全、验证、支持 Antigravity/Claude Code/Cursor/Copilot 等。它值得记录，因为 skill supply chain 安全正在变成显性卖点；边界是 README 不能证明漏洞率、审计流程或实际安全性。归档：[`../raw/2026-05-18/github-trending-readmes/tech-leads-club__agent-skills.md`](../raw/2026-05-18/github-trending-readmes/tech-leads-club__agent-skills.md)。
- [`BigBodyCobain/Shadowbroker`](https://github.com/BigBodyCobain/Shadowbroker)：多源 OSINT / geospatial intelligence platform，README 记录 aircraft、ships、satellites、conflict zones、CCTV、GPS jamming、mesh radio、breaking events 等聚合。它是 agent + OSINT 高风险 discovery signal；风险包括隐私、误报、执法/地缘政治使用、数据许可和安全滥用。归档：[`../raw/2026-05-18/github-trending-readmes/BigBodyCobain__Shadowbroker.md`](../raw/2026-05-18/github-trending-readmes/BigBodyCobain__Shadowbroker.md)。

## 来源证据表

| 信号 | 证据等级 | 来源 | URL | 本地归档 |
| --- | --- | --- | --- | --- |
| Malta ChatGPT Plus partnership | official-source | OpenAI Blog RSS/fulltext | https://openai.com/index/malta-chatgpt-plus-partnership | [`../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-openai-and-malta-partner-to-bring-chatgpt-plus-to-all-citizens-f0106247de.autocli.md`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-openai-and-malta-partner-to-bring-chatgpt-plus-to-all-citizens-f0106247de.autocli.md) |
| ChatGPT personal finance | official-source | OpenAI Blog RSS/fulltext | https://openai.com/index/personal-finance-chatgpt | [`../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-a-new-personal-finance-experience-in-chatgpt-ada6c14251.autocli.md`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-a-new-personal-finance-experience-in-chatgpt-ada6c14251.autocli.md) |
| Databricks GPT-5.5 enterprise agent workflows | official-source | OpenAI Blog RSS/fulltext | https://openai.com/index/databricks | [`../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-databricks-brings-gpt-5.5-to-enterprise-agent-workflows-c64312c312.autocli.md`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-databricks-brings-gpt-5.5-to-enterprise-agent-workflows-c64312c312.autocli.md) |
| Codex for sales teams | official-source | OpenAI Academy | https://openai.com/academy/codex-for-work/how-sales-teams-use-codex | [`../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-how-sales-teams-use-codex-248b5ff069.autocli.md`](../raw/2026-05-18/rss-fulltext/openai-blog/openai-blog-how-sales-teams-use-codex-248b5ff069.autocli.md) |
| Claude Code v2.1.143 | official-source | GitHub release Atom | https://github.com/anthropics/claude-code/releases/tag/v2.1.143 | [`../raw/2026-05-18/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.143-cf9984cc93.atom.md`](../raw/2026-05-18/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.143-cf9984cc93.atom.md) |
| OpenHuman / CLI-Anything / Skills repos | secondary-source | GitHub Trending / README | multiple GitHub URLs | [`../raw/2026-05-18/github-trending-readmes/`](../raw/2026-05-18/github-trending-readmes/) |
| Direct X usage and product signals | direct-x | `twitterapi.io` | multiple X URLs | [`../raw/2026-05-18/twitterapi-io-results.json`](../raw/2026-05-18/twitterapi-io-results.json) |

## X/Twitter 覆盖说明

- 本次 X/Twitter 只使用 `twitterapi.io` 的 `GET https://api.twitterapi.io/twitter/user/last_tweets` read endpoint，`includeReplies=false`。
- `twitterapi.io` 顶层状态为 `ok`，27 个账号均返回 `status=ok`；没有把任何 credential/API 异常当作“无推文”。
- 本轮共保留 88 条 direct-x 原始条目。保留数较高的账号包括 `cellinlab` 16 条、`Hesamation` 14 条、`levelsio` 11 条、`rileybrown` 7 条、`mattpocockuk` 6 条、`marclou` 6 条。
- `karpathy`、`OpenAI`、`AnthropicAI`、`gregisenberg`、`corbin_braun`、`rryssf_`、`Yangyixxxx`、`genspark_ai`、`lidang`、`cnyzgkc`、`_LuoFuli` 请求成功但 kept_count 为 0；这表示 36 小时窗口和脚本过滤下没有保留条目，不等于账号没有更新。
- direct-x 内容包含个人观点、短评论、转发、产品线索和活动宣传；日报只把它们作为直接来源线索，不把个人观点写成官方事实。

## 运行结果与失败源

- RSS：31/31 成功；相关全文 49 条尝试，38 条 ok、11 条 limited、0 条 failed。
- RSS limited：antirez 4 条、forward-deployed 2 条、svpg 2 条、minimaxir 1 条、steve-blank 1 条、ted-mabrey 1 条。
- GitHub releases：7/7 release Atom feed 成功；GitHub REST API 状态为 `skipped`，脚本按设计使用 Atom feed。
- GitHub release fulltext：Claude Code 5/5 ok；OpenAI Codex 5/5 limited，因此不能从 Codex release body 推断具体变更。
- GitHub Trending：1/1 成功，解析 10 个每日热门 repo，10 个 README 文件已归档。
- 官方页面：4/4 ok，0 limited，0 failed；Claude Blog 返回 5 个近期 blog metadata。
- X/Twitter：`twitterapi.io` 顶层 `ok`，27 个账号请求成功；没有 failed accounts，没有 Exa fallback。

## 不确定性与待验证项

- 已确认边界：本日报覆盖 2026-05-18 raw 输出、[`../raw/2026-05-18/manifest.json`](../raw/2026-05-18/manifest.json)、[`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)；GitHub Trending 只覆盖 `https://github.com/trending?since=daily` 当前 HTML 中解析到的 10 个 repo，以及脚本归档的 README；X/Twitter 只覆盖 `twitterapi.io` 返回并被 36 小时窗口保留的 direct-x 条目。
- 未覆盖范围：没有抓取登录态网页、没有补采 X thread/context、没有浏览器渲染 official pages、没有审计 GitHub Trending repo 源码质量或运行效果、没有复现 OpenHuman/CLI-Anything/skills repos、没有检查 ChatGPT personal finance 实际 UI 和账户连接流程。
- 推断项：【推断得出】本日报把“国家级 AI access、connected financial context、enterprise document agents、agent skills/personal memory tree”作为今天主线。依据是 OpenAI first-party fulltext、Claude Code release fulltext、GitHub Trending README 和 direct-x 同日出现；失效条件是后续产品文档、源码或真实运行显示这些只是 marketing framing、demo 项目或不可复现实现。
- 待验证项：验证 Malta programme 的资格、课程完成、ChatGPT Plus 发放与数据治理边界；实际检查 ChatGPT Finances 的 Plaid/Intuit permission、data deletion、Financial memories 和 professional-advice disclaimer；读取 Databricks AgentBricks / Agent Supervisor API 文档确认 production workflow；复现 OpenHuman 的 auto-fetch、delete governance 和 local vault；检查 CLI-Anything generated CLIs 的 side-effect controls；追踪 Claude Code `worktree.bgIsolation` 与 background session safety 的实际行为。

## 运行统计

- 新增条目：`seen_added=35`。
- 高信号条目：8 条。
- 失败来源：RSS failed 0 个；official page failed 0 个；twitterapi.io failed accounts 0 个。
- limited 来源：RSS fulltext limited 11 条；OpenAI Codex release fulltext limited 5 条。

## 完成审计

- 用户目标拆解：稳定来源采集、twitterapi.io direct-x 采集、状态更新、日报生成、trend report 生成、enabled trends 检查、失败/limited 来源说明、输出路径汇总。
- 证据对应：raw JSON 写入 [`../raw/2026-05-18/`](../raw/2026-05-18/)，状态文件写入 [`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)，日报为当前文件。
- 状态同步：`update-state.py` 已生成 [`../raw/2026-05-18/manifest.json`](../raw/2026-05-18/manifest.json)，并更新 source health 与 seen。
- 来源边界：所有 X/Twitter 内容标为 `direct-x`，GitHub Trending 标为 `secondary-source`，官方 RSS/GitHub release/official pages 标为 `official-source`、official metadata 或 limited；未用 Exa fallback。
- Trend 检查：`memory-dream`、`financial-agents`、`forward-deployed-engineering` 均已检查；trend raw 归档见 [`../trend/raw/2026-05-18/`](../trend/raw/2026-05-18/)。
