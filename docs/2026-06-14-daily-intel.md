# 2026-06-14 Daily Source Intelligence

## 采集范围

- 运行日期：2026-06-14，时区：Asia/Shanghai。
- 稳定来源：RSS/Atom 32/32 个 source ok；命中原文 46/46 attempted，46 个 `ok`、0 个 `limited`、0 个 `failed`。GitHub releases 7 个 source 均通过 Atom feed ok，REST API 路径为 `skipped`；GitHub release always-read 10 条，其中 4 条 fulltext `ok`、6 条 `limited`。GitHub Trending daily 1 个 source ok，解析 repo 10 个，README 10/10 归档。official pages 4 个 source ok，0 个 limited/failed。
- X/Twitter：`twitterapi.io` status 为 `ok`，27 个账号请求完成，保留 112 条 direct-x tweet；官方链接候选 2 条，全文均 `ok`。
- 原始产物：[rss-items.json](../raw/2026-06-14/rss-items.json)、[github-items.json](../raw/2026-06-14/github-items.json)、[github-trending.json](../raw/2026-06-14/github-trending.json)、[official-pages.json](../raw/2026-06-14/official-pages.json)、[twitterapi-io-results.json](../raw/2026-06-14/twitterapi-io-results.json)、[official-link-candidates.json](../raw/2026-06-14/official-link-candidates.json)。
- 状态产物：[manifest.json](../raw/2026-06-14/manifest.json)、[source-health.json](../state/source-health.json)、[seen.json](../state/seen.json)。
- 今日新增去重记录：38 条。

## 今日高信号

1. Anthropic 称美国政府以国家安全为由要求暂停所有外籍人士访问 Fable 5 和 Mythos 5，Anthropic 因合规把两个模型对所有客户临时下线。证据等级 `official-source` + `direct-x`，全文 `ok`；今天仍是最强治理信号，因为它把模型能力、出口控制、客户连续性和公共证据标准直接绑在一起，见 [fable-mythos-access](../raw/2026-06-14/official-link-candidates/anthropicai-2065597531644743999-fable-mythos-access.extracted.md)。
2. OpenAI Academy 新增 AI Foundations、Applied AI Foundations、Agents and Workflows 三门课程，继续把企业 AI 培训推进到可复用工作流、检查点和人工复核。证据等级 `official-source`，fulltext `ok`；它说明供应商正在把 adoption 包装成可执行的组织学习系统，见 [OpenAI Academy courses](../raw/2026-06-14/rss-fulltext/openai-blog/openai-blog-new-openai-academy-courses-for-the-next-era-of-work-e17db83823.opencli.md)。
3. OpenAI/BBVA 案例显示 BBVA 把 ChatGPT Enterprise 扩到约 100,000 名员工，并把客户体验、运营和内部工作一起纳入 AI 转型。证据等级 `official-source`，fulltext `ok`；这是金融机构大规模采用 AI 的一手客户叙事，见 [BBVA](../raw/2026-06-14/rss-fulltext/openai-blog/openai-blog-bbva-puts-ai-at-the-core-of-banking-with-openai-a9f0898c41.opencli.md)。
4. OpenAI 宣布将收购 Ona，用安全、客户可控的云执行与编排能力扩展 Codex。证据等级 `official-source`，fulltext `ok`；它把 Codex 从个人 coding helper 推向长任务、持久云环境和企业工作流基础设施，见 [OpenAI to acquire Ona](../raw/2026-06-14/rss-fulltext/openai-blog/openai-blog-openai-to-acquire-ona-6600f3e4b9.opencli.md)。
5. Claude Code `v2.1.173` 到 `v2.1.176` release body 可读，集中在 managed model allowlist、alias 阻断、background sessions、Remote Control、hooks、tmux/SSH 剪贴板、Bedrock 凭据缓存和 Windows/Linux sandbox 修复。证据等级 `official-source`，fulltext `ok`；这是 agent runtime 继续向企业策略、后台任务和跨环境可靠性硬化的信号，见 [v2.1.176](../raw/2026-06-14/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.176-7a83e31276.atom.md)。
6. Simon Willison 记录 Pyodide 314 支持把 Python 扩展编译为 WASM wheel 并发布到 PyPI，他用 Codex 和 GPT-5.5 xhigh 把 Luau WebAssembly spike 打包成 `luau-wasm`。证据等级 `secondary-source`，fulltext `ok`；它对浏览器内 Python、可分发 WASM 扩展和 agent 辅助工程流水线都有参考价值，见 [Publishing WASM wheels](../raw/2026-06-14/rss-fulltext/simonwillison/simonwillison-publishing-wasm-wheels-to-pypi-for-use-with-pyodide-5c61c28c3e.extracted.md)。
7. GitHub Trending 中 `addyosmani/agent-skills`、`obra/superpowers`、`kenn-io/agentsview`、`LMCache/LMCache`、`apple/container` 和 `andrewyng/aisuite` 同时出现，说明 agent workflow 正在被包装成技能、会话分析、本地执行、缓存和多模型接口。证据等级 `secondary-source`，README 已归档；边界是 discovery，不代表质量、安全或长期采用已验证。
8. `steipete` 的 direct-x 指向 `openclaw/crabbox`：Codex 在 crabbox 内构建 crabbox，并用可端到端验证的多 worktree 循环落地。证据等级 `direct-x` + GitHub official-link-candidate，全文 `ok`；它是 coding agent 与隔离执行箱结合的现场使用信号，见 [crabbox](../raw/2026-06-14/official-link-candidates/steipete-2065650561484267540-crabbox.extracted.md)。

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog RSS：5 条 always-read 均 fulltext `ok`。OpenAI Academy 是企业学习和 agent workflow 采用信号；Preply 是教育垂直里的“人类导师 + AI 个性化反馈 + Codex 工程工作流”案例；欧洲可信 AI 生态、BBVA 和 Ona 分别覆盖治理、金融企业采用和 Codex 云执行基础设施。
- OpenAI Codex releases：`0.140.0-alpha.15`、`0.140.0-alpha.16`、`0.140.0-alpha.17`、`0.140.0-alpha.18`、`0.140.0-alpha.19` 均为 always-read，但 fulltext `limited`；只记录版本线，不写功能判断。
- Claude Code releases：`v2.1.173`、`v2.1.174`、`v2.1.175`、`v2.1.176` fulltext `ok`，`v2.1.177` fulltext `limited`。可读 release body 继续围绕模型选择治理、可用模型 allowlist、后台 session、远程控制、hooks、sandbox、tmux/SSH 和企业用量归因展开。
- Official pages：OpenAI News 和 Claude Docs release notes 通过 `opencli-read` 归档；Anthropic News 和 Claude Blog 均 ok。Claude Docs release notes 的公开页面返回区域不可用文案，只能证明访问边界，不能当作 release note 内容证据。

## 按主题分组摘要

### AI governance / public legitimacy

- Anthropic Fable 5 / Mythos 5 访问暂停继续是今天最强治理信号。公司一手声明同时给出政府指令、越狱证据、模型安全策略、客户中断和透明程序主张；适合写入 public legitimacy trend，但必须保留“单方公开声明，政府具体技术证据未公开”的边界。
- OpenAI 支持欧洲 AI 内容透明度实践守则仍在窗口内，和 Anthropic 事件共同说明 frontier model deployment 已进入公共权力、跨境访问、内容来源标识和公司可用性承诺之间的冲突区。
- Armin Ronacher 的 [Dangerous Technology For Americans Only](../raw/2026-06-14/rss-fulltext/lucumr/lucumr-dangerous-technology-for-americans-only-7f3a3d4409.extracted.md) 是高质量 secondary-source 评论，重点在 Anthropic 过去安全叙事与政府出口控制之间的反噬风险；主证据仍以 Anthropic 官方声明和 direct-x 为准。

### Enterprise delivery / FDE / regulated adoption

- OpenAI Academy 把企业采用拆成基础理解、结构化工作流、agent 辅助工作和人工复核，说明供应商正在把“培训”变成部署系统的一部分，而不是只卖工具访问。
- OpenAI/Preply 案例把语言学习里的课后总结、反馈、练习生成、内部 ChatGPT Enterprise 使用和 Codex 工程工作流放在同一个客户故事里。证据等级 `official-source`，fulltext `ok`；它是“人类服务 + AI 工作流 + 生产工程”的垂直行业落地信号，见 [Preply](../raw/2026-06-14/rss-fulltext/openai-blog/openai-blog-how-preply-combines-ai-and-human-tutors-to-personalize-learning-dcc2fd07a9.opencli.md)。
- BBVA 案例把银行内部用量、效率指标、客户体验和运营转型放在同一个客户故事里。它是金融企业采用 AI 的强叙事，但指标来自 OpenAI/BBVA 联合材料，仍需独立 adoption 和风控证据。
- FDEHub 的 [The Eval Lifecycle](../raw/2026-06-14/rss-fulltext/fde-hub/fde-hub-the-eval-lifecycle-what-actually-happens-between-proof-of-concept-and-production-4f68492ee7.opencli.md)、Ted Mabrey 的 [Sorry, that isn't an FDE](../raw/2026-06-14/rss-fulltext/ted-mabrey/ted-mabrey-sorry-that-isn-t-an-fde-871b5124a1.extracted.md) 和 Thomas Otter 的 [DIY, Context layers and the curious growth of the FDE](../raw/2026-06-14/rss-fulltext/thomas-otter/thomas-otter-diy-context-layers-and-the-curious-growth-of-the-fde.-8fb7cb34db.extracted.md) 继续把企业 AI 落地瓶颈指向评估生命周期、上下文层和现场产品反馈，而不是简单人力外包。
- Ramp Builders 的 [marketing incentives to AI agents](../raw/2026-06-14/rss-fulltext/ramp-builders/ramp-builders-we-tested-marketing-incentives-to-ai-agents.-here-s-what-happened.-6b5a2afb52.extracted.md) 和 [on-device receipt matching](../raw/2026-06-14/rss-fulltext/ramp-builders/ramp-builders-automating-receipt-collection-apple-intelligence-for-on-device-inference-fb6f7f1d76.extracted.md) 是企业运营里 agent 激励、收据自动化和端侧推理的线索；今天作为 trend 候选，不升为主高信号。

### LLM / model and evaluation

- Google DeepMind 的 [Gemini 3.5 Live Translate](../raw/2026-06-14/rss-fulltext/google-deepmind-blog/google-deepmind-blog-fluid-natural-voice-translation-with-gemini-3.5-live-translate-8065dada88.extracted.md) 是实时语音翻译产品信号，fulltext `ok`；它和 direct-x 中用户对自动翻译的反馈共同说明多语音交互正在从演示进入日常工具，但本日报未验证延迟、覆盖语言和质量。
- Hugging Face / Ai2 的 [olmo-eval](../raw/2026-06-14/rss-fulltext/huggingface-blog/huggingface-blog-olmo-eval-an-evaluation-workbench-for-the-model-development-loop-80b8efd89b.opencli.md) 把评估做成模型开发循环里的 workbench。它是 infra/eval 信号，今天作为长期评估体系候选处理，不升级为主高信号。
- Xe Iaso 的 [cached input tokens](../raw/2026-06-14/rss-fulltext/xeiaso/xeiaso-why-are-cached-input-tokens-cheaper-with-ai-services-c9756d2a29.extracted.md) 和 antirez 的 DwarfStar 系列继续说明 token cache、本地推理和 agent edit 工具正在成为工程师层面的成本/质量讨论；这些是 secondary-source 技术解释，不是供应商价格公告。

### AI coding / agent runtime

- Claude Code release 线最有可审计信息量：`enforceAvailableModels`、alias 阻断、Default model fallback、background sessions、Remote Control 和 sandbox 修复都指向企业可控性，而不是单纯模型能力。
- Codex alpha release body limited，只能记录 `0.140.0-alpha.15` 到 `0.140.0-alpha.19` 版本线；不能从 alpha 号推断功能变化。
- OpenAI 收购 Ona 和 `steipete` 的 crabbox direct-x 共同显示 coding agent 正向“持久执行环境 + 隔离箱 + 可验证循环”靠近。前者是一手公司动作，后者是 practitioner field note，证据等级不同。

### Agent skills / workflow packaging

- `addyosmani/agent-skills` 和 `obra/superpowers` 再次说明 skill 正从“提示词文件”转为可安装、可组合、带质量门的工作流资产。它解决的是 agent 执行质量不稳定、质量门缺失和流程不可复制的问题。
- Matt Pocock 关于 Fable 访问暂停的 direct-x 更像模型可用性反馈，不足以作为教学或 skill 效果证据；今天不升级成高信号。
- 这组信号的长期意义是：agent ecosystem 竞争点从 IDE 和模型扩展到 workflow package、权限边界、技能市场、安全扫描、会话分析和组织方法论。

### Memory / local knowledge / operator substrate

- `kenn-io/agentsview` 是本地优先的 coding agent 会话分析工具，发现 Claude Code、Codex 等多种 agent session 后同步到本地 SQLite 并开放 Web UI。它对成本、使用轨迹和 agent 操作审计有参考价值；风险是本地日志敏感信息和远程访问配置需要审计。
- `LMCache/LMCache` 把 KV cache 管理、agentic workload benchmark 和推理效率放在一起；它对长期 agent 成本、上下文复用和服务端推理层有参考价值，但本日报未实测性能。
- `apple/container` 和 crabbox 指向同一个底层需求：agent 需要更稳定、隔离、可复现的执行环境。前者是 Mac 上 OCI-compatible container 工具，后者是 coding agent 工作箱实践；两者都还需要安装和安全边界验证。

### Financial agents

- OpenAI/BBVA 是今天最强金融服务信号，说明大型银行正在把 ChatGPT Enterprise 作为员工工作和客户体验转型底座。它不是 autonomous trading 或投资建议 agent 证据，更适合归入 regulated enterprise adoption。
- 今天没有新的 autonomous trading、portfolio、AML、credit decisioning 或 human sign-off financial-agent workflow 证据；不写入 financial agents 强结论。

### GitHub Trending discovery

GitHub Trending 今日解析到 10 个 repo，Trending description 覆盖 10/10，README 归档 10/10 成功，来源边界是 `secondary-source` discovery signal。

- `iptv-org/iptv` 是公开 IPTV channel playlist 集合，提供播放列表、EPG、数据库和 API。它不是 AI 项目，且涉及版权、地域可用性和内容源可靠性边界；本日报只作为 Trending 覆盖记录，不写入长期趋势。
- `addyosmani/agent-skills` 是面向 AI coding agents 的工程技能集合，把需求澄清、计划、构建、测试、评审、简化和发布等 senior engineering workflow 包装成可复用技能。它解决的是 agent 执行质量不稳定、质量门缺失和流程不可复制的问题；今天值得记录是技能市场化和工程方法论继续占据开发者注意力，边界是 README discovery，安装脚本、权限和实际产出质量仍需审计。
- `chatwoot/chatwoot` 是开源、自托管的客户支持平台，集中管理多渠道客户对话，并在 README 中突出 Captain AI support agent。它面向希望保留客户数据控制权的支持团队；今天值得记录是 AI support agent 正进入开源客服平台叙事，边界是 README claim，未验证实际问答质量、数据权限和自动回复风险。
- `obra/superpowers` 是面向 coding agents 的软件开发方法论和 composable skills 框架，覆盖 Claude Code、Codex CLI、Codex App、Gemini CLI、OpenCode 等。它解决的是 agent 直接写代码前缺少 spec、plan、TDD、review 等纪律的问题；边界是 workflow methodology discovery，不代表所有 repo 都适合完整流程。
- `apple/container` 是 Apple 用 Swift 写的 Mac 本地 Linux container 工具，面向 Apple silicon，用轻量虚拟机运行 OCI-compatible images。它解决的是开发者在 Mac 上创建、拉取、运行和构建容器镜像的问题；今天值得记录是本地可控执行环境与 agent sandbox、开发环境隔离有关，边界是 README discovery，未实测 macOS 26 要求和虚拟化限制。
- `music-assistant/server` 是开源媒体库和播放控制服务，连接流媒体服务与多种音箱，server 需要运行在 Raspberry Pi、NAS 或 NUC 这类常开设备上。它不是 AI agent 项目，但对长期后台服务、家庭自动化和本地运行底座有参考价值；本日报不做 AI 功能判断。
- `kenn-io/agentsview` 是本地优先的 coding agent 会话智能和成本分析工具，支持 Claude Code、Codex 和二十多种 agent，首启会发现本机 session、同步到本地 SQLite 并打开本地 Web UI。它解决的是多 agent 使用轨迹、成本和会话搜索分散的问题；风险是会话日志可能包含敏感内容，远程访问和 Host header 配置要审计。
- `LMCache/LMCache` 是面向 LLM inference 的 KV cache 管理层，目标是提升多轮、长上下文和 agentic workload 的吞吐与成本效率。它解决的是重复上下文和长任务推理成本问题；今天值得记录是 memory/cache 逐渐成为 agent 基础设施显性组件，边界是 README discovery，未实测性能。
- `microsoft/PowerToys` 是 Windows 实用工具集合，覆盖窗口管理、搜索、剪贴板、快捷操作和系统定制。它不是 AI 项目，但对个人开发者工作台和本地生产力工具仍有背景意义；本日报不写入长期 AI 趋势。
- `andrewyng/aisuite` 是多模型提供商统一接口，并在 README 顶部展示 OpenCoworker 这个桌面 AI agent 参考应用。它面向想把 OpenAI、Anthropic、Google 或本地 Ollama 接到同一应用层的开发者；今天值得记录是多模型接口与本地桌面 agent 被放在同一 repo 叙事里，边界是 README discovery，未审计凭据处理和自动化权限。

## 来源证据表

| 信号 | 证据等级 | 本地归档 | 边界 |
| --- | --- | --- | --- |
| Anthropic Fable 5 / Mythos 5 访问暂停 | official-source + direct-x | [fable-mythos-access](../raw/2026-06-14/official-link-candidates/anthropicai-2065597531644743999-fable-mythos-access.extracted.md) | 公司一手声明；政府技术证据和法律程序未公开。 |
| OpenAI Academy courses | official-source | [Academy courses](../raw/2026-06-14/rss-fulltext/openai-blog/openai-blog-new-openai-academy-courses-for-the-next-era-of-work-e17db83823.opencli.md) | 供应商培训叙事；学习效果和客户落地需后续验证。 |
| OpenAI / BBVA | official-source | [BBVA](../raw/2026-06-14/rss-fulltext/openai-blog/openai-blog-bbva-puts-ai-at-the-core-of-banking-with-openai-a9f0898c41.opencli.md) | 客户案例和效率指标来自 OpenAI/BBVA 叙事。 |
| OpenAI / Ona | official-source | [OpenAI to acquire Ona](../raw/2026-06-14/rss-fulltext/openai-blog/openai-blog-openai-to-acquire-ona-6600f3e4b9.opencli.md) | 收购计划和产品方向来自 OpenAI 公告；交易完成和具体集成时间未验证。 |
| Claude Code `v2.1.173`-`v2.1.176` | official-source | [v2.1.176](../raw/2026-06-14/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.176-7a83e31276.atom.md) / [v2.1.175](../raw/2026-06-14/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.175-1457a62573.atom.md) | Release body 可读；未本地复现 managed settings、Remote Control 和 sandbox 行为。 |
| Codex `0.140.0-alpha.*` | official-source | [0.140.0-alpha.19](../raw/2026-06-14/github-release-fulltext/openai-codex/openai-codex-0.140.0-alpha.19-49886a01ae.atom.md) | Fulltext `limited`；只记录版本线。 |
| Pyodide WASM wheels / `luau-wasm` | secondary-source | [Publishing WASM wheels](../raw/2026-06-14/rss-fulltext/simonwillison/simonwillison-publishing-wasm-wheels-to-pypi-for-use-with-pyodide-5c61c28c3e.extracted.md) | Practitioner write-up；未复现构建和 PyPI 安装。 |
| Agent skills / workflow packaging | secondary-source | [agent-skills](../raw/2026-06-14/github-trending-readmes/addyosmani__agent-skills.md) / [superpowers](../raw/2026-06-14/github-trending-readmes/obra__superpowers.md) | README discovery；需安装、安全和效果审计。 |
| Local/cache/operator substrate | secondary-source / direct-x | [agentsview](../raw/2026-06-14/github-trending-readmes/kenn-io__agentsview.md) / [LMCache](../raw/2026-06-14/github-trending-readmes/LMCache__LMCache.md) / [crabbox](../raw/2026-06-14/official-link-candidates/steipete-2065650561484267540-crabbox.extracted.md) | README 和 direct-x field note；未验证隐私、性能和隔离边界。 |

## X/Twitter 覆盖说明

`twitterapi.io` status 为 `ok`，27 个账号均完成请求；共保留 112 条窗口内 tweet。高相关 direct-x 包括 `AnthropicAI` 对 Fable 5 / Mythos 5 访问暂停的声明、`steipete` 对 crabbox/Codex 多 worktree 循环的 field note、`simonw` 对 Pyodide WASM wheels 和 OpenAI WebRTC document context 的记录、`gregisenberg` 与 `kloss_xyz` 对 Fable 访问暂停引发本地模型控制权的讨论、`rileybrown` 对自动营销内容 agent 的试用招募，以及 `genspark_ai` 暂停 Claude Fable 5 访问的产品声明。所有直接来自 API 的 tweet 按 `direct-x` 处理；official-link candidates 为 2 条且全文均 ok，见 [official-link-candidates.json](../raw/2026-06-14/official-link-candidates.json)。

## Candidate audit 处理记录

[`../reviews/2026-06-14-candidate-audit.md`](../reviews/2026-06-14-candidate-audit.md) 已生成：`covered=8`、`missed=50`。处理如下：

- official-link-candidate：Anthropic Fable 5 / Mythos 5 访问暂停和 `openclaw/crabbox` 已进入今日高信号、主题摘要、证据表和 X/Twitter 覆盖说明。
- matched-rss：OpenAI Academy、BBVA、Ona、Simon Pyodide WASM wheels、Armin Anthropic 评论、Ted Mabrey FDE 已被 audit 判定 covered；Preply、OpenAI EU 透明度、Google Live Translate、OLMo Eval、FDEHub、Thomas Otter、Ramp Builders、Xe Iaso、antirez 已在主题摘要中补充处理。Lilian Weng、Max Woolf、Steve Blank、Keygen、SVPG、Palantir Elasticsearch 等命中来自宽关键词或旧窗口背景，本日新信息量弱，不升级为高信号。
- top-direct-x：Greg Isenberg / kloss_xyz / levelsio 关于 Fable 访问暂停和本地模型控制权的讨论已在 X/Twitter 覆盖说明中处理；`steipete` 的 appshots、Artificial Analysis coding agent index、OpenClaw 2026.6.6 转发作为 AI coding field notes 保留，未作为可复现 benchmark；SpaceX、玩笑/生活类、个人金融体验和泛 founder 帖弱相关，不升级为 DSI 主结论。

## 不确定性与待验证项

- OpenAI Codex `0.140.0-alpha.*` release body 均为 `limited`，不能从版本号推断功能更新。
- Claude Code `v2.1.177` release body 为 `limited` / no content；只记录版本出现，不写功能判断。
- Claude Docs release notes 官方页面抓取到区域不可用文案，不能当作 release note 内容证据。
- Anthropic Fable/Mythos 访问暂停来自 Anthropic 一手声明和 direct-x，政府指令全文、具体技术证据、恢复时间和客户影响范围未独立验证。
- GitHub Trending README 只证明上榜和 README 可读；skills、会话分析、KV cache、多模型接口、支持平台和容器工具都需要安装、安全、隐私和性能审计。
- Direct-x field notes 是 practitioner narrative；除非有官方链接全文或本地归档机制证据，不升级成 adoption metrics。

## 今日文档翻译

翻译阶段已完成：4 个 shard，32 个目标，32 个已翻译，0 个缺失/跳过。父级校验使用 `python3 scripts/translation-targets.py --date 2026-06-14 --check`，结果为 `ok=true`。

- 索引：[2026-06-14 中文译读索引](../translations/2026-06-14/index.md)
- Manifest：[manifest.json](../translations/2026-06-14/manifest.json)
- daily-high-signal：7 篇，见 [daily-high-signal](../translations/2026-06-14/daily-high-signal/)
- ai-governance-legitimacy：3 篇，见 [ai-governance-legitimacy](../translations/2026-06-14/ai-governance-legitimacy/)
- claude-code-feature-watch：4 篇，见 [claude-code-feature-watch](../translations/2026-06-14/claude-code-feature-watch/)
- codex-claude-usage-tactics：3 篇，见 [codex-claude-usage-tactics](../translations/2026-06-14/codex-claude-usage-tactics/)
- codex-feature-watch：3 篇，见 [codex-feature-watch](../translations/2026-06-14/codex-feature-watch/)
- enterprise-delivery-system：5 篇，见 [enterprise-delivery-system](../translations/2026-06-14/enterprise-delivery-system/)
- financial-agents：1 篇，见 [financial-agents](../translations/2026-06-14/financial-agents/)
- forward-deployed-engineering：3 篇，见 [forward-deployed-engineering](../translations/2026-06-14/forward-deployed-engineering/)
- memory-dream：3 篇，见 [memory-dream](../translations/2026-06-14/memory-dream/)
