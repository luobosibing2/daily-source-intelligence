## 直接答案

本轮 `report-reading-list.json` 有 19 条记录，11 条带可读正文、8 条只有结构化证据或覆盖边界；`seen_added=70`。最值得跟进的四项是 Claude Code v2.1.325 的权限与沙箱修复、Anthropic 对安全评估设计的具体建议、Sierra 的个人智能体协议 Poppy 1.0，以及 ChatGPT Wallet 的逐笔用户批准安排。后两项由 AIHOT 发现并保留 `secondary-source` 边界；其他产品与安全结论也按发布方自述处理。

<!-- dsi-candidate-audit: covered=15 missed=99 -->

## 采集范围

本轮使用统一入口 `DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-11-14`。最终网络运行完成：RSS/Atom 33/33 个源成功，52 条命中主题或一手重点源的正文读取均成功；GitHub release Atom 7/7；GitHub Trending 解析 10 个项目；官方页面 4/5；twitterapi.io 查询 50/50 个配置账号成功，保留 235 条 `direct-x` 推文。流程摘要、来源状态和阅读清单分别见[run-summary](../raw/2026-11-14/run-summary.json)、[manifest](../raw/2026-11-14/manifest.json)和[正文阅读清单](../raw/2026-11-14/report-reading-list.json)。

- **AIHOT 精选 RSS：** `aihot-selected` 请求成功，读取精选 feed 最新 50 条；8 条落在 2026-11-14 北京时间窗口，42 条在窗口外，未知发布时间为 0。50 条均保留 GUID、AIHOT 站内链接、原文链接和发布时间；窗口内 4 条匹配关注主题且原文读取 4/4 成功，另 4 条判为不相关并跳过原文读取。feed 快照为[aihot-selected.xml](../raw/2026-11-14/rss-feeds/aihot-selected.xml)。这只是有界发现源，不代表完整 AI 资讯覆盖；AIHOT 标题与摘要始终作为 `secondary-source`。
- **follow-builders 播客：** [结构化记录](../raw/2026-11-14/podcast-items.json)状态为 `ok`，上游提供 1 集、配置允许 1 集、窗口内 0、窗口外 1、未知 0；transcript 1/1 可读、单集链接 0/1 可用、上游错误 0。完整上游快照：[feed-podcasts.json](../raw/2026-11-14/podcasts/follow-builders/feed-podcasts.json)。
- **X/Twitter：** 50 个配置账号查询均返回成功；主题简报保留 235 条推文，均按 `direct-x` 处理。该接口只覆盖本次请求返回的公开推文，不代表完整账号时间线。

## 今日高信号

1. [Claude Code v2.1.325](https://github.com/anthropics/claude-code/releases/tag/v2.1.325) 的发布说明列出解码安全修复、Bash 权限检查和沙箱写入保护调整，也修复 MCP 任务恢复、上下文压缩和异常退出恢复等问题。它直接涉及智能体执行权限与长任务可靠性；证据是 Anthropic 发布说明，未提供 CVE、严重度或独立复现。[本地 release 正文](../raw/2026-11-14/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.325-3578b3def0.atom.md)
2. Anthropic 的[安全评估设计文章](https://www.anthropic.com/research/building-strong-safety-evaluations)主张按具体风险构造评估，而不是把拒绝率当作安全性的替代指标；文章进一步说明威胁模型、多轮场景、评分规则、人评校准和不确定性报告。方法细节较强，但这是 Anthropic 对自家方法的说明，并非独立审计。[本地正文](../raw/2026-11-14/official-link-candidates/anthropicai-2121317227618340990-building-strong-safety-evaluations.extracted.md)
3. AIHOT 收录的 Sierra 博文称 Poppy 1.0 为个人智能体提供与企业服务交互的身份、权限和沟通层，并以 OAuth、分阶段接入及动作确认来描述授权边界。它与 `MCP`、`OpenAPI`、`UCP` 的分工值得关注；本日报按 AIHOT 发现链保留 `secondary-source`，合作伙伴和生产可用性仍是发布方说法。[AIHOT 条目](https://aihot.news/items/z4wsrxr1xmhg3lq3y0ouq5rmr)（GUID `z4wsrxr1xmhg3lq3y0ouq5rmr`）→ [Sierra 原文](https://sierra.ai/blog/releasing-poppy) · [本地正文](../raw/2026-11-14/rss-fulltext/aihot-selected/aihot-selected-sierra-personal-agent-protocol-poppy-v1.0-53159014de.extracted.md)
4. AIHOT 当日条目链接到 ChatGPT 的公开帖文，称 ChatGPT Wallet 正向美国部分 Pro 用户的 dots 推出，智能体须先取得用户批准，且不接触真实卡号。它把付款确认和凭据隔离带入智能体行动边界讨论；当前证据为 `secondary-source`，帖文没有详述安全检查实现、适用范围或完整推出节奏。[AIHOT 条目](https://aihot.news/items/vot1htumxjgnb0i88rbq3zsuq)（GUID `vot1htumxjgnb0i88rbq3zsuq`）→ [ChatGPT 原帖](https://x.com/ChatGPT/status/2121283151729496235) · [本地归档](../raw/2026-11-14/rss-fulltext/aihot-selected/aihot-selected-chatgpt-chatgpt-wallet-dot-3ddf07f20f.extracted.md)

## 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- **Claude Code：** v2.1.325 的完整发布正文确认，更新覆盖 zstd 解码安全问题、Bash 复合命令权限绕过与规则匹配、`cd` 后拒绝规则失效、worktree/共享 Git 目录的沙箱写保护，以及 MCP 任务和异常退出恢复。发布说明还写明沙箱 Bash 默认走常规权限流程；要在沙箱中免提示执行，需显式设置 `sandbox.autoAllowBashIfSandboxed: true`。这是版本发布方的变更记录，不能据此推导未披露漏洞影响范围。
- **Codex：** 当日阅读清单中的 `0.171.0-alpha.4` release Atom 正文只有 23 个字符（仅 “Release” 与版本号），状态为 `limited`，无法总结其功能或修复。[记录](../raw/2026-11-14/github-items.json) · [受限正文](../raw/2026-11-14/github-release-fulltext/openai-codex/openai-codex-0.171.0-alpha.4-211c809ec5.atom.md)
- **OpenAI 新闻 RSS：** 本次仍按 `fulltext_policy: always` 读取 5 篇全文，均为 `ok`：[*Introducing ChatGPT Wallet*](https://openai.com/index/introducing-chatgpt-wallet)（[本地正文](../raw/2026-11-14/rss-fulltext/openai-blog/openai-blog-introducing-chatgpt-wallet-5bf4951adb.opencli.md)）、[*How Amplitude ships product improvements in 1–2 days with OpenAI*](https://openai.com/business/customer-stories/amplitude)（[本地正文](../raw/2026-11-14/rss-fulltext/openai-blog/openai-blog-how-amplitude-ships-product-improvements-in-1-2-days-with-openai-5b0f73df89.opencli.md)）、[*Gondola doubles revenue as its team builds more with Codex*](https://openai.com/business/customer-stories/gondola)（[本地正文](../raw/2026-11-14/rss-fulltext/openai-blog/openai-blog-gondola-doubles-revenue-as-its-team-builds-more-with-codex-90d7922370.opencli.md)）、[*Holiday Extras is rethinking what it can build with Codex*](https://openai.com/business/customer-stories/holidays-extras-codex)（[本地正文](../raw/2026-11-14/rss-fulltext/openai-blog/openai-blog-holiday-extras-is-rethinking-what-it-can-build-with-codex-0990939c7d.opencli.md)）和[*Supporting research on AI and children’s safety*](https://openai.com/index/children-first-declaration)（[本地正文](../raw/2026-11-14/rss-fulltext/openai-blog/openai-blog-supporting-research-on-ai-and-children-s-safety-b06379671e.opencli.md)）。其 RSS 发布时间换算为北京时间均早于 11 月 14 日目标日；Wallet 条目为 11 月 13 日 23:00，因此不作为本日一手新增。Wallet 的当日 AIHOT/X 发现另按 `secondary-source` 记录，未把该聚合条目升级为 `official-source`。
- **Codex 历史 release 正文：** `0.169.0` 可读正文列出终端工作区、历史任务搜索、会话恢复、自定义模型提供商等更新，但它不在当日阅读清单中，本日报不把它列作 11 月 14 日新发布。其余 Codex 与 Claude Code 的 release Atom 正文状态见[GitHub 原始记录](../raw/2026-11-14/github-items.json)和[manifest](../raw/2026-11-14/manifest.json)。

### 智能体权限、支付与企业互操作

- **Poppy 1.0：** Sierra 的文章把 Poppy 描述为个人智能体和企业服务之间的身份、权限及沟通层；`OAuth` 用来让客户管理智能体权限，可逐步接入并以行业扩展补充能力。文章区分 Poppy 与 `UCP`：前者处理智能体身份/权限/沟通，后者处理商品发现、购物车和结账。文中 Mercury 查询账户信息但转账须走账户审批、Turkish Airlines 预订和付款前由用户批准等均是发布文章里的示例，不表示这些合作流程都已生产上线。AIHOT 的[站内条目与 GUID](https://aihot.news/items/z4wsrxr1xmhg3lq3y0ouq5rmr)保留为发现出处，正文通过其明确的[原文链接](https://sierra.ai/blog/releasing-poppy)读取，证据等级仍为 `secondary-source`。
- **ChatGPT Wallet：** AIHOT 在目标日 00:44（北京时间）记录了 ChatGPT 原帖。归档文本称每笔购买须经用户批准、智能体不接触真实卡号；这只是发布帖的表述，未能从该帖确认安全检查的技术合同。AIHOT[站内记录/GUID](https://aihot.news/items/vot1htumxjgnb0i88rbq3zsuq)与[原帖](https://x.com/ChatGPT/status/2121283151729496235)均保留；该条证据标为 `secondary-source`。
- **Claude Duet：** AIHOT 条目称，原有美国 Pro、Max、Ultra 候补名单用户已获邀请，新用户仍可继续登记，并不表示全球开放。该发现来自 Ado 的 X 帖，属于 `secondary-source`；[官方产品文章](https://claude.com/resources/articles/claude-duet)标注于 2026-10-21，说明早期研究预览在隔离虚拟机/浏览器中运行并在发送、付款、签署或删除前等待用户确认，属于产品方描述。AIHOT[站内记录/GUID](https://aihot.news/items/ajfypca37l5knyrnij49v5ofz) → [原始 X 帖](https://x.com/adocomplete/status/2121338030967697908) · [AIHOT 正文归档](../raw/2026-11-14/rss-fulltext/aihot-selected/aihot-selected-claude-duet-pro-max-ultra-5a9fce8b1e.extracted.md) · [官方文章归档](../raw/2026-11-14/official-link-candidates/corbin_braun-2121263818571669994-claude-duet.extracted.md)。
- **Claude Code Stop hook：** AIHOT 原文链接到 Lydia Hallie 的 X 帖，建议检查失败时用退出码 `2` 将错误交回 Claude 以触发重试；回复指出应限制重试次数，避免不稳定测试造成循环和额外 token 消耗。这是社区帖文，不是本次读取的官方规范，具体行为须按对应版本文档复核。AIHOT[站内记录/GUID](https://aihot.news/items/p0jsxs2bnv6tmnmn1soi56759) → [原始 X 帖](https://x.com/lydiahallie/status/2121313048820617645) · [本地归档](../raw/2026-11-14/rss-fulltext/aihot-selected/aihot-selected-claude-code-stop-hook-exit-code-2-claude-1eae5b2a45.extracted.md)。

### 模型安全评估与治理

Anthropic 的[文章](https://www.anthropic.com/research/building-strong-safety-evaluations)把安全评估拆成可操作的设计问题：先定义具体风险构念，再由领域专家和评估方法专家设计场景；区分描述行为的问题与验证干预效果的问题；高风险情境在无网沙箱运行并实时监控；LLM 评分器用窄而可判定的规则，并先对照人类评分校准。文章用自伤场景说明“拒绝率”不是适当行为的等价指标，也建议预注册指标、报告切片与不确定性。文中的样本量建议和案例属于 Anthropic 的方法说明，不是适用于所有任务的外部标准。[本地正文](../raw/2026-11-14/official-link-candidates/anthropicai-2121317227618340990-building-strong-safety-evaluations.extracted.md)；关联的 [Anthropic X 帖](https://x.com/AnthropicAI/status/2121317227618340990)为 `direct-x`。

### X/Twitter 推主主题摘要

[推主主题简报](../raw/2026-11-14/twitter-topic-brief.json)共保留 235 条 `direct-x`。以下合并了跨主题重复项，只列目标日窗口内较有信息量的帖子；账户查询结果不等于完整时间线。

- 大模型、智能体、编程和治理多个标签都命中 Anthropic 的[安全评估方法公告](https://x.com/AnthropicAI/status/2121317227618340990)：该帖指向其工程博客的 10 条设计、运行和报告建议。帖子为 `direct-x`；技术细节以链接的官方文章为准。
- 智能体系统：`@rauchg` 表示 Workflow SDK 5 / Vercel Workflows 改善首次执行和步骤间延迟，加强加密与安全，并称其持久化日志可供不同智能体运行框架复用。[推文](https://x.com/rauchg/status/2121277727940776114)为 `direct-x`；延迟和规模表现是发布方在社交帖中的说法，未独立测试。
- 独立开发、产品增长与智能体：`@gregisenberg` 提出把个人/公司知识整理进 Markdown、版本管理、事实与语气文件、工作流技能和预算日志，再让每次任务结果反馈到知识库。[推文](https://x.com/gregisenberg/status/2121331227009364340)为 `direct-x`，属于个人实践建议，不是效果评测。
- 大模型、智能体、编程与系统标签还命中 `@Hesamation` 的一年回顾帖；其中市场估值、模型排名和产品状态比较没有附可核对的原始证据，故只保留为[未核实的评论性回顾](https://x.com/Hesamation/status/2121275656310784081)，不把它写成行业事实或高信号。
- 主题简报中的基础设施标签没有目标日内可用的新条目；历史回看帖和只有短链接/无新增技术细节的候选未当作本日高信号。

### GitHub Trending 每日热门项目

本轮解析 10 个项目，10/10 保留 Trending 描述，README 归档和读取均为 10/10。下列机制来自项目 README 与页面描述合并；Trending 只代表本次页面快照中的发现信号，星数和当日增量不是质量背书。

- [alibaba/open-code-review](https://github.com/alibaba/open-code-review) 将确定性规则管线与 LLM 上下文分析结合：`ocr review` 检查 diff、分支或提交，`ocr scan` 扫描整文件。今天值得记录的是它把规则定位与模型判断组合在同一审查流程；README 自报基准称准确率较高但召回率较低，数据、规模与性能尚未独立核验。[本地 README](../raw/2026-11-14/github-trending-readmes/alibaba__open-code-review.md)
- [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) 为编程智能体提供 Web 平台指南，命令行用 `search` 和 `retrieve` 检索相关做法，也提供旧式 API 扫描；对 Origin Trial 和近期易变 API 默认增加采用门槛。它把不断更新的平台知识接入编程流程；项目 README 中的评测提升是自报结果，工具还会收集安装量、智能体名称和检索查询，可通过 `DISABLE_TELEMETRY=1` 退出。[本地 README](../raw/2026-11-14/github-trending-readmes/GoogleChrome__modern-web-guidance-src.md)
- [openai/codex-security](https://github.com/openai/codex-security) 提供 CLI、TypeScript SDK 和 GitHub Action，可扫描仓库、路径或差异，并保存含源代码证据和排除项的发现报告，再验证候选、生成补丁或复核修复。它值得关注的是把安全扫描接入带证据的验证与修复流程；README 要求检查覆盖范围，扫描结果不证明没有漏报。[本地 README](../raw/2026-11-14/github-trending-readmes/openai__codex-security.md)
- [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) 把多市场行情、新闻和公告汇总为 LLM 分析，再通过 Actions、Docker、本地定时任务或 Web 界面生成并分发报告。它展示了“数据汇总→报告→定时分发”的个人投资流程；README 提醒免费行情源可能限流或变化，项目声明仅供研究、不构成投资建议，样例输出不能证明准确性或收益。[本地 README](../raw/2026-11-14/github-trending-readmes/ZhuLinsen__daily_stock_analysis.md)
- [we-promise/sure](https://github.com/we-promise/sure) 是已归档 Maybe Finance 的社区 fork，主打自托管理财数据和多端/API/LLM agent 接入。它为“个人财务数据如何接入不同客户端和智能体”提供一个可观察的开源样例；README 未说明具体 AI 能力与数据流，并提到数据量大时的性能问题，项目也声明与原公司无关联或背书。[本地 README](../raw/2026-11-14/github-trending-readmes/we-promise__sure.md)
- [backnotprop/plannotator](https://github.com/backnotprop/plannotator) 通过 hooks、插件或命令接收智能体计划、文件和差异，供人标注、批准/拒绝后把反馈送回智能体，也支持异步问题收件箱。它把人类审阅和智能体继续执行连成闭环；README 明示远程模式无登录且监听 `0.0.0.0`，分享链接有保密边界，涉及远程部署或内容分享时应先核实访问控制。[本地 README](../raw/2026-11-14/github-trending-readmes/backnotprop__plannotator.md)
- [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) 是自托管监控工具，支持 HTTP、TCP、WebSocket、DNS、Docker 等检查以及多种通知、状态页和双重验证。它是智能体服务和常驻工作流可搭配的运维观察工具；README 的功能列表不证明监控准确度或 SLA，示例默认暴露端口，同时提供仅本机监听方式。[本地 README](../raw/2026-11-14/github-trending-readmes/louislam__uptime-kuma.md)
- [block/buzz](https://github.com/block/buzz) 的 0.X 版本是可自托管的协作中继，把人员、智能体、工作流和 Git 事件写入可搜索的签名事件流，并提供 CLI、ACP/MCP 与 YAML 工作流。它可作为智能体身份、协作和审计共用事件流的探索样例；README 将移动端与审批门列为仍在开发的能力，1.0 位于另一仓库，插件 API 仍处预览期。[本地 README](../raw/2026-11-14/github-trending-readmes/block__buzz.md)
- [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) 把市场复盘、风险管理、交易计划、日志和复盘做成 Claude Code 技能，面向以长期投资为主、择机波段为辅的个人投资者。它显示金融类技能包尝试把研究与交易纪律结构化；README 明确这不是交易信号服务，也不承诺盈利，模型分析和策略建议仍有金融风险。[本地 README](../raw/2026-11-14/github-trending-readmes/tradermonty__claude-trading-skills.md)
- [tailscale/tailcat](https://github.com/tailscale/tailcat) 复用 WireGuard、NAT 穿透和 DERP 数据通路，以带外交换连接地址，提供命令执行、SSH、转发和文件传输。它展示了开发工具在无控制面时复用加密数据通路的方式；地址含预共享密钥，可构成持有者能力，`no-auth-ssh` 下地址相当于 shell 凭据。README 还说明接口不承诺稳定，公共 DERP 无 SLA。[本地 README](../raw/2026-11-14/github-trending-readmes/tailscale__tailcat.md)

### 播客 / 长对话

follow-builders 本轮实际提供 **1 集**，GUID `c9a0c39e-de2a-11f1-9237-d39059052d4c`（身份 `podcast:no-priors:c9a0c39e-de2a-11f1-9237-d39059052d4c`）：*Powering AI-Driven Drug Discovery with President of Isomorphic Labs Max Jaderberg*。发布时间为 `2026-11-12T11:00:00Z`，在本轮窗口外；transcript 可读（47,939 字符），但精确 GUID 未能在 No Priors RSS 中匹配到单集链接，`link_status=limited`。因此本节报告实际 offered/window/status 边界，不把它解释成节目无更新，也不从窗口外 transcript 生成当日洞察。材料来自 follow-builders 聚合 transcript，未做音频复核，证据等级为 `secondary-source`。

- [播客结构化记录](../raw/2026-11-14/podcast-items.json) · [feed 快照](../raw/2026-11-14/podcasts/follow-builders/feed-podcasts.json)
- [唯一单集 transcript](../raw/2026-11-14/podcasts/follow-builders/transcripts/powering-ai-driven-drug-discovery-with-president-of-isomorphic-labs-max-jaderber-2ac097442ec4.md)；上游提供的频道页为 [No Priors YouTube](https://www.youtube.com/@NoPriorsPodcast)，不是经过 GUID 核验的单集链接。

## 来源证据表

| 来源 | 本轮状态 | 证据与覆盖说明 |
| --- | --- | --- |
| RSS / Atom | 33/33 成功 | [原始记录](../raw/2026-11-14/rss-items.json)；52/52 命中或一手重点源正文读取成功。 |
| AIHOT 精选 | `ok`；最新 50 条 | [feed 快照](../raw/2026-11-14/rss-feeds/aihot-selected.xml)与[条目记录](../raw/2026-11-14/rss-items.json)；8 条窗口内、4 条匹配并读取原文，4 条不相关跳过；0 条缺发布时间、GUID 或原文链接。摘要仍是 `secondary-source`，仅覆盖当前最新 50 条。 |
| GitHub release | 7/7 Atom 成功 | [release 记录](../raw/2026-11-14/github-items.json)；10 个一手 release 正文尝试中 5 个 `ok`、5 个 `limited`。 |
| GitHub Trending | 1/1 页面成功，10 个项目 | [项目记录](../raw/2026-11-14/github-trending.json)；描述 10/10、README 10/10；仅作发现信号。 |
| 官方页面 | 4 `ok`、1 `limited`、0 `failed` | [页面记录](../raw/2026-11-14/official-pages.json)；Anthropic Engineering 页面 HTML 已归档但解析出 0 张文章卡，状态为 `limited`，不能据此判断当天没有文章。 |
| X/Twitter | 50/50 账号请求成功 | [API 原始结果](../raw/2026-11-14/twitterapi-io-results.json)及[主题简报](../raw/2026-11-14/twitter-topic-brief.json)；保留 235 条 `direct-x`，不是完整时间线。 |
| 优先 X 官方链接候选 | 正文候选已归档 | [候选索引](../raw/2026-11-14/official-link-candidates.json)；安全评估文章正文可读；Anthropic IPO 页面未提供可确认发布日期，Claude Duet 官方文章日期为 2026-10-21。 |
| follow-builders 播客 | `ok`；offered 1 | [播客记录](../raw/2026-11-14/podcast-items.json)、[feed 快照](../raw/2026-11-14/podcasts/follow-builders/feed-podcasts.json)和[窗口外 transcript](../raw/2026-11-14/podcasts/follow-builders/transcripts/powering-ai-driven-drug-discovery-with-president-of-isomorphic-labs-max-jaderber-2ac097442ec4.md)；1 集窗口外、transcript 可读、单集链接受限、上游错误 0。 |

## 不确定性与待验证项

- AIHOT 的 50 条只是最新精选窗口。8 条窗口内候选中 4 条相关原文读取成功，4 条不相关条目没有进行全文抓取；因此不能从该 feed 推断完整 AI 资讯覆盖。ChatGPT Wallet 官方 RSS 正文时间为北京时间 11 月 13 日 23:00，而 AIHOT 对应 X 条目标注为 11 月 14 日 00:44；日报保留 AIHOT 项为 `secondary-source`，不以两个时间戳不一致的记录合并升级为当日官方原文证据。
- OpenAI RSS 的 5 篇可读正文发布时间都早于 11 月 14 日目标日；日报只说明一手重点源已按策略读取，不将较早客户案例记为今天新发布。
- Codex `0.171.0-alpha.4`、`rust-v0.171.0-alpha.3`、`0.171.0-alpha.2`、`0.171.0-alpha.1` 正文均为 23 字符并标为 `limited`；Claude Code `v2.1.322` 正文也 `limited`。除可读的 Claude Code v2.1.325 外，受限版本不能据此总结功能变更。
- Anthropic Engineering 索引虽成功获取，但解析器没有识别出文章卡；其 0 张卡是解析受限，不是当日无文章的证据。[索引快照](../raw/2026-11-14/official-page-text/anthropic-engineering/anthropic-engineering-anthropic-engineering-9bba7c6d8f.index.html)
- Anthropic IPO 页面来自较早的 X 链接候选，正文没有明确发布日期；页面所列 11 月 19 日定价/上市安排属于当时的条件性预期，不作为当日新闻。[X 链接候选正文](../raw/2026-11-14/official-link-candidates/anthropicai-2120841731302154708-ipo.anthropic.com.extracted.md)
- follow-builders 只表示中央 feed 本轮提供 1 集，不代表六个配置节目逐一完成检查。该集在窗口外，GUID 匹配节目 RSS 未找到单集永久链接；transcript 虽可读，但说话人/时间戳归属和完整节目覆盖仍以聚合器材料为限，且未做音频复核。
- X/Twitter 的接口返回数受账号、端点回溯范围和请求上限约束；50/50 成功只说明请求完成，不证明已读取全部发帖。未使用登录态浏览器或 X 写操作。
- GitHub Trending 的排名、星数和单日星数变化只是采集时点的发现信号。项目功能与风险描述来自 README，自述基准、效果和兼容性尚未独立验证。

## 当天产物

- [本日报](2026-11-14-daily-intel.md)
- [manifest](../raw/2026-11-14/manifest.json) · [run-summary](../raw/2026-11-14/run-summary.json) · [signals](../raw/2026-11-14/signals.json) · [report-reading-list](../raw/2026-11-14/report-reading-list.json)
- [RSS 条目](../raw/2026-11-14/rss-items.json) · [GitHub release](../raw/2026-11-14/github-items.json) · [GitHub Trending](../raw/2026-11-14/github-trending.json) · [官方页面](../raw/2026-11-14/official-pages.json)
- [X/Twitter API 结果](../raw/2026-11-14/twitterapi-io-results.json) · [X/Twitter 主题简报](../raw/2026-11-14/twitter-topic-brief.json) · [优先链接候选](../raw/2026-11-14/official-link-candidates.json)
- 播客：[结构化记录](../raw/2026-11-14/podcast-items.json) · [上游 feed 快照](../raw/2026-11-14/podcasts/follow-builders/feed-podcasts.json) · [窗口外 transcript](../raw/2026-11-14/podcasts/follow-builders/transcripts/powering-ai-driven-drug-discovery-with-president-of-isomorphic-labs-max-jaderber-2ac097442ec4.md)
- 候选审计将在日报生成后写入：[JSON](../reviews/2026-11-14-candidate-audit.json) · [Markdown](../reviews/2026-11-14-candidate-audit.md)

## 边界与验证

本日报依据当日 raw 归档、`report-reading-list.json` 指向的全部可读正文、X/Twitter 结构化证据，以及 README、release body 和 official-link candidate 正文编写。可读窗口外材料只用于说明覆盖边界；AIHOT 与 follow-builders 仍按 `secondary-source` 处理；任何页面解析失败、正文受限或链接未匹配情况均未解释成“没有更新”。
