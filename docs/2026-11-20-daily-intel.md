## 直接答案

2026-11-20 北京时间运行新增入库 56 条，去重状态总数为 8,405。阅读清单有 20 项：9 项指向可读本地正文，11 项是结构化帖子、受限正文或时间边界。本日报整理 8 条高信号，覆盖 OpenAI 的性能故障处理流程与研究加速数据、Claude Code 权限与工具更新、Anthropic 上市及其安全立场、Google 的工具检索和实时世界模型、a16z 的 FDE 培养计划，以及一个个人智能体产品。厂商数据、聚合源摘要、社交帖和项目方 README 均保留原有证据边界。

## 采集范围

- 统一采集命令：DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-11-20，退出码为 0。采集于 2026-11-20 05:26（北京时间）完成；运行、来源计数与证据路径见[run-summary.json](../raw/2026-11-20/run-summary.json)、[manifest.json](../raw/2026-11-20/manifest.json)、[signals.json](../raw/2026-11-20/signals.json)和[report-reading-list.json](../raw/2026-11-20/report-reading-list.json)。
- RSS/Atom：33 个源中 32 个成功；50/50 条命中主题或一手重点正文读取成功。dwarkesh-patel 返回空响应。AIHOT 精选 RSS 单独按最多 50 条最新记录统计，见下文。
- GitHub Releases：7/7 个 Atom 源成功；10 条 OpenAI / Claude Code 一手重点正文均尝试读取，6 条可读、4 条受限。受限的 4 条 Codex Atom 正文只含版本标签。[发布记录](../raw/2026-11-20/github-items.json)。
- GitHub Trending：解析到 10 个项目，Trending 描述与 README 归档均为 10/10。以下项目说明结合榜单描述和本地 README；本轮未安装或运行项目。上榜不代表采用规模、质量、安全性或生产效果。[Trending 记录](../raw/2026-11-20/github-trending.json)。
- 官方页面：4/5 个源成功。Anthropic Engineering 页面已读取，但没有解析出有效文章卡片，状态为 limited；不能据此断言当天没有文章。[页面状态](../raw/2026-11-20/official-pages.json)。
- X/Twitter：twitterapi.io 配置的 50/50 个账号请求成功，共取得 920 条原始帖子，按采集规则保留 239 条 direct-x 记录。API 返回不代表完整账号时间线。[API 结果](../raw/2026-11-20/twitterapi-io-results.json) · [主题 brief](../raw/2026-11-20/twitter-topic-brief.json)。
- 播客：follow-builders 状态 ok，上游本轮 offered 1 集；inside/outside/unknown 为 0/1/0，transcript ok/limited 为 1/0，单集链接 ok/limited 为 1/0，上游错误 0。[podcast-items.json](../raw/2026-11-20/podcast-items.json) · [feed 快照](../raw/2026-11-20/podcasts/follow-builders/feed-podcasts.json)。
- priority X 链接候选：5/5 个候选有归档正文，方法为 curl 或 opencli-read；其中 3 个进入本轮阅读清单。候选来源仍按各自的 X 链接或仓库身份记录。[候选采集记录](../raw/2026-11-20/official-link-candidates.json)。

## 今日高信号

1. **OpenAI 把性能回归从告警调查串成可交接的智能体工作流。** OpenAI 描述的 Performance Factory 由任务服务、工作流状态和转换规则、派发循环、Codex 云端执行及 GitHub／部署事件订阅组成：代理调查告警并提出修复，工程师审查和部署，后续代理再检查性能是否恢复。OpenAI 称流程运行三个多月跟踪了 1,700 多次调查、定位 600 多个根因；其人工抽查的 100 条根因建议中 70% 准确，另外 30% 仍需完善或没有充分证明因果关系。PR 仍须工程师审查合并，统计为厂商自报。[OpenAI 原文](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast) · [本地正文](../raw/2026-11-20/rss-fulltext/openai-blog/openai-blog-how-openai-s-performance-factory-keeps-chatgpt-fast-6687f7be62.opencli.md)。
2. **Claude Code v2.1.328 增加可阻断失败工具调用的钩子。** Claude Code 还扩大了 Opus 4.6 和 Sonnet 4.6 的 auto mode 接入范围，增加 managed policy 的 allowManagedModsOnly 选项，并为自托管 runner 加入会话元数据和队列指标。改动来自官方 GitHub Release Atom 正文；版本页时间为 11 月 19 日 01:14 UTC，约为北京时间当日 09:14。[发布说明](https://github.com/anthropics/claude-code/releases/tag/v2.1.328) · [本地正文](../raw/2026-11-20/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.328-249cf944c1.atom.md)。
3. **Anthropic 宣布以每股 83 美元定价 IPO，并重申其安全立场。** 公司公告称发行 9.8 亿股，预计以 ANT 在 Nasdaq 开始交易，发行完成仍取决于常规交割条件。CEO Dario Amodei 随后的公开声明称，上市让公司财务状况更稳固，并承诺在对安全和人类控制有信心前控制训练与部署节奏。这是公司公告和管理层立场，不是对其安全实践效果的独立验证。[发行公告](https://www.anthropic.com/news/anthropic-prices-initial-public-offering) · [本地公告正文](../raw/2026-11-20/official-link-candidates/anthropicai-2123196808675405860-anthropic-prices-initial-public-offering.extracted.md) · [CEO 帖子](https://x.com/AnthropicAI/status/2123461658890686863)（direct-x）。
4. **Google 在 Gemini API 预览按需检索工具参数。** Gemini Interactions API 可让模型通过 tool_search 按需载入延迟工具的参数 schema；单次请求会记录搜索、返回 schema 和工具调用步骤，也支持远程 MCP server。Google 称该设计针对工具库扩大后提示词开销、延迟和选择准确度问题；功能仍处于 preview，实际节省取决于工具调用比例。[Google 原文](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/) · [本地正文](../raw/2026-11-20/rss-fulltext/aihot-selected/aihot-selected-google-gemini-api-tool-retrieval-57728669e0.extracted.md)。AIHOT 是发现入口，具体机制依据另行读取的 Google 原文；AIHOT 站内记录本身仍是 secondary-source。
5. **AIHOT 发现一则称 Genie 4 已开放 API 与 AI Studio 的公开帖子。** 所链接的公开 X 页面称用户可从文本或图像生成 720p、24fps 的世界，并用 WASD 与提示实时操控；传输方式提到 WebRTC 临时令牌或 WebSocket。该条由 AIHOT 收录并以 curl 读取公开 X 页面，未在本轮通过 twitterapi.io 独立收录，因此保留 secondary-source，不标为 direct-x 或 official-source。[AIHOT 站内条目](https://aihot.news/items/n1nzpfmd3f6zc4abq5s8yxrde) · [所链接帖子](https://x.com/_philschmid/status/2123465741592637445) · [本地正文](../raw/2026-11-20/rss-fulltext/aihot-selected/aihot-selected-google-gemini-api-ai-studio-genie-4-83e8de6339.extracted.md)。
6. **OpenAI 更新其关于智能体加速 AI 研究的内部数据。** 文章报告称，估计需 2–4 小时的人类任务中，智能体无人干预的成功率从 23% 升至 46%；4–8 小时任务从 13% 升至 35%，但不同任务差异显著。该文章标注为 11 月 18 日发布，本轮窗口内的是 OpenAI 官方账号于 11 月 18 日晚间分享它的帖子；数字来自 OpenAI 内部测量、分类和调查，不能直接外推为未来研发加速或递归自我改进结论。[OpenAI 原文](https://openai.com/index/research-acceleration-jagged-frontier/) · [本地正文](../raw/2026-11-20/official-link-candidates/openai-2123191365983248653-research-acceleration-jagged-frontier.opencli.md) · [官方帖子](https://x.com/OpenAI/status/2123191365983248653)（direct-x）。
7. **a16z 启动第二期 FDE Fellowship。** 这期八周项目面向 FDE 和应用 AI 负责人，预计 2027 年 1 月开始；公开名单包括来自 SpaceXSI、OpenAI、Harvey、Exa、Perplexity、Decagon、Cognition、Anthropic、Wonderful 和 Replit 的从业者。它显示机构正持续组织客户现场 AI 交付人才，但项目公告本身不能证明岗位需求或培养效果。[a16z 原文](https://www.a16z.news/p/the-a16z-fde-fellowship-is-back) · [本地正文](../raw/2026-11-20/rss-fulltext/a16z-news/a16z-news-the-a16z-fde-fellowship-is-back-cfaa53aa1f.extracted.md)。
8. **DuskBot 将个人智能体设计成带独立电脑、权限档位和日程的桌面产品。** 项目 README 描述每个 bot 都有独立记忆、浏览器或桌面环境，可按权限设置为先询问或完全访问，并能暂停接管、运行例行任务及连接用户已有 AI 订阅。项目还称秘密由应用代为输入，不暴露给模型；这些都是项目方自述，未做代码、安全或运行验证，真实电脑操作与远程部署权限仍需审查。[仓库](https://github.com/DuskBotAI/duskbot) · [本地仓库页面正文](../raw/2026-11-20/official-link-candidates/exm7777-2123449830291001575-duskbot.extracted.md) · [项目帖子](https://x.com/EXM7777/status/2123449830291001575)（direct-x）。

## 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

OpenAI Blog 的 5 篇一手重点正文均已读取，状态 5/5 ok，方法均为 opencli-read。按 RSS published 时间判断滚动窗口，只有 Performance Factory 在窗口内；其余文章仍保留在一手重点源摘要中，但不作为本日新发布：

- **Performance Factory，11 月 19 日 08:00 UTC。** 用状态化工作流串联性能告警、调查、修复建议、人工审查、部署和回归验证。文章报告三个月处理量及人工评估数字，详见[今日高信号](#今日高信号)。[本地正文](../raw/2026-11-20/rss-fulltext/openai-blog/openai-blog-how-openai-s-performance-factory-keeps-chatgpt-fast-6687f7be62.opencli.md)。
- **The Silent Consensus，11 月 18 日 10:00 UTC。** Dean Ball 讨论市场激励可能如何逐步削弱人类对公司和机构的控制，并主张让智能体权限可理解、可限制、可审计、可撤销。作者明确说明这是个人观点，不代表 OpenAI 或员工，也不是组织政策。[原文](https://openai.com/index/the-silent-consensus) · [本地正文](../raw/2026-11-20/rss-fulltext/openai-blog/openai-blog-the-silent-consensus-e683d40fba.opencli.md)。
- **How Sumitomo Life’s leaders helped teams adopt ChatGPT Enterprise，11 月 18 日 08:00 UTC。** 客户案例称住友生命把 ChatGPT 用于保险研究、管理层提案和投资风险分析代码；周活跃率和 ROI 数字来自厂商案例与使用时间估算，非独立因果评估。[原文](https://openai.com/business/customer-stories/sumitomo-life) · [本地正文](../raw/2026-11-20/rss-fulltext/openai-blog/openai-blog-how-sumitomo-life-s-leaders-helped-teams-adopt-chatgpt-enterprise-b527b6f0dd.opencli.md)。
- **Research acceleration: The jagged frontier，11 月 18 日 08:00 UTC。** 以任务成功率、研究员 agent 使用量、调查和访谈分析研发提效与人类参与；按任务类型差异明显，内部定义和调查方法存在局限。OpenAI 官方账号于 11 月 18 日 23:07 UTC（北京时间 11 月 19 日 07:07）再次分享该文，这条帖子位于本轮滚动窗口内；文章本身不是 11 月 20 日发布。[原文](https://openai.com/index/research-acceleration-jagged-frontier/) · [本地 RSS 正文](../raw/2026-11-20/rss-fulltext/openai-blog/openai-blog-research-acceleration-the-jagged-frontier-9fa731b0ef.opencli.md)。
- **Inside the Codex sandbox，RSS published 为 11 月 18 日 08:00 UTC。** 说明工作区可写而 Git 元数据与 Codex 配置只读、默认关闭网络，以及 macOS Seatbelt、Linux bubblewrap/seccomp 和扩权审批。正文特别说明 stdio MCP server 默认不受 Codex 沙箱约束。按 RSS 发布时间它在窗口外；OpenCLI metadata 显示 11 月 19 日 08:00 UTC，与 RSS 和正文日期不一致。[原文](https://openai.com/index/inside-the-codex-sandbox) · [本地正文](../raw/2026-11-20/rss-fulltext/openai-blog/openai-blog-inside-the-codex-sandbox-53f2a14376.opencli.md)。

Claude Code 与 Codex GitHub Atom 本轮各返回 5 条。Claude Code 的 5 份正文均为 ok：v2.1.328 扩大 auto mode 支持，允许 MCP tool hook 在失败时阻断动作，并修复 deferred tool、agent 恢复和权限问题；v2.1.327 增加从 stdin 读取 MCP JSON、安装 GitHub App 前确认和状态诊断；v2.1.326 增加 Code Mode 与 agent teams 同用及 MCP tool-search 修复；v2.1.325 修复 zstd 响应解码安全问题并加强 shell、沙箱和 worktree 边界；v2.1.323 首次加入可选 Code Mode。版本日期见[GitHub 记录](../raw/2026-11-20/github-items.json)，正文见[Claude Code 归档目录](../raw/2026-11-20/github-release-fulltext/anthropics-claude-code/)。

Codex 5 条中 0.170.0 正文可读，包含 TUI WebRTC 实时语音协商、OpenTelemetry exporter 认证头刷新、跨环境同名 MCP server 实验支持以及若干并发、恢复和沙箱修复。其余 0.172.0-alpha.2、0.172.0-alpha.1、0.171.0-alpha.13.1 和 0.171.0-alpha.13 的 Atom 正文仅有版本名，状态 limited，不能据此推断功能变化。[Codex 正文归档目录](../raw/2026-11-20/github-release-fulltext/openai-codex/)。

### 智能体、工具和工程实践

- Google Tool Retrieval 把大型工具库的参数 schema 按需载入，减少每次请求都携带完整参数的负担；工具检索步骤在同一 Interactions 请求中可审查。功能处于 preview，实际成本和准确度变化需结合工具库与流量验证。[官方原文](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/) · [本地正文](../raw/2026-11-20/rss-fulltext/aihot-selected/aihot-selected-google-gemini-api-tool-retrieval-57728669e0.extracted.md)。
- DuskBot 仓库和作者帖子描述一个以桌面聊天为入口的个人智能体：按 bot 分开记忆和电脑，连接本地或自托管执行环境，并让高风险动作通过审批卡片回到用户。项目方宣称支持多种模型和应用账户；并未独立检查 secret redaction、沙箱或远程连接实现。[帖子](https://x.com/EXM7777/status/2123449830291001575)（direct-x）· [仓库](https://github.com/DuskBotAI/duskbot)。
- Peter Steinberger 的帖子称其已修复 OpenClaw 嵌入式 harness 中的一项问题，并表示部分 harness 尚未更新。这是开发者对代码进展的直接帖子；没有本轮独立查看提交或复测，不据此断言所有集成已修复。[帖子](https://x.com/steipete/status/2123487048250327497)（direct-x）。
- Simon Willison 转述 PostgreSQL 19 的 WAIT FOR LSN 命令可让读副本等到指定 WAL 位置后再读取，从而支持跨请求的 read-your-writes 一致性。该说明是作者博客的转述；具体版本发布时间和数据库行为应以 PostgreSQL 官方发行说明为准。[文章](https://simonwillison.net/2026/Nov/19/postgresql-19/) · [本地正文](../raw/2026-11-20/rss-fulltext/simonwillison/simonwillison-postgresql-19-released-7339d690df.extracted.md)。

### 客户交付与 FDE

a16z 的八周 Fellowship 招募 FDE 和 Applied AI 负责人，第二期预计 2027 年 1 月开始。名单显示客户现场 AI 交付已形成跨公司的专业角色网络，但仍是机构宣布的培训项目，不是岗位或商业化效果数据。[a16z 文章](https://www.a16z.news/p/the-a16z-fde-fellowship-is-back) · [本地正文](../raw/2026-11-20/rss-fulltext/a16z-news/a16z-news-the-a16z-fde-fellowship-is-back-cfaa53aa1f.extracted.md)。

### GitHub Trending 项目

以下介绍依据榜单描述与各项目 README。每项都只是 GitHub Trending 发现信号和项目方自述；本轮没有安装或运行它们。

- [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) 是面向 Claude Code 的授权漏洞赏金与红队技能包，README 称含 83 项技能、15 个命令，覆盖 24 类 Web 漏洞、范围检查、证据整理和报告流程。Trending 描述写 82 项技能，与 README 数字不一致；技能包包含可用于真实目标的攻击知识，只能在明确授权范围内使用。[README](../raw/2026-11-20/github-trending-readmes/elementalsouls__Claude-BugHunter.md)（secondary-source）。
- [obra/superpowers](https://github.com/obra/superpowers) 把需求澄清、设计确认、隔离 worktree、计划、TDD、实现评审和收尾组织成可触发的编码智能体技能流程，目标是让团队按可检查步骤交付代码。不同宿主需要分别安装或配置；README 的流程描述不代表每个宿主都能一致触发。[README](../raw/2026-11-20/github-trending-readmes/obra__superpowers.md)（secondary-source）。
- [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) 提供 CLI-Hub 浏览和安装现有 CLI，也提供七阶段生成流程，把可访问源码的软件封装成智能体能调用的命令、JSON 输出和可撤销操作。仓库自报的应用与测试数量未独立核验；生成的 CLI 会操作真实软件和文件，执行前需检查副作用与授权。[README](../raw/2026-11-20/github-trending-readmes/HKUDS__CLI-Anything.md)（secondary-source）。
- [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 是用于学习训练流程的轻量 PyTorch 模型与教程，涵盖分词、预训练、SFT、LoRA、偏好优化、工具调用和 Agentic RL。README 中“约两小时、约三美元”描述单张 RTX 3090 上的小数据训练与微调，不代表能训练出高能力通用模型。[README](../raw/2026-11-20/github-trending-readmes/jingyaogong__minimind.md)（secondary-source）。
- [cursor/plugins](https://github.com/cursor/plugins) 是 Cursor 插件目录，用插件清单组织 skills、rules 和 MCP 配置，供开发者安装第三方工具和服务。目录同时包含只读与会发邮件、改记录、购买、发布或交易的插件；逐项核实权限和确认机制，不要把被列入市场当作安全审查。[README](../raw/2026-11-20/github-trending-readmes/cursor__plugins.md)（secondary-source）。
- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) 提供网页搜索、抓取、爬取、URL map 和 Agent 数据接口，支持本机单页工具与 Docker 自托管服务。README 说明本机加载失败时可能转向 Firecrawl Cloud，只有显式关闭云端 fallback 才保证本机路径；抓取的站点政策与数据流需要用户核对。[README](../raw/2026-11-20/github-trending-readmes/firecrawl__firecrawl.md)（secondary-source）。
- [nginx/nginx](https://github.com/nginx/nginx) 是成熟的 Web 服务、反向代理、负载均衡、API 网关和缓存工具，基于文本配置与 master/worker 进程管理请求。它是部署基础设施而非本日 AI 新发布；README 将 Windows 构建描述为开发测试 PoC。[README](../raw/2026-11-20/github-trending-readmes/nginx__nginx.md)（secondary-source）。
- [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) 为 PyTorch、TensorFlow、ONNX 等模型提供转换和推理优化，并支持 CPU、GPU 与 Intel NPU 部署，适合降低边缘或云推理资源需求。README 与榜单描述证明的是工具包宣称的功能，未在本轮测量模型性能。[README](../raw/2026-11-20/github-trending-readmes/openvinotoolkit__openvino.md)（secondary-source）。
- [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) 是生成自包含 HTML 与 SVG 教学图的设计技能，可把 Mermaid、draw.io 等图表导入后继续编辑并导出。Trending 描述称 45 种图，README 列 51 种；本地 README 的数字较新但未独立验证。[README](../raw/2026-11-20/github-trending-readmes/cathrynlavery__diagram-design.md)（secondary-source）。
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) 并行检索 Reddit、X、YouTube、Hacker News、Polymarket 和 GitHub 等来源，按相关度、互动度和新鲜度排序，再合并重复事件生成带来源的研究简报，也支持本地 SQLite watchlist。覆盖取决于密钥、登录态和启用工具；若使用外部模型重排，检索主题和片段会发送给所选模型。[README](../raw/2026-11-20/github-trending-readmes/mvanhorn__last30days-skill.md)（secondary-source）。

### X/Twitter 推主主题摘要

下表按本轮阅读清单选取窗口内的代表帖子。帖子可能被多个主题标签重复匹配；同一帖子只计为一个信号。内容来自 twitterapi.io，均标为 direct-x。

| 主题 | 窗口内代表帖子 |
| --- | --- |
| LLM / Frontier Models | OpenAI 分享其研究加速数据，详见[官方文章](https://openai.com/index/research-acceleration-jagged-frontier/)和[帖子](https://x.com/OpenAI/status/2123191365983248653)；Anthropic CEO 的 IPO 安全立场见[帖子](https://x.com/AnthropicAI/status/2123461658890686863)。 |
| AI Agent / Agentic Workflow | DuskBot 团队成员谈其个人智能体产品定位，链接[项目帖](https://x.com/EXM7777/status/2123449830291001575)和[仓库](https://github.com/DuskBotAI/duskbot)；Steipete 提到 OpenClaw embedded harness 修复，[帖子](https://x.com/steipete/status/2123487048250327497)，未独立复测。 |
| AI Coding / Developer Tools | Steipete 的 OpenClaw harness 修复说明仍是工程进展自述；[另一帖子](https://x.com/steipete/status/2123473243520864573)转发了对终端编码智能体的评论，没有形成可验证的产品或能力结论。 |
| AI Governance / Public Legitimacy | Anthropic CEO 在上市声明中谈训练和部署节奏，[帖子](https://x.com/AnthropicAI/status/2123461658890686863)；Garry Tan 转发了是否应放慢前沿 AI 的辩论提问，[帖子](https://x.com/garrytan/status/2123453540631036230)，本轮没有辩论完整内容；Steipete 分享 Dean Ball 的 The Silent Consensus 文章，[帖子](https://x.com/steipete/status/2123494388743741574)（文章作者说明这是个人观点，并非组织立场）。 |
| AI Infrastructure / Open Source | 本轮阅读清单没有选入窗口内可独立核验的高相关 X 帖。OpenAI 与 AMD 的芯片设计帖只在较宽的原始回看范围内；该[原帖](https://x.com/OpenAI/status/2123100386638877054)发表于本日滚动窗口之前，仅作为窗口边界示例，不计作今日信号。 |
| Indie Hacking / Solo Founder | 本轮没有选入高相关的新产品或营收信号；一条关于购买 $ANT 的帖子不构成可核验 AI 进展。 |
| Product / Growth / GTM | DuskBot 帖子提供个人智能体产品自述，[帖子](https://x.com/EXM7777/status/2123449830291001575)；没有独立用户或收入数据。 |
| AI Systems / Automation | DuskBot 描述按 bot 分开的记忆、电脑和审批档位，[帖子](https://x.com/EXM7777/status/2123449830291001575)；Steipete 称其修复了嵌入式 harness 的一个问题，[帖子](https://x.com/steipete/status/2123487048250327497)，尚无本轮复现。 |

### 播客 / 长对话

follow-builders 本轮 status 为 ok，中央 feed offered 1 集，inside/outside/unknown 为 0/1/0，transcript ok/limited 为 1/0，单集 canonical link ok/limited 为 1/0，上游错误为 0。唯一单集是 AI & I by Every 的《Notion’s Founder on the One Thing Your AI Is Missing》，GUID 为 flightcast:01M7N6THM33K8YFWM1YCX4ZFKV，发布时间 2026-11-18 18:19:30 UTC，位于本日窗口外。它的 transcript 路径存在，但不属于可读的窗口内单集，本日报不写洞察卡，也未复核音频；speaker 和 timestamp 覆盖均为 false。[canonical 单集链接](https://www.youtube.com/watch?v=PGWvMrF4XIA) · [podcast-items.json](../raw/2026-11-20/podcast-items.json) · [follow-builders 原始 feed 快照](../raw/2026-11-20/podcasts/follow-builders/feed-podcasts.json) · [窗外 transcript](../raw/2026-11-20/podcasts/follow-builders/transcripts/notion-s-founder-on-the-one-thing-your-ai-is-missing-673dba75232b.md)。这是 follow-builders 聚合 transcript，证据等级为 secondary-source；offered 1 集不等于逐节目检查或完整覆盖。

## 来源证据表

| 来源 | 本轮状态与覆盖 | 证据等级与本地入口 |
| --- | --- | --- |
| RSS/Atom | 32/33 源成功；50/50 条命中或一手重点正文读取成功；dwarkesh-patel 返回空响应 | [rss-items.json](../raw/2026-11-20/rss-items.json) |
| AIHOT 精选 RSS | 最新 50 条；9 条窗内、41 条窗外、0 条时间未知；3 条匹配、6 条不相关；原文链接 50/50 存在；3/3 匹配原文经 curl 读取成功 | secondary-source；[XML 快照](../raw/2026-11-20/rss-feeds/aihot-selected.xml) · [采集记录](../raw/2026-11-20/rss-items.json) |
| GitHub Releases | 7/7 Atom 源成功；一手重点正文 6 ok、4 limited；Claude Code 5/5 可读，Codex 1/5 可读 | official-source；[github-items.json](../raw/2026-11-20/github-items.json) |
| GitHub Trending | 10 个项目；描述、README 均 10/10 可读 | 项目方 README 自述，secondary-source；[Trending 记录](../raw/2026-11-20/github-trending.json) |
| 官方页面 | 4 个成功、1 个 limited；Anthropic Engineering 索引抓取成功但未解析出文章卡片 | [official-pages.json](../raw/2026-11-20/official-pages.json) |
| OpenAI Blog 一手 RSS | 5 篇全文 5/5 ok；仅 Performance Factory 的 RSS 发布时间落入本日滚动窗口 | official-source；[RSS 与正文状态](../raw/2026-11-20/rss-items.json) · [正文目录](../raw/2026-11-20/rss-fulltext/openai-blog/) |
| X/Twitter | twitterapi.io 50/50 账号成功；920 条原始、239 条保留 | direct-x；[API 原始结果](../raw/2026-11-20/twitterapi-io-results.json) · [主题 brief](../raw/2026-11-20/twitter-topic-brief.json) |
| follow-builders 播客 | status ok；offered/inside/outside/unknown 为 1/0/1/0；transcript 与链接各 1/0 ok/limited；上游错误 0 | 聚合 transcript 为 secondary-source；[podcast-items.json](../raw/2026-11-20/podcast-items.json) · [feed 快照](../raw/2026-11-20/podcasts/follow-builders/feed-podcasts.json) · [本地 transcript](../raw/2026-11-20/podcasts/follow-builders/transcripts/notion-s-founder-on-the-one-thing-your-ai-is-missing-673dba75232b.md) |

## X/Twitter 覆盖说明

twitterapi.io 本轮对配置中的 50 个账号均返回成功，共获得 920 条 API 原始记录，按采集规则保留 239 条 direct-x。主题 brief 会按多个标签重复收录同一帖子，也可能包含转帖和个人评论；报告按帖子链接去重，不把个人观点写成产品公告或测试结论。OpenAI 与 AMD 的旧帖仍可能出现在 API 较宽的原始回看范围内，但超出本日报滚动窗口，未列为今日信号。该覆盖不等于完整时间线；未使用登录态浏览器、Exa、X 写操作或账号凭据。

## 不确定性与待验证项

- dwarkesh-patel RSS 返回 curl: (52) Empty reply from server；本轮缺少该来源的 feed 覆盖。
- Anthropic Engineering 首页读取成功但 article card 解析数为 0，状态 limited；不能据此写成当天没有文章。
- Codex 4 条 Alpha release Atom 正文只有版本标签。版本名可确认，具体功能变化不可确认；未写成 changelog。
- OpenAI 博客部分页面的日期元数据互相冲突。本轮按 RSS published 字段判断窗口：Performance Factory 的 RSS 时间与文章日期均为 11 月 19 日，但 OpenCLI metadata 标为 11 月 18 日；Inside the Codex sandbox 的 RSS 和正文日期为 11 月 18 日，OpenCLI metadata 却标为 11 月 19 日。The Silent Consensus、Sumitomo Life 也有 OpenCLI 日期与 RSS／正文日期差异。四篇较早文章保留为一手重点源材料，不据 OpenCLI metadata 将其升级为窗口内信号。
- AIHOT 只覆盖站点最新 50 条精选。50 条均保留 AIHOT feed 发布时间、GUID、station URL 和原文链接；9 条在窗内，3 条命中主题且原文 3/3 可读，6 条因不相关未读取，41 条窗外。feed 标题与摘要始终是 secondary-source；Google Tool Retrieval 另有独立读取的 Google 原文，不能把 AIHOT 摘要当作该原文。Genie 4 的链接页是公开 X 页面，记录仍按 secondary-source，不升级成 direct-x。
- DuskBot 与 GitHub Trending 的功能、安全和使用量说明来自项目方材料；本轮没有做代码审查、安装测试或生产验证。Claude-BugHunter 只应在授权目标上使用；Cursor 插件目录、CLI-Anything 和 last30days-skill 涉及外部服务、写操作或已登录数据，需要先核对权限和数据流。Claude-BugHunter 的技能数和 diagram-design 的图表数在榜单描述与 README 间不一致。
- 播客上游只提供 1 集且它位于窗口外。transcript 可读、canonical link 存在，但本日没有窗口内 transcript；speaker/timestamp 覆盖均为 false。该中央 feed 结果不能解释为所有节目都没有更新。
- X/Twitter 只反映 API 本轮返回的 50 个账号和 239 条保留帖子；主题标签有重叠，帖子观点没有独立复现。直接 X 内容按 direct-x，AIHOT 与项目方材料按 secondary-source。
- 候选审计共 115 项：15 项正文覆盖、100 项未覆盖。100 条未覆盖记录均有处置和说明：87 条 outside_window、4 条 not_selected、4 条 insufficient_evidence、4 条 read_not_relevant、1 条 duplicate。[审计 JSON](../reviews/2026-11-20-candidate-audit.json) · [审计 Markdown](../reviews/2026-11-20-candidate-audit.md)。

## 当天产物

- 日报：[2026-11-20-daily-intel.md](2026-11-20-daily-intel.md)
- 流程和阅读证据：[run-summary.json](../raw/2026-11-20/run-summary.json) · [manifest.json](../raw/2026-11-20/manifest.json) · [signals.json](../raw/2026-11-20/signals.json) · [report-reading-list.json](../raw/2026-11-20/report-reading-list.json)
- 候选审计：[JSON](../reviews/2026-11-20-candidate-audit.json) · [Markdown](../reviews/2026-11-20-candidate-audit.md)
- AIHOT：[XML feed 快照](../raw/2026-11-20/rss-feeds/aihot-selected.xml) · [采集记录](../raw/2026-11-20/rss-items.json) · [3 条已读原文目录](../raw/2026-11-20/rss-fulltext/aihot-selected/)
- 播客：[podcast-items.json](../raw/2026-11-20/podcast-items.json) · [feed 快照](../raw/2026-11-20/podcasts/follow-builders/feed-podcasts.json) · [窗外 transcript](../raw/2026-11-20/podcasts/follow-builders/transcripts/notion-s-founder-on-the-one-thing-your-ai-is-missing-673dba75232b.md)
- 派生展示：[日报索引 JSON](2026-11-20-daily-intel.index.json) · [日报 HTML](2026-11-20-daily-intel.html) · [总索引页](index.html)
- 趋势分析：[trend report](../trend/reports/2026-11-20-trend-report.md)

## 边界与验证

本日报依据 2026-11-20 的统一采集、状态准备与可读正文归档，按北京时间滚动窗口整理。AIHOT 与 follow-builders transcript 保留 secondary-source 身份，X/Twitter 帖子按 direct-x 标记，GitHub Trending 项目按项目方 README 自述处理；未知窗口、受限 changelog、平台范围与项目安全结论均未超出本地证据。候选审计、严格日报校验、日期 bundle、趋势 Phase 1/2、趋势检查和 dsi.py check 的最终状态以本轮实际命令结果为准。

<!-- dsi-candidate-audit: covered=15 missed=100 -->
