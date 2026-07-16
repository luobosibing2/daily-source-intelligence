# 2026-06-02 Daily Source Intelligence

## 采集范围

- 运行日期：2026-06-02，时区：Asia/Shanghai。
- 稳定来源：RSS/Atom 32 个 source 全部 ok；命中原文 46/46 fulltext `ok`。GitHub releases 7 个 source 全部通过 Atom fallback ok，GitHub REST API `skipped`；GitHub release always-read 10 条，其中 4 条 fulltext `ok`、6 条 `limited`。GitHub Trending daily 1 个 source ok，解析 repo 10 个，README 10/10 归档；official pages 4 个 source ok。
- X/Twitter：`twitterapi.io` status 为 `ok`，27 个账号请求成功，保留 84 条 direct-x tweet；官方链接候选 4 条且 fulltext `ok`。
- 原始产物：[`../raw/2026-06-02/rss-items.json`](../raw/2026-06-02/rss-items.json)、[`../raw/2026-06-02/github-items.json`](../raw/2026-06-02/github-items.json)、[`../raw/2026-06-02/github-trending.json`](../raw/2026-06-02/github-trending.json)、[`../raw/2026-06-02/official-pages.json`](../raw/2026-06-02/official-pages.json)、[`../raw/2026-06-02/twitterapi-io-results.json`](../raw/2026-06-02/twitterapi-io-results.json)、[`../raw/2026-06-02/official-link-candidates.json`](../raw/2026-06-02/official-link-candidates.json)。
- 状态产物：[`../raw/2026-06-02/manifest.json`](../raw/2026-06-02/manifest.json)、[`../state/source-health.json`](../state/source-health.json)、[`../state/seen.json`](../state/seen.json)。
- 今日新增去重记录：61 条。

## 今日高信号

1. OpenAI on AWS / Codex on Amazon Bedrock 是今天最强 enterprise delivery official-source：OpenAI 写到 frontier models 与 Codex 已在 AWS 上一般可用，企业可以通过既有 security、compliance、procurement、billing、governance 和 GovCloud 路径把 OpenAI capability 放进生产环境。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-06-02/rss-fulltext/openai-blog/openai-blog-openai-frontier-models-and-codex-are-now-available-on-aws-00ed5eb9be.opencli.md`](../raw/2026-06-02/rss-fulltext/openai-blog/openai-blog-openai-frontier-models-and-codex-are-now-available-on-aws-00ed5eb9be.opencli.md)。
2. Codex `0.136.0` 是今天最强 Codex Feature Watch 信号：release body 可读，新增 TUI OSC 8 links / key-value table rendering、`/archive` 与 `codex archive`、app-server resume turns page / MCP status / `--stdio`、`CODEX_API_KEY` remote registration、remote-control server tokens、Windows sandbox elevated setup、standalone image generation extension，并强化 auth refresh、command safety、sandbox cleanup、Bedrock fallback、SDK docs 和 built-in tool schema。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-06-02/github-release-fulltext/openai-codex/openai-codex-0.136.0-1ddf64187c.atom.md`](../raw/2026-06-02/github-release-fulltext/openai-codex/openai-codex-0.136.0-1ddf64187c.atom.md)。
3. OpenAI AI policy and political advocacy 是今天最强 governance legitimacy official-source：OpenAI 明确说明公司没有 super PAC、employee-funded PAC 或候选人/竞选捐款，并把员工个人政治参与与公司 policy positions 切开，同时主张 AI policy 倡议应公开代表关系、政策观点和反 astroturfing。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-06-02/rss-fulltext/openai-blog/openai-blog-our-views-on-ai-policy-and-political-advocacy-c8b9a6b007.opencli.md`](../raw/2026-06-02/rss-fulltext/openai-blog/openai-blog-our-views-on-ai-policy-and-political-advocacy-c8b9a6b007.opencli.md)。
4. Anthropic confidential S-1 是 AI lab institutional / public-market legitimacy 信号：Anthropic 官方页面写到已向 SEC confidentially submitted draft registration statement on Form S-1，为潜在 IPO 保留路径；边界是 Rule 135 公告，不是融资条款或上市已完成事实。证据等级 `official-source` + `direct-x` candidate fulltext `ok`，归档见 [`../raw/2026-06-02/official-link-candidates/anthropicai-2061478052257841495-confidential-draft-s1-sec.extracted.md`](../raw/2026-06-02/official-link-candidates/anthropicai-2061478052257841495-confidential-draft-s1-sec.extracted.md)。
5. GitHub Trending 的 `supermemoryai/supermemory`、`nesquena/hermes-webui`、`EveryInc/compound-engineering-plugin`、`revfactory/harness` 与 `pbakaus/impeccable` 是今天最强 Memory & Dream / operator substrate discovery cluster：README 分别指向 memory/context API、长期运行 agent Web UI、工程方法 plugin、agent team/skill factory 和 frontend design skill vocabulary。证据等级 `secondary-source`，README 10/10 已归档，汇总见 [`../raw/2026-06-02/github-trending.json`](../raw/2026-06-02/github-trending.json)。
6. direct-x 使用战术显示 Codex / Claude Code 正在被当作可组合 operator runtime：Steipete 记录 Codex + webVNC/computer/browser use 做 QA assistant、Codex ad-hoc codemod、voice unblock；Riley Brown 记录 Codex Browser Use、多线程/云 agent 复制；Simon Willison 的 GitHub issue 指向 Codex Desktop `Copy as Markdown` 消失。证据等级 `direct-x`，边界是使用反馈和 issue 线索，不是官方 roadmap，归档见 [`../raw/2026-06-02/twitterapi-io-results.json`](../raw/2026-06-02/twitterapi-io-results.json) 与 [`../raw/2026-06-02/official-link-candidates/simonw-2061158636311958005-25201.extracted.md`](../raw/2026-06-02/official-link-candidates/simonw-2061158636311958005-25201.extracted.md)。

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS：5 条 always-read 全部 fulltext `ok`。今日主线是 OpenAI on AWS / Codex on Bedrock、AI policy and political advocacy、Stargate Michigan infrastructure；Boston Children’s 与 Braintrust/Codex 是前几日已处理过的重复窗口，仍有本地 fulltext。
- OpenAI Codex releases：`0.136.0` fulltext `ok`，可写功能判断；`0.136.0-alpha.2`、`0.136.0-alpha.1`、`python-v0.1.0b2` 为 `limited`，只记录 version-line。`0.135.0` 仍可读但已在前几日处理。
- Claude Code releases：`v2.1.159` 与 `v2.1.158` 为 `limited`，不展开新功能判断；`v2.1.157`、`v2.1.154` 是重复窗口且 fulltext `ok`。
- Official pages：OpenAI news 与 Claude docs release notes 可读；Anthropic newsroom/blog 页面没有可读 fulltext，但 Anthropic S-1 单页通过 official-link candidate 归档为 fulltext `ok`。

## 按主题分组摘要

### AI coding / agent runtime

- Codex `0.136.0` 把用户侧可见 UX、session lifecycle、app-server integration、remote auth、Windows sandbox、extension image artifact、command-safety 和 SDK 文档一起推进，是 runtime hardening + integration surface 扩张。
- OpenAI on AWS 把 Codex 放进 Amazon Bedrock / AWS security-governance operating model，信号重点不是单个模型能力，而是让 coding agent 进入企业既有 cloud procurement、compliance、GovCloud 和 deployment workflow。
- Claude Code 今天没有新的可读 release body；`v2.1.159` 只能记录 limited version-line。

### Memory / context / operator substrate

- `supermemoryai/supermemory` README 把自己定位为 AI memory/context layer，并强调 benchmark 与 API；这是 Memory & Dream 的 discovery signal，需要后续验证 API、数据边界、隐私和 benchmark 可复现性。
- `nesquena/hermes-webui` 把 Hermes Agent 从 terminal/messaging app 扩展到 browser/mobile Web UI，强调 agent remembers what it learns 和 longer-running capability；边界是 README self-description。
- `EveryInc/compound-engineering-plugin`、`revfactory/harness`、`pbakaus/impeccable` 都在把 agent work method、team architecture 和 design vocabulary 包成可安装技能/插件，说明 operator playbook 正在变成 repo/package artifact。

### Enterprise / delivery system

- OpenAI on AWS 是企业交付系统强信号：AWS-native security/governance controls、Commercial and GovCloud regions、procurement/billing/compliance paths 会降低从 evaluation 到 production 的组织摩擦。
- Codex `0.136.0` 的 app-server `--stdio`、remote server tokens、API-key remote registration、MCP status 与 Windows sandbox setup，对 enterprise embedding、remote execution 和治理边界都有直接含义。
- Stargate Michigan infrastructure 是 AI infrastructure / policy investment signal，但与本仓 enterprise delivery 主题的直接 workflow 证据弱于 AWS/Codex。

### AI governance / public legitimacy

- OpenAI political advocacy 文档直接回应 AI policy 进入政治叙事后的代表性、透明度和 astroturfing 风险，是 public legitimacy 高信号；它仍是 OpenAI 官方立场，不是外部审计。
- Anthropic confidential S-1 是 frontier AI lab 进入 public-market governance 的制度化信号；它不说明 IPO 时间、价格或完成状态。
- Rosalind Biodefense 官方链接候选本日再次出现且 fulltext `ok`，但此前已处理为高信号；今天只作为 OpenAI public-good / high-stakes framing 的重复窗口保留。

### Financial agents

- `TauricResearch/TradingAgents` 上榜并有 README；它是 multi-agent LLM financial trading framework discovery signal，涉及 trading、sentiment analyst、API key、ticker path traversal fix 与 benchmark claims。边界：GitHub Trending + README 不等于金融机构采用，不可写成投资建议或交易有效性证明。

### Forward Deployed Engineering

- 今天没有新的 FDE official/customer high-signal。a16z FDE Fellowship、FDE Hub、Forward Deployed podcast 等仍是重复或背景窗口；不重复升级。

### Codex & Claude Code Usage Tactics

- Steipete 的 QA assistant 做法把 Codex 与 webVNC/computer/browser use 接成后台用户验收测试；这是可复用 operator tactic，但仍是 direct-x 单人经验。
- Riley Brown 的 Codex Browser Use / cloud agent copy prompt 说明用户在把 Codex setup 复制到 persistent cloud agent 和 messaging interface；需要区分战术线索与官方产品能力。
- Matt Pocock 对 Claude Code “workflow” 模式误触的抱怨，是 agent command semantics / skill trigger ambiguity 的负面使用反馈，可作为 usage-tactics 的失败模式而不是产品发布结论。

### GitHub Trending discovery

GitHub Trending 今日解析到 10 个 repo，README 归档 10/10 成功，来源边界是 `secondary-source` discovery signal。

- `microsoft/markitdown`：Microsoft 的文件/Office 文档转 Markdown 工具，面向 LLM ingestion 和文本分析 pipeline；README 特别提醒它以当前进程权限执行 I/O，非可信环境要清洗输入并选择最窄 `convert_*` 函数。今天值得记录的是它继续作为 agent 文档入口工具上榜；不等于新发布或安全审计通过。
- `nesquena/hermes-webui`：Hermes Agent 的 Web/mobile UI，把原本 terminal/messaging app 中的长期运行 agent 暴露到 browser，README 声称保持 CLI parity、无 build step、可远程访问。它解决的是 server-side autonomous agent 的可视化/移动端操作问题；风险是远程 agent UI 的认证、权限和长期记忆边界需另行审计。
- `supermemoryai/supermemory`：AI memory/context engine 与 personal/company brain，README 声称 LongMemEval、LoCoMo、ConvoMem 排名和 API。它面向跨会话记忆、语义检索和上下文层；今天只作为 memory substrate discovery，不验证 benchmark 或数据治理。
- `harry0703/MoneyPrinterTurbo`：AI 短视频生成工具，从主题/关键词自动生成文案、素材、字幕、配乐并合成视频，支持 Web/API。它面向内容生产自动化；风险是版权、素材来源、平台滥用和低质量内容扩散。
- `D4Vinci/Scrapling`：自适应 Web scraping framework，提供 parser、fetchers、spiders、proxy rotation、CLI 和 MCP，强调网站变化后的元素重定位。它对 agent web data collection 有工具价值；风险是反爬、合规、目标站点 ToS 和凭据/代理使用边界。
- `pbakaus/impeccable`：面向 AI harness 的 frontend design skill / command bundle，提供 design vocabulary 和 anti-patterns，让模型生成更稳定的前端设计。它属于 operator skill package discovery；需要验证安装面、命令内容和是否过度覆盖项目本地设计系统。
- `p-e-w/heretic`：自动移除模型 safety alignment/censorship 的工具，README 声称使用 directional ablation 和 Optuna 优化。它与本 watch 的安全/治理边界高度敏感；只能记录为 risk discovery，不应作为正常 agent tooling 推荐。
- `EveryInc/compound-engineering-plugin`：跨 Claude Code、Codex、Cursor 等的 Compound Engineering plugin，把 engineering strategy、brainstorm、plan、debug、review 等方法打包成技能/agent。它是 agent operator methodology packaging 的强 discovery signal；仍需安装、权限和文件写入审计。
- `TauricResearch/TradingAgents`：多智能体 LLM 金融交易框架，README 提到 sentiment analyst、GPT-5.5、Qwen/GLM/MiniMax、API-key auto-detection、remote Ollama 和 ticker path traversal fix。它是 Financial Agents discovery signal；不证明交易收益或合规可用。
- `revfactory/harness`：Claude Code 的 team-architecture factory，根据项目描述生成 domain-specific agent team 和 skills。它对 Memory & Dream / operator tactics 有 substrate 价值；README discovery 不能替代实际生成质量、权限和维护成本审计。

## 来源证据表

| 信号 | 证据等级 | 本地归档 | 边界 |
| --- | --- | --- | --- |
| OpenAI on AWS / Codex on Bedrock | official-source | [`../raw/2026-06-02/rss-fulltext/openai-blog/openai-blog-openai-frontier-models-and-codex-are-now-available-on-aws-00ed5eb9be.opencli.md`](../raw/2026-06-02/rss-fulltext/openai-blog/openai-blog-openai-frontier-models-and-codex-are-now-available-on-aws-00ed5eb9be.opencli.md) | OpenAI 官方产品发布；客户采用效果未独立验证。 |
| Codex `0.136.0` | official-source | [`../raw/2026-06-02/github-release-fulltext/openai-codex/openai-codex-0.136.0-1ddf64187c.atom.md`](../raw/2026-06-02/github-release-fulltext/openai-codex/openai-codex-0.136.0-1ddf64187c.atom.md) | Release body 可读；未本地实测各功能。 |
| OpenAI political advocacy | official-source | [`../raw/2026-06-02/rss-fulltext/openai-blog/openai-blog-our-views-on-ai-policy-and-political-advocacy-c8b9a6b007.opencli.md`](../raw/2026-06-02/rss-fulltext/openai-blog/openai-blog-our-views-on-ai-policy-and-political-advocacy-c8b9a6b007.opencli.md) | OpenAI 自述立场；不是外部政治资金审计。 |
| Anthropic confidential S-1 | official-source / direct-x candidate | [`../raw/2026-06-02/official-link-candidates/anthropicai-2061478052257841495-confidential-draft-s1-sec.extracted.md`](../raw/2026-06-02/official-link-candidates/anthropicai-2061478052257841495-confidential-draft-s1-sec.extracted.md) | Rule 135 公告；不是 IPO 已完成或条款确定。 |
| GitHub Trending memory/operator cluster | secondary-source | [`../raw/2026-06-02/github-trending.json`](../raw/2026-06-02/github-trending.json) | README discovery；不证明 adoption、安全或质量。 |
| Codex / Claude Code usage tactics | direct-x | [`../raw/2026-06-02/twitterapi-io-results.json`](../raw/2026-06-02/twitterapi-io-results.json) | 公开使用反馈；未补 thread/context，不等于官方功能承诺。 |

## X/Twitter 覆盖说明

`twitterapi.io` status 为 `ok`，27 个账号均成功请求；共保留 84 条窗口内 tweet。高相关 direct-x 包括 OpenAI 的 AWS/Codex 发布、Anthropic 的 S-1 公告、Steipete 的 Codex QA assistant / ad-hoc codemod / voice unblock 使用反馈、Simon Willison 的 Codex Desktop `Copy as Markdown` issue、Riley Brown 的 Codex Browser Use / persistent cloud agent setup、Matt Pocock 的 Claude Code workflow mode 误触反馈、frxiaobei 的 Codex as agent runtime 观察。所有直接来自 API 的 tweet 按 `direct-x` 处理；官方链接候选 4 条均已抓取 fulltext，见 [`../raw/2026-06-02/official-link-candidates.json`](../raw/2026-06-02/official-link-candidates.json)。

## Candidate audit 处理记录

[`../reviews/2026-06-02-candidate-audit.md`](../reviews/2026-06-02-candidate-audit.md) 已生成：`covered=4`、`missed=56`。已覆盖项包括 OpenAI political advocacy、OpenAI on AWS / Codex、Anthropic S-1、Simon Willison 的 Codex Desktop `Copy as Markdown` issue。剩余 missed 已审计，处理如下：

### official-link-candidate / repeated first-party

- OpenAI on AWS official-link-candidate 被 audit 记为 missed 是 URL trailing slash / source-category 匹配问题；正文已在“今日高信号”“Enterprise / delivery system”“来源证据表”中覆盖，证据为 RSS fulltext 与 official-link candidate 双重归档。
- Rosalind Biodefense official-link-candidate 是 2026-05-30/2026-05-31 已处理过的重复窗口；今天只在 governance 摘要和 X/Twitter 覆盖说明中保留，不重复升级。
- Boston Children’s 与 Braintrust/Codex 是 2026-05-31 已写入日报和 trend 的重复窗口；今天的 enterprise 主线选择更新的 OpenAI on AWS / Codex on Bedrock。
- Stargate Michigan infrastructure 是 AI infrastructure / policy investment signal；与本仓 enabled trends 的直接 agent workflow 证据弱于 OpenAI on AWS，不进入今日高信号。

### matched-rss

- Gemini Omni、IBM/Hugging Face agent logic、Simon Willison newsletter / subscription note、Lilian Weng 旧文、antirez / lucumr / minimaxir / geohot / Steve Blank / Keygen / SVPG 多篇文章多为旧文、背景阅读或弱相关 product/infra 材料；不压过今日 first-party OpenAI/Codex 与 Trending substrate。
- Simon Willison 的 Meta AI account access security story 与 OpenAI/Codex issue 中的 `Copy as Markdown` 更相关者已选后者；前者作为 AI security 背景，不写成本仓 enabled trend 新结论。
- FDE Hub、Forward Deployed Episode 4/5/6、a16z FDE Fellowship、Ted Mabrey 是 FDE 背景或前几日重复窗口；今天没有新的 FDE official/customer high-signal。
- Ramp marketing-to-agents / receipt matching / ML serving 和 a16z B2B support copilot 与 product/finance 背景有关，但今天未提供比 AWS/Codex、Codex `0.136.0`、TradingAgents README 更强的新趋势信息。

### top-direct-x

- Greg Isenberg 的 GPT wrappers / AI platform-shift 和 GPT Realtime startup ideas 是 broad startup commentary；缺少本地 official fulltext 或可验证 deployment，不升级为趋势结论。
- Steipete 的 Codex QA assistant、Matt Pocock 的 Claude Code workflow mode 误触、Riley Brown 的 Codex Browser Use / cloud agent setup 已在“今日高信号”“Codex & Claude Code Usage Tactics”“X/Twitter 覆盖说明”中按 `direct-x` 使用战术处理。
- Hesamation 的 self-hosted AI workspace、OpenAI Robotics hiring、Codex 5M users retweet、AI animation prompting retweet、European Commission commentary 等为弱相关、招聘、转推或泛政治/创作话题；不进入高信号。

## 不确定性与待验证项

- GitHub REST API 本轮为 `skipped`，release 判断绑定 Atom fallback bodies；limited-body release 只记录版本线。
- OpenAI on AWS 是官方产品发布与客户 quote；Amgen、Autodesk 的实际部署深度、生产效果、GovCloud 使用和安全流程未独立验证。
- Codex `0.136.0` 未本地实测；`/archive`、remote-control server tokens、Windows sandbox elevated setup、standalone image generation extension 与 Bedrock fallback 需要分别在对应平台/账号环境验证。
- OpenAI political advocacy 是公司自述；政治资金、outside group 关系与 astroturfing 边界需要外部披露/监管材料才能独立核查。
- Anthropic S-1 公告不包含注册文件正文、发行数量、价格或上市时间；不能写成 IPO 已完成。
- GitHub Trending README 只证明上榜和 README 可读；`heretic`、`TradingAgents`、`Scrapling` 等涉及 safety removal、trading、scraping 和代理/凭据边界的项目需要额外安全与合规审计。

## 今日文档翻译

翻译阶段已完成，父 runner 使用 4 个 shard 运行 `codex exec --json --model gpt-5.4-mini`，最终 check 通过。

- 译读索引：[`../translations/2026-06-02/index.md`](../translations/2026-06-02/index.md)
- 翻译 manifest：[`../translations/2026-06-02/manifest.json`](../translations/2026-06-02/manifest.json)
- `target_count`: 18
- `translated_count`: 18
- `missing_count`: 0

### daily-high-signal

- [`../translations/2026-06-02/daily-high-signal/openai-blog-openai-frontier-models-and-codex-are-now-available-on-aws-00ed5eb9be.opencli.zh.md`](../translations/2026-06-02/daily-high-signal/openai-blog-openai-frontier-models-and-codex-are-now-available-on-aws-00ed5eb9be.opencli.zh.md)
- [`../translations/2026-06-02/daily-high-signal/openai-codex-0.136.0-1ddf64187c.atom.zh.md`](../translations/2026-06-02/daily-high-signal/openai-codex-0.136.0-1ddf64187c.atom.zh.md)
- [`../translations/2026-06-02/daily-high-signal/openai-blog-our-views-on-ai-policy-and-political-advocacy-c8b9a6b007.opencli.zh.md`](../translations/2026-06-02/daily-high-signal/openai-blog-our-views-on-ai-policy-and-political-advocacy-c8b9a6b007.opencli.zh.md)
- [`../translations/2026-06-02/daily-high-signal/anthropicai-2061478052257841495-confidential-draft-s1-sec.extracted.zh.md`](../translations/2026-06-02/daily-high-signal/anthropicai-2061478052257841495-confidential-draft-s1-sec.extracted.zh.md)
- [`../translations/2026-06-02/daily-high-signal/simonw-2061158636311958005-25201.extracted.zh.md`](../translations/2026-06-02/daily-high-signal/simonw-2061158636311958005-25201.extracted.zh.md)

### trend

- [`../translations/2026-06-02/ai-governance-legitimacy/anthropicai-2061478052257841495-confidential-draft-s1-sec.extracted.zh.md`](../translations/2026-06-02/ai-governance-legitimacy/anthropicai-2061478052257841495-confidential-draft-s1-sec.extracted.zh.md)
- [`../translations/2026-06-02/ai-governance-legitimacy/openai-blog-our-views-on-ai-policy-and-political-advocacy-c8b9a6b007.opencli.zh.md`](../translations/2026-06-02/ai-governance-legitimacy/openai-blog-our-views-on-ai-policy-and-political-advocacy-c8b9a6b007.opencli.zh.md)
- [`../translations/2026-06-02/codex-claude-usage-tactics/simonw-2061158636311958005-25201.extracted.zh.md`](../translations/2026-06-02/codex-claude-usage-tactics/simonw-2061158636311958005-25201.extracted.zh.md)
- [`../translations/2026-06-02/codex-feature-watch/openai-blog-openai-frontier-models-and-codex-are-now-available-on-aws-00ed5eb9be.opencli.zh.md`](../translations/2026-06-02/codex-feature-watch/openai-blog-openai-frontier-models-and-codex-are-now-available-on-aws-00ed5eb9be.opencli.zh.md)
- [`../translations/2026-06-02/codex-feature-watch/openai-codex-0.136.0-1ddf64187c.atom.zh.md`](../translations/2026-06-02/codex-feature-watch/openai-codex-0.136.0-1ddf64187c.atom.zh.md)
- [`../translations/2026-06-02/enterprise-delivery-system/openai-blog-openai-frontier-models-and-codex-are-now-available-on-aws-00ed5eb9be.opencli.zh.md`](../translations/2026-06-02/enterprise-delivery-system/openai-blog-openai-frontier-models-and-codex-are-now-available-on-aws-00ed5eb9be.opencli.zh.md)
- [`../translations/2026-06-02/enterprise-delivery-system/openai-codex-0.136.0-1ddf64187c.atom.zh.md`](../translations/2026-06-02/enterprise-delivery-system/openai-codex-0.136.0-1ddf64187c.atom.zh.md)
- [`../translations/2026-06-02/financial-agents/TauricResearch__TradingAgents.zh.md`](../translations/2026-06-02/financial-agents/TauricResearch__TradingAgents.zh.md)
- [`../translations/2026-06-02/memory-dream/EveryInc__compound-engineering-plugin.zh.md`](../translations/2026-06-02/memory-dream/EveryInc__compound-engineering-plugin.zh.md)
- [`../translations/2026-06-02/memory-dream/nesquena__hermes-webui.zh.md`](../translations/2026-06-02/memory-dream/nesquena__hermes-webui.zh.md)
- [`../translations/2026-06-02/memory-dream/pbakaus__impeccable.zh.md`](../translations/2026-06-02/memory-dream/pbakaus__impeccable.zh.md)
- [`../translations/2026-06-02/memory-dream/revfactory__harness.zh.md`](../translations/2026-06-02/memory-dream/revfactory__harness.zh.md)
- [`../translations/2026-06-02/memory-dream/supermemoryai__supermemory.zh.md`](../translations/2026-06-02/memory-dream/supermemoryai__supermemory.zh.md)
