# 2026-06-13 Daily Source Intelligence

## 采集范围

- 运行日期：2026-06-13，时区：Asia/Shanghai。
- 稳定来源：RSS/Atom 31/32 个 source ok，`palantir-blog` failed；命中原文 44/44 attempted，44 个 `ok`、0 个 `limited`、0 个 `failed`。GitHub releases 7 个 source 均通过 Atom feed ok，REST API 路径为 `skipped`；GitHub release always-read 10 条，其中 4 条 fulltext `ok`、6 条 `limited`。GitHub Trending daily 1 个 source ok，解析 repo 10 个，README 10/10 归档；official pages 4 个 source ok。
- X/Twitter：`twitterapi.io` status 为 `ok`，27 个账号请求完成，保留 130 条 direct-x tweet；官方链接候选 1 条，全文 `ok`。
- 原始产物：[rss-items.json](../raw/2026-06-13/rss-items.json)、[github-items.json](../raw/2026-06-13/github-items.json)、[github-trending.json](../raw/2026-06-13/github-trending.json)、[official-pages.json](../raw/2026-06-13/official-pages.json)、[twitterapi-io-results.json](../raw/2026-06-13/twitterapi-io-results.json)、[official-link-candidates.json](../raw/2026-06-13/official-link-candidates.json)。
- 状态产物：[manifest.json](../raw/2026-06-13/manifest.json)、[source-health.json](../state/source-health.json)、[seen.json](../state/seen.json)。
- 今日新增去重记录：55 条。

## 今日高信号

1. Anthropic 称美国政府以国家安全为由要求暂停所有外籍人士访问 Fable 5 和 Mythos 5，Anthropic 因合规把两个模型对所有客户临时下线。证据等级 `official-source` + `direct-x`，全文 `ok`；这是模型发布治理、出口控制、越狱证据标准和商业可用性之间的强冲突信号，见 [fable-mythos-access](../raw/2026-06-13/official-link-candidates/anthropicai-2065597531644743999-fable-mythos-access.extracted.md)。
2. OpenAI Academy 新增 AI Foundations、Applied AI Foundations、Agents and Workflows 三门课程，把企业 AI 培训从提示词基础推进到可复用工作流和 agent 辅助工作。证据等级 `official-source`，fulltext `ok`；今天值得看的是 OpenAI 把部署、培训、检查点和人工复核一起包装成企业采用系统，见 [OpenAI Academy courses](../raw/2026-06-13/rss-fulltext/openai-blog/openai-blog-new-openai-academy-courses-for-the-next-era-of-work-e17db83823.opencli.md)。
3. OpenAI/Preply 案例把语言学习里的课后总结、反馈、练习生成、内部 ChatGPT Enterprise 使用和 Codex 工程工作流放在同一个客户故事里。证据等级 `official-source`，fulltext `ok`；它是“人类服务 + AI 工作流 + 生产工程”的垂直行业落地信号，见 [Preply](../raw/2026-06-13/rss-fulltext/openai-blog/openai-blog-how-preply-combines-ai-and-human-tutors-to-personalize-learning-dcc2fd07a9.opencli.md)。
4. OpenAI direct-x 继续确认 Codex rate limit resets 可以保存后再用。证据等级 `direct-x`；它说明 Codex included usage 正被用户理解为可调度资源，但具体可保存数量、计划覆盖和 UI 行为仍需产品文档或账号实测验证，见 [twitterapi-io-results.json](../raw/2026-06-13/twitterapi-io-results.json)。
5. Claude Code `v2.1.175` 和 `v2.1.176` release body 可读，集中在 managed model allowlist、alias 阻断、background sessions、Remote Control、hooks、tmux/SSH 剪贴板、Bedrock 凭据缓存和 Windows/Linux sandbox 修复。证据等级 `official-source`，fulltext `ok`；这是 agent runtime 从功能发布转向企业策略、后台任务和跨环境可靠性的持续硬化线，见 [v2.1.176](../raw/2026-06-13/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.176-7a83e31276.atom.md) 与 [v2.1.175](../raw/2026-06-13/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.175-1457a62573.atom.md)。
6. OpenAI Codex `0.140.0-alpha.13` 到 `0.140.0-alpha.17` 进入 release feed，但 Atom body 均为 `limited`。证据等级 `official-source`；只能记录版本线，不能从 alpha 号推断功能变化，见 [0.140.0-alpha.17](../raw/2026-06-13/github-release-fulltext/openai-codex/openai-codex-0.140.0-alpha.17-02c31ce81a.atom.md)。
7. GitHub Trending 中 `addyosmani/agent-skills`、`obra/superpowers`、`phuryn/pm-skills` 再次上榜，和 Mattermost、LMCache、Tolaria、Apple container 共同说明 agent workflow 的外围正在被包装成技能、协作平台、缓存层、知识库和本地运行底座。证据等级 `secondary-source`，README 已归档；边界是 discovery，不代表质量、安全或长期采用已验证。
8. Simon Willison 记录 OpenAI realtime voice playground 支持 document context、Claude Fable 主动性、Datasette release 借助 Claude Fable 完成等 field notes。证据等级 `secondary-source` + direct-x；这些是 practitioner 证据，可用于观察 agent 工具链使用方式，但不等同于官方产品指标。

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS：5 条 always-read 均 fulltext `ok`。OpenAI Academy 课程是企业 AI 培训和 agent workflow adoption 信号；Preply 是教育垂直行业中“人类导师 + AI 个性化反馈 + Codex 工程工作流”的客户案例；欧洲可信 AI、BBVA 和 Ona 仍在窗口内，作为治理、金融企业采用和知识工作收购背景材料处理。
- OpenAI Codex releases：`0.140.0-alpha.13`、`0.140.0-alpha.14`、`0.140.0-alpha.15`、`0.140.0-alpha.16`、`0.140.0-alpha.17` 均为 always-read，但 fulltext `limited`；只记录版本线，不写功能判断。
- Claude Code releases：`v2.1.173`、`v2.1.174`、`v2.1.175`、`v2.1.176` fulltext `ok`，`v2.1.177` fulltext `limited`。可读 release body 继续围绕模型选择治理、可用模型 allowlist、后台 session、远程控制、hooks、sandbox、tmux/SSH 和企业用量归因展开。
- Official pages：OpenAI News 和 Claude Docs release notes 通过 `opencli-read` 归档；Anthropic News 和 Claude Blog 均 ok。Claude Blog 仍显示 Managed Agents、scheduled agents、vaults、Foundation Models、connector observability 与 Cowork guide 等近期入口，作为 Claude 产品面背景材料处理。

## 按主题分组摘要

### AI governance / public legitimacy

- Anthropic Fable 5 / Mythos 5 访问暂停是今天最强治理信号。公司一手声明同时给出政府指令、越狱证据、模型安全策略、客户中断和透明程序主张；这适合写入 public legitimacy trend，但必须保留“单方公开声明，政府具体技术证据未公开”的边界。
- OpenAI 欧洲可信 AI 生态文章仍在窗口内，和 Anthropic 事件共同说明 frontier model deployment 已从公司安全声明进入公共权力、监管程序和跨境访问控制的冲突区。
- Simon Willison 对 Anthropic 访问暂停的收录可作为 secondary-source 背景，但主证据仍以 Anthropic 官方链接候选全文和 direct-x 为准。

### Enterprise delivery / FDE / regulated adoption

- OpenAI Academy 把企业采用拆成基础理解、结构化工作流、agent 辅助工作和人工复核，说明供应商正在把“培训”变成部署系统的一部分，而不是只卖工具访问。
- Preply 案例展示了客户面功能、内部 enablement、工程提速和运营流程一起推进。它的长期意义不只是教育 AI，而是企业把 AI 嵌入可衡量 workflow 的叙事越来越具体。
- BBVA、Oracle commitment、FDEHub eval lifecycle 和 Thomas Otter 的 context layer 仍是今天 enterprise/FDE 的背景材料：企业落地的瓶颈继续集中在学习系统、评估生命周期、数据上下文和治理路径。

### AI coding / agent runtime

- Claude Code release 线最有可审计信息量：`enforceAvailableModels`、alias 阻断、Default model fallback、background sessions、Remote Control 和 sandbox 修复都指向企业可控性，而不是单纯模型能力。
- Codex alpha release body limited，只能记录版本线；direct-x 中 rate limit reset 可保存和用户对 appshots/Codex live 的反馈，说明 Codex 的实际使用正在向可调度 worker 和视觉上下文工作流靠近。
- Simon Willison 的 Claude Fable / Datasette notes 与 Riley Brown、Levelsio、Greg Isenberg 等 direct-x field notes 显示 Fable/Mythos 发布后用户仍在测试长任务 app building、旧游戏移植、PDF/移动 app 生成和高价 API 工作流；这些是强叙事，不是可复现 benchmark。

### Agent skills / workflow packaging

- `agent-skills`、`superpowers` 和 `pm-skills` 继续出现在 Trending，说明 skill 正从“提示词文件”转为可安装、可组合、带质量门的工作流资产。
- Matt Pocock `/teach` 相关 direct-x 继续显示技能可用于长期教学/练习，而不只用于 coding；但 evidence 仍是用户叙事，不能当作学习效果统计。
- 这组信号的长期意义是：agent ecosystem 竞争点从 IDE 和模型扩展到 workflow package、权限边界、技能市场、安全扫描和组织方法论。

### Memory / local knowledge / operator substrate

- `refactoringhq/tolaria` 是 files-first Markdown knowledge base 桌面应用，继续适合作为 memory/operator substrate discovery signal。
- `LMCache/LMCache` 把 KV cache 管理、agentic workload benchmark 和推理效率放在一起；它对长期 agent 成本、上下文复用和服务端推理层有参考价值，但本日报未实测。
- `apple/container`、`mattermost/mattermost` 和 `music-assistant/server` 分别提供本地容器、协作平台和长期运行服务的基础设施观察点；它们不是同一 AI 趋势，只能作为 agent 工作环境外围底座的 discovery。

### Financial agents

- OpenAI/BBVA 仍是窗口内最强 financial-services 信号，说明银行采用 AI 的企业叙事继续存在；今天没有新的 autonomous trading、portfolio、AML、credit decisioning 或 human sign-off financial-agent workflow 证据。
- Levelsio 关于 Wise Business 转账延迟的 direct-x 是个人金融服务体验，不是 AI financial agents 信号；不写入长期 financial agents 强结论。

### GitHub Trending discovery

GitHub Trending 今日解析到 10 个 repo，README 归档 10/10 成功，来源边界是 `secondary-source` discovery signal。

- `addyosmani/agent-skills` 是面向 AI coding agents 的工程技能集合，把需求澄清、计划、构建、测试、评审、简化和发布等 senior engineering workflow 包装成可复用技能。它解决的是 agent 执行质量不稳定、质量门缺失和流程不可复制的问题；今天值得记录是技能市场化和工程方法论继续占据开发者注意力，边界是 README discovery，安装脚本、权限和实际产出质量仍需审计。
- `music-assistant/server` 是开源媒体库和播放控制服务，连接流媒体服务与多种音箱，server 需要运行在 Raspberry Pi、NAS 或 NUC 这类常开设备上。它不是 AI agent 项目，但对长期后台服务、家庭自动化和本地运行底座有参考价值；本日报不做 AI 功能判断。
- `mattermost/mattermost` 是自托管协作平台，覆盖聊天、工作流自动化、语音、屏幕共享和 AI integration。它面向需要安全协作和软件开发生命周期协同的团队；今天值得记录是 agent/AI 工作流需要进入可审计协作平台，边界是 README claim，未验证企业部署和权限模型。
- `apple/container` 是 Apple 用 Swift 写的 Mac 本地 Linux container 工具，面向 Apple silicon，用轻量虚拟机运行 OCI-compatible images。它解决的是开发者在 Mac 上创建、拉取、运行和构建容器镜像的问题；今天值得记录是本地可控执行环境与 agent sandbox、开发环境隔离有关，边界是 README discovery，未实测 macOS 26 要求和虚拟化限制。
- `iptv-org/iptv` 是公开 IPTV channel playlist 集合，提供播放列表、EPG、数据库和 API。它不是 AI 项目，且涉及版权、地域可用性和内容源可靠性边界；本日报只作为 Trending 覆盖记录，不写入长期趋势。
- `obra/superpowers` 是面向 coding agents 的软件开发方法论和 composable skills 框架，覆盖 Claude Code、Codex CLI、Codex App、Gemini CLI、OpenCode 等。它解决的是 agent 直接写代码前缺少 spec、plan、TDD、review 等纪律的问题；边界是 workflow methodology discovery，不代表所有 repo 都适合完整流程。
- `refactoringhq/tolaria` 是跨平台 Markdown knowledge base 桌面应用，强调 files-first、Git-first、AI context、memory 和 procedures。它解决个人或团队知识库难以作为 AI 上下文持续维护的问题；今天值得记录是 memory/operator substrate discovery，边界是 README，没有验证同步、冲突和隐私实现。
- `maziyarpanahi/openmed` 是 local-first healthcare AI 工具，面向临床文本结构化、实体抽取和 PII 去标识化，强调模型和数据在本地设备运行。它解决医疗文本不能随意上传云端的问题；今天值得记录是端侧医疗 AI 的 packaging 信号，边界是 README claim，不能视为医疗建议、合规认证或临床有效性证明。
- `LMCache/LMCache` 是面向 LLM inference 的 KV cache 管理层，目标是提升多轮、长上下文和 agentic workload 的吞吐与成本效率。它解决的是重复上下文和长任务推理成本问题；今天值得记录是 memory/cache 逐渐成为 agent 基础设施显性组件，边界是 README discovery，未实测性能。
- `phuryn/pm-skills` 是面向产品经理的 skill marketplace，把 discovery、strategy、PRD、launch、metrics、growth 等框架做成技能和 chained workflows。它解决的是产品决策过程缺少结构化 agent workflow 的问题；风险是 PM 框架被包装成自动化后可能放大错误假设，需验证输入质量和组织上下文。

## 来源证据表

| 信号 | 证据等级 | 本地归档 | 边界 |
| --- | --- | --- | --- |
| Anthropic Fable 5 / Mythos 5 访问暂停 | official-source + direct-x | [fable-mythos-access](../raw/2026-06-13/official-link-candidates/anthropicai-2065597531644743999-fable-mythos-access.extracted.md) | 公司一手声明；政府技术证据和法律程序未公开。 |
| OpenAI Academy courses | official-source | [Academy courses](../raw/2026-06-13/rss-fulltext/openai-blog/openai-blog-new-openai-academy-courses-for-the-next-era-of-work-e17db83823.opencli.md) | 供应商培训叙事；学习效果和客户落地需后续验证。 |
| OpenAI / Preply | official-source | [Preply](../raw/2026-06-13/rss-fulltext/openai-blog/openai-blog-how-preply-combines-ai-and-human-tutors-to-personalize-learning-dcc2fd07a9.opencli.md) | 客户案例和平台指标来自 OpenAI/Preply 叙事。 |
| Claude Code `v2.1.175`-`v2.1.176` | official-source | [v2.1.175](../raw/2026-06-13/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.175-1457a62573.atom.md) / [v2.1.176](../raw/2026-06-13/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.176-7a83e31276.atom.md) | Release body 可读；未本地复现 managed settings、Remote Control 和 sandbox 行为。 |
| Codex `0.140.0-alpha.*` | official-source | [0.140.0-alpha.17](../raw/2026-06-13/github-release-fulltext/openai-codex/openai-codex-0.140.0-alpha.17-02c31ce81a.atom.md) | Fulltext `limited`；只记录版本线。 |
| Agent skills / workflow packaging | secondary-source / direct-x | [agent-skills](../raw/2026-06-13/github-trending-readmes/addyosmani__agent-skills.md) / [superpowers](../raw/2026-06-13/github-trending-readmes/obra__superpowers.md) / [pm-skills](../raw/2026-06-13/github-trending-readmes/phuryn__pm-skills.md) | README 和 direct-x discovery；需安装、安全和效果审计。 |
| Local/cache/operator substrate | secondary-source | [LMCache](../raw/2026-06-13/github-trending-readmes/LMCache__LMCache.md) / [Tolaria](../raw/2026-06-13/github-trending-readmes/refactoringhq__tolaria.md) / [Apple container](../raw/2026-06-13/github-trending-readmes/apple__container.md) | README discovery；未验证性能、隐私、同步和部署边界。 |

## X/Twitter 覆盖说明

`twitterapi.io` status 为 `ok`，27 个账号均完成请求；共保留 130 条窗口内 tweet。高相关 direct-x 包括 `AnthropicAI` 对 Fable 5 / Mythos 5 访问暂停的声明、`OpenAI` 的 Codex rate limit resets rollout、`simonw` 的 OpenAI WebRTC document context 与 Claude Fable/Datasette notes、`steipete` 对 Fable/Mythos、Codex appshots、coding-agent benchmark 和 OpenClaw/Codex workflow 的 field notes、`mattpocockuk` 的 subagent 与 `/teach` skill 反馈，以及 `genspark_ai` 的企业 AI 执行层融资叙事。所有直接来自 API 的 tweet 按 `direct-x` 处理；official-link candidates 为 1 条且全文 ok，见 [official-link-candidates.json](../raw/2026-06-13/official-link-candidates.json)。

## Candidate audit 处理记录

[`../reviews/2026-06-13-candidate-audit.md`](../reviews/2026-06-13-candidate-audit.md) 已生成：`covered=3`、`missed=52`。处理如下：

- official-link-candidate：Anthropic Fable 5 / Mythos 5 访问暂停已进入今日高信号、AI governance 摘要和证据表。
- matched-rss：OpenAI Academy 与 Preply 已进入今日高信号；OpenAI EU trustworthy AI、BBVA、Ona 在“一手重点源”和治理/金融/企业采用背景中处理，因已在 6 月 12 日日报作为主高信号记录，本日不重复升级。Google Live Translate、OLMo Eval、Simon Willison、antirez、Xe Iaso、Lucumr、Minimaxir、FDEHub、Forward Deployed、SVPG、Ramp、Ted Mabrey、Thomas Otter 等 fulltext-ok 材料保留为主题背景或 trend 候选；今天的新信息量仍弱于 Anthropic 访问暂停、OpenAI Academy/Preply、Claude Code release 线和 skills/local substrate。
- top-direct-x：OpenAI Codex rate limit resets、Simon Willison Claude Fable / OpenAI WebRTC / Datasette notes、Steipete Codex appshots / PR / benchmark field notes、Matt Pocock subagent feedback、Greg Isenberg/Riley Brown/Levelsio Fable 体验已在今日高信号、AI coding 或 X/Twitter 覆盖说明中处理。SpaceX、个人金融服务体验、founder motivational posts 等虽分数高但弱相关，未升级为 DSI 主结论。

## 不确定性与待验证项

- RSS `palantir-blog` failed；当天日报不把 Palantir 博客作为已覆盖来源。
- OpenAI Codex `0.140.0-alpha.*` release body 均为 `limited`，不能从版本号推断功能更新。
- Claude Code `v2.1.177` release body 为 `limited` / no content；只记录版本出现，不写功能判断。
- Anthropic Fable/Mythos 访问暂停来自 Anthropic 一手声明和 direct-x，政府指令全文、具体技术证据、恢复时间和客户影响范围未独立验证。
- GitHub Trending README 只证明上榜和 README 可读；skills、协作平台、KV cache、本地医疗、知识库和容器工具都需要安装、安全、隐私和性能审计。
- Direct-x field notes 是 practitioner narrative；除非有官方链接全文或本地归档机制证据，不升级成 adoption metrics。

## 今日文档翻译

翻译阶段已完成：4 个 shard，22 个目标，22 个已翻译，0 个缺失/跳过。父级校验使用 `python3 scripts/translation-targets.py --date 2026-06-13 --check`，结果为 `ok=true`。

- 索引：[2026-06-13 中文译读索引](../translations/2026-06-13/index.md)
- Manifest：[manifest.json](../translations/2026-06-13/manifest.json)
- daily-high-signal：6 篇，见 [daily-high-signal](../translations/2026-06-13/daily-high-signal/)
- ai-governance-legitimacy：1 篇，见 [ai-governance-legitimacy](../translations/2026-06-13/ai-governance-legitimacy/)
- claude-code-feature-watch：3 篇，见 [claude-code-feature-watch](../translations/2026-06-13/claude-code-feature-watch/)
- codex-claude-usage-tactics：3 篇，见 [codex-claude-usage-tactics](../translations/2026-06-13/codex-claude-usage-tactics/)
- codex-feature-watch：5 篇，见 [codex-feature-watch](../translations/2026-06-13/codex-feature-watch/)
- enterprise-delivery-system：2 篇，见 [enterprise-delivery-system](../translations/2026-06-13/enterprise-delivery-system/)
- memory-dream：2 篇，见 [memory-dream](../translations/2026-06-13/memory-dream/)
- financial-agents / forward-deployed-engineering：本日为 `no-new-signal`，无新增中文译读目标。
