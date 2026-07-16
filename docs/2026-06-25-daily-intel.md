# 2026-06-25 Daily Source Intelligence

## 采集范围

- 运行日期：2026-06-25，时区：Asia/Shanghai。
- 稳定来源：RSS/Atom 32 个 source 中 31 个 ok、1 个 failed；命中并尝试原文 50 条，50 条 `ok`、0 条 `limited`、0 条 `failed`。GitHub releases 7 个 source 均通过 Atom feed ok；GitHub REST API 本轮 `skipped`，按脚本策略使用 Atom feed。GitHub release always-read 10 条，其中 3 条 fulltext `ok`、7 条 `limited`。GitHub Trending daily 1 个 source ok，解析 repo 10 个，README 10/10 归档。official pages 4 个 source ok，0 个 limited/failed。
- X/Twitter：`twitterapi.io` status 为 `ok`，27 个账号请求完成；保留 132 条 direct-x tweet。official-link candidates 为 3 条，3 条 fulltext `ok`。
- 原始产物：[rss-items.json](../raw/2026-06-25/rss-items.json)、[github-items.json](../raw/2026-06-25/github-items.json)、[github-trending.json](../raw/2026-06-25/github-trending.json)、[official-pages.json](../raw/2026-06-25/official-pages.json)、[twitterapi-io-results.json](../raw/2026-06-25/twitterapi-io-results.json)、[official-link-candidates.json](../raw/2026-06-25/official-link-candidates.json)。
- 状态产物：[manifest.json](../raw/2026-06-25/manifest.json)、[source-health.json](../state/source-health.json)、[seen.json](../state/seen.json)。
- 今日新增去重记录：49 条。

## 今日高信号

1. OpenAI 与 Broadcom 发布 Jalapeño 推理芯片。证据等级 `official-source` + `direct-x`，fulltext `ok`；它把 OpenAI 的全栈叙事从模型、产品、API、Codex 扩展到芯片、网络、调度和数据中心部署，见 [OpenAI and Broadcom unveil LLM-optimized inference chip](../raw/2026-06-25/rss-fulltext/openai-blog/openai-blog-openai-and-broadcom-unveil-llm-optimized-inference-chip-1a015f5dfa.opencli.md)。
2. Google DeepMind 把 computer use 内置进 Gemini 3.5 Flash。证据等级 `official-source`，fulltext `ok`；重点不是单独 demo，而是浏览器、移动端、桌面环境的可视化操作能力进入主力 Flash 模型，并配套企业确认与 prompt injection 防护，见 [Introducing computer use in Gemini 3.5 Flash](../raw/2026-06-25/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-computer-use-in-gemini-3.5-flash-0ce8c6adc2.extracted.md)。
3. Claude Blog 页面发现 `Building effective human-agent teams` 与 `Agent identity in Claude Tag`。证据等级 `official-source` discovery + `direct-x`；官方页面只保存列表 metadata，Karpathy、AnthropicAI、Greg Isenberg 等 direct-x 强化了“agent 作为团队成员和组织账号”的方向，但单篇正文未归档前不能写成完整机制结论，见 [official-pages.json](../raw/2026-06-25/official-pages.json)。
4. Claude Code `v2.1.191` release body 可读。证据等级 `official-source`，fulltext `ok`；新增 `/rewind` 支持、background agents 停止后不再复活、MCP capability discovery 和 OAuth transient retry、sandbox 网络权限会话内记忆、managed settings 强制刷新，以及流式响应 CPU 和长会话内存增长优化，见 [v2.1.191](../raw/2026-06-25/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.191-046437509e.atom.md)。
5. OpenAI 宣布 GPT-5.5 Instant 新版本。证据等级 `direct-x`；这是模型体验更新线索，来自 OpenAI X 账号，今天没有对应官方正文归档，所以只能按 direct-x 记录为待官方页确认的产品信号，见 [twitterapi-io-results.json](../raw/2026-06-25/twitterapi-io-results.json)。
6. Matt Pocock 连续讨论 agent skill 的 no-op、手写质量和技能膨胀。证据等级 `direct-x`；这是可操作的方法论信号，指向 skill 文档需要可测、少废话、少 token 消耗，但仍是个人观点，不是平台发布。
7. GitHub Trending 出现 `stablyai/orca`、`google-labs-code/design.md`、`interviewstreet/hiring-agent`、`JCodesMore/ai-website-cloner-template` 和 `revfactory/harness`。证据等级 `secondary-source`；README 均已归档，说明 agent 编排、设计系统上下文、招聘评分、网站复刻和技能生成继续被包装成可直接使用的 repo，但本日报没有安装验证。
8. `ZhuLinsen/daily_stock_analysis` 继续上榜。证据等级 `secondary-source`；README 描述多市场行情、新闻、决策看板、内置策略、推送和部署形态，命中 financial-agent 候选，但涉及投资分析，不能写成收益、交易或投资建议。
9. `cnyzgkc` 的 PPT skill tweet 抽取到两个 GitHub official-link candidates。证据等级 `direct-x` + repo fulltext `ok`；这是 Codex/Claude 生态里把演示文稿生产沉淀成 skill 的实践线索，见 [guizang-ppt-skill](../raw/2026-06-25/official-link-candidates/cnyzgkc-2069444827427778960-guizang-ppt-skill.extracted.md) 与 [frontend-slides](../raw/2026-06-25/official-link-candidates/cnyzgkc-2069444827427778960-frontend-slides.extracted.md)。

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS：5 条 always-read 均 fulltext `ok`。今日新增最强信号是 Jalapeño 推理芯片；advanced AI shared standards、GPT-5 immunology mystery、Omio conversational travel 和 Daybreak 继续作为治理、科学协作、企业落地和安全工作流背景。
- OpenAI Codex releases：`rust-v0.143.0-alpha.16`、`0.143.0-alpha.15`、`0.143.0-alpha.14`、`0.143.0-alpha.13`、`0.143.0-alpha.12` 均为 `limited`，release Atom 只有短标题；只记录版本出现，不从 alpha 版本号推断功能变化。
- Claude Code releases：`v2.1.191`、`v2.1.187`、`v2.1.186` fulltext `ok`，`v2.1.190` 与 `v2.1.185` 为 `limited`。今日最强一手新增是 `v2.1.191` 的 `/rewind`、background agents、MCP retry、sandbox 网络权限和长会话性能修复。
- Official pages：OpenAI News、Anthropic News、Claude docs release notes、Claude Blog 均为 ok。Claude Blog 列表发现 human-agent teams、Claude Tag agent identity、Claude Desktop on cloud providers、Claude Code steering 和 MCP managed auth；本轮没有单篇正文归档，日报只把它们作为 official-page discovery。

## 按主题分组摘要

### AI coding / agent runtime

- Gemini 3.5 Flash 的 computer use 把可视化操作能力从专用模型变成主力模型内置工具，面向长任务、企业自动化、软件测试和专业应用操作；它同时把敏感动作确认、间接 prompt injection 自动停止、沙箱、人类复核和访问控制放在同一安全框架里。
- Claude Code `v2.1.191` 的改动集中在长会话和企业控制面：`/rewind` 补救误清空、background agents 停止语义、MCP discovery/OAuth retry、headless OAuth、managed settings 刷新、sandbox 网络许可会话记忆、CPU 和内存增长优化。这些不是单一大功能，但都是 runtime 产品化信号。
- Simon Willison 记录 `browser-compat-db`：用 Claude Code for web 生成脚本、用 Codex Desktop 构建 GitHub Actions，把 MDN browser compatibility data 转成 SQLite 并通过 GitHub CDN 暴露给 Datasette Lite。它是 AI coding 进入小型数据产品流水线的可读 field note，见 [browser-compat-db](../raw/2026-06-25/rss-fulltext/simonwillison/simonwillison-simonw-browser-compat-db-ff39842eb3.extracted.md)。

### Memory / context / skills

- Claude Tag 相关 direct-x 把 agent 描述成有组织上下文、工具、记忆、权限和异步持续性的“团队成员”。这对 memory/context 的意义很强，但官方正文未归档，今天只写为待验证方向。
- Matt Pocock 的 skill no-op 讨论、`/loop-me` 设想、手写 skill 质量判断和“哪些 AI coding 资产不该进 git”的问题，说明 skill 从“能写”进入“要能评估、维护、删废话”的阶段。证据是 direct-x，不升级为平台事实。
- GitHub Trending 的 `revfactory/harness` 与 `google-labs-code/design.md` 分别把 agent team/skills 生成和设计系统上下文格式化；二者 README 已读，说明 agent 上下文正在从自由提示转向可分发工件。

### Security / governance / public legitimacy

- OpenAI Jalapeño 文章强调推理成本、可靠性、访问扩大、数据中心伙伴和多代平台；它本质上是算力治理与供应链自主权信号，而不只是硬件新闻。
- Gemini computer use 明确把 prompt injection、防御分层、敏感动作确认和企业权限控制写进发布叙事。这是 agent 可操作外部环境后必须补齐的治理层。
- Simon Willison 的 Claude Code for web egress policy direct-x 是小但有边界价值的运行时限制线索：远程 agent 的网络策略会直接影响常见开发提示词，但今天只来自个人反馈，需等平台状态或官方说明。

### Enterprise delivery / FDE

- Claude Tag discovery 与 Karpathy/Greg Isenberg 的 direct-x 都把 agent 放到 Slack、账号、团队协作和责任边界里；这正命中企业交付系统的组织吸收问题。但缺单篇官方正文，因此只能写“方向成立、机制待读”。
- Google DeepMind 的 computer use 发布面向企业自动化和专业应用操作，说明厂商在把 agent 从开发者 demo 推向可管控工作流：确认、停止、沙箱、复核和访问控制成为交付前置条件。
- FDEHub、Forward Deployed、SVPG、Ted Mabrey、Thomas Otter 等 RSS 原文继续支持“从 proof-of-concept 到生产部署”的长期观察；今天没有把这些背景材料单独升级成主高信号。

### Model / evaluation / infra

- Jalapeño 的关键不在“OpenAI 有芯片”这个标题，而在软件-硬件联合设计：面向 ChatGPT、Codex、API 和未来 agent 产品的推理需求，减少数据移动、平衡计算/内存/网络资源，并声称九个月 tape-out。性能报告尚未发布，不能写成已验证 benchmark。
- Antirez 的 AI QA/testing、edit tool 替代、分布式推理文章都已读原文；它们继续支持“agent 不只是写代码，也能做更宽的 QA 和系统实验”的背景判断，见 [A new era for software testing](../raw/2026-06-25/rss-fulltext/antirez/antirez-a-new-era-for-software-testing-81001b41cc.opencli.md)。
- Hugging Face FFASR leaderboard、Lilian Weng hallucination/human data、Sean Goedecke GPU lifespan、Minimaxir agent coding/Hy3 等均有归档或命中，但今天不把它们合并成单一模型结论。

### Financial agents

- `ZhuLinsen/daily_stock_analysis` 是今日最明确的 financial-agent discovery：README 描述行情、新闻、评分、买卖点位、风险警报、推送、Web/API/Bot 和多种部署方式。边界是它来自 Trending + README，未验证数据质量、回测、合规、人类审批和风险提示是否足够。
- direct-x 里有市场、投资和创业收入讨论，但缺少金融机构、审计、人类审批或合规 workflow 证据，暂不升级为 financial-agent 主判断。

### Indie / product growth

- `OpenMontage`、`Genspark Design` direct-x、`ai-website-cloner-template` 和 PPT skills 都指向“AI 把设计、网站、视频和演示文稿变成可自动化生产线”。今天只记录形态，不验证输出质量、版权、素材来源和商业可用性。
- `marclou` 的 DataFast onboarding flow、`jackfriks` 的 remote-control mobile web app field note、`cellinlab` 的 Codex 插件/Skill/Loop 讨论都可读，但多数仍是个人实践记录，不写成 adoption metrics。

### GitHub Trending discovery

GitHub Trending 今日解析到 10 个 repo，Trending description 覆盖 10/10，README 归档 10/10 成功，来源边界是 `secondary-source` discovery signal。

- `calesthio/OpenMontage` 是开源 agentic video production system，README 说它把 coding assistant 变成视频生产 studio，可处理研究、脚本、素材生成、剪辑和合成。它解决的是视频生产流程自动化问题；今天值得记录是创意生产开始复用 coding-agent pipeline，但素材版权、成本、质量和 provider 依赖待验证。
- `ZhuLinsen/daily_stock_analysis` 是 LLM 驱动的多市场股票分析系统，覆盖行情、新闻、决策看板、策略问答和自动推送。它命中 financial-agent 候选，但 README discovery 不能证明投资收益或交易可靠性。
- `apple/container` 是 Apple Silicon Mac 上用轻量虚拟机运行 Linux containers 的 Swift 工具，支持 OCI 镜像。它对本仓关注的 agent 运行环境有间接基础设施价值，但不是 AI agent 专用发布。
- `interviewstreet/hiring-agent` 是简历到评分的 agent pipeline：PDF 转 Markdown、LLM 抽取结构化 JSON、补充 GitHub 信号、输出可解释评分。它涉及招聘决策，必须额外验证公平性、偏见、隐私和人工审核边界。
- `JCodesMore/ai-website-cloner-template` 是用 AI coding agents 复刻网站的 Next.js 模板。它面向设计还原和前端生成，但可能涉及版权、商标、站点资产授权和过度复刻风险。
- `revfactory/harness` 是 Claude Code 的 team-architecture factory，按项目描述生成 agent team 与 skills。它命中多 agent 编排和 skills 生成主线，但 README claim 需要实际项目运行验证。
- `flutter/flutter` 是 Flutter 主仓今日上榜，README 是成熟 SDK 基础介绍。它不是本轮 AI 高信号，只作为 Trending 覆盖记录。
- `andreknieriem/headunit-revived` 是 Android Auto headunit app。它与本仓关注方向弱相关，只保留为 Trending 覆盖记录。
- `stablyai/orca` 是并行 agent 桌面/移动编排工具，README 说可在隔离 worktree 中并行运行 Codex、Claude Code、OpenCode 等，并提供手机监控、终端分屏、设计模式、GitHub/Linear 入口。它命中 agent orchestrator 主线，但未安装验证。
- `google-labs-code/design.md` 是给 coding agents 的视觉身份描述规范，结合 YAML tokens 与 Markdown 设计理由，并提供校验/对比。它解决的是 agent 生成 UI 时的长期设计上下文一致性问题，今天值得记录为“设计系统也在变成 agent-readable context”。

## 来源证据表

| 信号 | 证据等级 | 本地归档 | 边界 |
| --- | --- | --- | --- |
| OpenAI Jalapeño 推理芯片 | official-source + direct-x | [OpenAI Jalapeño](../raw/2026-06-25/rss-fulltext/openai-blog/openai-blog-openai-and-broadcom-unveil-llm-optimized-inference-chip-1a015f5dfa.opencli.md) | 已读官方正文；性能报告尚未发布。 |
| Gemini 3.5 Flash computer use | official-source | [Gemini computer use](../raw/2026-06-25/rss-fulltext/google-deepmind-blog/google-deepmind-blog-introducing-computer-use-in-gemini-3.5-flash-0ce8c6adc2.extracted.md) | 已读官方正文；未调用 Gemini API 复现。 |
| Claude Code v2.1.191 | official-source | [v2.1.191](../raw/2026-06-25/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.191-046437509e.atom.md) | release body 已读；未本地运行 Claude Code。 |
| Claude Tag / human-agent teams | official-source discovery + direct-x | [official-pages](../raw/2026-06-25/official-pages.json) | 只有列表 metadata 与 direct-x 扩散，缺单篇正文。 |
| GPT-5.5 Instant 更新 | direct-x | [twitterapi.io](../raw/2026-06-25/twitterapi-io-results.json) | 来自 OpenAI X；缺官方正文归档。 |
| Skill no-op / skill hell | direct-x | [twitterapi.io](../raw/2026-06-25/twitterapi-io-results.json) | 个人方法论观点；非平台发布。 |
| PPT skills GitHub candidates | direct-x + repo fulltext | [guizang-ppt-skill](../raw/2026-06-25/official-link-candidates/cnyzgkc-2069444827427778960-guizang-ppt-skill.extracted.md) | 使用体验来自 direct-x；未复现生成质量。 |
| GitHub Trending agent repos | secondary-source | [Orca](../raw/2026-06-25/github-trending-readmes/stablyai__orca.md) | README discovery；未安装验证。 |
| Financial-agent candidate | secondary-source | [daily_stock_analysis](../raw/2026-06-25/github-trending-readmes/ZhuLinsen__daily_stock_analysis.md) | README discovery；不构成投资建议。 |

## X/Twitter 覆盖说明

`twitterapi.io` status 为 `ok`，27 个账号请求完成，共保留 132 条窗口内 tweet。高相关 direct-x 包括 OpenAI 对 Jalapeño、GPT-5.5 Instant、DevDay 2026 的发布扩散，AnthropicAI/Claude 相关账号对 Claude Tag 的扩散，Karpathy 对“持久、异步、带组织工具和上下文的团队 agent”的评价，Matt Pocock 对 skills no-op 和 skill 维护性的讨论，Simon Willison 对 Claude Code for web egress policy 的反馈，Genspark 的 design/productivity 发布扩散，以及中文圈关于 Codex 插件、Doubao 接入 Codex、PPT skills、Codex Loop 的实践线索。所有直接来自 API 的 tweet 按 `direct-x` 处理；其中 3 条 official-link candidates 已抓取正文。

## Candidate audit 处理记录

[candidate-audit](../reviews/2026-06-25-candidate-audit.md) 已生成：`covered=6`、`missed=57`。处理如下：

- covered：OpenAI Jalapeño、Gemini 3.5 Flash computer use、Simon Willison `browser-compat-db`、Antirez AI testing、`guizang-ppt-skill` 和 `frontend-slides` 已被 audit 判定 covered。
- official-link-candidate missed：OpenAI DevDay 2026 application page 被 audit 判定 missed，但日报已在采集范围、X/Twitter 覆盖说明和运行统计中记录，今天未放入“今日高信号”的原因是它延续昨日已覆盖的日程/申请窗口信号，非今日新增产品或机制变化。
- matched-rss missed：OpenAI advanced standards、GPT-5 immunology、Omio、Daybreak 均为一手重点源背景，已在“一手重点源”中处理；Google UK planning、Hugging Face FFASR、Lilian Weng、Sean Goedecke、Xe Iaso、Lucumr、Minimaxir、Geohot、Steve Blank、Keygen、Palantir、Ramp、FDEHub、Forward Deployed、SVPG、Ted Mabrey、Thomas Otter 等已在模型/infra、企业交付/FDE、security 或不确定性中按背景材料处理，没有逐条放入“今日高信号”的原因是它们多数为长期背景、方法论材料、旧文重现或同一主题组内的支撑材料。
- top-direct-x missed：OpenAI Jalapeño 已通过 official-source 升级；Karpathy、Greg Isenberg、AnthropicAI、frxiaobei 的 Claude Tag 扩散已在高信号和 X/Twitter 覆盖说明中作为 direct-x + official-page discovery 处理；Matt Pocock skill no-op 已在高信号处理；Riley Brown/Genspark 设计工具、levelsio 空调/个人生活、marclou/jackfriks/cellinlab 等保留为 field notes，不写成官方发布、企业采用或模型能力事实。

## 不确定性与待验证项

- RSS failed sources：`dwarkesh-patel` 返回 `curl: (52) Empty reply from server`；这不是“无更新”，只是本轮抓取失败。
- OpenAI Codex `0.143.0-alpha.16` 到 `0.143.0-alpha.12` release body 为 `limited`，不能从版本号推断功能变化。
- Claude Code `v2.1.190` 与 `v2.1.185` release body 为 `limited`；今日可读 release 主体以 `v2.1.191`、`v2.1.187`、`v2.1.186` 为准。
- Claude Blog `Building effective human-agent teams`、`Agent identity in Claude Tag`、Claude Desktop 云供应商体验、Claude Code steering、MCP managed auth 等只在 official page 列表中出现，缺单篇正文归档；后续最小验证路径是抓取对应 blog fulltext 后再写机制判断。
- OpenAI DevDay 2026 application page 今天仍作为 official-link candidate 出现，但已在 2026-06-24 日报作为高信号处理；本日报不把重复日程线索升级为新的产品判断。
- GitHub Trending 是 discovery signal；`Orca`、`design.md`、`hiring-agent`、`ai-website-cloner-template`、`OpenMontage`、`daily_stock_analysis`、`revfactory/harness` 都需要安装、权限、安全、成本和运行行为验证。
- direct-x field notes 不能替代官方发布、模型基准或企业采用数据；GPT-5.5 Instant 今天只有 OpenAI X 证据，需等官方页面、release note 或 API 文档补证。
- `hiring-agent` 与 `daily_stock_analysis` 分别涉及招聘评价和投资分析，不能只凭 README 接受公平性、合规性或建议质量。

## 运行统计

- 新增条目：`seen_added=49`。
- 高信号条目：9 条。
- 失败/受限来源：RSS 1 failed（`dwarkesh-patel`）；official pages 0 failed；twitterapi.io 0 failed；GitHub REST API `skipped` 后使用 Atom；GitHub release always-read 7 条 `limited`，包括 OpenAI Codex 5 条 alpha release 与 Claude Code `v2.1.190`、`v2.1.185`。
- official-link candidates：3 条，OpenAI DevDay、`op7418/guizang-ppt-skill`、`zarazhangrui/frontend-slides` 均 fulltext `ok`。

## 完成审计

- 日报已写入：[docs/2026-06-25-daily-intel.md](2026-06-25-daily-intel.md)。
- candidate audit 已写入：[reviews/2026-06-25-candidate-audit.md](../reviews/2026-06-25-candidate-audit.md)；`covered=6`、`missed=57`，missed 已按重复官方候选、同组背景、弱相关或 direct-x field note 处理。
- trend raw marker 已写入：[trend/raw/2026-06-25/](../trend/raw/2026-06-25/)；9 个 enabled trend 均有 `manifest.json`，无 `no-new-signal` marker。
- trend Phase 1 已完成：`python3 scripts/run-trend-stage.py --date 2026-06-25 --phase phase1` 返回 `candidate_count=20`。
- trend Phase 2 未完成：`python3 scripts/run-trend-stage.py --date 2026-06-25 --phase phase2` 在 `ai-governance-legitimacy` 的 topic consolidator 子进程失败；`codex exec` 访问 `https://chatgpt.com/backend-api/codex/responses` 返回 `403 Forbidden`。
- trend report 未写入：[trend/reports/2026-06-25-trend-report.md](../trend/reports/2026-06-25-trend-report.md) 不存在。
- 专题报告未更新到 2026-06-25 claim：Phase 2 失败后，SQLite 中当天 20 个 candidates 已提升为 claim，但各 `trend/*.md` 还没有写入对应正文和状态索引。
- trend check 未通过：`python3 scripts/run-trend-stage.py --date 2026-06-25 --check` 返回 `ok=false`；主要错误是缺 daily trend report，以及当天 claims 未写入各专题正文/状态索引。
