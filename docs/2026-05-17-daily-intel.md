# 2026-05-17 Daily Source Intelligence

## 采集范围

- 运行时间：2026-05-17 Asia/Shanghai，本轮写入 [`../raw/2026-05-17/`](../raw/2026-05-17/)。
- 稳定来源：RSS/Atom 31 个源，31 个成功；相关全文 49/49 成功；GitHub releases 7 个源，7 个通过 Atom feed 成功；GitHub Trending 1 个源成功，解析 8 个每日热门 repo；official pages 4 个源，4 个成功、0 个 limited、0 个 failed。
- X/Twitter：通过 `twitterapi.io` read endpoint 成功采集，顶层状态 `ok`；26 个账号均返回 `ok`，保留 118 条 direct-x 原始条目。
- 状态更新：[`../raw/2026-05-17/manifest.json`](../raw/2026-05-17/manifest.json)、[`../state/source-health.json`](../state/source-health.json)、[`../state/seen.json`](../state/seen.json) 已由 `update-state.py` 更新；本轮 `seen_added=42`，累计 761 条。
- 本次没有使用 Exa MCP、登录态浏览器、X/Twitter 账号凭证、写操作 endpoint、posting、liking、following 或 DM。
- 本地归档：[`../raw/2026-05-17/rss-items.json`](../raw/2026-05-17/rss-items.json)、[`../raw/2026-05-17/github-items.json`](../raw/2026-05-17/github-items.json)、[`../raw/2026-05-17/github-trending.json`](../raw/2026-05-17/github-trending.json)、[`../raw/2026-05-17/github-trending-readmes/`](../raw/2026-05-17/github-trending-readmes/)、[`../raw/2026-05-17/official-pages.json`](../raw/2026-05-17/official-pages.json)、[`../raw/2026-05-17/twitterapi-io-results.json`](../raw/2026-05-17/twitterapi-io-results.json)。

## 今日高信号

1. OpenAI personal finance 原文今天完整归档成功。它确认 ChatGPT Pro U.S. 用户可连接 12,000+ 金融机构，账户连接通过 Plaid，Intuit 支持即将到来；ChatGPT 可读取余额、交易、投资和 liabilities，但不能看到完整账号，也不能改账户。【有明确证据支撑 / official-source / fulltext-ok】
2. 同一 OpenAI personal finance 原文确认了更关键的边界：它不是 professional financial advice replacement；断开账户后同步账户数据会在 30 天内从 OpenAI 系统删除；Financial memories 是专用记忆类型，可查看或删除；temporary chats 不访问已连接金融账户。【有明确证据支撑 / official-source / fulltext-ok】
3. OpenAI Databricks/GPT-5.5 原文完整归档成功。它把 OfficeQA Pro 定义为企业文档任务 benchmark，覆盖 scanned PDFs、legacy files、long-context documents、parsing、retrieval 和 grounded reasoning；GPT-5.5 在 agent-harness setting 下比 GPT-5.4 减少 46% errors，并首次超过 50% accuracy。【有明确证据支撑 / official-source / fulltext-ok】
4. OpenAI Academy 连续新增 Codex for business operations 和 Codex for data science 两篇使用指南。它们把 Codex 放进 KPI dashboards、planning docs、Slack threads、spreadsheets、metric definitions、exports、experiment notes 等工作上下文，输出 off-track brief、decision packet、root-cause brief、dashboard spec 等可 review artifact。【有明确证据支撑 / first-party-openai / fulltext-ok】
5. GitHub Trending Daily 中 `colbymchenry/codegraph` 上榜。README 把它定位为 Claude Code 的本地语义代码图，声称用 pre-indexed symbol/call graph 降低探索工具调用，支持 19+ languages、framework-aware routes、SQLite、本地 file watcher。这是 coding agent context retrieval / memory substrate 的新 discovery signal。【有明确证据支撑 / secondary-source】
6. Google DeepMind `AlphaEvolve` 原文归档成功。它把 Gemini-powered coding agent 从算法发现扩展到 genomics、power grid、quantum circuits、TPU design、Spanner compaction、compiler optimization、commercial enterprise optimization 等场景，是 agentic optimization 进入 infra 和企业场景的官方强信号。【有明确证据支撑 / official-source / fulltext-ok】
7. Pragmatic Engineer `Forward deployed engineering heats up again` 抓取到付费墙前摘要，明确提到 Google、OpenAI、Anthropic 对 FDE role demand 上升。这是 FDE 热度的弱但直接外部线索；因为正文受付费墙限制，不能用它支撑组织细节结论。【有明确证据支撑 / limited-fulltext】
8. direct-x 中 `@gregisenberg` 继续谈 managed AI employees、Claude skills 和 agent memory；`@rileybrown` 转发“新数字产品应考虑 CLI 或 MCP 作为 AI agent 一等入口”；`@kloss_xyz` 发布 Codex `/goal` 模板；`@levelsio` 和 `@steipete` 继续给出 Claude Code/Codex 使用体验信号。这些是 direct-x 使用者线索，不是官方规格。【有明确证据支撑 / direct-x】

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS 今天 5/5 条都按 `fulltext_policy: always` 读取并归档成功：Malta ChatGPT Plus partnership、Codex for business operations、Databricks/GPT-5.5、Codex for data science、personal finance。归档见 [`../raw/2026-05-17/rss-fulltext/openai-blog/`](../raw/2026-05-17/rss-fulltext/openai-blog/)。
- personal finance 是今天最需要跟踪的金融 agent 信号。原文确认了 account linking、dashboard、Financial memories、Plaid/Intuit、数据删除和非专业建议边界；它不是交易执行或投资顾问能力，但已经触达敏感 financial context 和 guidance。
- Databricks/GPT-5.5 是今天最强 enterprise-agent benchmark 信号。原文明确把 production agent failure 归到 parsing、retrieval、grounded reasoning、multi-step detours 和 scanned/legacy enterprise docs；生产路径是 Databricks AI Unity Gateway、AgentBricks 和 Agent Supervisor API。
- Codex for work 两篇指南把 Codex 从 coding 扩展到 business operations 和 data science artifacts。它们的共同边界是“first usable draft + human validation”，不是系统自动决策或自动写入 source of truth。
- Claude Code GitHub release Atom 成功读取 `v2.1.143` 到 `v2.1.139`，release fulltext 5/5 ok；OpenAI Codex release Atom 读取 `0.131.0-alpha.22` 到 `.18`，但 release fulltext 5/5 limited，只能记录 release surface，不能推断具体变更。

## 按主题分组摘要

### LLM / Frontier Models

- OpenAI personal finance 与 Databricks/GPT-5.5 今天都从昨天的 limited 变成 fulltext-ok，证据强度提高。personal finance 侧重 consumer financial context，Databricks 侧重 enterprise document-agent benchmark 和 production workflow。
- Google DeepMind AlphaEvolve 是官方长文，价值在于说明 coding agent / algorithm discovery 不只服务软件开发，还在 TPU、Spanner、compiler、quantum、genomics、grid optimization 和商业优化中出现可部署案例。
- Claude Blog official page 仍列出 legal industry、AI-native startup、Claude Code large codebases、computer/browser use best practices 等近期条目；今天 official page 状态为 ok，但未出现比 OpenAI/DeepMind 更强的新正文增量。

### AI Agent / Agentic Workflow

- `codegraph` 是今天 Memory & Dream 主线：它不是普通代码搜索，而是把代码库预索引成 local graph 给 Claude Code 查询，目标是减少探索型 subagent 的 grep/read/tool-call 成本。README 证据只能证明项目主张和 benchmark claim，不能证明在真实大型 repo 中长期稳定。
- `Scientific Agent Skills` 与 `Superpowers` 继续上榜，延续 skills-as-workflow / domain skills 方向。前者强调 135 scientific/research skills、100+ databases、70+ optimized Python package skills 和 open Agent Skills standard；后者强调 coding-agent software development methodology。
- direct-x 中 `@gregisenberg`、`@kloss_xyz`、`@rileybrown` 都在讨论 agent skills、goal templates、CLI/MCP as first-class product surface，这和 GitHub Trending 的 skills/codegraph 信号同向，但仍属于观点或使用者线索。

### AI Coding / Developer Tools

- Codex for business operations / data science 两篇 OpenAI Academy 指南把 AI coding agent 的“读上下文、产出 artifact、留 review flags”模式扩展到运营和数据科学。高价值点不是 prompt 示例本身，而是第一方把 Codex 与 Google Drive、Slack、Gmail、Documents、Spreadsheets、Presentations 等工作资料组合成企业 artifact workflow。
- OpenAI Codex release Atom 今日可见 `0.131.0-alpha.22`、`.21`、`rust-v0.131.0-alpha.20`、`.19`、`.18`，但 release body limited。Claude Code release Atom 可见 `v2.1.143` 到 `v2.1.139`，fulltext ok。
- `levelsio`、`steipete`、`rileybrown` direct-x 继续给出 Claude Code/Codex 体验与教程分发信号。日报只把它们作为 usage sentiment，不把个人体验写成产品事实。

### Forward Deployed Engineering / Enterprise AI

- Databricks/GPT-5.5 原文是今天 FDE 主线：企业 agent 失败点被具体化为 scanned PDFs、legacy files、long context、parsing errors、retrieval detours 和 grounded reasoning，生产落点是 AgentBricks / Agent Supervisor API。
- Pragmatic Engineer 的付费墙前摘要直接说 FDE role 在 Google、OpenAI、Anthropic 有 massive demand，但正文不可读，所以只能作为“FDE 热度上升”的 limited 线索。
- AlphaEvolve 和 Codex for work 都提示 enterprise AI deployment 不只是在客户现场交付模型，而是把 agentic optimization / artifact workflow 放进真实业务和工程系统。需要继续验证这些案例是否形成 reusable product capability。

### Financial Agents

- OpenAI personal finance 是今天最强 Financial Agents 信号，且全文已读。它确认了 connected accounts、dashboard、cash-flow/spending/portfolio/subscriptions/upcoming payments、Financial memories、Plaid、Intuit、temporary chat 不访问账户、断开后 30 天删除同步账户数据。
- 风险边界仍要保守：原文说它不能替代 professional financial advice，也不能改账户；但后续提到从 credit card recommendation 到 approval odds / application、stock sale tax estimate / local tax expert，这说明 future action surface 可能靠 ecosystem partners 扩展，需要更高证据门槛。
- 今天没有新的 trading/copy-trading repo 进入高信号；Financial Agents trend 应更新为“personal finance 从 limited RSS 升级为 fulltext confirmed connected-data guidance”，而不是交易执行。

### Product / Growth / Indie Founder

- `@gregisenberg` 的 36 startup opportunities 包含 managed AI employees for businesses；这是 product/growth 线索，不是 official market data。
- `@marclou`、`@jackfriks`、`@pangyusio`、`@cellinlab` 继续提供 indie/product/AI workflow 线索，包括 micro-acquisition、DataFast keyboard shortcuts、AI project work 和内容分发经验。它们适合保留方向感，不进入技术强结论。

## GitHub Trending / Daily Repos

本轮 GitHub Trending Daily 成功解析 8 个 repo，8/8 README 文件已写入目录。索引见 [`../raw/2026-05-17/github-trending.json`](../raw/2026-05-17/github-trending.json)，README 原文见 [`../raw/2026-05-17/github-trending-readmes/`](../raw/2026-05-17/github-trending-readmes/)。证据等级统一按 `secondary-source` 处理：它只能说明项目当天在 GitHub Trending 页面可见，不代表官方发布、质量背书或长期趋势。

- [`oven-sh/bun`](https://github.com/oven-sh/bun)：JavaScript / TypeScript all-in-one runtime、bundler、test runner 和 package manager。README 能确认它作为单 executable 提供 runtime、toolchain 和文档入口；今天价值主要是 infra 背景，不是 AI/agent 主线。归档：[`../raw/2026-05-17/github-trending-readmes/oven-sh__bun.md`](../raw/2026-05-17/github-trending-readmes/oven-sh__bun.md)。
- [`K-Dense-AI/scientific-agent-skills`](https://github.com/K-Dense-AI/scientific-agent-skills)：scientific/research skills 集合，README 明确说从 Claude Scientific Skills 更名为 Scientific Agent Skills，支持 open Agent Skills standard，并覆盖 Cursor、Claude Code、Codex 等 agent。它解决的是把科研数据库、Python packages、clinical/research workflows 和科学写作做成可安装技能；风险是专业输出仍需 provenance、license、人工 review 和临床/金融边界。归档：[`../raw/2026-05-17/github-trending-readmes/K-Dense-AI__scientific-agent-skills.md`](../raw/2026-05-17/github-trending-readmes/K-Dense-AI__scientific-agent-skills.md)。
- [`obra/superpowers`](https://github.com/obra/superpowers)：coding-agent methodology / skills framework，README 说明它给 Claude Code、Codex CLI、Codex App、Gemini CLI、OpenCode、Cursor 等工具注入可组合 skills 和初始 instructions。它解决的是 agent 开发中的意图澄清、计划、实现和验证纪律；边界是方法论能否被 runtime 强制执行仍需实际验证。归档：[`../raw/2026-05-17/github-trending-readmes/obra__superpowers.md`](../raw/2026-05-17/github-trending-readmes/obra__superpowers.md)。
- [`Anil-matcha/Open-Generative-AI`](https://github.com/Anil-matcha/Open-Generative-AI)：开源 AI image/video generation studio，README 宣称支持 200+ models、Flux、Midjourney、Kling、Sora、Veo 等模型入口，并强调 self-hosted / MIT licensed / no content filters。它是 generative media tooling discovery signal；风险在模型授权、内容安全、服务密钥、滥用控制和“no content filters”带来的合规边界。归档：[`../raw/2026-05-17/github-trending-readmes/Anil-matcha__Open-Generative-AI.md`](../raw/2026-05-17/github-trending-readmes/Anil-matcha__Open-Generative-AI.md)。
- [`supertone-inc/supertonic`](https://github.com/supertone-inc/supertonic)：on-device multilingual TTS，README 记录 ONNX Runtime、本地推理、多语言和无云端调用。它和 agent 主线的交集在本地 voice interface 和隐私友好语音层，但不是今天的强 agent workflow 信号。归档：[`../raw/2026-05-17/github-trending-readmes/supertone-inc__supertonic.md`](../raw/2026-05-17/github-trending-readmes/supertone-inc__supertonic.md)。
- [`tinyhumansai/openhuman`](https://github.com/tinyhumansai/openhuman)：personal AI assistant / desktop agent，README 继续强调 private/simple/powerful、integrations、Memory Tree 和 personal AI context。它解决的是个人上下文如何持续汇入 agent；风险仍是 OAuth 权限、后台同步、删除治理和记忆污染。归档：[`../raw/2026-05-17/github-trending-readmes/tinyhumansai__openhuman.md`](../raw/2026-05-17/github-trending-readmes/tinyhumansai__openhuman.md)。
- [`ruvnet/RuView`](https://github.com/ruvnet/RuView)：把 commodity WiFi/ESP32 CSI 信号用于 spatial intelligence、vital sign monitoring 和 presence detection。它属于 camera-free sensing / edge intelligence discovery signal；不能把 README claim 当成医疗、安全或生产可部署能力。归档：[`../raw/2026-05-17/github-trending-readmes/ruvnet__RuView.md`](../raw/2026-05-17/github-trending-readmes/ruvnet__RuView.md)。
- [`colbymchenry/codegraph`](https://github.com/colbymchenry/codegraph)：Claude Code 语义代码图工具，README 记录 pre-indexed knowledge graph、symbol relationships、call graphs、framework-aware routes、file watcher 和本地 SQLite；它面向的具体问题是 agent 探索代码库时过度消耗 grep/read/tool calls。今天值得记录，因为它把 coding-agent context retrieval 做成了可本地安装的 memory/index layer；边界是 benchmark 和自动配置 claim 仍需在真实项目中复现。归档：[`../raw/2026-05-17/github-trending-readmes/colbymchenry__codegraph.md`](../raw/2026-05-17/github-trending-readmes/colbymchenry__codegraph.md)。

## 来源证据表

| 信号 | 证据等级 | 来源 | URL | 本地归档 |
| --- | --- | --- | --- | --- |
| ChatGPT personal finance fulltext | official-source | OpenAI Blog RSS/fulltext | https://openai.com/index/personal-finance-chatgpt | [`../raw/2026-05-17/rss-fulltext/openai-blog/openai-blog-a-new-personal-finance-experience-in-chatgpt-ada6c14251.autocli.md`](../raw/2026-05-17/rss-fulltext/openai-blog/openai-blog-a-new-personal-finance-experience-in-chatgpt-ada6c14251.autocli.md) |
| Databricks GPT-5.5 enterprise agent workflows | official-source | OpenAI Blog RSS/fulltext | https://openai.com/index/databricks | [`../raw/2026-05-17/rss-fulltext/openai-blog/openai-blog-databricks-brings-gpt-5.5-to-enterprise-agent-workflows-c64312c312.autocli.md`](../raw/2026-05-17/rss-fulltext/openai-blog/openai-blog-databricks-brings-gpt-5.5-to-enterprise-agent-workflows-c64312c312.autocli.md) |
| Codex for business operations | official-source | OpenAI Academy | https://openai.com/academy/codex-for-work/how-business-operations-teams-use-codex | [`../raw/2026-05-17/rss-fulltext/openai-blog/openai-blog-how-business-operations-teams-use-codex-b5b1610b25.autocli.md`](../raw/2026-05-17/rss-fulltext/openai-blog/openai-blog-how-business-operations-teams-use-codex-b5b1610b25.autocli.md) |
| Codex for data science | official-source | OpenAI Academy | https://openai.com/academy/codex-for-work/how-data-science-teams-use-codex | [`../raw/2026-05-17/rss-fulltext/openai-blog/openai-blog-how-data-science-teams-use-codex-cca00ce687.autocli.md`](../raw/2026-05-17/rss-fulltext/openai-blog/openai-blog-how-data-science-teams-use-codex-cca00ce687.autocli.md) |
| AlphaEvolve impact update | official-source | Google DeepMind Blog | https://deepmind.google/discover/blog/alphaevolve-how-our-gemini-powered-coding-agent-is-scaling-impact-across-fields/ | [`../raw/2026-05-17/rss-fulltext/google-deepmind-blog/google-deepmind-blog-alphaevolve-how-our-gemini-powered-coding-agent-is-scaling-impact-acro-049666cfa3.extracted.md`](../raw/2026-05-17/rss-fulltext/google-deepmind-blog/google-deepmind-blog-alphaevolve-how-our-gemini-powered-coding-agent-is-scaling-impact-acro-049666cfa3.extracted.md) |
| CodeGraph for Claude Code | secondary-source | GitHub Trending / README | https://github.com/colbymchenry/codegraph | [`../raw/2026-05-17/github-trending-readmes/colbymchenry__codegraph.md`](../raw/2026-05-17/github-trending-readmes/colbymchenry__codegraph.md) |
| FDE heats up again | limited secondary-source | Pragmatic Engineer RSS/fulltext | https://newsletter.pragmaticengineer.com/p/the-pulse-forward-deployed-engineering | [`../raw/2026-05-17/rss-fulltext/pragmatic-engineer/pragmatic-engineer-the-pulse-forward-deployed-engineering-heats-up-again-c1ec95ebdd.extracted.md`](../raw/2026-05-17/rss-fulltext/pragmatic-engineer/pragmatic-engineer-the-pulse-forward-deployed-engineering-heats-up-again-c1ec95ebdd.extracted.md) |
| Direct X usage and product signals | direct-x | `twitterapi.io` | multiple X URLs | [`../raw/2026-05-17/twitterapi-io-results.json`](../raw/2026-05-17/twitterapi-io-results.json) |

## X/Twitter 覆盖说明

- 本次 X/Twitter 只使用 `twitterapi.io` 的 `GET https://api.twitterapi.io/twitter/user/last_tweets` read endpoint，`includeReplies=false`。
- `twitterapi.io` 顶层状态为 `ok`，26 个账号均返回 `status=ok`；没有把任何 credential/API 异常当作“无推文”。
- 本轮共保留 118 条 direct-x 原始条目。保留数较高的账号包括 `Hesamation` 20 条、`steipete` 20 条、`cellinlab` 15 条、`corbin_braun` 12 条、`rileybrown` 11 条。
- `karpathy`、`OpenAI`、`AnthropicAI`、`rryssf_`、`frxiaobei`、`Yangyixxxx`、`genspark_ai`、`lidang`、`cnyzgkc`、`_LuoFuli` 请求成功但 kept_count 为 0；这表示 36 小时窗口和脚本过滤下没有保留条目，不等于账号没有更新。
- direct-x 内容包含个人观点、短评论、转发、产品线索和活动宣传；日报只把它们作为直接来源线索，不把个人观点写成官方事实。

## 运行结果与失败源

- RSS：31/31 成功；相关全文 49/49 成功；本轮没有 RSS failed source。
- GitHub releases：7/7 release Atom feed 成功；GitHub REST API 状态为 `skipped`，脚本按设计使用 Atom feed。
- GitHub release fulltext：Claude Code 5/5 ok；OpenAI Codex 5/5 limited，因此不能从 Codex release body 推断具体变更。
- GitHub Trending：1/1 成功，解析 8 个每日热门 repo，8 个 README 文件已归档。
- 官方页面：4/4 ok，0 limited，0 failed；Claude Blog 返回 5 个近期 blog metadata。
- X/Twitter：`twitterapi.io` 顶层 `ok`，26 个账号请求成功；没有 failed accounts，没有 Exa fallback。

## 不确定性与待验证项

- 已确认边界：本日报覆盖 2026-05-17 raw 输出、[`../raw/2026-05-17/manifest.json`](../raw/2026-05-17/manifest.json)、[`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)；GitHub Trending 只覆盖 `https://github.com/trending?since=daily` 当前 HTML 中解析到的 8 个 repo，以及脚本归档的 README；X/Twitter 只覆盖 `twitterapi.io` 返回并被 36 小时窗口保留的 direct-x 条目。
- 未覆盖范围：没有抓取登录态网页、没有补采 X thread/context、没有浏览器渲染 official pages、没有审计 GitHub Trending repo 源码质量或运行效果、没有复现 CodeGraph benchmark、没有检查 OpenAI personal finance 实际 UI 和账户连接流程。
- 推断项：【推断得出】本日报把“connected financial context + enterprise document agent benchmark + local code graph + agentic optimization”作为今天主线。依据是 OpenAI fulltext、Google DeepMind fulltext、GitHub Trending README 和 direct-x 同日出现；失效条件是后续产品文档、源码或真实运行显示这些只是 marketing framing、demo 项目或不可复现实现。
- 待验证项：实际验证 ChatGPT Finances 的 Plaid/Intuit permission、data deletion、Financial memories 和 professional-advice disclaimer；读取 Databricks AgentBricks / Agent Supervisor API 文档确认 GPT-5.5 production workflow；复现 CodeGraph 在本地大型 repo 的 tool-call 和 freshness claim；检查 AlphaEvolve API / Google Cloud commercial access 与客户案例边界；获取 Pragmatic Engineer FDE 正文或其它公开材料确认 FDE role demand 细节。

## 运行统计

- 新增条目：`seen_added=42`。
- 高信号条目：8 条。
- 失败来源：RSS failed 0 个；official page failed 0 个；twitterapi.io failed accounts 0 个。
- limited 来源：OpenAI Codex release fulltext limited 5 条；Pragmatic Engineer FDE 原文只读到付费墙前摘要。

## 完成审计

- 用户目标拆解：稳定来源采集、twitterapi.io direct-x 采集、状态更新、日报生成、trend report 生成、enabled trends 检查、失败/limited 来源说明、输出路径汇总。
- 证据对应：raw JSON 写入 [`../raw/2026-05-17/`](../raw/2026-05-17/)，状态文件写入 [`../state/source-health.json`](../state/source-health.json) 与 [`../state/seen.json`](../state/seen.json)，日报为当前文件。
- 状态同步：`update-state.py` 已生成 [`../raw/2026-05-17/manifest.json`](../raw/2026-05-17/manifest.json)，并更新 source health 与 seen。
- 来源边界：所有 X/Twitter 内容标为 `direct-x`，GitHub Trending 标为 `secondary-source`，官方 RSS/GitHub release/official pages 标为 `official-source`、official metadata 或 limited；未用 Exa fallback。
- Trend 检查：`memory-dream`、`financial-agents`、`forward-deployed-engineering` 均有新增趋势信号并已更新专题；trend raw 归档见 [`../trend/raw/2026-05-17/`](../trend/raw/2026-05-17/)。
