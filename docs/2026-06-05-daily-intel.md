# 2026-06-05 Daily Source Intelligence

## 采集范围

- 运行日期：2026-06-05，时区：Asia/Shanghai。
- 稳定来源：RSS/Atom 32 个 source 全部 ok；命中原文 41/41 fulltext `ok`。GitHub releases 7 个 source 全部通过 Atom fallback ok，GitHub REST API `skipped`；GitHub release always-read 10 条，其中 5 条 fulltext `ok`、5 条 `limited`。GitHub Trending daily 1 个 source ok，解析 repo 10 个，README 10/10 归档；official pages 4 个 source ok。
- X/Twitter：`twitterapi.io` status 为 `ok`，27 个账号请求成功，保留 122 条 direct-x tweet；官方链接候选 5 条且 fulltext `ok`。
- 原始产物：[`../raw/2026-06-05/rss-items.json`](../raw/2026-06-05/rss-items.json)、[`../raw/2026-06-05/github-items.json`](../raw/2026-06-05/github-items.json)、[`../raw/2026-06-05/github-trending.json`](../raw/2026-06-05/github-trending.json)、[`../raw/2026-06-05/official-pages.json`](../raw/2026-06-05/official-pages.json)、[`../raw/2026-06-05/twitterapi-io-results.json`](../raw/2026-06-05/twitterapi-io-results.json)、[`../raw/2026-06-05/official-link-candidates.json`](../raw/2026-06-05/official-link-candidates.json)。
- 状态产物：[`../raw/2026-06-05/manifest.json`](../raw/2026-06-05/manifest.json)、[`../state/source-health.json`](../state/source-health.json)、[`../state/seen.json`](../state/seen.json)。
- 今日新增去重记录：55 条。

## 今日高信号

1. OpenAI `Dreaming` memory update 是 Memory & Dream 今日最高信号：OpenAI 把 ChatGPT memory 描述为后台综合历史对话、处理 freshness/continuity/relevance、可在 memory summary 中审阅和纠正的系统，并开始向 US Plus/Pro 推出。证据等级 `official-source` + `direct-x` candidate fulltext `ok`，归档见 [`../raw/2026-06-05/rss-fulltext/openai-blog/openai-blog-dreaming-better-memory-for-a-more-helpful-chatgpt-58a72a3a66.opencli.md`](../raw/2026-06-05/rss-fulltext/openai-blog/openai-blog-dreaming-better-memory-for-a-more-helpful-chatgpt-58a72a3a66.opencli.md) 与 [`../raw/2026-06-05/official-link-candidates/openai-2062567556524003631-chatgpt-memory-dreaming.opencli.md`](../raw/2026-06-05/official-link-candidates/openai-2062567556524003631-chatgpt-memory-dreaming.opencli.md)。
2. OpenAI Endava case 是 enterprise delivery / FDE-adjacent 高信号：Endava 把 OpenAI 作为 enterprise AI platform，DavaFlow 从 meeting prep、planning、product discovery 到 engineering/deployment 都嵌入 ChatGPT/Codex，并把 requirements、business analysis、governance reports、internal pricing app 等非编码环节也放进 agent workflow。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-06-05/rss-fulltext/openai-blog/openai-blog-how-endava-is-redesigning-software-delivery-around-ai-agents-d0841d29a3.opencli.md`](../raw/2026-06-05/rss-fulltext/openai-blog/openai-blog-how-endava-is-redesigning-software-delivery-around-ai-agents-d0841d29a3.opencli.md)。
3. Anthropic `Recursive self-improvement` 是 AI governance / AI lab operations 高信号：Anthropic 用内部数据描述 Claude 正在加速 AI development，讨论从 code writing 到 experiment/research judgment 的人机分工变化、human review bottleneck、Amdahl's law、verifiable slowdown/pause 等治理问题。证据等级 `official-source` + `direct-x` candidate fulltext `ok`，归档见 [`../raw/2026-06-05/official-link-candidates/anthropicai-2062568862479208923-recursive-self-improvement.extracted.md`](../raw/2026-06-05/official-link-candidates/anthropicai-2062568862479208923-recursive-self-improvement.extracted.md)。
4. OpenAI `Biodefense in the Intelligence Age` 是 high-risk domain governance 高信号：OpenAI 把 frontier model access、biosecurity preparedness、expert review 和 institutional partnership 放在 biodefense 框架里讨论。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-06-05/rss-fulltext/openai-blog/openai-blog-biodefense-in-the-intelligence-age-dbb39445d0.opencli.md`](../raw/2026-06-05/rss-fulltext/openai-blog/openai-blog-biodefense-in-the-intelligence-age-dbb39445d0.opencli.md)。
5. Claude Code `v2.1.163` 是今日最强 first-party Claude Code runtime release：新增 managed version bounds、`/plugin list`、hook `additionalContext`、skills `$` escape、MCP session id propagation，并修复 `claude -p` hang、Bedrock/Vertex/Foundry CI auth、TMPDIR regression、managed permission startup、background sessions update/reattach、Windows/OneDrive session-env 等问题。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-06-05/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.163-d2176cb2c2.atom.md`](../raw/2026-06-05/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.163-d2176cb2c2.atom.md)。
6. GitHub Trending `github/copilot-sdk` 是 agent runtime productization 高信号：README 显示 GitHub 正把 Copilot CLI agent engine 暴露为 Python、TypeScript、Go、.NET、Java、Rust SDK，可通过 JSON-RPC 调 Copilot CLI server，并支持 BYOK、OAuth/GitHub token、custom agents/tools/skills。证据等级 `secondary-source` discovery，README 归档见 [`../raw/2026-06-05/github-trending-readmes/github__copilot-sdk.md`](../raw/2026-06-05/github-trending-readmes/github__copilot-sdk.md)。
7. GitHub Trending `github/spec-kit` 是 Spec-Driven Development / usage tactics 高信号：README 把 specifications 作为 executable artifact，给出 `specify init`、`/speckit.constitution`、`/speckit.specify`、`/speckit.plan`、`/speckit.tasks`、`/speckit.implement` 的 agent workflow。证据等级 `secondary-source` discovery，README 归档见 [`../raw/2026-06-05/github-trending-readmes/github__spec-kit.md`](../raw/2026-06-05/github-trending-readmes/github__spec-kit.md)。
8. GitHub Trending 的 `Hermes Agent`、`Headroom`、`ECC`、`open-notebook` 继续形成 Memory & Dream / operator substrate cluster：README 分别指向 self-improving skills、persistent memory、context compression、cross-harness operator rules、NotebookLM-like flexible research notebook。证据等级 `secondary-source`，README 10/10 已归档，汇总见 [`../raw/2026-06-05/github-trending.json`](../raw/2026-06-05/github-trending.json)。

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS：5 条 always-read 全部 fulltext `ok`。今天新增 Endava enterprise delivery case、ChatGPT memory dreaming、biodefense；GPT-Rosalind 与 Wasmer/Codex 是 2026-06-04 已处理过的重复窗口，但仍保留归档证据。
- OpenAI Codex releases：`0.137.0` fulltext `ok`，但已在 2026-06-04 作为主信号处理；`0.138.0-alpha.1` 到 `0.138.0-alpha.4` 均为 `limited`，只记录版本线，不展开为 feature claim。
- Claude Code releases：`v2.1.163` fulltext `ok`，作为今天 feature-watch 主信号；`v2.1.162` / `v2.1.161` / `v2.1.160` 是重复窗口或前日已处理内容；`v2.1.159` 为 `limited`。
- Official pages：OpenAI News、Anthropic News、Claude Docs release notes、Claude Blog 均 ok；official-link candidates 把 ChatGPT memory dreaming、Anthropic recursive self-improvement、GPT-Rosalind、Anthropic cyber threats、Steipete MS Build talk 归档为 fulltext `ok`。

## 按主题分组摘要

### Memory / context / operator substrate

- OpenAI `Dreaming` 把 consumer memory 从显式 saved memories 推向后台综合与 summary review。关键点不是“多记一点”，而是 memory lifecycle：freshness、continuity、relevance、用户可审阅/纠错、跨多年历史和数亿用户规模的 compute-efficient synthesis。
- GitHub Trending 的 Hermes Agent / Headroom / ECC / open-notebook 继续说明 agent memory 正在从单点记忆扩成 runtime substrate：skills 自我改进、session search、context compression、cross-agent memory、可逆 retrieval、研究 notebook 和 messaging gateway。
- Direct-x 中 Greg Isenberg、EXM7777、Jack Friks、zhaogua61654931 也都在讨论 skills、safe actions、memory、agent coordination 和 skill 安装风险；这些是 operator notes，不是官方产品事实。

### Enterprise delivery / FDE

- Endava case 的核心是软件交付链路重排：工程产出加速后，requirements、business analysis、planning、stakeholder coordination、governance reporting 和 internal app generation 也要同步提速。它比“开发者使用 AI coding”更接近 enterprise delivery operating model。
- FDE 角度上，Endava 不是标准 FDE/FDSE 组织案例，但它证明 enterprise AI deployment 的瓶颈在 workflow redesign 与组织行为改变；Ted Mabrey `Sorry, that isn't an FDE` 仍作为 FDE 边界旧文保留，提醒不要把 implementation engineer 直接改名为 FDE。
- GitHub Copilot SDK 把 agent engine 开放给应用，Spec Kit 把 spec/plan/tasks/implement 流程产品化；两者都是 delivery system substrate，而不是单个项目 adoption 证明。

### AI governance / public legitimacy

- Anthropic recursive self-improvement 把治理问题推进到 lab 内部生产函数：如果 Claude 写代码、跑实验和提出 next-step research choice 的能力持续上升，human review、research taste、verification 和 coordinated slowdown/pause 将变成关键瓶颈。
- OpenAI biodefense 与 GPT-Rosalind 延续 high-risk domain trusted access 线索：生命科学/生物安全能力需要 expert review、mission gating、institutional partnership 和 access-control，而不是单纯按模型能力发布。
- Anthropic cyber threats 是昨日已处理但今天仍作为 official-link candidate 出现；今天不重复升级，只在治理 cluster 中保留边界。

### AI coding / agent runtime

- Claude Code `v2.1.163` 继续把企业管控、plugin observability、hook feedback、skills command bodies、MCP/session identity、background sessions 和 Windows/EDR/Bazel 环境兼容性做扎实。它的意义是 Claude Code runtime 更像可被 org-managed policies 约束的长期 agent environment。
- Codex `0.137.0` 今天仍在 Atom 窗口内，但主信号已于 2026-06-04 处理；今天仅作为 Codex Feature Watch 的重复证据，不重复升级。
- GitHub Copilot SDK 是更大的 product-shape 信号：Copilot agent 不只在 GitHub UI/CLI 中运行，而是可以嵌进外部应用和服务；README 明确提到 custom agents、skills、tools 和 permission handler。

### Product / growth / indie founder

- Greg Isenberg 的 Codex Sites 长帖把 apps framed as live agent-controlled systems：persistent storage、safe actions、skills、save gates、agent 可以从任意 chat/context 更新 app。证据等级 `direct-x`，但缺少官方本地归档链接和产品文档验证，所以只写 usage-tactics 摘要。
- Levelsio 提出 `$ / Mt`，用每百万 tokens 创造的收入衡量 AI token spend；与 Uber cap / token budget 线索一起说明 operator cost accounting 正在成为实践问题。
- Marc Lou、Jack Friks 的 direct-x 主要是独立开发产品/支持/feature shipping 经验，质量参差，不进入高信号。

### Financial agents

- 今天没有新的 finance-specific official/customer/action-surface 信号。Levelsio/Marc Lou/Jack Friks 的 finance/money tweets 是个人创业或个人财务经验，不是金融服务 agent workflow；因此 Financial Agents 在 trend report 中记录 `no-new-signal`。

### GitHub Trending discovery

GitHub Trending 今日解析到 10 个 repo，README 归档 10/10 成功，来源边界是 `secondary-source` discovery signal。

- `chopratejas/headroom`：agent context compression layer，面向 tool outputs、logs、RAG chunks、files 和 conversation history，提供 library、proxy、agent wrap、MCP server、cross-agent memory、`headroom learn`、reversible retrieval。它解决的是 agent 上下文成本和可检索压缩问题；风险是代理/包装层会接触 prompt、tool output、provider traffic 和本地存储，需要隐私、日志、回放与 retrieval 权限审计。
- `NousResearch/hermes-agent`：self-improving AI agent，README 描述 built-in learning loop、skills from experience、session search、messaging gateway、cron、subagents、terminal backends、trajectory compression 和 cloud/serverless persistence。它是 Memory & Dream 强 discovery；风险是 messaging credentials、remote terminal、persistent memory、gateway permissions 和 auto-skill update 都需要审计。
- `affaan-m/ECC`：cross-harness operator system，覆盖 Codex、Claude Code、OpenCode、Cursor、Gemini、Copilot 等，打包 skills、instincts、memory optimization、continuous learning、security scanning、hooks、rules、MCP configs。它是 usage-tactics discovery，不证明 star 数、安全或生产质量。
- `PaddlePaddle/PaddleOCR`：AI-ready OCR toolkit，把 PDF/image 转结构化数据，支持多语言和文档解析；与本仓主线的关系是 document ingestion substrate，需要验证 layout fidelity、OCR benchmark、隐私和版权处理。
- `github/spec-kit`：Spec-Driven Development toolkit，将 spec、plan、tasks、implement 做成 agent workflow；适合纳入 usage tactics / enterprise delivery，但 README 不能证明真实项目成功率。
- `NVIDIA/cosmos`：physical AI world models / datasets / tools platform，面向 robotics、autonomous vehicles、smart infrastructure；与 agent/devtool 主线相邻，需另行验证模型、数据许可和部署边界。
- `lfnovo/open-notebook`：NotebookLM-like open source implementation，面向灵活研究 notebook；是 memory/research workspace discovery，需验证 data ingestion、citation fidelity 和隐私。
- `Open-LLM-VTuber/Open-LLM-VTuber`：本地 voice/Live2D LLM interaction 项目；与 agent 主线弱相关，涉及 voice/avatar/always-on interaction 风险。
- `jwasham/coding-interview-university`：计算机科学学习计划，多年成熟 repo；今天只是泛 dev education discovery，不是 AI signal。
- `github/copilot-sdk`：GitHub Copilot agent SDK，跨语言嵌入 Copilot CLI engine；是 agent runtime productization discovery，但 README 不能替代官方 release/adoption 证据。

## 来源证据表

| 信号 | 证据等级 | 本地归档 | 边界 |
| --- | --- | --- | --- |
| ChatGPT memory dreaming | official-source / direct-x candidate | [`../raw/2026-06-05/rss-fulltext/openai-blog/openai-blog-dreaming-better-memory-for-a-more-helpful-chatgpt-58a72a3a66.opencli.md`](../raw/2026-06-05/rss-fulltext/openai-blog/openai-blog-dreaming-better-memory-for-a-more-helpful-chatgpt-58a72a3a66.opencli.md) | OpenAI 自述 rollout 与 eval；未验证用户实际 memory behavior、地区 rollout 或 opt-out UX。 |
| Endava / DavaFlow | official-source | [`../raw/2026-06-05/rss-fulltext/openai-blog/openai-blog-how-endava-is-redesigning-software-delivery-around-ai-agents-d0841d29a3.opencli.md`](../raw/2026-06-05/rss-fulltext/openai-blog/openai-blog-how-endava-is-redesigning-software-delivery-around-ai-agents-d0841d29a3.opencli.md) | OpenAI customer case；组织 adoption 与效果数字未独立审计。 |
| Anthropic recursive self-improvement | official-source / direct-x candidate | [`../raw/2026-06-05/official-link-candidates/anthropicai-2062568862479208923-recursive-self-improvement.extracted.md`](../raw/2026-06-05/official-link-candidates/anthropicai-2062568862479208923-recursive-self-improvement.extracted.md) | Anthropic 内部数据和观点；对未来 recursive self-improvement 的判断含推断和场景分析。 |
| OpenAI biodefense | official-source | [`../raw/2026-06-05/rss-fulltext/openai-blog/openai-blog-biodefense-in-the-intelligence-age-dbb39445d0.opencli.md`](../raw/2026-06-05/rss-fulltext/openai-blog/openai-blog-biodefense-in-the-intelligence-age-dbb39445d0.opencli.md) | 政策/风险框架；具体 access criteria、partner review 和 operational controls 需后续验证。 |
| Claude Code `v2.1.163` | official-source | [`../raw/2026-06-05/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.163-d2176cb2c2.atom.md`](../raw/2026-06-05/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.163-d2176cb2c2.atom.md) | Release body 可读；未本地复现 managed version bounds、hooks、MCP/session、background fixes。 |
| GitHub Copilot SDK | secondary-source | [`../raw/2026-06-05/github-trending-readmes/github__copilot-sdk.md`](../raw/2026-06-05/github-trending-readmes/github__copilot-sdk.md) | README discovery；需官方 release/docs、API install test、auth/billing/permission 审计。 |
| Spec Kit | secondary-source | [`../raw/2026-06-05/github-trending-readmes/github__spec-kit.md`](../raw/2026-06-05/github-trending-readmes/github__spec-kit.md) | README discovery；不证明 SDD 成功率或 agent execution quality。 |
| Memory/operator Trending cluster | secondary-source | [`../raw/2026-06-05/github-trending.json`](../raw/2026-06-05/github-trending.json) | README discovery；不证明 adoption、安全、benchmark 或生产可用性。 |

## X/Twitter 覆盖说明

`twitterapi.io` status 为 `ok`，27 个账号均成功请求；共保留 122 条窗口内 tweet。高相关 direct-x 包括 OpenAI 的 ChatGPT memory dreaming / GPT-Rosalind / math podcast、Anthropic 的 recursive self-improvement / AI-enabled cyber threats、Greg Isenberg 的 Codex Sites autonomous app framing、Matt Pocock 的 `/grill-prep` / AI coding dictionary / skills discussion、Steipete 的 OpenClaw / MS Build talk、EXM7777 的 skill install hygiene 和 agent auditability、Riley Brown 的 agent-visible content / building-block thinking、Genspark + Microsoft Build enterprise-agent positioning。所有直接来自 API 的 tweet 按 `direct-x` 处理；官方链接候选 5 条均已抓取 fulltext，见 [`../raw/2026-06-05/official-link-candidates.json`](../raw/2026-06-05/official-link-candidates.json)。

## Candidate audit 处理记录

[`../reviews/2026-06-05-candidate-audit.md`](../reviews/2026-06-05-candidate-audit.md) 已生成：`covered=6`、`missed=50`。已覆盖项包括 ChatGPT memory dreaming、Anthropic recursive self-improvement、Endava/DavaFlow、OpenAI biodefense、Ted Mabrey FDE 边界文本。剩余 missed 已审计，处理如下：

### official-link-candidate / repeated first-party

- GPT-Rosalind 和 Anthropic AI-enabled cyber threats 是 2026-06-04 已作为高信号处理的重复窗口；今天只在一手重点源、治理摘要和不确定性中保留，不重复升级。
- Steipete MS Build `BRK245` 是 OpenClaw / agentic-scale talk 候选；今天只有 direct-x + public session page 归档，缺少演讲正文逐字稿或 official product release，不升级为 Enterprise Delivery / OpenClaw 结论。

### matched-rss

- Wasmer/Codex 是 2026-06-04 已处理的 official customer story；今天只作为 first-party 重复窗口保留。
- Gemini Omni、Microsoft MAI models、datasette-agent-micropython、Lilian Weng 旧文、antirez 系列、lucumr 系列、minimaxir 旧文、geohot/Steve Blank/Keygen/SVPG/Ramp 多篇文章多为重复窗口、旧文、背景阅读、泛 product/infra 工程或弱相关 product-growth；保留 raw fulltext，但不进入今日高信号。
- Forward Deployed Episode 4/5/6 是 FDE/agent market 背景材料；今天 trend 只选 Endava 和 Ted Mabrey 作为更直接的 enterprise-delivery/FDE 边界证据。
- Pragmatic Engineer `Building OpenCode with Dax Raad` 与 Ramp/SVPG 文章可作为产品/工程背景，但今天没有比 OpenAI/Anthropic/GitHub/Claude Code 一手信号更强的新事实，不升级。

### top-direct-x

- Matt Pocock AI Coding Dictionary、Greg Isenberg agent-first Slack / Codex Sites、EXM7777 skills hygiene、Riley Brown building-blocks、zhaogua61654931 Codex thread/social-engineering 等已在 X/Twitter 覆盖说明、Memory/Usage Tactics 摘要或 trend report 中处理为 `direct-x` field notes；它们支持 playbook 候选，不是官方事实。
- Marc Lou UI/UX、Levelsio product/hotel/token-spend、Hesamation AI image / meme、OpenAI teaser retweets、Boeing/travel 等与今日高信号弱相关或无本地官方原文，不升级。
- OpenAI memory retweet 与 OpenAIDevs Showcase teaser 属于已覆盖官方信号或未展开 teaser；不重复写入高信号。

## 不确定性与待验证项

- GitHub REST API 本轮为 `skipped`，release 判断绑定 Atom fallback bodies；limited-body Codex alpha release 只记录版本线。
- OpenAI `Dreaming` 的 memory quality、freshness、review UX、地区 rollout 和 user controls 都来自 OpenAI 自述；需要实际产品验证和隐私/retention policy 查证。
- Endava/DavaFlow 是 OpenAI customer story；组织效果、delivery acceleration、AI fluency hiring/promotion 规则和 client outcomes 未独立审计。
- Anthropic recursive self-improvement 使用内部数据和员工引述；AI research judgment、human review bottleneck 与 future scenarios 需要结合 system card、external benchmarks 和 policy follow-up 验证。
- Claude Code `v2.1.163` 的 managed settings、hooks、MCP session id、background sessions、Windows/EDR/Bazel fixes 未本地复现。
- GitHub Trending README 只证明上榜和 README 可读；Copilot SDK、Spec Kit、Hermes Agent、Headroom、ECC、open-notebook 等涉及 auth、billing、permission handlers、memory storage、context proxy、remote terminal、skills/hooks 和 data ingestion，需要安装审计。
- Direct-x usage tactics 是 practitioner notes；可形成假设和 playbook 候选，但不能当作官方事实或市场 adoption 证据。

## 今日文档翻译

翻译阶段已完成：4 个 shard，27 个目标，27 个已翻译，0 个缺失/跳过。父 runner 初次 check 发现 1 个同源重复目标缺失（`enterprise-delivery-system/github__spec-kit.zh.md`），已从相同 `source_content_hash` 的 Spec Kit 译读稿补齐并修正原文归档链接；最终校验使用 `python3 scripts/translation-targets.py --date 2026-06-05 --check`，结果为 `ok=true`。

- 索引：[2026-06-05 中文译读索引](../translations/2026-06-05/index.md)
- Manifest：[manifest.json](../translations/2026-06-05/manifest.json)
- daily-high-signal：8 篇
  - [ChatGPT memory dreaming official blog](../translations/2026-06-05/daily-high-signal/openai-blog-dreaming-better-memory-for-a-more-helpful-chatgpt-58a72a3a66.opencli.zh.md)
  - [ChatGPT memory dreaming official-link candidate](../translations/2026-06-05/daily-high-signal/openai-2062567556524003631-chatgpt-memory-dreaming.opencli.zh.md)
  - [Endava / DavaFlow](../translations/2026-06-05/daily-high-signal/openai-blog-how-endava-is-redesigning-software-delivery-around-ai-agents-d0841d29a3.opencli.zh.md)
  - [Anthropic recursive self-improvement](../translations/2026-06-05/daily-high-signal/anthropicai-2062568862479208923-recursive-self-improvement.extracted.zh.md)
  - [OpenAI biodefense](../translations/2026-06-05/daily-high-signal/openai-blog-biodefense-in-the-intelligence-age-dbb39445d0.opencli.zh.md)
  - [Claude Code v2.1.163](../translations/2026-06-05/daily-high-signal/anthropics-claude-code-v2.1.163-d2176cb2c2.atom.zh.md)
  - [GitHub Copilot SDK](../translations/2026-06-05/daily-high-signal/github__copilot-sdk.zh.md)
  - [Spec Kit](../translations/2026-06-05/daily-high-signal/github__spec-kit.zh.md)
- 趋势分组：Memory & Dream 5 篇、AI Governance Legitimacy 3 篇、Enterprise Delivery System 3 篇、Codex & Claude Usage Tactics 3 篇、Forward Deployed Engineering 2 篇、Codex Feature Watch 2 篇、Claude Code Feature Watch 1 篇；完整链接见[译读索引](../translations/2026-06-05/index.md)。
