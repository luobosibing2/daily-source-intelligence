# 2026-05-27 Daily Source Intelligence

## 采集范围

- 运行日期：2026-05-27，时区：Asia/Shanghai。
- 稳定来源：RSS/Atom 32 个 source 全部 ok；GitHub release Atom 7 个 source 全部 ok；GitHub Trending daily 1 个 source ok；official pages 4 个 source ok。
- 原始产物：[`../raw/2026-05-27/rss-items.json`](../raw/2026-05-27/rss-items.json)、[`../raw/2026-05-27/github-items.json`](../raw/2026-05-27/github-items.json)、[`../raw/2026-05-27/github-trending.json`](../raw/2026-05-27/github-trending.json)、[`../raw/2026-05-27/official-pages.json`](../raw/2026-05-27/official-pages.json)、[`../raw/2026-05-27/twitterapi-io-results.json`](../raw/2026-05-27/twitterapi-io-results.json)。
- 状态产物：[`../raw/2026-05-27/manifest.json`](../raw/2026-05-27/manifest.json)、[`../state/source-health.json`](../state/source-health.json)、[`../state/seen.json`](../state/seen.json)。
- 今日新增去重记录：29 条。

## 今日高信号

1. Anthropic 官方工程博客把 agent containment 写成 Claude 产品线的核心安全控制面：permission prompt 会疲劳，真正能兜底的是 sandbox、VM、egress、filesystem boundary、tool permission 和 connector review。证据等级 `official-source`，全文已用 OpenCLI 归档为 [`../raw/2026-05-27/official-page-text/anthropic-how-we-contain-claude.opencli.md`](../raw/2026-05-27/official-page-text/anthropic-how-we-contain-claude.opencli.md)。
2. Codex `0.134.0` release body 把 conversation history search、`--profile` migration、MCP per-server environment/OAuth、connector schema compaction、read-only MCP 并发、extension/hook context、remote reliability 和 managed network proxy 放在同一条 release 里。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-05-27/github-release-fulltext/openai-codex/openai-codex-0.134.0-19a95e38b8.atom.md`](../raw/2026-05-27/github-release-fulltext/openai-codex/openai-codex-0.134.0-19a95e38b8.atom.md)。
3. Claude Code `v2.1.152` 继续扩展 skills/plugins/hooks 的运行时控制：`disallowed-tools` frontmatter、`/reload-skills`、`SessionStart` hook reload/title、`MessageDisplay` hook、plugin marketplace allowlist、large session usage scan、background agent/workflow status、MCP dedupe/egress 修复都进入 release body。证据等级 `official-source`，fulltext `ok`，归档见 [`../raw/2026-05-27/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.152-cd92a18e48.atom.md`](../raw/2026-05-27/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.152-cd92a18e48.atom.md)。
4. GitHub Trending 的 `Understand-Anything`、`ECC`、`knowledge-work-plugins`、`Anthropic-Cybersecurity-Skills`、`stop-slop`、`taste-skill` 继续把 agent 能力包装为 knowledge graph、skills、plugins、hooks、MCP configs、security/domain skill library 和 taste/rubric carrier。证据等级 `secondary-source`，README 10/10 已归档；不能视为质量、采用或安全验证。
5. `twitterapi.io` 直接证据里，Anthropic 官方账号发布 containment 工程博客；Matt Pocock 提到 Sandcastle `Output.object`、Cursor CLI、GitHub Copilot CLI 支持，以及 GitHub label-triggered agent workflow；Steipete 提到 autoreview skill、Rastermill 和 OpenClaw dependency purge。证据等级 `direct-x`，归档见 [`../raw/2026-05-27/twitterapi-io-results.json`](../raw/2026-05-27/twitterapi-io-results.json)。
6. `gregisenberg` 的 direct-x SF field notes 继续把 FDE、usage intelligence、MCP endpoint visibility、agent debt 和 Obsidian/knowledge-base status 放在同一个 builder narrative 中。证据等级 `direct-x`，这是一线观察，不是行业定量事实。

## 一手重点源 / First-party OpenAI & Claude Code

- OpenAI Blog：5 条 always-read RSS 均 fulltext `ok`，与 2026-05-26 相同，主要包括 Grupo Folha/UOL partnership、Virgin Atlantic/Codex、Gartner enterprise coding agents、AdventHealth healthcare adoption、AI math/discrete geometry。今天没有比 2026-05-26 更强的新 OpenAI blog 增量；Virgin Atlantic、Gartner、AdventHealth 仍作为 trend raw 的 official-source 复用。
- OpenAI Codex releases：`0.134.0` fulltext `ok`，是今天最强的一手增量；`rust-v0.134.0-alpha.4` 与 `0.134.0-alpha.1/2/3` 标为 `limited`，只当版本线索。
- Claude Code releases：`v2.1.152` fulltext `ok`，`v2.1.149`、`v2.1.147` 仍可读；`v2.1.150`、`v2.1.148` 标为 `limited`。
- Anthropic Engineering Blog：`How we contain Claude across products` 是今天补采的一手高信号，来自 Anthropic 官方 X 账号 direct-x 发现，并已用 OpenCLI 写入 raw。

## 按主题分组摘要

### AI coding / agent runtime

- Codex `0.134.0` 和 Claude Code `v2.1.152` 共同说明 coding-agent runtime 的竞争面继续从单次代码生成扩展到 session history、profile/permission migration、MCP environment/OAuth、tool schema exposure、read-only tool concurrency、skills reload、hook lifecycle、plugin marketplace allowlist、usage attribution、background workflow visibility 和 remote reliability。
- Anthropic containment 原文把“用户每步批准”降级为易疲劳的人类监督层，把 hard boundary 放到 environment：Claude Code 用 OS-level sandbox 降低 permission prompts，Claude Cowork 用 local VM、mount mode、egress proxy、scoped token、MCP placement 和 connector review 管 blast radius。它的价值在于把 agent 安全从 prompt policy 推到 product runtime architecture。

### Memory / context / skills substrate

- `Understand-Anything` 继续提供 code/knowledge graph discovery；`knowledge-work-plugins` 把 role/team/company workflow 包成 skills/connectors/slash commands/sub-agents；`ECC` 把 skills、rules、hooks、memory optimization、MCP configs 和 security scanning 写成跨 harness operator system；`Anthropic-Cybersecurity-Skills` 把 754 个 security skills 按框架映射。
- 这些 README 只能作为 `secondary-source` discovery。今天的强结论来自 first-party：Codex/Claude Code/Anthropic containment 都在把 context、skills、plugins、hooks、connectors、MCP、permissions 和 sandbox 当作长期 agent state/control plane。

### Enterprise / FDE / delivery system

- OpenAI/Virgin Atlantic、OpenAI/Gartner 和 AdventHealth 仍是今天 trend 的 official-source 复用材料。它们继续支撑 enterprise delivery system 的判断：agent 加速会暴露 backend/API readiness、review/QA、governance、audit、deployment topology、workflow measurement 和 human judgment boundary。
- Anthropic containment 为这条趋势补了安全侧证据：企业不能只问 agent 是否会做事，还要问它在哪个隔离层执行、哪些文件和网络可达、approved domain 是否等价于 capability grant、local/remote MCP 的 trust model 如何变化。
- `gregisenberg` direct-x 的 FDE/usage-intelligence/MCP field notes 可作为辅助观察，但不写入长期专题核心事实，避免把个人现场感受升级成行业结论。

### GitHub Trending discovery

GitHub Trending 今日解析到 10 个 repo，README 归档 10/10 成功，来源边界是 `secondary-source` discovery signal。

- `Lum1104/Understand-Anything`：README 说它把 codebase、knowledge base 或 docs 变成可搜索、可点击、可问答的 knowledge graph，并面向 Claude Code、Codex、Cursor、Copilot、Gemini CLI 等 agent。今天值得继续记录，因为它把 code understanding 做成 agent context substrate；边界是 README 不能证明大型仓库 freshness、跨语言准确性或 permission behavior。
- `affaan-m/ECC`：README 把 skills、instincts、memory optimization、continuous learning、security scanning、rules、hooks 和 MCP configs 打包成 harness-native operator system。它是跨 harness workflow substrate 的强 discovery signal；风险是安装面、权限合并、MCP 安全和卸载路径需要实测。
- `rohitg00/ai-engineering-from-scratch`：AI engineering curriculum，强调 435 lessons、20 phases、每课输出 reusable artifact。它是教育/课程信号，不是 runtime 或产品发布。
- `anthropics/knowledge-work-plugins`：Claude Cowork/Claude Code 的 role plugins 仓库，README 说每个 plugin bundle skills/connectors/slash commands/sub-agents。它值得记录是因为 vendor-adjacent plugin substrate 继续上榜；边界是 README 不能证明企业定制、权限隔离或 marketplace review 质量。
- `mukul975/Anthropic-Cybersecurity-Skills`：社区 cybersecurity skill library，覆盖 754 个 skills、26 security domains、多个框架映射，并声明不是 Anthropic 官方项目。它是 domain skill supply signal，不是 Anthropic 官方发布。
- `hardikpandya/stop-slop` 与 `Leonxlnx/taste-skill`：把 writing/frontend taste 做成 skill/rubric carrier，说明 skills 正在从工具调用扩到风格、审美和质量约束。它们适合做 Memory & Dream 的轻量观察，不宜提升为工程能力事实。
- `DigitalPlatDev/FreeDomain`、`jellyfin/jellyfin`、`Axorax/awesome-free-apps` 与今日 watch 主题弱相关，仅保留 discovery 覆盖。

## 来源证据表

| 信号 | 证据等级 | 本地归档 | 边界 |
| --- | --- | --- | --- |
| Anthropic agent containment | official-source | [`../raw/2026-05-27/official-page-text/anthropic-how-we-contain-claude.opencli.md`](../raw/2026-05-27/official-page-text/anthropic-how-we-contain-claude.opencli.md) | 官方工程博客；未替代产品配置实测。 |
| OpenAI Codex `0.134.0` | official-source | [`../raw/2026-05-27/github-release-fulltext/openai-codex/openai-codex-0.134.0-19a95e38b8.atom.md`](../raw/2026-05-27/github-release-fulltext/openai-codex/openai-codex-0.134.0-19a95e38b8.atom.md) | release body 可读；alpha releases limited。 |
| Claude Code `v2.1.152` | official-source | [`../raw/2026-05-27/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.152-cd92a18e48.atom.md`](../raw/2026-05-27/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.152-cd92a18e48.atom.md) | release body 可读；相邻旧 patch mixed。 |
| GitHub Trending README set | secondary-source | [`../raw/2026-05-27/github-trending.json`](../raw/2026-05-27/github-trending.json) | discovery signal，不代表采用、质量或安全。 |
| X/Twitter direct evidence | direct-x | [`../raw/2026-05-27/twitterapi-io-results.json`](../raw/2026-05-27/twitterapi-io-results.json) | API read evidence；未补 thread/context；不使用 Exa fallback。 |

## X/Twitter 覆盖说明

`twitterapi.io` status 为 `ok`，27 个账号均成功请求；共保留 133 条窗口内 tweet。高相关账号包括 `AnthropicAI`、`simonw`、`mattpocockuk`、`gregisenberg`、`steipete`、`rileybrown`、`EXM7777`、`oviswang`、`cellinlab` 等。所有直接来自 API 的 tweet 在日报解释中按 `direct-x` 处理；没有把缺少 thread/context 的社交观点升级成官方事实。

## 不确定性与待验证项

- Anthropic containment 原文已归档，但日报没有实测 Claude Code auto mode、Cowork VM、MCP proxy、egress proxy 或 connector directory 行为。
- Codex `0.134.0-alpha.*` 与 Claude Code `v2.1.150`/`v2.1.148` fulltext limited，只能作为版本线索。
- Official pages 中 Anthropic News 与 Claude Blog 页面没有 fulltext path；Claude docs release notes 返回 region unavailable 内容，不能当作实际 release note 证据。
- GitHub Trending 只证明上榜和 README 可读；需要源码/运行验证才能判断能力、freshness、权限和安全。
- Financial Agents 今日没有新的 readable high-signal source，已在 trend raw 中记录 no-new-signal。

## 今日文档翻译

翻译阶段已完成，父 runner 使用 4 个 shard 运行 `codex exec --json --model gpt-5.4-mini`，最终 check 通过。

- 译读索引：[`../translations/2026-05-27/index.md`](../translations/2026-05-27/index.md)
- 翻译 manifest：[`../translations/2026-05-27/manifest.json`](../translations/2026-05-27/manifest.json)
- `target_count`: 15
- `translated_count`: 15
- `missing_count`: 0

### daily-high-signal

- [`../translations/2026-05-27/daily-high-signal/anthropic-how-we-contain-claude.opencli.zh.md`](../translations/2026-05-27/daily-high-signal/anthropic-how-we-contain-claude.opencli.zh.md)
- [`../translations/2026-05-27/daily-high-signal/openai-codex-0.134.0-19a95e38b8.atom.zh.md`](../translations/2026-05-27/daily-high-signal/openai-codex-0.134.0-19a95e38b8.atom.zh.md)
- [`../translations/2026-05-27/daily-high-signal/anthropics-claude-code-v2.1.152-cd92a18e48.atom.zh.md`](../translations/2026-05-27/daily-high-signal/anthropics-claude-code-v2.1.152-cd92a18e48.atom.zh.md)

### enterprise-delivery-system

- [`../translations/2026-05-27/enterprise-delivery-system/anthropic-how-we-contain-claude.opencli.zh.md`](../translations/2026-05-27/enterprise-delivery-system/anthropic-how-we-contain-claude.opencli.zh.md)
- [`../translations/2026-05-27/enterprise-delivery-system/openai-gartner-coding-agents.opencli.zh.md`](../translations/2026-05-27/enterprise-delivery-system/openai-gartner-coding-agents.opencli.zh.md)
- [`../translations/2026-05-27/enterprise-delivery-system/openai-virgin-atlantic-codex.opencli.zh.md`](../translations/2026-05-27/enterprise-delivery-system/openai-virgin-atlantic-codex.opencli.zh.md)

### forward-deployed-engineering

- [`../translations/2026-05-27/forward-deployed-engineering/openai-gartner-coding-agents.opencli.zh.md`](../translations/2026-05-27/forward-deployed-engineering/openai-gartner-coding-agents.opencli.zh.md)
- [`../translations/2026-05-27/forward-deployed-engineering/openai-virgin-atlantic-codex.opencli.zh.md`](../translations/2026-05-27/forward-deployed-engineering/openai-virgin-atlantic-codex.opencli.zh.md)

### memory-dream

- [`../translations/2026-05-27/memory-dream/Lum1104__Understand-Anything.zh.md`](../translations/2026-05-27/memory-dream/Lum1104__Understand-Anything.zh.md)
- [`../translations/2026-05-27/memory-dream/affaan-m__ECC.zh.md`](../translations/2026-05-27/memory-dream/affaan-m__ECC.zh.md)
- [`../translations/2026-05-27/memory-dream/anthropic-how-we-contain-claude.opencli.zh.md`](../translations/2026-05-27/memory-dream/anthropic-how-we-contain-claude.opencli.zh.md)
- [`../translations/2026-05-27/memory-dream/anthropics__knowledge-work-plugins.zh.md`](../translations/2026-05-27/memory-dream/anthropics__knowledge-work-plugins.zh.md)
- [`../translations/2026-05-27/memory-dream/claude-code-v2.1.152.atom.zh.md`](../translations/2026-05-27/memory-dream/claude-code-v2.1.152.atom.zh.md)
- [`../translations/2026-05-27/memory-dream/mukul975__Anthropic-Cybersecurity-Skills.zh.md`](../translations/2026-05-27/memory-dream/mukul975__Anthropic-Cybersecurity-Skills.zh.md)
- [`../translations/2026-05-27/memory-dream/openai-codex-0.134.0.atom.zh.md`](../translations/2026-05-27/memory-dream/openai-codex-0.134.0.atom.zh.md)
