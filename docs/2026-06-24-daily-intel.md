# 2026-06-24 Daily Source Intelligence

## 采集范围

- 运行日期：2026-06-24，时区：Asia/Shanghai。
- 稳定来源：RSS/Atom 32 个 source 全部 ok；命中并尝试原文 49 条，49 条 `ok`、0 条 `limited`、0 条 `failed`。GitHub releases 7 个 source 均通过 Atom feed ok；GitHub REST API 本轮 failed/rate-limited，按脚本策略降级使用 Atom feed。GitHub release always-read 10 条，其中 4 条 fulltext `ok`、6 条 `limited`。GitHub Trending daily 1 个 source ok，解析 repo 10 个，README 10/10 归档。official pages 4 个 source ok，0 个 limited/failed。
- X/Twitter：`twitterapi.io` status 为 `ok`，27 个账号请求全部 ok；保留 123 条 direct-x tweet。official-link candidates 为 4 条，4 条 fulltext `ok`。
- 原始产物：[rss-items.json](../raw/2026-06-24/rss-items.json)、[github-items.json](../raw/2026-06-24/github-items.json)、[github-trending.json](../raw/2026-06-24/github-trending.json)、[official-pages.json](../raw/2026-06-24/official-pages.json)、[twitterapi-io-results.json](../raw/2026-06-24/twitterapi-io-results.json)、[official-link-candidates.json](../raw/2026-06-24/official-link-candidates.json)。
- 状态产物：[manifest.json](../raw/2026-06-24/manifest.json)、[source-health.json](../state/source-health.json)、[seen.json](../state/seen.json)。
- 今日新增去重记录：30 条。

## 今日高信号

1. OpenAI 发布 advanced AI shared standards 文章，把强模型的网络安全、科学发现、政府可见性、第三方评估和 Appia Foundation 放进同一套安全标准叙事。证据等级 `official-source`，fulltext `ok`；值得看是因为它把能力释放和外部标准建设绑定，见 [Helping build shared standards for advanced AI](../raw/2026-06-24/rss-fulltext/openai-blog/openai-blog-helping-build-shared-standards-for-advanced-ai-6507bbb397.opencli.md)。
2. OpenAI 记录 GPT-5 Pro 帮助免疫学团队重审三年难题。证据等级 `official-source`，fulltext `ok`；它不是 agent runtime 发布，但强化了“模型作为专业研究协作者”的官方案例线，见 [GPT-5 immunology mystery](../raw/2026-06-24/rss-fulltext/openai-blog/openai-blog-how-gpt-5-helped-immunologist-derya-unutmaz-solve-a-3-year-old-mystery-7c36fb32c6.opencli.md)。
3. OpenAI DevDay 2026 applications 已开放。证据等级 `direct-x` + official-link candidate，fulltext `ok`；这是开发者生态日程信号，日期、申请窗口和地点可回溯到 [DevDay page](../raw/2026-06-24/official-link-candidates/openai-2069483224158646739-devday.openai.com.extracted.md)，不代表产品发布已经发生。
4. Daybreak 与 Patch the Planet 继续进入今日窗口。证据等级 `official-source` + `direct-x`，fulltext `ok`；它把 Codex Security plugin、GPT-5.5-Cyber、漏洞验证、补丁生成、维护者支持和受信任访问组织成防御型软件修复工作流，见 [Daybreak](../raw/2026-06-24/rss-fulltext/openai-blog/openai-blog-daybreak-tools-for-securing-every-organization-in-the-world-f7e9d38ae7.opencli.md) 与 [Patch the Planet](../raw/2026-06-24/rss-fulltext/openai-blog/openai-blog-patch-the-planet-a-daybreak-initiative-to-support-open-source-maintain-f0ab1740b8.opencli.md)。
5. Claude Code `v2.1.187` release body 可读。证据等级 `official-source`，fulltext `ok`；新增 sandbox credential 隔离、组织级模型限制、菜单鼠标选择、remote MCP idle timeout、background/subagent/worktree/session 多项修复，说明 Claude Code 正在继续补企业控制面和长会话可靠性，见 [v2.1.187](../raw/2026-06-24/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.187-8181476b54.atom.md)。
6. Claude Blog 页面发现 `Agent identity in Claude Tag`。证据等级 `official-source` 发现线索；页面索引显示 2026-06-24 发布，但本轮 `official-pages.json` 只保存列表 metadata，没有单篇 fulltext 归档，所以只能记录为待读官方候选，见 [official-pages.json](../raw/2026-06-24/official-pages.json)。
7. Karpathy 与 Anthropic 相关 direct-x 继续指向 Claude Tag 的“团队成员式 agent 身份”叙事。证据等级 `direct-x`；它与 Claude Blog metadata 相互印证主题方向，但正文未归档前不能写成完整机制判断。
8. GitHub Trending 继续出现 `anthropics/claude-plugins-official`、`bytedance/deer-flow`、`revfactory/harness`、`mukul975/Anthropic-Cybersecurity-Skills` 和 `garrytan/gstack`。证据等级 `secondary-source`；README 均已归档，说明 agent 生态围绕 plugin、skills、harness、团队角色和长任务运行打包，但本日报没有安装验证这些 repo。
9. 中文 direct-x 中 `cnyzgkc` 的 AI 做 PPT skill 线索抓到了两个 GitHub official-link candidates：`op7418/guizang-ppt-skill` 与 `zarazhangrui/frontend-slides`。证据等级 `direct-x` + repo fulltext `ok`；这是 skills 用于演示文稿生产的实践线索，今天只作为候选，不升级为长期结论。

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS：5 条 always-read 均 fulltext `ok`。今日新增可读重点是 advanced AI shared standards、GPT-5 immunology mystery、Omio conversational travel；Daybreak 与 Patch the Planet 继续作为安全治理和开源修补工作流背景。
- OpenAI Codex releases：`0.143.0-alpha.12` 到 `0.143.0-alpha.8` 均为 `limited`，release Atom 只有短标题；只记录版本出现，不从 alpha 版本号推断功能变化。
- Claude Code releases：`v2.1.187`、`v2.1.186`、`v2.1.183`、`v2.1.181` fulltext `ok`，`v2.1.185` 为 `limited`。今日最强一手新增是 `v2.1.187` 的 credential 隔离、模型限制、remote MCP 超时、background/subagent/worktree 修复。
- Official pages：OpenAI News、Anthropic News、Claude docs release notes、Claude Blog 均为 ok。Claude Blog 列表发现 `Agent identity in Claude Tag`、Claude Desktop on cloud providers、Claude Code steering、MCP connector managed auth、Claude Code artifacts；但本轮没有单篇正文归档，日报只把它们作为 official-page discovery。

## 按主题分组摘要

### AI coding / agent runtime

- Claude Code `v2.1.187` 把安全和组织治理继续下沉到 runtime：sandboxed command 不能读取 credential 文件和 secret env、模型选择受组织配置限制、remote MCP 工具调用 5 分钟无响应会中止、remote session 启动延迟修复、background jobs 和 subagent 深度/工作树清理修复。这些都是面向长会话、远程执行和企业使用的控制面补丁。
- Claude Blog 页面显示 Claude Tag、Claude Desktop 云供应商体验、Claude Code steering、MCP connector managed auth 和 artifacts 都在近期列表中。由于 only-list metadata，没有逐篇 fulltext，本日报不展开功能机制。
- GitHub Trending 的 `claude-plugins-official`、`claude-code-best-practice`、`revfactory/harness` 和 `deer-flow` 继续提供生态线索：plugin、skills、agent team、message gateway、sandbox 和长任务 harness 正在被包装成可分发操作栈。

### Memory / context / skills

- `deer-flow` README 把长任务 SuperAgent harness 拆成子代理、记忆、沙箱、工具、skills 和 message gateway；`revfactory/harness` 把项目描述转成 agent team 与 skills；`gstack` 则把 Claude Code 用法组织成 CEO、Designer、Release Manager、QA 等角色工具集合。这些仍是 README discovery，不能替代安装验证。
- Matt Pocock direct-x 强调手写 skills、specs 与 code watch 的关系；中文 direct-x 里 PPT skills、Codex Gmail plugin 使用、AI 记忆卡等线索都指向“把 agent 操作能力沉淀成可复用流程”的方向。证据多是个人 field notes，应作为候选而不是确定趋势结论。
- Simon Willison 的 OPFS/Pyodide test harness、Datasette release 和 Moebius browser port 文章都已读原文。今天的机制价值主要在“可在浏览器/本地环境复现的测试与模型移植 workflow”，但不是新产品发布。

### Security / governance / public legitimacy

- OpenAI advanced standards 文章与 Daybreak 组合强化同一条线：高能力模型释放越来越依赖评估、标准组织、政府沟通、受信任访问和具体防御 workflow，而不是单纯发布更强模型。
- Claude Code `v2.1.187` 的 credential 隔离和组织模型限制是治理层面的小但明确的 runtime 变化，和 Claude Blog 中 managed auth / team-wide AI identity 的方向相邻。
- Simon Willison 的 prompt injection as role confusion 仍是今日可读安全背景：agent 读取网页、README、issue 或工具输出时，角色边界混淆不是靠格式标签就能彻底解决。

### Enterprise delivery / FDE

- OpenAI Omio 文章继续展示 conversational travel 与 AI-native company 案例。它对企业落地的意义在于产品团队如何把自然语言交互嵌入实际用户流程，而不是只展示聊天 UI，见 [Omio](../raw/2026-06-24/rss-fulltext/openai-blog/openai-blog-how-omio-is-building-the-future-of-conversational-travel-0c794cbb25.opencli.md)。
- FDEHub 的 eval lifecycle、SVPG 的 internal/commercial product 模型、Palantir/Thomas Otter/Ted Mabrey 相关 RSS fulltext 仍在今日窗口内被归档。它们支持“从概念验证到生产”的最后一公里观察，但多数是观点和框架材料。
- Claude Tag discovery 如果正文后续确认，会直接命中企业协作 agent 身份和权限边界；本轮仅记录为待读官方候选。

### Model / evaluation / infra

- GPT-5 immunology mystery 是官方应用案例，强调模型帮助专家生成新假设和重审实验解释；它对长期评估的价值在于“模型协作如何进入专业科学 workflow”，不是可复现 benchmark。
- Google DeepMind 的 AI-accelerated planning 与 Gemini Live Translate、Lilian Weng 的 hallucination/数据文章、Antirez 的 testing/inference/edit tool 文章、Minimaxir 的 Hy3/agent coding 文章均有归档或命中。今天不把这些背景材料升级成单一主结论。
- GitHub release 源里 LangChain、LlamaIndex、vLLM、vLLM Ascend、MCP servers 均有版本条目，但本轮没有 always-read release body；只记录 release 出现。

### Financial agents

- `ZhuLinsen/daily_stock_analysis` 继续作为 GitHub Trending financial-agent discovery candidate。README 描述多市场行情、新闻、决策看板和自动推送；由于涉及投资分析，本日报只记录系统形态，不采纳收益、交易或建议结论。
- direct-x 中个人投资、基金、市场观点较多，但缺少金融机构、合规、人类审批、审计或真实业务 workflow 证据，暂不升级为 financial-agent 主判断。

### Indie / product growth

- `OpenMontage` 与 `palmier-pro` 延续 AI 视频生产方向：前者把 coding assistant 变成视频生产 studio，后者把人和 agent 放进 macOS 视频编辑器。二者 README 已归档，但版权、成本、素材来源、部署门槛和输出可控性待验证。
- `marclou`、`levelsio`、`cellinlab` 等 direct-x 有 onboarding、收购、副业收入和独立产品运营线索；多数是个人经验或短 field note，不写成 adoption metrics。
- `cnyzgkc` 的 Codex Gmail plugin 和 PPT skill 用法是“轻量个人工作流自动化”的高可读线索，但需要单独复现插件授权、邮箱规则和输出质量。

### GitHub Trending discovery

GitHub Trending 今日解析到 10 个 repo，Trending description 覆盖 10/10，README 归档 10/10 成功，来源边界是 `secondary-source` discovery signal。

- `calesthio/OpenMontage` 是开源 agentic video production system，README 提到 pipelines、tools、agent skills、provider 文档和 agent guide。它解决的是从提示到视频素材、剪辑和生产流程自动化的问题；今天值得记录是视频生产开始借用 coding agent 工作流，但 provider 成本、素材版权和生成质量未验证。
- `ZhuLinsen/daily_stock_analysis` 是 LLM 驱动的多市场股票分析系统，面向 A 股、港股、美股、日股、韩股自选股，提供行情、新闻、决策看板和自动推送。它命中 financial-agent 候选，但不能作为投资建议或交易系统证据。
- `mukul975/Anthropic-Cybersecurity-Skills` 是 AI agents 用的网络安全 skills 集合，README 标称 817 个 skills、29 个安全域和多框架映射。它说明专业域技能库正在平台化，但需要审查每个 skill 的质量、权限和安全边界。
- `garrytan/gstack` 是一套面向 Claude Code 的个人高强度操作栈，README 把 CEO、Designer、Eng Manager、Release Manager、Doc Engineer 和 QA 等角色组织成工具集合。它是 usage tactic discovery，不是可复现实验结论。
- `bytedance/deer-flow` 是长任务 SuperAgent harness，README 提到子代理、记忆、沙箱、工具、skills 和 message gateway。它命中 memory/context/runtime 主线，但本日报未安装验证。
- `koala73/worldmonitor` 是实时全球情报 dashboard，聚合新闻、地缘政治和基础设施监控。它对情报工作流有背景价值，但 README discovery 不能证明数据源质量、延迟或误报控制。
- `palmier-io/palmier-pro` 是 Apple Silicon macOS 视频编辑器，强调人和 agent 在时间线里共同生成和编辑视频。它是创意工具 agent 化信号，风险在 macOS 26 门槛、版权和输出可控性。
- `anthropics/claude-plugins-official` 是 Anthropic 管理的 Claude Code plugin 目录，包含内部插件与外部插件提交机制，并声明 plugin 结构。它是 Claude Code runtime 生态信号，但第三方插件仍需用户自行信任。
- `shanraisshan/claude-code-best-practice` 是 Claude Code best practice 仓库，主题从 vibe coding 到 agentic engineering，包含 agents、commands、skills 和 workflow 索引。它是操作方法候选，内容质量需要逐条验证。
- `revfactory/harness` 是 Claude Code 的 team-architecture factory，目标是根据项目描述生成 agent team 与 skills。它命中多 agent 编排和 skills 生成，但 README claim 需要实际项目运行验证。

## 来源证据表

| 信号 | 证据等级 | 本地归档 | 边界 |
| --- | --- | --- | --- |
| OpenAI advanced AI standards | official-source | [OpenAI standards](../raw/2026-06-24/rss-fulltext/openai-blog/openai-blog-helping-build-shared-standards-for-advanced-ai-6507bbb397.opencli.md) | 已读官方正文；标准组织和政策效果未验证。 |
| GPT-5 immunology mystery | official-source | [GPT-5 immunology](../raw/2026-06-24/rss-fulltext/openai-blog/openai-blog-how-gpt-5-helped-immunologist-derya-unutmaz-solve-a-3-year-old-mystery-7c36fb32c6.opencli.md) | 官方案例；不是独立 benchmark。 |
| OpenAI DevDay 2026 applications | direct-x + official-source candidate | [DevDay](../raw/2026-06-24/official-link-candidates/openai-2069483224158646739-devday.openai.com.extracted.md) | 日程/申请窗口信号；非产品发布。 |
| Daybreak / Patch the Planet | official-source + direct-x | [Daybreak](../raw/2026-06-24/rss-fulltext/openai-blog/openai-blog-daybreak-tools-for-securing-every-organization-in-the-world-f7e9d38ae7.opencli.md) | 已读官方正文；未复现安全扫描和补丁质量。 |
| Claude Code v2.1.187 | official-source | [v2.1.187](../raw/2026-06-24/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.187-8181476b54.atom.md) | release body 已读；未本地运行 Claude Code。 |
| Claude Tag blog listing | official-source discovery | [official-pages](../raw/2026-06-24/official-pages.json) | 只有列表 metadata，缺单篇 fulltext。 |
| PPT skills GitHub candidates | direct-x + repo fulltext | [guizang-ppt-skill](../raw/2026-06-24/official-link-candidates/cnyzgkc-2069444827427778960-guizang-ppt-skill.extracted.md) | 使用体验来自 direct-x；未复现生成质量。 |
| GitHub Trending agent repos | secondary-source | [deer-flow](../raw/2026-06-24/github-trending-readmes/bytedance__deer-flow.md) | README discovery；未安装验证。 |
| Financial-agent candidate | secondary-source | [daily_stock_analysis](../raw/2026-06-24/github-trending-readmes/ZhuLinsen__daily_stock_analysis.md) | README discovery；不构成投资建议。 |

## X/Twitter 覆盖说明

`twitterapi.io` status 为 `ok`，27 个账号全部请求完成，共保留 123 条窗口内 tweet。高相关 direct-x 包括 OpenAI/Sam Altman 对 Daybreak 与 DevDay 的发布扩散，Anthropic/Claude 相关账号对 Claude Tag 的扩散，Karpathy 对团队内 agent identity 的评价，Simon Willison 的 Claude Code 并行移植 Moebius field note，Matt Pocock 关于 skills/specs/code watch 的观点，`EXM7777` 对 Claude Code + Codex + omp 多 harness setup 的使用记录，以及中文圈关于 PPT skills、Codex Gmail plugin、AI 记忆卡和个人工作流自动化的实践线索。所有直接来自 API 的 tweet 按 `direct-x` 处理；其中 4 条 official-link candidates 已抓取正文，但只有 OpenAI DevDay 与 Daybreak 属于官方域名强候选。

## Candidate audit 处理记录

[candidate-audit](../reviews/2026-06-24-candidate-audit.md) 已生成：`covered=8`、`missed=55`。处理如下：

- covered：OpenAI advanced standards、GPT-5 immunology、Omio、Daybreak、Patch the Planet、OpenAI DevDay、`guizang-ppt-skill` 和 `frontend-slides` 已被 audit 判定 covered。
- official-link-candidate missed：OpenAI Daybreak 的 X official-link candidate 仍显示 missed，但同一 URL 的 RSS fulltext 已被 audit 判定 covered，并已在“今日高信号”和来源证据表中处理；这是同一官方材料的候选去重问题，不是遗漏。
- matched-rss missed：Google DeepMind planning/translation、Simon Willison、Lilian Weng、Antirez、Xe Iaso、Lucumr、Minimaxir、Geohot、Steve Blank、Keygen、FDEHub、Forward Deployed、SVPG、Ramp、Palantir、Ted Mabrey、Thomas Otter 等已在模型/infra、企业交付/FDE、Memory/skills 或不确定性中按背景材料处理。没有逐条放入“今日高信号”的原因是它们多数为长期背景、观点、旧文重现或同一主题组内的支撑材料。
- top-direct-x missed：Karpathy/Anthropic/Frxiaobei 的 Claude Tag 扩散已在高信号和 X/Twitter 覆盖说明中作为 direct-x + official-page discovery 处理；Sam Altman/OpenAI Daybreak 通过 official-source 升级；levelsio、marclou、jackfriks 等个人叙事保留为 field notes，不写成官方发布、企业采用或模型能力事实。

## 不确定性与待验证项

- OpenAI Codex `0.143.0-alpha.12` 到 `0.143.0-alpha.8` release body 为 `limited`，不能从版本号推断功能变化。
- Claude Code `v2.1.185` release body 为 `limited`；今日可读 release 主体以 `v2.1.187`、`v2.1.186`、`v2.1.183`、`v2.1.181` 为准。
- Claude Blog `Claude Tag`、managed auth、Claude Code steering、artifacts 等只在 official page 列表中出现，缺单篇正文归档；后续最小验证路径是抓取对应 blog fulltext 后再写机制判断。
- GitHub Trending 是 discovery signal；`OpenMontage`、`daily_stock_analysis`、`Anthropic-Cybersecurity-Skills`、`gstack`、`deer-flow`、`claude-plugins-official`、`claude-code-best-practice`、`revfactory/harness` 都需要安装、权限、安全、成本和运行行为验证。
- direct-x field notes 不能替代官方发布、模型基准或企业采用数据；OpenAI DevDay 与 Daybreak 之所以升级，是因为 official-link candidate 抓到了官方域名全文。
- Daybreak/GPT-5.5-Cyber 涉及高风险网络安全能力，本日报只记录官方防御叙述和治理边界，不提供攻击执行步骤。

## 运行统计

- 新增条目：`seen_added=30`。
- 高信号条目：9 条。
- 失败/受限来源：RSS 0 failed；official pages 0 failed；twitterapi.io 0 failed；GitHub REST API failed/rate-limited 后降级 Atom；GitHub release always-read 6 条 `limited`，包括 OpenAI Codex 5 条 alpha release 与 Claude Code `v2.1.185`。
- official-link candidates：4 条，OpenAI Daybreak、OpenAI DevDay、`op7418/guizang-ppt-skill`、`zarazhangrui/frontend-slides` 均 fulltext `ok`。

## 完成审计

- 日报已写入：[docs/2026-06-24-daily-intel.md](2026-06-24-daily-intel.md)。
- candidate audit 已写入：[reviews/2026-06-24-candidate-audit.md](../reviews/2026-06-24-candidate-audit.md)；`covered=8`、`missed=55`，missed 已按重复官方候选、同组背景、弱相关或 direct-x field note 处理。
- trend report 已写入：[trend/reports/2026-06-24-trend-report.md](../trend/reports/2026-06-24-trend-report.md)。
- enabled trends 已检查并写入 manifest：9 个 trend 均有 [trend raw marker](../trend/raw/2026-06-24/)；无 `no-new-signal` marker。`financial-agents` 为 `limited`，`claude-code-feature-watch`、`codex-claude-usage-tactics`、`codex-feature-watch`、`memory-dream`、`claude-tag-identity` 含 `limited` 条目。
- 专题报告已更新：[memory-dream](../trend/memory-dream.md)、[financial-agents](../trend/financial-agents.md)、[forward-deployed-engineering](../trend/forward-deployed-engineering.md)、[enterprise-delivery-system](../trend/enterprise-delivery-system.md)、[codex-feature-watch](../trend/codex-feature-watch.md)、[ai-governance-legitimacy](../trend/ai-governance-legitimacy.md)、[claude-code-feature-watch](../trend/claude-code-feature-watch.md)、[codex-claude-usage-tactics](../trend/codex-claude-usage-tactics.md)、[claude-tag-identity](../trend/claude-tag-identity.md)。
- trend check 已通过：`python3 scripts/run-trend-stage.py --date 2026-06-24 --check` 返回 `ok=true`，`state/trend-state.sqlite` 中 `trend_phase2_runs.status=succeeded`、`verification_ok=1`。
