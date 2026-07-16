# 2026-05-29 Daily Source Intelligence

## 采集范围

- 运行日期：2026-05-29，时区：Asia/Shanghai。
- 稳定来源：RSS/Atom 32 个 source 全部 ok，命中原文 47/47 fulltext `ok`；GitHub release Atom 7 个 source 全部 ok，GitHub API 状态 `failed` 但 Atom fallback 正常；GitHub Trending daily 1 个 source ok，README 10/10 归档；official pages 4 个 source ok。
- 原始产物：[`../raw/2026-05-29/rss-items.json`](../raw/2026-05-29/rss-items.json)、[`../raw/2026-05-29/github-items.json`](../raw/2026-05-29/github-items.json)、[`../raw/2026-05-29/github-trending.json`](../raw/2026-05-29/github-trending.json)、[`../raw/2026-05-29/official-pages.json`](../raw/2026-05-29/official-pages.json)、[`../raw/2026-05-29/twitterapi-io-results.json`](../raw/2026-05-29/twitterapi-io-results.json)、[`../raw/2026-05-29/official-link-candidates.json`](../raw/2026-05-29/official-link-candidates.json)。
- 状态产物：[`../raw/2026-05-29/manifest.json`](../raw/2026-05-29/manifest.json)、[`../state/source-health.json`](../state/source-health.json)、[`../state/seen.json`](../state/seen.json)。
- 今日新增去重记录：65 条。

## 今日高信号

1. OpenAI/Endava 把 Codex 写成贯穿 requirements analysis、design、specification、development、operations 和 client communication 的 desktop agent：Endava 说 requirements analysis 从 weeks 压缩到 hours，并把 senior architects 的判断编码进 Codex 让 junior teams 并行使用。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-05-29/rss-fulltext/openai-blog/openai-blog-how-endava-builds-an-agentic-organization-with-codex-c4a9a57761.opencli.md`](../raw/2026-05-29/rss-fulltext/openai-blog/openai-blog-how-endava-builds-an-agentic-organization-with-codex-c4a9a57761.opencli.md)。
2. OpenAI/MUFG 是今天最强 financial-agents / regulated enterprise adoption 信号：MUFG Bank 约 35,000 名员工部署 ChatGPT Enterprise，配套 mandatory e-learning、AI champions、1,800+ custom GPTs，并探索 Moneytree / WealthNavi / digital bank 的 customer-facing AI finance experiences。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-05-29/rss-fulltext/openai-blog/openai-blog-mufg-aims-to-become-ai-native-with-openai-cb031b5cf3.opencli.md`](../raw/2026-05-29/rss-fulltext/openai-blog/openai-blog-mufg-aims-to-become-ai-native-with-openai-cb031b5cf3.opencli.md)。
3. OpenAI Frontier Governance Framework 把 Preparedness Framework 映射到 emerging legal requirements，包括 California Transparency in Frontier AI Act 和 EU AI Act GPAI Code of Practice，并覆盖 cyber offense、CBRN、harmful manipulation、loss of control、model reporting、security risk management、incident response、external expert input。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-05-29/rss-fulltext/openai-blog/openai-blog-openai-s-frontier-governance-framework-3e9dde27d0.opencli.md`](../raw/2026-05-29/rss-fulltext/openai-blog/openai-blog-openai-s-frontier-governance-framework-3e9dde27d0.opencli.md)。
4. Codex `0.135.0` 是可读 stable release：`codex doctor` 增加 environment/Git/terminal/app-server/thread inventory diagnostics，`/status` 显示 remote transport details，Vim mode 增加 text objects 和 interrupt-turn binding，`/permissions` 支持 named profiles，Python SDK 增加 Sandbox presets，并把 memory runtime state 移入 dedicated SQLite DB。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-05-29/github-release-fulltext/openai-codex/openai-codex-0.135.0-42234c469d.atom.md`](../raw/2026-05-29/github-release-fulltext/openai-codex/openai-codex-0.135.0-42234c469d.atom.md)。
5. Claude Code `v2.1.154` 是今天最强 Claude Code feature signal：Opus 4.8、dynamic workflows、tens-to-hundreds background agents、`/workflows`、`claude --bg --exec`、plugin `defaultEnabled: false`、directory-aware plugin suggestions、always-on streaming tool execution、MCP env markers、unapproved `.mcp.json` pending approval，以及 background/worktree/sandbox fixes 同时出现。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-05-29/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.154-33b228088c.atom.md`](../raw/2026-05-29/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.154-33b228088c.atom.md)。
6. a16z FDE Fellowship 把 FDE 角色明确包装为 AI-native enterprise deployment 的 peer network：Decagon、ElevenLabs、Cursor、Databricks、Harvey、Google、Snowflake、Ramp、Rippling 等角色被列为 founding fellows / industry leaders。证据等级 `secondary-source`，fulltext `ok`，归档见 [`../raw/2026-05-29/rss-fulltext/a16z-news/a16z-news-introducing-the-a16z-fde-fellowship-576b225917.extracted.md`](../raw/2026-05-29/rss-fulltext/a16z-news/a16z-news-introducing-the-a16z-fde-fellowship-576b225917.extracted.md)。
7. a16z/Pylon 的 B2B support 数据给 enterprise delivery 一个反向校准：AI 不是只看 deflection rate 的 replacement，而是多数时候做 silent triage、context handoff 和 human workload reduction；B2B support end-to-end resolution 约 15%，B2C 约 35%。证据等级 `secondary-source`，fulltext `ok`，归档见 [`../raw/2026-05-29/rss-fulltext/a16z-news/a16z-news-narrative-violation-in-b2b-customer-support-ai-is-a-copilot-not-a-repl-dc106c0251.extracted.md`](../raw/2026-05-29/rss-fulltext/a16z-news/a16z-news-narrative-violation-in-b2b-customer-support-ai-is-a-copilot-not-a-repl-dc106c0251.extracted.md)。
8. GitHub Trending 继续出现 agent methodology / skill substrate：`obra/superpowers`、`revfactory/harness`、`affaan-m/ECC`、`Leonxlnx/taste-skill`、`hardikpandya/stop-slop` 都把 skills、agent teams、rules、methodology 或 writing/design rubric 包成可安装材料。证据等级 `secondary-source`，README 归档见 [`../raw/2026-05-29/github-trending.json`](../raw/2026-05-29/github-trending.json)。

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog：5 条 always-read RSS 全部 fulltext `ok`。今天新增强信号是 Endava agentic organization、MUFG AI-native finance adoption、Frontier Governance Framework；Cisco 和 Tax AI 是昨日强信号的重复窗口，不再当作今日新增主线。
- OpenAI Codex releases：`0.135.0` fulltext `ok`；`0.136.0-alpha.1`、`python-v0.1.0b1/b2`、`0.135.0-alpha.2` 均 limited，只作为 version-line signal。
- Claude Code releases：`v2.1.154`、`v2.1.153`、`v2.1.152` fulltext `ok`；`v2.1.156` limited，仅能说明 Opus 4.8 thinking-block API error fix，不能展开成完整功能判断。

## 按主题分组摘要

### AI coding / agent runtime

- Codex `0.135.0` 延续 runtime control plane：diagnostics、remote status、permission profiles、Vim editing、SDK Sandbox presets、resume/cwd fixes、memory SQLite state、MCP/tool naming cleanup，都在支持更可恢复、更可诊断的 agent runtime。
- Claude Code `v2.1.154` 把竞争面推到 dynamic workflows 和 background agent orchestration，同时继续补 plugin/MCP/sandbox/background session 的治理和可靠性。
- Endava 是 Codex 使用面的强证据：Codex 不只写代码，还参与 requirements/spec/design/client communication/operations，并作为 senior judgment distribution mechanism。

### Memory / context / eval substrate

- Claude Code dynamic workflows、Codex dedicated memory SQLite state、Superpowers/Harness/ECC 共同说明“长期 agent 能力”正在由 workflow decomposition、skills/rules、agent team architecture、background orchestration、diagnostics 和 state persistence 组成。
- 这些 README discovery 只证明项目主张和可见性；实际有效性仍要看安装面、权限面、是否生成可审计 artifacts，以及能否在真实 repo 中稳定复用。

### Enterprise / FDE / delivery system

- Endava 和 a16z B2B support 把 enterprise delivery 的核心从“AI 自动替代人”拉回到组织流程：需求澄清、专家判断传播、silent triage、context handoff、human specialist escalation 和 measurable workload reduction。
- a16z FDE Fellowship 是 FDE 社群/人才市场层面的二级信号：FDE 正被包装成 AI-native enterprise deployment 的关键角色，但它不是岗位需求规模或客户结果的量化证据。

### AI governance / public legitimacy

- Frontier Governance Framework 是 governance legitimacy 的新一手材料：OpenAI 把 safety/security practice 和法律框架对齐，并把 Preparedness Framework 中的高级风险管理机制转成 public governance document。
- 这条不同于 election safeguards：它更偏 regulatory compliance / frontier model risk governance，而不是 election information/provenance enforcement。

### Financial agents

- MUFG 是 regulated finance adoption 的强一手信号，但目前主要是 employee productivity、custom GPTs、training/governance 和 customer-facing discovery/advisory exploration；不是 autonomous trading、payment、ledger posting 或 regulated advice execution。
- Moneytree、WealthNavi、digital bank / AI concierge / MAP 都是需要继续观察的 action surface：账户数据、personalized recommendations 和 customer journey 越靠近金融建议，证据门槛越高。

### GitHub Trending discovery

GitHub Trending 今日解析到 10 个 repo，README 归档 10/10 成功，来源边界是 `secondary-source` discovery signal。

- `harry0703/MoneyPrinterTurbo`：AI 短视频生成工具，从主题/关键词生成文案、素材、字幕、背景音乐并合成视频；风险是版权、素材来源、平台滥用和质量未验证。
- `affaan-m/ECC`：跨 Claude Code、Codex、OpenCode、Cursor 的 agent harness / rules / memory / security / research-first workflow 包装；需要 install audit。
- `Leonxlnx/taste-skill`：面向 AI frontend 的 portable design skills 和 image-generation reference board workflow；不能证明 UI 输出质量。
- `hardikpandya/stop-slop`：移除 AI prose tells 的 skill file；是 writing-quality rubric packaging，不是可靠评测。
- `twentyhq/twenty`：AI-oriented open-source CRM，强调 objects、views、workflows、agents；可作为 business app substrate discovery，不能证明 enterprise deployment。
- `DigitalPlatDev/FreeDomain`、`byoungd/English-level-up-tips`：与本 watch 弱相关或噪声。
- `microsoft/markitdown`：Microsoft document-to-Markdown converter，强调 untrusted input security considerations；对 agent document ingestion 有 substrate 价值。
- `obra/superpowers`：agentic skills framework + software development methodology，明确面向 Codex App/CLI、Claude Code、Gemini CLI 等；是 methodology packaging signal。
- `revfactory/harness`：为 Claude Code 生成 domain-specific agent teams 和 skills 的 meta-skill；是 multi-agent decomposition discovery。

## 来源证据表

| 信号 | 证据等级 | 本地归档 | 边界 |
| --- | --- | --- | --- |
| Endava agentic organization with Codex | official-source | [`../raw/2026-05-29/rss-fulltext/openai-blog/openai-blog-how-endava-builds-an-agentic-organization-with-codex-c4a9a57761.opencli.md`](../raw/2026-05-29/rss-fulltext/openai-blog/openai-blog-how-endava-builds-an-agentic-organization-with-codex-c4a9a57761.opencli.md) | 官方客户案例，未独立验证 Endava 内部交付指标。 |
| MUFG AI-native finance adoption | official-source | [`../raw/2026-05-29/rss-fulltext/openai-blog/openai-blog-mufg-aims-to-become-ai-native-with-openai-cb031b5cf3.opencli.md`](../raw/2026-05-29/rss-fulltext/openai-blog/openai-blog-mufg-aims-to-become-ai-native-with-openai-cb031b5cf3.opencli.md) | 官方客户案例，金融建议/交易执行边界未验证。 |
| OpenAI Frontier Governance Framework | official-source | [`../raw/2026-05-29/rss-fulltext/openai-blog/openai-blog-openai-s-frontier-governance-framework-3e9dde27d0.opencli.md`](../raw/2026-05-29/rss-fulltext/openai-blog/openai-blog-openai-s-frontier-governance-framework-3e9dde27d0.opencli.md) | Blog 摘要可读；PDF 原文未单独全文解析。 |
| Codex `0.135.0` | official-source | [`../raw/2026-05-29/github-release-fulltext/openai-codex/openai-codex-0.135.0-42234c469d.atom.md`](../raw/2026-05-29/github-release-fulltext/openai-codex/openai-codex-0.135.0-42234c469d.atom.md) | Release body 可读，未本地实测每个功能。 |
| Claude Code `v2.1.154` | official-source | [`../raw/2026-05-29/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.154-33b228088c.atom.md`](../raw/2026-05-29/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.154-33b228088c.atom.md) | Release body 可读，未本地实测 dynamic workflows。 |
| a16z FDE Fellowship / B2B support copilot | secondary-source | [`../raw/2026-05-29/rss-fulltext/a16z-news/a16z-news-introducing-the-a16z-fde-fellowship-576b225917.extracted.md`](../raw/2026-05-29/rss-fulltext/a16z-news/a16z-news-introducing-the-a16z-fde-fellowship-576b225917.extracted.md), [`../raw/2026-05-29/rss-fulltext/a16z-news/a16z-news-narrative-violation-in-b2b-customer-support-ai-is-a-copilot-not-a-repl-dc106c0251.extracted.md`](../raw/2026-05-29/rss-fulltext/a16z-news/a16z-news-narrative-violation-in-b2b-customer-support-ai-is-a-copilot-not-a-repl-dc106c0251.extracted.md) | VC/media source；Pylon 数据和 role market claims 未独立验证。 |
| GitHub Trending README set | secondary-source | [`../raw/2026-05-29/github-trending.json`](../raw/2026-05-29/github-trending.json) | Discovery signal，不代表采用、质量、安全或长期趋势已确认。 |
| X/Twitter direct evidence | direct-x | [`../raw/2026-05-29/twitterapi-io-results.json`](../raw/2026-05-29/twitterapi-io-results.json) | API read evidence；未补 thread/context；不使用 Exa fallback。 |

## X/Twitter 覆盖说明

`twitterapi.io` status 为 `ok`，27 个账号均成功请求；共保留 117 条窗口内 tweet。高相关 direct-x 包括 OpenAI 的 `R&D Part 1: Here to Win` 视频、Anthropic/Claude 的 Opus 4.8 与 model pre-ship stress-testing叙述、Greg Isenberg 对 Claude Code dynamic workflows 的使用反馈、Riley Brown 对 Codex browser signed-in state / app surface 的观察、Steipete 对 OpenClaw dependency/runtime cleanup 与 GitHub token pooling 的项目线索。所有直接来自 API 的 tweet 在日报解释中按 `direct-x` 处理；官方链接候选 0 条，见 [`../raw/2026-05-29/official-link-candidates.json`](../raw/2026-05-29/official-link-candidates.json)。

## Candidate audit 处理记录

[`../reviews/2026-05-29-candidate-audit.md`](../reviews/2026-05-29-candidate-audit.md) 已生成；今日无 official-link-candidate。强相关 RSS / release / Trending 项已进入“今日高信号”、主题摘要或 trend report；以下候选已审计但因重复窗口、弱相关、旧文章、secondary-source 边界或缺少新增本地官方全文，不升级为今日高信号。

### matched-rss

- `Cisco and OpenAI redefine enterprise engineering with Codex`、`Building self-improving tax agents with Codex`、`ITBench-AA: Frontier Models Score Below 50% on the First Benchmark for Agentic Enterprise IT Tasks — by Artificial Analysis and IBM`：昨日已作为强主线处理，今天只保留重复窗口边界。
- `Introducing Gemini Omni`：模型/产品相关但已是 2026-05-17 发布，今天没有比 OpenAI/Claude release 更强的新信息量。
- `Anthropic's run-rate revenue hits $47 billion`、`Claude Opus 4.8: "a modest but tangible improvement"`、`llm-anthropic 0.25.1`、`markdown-svg-renderer`：Simon Willison 条目可读，但分别是增长新闻评论、模型观察、插件小版本和工具小记；今天只作为 Claude/LLM 背景，不升级为高信号。
- `Extrinsic Hallucinations in LLMs`、`Thinking about High-Quality Human Data`：Lilian Weng 旧文被关键词命中；可作为长期背景，不是今日新增。
- `Distributing LLM inference in DwarfStar`、`Alternatives for the EDIT tool of LLM agents`、`A few words on DS4`、`Redis array type: short story of a long development`、`AI cybersecurity is not proof of work`：antirez 文章可读，但多数是多日/旧窗口延续；今天不压过 first-party release/customer case。
- `Clanker: A Word For The Machine`、`Building Pi With Pi`、`Pushing Local Models With Focus And Polish`、`Content for Content’s Sake`、`Before GitHub`：Armin Ronacher 文章偏背景或旧窗口，未形成新的 trend update。
- `The mysterious Hy3 LLM is topping OpenRouter Model Rankings by a large margin`、`An AI agent coding skeptic tries AI agent coding, in excessive detail`、`Claude Haiku 4.5 does not appreciate my attempts to jailbreak it`、`What will better AI mean?`：模型/agent 观察可读，但没有新增官方产品、benchmark 复核或 enterprise workflow 证据。
- `AI and Teaching – The Brave New World`、`How to Build a Webhook System in Rails Using Sidekiq`、`How to License and Distribute a Private Node Module`：弱相关或旧文，不进入日报主线。
- `Two Archetypes: A Conversation with Kanav Bhatnagar`、`Forward Deployed, Episode 6: Market Mechanisms for Agents`、`Forward Deployed, Episode 5: Aligning Agents`、`Forward Deployed, Episode 4: The Special Forces Model`、`Sorry, that isn't an FDE`：FDE 背景/延续材料；今日 FDE 新信号优先记录 a16z FDE Fellowship。
- `Building OpenCode with Dax Raad`、`The Pulse: Antigravity 2.0 takes ‘IDE’ out of its new IDE`：开发者工具媒体材料，保留为背景，不写成官方产品事实。
- `Build To Learn FAQ`、`Build to Learn vs Build to Earn`、`Commercial vs Internal Products`、`Product Coaching and AI`、`The Product Model at Google`：产品管理背景材料，非今日 AI agent 高信号。
- `We Tested Marketing Incentives to AI Agents. Here's What Happened.`、`Automating Receipt Collection: Apple Intelligence for On-Device Inference`、`Re-imagining ML Serving Infra: My Winter Internship at Ramp`：Ramp 材料可读，但今天没有新 finance/action-surface 或 serving 架构增量。

### top-direct-x

- `Claude Code just dropped "dynamic workflows" and it's pretty cool. You type "create a wor...`：已通过 Claude Code `v2.1.154` official release body 处理；direct-x 只作使用反馈。
- `I hope you know tomorrow is going to be a VERY big day in the world of AI agents...`：弱预告，不当作事实。
- `RT @claudeai: Before we ship a new model, these teams try to break it. They build with it...`、`RT @claudeai: Introducing Claude Opus 4.8: it builds on Opus 4.7 with sharper judgment, m...`、`We've raised $65 billion in Series H funding at a $965 billion post-money valuation, led....`：Anthropic/Claude direct-x 可作背景，但今天没有对应本地官方全文；不升级为主线。
- `she's right, the industry seems to be in a state of mass psychosis. everyone is spending....`、`Cursor shipped a /thermo-nuclear-code-review for the TOUGHEST AI code review possible. Bu...`、`Every CEO layoff letter in 2026 follows the same template. "Hardest decision I've ever ma...`、`RT @ay_ushr: what the shit is my agent doing https://t.co/kMBFFni5QQ`、`RT @eliebakouch: this is so funny, training opus 4.7 on business skills makes it misalign...`：社交观点或使用感受，保留 direct-x 边界，不写成行业事实。

## 不确定性与待验证项

- GitHub API 状态为 `failed`，但 releases Atom fallback 成功；今天 release 结论只基于 Atom content。
- OpenAI Frontier Governance Framework 的 blog 摘要已归档，PDF 框架全文未单独解析；不能声称已逐条审计 regulatory mapping。
- MUFG 金融 customer-facing AI 仍是官方案例里的 planned/exploratory surface；本次未验证 Moneytree、WealthNavi、emutt/MAP 的数据权限、advice disclaimers、transaction boundary 或 audit logs。
- Claude Code `v2.1.154` dynamic workflows 和 Codex `0.135.0` 新功能都未本地实测；报告只写 release body 事实。
- GitHub Trending README 只证明上榜和 README 可读；`Superpowers`、`Harness`、`ECC`、`taste-skill` 需要 install audit、权限审计和真实 repo 试跑。

## 今日文档翻译

翻译阶段已完成，父 runner 使用 4 个 shard 运行 `codex exec --json --model gpt-5.4-mini`，最终 check 通过。

- 译读索引：[`../translations/2026-05-29/index.md`](../translations/2026-05-29/index.md)
- 翻译 manifest：[`../translations/2026-05-29/manifest.json`](../translations/2026-05-29/manifest.json)
- `target_count`: 20
- `translated_count`: 20
- `missing_count`: 0

### daily-high-signal

- [`../translations/2026-05-29/daily-high-signal/openai-blog-how-endava-builds-an-agentic-organization-with-codex-c4a9a57761.opencli.zh.md`](../translations/2026-05-29/daily-high-signal/openai-blog-how-endava-builds-an-agentic-organization-with-codex-c4a9a57761.opencli.zh.md)
- [`../translations/2026-05-29/daily-high-signal/openai-blog-mufg-aims-to-become-ai-native-with-openai-cb031b5cf3.opencli.zh.md`](../translations/2026-05-29/daily-high-signal/openai-blog-mufg-aims-to-become-ai-native-with-openai-cb031b5cf3.opencli.zh.md)
- [`../translations/2026-05-29/daily-high-signal/openai-blog-openai-s-frontier-governance-framework-3e9dde27d0.opencli.zh.md`](../translations/2026-05-29/daily-high-signal/openai-blog-openai-s-frontier-governance-framework-3e9dde27d0.opencli.zh.md)
- [`../translations/2026-05-29/daily-high-signal/openai-codex-0.135.0-42234c469d.atom.zh.md`](../translations/2026-05-29/daily-high-signal/openai-codex-0.135.0-42234c469d.atom.zh.md)
- [`../translations/2026-05-29/daily-high-signal/anthropics-claude-code-v2.1.154-33b228088c.atom.zh.md`](../translations/2026-05-29/daily-high-signal/anthropics-claude-code-v2.1.154-33b228088c.atom.zh.md)
- [`../translations/2026-05-29/daily-high-signal/a16z-news-introducing-the-a16z-fde-fellowship-576b225917.extracted.zh.md`](../translations/2026-05-29/daily-high-signal/a16z-news-introducing-the-a16z-fde-fellowship-576b225917.extracted.zh.md)
- [`../translations/2026-05-29/daily-high-signal/a16z-news-narrative-violation-in-b2b-customer-support-ai-is-a-copilot-not-a-repl-dc106c0251.extracted.zh.md`](../translations/2026-05-29/daily-high-signal/a16z-news-narrative-violation-in-b2b-customer-support-ai-is-a-copilot-not-a-repl-dc106c0251.extracted.zh.md)

### trend

- [`../translations/2026-05-29/ai-governance-legitimacy/openai-blog-openai-s-frontier-governance-framework-3e9dde27d0.opencli.zh.md`](../translations/2026-05-29/ai-governance-legitimacy/openai-blog-openai-s-frontier-governance-framework-3e9dde27d0.opencli.zh.md)
- [`../translations/2026-05-29/claude-code-feature-watch/anthropics-claude-code-v2.1.154-33b228088c.atom.zh.md`](../translations/2026-05-29/claude-code-feature-watch/anthropics-claude-code-v2.1.154-33b228088c.atom.zh.md)
- [`../translations/2026-05-29/codex-feature-watch/openai-blog-how-endava-builds-an-agentic-organization-with-codex-c4a9a57761.opencli.zh.md`](../translations/2026-05-29/codex-feature-watch/openai-blog-how-endava-builds-an-agentic-organization-with-codex-c4a9a57761.opencli.zh.md)
- [`../translations/2026-05-29/codex-feature-watch/openai-codex-0.135.0-42234c469d.atom.zh.md`](../translations/2026-05-29/codex-feature-watch/openai-codex-0.135.0-42234c469d.atom.zh.md)
- [`../translations/2026-05-29/enterprise-delivery-system/a16z-news-narrative-violation-in-b2b-customer-support-ai-is-a-copilot-not-a-repl-dc106c0251.extracted.zh.md`](../translations/2026-05-29/enterprise-delivery-system/a16z-news-narrative-violation-in-b2b-customer-support-ai-is-a-copilot-not-a-repl-dc106c0251.extracted.zh.md)
- [`../translations/2026-05-29/enterprise-delivery-system/microsoft__markitdown.zh.md`](../translations/2026-05-29/enterprise-delivery-system/microsoft__markitdown.zh.md)
- [`../translations/2026-05-29/enterprise-delivery-system/openai-blog-how-endava-builds-an-agentic-organization-with-codex-c4a9a57761.opencli.zh.md`](../translations/2026-05-29/enterprise-delivery-system/openai-blog-how-endava-builds-an-agentic-organization-with-codex-c4a9a57761.opencli.zh.md)
- [`../translations/2026-05-29/financial-agents/openai-blog-mufg-aims-to-become-ai-native-with-openai-cb031b5cf3.opencli.zh.md`](../translations/2026-05-29/financial-agents/openai-blog-mufg-aims-to-become-ai-native-with-openai-cb031b5cf3.opencli.zh.md)
- [`../translations/2026-05-29/forward-deployed-engineering/a16z-news-introducing-the-a16z-fde-fellowship-576b225917.extracted.zh.md`](../translations/2026-05-29/forward-deployed-engineering/a16z-news-introducing-the-a16z-fde-fellowship-576b225917.extracted.zh.md)
- [`../translations/2026-05-29/memory-dream/anthropics-claude-code-v2.1.154-33b228088c.atom.zh.md`](../translations/2026-05-29/memory-dream/anthropics-claude-code-v2.1.154-33b228088c.atom.zh.md)
- [`../translations/2026-05-29/memory-dream/obra__superpowers.zh.md`](../translations/2026-05-29/memory-dream/obra__superpowers.zh.md)
- [`../translations/2026-05-29/memory-dream/openai-codex-0.135.0-42234c469d.atom.zh.md`](../translations/2026-05-29/memory-dream/openai-codex-0.135.0-42234c469d.atom.zh.md)
- [`../translations/2026-05-29/memory-dream/revfactory__harness.zh.md`](../translations/2026-05-29/memory-dream/revfactory__harness.zh.md)
