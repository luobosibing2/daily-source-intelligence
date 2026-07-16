# 2026-06-22 Daily Source Intelligence

## 采集范围

- 运行日期：2026-06-22，时区：Asia/Shanghai。
- 稳定来源：RSS/Atom 32 个 source 中 31 个 ok、1 个 failed；命中并尝试原文 43 条，其中 42 条 `ok`、1 条 `limited`、0 条 `failed`。GitHub releases 7 个 source 中 6 个 ok、1 个 failed；REST API 返回 403 rate limit 后按 runbook 降级到 Atom feed。GitHub release always-read 10 条，其中 4 条 fulltext `ok`、6 条 `limited`。GitHub Trending daily 1 个 source ok，解析 repo 10 个，README 10/10 归档。official pages 4 个 source ok，0 个 limited/failed。
- X/Twitter：`twitterapi.io` status 为 `partial`，27 个账号请求中 26 个 ok、1 个 failed；保留 86 条 direct-x tweet。official-link candidates 为 0 条。
- 原始产物：[rss-items.json](../raw/2026-06-22/rss-items.json)、[github-items.json](../raw/2026-06-22/github-items.json)、[github-trending.json](../raw/2026-06-22/github-trending.json)、[official-pages.json](../raw/2026-06-22/official-pages.json)、[twitterapi-io-results.json](../raw/2026-06-22/twitterapi-io-results.json)、[official-link-candidates.json](../raw/2026-06-22/official-link-candidates.json)。
- 状态产物：[manifest.json](../raw/2026-06-22/manifest.json)、[source-health.json](../state/source-health.json)、[seen.json](../state/seen.json)。
- 今日新增去重记录：37 条。

## 今日高信号

1. OpenAI 宣布 Samsung Electronics 向员工开放 ChatGPT 和 Codex。证据等级 `official-source`，fulltext `ok`；今天值得看是因为 Codex 被放进大型企业员工工作流，而不只是开发者个人工具，见 [OpenAI Samsung](../raw/2026-06-22/rss-fulltext/openai-blog/openai-blog-samsung-electronics-brings-chatgpt-and-codex-to-employees-eebdb7f63b.opencli.md)。
2. OpenAI 的企业用量分析和 spend controls 已读官方正文。证据等级 `official-source`，fulltext `ok`；它继续说明企业 AI 采用的关键瓶颈正在转向预算、用量可见性、管理员治理和 Cost API，见 [OpenAI spend controls](../raw/2026-06-22/rss-fulltext/openai-blog/openai-blog-new-usage-analytics-and-updated-spend-controls-for-enterprises-217d8a1a56.opencli.md)。
3. OpenAI 连续归档了健康问答、罕见病诊断和 AI chemist 三条科学/医疗任务材料。证据等级 `official-source`，fulltext 均 `ok`；这组信号说明模型产品正在进入高风险专家流程，但本日报只记录公开研究和产品方向，不复现实验，见 [health intelligence](../raw/2026-06-22/rss-fulltext/openai-blog/openai-blog-improving-health-intelligence-in-chatgpt-3338356751.opencli.md)、[rare diseases](../raw/2026-06-22/rss-fulltext/openai-blog/openai-blog-using-ai-to-help-physicians-diagnose-rare-genetic-diseases-affecting-c-2155d7cb8c.opencli.md)、[AI chemist](../raw/2026-06-22/rss-fulltext/openai-blog/openai-blog-a-near-autonomous-ai-chemist-improves-a-challenging-reaction-in-medici-1a8cd099cf.opencli.md)。
4. Claude Code `v2.1.183`、`v2.1.181`、`v2.1.179`、`v2.1.178` release body 可读，重点仍是 auto mode 安全、配置、本机权限、presence marker、nested skills 和后台/远程会话稳定性。证据等级 `official-source`，fulltext `ok`；`v2.1.185` 为 `limited`，不能推断新增功能，见 [v2.1.183](../raw/2026-06-22/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.183-caf72d232d.atom.md)。
5. `chopratejas/headroom`、`DeusData/codebase-memory-mcp`、`bytedance/deer-flow` 和 `mukul975/Anthropic-Cybersecurity-Skills` 同日进入 GitHub Trending，README 均已归档。证据等级 `secondary-source`；它们共同指向 agent 的上下文压缩、代码库记忆、长任务 harness 和技能库，但 Trending 只能作为 discovery signal。
6. Simon Willison 的 `Temporary Cloudflare Accounts for AI agents` 与 `sqlite-utils 4.0rc1` 已读 RSS 全文。证据等级 `secondary-source`，fulltext `ok`；前者命中 agent 临时账号/权限边界，后者是开发者工具链更新，见 [Cloudflare temporary accounts](../raw/2026-06-22/rss-fulltext/simonwillison/simonwillison-temporary-cloudflare-accounts-for-ai-agents-9feea51014.extracted.md)。
7. FDE/企业落地方向今天有 Ted Mabrey、Thomas Otter、Forward Deployed 和 FDEHub 的多条归档。证据等级多为 `secondary-source`，fulltext `ok`；值得看的是它们围绕 FDE 定义、企业 context layer、eval lifecycle 和 agent 市场机制继续收敛，但多为观点文章，不能当作客户部署事实。

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS：5 条 always-read 均 fulltext `ok`。今天的一手重点是 Samsung 企业部署、企业用量/成本治理、健康问答、罕见病诊断和 AI chemist；其中企业治理与科学/医疗任务最适合进入长期趋势观察。
- OpenAI Codex releases：`0.142.0-alpha.10` 到 `0.142.0-alpha.6` 均为 `limited`，release Atom 只有短标题；只记录版本出现，不从 alpha 版本号推断功能变化。
- Claude Code releases：`v2.1.183`、`v2.1.181`、`v2.1.179`、`v2.1.178` fulltext `ok`，`v2.1.185` 为 `limited`。今天仍以安全边界、配置入口、权限、本机集成、嵌套 skills 和会话稳定性为主。
- Official pages：OpenAI News 和 Claude docs release notes 页面已归档；Claude docs release notes 返回区域不可用提示。Claude Blog official page 发现 5 条新近文章标题，但本次 official page 结果没有可引用 fulltext path，因此日报不把这些标题升级成已读正文。

## 按主题分组摘要

### AI coding / agent runtime

- Claude Code release 的可读条目继续显示 coding agent 产品化重点：auto mode 需要阻断危险 git/infra 操作，`/config`、Apple Events opt-in、presence marker、nested skills 和子代理权限都在补运行时边界。
- OpenAI Codex alpha release body 今天仍为 `limited`，只能记录版本出现。direct-x 里有 Codex 额度、Swift 权限流实现、Codex/Claude Code 使用体验等 field notes，但都不是一手产品文档。
- `headroom` 把工具输出、日志、文件和 RAG chunks 送进 LLM 之前做压缩，README 声称支持 library、proxy 和 MCP server。它命中 agent context 成本问题，但压缩质量、可逆性和安全边界未本地验证。

### Memory / context / skills

- `codebase-memory-mcp` README 声称把代码库索引成持久知识图谱，供 coding agent 查询结构关系。它直接命中 memory/context 主题；今天只按 README discovery 记录，未验证索引正确性、语言覆盖和权限隔离。
- `deer-flow` README 把长任务 agent 描述为包含沙箱、记忆、工具、skills、subagents 和 message gateway 的 harness。它值得记录，因为它把长任务能力拆成运行时部件，但本日报没有安装或跑样例。
- `Anthropic-Cybersecurity-Skills` 是面向 AI agents 的安全技能库，README 标称映射多个安全框架。它说明“skills”正在从个人 productivity 扩展到专业域知识包；但技能质量、适配平台和安全使用边界待验证。

### Model / evaluation / infra

- Hugging Face 的 agentic benchmark 文章仍被归档为全文 `ok`，强调在自有工具上评测开放模型。它对本仓有价值的点是：agent 评测应绑定工具、权限、任务环境和业务接口，而不是只看聊天排行榜。
- `minimaxir` 的 Hy3 / Claude Haiku 4.5 / AI agent coding 文章、`Hesamation` 和 `mattpocockuk` 关于 GLM-5.2 的 direct-x 讨论，提供模型体验背景；但它们不是本地基准或官方能力报告。
- `sean-goedecke` 关于 AI GPU 生命周期、`xeiaso` 关于 cached input token 成本、Palantir Elasticsearch reindex 文章都属于 infra 背景；今天不升级为 agent 产品主结论。

### Enterprise delivery / FDE

- OpenAI Samsung 和 enterprise spend controls 是今天最强企业交付信号：前者说明大型企业员工级部署，后者说明管理员需要成本、用量、预算和组织分析。
- Ted Mabrey 的 `Sorry, that isn't an FDE`、Thomas Otter 的 context layers/FDE、FDEHub 的 eval lifecycle、Forward Deployed 的 agent 市场机制与 special forces model 都已归档。它们支持“FDE 正在被重新定义为企业 AI 最后一公里”的长期观察，但多为观点/框架文章。
- Ramp Builders 的 `We Tested Marketing Incentives to AI Agents` 已读全文，属于 agent-facing distribution 的实验线索；是否能推广到真实采购或用户行为仍待验证。

### Science / health / governance

- OpenAI 健康问答、罕见病诊断、AI chemist 三条一手材料共同说明模型正在进入专业任务，但都需要专家评估、数据边界和失败模式说明；日报不把它们写成临床可替代结论。
- Google DeepMind 的英国建房规划 AI 与 Gemini 3.5 Live Translate 被 RSS 归档；前者是公共事务应用背景，后者是多语言交互背景。今天仅做归档，不升级为本仓主线。
- direct-x 里有模型访问、公平性、开源模型和社会契约讨论，但缺少一手政策/监管材料，暂不写成 AI governance 新判断。

### Financial agents

- 今日没有新的 autonomous trading、portfolio、AML、credit decisioning、Treasury 或 human sign-off financial-agent workflow 一手证据。
- `ZhuLinsen/daily_stock_analysis` 在 GitHub Trending 出现，README 是 LLM 驱动的多市场股票分析系统，含行情、新闻、看板和自动推送。它是 financial-agent discovery candidate；涉及投资/交易风险，不能把 README claim 写成可用投资建议。

### Indie / product growth

- `marclou`、`jackfriks`、`levelsio`、`cellinlab` 等 direct-x 中有独立产品、收入、增长和 AI 工具使用 field notes，但多数是个人叙事或产品小更新，不升级成 adoption metrics。
- `palmier-pro` 和 `OpenMontage` 延续 AI 视频生产方向：前者是 macOS Apple Silicon 视频编辑器，强调人在时间线里和 agent 一起生成/编辑视频；后者是 agentic video production system，README 提到 pipelines、providers 和 agent guide。二者均需验证安装门槛、版权、成本和输出可控性。
- Penpot、Turso、World Monitor 等 Trending 项目对设计协作、数据库和情报 dashboard 有背景价值，但与本仓 agent 主线的直接关系弱于 memory/context 和视频生产候选。

### GitHub Trending discovery

GitHub Trending 今日解析到 10 个 repo，Trending description 覆盖 10/10，README 归档 10/10 成功，来源边界是 `secondary-source` discovery signal。

- `palmier-io/palmier-pro` 是 Apple Silicon macOS 视频编辑器，强调人和 agent 在时间线里协同生成与编辑视频。今天值得记录是创意软件正在把 agent 放进专业编辑界面；风险是 macOS 26 门槛、素材版权和输出质量未验证。
- `calesthio/OpenMontage` 是开源 agentic video production system，README 提到 12 条 pipelines、52 个工具、500+ agent skills、providers 和 agent guide。它适合作为视频生产自动化候选，需验证 provider 成本、素材输入、可控性和版权边界。
- `chopratejas/headroom` 是 AI agent context compression layer，目标是在工具输出、日志、文件和 RAG chunks 进入 LLM 前减少 token。它命中长任务成本和上下文卫生，但压缩后答案质量未验证。
- `tursodatabase/turso` 是兼容 SQLite 的 in-process SQL database。它是 infra discovery，今天不直接更新 agent 趋势。
- `penpot/penpot` 是开源设计与代码协作工具。它对设计协作有背景价值，但今日没有 agent-specific 证据。
- `ZhuLinsen/daily_stock_analysis` 是 LLM 驱动的股票分析系统，涉及行情、新闻、看板、自动推送和定时运行。它是 financial-agent discovery candidate，投资风险和数据源可靠性必须待验证。
- `koala73/worldmonitor` 是实时全球情报 dashboard，聚合新闻、地缘政治和基础设施监控。它可能对情报工作流有启发，但 README discovery 不能证明数据源质量或误报控制。
- `bytedance/deer-flow` 是长任务 SuperAgent harness，README 提到 sandboxes、memories、tools、skill、subagents 和 message gateway。它命中 agent runtime，但本日报没有安装验证。
- `DeusData/codebase-memory-mcp` 是代码智能 MCP server，目标是把代码库索引成持久知识图谱。它命中 coding agent memory，但性能、索引正确性和安全边界未验证。
- `mukul975/Anthropic-Cybersecurity-Skills` 是 AI agents 用的网络安全 skills 集合，映射多个安全框架。它是专业技能库 discovery，不能替代安全专家审查。

## 来源证据表

| 信号 | 证据等级 | 本地归档 | 边界 |
| --- | --- | --- | --- |
| Samsung employees use ChatGPT and Codex | official-source | [OpenAI Samsung](../raw/2026-06-22/rss-fulltext/openai-blog/openai-blog-samsung-electronics-brings-chatgpt-and-codex-to-employees-eebdb7f63b.opencli.md) | 已读官方正文；未验证企业内部实际使用规模。 |
| Enterprise usage analytics / spend controls | official-source | [OpenAI spend controls](../raw/2026-06-22/rss-fulltext/openai-blog/openai-blog-new-usage-analytics-and-updated-spend-controls-for-enterprises-217d8a1a56.opencli.md) | 已读官方正文；未验证 Global Admin Console 和 Cost API。 |
| OpenAI health / rare disease / AI chemist | official-source | [health](../raw/2026-06-22/rss-fulltext/openai-blog/openai-blog-improving-health-intelligence-in-chatgpt-3338356751.opencli.md) | 官方研究/产品材料；未复现实验或临床结论。 |
| Claude Code release body | official-source | [v2.1.183](../raw/2026-06-22/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.183-caf72d232d.atom.md) | 部分版本可读；`v2.1.185` limited。 |
| Temporary Cloudflare Accounts for AI agents | secondary-source | [Simon Willison](../raw/2026-06-22/rss-fulltext/simonwillison/simonwillison-temporary-cloudflare-accounts-for-ai-agents-9feea51014.extracted.md) | 已读博客；未验证 Cloudflare 产品细节。 |
| FDE / enterprise context layer / eval lifecycle | secondary-source | [Ted Mabrey](../raw/2026-06-22/rss-fulltext/ted-mabrey/ted-mabrey-sorry-that-isn-t-an-fde-9f296bf65a.opencli.md) | 多为观点文章；不能当作客户部署事实。 |
| GitHub Trending memory/context/video candidates | secondary-source | [github-trending.json](../raw/2026-06-22/github-trending.json) | README discovery；未安装、跑样例或验证 claim。 |

## X/Twitter 覆盖说明

`twitterapi.io` status 为 `partial`，27 个账号中 `corbin_braun` failed，其余账号请求完成；共保留 86 条窗口内 tweet。高相关 direct-x 主要包括 `mattpocockuk` 关于 harness/eval 和模型上下文体验的观点、`simonw` 的 sqlite-utils 发布、`Hesamation` / `gregisenberg` / `EXM7777` 关于 GLM-5.2 与 agent coding 的 field notes、`steipete` 对 Codex 权限流和使用体验的转发、`oviswang` 关于 Agent 能力开放到 SDK 的产品叙事，以及若干中文 Codex 生图/无限画布实践线索。所有直接来自 API 的 tweet 按 `direct-x` 处理；由于 official-link candidates 为 0，本日报没有把 direct-x 链接升级为官方正文证据。

## Candidate audit 处理记录

[candidate-audit](../reviews/2026-06-22-candidate-audit.md) 已生成：`covered=7`、`missed=46`。处理如下：

- matched-rss：OpenAI Samsung、enterprise spend controls、健康问答、罕见病诊断、AI chemist、Simon Willison 的 temporary Cloudflare accounts、Ted Mabrey 的 FDE 定义文章已被 audit 判定 covered。
- Google DeepMind 建房规划和 Gemini Live Translate、Hugging Face agentic benchmark、Simon Willison sqlite-utils、Lilian Weng、Sean Goedecke、Xe Iaso、lucumr、minimaxir、geohot、Steve Blank、Keygen、FDEHub、Forward Deployed、SVPG、Ramp、Palantir、Thomas Otter 等被标为 missed 的 RSS 条目，多数已在主题摘要中按背景/弱相关/观点材料降级处理；它们保留归档，不全部升级为“今日高信号”。
- Datasette Apps fulltext 为 `limited`，已在“不确定性与待验证项”中保留边界。
- top-direct-x：Codex 使用体验、GLM-5.2、agent coding、indie field notes、private equity 类比等均属于 direct-x field notes 或个人叙事；本日报只在 X/Twitter 覆盖说明中概括，不把它们写成官方发布、模型基准或 adoption metrics。

## 不确定性与待验证项

- RSS source `antirez` failed；这不代表该源今日没有更新。
- GitHub REST API 返回 403 rate limit，已降级到 Atom feed；`modelcontextprotocol-servers` release source failed。
- `simonwillison` 的 Datasette Apps RSS 命中项 fulltext 为 `limited`，不能写成已读原文。
- OpenAI Codex `0.142.0-alpha.10` 到 `0.142.0-alpha.6` release body 为 `limited`，不能从版本号推断功能。
- Claude Code `v2.1.185` release body 为 `limited`；只记录版本出现。
- `twitterapi.io` 对 `corbin_braun` failed；这不代表该账号没有更新。
- official-link candidates 为 0；今日 direct-x 未升级成官方正文证据。
- GitHub Trending README 是 discovery signal；`headroom`、`codebase-memory-mcp`、`deer-flow`、`Anthropic-Cybersecurity-Skills`、`Palmier Pro`、`OpenMontage`、`daily_stock_analysis` 等都需要安装、权限、安全、成本和运行行为验证。

## 运行统计

- 新增条目：`seen_added=37`。
- 高信号条目：7 条。
- 失败/受限来源：RSS source `antirez` failed；GitHub REST API 403 后 Atom fallback；GitHub release source `modelcontextprotocol-servers` failed；RSS fulltext 1 条 `limited`；GitHub release always-read 6 条 `limited`；twitterapi.io `corbin_braun` failed。
- official-link candidates：0 条。
- candidate audit：[reviews/2026-06-22-candidate-audit.md](../reviews/2026-06-22-candidate-audit.md)，`covered=7`、`missed=46`，missed 已按弱相关/同组背景/direct-x field note 处理。

## 完成审计

- 日报已写入：[docs/2026-06-22-daily-intel.md](2026-06-22-daily-intel.md)。
- candidate audit 已写入：[reviews/2026-06-22-candidate-audit.md](../reviews/2026-06-22-candidate-audit.md)；missed 候选已解释或降级为背景。
- trend report 已写入：[trend/reports/2026-06-22-trend-report.md](../trend/reports/2026-06-22-trend-report.md)，并通过 `python3 scripts/run-trend-stage.py --date 2026-06-22 --check`。
- enabled trends 已检查：7 个 trend 写入 `manifest.json`，`codex-feature-watch` 写入 [no-new-signal.json](../trend/raw/2026-06-22/codex-feature-watch/no-new-signal.json)。
- 专题报告已更新或记录无新增：[memory-dream](../trend/memory-dream.md)、[financial-agents](../trend/financial-agents.md)、[forward-deployed-engineering](../trend/forward-deployed-engineering.md)、[enterprise-delivery-system](../trend/enterprise-delivery-system.md)、[codex-feature-watch](../trend/codex-feature-watch.md)、[ai-governance-legitimacy](../trend/ai-governance-legitimacy.md)、[claude-code-feature-watch](../trend/claude-code-feature-watch.md)、[codex-claude-usage-tactics](../trend/codex-claude-usage-tactics.md)。
