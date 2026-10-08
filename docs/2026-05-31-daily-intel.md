# 2026-05-31 Daily Source Intelligence

## 采集范围

- 运行日期：2026-05-31，时区：Asia/Shanghai。
- 稳定来源：RSS/Atom 32 个 source 全部 ok；命中原文 46/46 fulltext `ok`。GitHub releases 7 个 source 全部通过 Atom fallback ok，GitHub REST API `skipped`；GitHub release always-read 10 条，其中 4 条 fulltext `ok`、6 条 `limited`。GitHub Trending daily 1 个 source ok，README 10/10 归档；official pages 4 个 source ok。
- X/Twitter：`twitterapi.io` status 为 `ok`，27 个账号请求成功，保留 116 条 direct-x tweet；官方链接候选 1 条且 fulltext `ok`。
- 原始产物：[`../raw/2026-05-31/rss-items.json`](../raw/2026-05-31/rss-items.json)、[`../raw/2026-05-31/github-items.json`](../raw/2026-05-31/github-items.json)、[`../raw/2026-05-31/github-trending.json`](../raw/2026-05-31/github-trending.json)、[`../raw/2026-05-31/official-pages.json`](../raw/2026-05-31/official-pages.json)、[`../raw/2026-05-31/twitterapi-io-results.json`](../raw/2026-05-31/twitterapi-io-results.json)、[`../raw/2026-05-31/official-link-candidates.json`](../raw/2026-05-31/official-link-candidates.json)。
- 状态产物：[`../raw/2026-05-31/manifest.json`](../raw/2026-05-31/manifest.json)、[`../state/source-health.json`](../state/source-health.json)、[`../state/seen.json`](../state/seen.json)。
- 今日新增去重记录：17 条。

## 今日高信号

1. OpenAI 的 third-party evaluations playbook 是今天最强 eval / governance official-source：它把 frontier model 评测从 prompt-response 扩展到 agentic task workflow，并建议第三方评测报告写清 claim、harness、tool setup、budget、elicitation、validity checks、reward hacking、refusals、contamination、broken problems 和 sandbagging；边界是这是 OpenAI 对评测报告的设计建议，不是独立标准机构结论。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-05-31/rss-fulltext/openai-blog/openai-blog-a-shared-playbook-for-trustworthy-third-party-evaluations-33e1df4abe.opencli.md`](../raw/2026-05-31/rss-fulltext/openai-blog/openai-blog-a-shared-playbook-for-trustworthy-third-party-evaluations-33e1df4abe.opencli.md)。
2. Braintrust/Codex 是今天最强 enterprise delivery / Codex customer-loop signal：OpenAI 官方 case 写到 Braintrust engineers 用 Codex + GPT-5.5 把 customer feature requests 变成 preview branches，半数团队一个月内转向 Codex，并把 workflow 从 backlog priority 改成 customer real-time iteration。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-05-31/rss-fulltext/openai-blog/openai-blog-how-braintrust-turns-customer-requests-into-code-with-codex-507ec0fdf6.opencli.md`](../raw/2026-05-31/rss-fulltext/openai-blog/openai-blog-how-braintrust-turns-customer-requests-into-code-with-codex-507ec0fdf6.opencli.md)。
3. Boston Children’s Hospital 是 enterprise AI layer / governed workflow adoption 信号：OpenAI 官方 case 写到 secure internal ChatGPT environment、governance、monitoring、evaluation、50+ automations、60,000 hours saved、40+ unresolved rare conditions diagnosed。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-05-31/rss-fulltext/openai-blog/openai-blog-boston-children-s-uses-ai-to-unlock-new-diagnoses-e63fa88b56.opencli.md`](../raw/2026-05-31/rss-fulltext/openai-blog/openai-blog-boston-children-s-uses-ai-to-unlock-new-diagnoses-e63fa88b56.opencli.md)。
4. Codex `0.135.0` 是本轮复核到的可读 stable release：release 更新于 2026-05-29，本日不是新发版本；可确认的功能面包括 `codex doctor` 增加 environment/Git/terminal/app-server/thread inventory diagnostics，`/status` 显示 remote transport details，Vim mode 增加 text-object editing，`/permissions` 支持 named permission profiles，Python SDK 增加 Sandbox presets，并把 memory runtime state 移到 dedicated SQLite DB。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-05-31/github-release-fulltext/openai-codex/openai-codex-0.135.0-42234c469d.atom.md`](../raw/2026-05-31/github-release-fulltext/openai-codex/openai-codex-0.135.0-42234c469d.atom.md)。
5. Claude Code `v2.1.158` 是轻量 first-party release signal：Auto mode 可在 Bedrock、Vertex、Foundry 上用于 Opus 4.7 / Opus 4.8，通过 `CLAUDE_CODE_ENABLE_AUTO_MODE=1` opt in；release body 很短，只能记录 provider coverage，不展开成功能大版本判断。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-05-31/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.158-4a43af6509.atom.md`](../raw/2026-05-31/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.158-4a43af6509.atom.md)。
6. Forward Deployed Episode 6 是今天最强 Memory & Dream / FDE 交叉访谈线索：Rohit Krishnan 讨论 enterprise world models、data-first ontologies、MarketBench、agent self-knowledge、onboarding/memory、spec 与 deliverable co-evolution。证据等级 `secondary-source` RSS fulltext `ok`，归档见 [`../raw/2026-05-31/rss-fulltext/forward-deployed/forward-deployed-forward-deployed-episode-6-market-mechanisms-for-agents-88f1c49929.opencli.md`](../raw/2026-05-31/rss-fulltext/forward-deployed/forward-deployed-forward-deployed-episode-6-market-mechanisms-for-agents-88f1c49929.opencli.md)。

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS：5 条 always-read 全部 fulltext `ok`。今日主线是 trustworthy third-party evaluations、Braintrust/Codex、Boston Children’s；Rosalind Biodefense 和 Endava/Codex 是前两日已处理过的重复窗口，仍有本地 fulltext。
- OpenAI Codex releases：`0.135.0` fulltext `ok`，可写功能判断；`0.136.0-alpha.1`、`python-v0.1.0b1/b2`、`0.135.0-alpha.2` limited，只记录 version-line。
- Claude Code releases：`v2.1.158` fulltext `ok`，但正文很短；`v2.1.157`、`v2.1.154`、`v2.1.153` fulltext `ok` 是重复窗口；`v2.1.156` limited。

## 按主题分组摘要

### AI coding / agent runtime

- Codex `0.135.0` 把 support diagnostics、remote status visibility、permission profiles、Vim editing、SDK sandbox presets、resume/cwd behavior 和 memory-state storage 收进 runtime/operability 层。
- Braintrust/Codex case 把 Codex 从个人 coding helper 写成 customer-request-to-preview workflow：价值点不是“生成代码”本身，而是让 customer feedback loop 直接进入 preview branch。
- Claude Code `v2.1.158` 只是 Auto mode provider coverage 扩展；功能面弱于昨天 `v2.1.157` 的 plugin/worktree/telemetry 更新。

### Memory / context / eval substrate

- OpenAI evaluations playbook 明确说 agentic systems 的 measured capability 依赖 harness、tools、state preservation、retry、budget、compaction 和 scoring validity；这会直接影响未来 agent benchmark 该如何读。
- Codex `0.135.0` 的 richer `doctor`、thread inventory、resume non-interactive exec sessions、memory state dedicated SQLite DB 和 Responses retry centralization，是长任务可恢复/可诊断的 substrate 信号。
- Forward Deployed Episode 6 把 enterprise world models、agent self-knowledge、daily retraining、data-first ontology 和 spec/workflow co-evolution 连到 agent memory/onboarding 问题，但它仍是访谈和 secondary-source，不是已验证产品发布。

### Enterprise / delivery system

- Braintrust/Codex 是最贴近 enterprise delivery 的新证据：customer feature request 被转成 preview branch 并即时给客户看，说明 agent value 正在向 feedback loop、experiment scope 和 release preview 迁移。
- Boston Children’s 的 enterprise AI layer 是 governed deployment pattern：secure internal ChatGPT environment、governance、monitoring、evaluation、role-specific workflows 和可量化 operational outcomes。
- OpenAI evaluations playbook 也有 enterprise delivery 含义：如果 agent/harness/budget 不透明，企业无法判断 benchmark 或供应商 claim 是否对应真实 workflow。

### AI governance / public legitimacy

- Third-party evaluations playbook 是 governance legitimacy 的评测标准化叙事信号：OpenAI 不只发布模型能力，也在提出外部评测报告应如何陈述 claim、validity evidence 和 failure modes；它本身仍是 OpenAI official framing。
- Boston Children’s 与 Rosalind Biodefense 都是 OpenAI 官方 public-good / high-stakes use case framing；今天不独立验证临床结果、部署安全或 partner outcome。

### Financial agents

- 今天没有新的 finance-specific high-signal。Boston Children’s 涉及 billing / invoice / operational workflow，但不是 financial services agent；不升级到 `financial-agents`。

### Forward Deployed Engineering

- Forward Deployed Episode 6 提供一个偏理论的新 FDE 线索：enterprise world models 可以从 email、Slack、docs、GitHub、Jira、Confluence 等工作流数据中学习组织状态，用来回答 renewal、contract、action outcome 等反事实问题。
- 边界：这是 podcast/transcript secondary-source；它支持 FDE 的企业现场知识建模问题意识，不证明某个 FDE deployment 已落地。

### GitHub Trending discovery

GitHub Trending 今日解析到 10 个 repo，README 归档 10/10 成功，来源边界是 `secondary-source` discovery signal。

- `microsoft/markitdown`：Microsoft 文档转 Markdown 工具，适合 agent document ingestion；今天是重复上榜/延续信号，不等于新企业部署。
- `harry0703/MoneyPrinterTurbo`：AI 短视频生成工具，从主题/关键词生成文案、素材、字幕、配乐并合成视频；风险是版权、素材来源、平台滥用和内容质量。
- `anthropics/claude-code`：Claude Code README 上榜；这是产品可见性信号，功能判断仍以 release body 为准。
- `cursor/plugins`：Cursor 官方 plugin marketplace repo，展示 continual learning、team kit、thermos、agent compatibility、CLI-for-agent、orchestration 等 plugin 类型；需要安装/权限审计。
- `revfactory/harness`：把 domain-specific agent teams 和 skills 生成成可复用 harness 的 meta-skill；仍是 README discovery。
- `EveryInc/compound-engineering-plugin`：把 strategy、brainstorm、plan、work、debug、review、compound、product pulse 包成跨 harness engineering methodology plugin；对 Memory & Dream / Enterprise Delivery System 有 substrate 价值。
- `affaan-m/ECC`：跨 Codex、Claude Code、Cursor、OpenCode、Gemini 等 harness 的 skills、memory、security、AgentShield 和 workflow package；README claims 较大，需要 install audit。
- `OpenBMB/VoxCPM`：多语言 speech generation / voice cloning TTS；与 watch 弱相关，涉及 voice cloning 风险。
- `galilai-group/stable-worldmodel`：reproducible world model research/evaluation platform；可作为 eval/research substrate 候选。
- `Crosstalk-Solutions/project-nomad`：离线 survival computer，含 AI/knowledge tools；与本 watch 弱相关。

## 来源证据表

| 信号 | 证据等级 | 本地归档 | 边界 |
| --- | --- | --- | --- |
| OpenAI third-party evaluations playbook | official-source | [`../raw/2026-05-31/rss-fulltext/openai-blog/openai-blog-a-shared-playbook-for-trustworthy-third-party-evaluations-33e1df4abe.opencli.md`](../raw/2026-05-31/rss-fulltext/openai-blog/openai-blog-a-shared-playbook-for-trustworthy-third-party-evaluations-33e1df4abe.opencli.md) | OpenAI 官方评测标准建议；不是独立标准机构结论。 |
| Braintrust/Codex customer loop | official-source | [`../raw/2026-05-31/rss-fulltext/openai-blog/openai-blog-how-braintrust-turns-customer-requests-into-code-with-codex-507ec0fdf6.opencli.md`](../raw/2026-05-31/rss-fulltext/openai-blog/openai-blog-how-braintrust-turns-customer-requests-into-code-with-codex-507ec0fdf6.opencli.md) | OpenAI customer story；未独立验证 adoption/outcome。 |
| Boston Children’s enterprise AI layer | official-source | [`../raw/2026-05-31/rss-fulltext/openai-blog/openai-blog-boston-children-s-uses-ai-to-unlock-new-diagnoses-e63fa88b56.opencli.md`](../raw/2026-05-31/rss-fulltext/openai-blog/openai-blog-boston-children-s-uses-ai-to-unlock-new-diagnoses-e63fa88b56.opencli.md) | OpenAI customer story；不替代医学/临床独立验证。 |
| Codex `0.135.0` | official-source | [`../raw/2026-05-31/github-release-fulltext/openai-codex/openai-codex-0.135.0-42234c469d.atom.md`](../raw/2026-05-31/github-release-fulltext/openai-codex/openai-codex-0.135.0-42234c469d.atom.md) | Release body 可读；未本地实测各功能。 |
| Claude Code `v2.1.158` | official-source | [`../raw/2026-05-31/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.158-4a43af6509.atom.md`](../raw/2026-05-31/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.158-4a43af6509.atom.md) | Release body 很短，只能记录 Auto mode provider coverage。 |
| Forward Deployed Episode 6 | secondary-source | [`../raw/2026-05-31/rss-fulltext/forward-deployed/forward-deployed-forward-deployed-episode-6-market-mechanisms-for-agents-88f1c49929.opencli.md`](../raw/2026-05-31/rss-fulltext/forward-deployed/forward-deployed-forward-deployed-episode-6-market-mechanisms-for-agents-88f1c49929.opencli.md) | Podcast/transcript，不是产品发布或部署证明。 |
| X/Twitter direct evidence | direct-x | [`../raw/2026-05-31/twitterapi-io-results.json`](../raw/2026-05-31/twitterapi-io-results.json) | API read evidence；未补 thread/context；不使用 Exa fallback。 |

## X/Twitter 覆盖说明

`twitterapi.io` status 为 `ok`，27 个账号均成功请求；共保留 116 条窗口内 tweet。高相关 direct-x 包括 Matt Pocock 的 ADR-for-agents 和 token smart-zone 观察、Steipete 对 GPT 5.5 / `/goal` / autoreview / crabbox 长任务的使用反馈、Riley Brown 对 Codex thread spawning、computer use speed、agent mini-apps 的观察、以及若干 OpenClaw / Opus 4.8 使用反馈。所有直接来自 API 的 tweet 按 `direct-x` 处理。官方链接候选 1 条为 OpenAI Rosalind Biodefense 的重复窗口 fulltext，见 [`../raw/2026-05-31/official-link-candidates.json`](../raw/2026-05-31/official-link-candidates.json)。

## Candidate audit 处理记录

[`../reviews/2026-05-31-candidate-audit.md`](../reviews/2026-05-31-candidate-audit.md) 已生成：`covered=4`、`missed=53`。已覆盖项为 Boston Children’s、Braintrust/Codex、third-party evaluations playbook、Forward Deployed Episode 6。其余 missed 已审计，处理如下：

### official-link-candidate / repeated first-party

- OpenAI Rosalind Biodefense official-link-candidate 与 RSS 条目是 2026-05-30 已写入主线和 trend 的重复窗口；今天只在 X/Twitter 覆盖说明中保留，不重复升级。
- OpenAI Endava/Codex 是 2026-05-29 已处理过的 enterprise Codex customer story；今天主线选择更新的 Braintrust/Codex case。
- ITBench-AA 是 2026-05-30 已处理过的 enterprise benchmark boundary；今天 OpenAI evaluations playbook 提供了更直接的新评测标准材料。

### matched-rss

- Simon Willison 的 Anthropic containment、Pyodide ASGI、offline retirement notes：第一条是重复 containment 背景，后两条与今日 watch 主线弱相关；不进入高信号。
- Lilian Weng、antirez、lucumr、minimaxir、geohot、Steve Blank、Keygen、SVPG、Ramp 多篇文章多为旧文、背景阅读或弱相关 product/infra 材料；不压过今天的 OpenAI first-party 和 Codex/Claude release。
- FDE Hub、Forward Deployed Episode 5/4、a16z FDE Fellowship、Ted Mabrey 是 FDE 背景/重复窗口；今日只把 Episode 6 作为新的 MarketBench / enterprise world model 线索。
- Pragmatic Engineer OpenCode 与 Antigravity 条目是开发者工具背景，不写成官方产品事实。
- a16z B2B support copilot 是 2026-05-29 已写入 enterprise trend 的重复窗口。

### top-direct-x

- Greg Isenberg / Steipete / Riley Brown / zhaogua61654931 / frxiaobei 的 Claude Opus 4.8、Codex thread spawning、Windows computer use、long-task prompting、review-loop notes：已在 X/Twitter 覆盖说明中按 `direct-x` 使用叙事处理；缺少本地 official fulltext 或独立验证，不升级为产品事实。
- OpenAI / Terence Tao research tweet 未抓到新的 official-link fulltext；保留为后续候选。
- levelsio luxury commentary、generic motivation retweets 与 watch 弱相关，作为噪声处理。

## 不确定性与待验证项

- GitHub REST API 本轮为 `skipped`，release 判断绑定 Atom fallback bodies；limited-body release 只记录版本线。
- OpenAI customer stories 是官方叙事，Braintrust 与 Boston Children’s 的采用数据、临床/业务 outcome、治理流程未独立验证。
- Third-party evaluations playbook 是 OpenAI 对评测报告的建议；需要对照 METR、Apollo、AISI、NIST/ISO 等原始材料后才能写成行业共识。
- Codex `0.135.0` 与 Claude Code `v2.1.158` 未本地实测；Auto mode on Bedrock/Vertex/Foundry 还需要具体 provider 配置验证。
- GitHub Trending README 只证明上榜和 README 可读；Compound Engineering、Cursor plugins、Harness、ECC 需要 install surface、权限、写入文件、卸载路径和真实 repo 试跑审计。

## 今日文档翻译

翻译阶段已完成，父 runner 使用 4 个 shard 运行 `codex exec --json --model gpt-5.4-mini`，最终 check 通过。

- 译读索引：[`../translations/2026-05-31/index.md`](../translations/2026-05-31/index.md)
- 翻译 manifest：[`../translations/2026-05-31/manifest.json`](../translations/2026-05-31/manifest.json)
- `target_count`: 20
- `translated_count`: 20
- `missing_count`: 0

### daily-high-signal

- [`../translations/2026-05-31/daily-high-signal/openai-blog-a-shared-playbook-for-trustworthy-third-party-evaluations-33e1df4abe.opencli.zh.md`](../translations/2026-05-31/daily-high-signal/openai-blog-a-shared-playbook-for-trustworthy-third-party-evaluations-33e1df4abe.opencli.zh.md)
- [`../translations/2026-05-31/daily-high-signal/openai-blog-how-braintrust-turns-customer-requests-into-code-with-codex-507ec0fdf6.opencli.zh.md`](../translations/2026-05-31/daily-high-signal/openai-blog-how-braintrust-turns-customer-requests-into-code-with-codex-507ec0fdf6.opencli.zh.md)
- [`../translations/2026-05-31/daily-high-signal/openai-blog-boston-children-s-uses-ai-to-unlock-new-diagnoses-e63fa88b56.opencli.zh.md`](../translations/2026-05-31/daily-high-signal/openai-blog-boston-children-s-uses-ai-to-unlock-new-diagnoses-e63fa88b56.opencli.zh.md)
- [`../translations/2026-05-31/daily-high-signal/openai-codex-0.135.0-42234c469d.atom.zh.md`](../translations/2026-05-31/daily-high-signal/openai-codex-0.135.0-42234c469d.atom.zh.md)
- [`../translations/2026-05-31/daily-high-signal/anthropics-claude-code-v2.1.158-4a43af6509.atom.zh.md`](../translations/2026-05-31/daily-high-signal/anthropics-claude-code-v2.1.158-4a43af6509.atom.zh.md)
- [`../translations/2026-05-31/daily-high-signal/forward-deployed-forward-deployed-episode-6-market-mechanisms-for-agents-88f1c49929.opencli.zh.md`](../translations/2026-05-31/daily-high-signal/forward-deployed-forward-deployed-episode-6-market-mechanisms-for-agents-88f1c49929.opencli.zh.md)

### trend

- [`../translations/2026-05-31/ai-governance-legitimacy/openai-blog-a-shared-playbook-for-trustworthy-third-party-evaluations-33e1df4abe.opencli.zh.md`](../translations/2026-05-31/ai-governance-legitimacy/openai-blog-a-shared-playbook-for-trustworthy-third-party-evaluations-33e1df4abe.opencli.zh.md)
- [`../translations/2026-05-31/ai-governance-legitimacy/openai-blog-boston-children-s-uses-ai-to-unlock-new-diagnoses-e63fa88b56.opencli.zh.md`](../translations/2026-05-31/ai-governance-legitimacy/openai-blog-boston-children-s-uses-ai-to-unlock-new-diagnoses-e63fa88b56.opencli.zh.md)
- [`../translations/2026-05-31/claude-code-feature-watch/anthropics-claude-code-v2.1.158-4a43af6509.atom.zh.md`](../translations/2026-05-31/claude-code-feature-watch/anthropics-claude-code-v2.1.158-4a43af6509.atom.zh.md)
- [`../translations/2026-05-31/codex-feature-watch/openai-blog-how-braintrust-turns-customer-requests-into-code-with-codex-507ec0fdf6.opencli.zh.md`](../translations/2026-05-31/codex-feature-watch/openai-blog-how-braintrust-turns-customer-requests-into-code-with-codex-507ec0fdf6.opencli.zh.md)
- [`../translations/2026-05-31/codex-feature-watch/openai-codex-0.135.0-42234c469d.atom.zh.md`](../translations/2026-05-31/codex-feature-watch/openai-codex-0.135.0-42234c469d.atom.zh.md)
- [`../translations/2026-05-31/enterprise-delivery-system/openai-blog-a-shared-playbook-for-trustworthy-third-party-evaluations-33e1df4abe.opencli.zh.md`](../translations/2026-05-31/enterprise-delivery-system/openai-blog-a-shared-playbook-for-trustworthy-third-party-evaluations-33e1df4abe.opencli.zh.md)
- [`../translations/2026-05-31/enterprise-delivery-system/openai-blog-boston-children-s-uses-ai-to-unlock-new-diagnoses-e63fa88b56.opencli.zh.md`](../translations/2026-05-31/enterprise-delivery-system/openai-blog-boston-children-s-uses-ai-to-unlock-new-diagnoses-e63fa88b56.opencli.zh.md)
- [`../translations/2026-05-31/enterprise-delivery-system/openai-blog-how-braintrust-turns-customer-requests-into-code-with-codex-507ec0fdf6.opencli.zh.md`](../translations/2026-05-31/enterprise-delivery-system/openai-blog-how-braintrust-turns-customer-requests-into-code-with-codex-507ec0fdf6.opencli.zh.md)
- [`../translations/2026-05-31/forward-deployed-engineering/forward-deployed-forward-deployed-episode-6-market-mechanisms-for-agents-88f1c49929.opencli.zh.md`](../translations/2026-05-31/forward-deployed-engineering/forward-deployed-forward-deployed-episode-6-market-mechanisms-for-agents-88f1c49929.opencli.zh.md)
- [`../translations/2026-05-31/memory-dream/anthropics-claude-code-v2.1.158-4a43af6509.atom.zh.md`](../translations/2026-05-31/memory-dream/anthropics-claude-code-v2.1.158-4a43af6509.atom.zh.md)
- [`../translations/2026-05-31/memory-dream/forward-deployed-forward-deployed-episode-6-market-mechanisms-for-agents-88f1c49929.opencli.zh.md`](../translations/2026-05-31/memory-dream/forward-deployed-forward-deployed-episode-6-market-mechanisms-for-agents-88f1c49929.opencli.zh.md)
- [`../translations/2026-05-31/memory-dream/galilai-group__stable-worldmodel.zh.md`](../translations/2026-05-31/memory-dream/galilai-group__stable-worldmodel.zh.md)
- [`../translations/2026-05-31/memory-dream/openai-blog-a-shared-playbook-for-trustworthy-third-party-evaluations-33e1df4abe.opencli.zh.md`](../translations/2026-05-31/memory-dream/openai-blog-a-shared-playbook-for-trustworthy-third-party-evaluations-33e1df4abe.opencli.zh.md)
- [`../translations/2026-05-31/memory-dream/openai-codex-0.135.0-42234c469d.atom.zh.md`](../translations/2026-05-31/memory-dream/openai-codex-0.135.0-42234c469d.atom.zh.md)
