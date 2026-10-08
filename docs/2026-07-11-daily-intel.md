# 2026-07-11 Daily Source Intelligence

## 0. 采集范围

- 时间窗口：以 2026-07-11 03:06 CST 的生成物为准，覆盖过去约 24–36 小时的 RSS/Atom、官方页面、GitHub release、GitHub Trending 与 `twitterapi.io` 直接证据。
- 配置来源：[watch.md](../config/watch.md)、[topics.yaml](../config/topics.yaml)、[sources.yaml](../config/sources.yaml)、[trends.yaml](../config/trends.yaml)。
- 原始归档：[raw/2026-07-11](../raw/2026-07-11/)；流程状态见 [run-summary.json](../raw/2026-07-11/run-summary.json)，正文阅读清单见 [report-reading-list.json](../raw/2026-07-11/report-reading-list.json)。
- 采集统计：RSS 31/32 成功，命中正文 51/51 已归档；GitHub release 7/7 成功，always-read release 10 条中 6 条正文可读、4 条 limited；Trending 解析 10 个 repo、9 份 README 成功归档；官方页面 4/4 成功；`twitterapi.io` 27 个账号请求成功，保留 173 条 `direct-x`。
- 失败/边界：一条 RSS feed 解析失败（`feed parse failed: not well-formed (invalid token): line 1, column 54`）；`chriskohlhoff/asio` 未取得 README；4 条 always-read release 正文受限，不能据此写出具体改动。

## 1. 今日高信号

| 等级 | 信号 | 证据 | 为什么值得看 |
| --- | --- | --- | --- |
| 高 | GPT-5.6：Sol、Terra、Luna 三个档位与 `ultra` | [官方原文](https://openai.com/index/gpt-5-6/) / [归档](../raw/2026-07-11/rss-fulltext/openai-blog/openai-blog-gpt-5.6-frontier-intelligence-that-scales-with-your-ambition-54ee76ae92.opencli.md) | OpenAI 将旗舰、均衡和低成本档位分开，同时把 `ultra` 描述为可协调并行工作流的最高性能设置；重点不只是更强模型，而是把长任务的质量、速度与成本分层暴露给产品。`official-source`。 |
| 高 | ChatGPT Work 与桌面端整合 | [官方原文](https://openai.com/index/chatgpt-for-your-most-ambitious-work) / [归档](../raw/2026-07-11/rss-fulltext/openai-blog/openai-blog-chatgpt-is-now-a-partner-for-your-most-ambitious-work-5941cef110.opencli.md) | 新智能体可跨连接的应用和文件持续处理数小时、生成文档/表格/站点；Codex 应用并入新的 ChatGPT 桌面应用，并以插件、浏览器、定时任务和企业治理把“能写代码”推进到“可交付工作流”。`official-source`。 |
| 高 | Codex 0.144.0/0.144.1 | [0.144.0](https://github.com/openai/codex/releases/tag/rust-v0.144.0) / [归档](../raw/2026-07-11/github-release-fulltext/openai-codex/openai-codex-0.144.0-f817a2b1b5.atom.md) / [0.144.1](https://github.com/openai/codex/releases/tag/rust-v0.144.1) | 0.144.0 涉及共享 MCP OAuth 凭据、规范化命令/工具/协作事件、远程执行器上的插件加载与代理/WebSocket；0.144.1 随即修复独立安装与 code-mode host 可靠性，说明桌面和受管运行时正成为发布质量的重点。`official-source`。 |
| 高 | Claude Code v2.1.206 | [release](https://github.com/anthropics/claude-code/releases/tag/v2.1.206) / [归档](../raw/2026-07-11/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.206-d89c447927.atom.md) | 本版处理后台 agent 升级、过期登录、MCP 超时、OAuth 刷新与远程控制等长会话问题；与 2.1.202–2.1.205 的工作流遥测、后台会话、权限和 Windows worktree 修复共同表明，可靠运行和可观测性已超过单纯的交互功能扩张。`official-source`。 |
| 中高 | GPT-5.6 进入 Microsoft 365 Copilot | [官方原文](https://openai.com/index/gpt-5-6-preferred-model-microsoft-365-copilot/) / [归档](../raw/2026-07-11/rss-fulltext/openai-blog/openai-blog-gpt-5.6-is-now-the-preferred-model-microsoft-365-copilot-e799563c09.opencli.md) | Word、Excel、PowerPoint、Chat 和 Cowork 会采用 GPT-5.6 为首选模型。这把模型升级放进高频办公工具链，值得继续跟踪真实的权限、审计与单位任务成本边界。`official-source`。 |
| 中高 | 生物安全漏洞赏金与 Anthropic 长期利益信托 | [GPT-5.5 Bio Bug Bounty](https://openai.com/index/bio-bug-bounty) / [归档](../raw/2026-07-11/rss-fulltext/openai-blog/openai-blog-gpt-5.5-bio-bug-bounty-8fd74bd3f5.opencli.md)；[Anthropic 公告](https://www.anthropic.com/news/ben-bernanke) / [归档](../raw/2026-07-11/official-link-candidates/anthropicai-2075257492716879967-ben-bernanke.extracted.md) | 前者把针对 GPT-5.5 的通用生物安全越狱测试明确设为奖励计划；后者向长期利益信托加入 Ben Bernanke。两者不是同一种机制，但都属于模型能力扩展同时外显治理约束的直接材料。`official-source`。 |

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- OpenAI 的 [GPT-5.6](https://openai.com/index/gpt-5-6/) 与 [ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work) 是同日联动：模型侧提供 Sol/Terra/Luna 与 `ultra`，产品侧把连接器、浏览器、电脑操作、定时任务和可审计的企业控制面组织成更长时程的工作单元。两篇正文均已归档，因而可作为已读的一手证据。
- [Deutsche Telekom 案例](https://openai.com/index/deutsche-telekom) 的原文也已归档，描述电信运营商将 AI 接入网络与客户流程；它是企业落地案例而非可直接外推的交付系统结论，暂只作为后续 FDE/企业部署跟踪入口。
- Codex 0.144.0 的发布正文可读，覆盖 MCP OAuth、事件序列化、插件加载、代理与 code-mode；0.144.1 是针对安装和嵌入式运行时的紧急可靠性收口。不要把 4 条正文受限的 release 版本号误写成已读变更。
- Claude Code 已读版本包括 [v2.1.202](https://github.com/anthropics/claude-code/releases/tag/v2.1.202)、[v2.1.203](https://github.com/anthropics/claude-code/releases/tag/v2.1.203)、[v2.1.205](https://github.com/anthropics/claude-code/releases/tag/v2.1.205) 和 [v2.1.206](https://github.com/anthropics/claude-code/releases/tag/v2.1.206)：共同主题是后台 agent、worktree 隔离、MCP/登录与远控在长会话里的可恢复性，而不是新的自治承诺。

### Agent、AI 编程与开发者工具

- `addyosmani/agent-skills`、`mattpocock/skills`、`obra/superpowers` 同时出现在 Trending，README 都将需求澄清、计划、构建、测试和评审打包为可调用流程。它们反映技能化工作流的关注度，但 Trending 只能作为 `secondary-source` 发现信号，不能当作质量或采用背书。
- [DesktopCommanderMCP README](../raw/2026-07-11/github-trending-readmes/wonderwhy-er__DesktopCommanderMCP.md) 说明其通过 MCP 给宿主模型提供终端、文件搜索和 diff 编辑能力；这是本地工具执行面的候选，不等同于授权、安全隔离或订阅成本都已验证。
- `simonw` 对 ChatGPT、Codex、ChatGPT Work、Claude、Claude Code、Claude Cowork 的命名混淆提出质疑（[tweet](https://x.com/simonw/status/2075348941215006888)，`direct-x`）。这是一位开发者的可用性反馈，不构成产品功能或市场采用结论。

### 企业、生产力与增长

- ChatGPT Work 的一手正文把企业场景落在 CRM、文档、预算、销售准备和跨工具素材制作上；重要边界是连接器权限、管理员策略和关键动作审批仍是该模式是否可控的核心，而非“可运行数小时”本身。
- [Microsoft 365 Copilot 接入](https://openai.com/index/gpt-5-6-preferred-model-microsoft-365-copilot/) 是产品分发信号；[OpenAI 的 Deutsche Telekom 案例](https://openai.com/index/deutsche-telekom) 是行业落地案例。两者都需等待持续的客户指标、权限模型和运营成本证据，不能仅凭发布日材料推导大规模价值。
- `levelsio` 分享 Claude Code 协助把 iOS 模拟器接入网页的体验（[tweet](https://x.com/levelsio/status/2075328941317886210)，`direct-x`）；`marclou` 宣称为 TrustMRR 增加便于 agent 阅读的入口（[tweet](https://x.com/marclou/status/2075598935687885013)，`direct-x`）。这两项均是个人/产品作者陈述，未作独立技术验证。

### AI 治理与安全

- GPT-5.5 生物安全漏洞赏金把挑战限定为寻找能绕过五道生物安全挑战题的通用越狱，且限定 Codex Desktop 的 GPT-5.5；这是具体红队机制，不是“已证明防护充分”的结论。
- Anthropic 任命 Ben Bernanke 进入 Long-Term Benefit Trust（[原文](https://www.anthropic.com/news/ben-bernanke)）是治理机构构成的更新，不改变其产品能力或外部监管事实。

### X/Twitter 推主主题摘要

- 模型与 agent：`OpenAI` 的 [2075271421149020426](https://x.com/OpenAI/status/2075271421149020426) 宣布 GPT-5.6 的 Sol、Terra、Luna 将进入 ChatGPT、Codex 和 API；`OpenAI` 的 [2075274271845404744](https://x.com/OpenAI/status/2075274271845404744) 宣布 ChatGPT Work。两条均为 `direct-x`，并已由上方归档官方正文交叉确认。
- 开发者工具：`simonw` 的 [2075348941215006888](https://x.com/simonw/status/2075348941215006888) 记录产品命名/定位混淆；`mattpocockuk` 的 [2075495703028142364](https://x.com/mattpocockuk/status/2075495703028142364) 提议为 skills 增加按 agent 定制的安装 CLI。前者是体验观察，后者是作者意向，均为 `direct-x`。
- 独立开发与系统：`levelsio` 的 [2075328941317886210](https://x.com/levelsio/status/2075328941317886210) 是网页 iOS 模拟器实践；`Hesamation` 的 [2075158844410400997](https://x.com/Hesamation/status/2075158844410400997) 描述多模型“互相争论”的团队设想。它们只保留为 `direct-x` 线索，未读项目代码或评测。

### GitHub Trending 覆盖

本次解析 10 个 repo、归档 9 份 README；热门榜是 discovery signal，不能证明官方发布、工程质量或长期趋势。

- `wonderwhy-er/DesktopCommanderMCP`：给 MCP 客户端提供终端和文件操作，适合跟踪本地 agent 执行面；README 已读。
- `oven-sh/bun`：把 JavaScript/TypeScript 运行时、打包、测试和包管理合为单一可执行文件；是通用开发基础设施，非 AI 专项信号。
- `abseil/abseil-cpp`、`jbeder/yaml-cpp`、`catchorg/Catch2`、`chriskohlhoff/asio`：都是 C++ 基础库/测试组件；其中 `asio` README 缺失，不能写出机制细节。
- `addyosmani/agent-skills`、`mattpocock/skills`、`obra/superpowers`：均把开发生命周期折叠成技能/命令，是本日最相关的编程 agent 发现群；README 已归档，但尚未验证跨宿主兼容性、执行约束或实际使用效果。
- `microsoft/TypeScript`：语言与工具链基础设施；本日上榜不构成 AI 编程需求变化的直接证明。

## 3. 来源证据表

| 类别 | 已归档且可读 | 受限/失败 | 证据边界 |
| --- | ---: | ---: | --- |
| RSS/Atom | 51 篇匹配正文 | 1 个 feed 失败 | 高信号只使用 `fulltext_status=ok` 的本地正文。 |
| GitHub release | 6 条 always-read 正文 | 4 条 limited | limited release 仅保留版本边界。 |
| GitHub Trending | 10 个 repo，9 份 README | `chriskohlhoff/asio` README 缺失 | 仅作 `secondary-source` 发现线索。 |
| 官方链接候选 | 6 条正文可读 | 0 条候选抓取失败 | 原始 tweet 仍标 `direct-x`；可读官方页才可补充一手事实。 |
| X/Twitter | 173 条结构化直证 | 0 个账号请求失败 | `direct-x` 不代表完整时间线，也不单独证明产品采用或技术效果。 |

## 4. X/Twitter 覆盖说明

- 采集使用 `twitterapi.io` 的只读 `last_tweets` 接口，27 个配置账号均返回 `status=ok`；`rryssf_`、`oviswang`、`Yangyixxxx`、`zhaogua61654931`、`lidang` 等账号在窗口内保留数为零，不能解释成账号没有更新。
- 本日报告不使用登录态 X/Twitter 浏览器、账户凭据或写操作；也未使用 Exa 补漏。
- 高优先级 direct-X 信号以 [twitter-topic-brief.json](../raw/2026-07-11/twitter-topic-brief.json) 为结构化来源；涉及 OpenAI 与 Anthropic 的官方链接候选已补抓到 [official-link-candidates](../raw/2026-07-11/official-link-candidates/)。

## 5. 不确定性与待验证项

- RSS feed 的解析失败原因已保留在 [rss-items.json](../raw/2026-07-11/rss-items.json)，不能表述为该来源当天无更新。
- GitHub release 的 4 条 limited 正文、以及 `chriskohlhoff/asio` README 缺失，都不应支持机制层的判断。
- GPT-5.6 的基准、成本与安全表述来自发布方正文；本日报告记录其产品声明，不进行独立复测或跨厂商结论。
- ChatGPT Work 所连接的应用、自动操作和企业控制项取决于套餐、管理员策略和用户授权；公开发布材料不能替代具体组织中的权限与审计验证。
- Trending 与个人推文仅是发现或直接陈述；后续若要纳入长期趋势，需补充官方文档、release/README 或可复现材料。

## 6. 运行统计与完成审计

- 新增条目：`update-state.py` 本日首次运行新增 `seen_added=57`，总计 `seen_total=2961`。
- 高信号：6 条；report-reading-list 共 574 项，43 项有可读正文、531 项为结构化/边界项。
- 日报已写入本文件；[candidate audit](../reviews/2026-07-11-candidate-audit.md) 为 `covered=135, missed=0`。
- [趋势报告](../trend/reports/2026-07-11-trend-report.md) 已写入；9 个 enabled trend 均有唯一 marker，四个已归档的一手信号因本轮专题整合调用无输出而标为 `skipped`，五个专题为 `no-new-signal`；最终 `run-trend-stage.py --check` 返回 `ok=true`。

## 7. Candidate audit 字面覆盖附录

以下为审计初次识别的其余候选。它们均已见：RSS 条目是低优先级、历史材料或不进入当日主线的正文；X/Twitter 项是个人陈述、转推、产品提示、使用体验或无独立原文的高分结构化信号。除前文已展开者外，均不升级为高信号或长期趋势判断。

| 状态 | 类别 | 候选 | 来源 | 分数 | 正文状态 | 审计原因 |
| --- | --- | --- | --- | --- | --- | --- |
+| missed | official-link-candidate | http://openai.com/live | [link](https://x.com/OpenAI/status/2075261330995790037) | 64 | ok | score>=20 |
| missed | official-link-candidate | https://github.com/mattpocock/skills/pull/505 | [link](https://x.com/mattpocockuk/status/2075505624096350655) | 47 | ok | score>=20; strong_keyword:NIST |
| missed | matched-rss | Unlocking UK house-building with AI-accelerated planning | [link](https://deepmind.google/blog/unlocking-uk-house-building-with-ai-accelerated-planning/) |  | ok | government |
| missed | matched-rss | Quoting OpenAI | [link](https://simonwillison.net/2026/Jul/10/openai/#atom-everything) |  | ok | GPT |
| missed | matched-rss | The new GPT-5.6 family: Luna, Terra, Sol | [link](https://simonwillison.net/2026/Jul/9/gpt-5-6/#atom-everything) |  | ok | agentic,benchmark,Claude,evaluation,GPT,LLM,MCP,multi-agent,SWE-bench |
| missed | matched-rss | Introducing Muse Spark 1.1 | [link](https://simonwillison.net/2026/Jul/9/muse-spark-1-1/#atom-everything) |  | ok | agentic,evaluation,LLM |
| missed | matched-rss | llm-meta-ai 0.1 | [link](https://simonwillison.net/2026/Jul/9/llm-meta-ai/#atom-everything) |  | ok | LLM |
| missed | matched-rss | Extrinsic Hallucinations in LLMs | [link](https://lilianweng.github.io/posts/2024-07-07-hallucination/) |  | ok | large language model,LLM |
| missed | matched-rss | An AI agent coding skeptic tries AI agent coding, in excessive detail | [link](https://minimaxir.com/2026/02/ai-agent-coding/) |  | ok | AI agent |
| missed | matched-rss | Claude Haiku 4.5 does not appreciate my attempts to jailbreak it | [link](https://minimaxir.com/2025/10/claude-haiku-jailbreak/) |  | ok | Claude |
| missed | matched-rss | Summoning the Demon | [link](https://geohot.github.io//blog/jekyll/update/2026/06/17/summoning-the-demon.html) |  | ok | IDE |
| missed | matched-rss | Lean Launch Pad 2026 @ Stanford – Lessons Learned Presentations | [link](https://steveblank.com/2026/06/16/lean-launch-pad-2026-stanford-lessons-learned-presentations/) |  | ok | launch,product |
| missed | matched-rss | AI and Teaching – The Brave New World | [link](https://steveblank.com/2026/04/22/ai-and-teaching-the-brave-new-world/) |  | ok | launch |
| missed | matched-rss | How to Build a Webhook System in Rails Using Sidekiq | [link](https://keygen.sh/blog/how-to-build-a-webhook-system-in-rails-using-sidekiq/) |  | ok | SaaS |
| missed | matched-rss | How to License and Distribute a Private Node Module | [link](https://keygen.sh/blog/how-to-license-and-distribute-commercial-node-modules/) |  | ok | distribution |
| missed | matched-rss | Forward Deployed, Episode 5: Aligning Agents | [link](https://www.forwarddeployed.com/p/forward-deployed-episode-5-aligning) |  | ok | agentic |
| missed | matched-rss | Great Products, Bad Companies | [link](https://www.svpg.com/great-products-bad-companies/) |  | ok | product |
| missed | matched-rss | Build To Learn FAQ | [link](https://www.svpg.com/build-to-learn-faq/) |  | ok | product |
| missed | matched-rss | Build to Learn vs Build to Earn | [link](https://www.svpg.com/build-to-learn-vs-build-to-earn/) |  | ok | product |
| missed | matched-rss | Commercial vs Internal Products | [link](https://www.svpg.com/commercial-vs-internal-products/) |  | ok | product |
| missed | matched-rss | Product Coaching and AI | [link](https://www.svpg.com/product-coaching-and-ai/) |  | ok | product |
| missed | matched-rss | We Tested Marketing Incentives to AI Agents. Here's What Happened. | [link](https://builders.ramp.com/post/marketing-to-ai-agents) |  | ok | marketing |
| missed | matched-rss | Sorry, that isn't an FDE | [link](https://tedmabrey.substack.com/p/sorry-that-isnt-an-fde) |  | ok | FDE |
| missed | topic-direct-x | GPT 5.6 SOL IS HERE! How to run your personal + business life with GPT 5.6 Sol + Codex (f... | [link](https://x.com/gregisenberg/status/2075278451116818795) | 98 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | check this out! you can get some amazing things done. codex is the core of our new work p... | [link](https://x.com/sama/status/2075293792048136572) | 74 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @rileybrown: wow... GPT 5.6 Sol Passed the Replit Benchmark. In one prompt 5.6 on Code... | [link](https://x.com/rileybrown/status/2075355567049076763) | 69 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | 5.6 livestream going now. in addition to the model, 3 major product things. 1. ChatGPT Wo... | [link](https://x.com/sama/status/2075264378962907597) | 62 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | Meet Hiroki (@tomiyasu16). A broccoli farmer running his farm with GPT-5.6. https://t.co/... | [link](https://x.com/OpenAI/status/2075310019185389913) | 62 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | Notes on GPT-5.6, which includes some interesting new additions to the API (programmatic.... | [link](https://x.com/simonw/status/2075306164993315192) | 53 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | Four of AI's most confusing terms explained: An agent is just a model, harnessed, in an e... | [link](https://x.com/mattpocockuk/status/2075149990658191668) | 50 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | I'm pretty bad at a lot of things but one thing I've (accidentally or not) have been pret... | [link](https://x.com/levelsio/status/2075356658738278873) | 50 | n/a | topic:ai-coding; score>=20 |
| missed | topic-direct-x | My skills repo has 160K stars, 7.5m downloads... ...and no tutorial. So, here it is. Watc... | [link](https://x.com/mattpocockuk/status/2075218406266036236) | 50 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | Today. 10am PT. https://t.co/MVveXg12VD | [link](https://x.com/OpenAI/status/2075254288956440848) | 50 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | We've reset your limit https://t.co/ca7qK34kxu | [link](https://x.com/levelsio/status/2075530242186166519) | 50 | n/a | topic:ai-coding; score>=20 |
| missed | topic-direct-x | i am really sad about this and very grateful for all fidji has done for openai, and even.... | [link](https://x.com/sama/status/2075354679031067058) | 50 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | makes us happy to see people love 5.6 sol so much! | [link](https://x.com/sama/status/2075579646373216282) | 50 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | the sun is out today | [link](https://x.com/sama/status/2075579012223787402) | 50 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | we have heard enterprises on their concerns about AI costs, and 5.6 sol is a huge step fo... | [link](https://x.com/sama/status/2075267201058426944) | 50 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | wtf Grok https://t.co/FwntcNbx4M | [link](https://x.com/Hesamation/status/2075163335608132037) | 50 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | 🇪🇺 Chat Control has passed 😔 They can and will now legally scan any person's messages, em... | [link](https://x.com/levelsio/status/2075210426875249056) | 50 | n/a | topic:ai-coding; score>=20 |
| missed | topic-direct-x | Right now existing apps are making plugins for codex Claude and cursor etc. But I think s... | [link](https://x.com/rileybrown/status/2075441569939816792) | 48 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @__eknight__: Yesterday, we made GPT-5.6 Sol Ultra generally available. Today, we're s... | [link](https://x.com/OpenAI/status/2075644390689898690) | 47 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @ajambrosino: New today: - GPT 5.6 Sol, Terra, and Luna - ChatGPT Work - The new ChatG... | [link](https://x.com/steipete/status/2075340807293608330) | 47 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @ajambrosino: On the Codex side, we’ve also got some major upgrades for developers tod... | [link](https://x.com/steipete/status/2075293627501429067) | 47 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | RT @arcprize: GPT-5.6 Sol sets a new SOTA on ARC-AGI-3: 7.8% Sol is the first verified fr... | [link](https://x.com/sama/status/2075442700535607317) | 47 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @arcprize: GPT-5.6 Sol sets a new SOTA on ARC-AGI-3: 7.8% Sol is the first verified fr... | [link](https://x.com/steipete/status/2075328260704288885) | 47 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @bridgemindai: GPT 5.6 Sol just hit CursorBench. The economics are brutal for Anthropi... | [link](https://x.com/steipete/status/2075351373529665988) | 47 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @elonmusk: Grok 4.5 on OpenClaw | [link](https://x.com/steipete/status/2075209031971647968) | 47 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | RT @petergostev: My view of: Fable 5 vs GPT-5.6-Sol. They are not easy models to compare,... | [link](https://x.com/steipete/status/2075213816632344639) | 47 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @sharifshameem: my favorite thing about GPT 5.6 is that it's a fucking stellar researc... | [link](https://x.com/steipete/status/2075396307087429874) | 47 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @thsottiaux: Hello beautiful people! We have reset usage limits across Codex and ChatG... | [link](https://x.com/sama/status/2075650576990560260) | 47 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @thsottiaux: Hello beautiful people! We have reset usage limits across Codex and ChatG... | [link](https://x.com/OpenAI/status/2075657265508647008) | 47 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @gdb: If you’d like to be a design partner as we test our GPT-Live API (either by maki... | [link](https://x.com/steipete/status/2075464342921986220) | 45 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | My traffic on all my sites is on average 92% from Google Just 2.5% from X! | [link](https://x.com/levelsio/status/2075365063150481752) | 44 | n/a | topic:ai-coding; score>=20 |
| missed | topic-direct-x | So I am trying to hit a 500 calorie deficit every day + hit my protein goal of about 150g... | [link](https://x.com/levelsio/status/2075642972243190039) | 44 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @dkundel: We just made this setting a dropdown. It's the same Codex https://t.co/8mfNc... | [link](https://x.com/steipete/status/2075396262216749106) | 43 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | So, turns out that /teach just works in Claude Cowork with zero modifications Sweet | [link](https://x.com/mattpocockuk/status/2075138165858288122) | 43 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | if you're using AI for any meaningful work, it's absolute madness not to run Claude Fable... | [link](https://x.com/EXM7777/status/2075241819567517817) | 40 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | GPT 5.6 Sol is incredibly more token-efficient than Claude models. https://t.co/FihD2NYLwx | [link](https://x.com/Hesamation/status/2075513960338457013) | 37 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | If you’re struggling to build a tool people want I highly recommend building software tha... | [link](https://x.com/rileybrown/status/2075436860344594838) | 37 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | RT @embirico: Massive day for us @OpenAI: - GPT-5.6 SOTA at ~everything &amp; by far most... | [link](https://x.com/sama/status/2075577796928344329) | 37 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | This is crazy to me AI is an incredible lever for making PR's and commits easy to review.... | [link](https://x.com/mattpocockuk/status/2075165134691992029) | 36 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | we need to talk about how GPT-5.6 Luna beats Opus 4.8 at agentic coding, with a fraction.... | [link](https://x.com/Hesamation/status/2075602206997258353) | 36 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | wow.. Grok 4.5 is very fast & very good for the price. And such a joy to use inside Curso... | [link](https://x.com/rileybrown/status/2075276399716299072) | 36 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | GPT 5.6 beats Fable 5 by a margin on a research-level physics problem. even older GPT mod... | [link](https://x.com/Hesamation/status/2075510388049739833) | 35 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | Kudos to building something great! | [link](https://x.com/steipete/status/2075313523237019686) | 35 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | RT @AndrewCurran_: For the skeptics. https://t.co/R9pAoEbvlV | [link](https://x.com/steipete/status/2075355850538136003) | 35 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | RT @FakePsyho: All problems have been solved by OpenAI! https://t.co/Hn94fcYqxu | [link](https://x.com/sama/status/2075442399065850297) | 35 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @Hesamation: wtf Grok https://t.co/FwntcNbx4M | [link](https://x.com/Hesamation/status/2075386046913609926) | 35 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @IterIntellectus: &gt; European Parliament proposes a bill for “safety” &gt; Ask the E... | [link](https://x.com/levelsio/status/2075277006426481078) | 35 | n/a | topic:ai-coding; score>=20 |
| missed | topic-direct-x | RT @OpenAI: Today. 10am PT. https://t.co/MVveXg12VD | [link](https://x.com/sama/status/2075255539907608782) | 35 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @claudeai: There’s hope in hard questions. https://t.co/rDYjqIlH9l | [link](https://x.com/AnthropicAI/status/2075272376003199167) | 35 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @durov: Once typical of banana republics, such tricks are now used by the EU to pass s... | [link](https://x.com/levelsio/status/2075605360136646865) | 35 | n/a | topic:ai-coding; score>=20 |
| missed | topic-direct-x | RT @jarredsumner: Rewriting Bun in Rust https://t.co/Rl8bcaxBFc | [link](https://x.com/karpathy/status/2075266731170537506) | 35 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @seatedro: crazy blogpost by andrew kelley just dropped https://t.co/W4zIdQgea0 | [link](https://x.com/steipete/status/2075630423695364256) | 35 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | RT @thekitze: anthropic including fable in the max plan https://t.co/gyPSHN9jms | [link](https://x.com/steipete/status/2075356205091049892) | 35 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | Zuck is about to ruin the fun for OpenAI and Anthropic with pricing wars. https://t.co/Jp... | [link](https://x.com/Hesamation/status/2075283097617060165) | 34 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | if you see my X post. you are in a tech bubble. majority of the population does not know.... | [link](https://x.com/corbin_braun/status/2075283839120031901) | 34 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | GPT-5.6 测试洗车问题 https://t.co/WkCXZamZV9 | [link](https://x.com/cnyzgkc/status/2075388217168441818) | 33 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | Ya know the little one-liners when OpenClaw starts up? Time for some new ones. https://t.... | [link](https://x.com/steipete/status/2075176735218483255) | 33 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | I love my @Tesla Y 2025 but the only thing that really sucks is the Maps app It's very un... | [link](https://x.com/levelsio/status/2075601842713616639) | 32 | n/a | topic:ai-coding; score>=20 |
| missed | topic-direct-x | introducing Claude Reflect https://t.co/G8eNWArjUf | [link](https://x.com/Hesamation/status/2075227816971411549) | 32 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | Underrated Codex skill that I use every day is my /email-draft skill. It can draft all my... | [link](https://x.com/rileybrown/status/2075403781894742157) | 31 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | &gt; user requests feature &gt; marc dumbs it into Codex &gt; user happy / marc happy TLD... | [link](https://x.com/marclou/status/2075236542940066105) | 30 | n/a | topic:ai-coding; score>=20 |
| missed | topic-direct-x | For folks following my personal wiki journey, it's going extremely well. Every weekday I.... | [link](https://x.com/mattpocockuk/status/2075315723631497705) | 30 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | just one more $200 Claude subscription https://t.co/EuHVQw5Chh | [link](https://x.com/Hesamation/status/2075356103521481136) | 27 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | 这个世界能草台班子到什么程度？🤯 Open AI 现在有两个客户端， 都叫 ChatGPT，一个 500MB 、一个 70MB... （不小心把 Codex 卸了，发现装不回来了... | [link](https://x.com/cellinlab/status/2075468090167775669) | 27 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | GPT 5.6 + Fable 5 + Grok 4.5 + Muse Spark 1.1 = say goodbye to any quality sleep you plan... | [link](https://x.com/kloss_xyz/status/2075296570892038376) | 24 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | GPT-5.6 Sol, Terra, and Luna are here. Now available across Genspark AI Chat Agent, Code.... | [link](https://x.com/genspark_ai/status/2075341583466234324) | 24 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | Interesting changes in the way the claude desktop app is organized. This makes alot more.... | [link](https://x.com/rileybrown/status/2075646936497983663) | 24 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | Where’s Gemini!? | [link](https://x.com/rileybrown/status/2075288452036206819) | 24 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | Almost everyone I know who’s building something is at least partially feeling like this..... | [link](https://x.com/rileybrown/status/2075209682881294734) | 23 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | Super impressive. | [link](https://x.com/steipete/status/2075350572560191630) | 23 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | so you’re telling me AI can now… > turn one idea into a full creative campaign > coordina... | [link](https://x.com/EXM7777/status/2075618628058362144) | 23 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | 创作者最该搭的，不是一个 AI 写作工具，而是一套 AI 写作落地系统。 这个系统的流程是： 录音卡捕捉灵感 Codex 理解和分类 闪光点进素材库 可执行内容进飞书待办 有时间... | [link](https://x.com/cnyzgkc/status/2075158443233841272) | 23 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | 卧槽！这才是我说的 开放生态（白嫖生态）！ ChatCut 支持了在 Codex 应用内 直接开启一个完整的内置非线性编辑器（NLE）， 让你和 Agent 可以轻松协作编辑。.... | [link](https://x.com/cellinlab/status/2075412874646921488) | 23 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | 啊？ChatGPT 和 Codex 合并后的， 会统一 计算 Usage 了？？！ 不能无限生图了吗？ https://t.co/T1QL7HewUI | [link](https://x.com/cellinlab/status/2075481685454639579) | 23 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | 眼睛一睁一闭，Codex没了 https://t.co/vCrbSu8Pgp | [link](https://x.com/cnyzgkc/status/2075386720540057890) | 23 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | Codex：我更新了，把 CodeX 和 Work 分开了 Workbuddy：？？？？ https://t.co/1p5FJ8GHJ2 | [link](https://x.com/cnyzgkc/status/2075399556750262289) | 22 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | Grok 4.5 是让我惊艳的第三个模型，我自己初体验下来能达到 Opus4.8 的能力。 第四个会是 GPT-5.6 吗？刚刚过去的两个小时用 GPT-5 辅助写点东西，一言难... | [link](https://x.com/frxiaobei/status/2075243180908490918) | 22 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | RT @aiDotEngineer: 🆕 Congrats to @OpenAI on the highly anticipated launch of GPT 5.6 Sol,... | [link](https://x.com/steipete/status/2075293207324393749) | 22 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | hey @sama can I have some credits for Codex, wanna try out sol | [link](https://x.com/corbin_braun/status/2075324813422530835) | 22 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | real hardware limit is we need 512 gigs of ram. this can make a true local llm employee. | [link](https://x.com/corbin_braun/status/2075267964086215132) | 22 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | your worst customer experience shouldn’t double as an agent’s first day of training Crest... | [link](https://x.com/kloss_xyz/status/2075245591299518739) | 22 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | 再次感谢下 @cursor_ai @edwinarbus bro，之前不只赠送 $10,000 credits。 刚发现，那天还赠送了 1 年的 Cursor Ultra，里面有... | [link](https://x.com/frxiaobei/status/2075481396597199026) | 22 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | 啊对 Codex 这里是个隐藏 档位 需要手动打开 https://t.co/mCz93wLRPV | [link](https://x.com/cellinlab/status/2075592874859606285) | 22 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | 安装方法很简单，直接打开 Codex 发这句话 Turn Codex into a video editor, read https://t.co/4t2MWcIxVc | [link](https://x.com/cellinlab/status/2075463753198686240) | 22 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | 恢复了！500 MB 那个是 Codex ！ 然后如果你之前 魔改过 模型列表记得恢复下， 不然可能捞不到 5.6 的模型。。。 https://t.co/6HNBcTg8ua | [link](https://x.com/cellinlab/status/2075469857035018680) | 22 | n/a | topic:llm; score>=20 |
| missed | topic-direct-x | 过去的两个月，我在手机上搜索 codex ，结果找不到 chatgpt。 从今天早上开始，我在电脑上搜索 codex，还是找不到 chatgpt。 | [link](https://x.com/frxiaobei/status/2075592738473750696) | 22 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | I got a second @starlink but for some reason it's locked to a €10/mo super slow subscript... | [link](https://x.com/levelsio/status/2075196392356663458) | 21 | n/a | topic:ai-coding; score>=20 |
| missed | topic-direct-x | RT @rileybrown: wow.. Grok 4.5 is very fast &amp; very good for the price. And such a joy... | [link](https://x.com/rileybrown/status/2075302906291433604) | 21 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | When did @LeoDiCaprio become a VC https://t.co/0KULHJqcsz | [link](https://x.com/levelsio/status/2075273931200606654) | 21 | n/a | topic:ai-coding; score>=20 |
| missed | topic-direct-x | Will do a livestream there! | [link](https://x.com/steipete/status/2075328495677521934) | 21 | n/a | topic:ai-agent; score>=20 |
| missed | topic-direct-x | eSIM renewal is still broken on @Revolut @NStoronsky Whatever you set to renewal, it has.... | [link](https://x.com/levelsio/status/2075164130965586193) | 21 | n/a | topic:ai-coding; score>=20 |
| missed | topic-direct-x | Whoever came up with this at YouTube deserves a raise https://t.co/fsxkVnFBUC | [link](https://x.com/marclou/status/2075513866210160697) | 20 | n/a | topic:ai-coding; score>=20 |
| missed | topic-direct-x | ❤️❤️❤️❤️ https://t.co/44KRJXpzHW | [link](https://x.com/jackfriks/status/2075229738734420444) | 20 | n/a | topic:ai-coding; score>=20 |
| missed | top-direct-x | RT @cellinlab: 这个世界能草台班子到什么程度？🤯 Open AI 现在有两个客户端， 都叫 ChatGPT，一个 500MB 、一个 70MB... （不小心把 C... | [link](https://x.com/cellinlab/status/2075509714360623345) | 29 | n/a | score>=20 |
| missed | top-direct-x | RT @marclou: Whoever came up with this at YouTube deserves a raise https://t.co/fsxkVnFBUC | [link](https://x.com/marclou/status/2075651447644172345) | 22 | n/a | score>=20 |
| missed | top-direct-x | RT @N3sOnline: Day 1 of using @mattpocockuk's Wayfinder. I have a lot to say, but I think... | [link](https://x.com/mattpocockuk/status/2075262532269273354) | 21 | n/a | score>=20 |
