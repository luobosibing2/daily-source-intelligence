# 每日情报 | 2026-11-11

<!-- dsi-candidate-audit: covered=31 missed=109 -->

## 采集范围

本轮按北京时间 2026-11-11 运行统一入口：`DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-11-11`。入口完成，`state/seen.json` 新增 89 条记录，阅读清单有 34 项，其中 18 项有可读本地正文、16 项是结构化证据或覆盖边界。

- **RSS / Atom**：33/33 个源成功；58/58 条命中或一手重点正文均尝试读取且可读。AIHOT 精选 Feed 状态 `ok`，只覆盖最新 50 条：16 条发布时间落在北京时间当天，10 条匹配主题、6 条不相关；10 条匹配项的原文均读取成功，34 条窗口外和 6 条不相关内容未读取原文。50 条均有 GUID 与原文链接。AIHOT 站点标题、摘要和发现记录按 `secondary-source` 处理，最新 50 条不是完整资讯覆盖。
- **GitHub Releases**：7/7 个 Atom feed 成功。10 条一手重点发布正文尝试读取，4 条可读、6 条 `limited`；其中 Codex 5 条均只有版本标题或短 changelog 片段，Claude Code 最新的 `v2.1.322` 正文也受限。
- **GitHub Trending**：解析 10 个项目，Trending description 10/10；README 9/10 可读。只有 `sherlock-project/sherlock` 缺 README，按待读候选处理。Trending 只作项目发现线索，不代表质量背书或当日发布。
- **官方页面**：4/5 成功。Anthropic Engineering 页面归档成功但没有解析出有效文章卡片，状态为 `limited`，不能据此说当天没有文章。
- **X/Twitter**：通过公开 `twitterapi.io` API 请求 50 个账号，50/50 请求成功，读取 894 条原始记录，保留 271 条 `direct-x`。4 个账号返回 0 条原始记录，另有 8 个账号返回记录但没有条目通过主题筛选；这不等于账号没有更新，也不代表完整时间线。
- **播客 / 长对话**：follow-builders 公共 Feed 状态 `ok`，本轮 offered 1 集、allowed 1；inside/outside/unknown 为 0/1/0，transcript 和单集 canonical link 均为 `ok`，无上游错误。该 offered 数只代表中央 Feed 本轮实际提供的内容。

## 今日高信号

1. **Gemini 4 Carbon 开始面向开发者与企业提供。** Google DeepMind 官方文章称该模型进入付费 Gemini API，并面向 Google AI Ultra 用户逐步开放 Gemini、Search AI Mode 和 Antigravity；文章还介绍由 `/swarm` 协调智能体处理多文件任务。Every 的 Dan Shipper 另称 Carbon 在其 Senior Engineer benchmark 一次运行中得分 44%，Argon 为 21%，同时提醒长任务可能超出预定范围；这是团队的 `direct-x` 日零测试陈述，方法和结果未独立核验。[官方文章](https://deepmind.google/blog/gemini-4-carbon-is-now-available/) · [Dan Shipper 帖子](https://x.com/danshipper/status/2120187507396530309) · [本地正文](../raw/2026-11-11/rss-fulltext/google-deepmind-blog/google-deepmind-blog-gemini-4-carbon-is-now-available-0b2e1c02de.extracted.md)
2. **Microsoft Research 报告一种可能影响工具型智能体的模型权重后门。** 该研究称，少量休眠神经元可被改写成触发器，使正常通过常见评测的模型在触发条件出现后输出恶意命令；微软建议关注模型来源、权重完整性、权限限制和运行监测。文章是 Microsoft Research 的原始研究说明，AIHOT 是发现入口；结论归因于研究团队，不应理解为本轮对攻击效果的独立复测。[原文](https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/) · [本地正文](../raw/2026-11-11/rss-fulltext/aihot-selected/aihot-selected-microsoft-research-lazarus-ai-agent-1d554c42ba.extracted.md)
3. **OpenAI 将 ChatGPT 商家资料功能开放测试。** 企业可认领并验证资料、更新商品信息，并查看达到隐私门槛后的聚合提及、点击和发现主题；Business Agents 目前只面向美国符合条件的电商和在线服务企业。OpenAI 称不会向商家分享用户对话或 Business Agent 聊天；这不是所有商家都已开放的完整上线。官方文章是 `official-source`，配套官方账号帖子是 `direct-x`。[官方文章](https://openai.com/index/introducing-businesses-chatgpt/) · [官方账号帖子](https://x.com/OpenAI/status/2120216592395174382) · [本地正文](../raw/2026-11-11/official-link-candidates/openai-2120216592395174382-introducing-businesses-chatgpt.opencli.md)
4. **Anthropic 发布 Claude 工作空间工具，并为订阅用户增加一次用量重置。** 官方 Claude 账号称 Whiteboards、Sheets 和 Data 开始分批推出；ClaudeDevs 另称 Pro、Max、Ultra 与 Team 用户可在 12 月 10 日 PT 前领取一次跨模型的完整用量重置，原因是此前少数使用量计数问题。两项均为官方账号的 `direct-x` 公告，具体账号可用状态需以产品页面为准。[工作空间工具帖子](https://x.com/claudeai/status/2120206365759094857) · [用量重置原帖](https://x.com/ClaudeDevs/status/2120275296637321476) · [twitterapi.io 收到的转发](https://x.com/kloss_xyz/status/2120295720112840802)
5. **Box 与 Anthropic 宣布把企业文件读写接入 Claude。** Box CEO Aaron Levie 在 `direct-x` 帖子中称，智能体可通过 MCP 在 Box 内容中读取、创建和更新文档；这是公司负责人发布的合作信息，本轮未独立验证权限、部署范围或安全控制。[帖子](https://x.com/levie/status/2120261416733036905)
6. **OpenRouter 发布两项有限样本的模型调用成本与量化测试。** 单一 GitHub 任务测试中，Sonnet 5.5 输入 token 中位数为 CLI 1,421、skill 3,315、默认加载 46 个 MCP 工具 59,417；工具搜索将定义开销降下来，但完整任务成本会随模型变化。另一项对 Qwen3.8 27B 六个服务端点、240 道精确答案题的比较，量化模型得分为 98.3%–99.2%；两项结果均为 OpenRouter 自有测试，不能外推为普遍结论。[MCP / CLI / Skills 测试](https://openrouter.ai/blog/insights/mcp-vs-cli-vs-skills/) · [量化测试](https://openrouter.ai/blog/insights/llm-quantization/)
7. **Vercel 宣称其 Security Review 智能体已识别并修复大量漏洞。** CEO Guillermo Rauch 在 `direct-x` 帖子中称，该服务上线不到一周识别 57,897 项漏洞，其中 6,029 项为高危或严重级别，智能体已修复 14,665 项；本轮未取得配套审计报告，数字和修复范围仍是公司自报。[帖子](https://x.com/rauchg/status/2120188488628977819)
8. **Cursor Projects 宣布多人协作工作区。** 产品负责人 Matt Palmer 在 `direct-x` 帖子中称，团队可共享任务板与上下文，各自运行智能体，并让智能体直接向队友的智能体索取工作信息；本轮未验证实际权限和运行行为。[Matt Palmer 原帖](https://x.com/mattyp/status/2120307529674883177) · [twitterapi.io 收到的转发](https://x.com/kloss_xyz/status/2120312658264207598) · [本地转发记录](../raw/2026-11-11/twitterapi-io-results.json)
9. **Graphon 宣布企业多模态记忆产品。** 创始人在 `direct-x` 帖子中称，该系统可从通话、视频、图片、扫描件和聊天中建立可追溯记忆；融资金额和 ATM-Bench、LoCoMo 等分数是创始人自述，本轮没有读取独立评测或产品文档。[创始人原帖](https://x.com/graphonfounder/status/2120201264932003990) · [twitterapi.io 归档的转发](https://x.com/kloss_xyz/status/2120211037509337548) · [本地记录](../raw/2026-11-11/twitterapi-io-results.json)
10. **Fish Audio 发布 Live 3 全双工语音模型。** 联合创始人 Rissa Cao 的 `direct-x` 帖子将其描述为能在说话时继续听取输入的语音模型；EXM7777 转述称快速回应低于 200 毫秒，但没有配套测量材料，本轮未做音频或延迟测试。[Rissa Cao 原帖](https://x.com/rissa_cao/status/2120214987633467626) · [EXM7777 转述](https://x.com/EXM7777/status/2120217603423826356) · [本地引用记录](../raw/2026-11-11/twitterapi-io-results.json)

## 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- **OpenAI：ChatGPT 商家资料与 Business Agent 测试版。** [官方文章](https://openai.com/index/introducing-businesses-chatgpt/)称商家可以在 Business Hub 认领和验证资料、维护商品价格与库存，并查看达到阈值后的聚合互动指标；符合条件的美国电商与在线服务企业可建立 Business Agent。隐私和可用范围以文章说明为准。[本地全文](../raw/2026-11-11/official-link-candidates/openai-2120216592395174382-introducing-businesses-chatgpt.opencli.md)
- **OpenAI：Cyber at the Frontier 活动。** 官方账号称将于 11 月 12 日 10:00 PT 举办网络安全主题演讲，并介绍最新安全公告；关联活动页只读到活动标题、时间和简短介绍。关于 OpenAI 用前沿模型发现、修复自有代码和基础设施漏洞的内容来自该账号 `direct-x` 自述，本轮没有独立核验。[X 帖子](https://x.com/OpenAI/status/2120202353907486826) · [活动页](https://openai.com/cyber-at-the-frontier/) · [本地页面](../raw/2026-11-11/official-link-candidates/openai-2120202353907486826-cyber-at-the-frontier.opencli.md)
- **OpenAI Codex：5 条 release Atom 均为 `limited`。** Feed 只提供版本标签或短 changelog 片段，不能据此推断功能变化；见[原始条目](../raw/2026-11-11/github-items.json)及[正文归档](../raw/2026-11-11/github-release-fulltext/openai-codex/)。
- **Claude Code：Feed 最新 `v2.1.322` 于北京时间 11 月 10 日发布，正文受限。** Atom 摘要提到 Vertex 的 fast mode 在 global、us、eu 区域可用，Vertex 拒绝时回退到标准速度；它在本轮作为前一日背景，不算 11 月 11 日新发布。[官方 release](https://github.com/anthropics/claude-code/releases/tag/v2.1.322) · [本地片段](../raw/2026-11-11/github-release-fulltext/anthropics-claude-code/anthropics-claude-code-v2.1.322-f7d3d2f1a8.atom.md)。
- **Claude 增加三类工作空间工具。** 官方账号发布 Whiteboards、Sheets、Data 的分批推出说明，分别用于规划、追踪和数据讲述；这是 `direct-x` 公告，当前只确认官方公布开始 rollout。[官方账号帖子](https://x.com/claudeai/status/2120206365759094857)
- **ClaudeDev 提供一次临时用量重置。** 账号称所有 Pro、Max、Ultra、Team 用户可在 12 月 10 日 PT 前领取一次跨模型完整重置，以补偿部分用量统计问题；这只是一项官方 `direct-x` 公告，不等于持续提高用量上限。[原帖](https://x.com/ClaudeDevs/status/2120275296637321476) · [twitterapi.io 收到的转发](https://x.com/kloss_xyz/status/2120295720112840802)

### AIHOT 精选条目与原文核验

[AIHOT Feed 快照](../raw/2026-11-11/rss-feeds/aihot-selected.xml)保留了每条记录的站点 URL、GUID、原始链接与发布时间。下表列出本轮 10 条窗口内主题匹配项；Feed 的摘要是 `secondary-source`。表中说法按实际读取到的链接原文归因，X 网页通过公开 HTTP 读取，不视为 `twitterapi.io` 的 `direct-x` 记录。

| AIHOT 条目与 GUID | 链接原文与阅读结果 |
| --- | --- |
| [Gemini 4 Carbon 发布](https://aihot.news/items/w8cvkd1j2o1c3m8ikh8x2kpfx) · `w8cvkd1j2o1c3m8ikh8x2kpfx` | [Google DeepMind 原文](https://deepmind.google/blog/gemini-4-carbon-is-now-available/)已读；模型可用范围与产品信息见上文。[本地正文](../raw/2026-11-11/rss-fulltext/google-deepmind-blog/google-deepmind-blog-gemini-4-carbon-is-now-available-0b2e1c02de.extracted.md) |
| [Philipp Schmid 分享 Carbon 使用情况](https://aihot.news/items/o6jzg6bjiaufh8no2rf1tep7u) · `o6jzg6bjiaufh8no2rf1tep7u` | [X 原帖](https://x.com/_philschmid/status/2120186354537812452)称他用 7 份规划 PDF、206 张工程图，经 `/swarm` 生成交互式 3D 重建；这是 Google DeepMind 员工的个人演示叙述，不是受控测试。[本地正文](../raw/2026-11-11/rss-fulltext/aihot-selected/aihot-selected-gemini-4-carbon-gemini-api-ai-studio-antigravity-06061a39c3.extracted.md) |
| [Cursor 接入 Carbon](https://aihot.news/items/tk36lg7rqiq1i67rq0ce28yo8) · `tk36lg7rqiq1i67rq0ce28yo8` | [Cursor 原帖](https://x.com/cursor_ai/status/2120193584670580857)称 Carbon 在 high effort 的 CursorBench 得分为 60.4；这是 Cursor 自有评测陈述。[本地正文](../raw/2026-11-11/rss-fulltext/aihot-selected/aihot-selected-gemini-4-carbon-cursor-effort-cursorbench-74333549cd.extracted.md) |
| [Claude Fable 5.2 实测观察](https://aihot.news/items/uditkv6u7rrzmtj1nx7pxbgjj) · `uditkv6u7rrzmtj1nx7pxbgjj` | [公众号原文](https://mp.weixin.qq.com/s/zgBGhOsuh6Z_5Enmzos3rQ)主要是作者对审美和创作任务的主观比较及社区演示，不是控制变量的模型评测。[本地正文](../raw/2026-11-11/rss-fulltext/aihot-selected/aihot-selected-claude-fable-5.2-107391eae5.opencli.md) |
| [Microsoft Research Lazarus 研究](https://aihot.news/items/womexcn3n0ijhbehvhbsxxm4f) · `womexcn3n0ijhbehvhbsxxm4f` | [Microsoft Research 原文](https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/)已读；研究发现和防御建议归因于微软研究人员。[本地正文](../raw/2026-11-11/rss-fulltext/aihot-selected/aihot-selected-microsoft-research-lazarus-ai-agent-1d554c42ba.extracted.md) |
| [OpenAI Business 第三方登录](https://aihot.news/items/y4pcrys3ewo3xnx1j45mbpbfy) · `y4pcrys3ewo3xnx1j45mbpbfy` | [OpenAI Developers 原帖](https://x.com/OpenAIDevs/status/2120212596850663712)称 ChatGPT Business 可用于 Notion、v0 等第三方工具；可用范围及管理方式以该账号帖子为准，AIHOT 仍是发现链路。[本地正文](../raw/2026-11-11/rss-fulltext/aihot-selected/aihot-selected-openai-chatgpt-business-notion-v0-7709b88bda.extracted.md) |
| [OpenRouter MCP、CLI 与 Skills 成本测试](https://aihot.news/items/wkpj021rmg6sgthgj9zwevei4) · `wkpj021rmg6sgthgj9zwevei4` | [OpenRouter 原文](https://openrouter.ai/blog/insights/mcp-vs-cli-vs-skills/)比较一个 GitHub 任务与多种 MCP 工具数、CLI 和 skill；结果受模型、工具定义和任务限制。[本地正文](../raw/2026-11-11/rss-fulltext/aihot-selected/aihot-selected-openrouter-mcp-vs-cli-vs-skills-token-d23e225ff7.extracted.md) |
| [OpenRouter fp8 / fp4 量化测试](https://aihot.news/items/i3gp1xj4j11gi4qoreya18izb) · `i3gp1xj4j11gi4qoreya18izb` | [OpenRouter 原文](https://openrouter.ai/blog/insights/llm-quantization/)比较 Qwen3.8 27B 的 6 个 endpoint 和有限任务；结论不适用于未测模型或服务商。[本地正文](../raw/2026-11-11/rss-fulltext/aihot-selected/aihot-selected-openrouter-fp8-fp4-970af0a737.extracted.md) |
| [NVIDIA / Megaspeed 指控文章](https://aihot.news/items/gqzca7y2h3m9p0fxtj60m4i1t) · `gqzca7y2h3m9p0fxtj60m4i1t` | [Where’s Your Ed At 原文](https://www.wheresyoured.at/jensens-bizarre-adventure/)已读，但涉及出口管制销售、公司人员和调查的指控带有强烈评论与推测，本轮没有独立核验；不将标题指控写为事实，审计标为 `insufficient_evidence`。[本地正文](../raw/2026-11-11/rss-fulltext/aihot-selected/aihot-selected-ed-zitron-nvidia-megaspeed-gpu-2decbd9aef.extracted.md) |
| [Stripe 收购 OpenRouter 说法](https://aihot.news/items/zycmiklep7i6dct58558jbp78) · `zycmiklep7i6dct58558jbp78` | [链接的 X 原帖](https://x.com/OpenRouter/status/2120234542183395787)本地页面内容为 X 的 404 错误，不能支持收购说法；不把该说法当作事实，审计标为 `insufficient_evidence`。[本地页面](../raw/2026-11-11/rss-fulltext/aihot-selected/aihot-selected-stripe-openrouter-0e7a9526e5.extracted.md) |

另有 6 条窗口内 AIHOT 项目没有匹配配置主题，因此未抓原文；其余 34 条在目标日之外，未抓原文。所有 50 条均保留 AIHOT GUID 与站点条目 URL；AIHOT 仅是最新 50 条的有界发现来源。

### 主要主题摘要

- **基础模型与模型评测：** Gemini 4 Carbon 的产品开放范围以 Google DeepMind 原文为准；Google 和 Cursor 公布的安全、能力及榜单数据均为厂商陈述。Simon Willison 的 `llm-gemini 0.36` 记录了其 Gemini 使用方式，属于第三方工具更新和个人测试，不替代官方价格或模型说明。[本地文章](../raw/2026-11-11/rss-fulltext/simonwillison/simonwillison-llm-gemini-0.36-c1fbfe2e3f.extracted.md)
- **智能体安全与权限：** Microsoft Research 的 Lazarus 文章将权重来源、完整性和最小权限视作防御重点。另有 AIHOT 转发的 OpenAI Control Room 背景材料，官方文章介绍研究推理请求按 `job_id` 查授权，停止作业后拒绝后续采样，目标是最多 35 秒内停止输出；该文章日期为 10 月 29 日，配套帖子也在北京时间 11 月 10 日，不算本日更新，且仅适用于 OpenAI 研究基础设施。[官方文章](https://openai.com/index/control-room/) · [本地正文](../raw/2026-11-11/official-link-candidates/openai-2119913172039868579-control-room.opencli.md)
- **Claude 模型与编程工具：** Anthropic 的 Claude Fable 5.2 提示文档建议按自有评测校准 effort，并提醒长任务、审批、代码所有权和进度通知会受提示与 harness 影响。文档链接来自 11 月 10 日的帖子、页面没有可用发布日期，因此作为背景材料；其小型测试结果仅是 Anthropic 自报。[官方文档](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) · [本地全文](../raw/2026-11-11/official-link-candidates/simonw-2120029347948220500-prompting-claude-fable-5-2.extracted.md)
- **企业 AI 产品：** OpenAI 的 Business Hub 与 Business Agent 扩展 ChatGPT 中的商家资料、发现和咨询场景；官方文章对聚合指标设置阈值，并表示不会共享用户对话。第三方接入名单另来自 OpenAI Developers 帖子，二者不应合并成全部功能已普遍开放的判断。
- **企业文件与智能体：** Aaron Levie 称 Box 与 Anthropic 正提供 Claude 对 Box 内容的读写互通，并支持通过 MCP 创建、编辑和更新企业文件。这一消息来自负责人的 `direct-x` 陈述；访问审批、租户范围和实际部署仍需进一步验证。[帖子](https://x.com/levie/status/2120261416733036905)
- **多仓库 Agent 工作区：** Matt Pocock 分享把 skills、steering 文件和 wiki 放在单独 Home Repo，再用 `AGENTS.md` 指向多个项目仓库的个人做法。这是 `direct-x` 工作流经验，原帖没有展示仓库或量化效果。[帖子](https://x.com/mattpocockuk/status/2120260969750540327) · [本地 API 归档](../raw/2026-11-11/twitterapi-io-results.json)
- **AI 安全工具：** Vercel CEO 声称 Security Review 可扫描代码仓库并由智能体自动修复部分发现项。上述漏洞数量和修复量来自 `direct-x` 自述，未有本轮独立审计材料支持。[帖子](https://x.com/rauchg/status/2120188488628977819)
- **多智能体协作：** Cursor Projects 的公告描述共享任务板、共享上下文和智能体之间的工作请求；这是新产品能力声明，实际边界仍需用户权限和运行记录验证。[Matt Palmer 原帖](https://x.com/mattyp/status/2120307529674883177)
- **长期记忆：** Graphon 创始人称其产品从通话、视频、照片、扫描文件和聊天中提取可追溯的企业记忆，并报告多个记忆基准成绩。产品机制、融资与基准均是创始人发布的 `direct-x` 自述，不能当作独立评测结果。[创始人原帖](https://x.com/graphonfounder/status/2120201264932003990) · [本地 X 归档](../raw/2026-11-11/twitterapi-io-results.json)
- **实时语音：** Fish Audio 联合创始人以 `direct-x` 宣布 Live 3，并称其为全双工语音模型；转述帖提到的延迟数字未核验，也没有本轮运行测试。[创始人原帖](https://x.com/rissa_cao/status/2120214987633467626) · [本地 X 归档](../raw/2026-11-11/twitterapi-io-results.json)

### GitHub Trending 每日热门项目

GitHub Trending 当日解析 10 个项目，description 10/10、README 9/10。下面把页面描述与 README 合并为项目介绍；上榜和日增星数只说明发现度，不代表质量、使用效果或当日发布。

1. **[meta/astryx](https://github.com/meta/astryx)**（今日 +3,108 星）：面向 React 团队的设计系统，README 称其处于 Beta，基于 React 19+ 与 StyleX，提供 150 多个可访问组件、主题、模板和 CLI；使用者可导入预构建 CSS 和有类型的组件，需自定义时可导出源码。README 所称 Meta 内部覆盖 13,000 多个应用未经本轮核验。[本地 README](../raw/2026-11-11/github-trending-readmes/meta__astryx.md)
2. **[anthropics/skills](https://github.com/anthropics/skills)**（+1,679 星）：Anthropic 的 Claude skills 示例仓库，把任务说明、脚本和资源放在可动态载入的技能目录中，供 Claude Code、Claude API 或 Claude.ai 等宿主使用。README 明确它是示范与教学材料，不等同于 Agent Skills 标准本身，也不能假设所有宿主安装后行为相同。[本地 README](../raw/2026-11-11/github-trending-readmes/anthropics__skills.md)
3. **[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)**（+465 星）：面向 AI 编程代理的工程技能集合，将需求、计划、实现、测试和评审整理为 slash commands、技能、角色与检查清单，并支持通过 `npx skills add` 或宿主原生方式安装。它是作者维护的工作流包，“production-grade”是作者定位；跨宿主支持并不完全一致。[本地 README](../raw/2026-11-11/github-trending-readmes/addyosmani__agent-skills.md)
4. **[anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts)**（+531 星）：Claude API 开发者可从客服知识库、金融数据分析、浏览器/桌面使用、编码代理及 Slack、Linear、Sentry、MCP 等示例起步，通常按子项目安装依赖、设置 API key 后运行。它是示例集合，不是统一部署产品；README 说明浏览器使用示例不是生产代码。[本地 README](../raw/2026-11-11/github-trending-readmes/anthropics__claude-quickstarts.md)
5. **[google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)**（+456 星）：面向机器人、生物力学、图形与机器学习研究者的多关节物理模拟器，模拟关节结构与环境接触；README 描述 C API、XML 编译器预分配仿真数据、Python 绑定、Unity 插件和浏览器可视化。README 提醒主分支可能不稳定，浏览器 WebAssembly 版慢于原生版本，并说明该项目虽由 Google DeepMind 维护但不是 Google 官方支持产品。[本地 README](../raw/2026-11-11/github-trending-readmes/google-deepmind__mujoco.md)
6. **[we-promise/sure](https://github.com/we-promise/sure)**（+159 星）：个人财务与财富管理应用，是已停止维护的 Maybe Finance 项目的社区 fork；README 描述可自行托管，并提供网页、手机、API 和 AI 助手接入方式。财务记录、身份认证和 AI 数据访问涉及敏感信息，部署与访问控制仍需自行审查。[本地 README](../raw/2026-11-11/github-trending-readmes/we-promise__sure.md)
7. **[homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp)**（+790 星）：通过 MCP 把 Home Assistant 设备、自动化、仪表板、历史和配置管理能力提供给 Claude、ChatGPT 等助手；README 主推 HACS/Marketplace 进程内安装，也提供多种服务端部署和工具搜索。它可读写家庭设备与配置，管理员令牌、Webhook 和写入工具扩大风险；部分 YAML 写入处于 Beta，README 明确只读 URL 复用相同凭据，不是权限隔离。[本地 README](../raw/2026-11-11/github-trending-readmes/homeassistant-ai__ha-mcp.md)
8. **[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**（+780 星）：面向智能体的 Rust 浏览器自动化 CLI，通过后台进程和 Chrome DevTools Protocol 维持会话；`snapshot` 把页面转成带元素引用的紧凑无障碍树，代理按引用操作后重新读取页面确认状态。页面变化后引用会失效，必须重新 snapshot；README 描述的多浏览器与云端连接能力未经本轮运行验证。[本地 README](../raw/2026-11-11/github-trending-readmes/vercel-labs__agent-browser.md)
9. **[sherlock-project/sherlock](https://github.com/sherlock-project/sherlock)**（+2,393 星）：Trending description 只说它按用户名搜索社交平台账号。README 状态为 `missing`，没有正文可确认平台列表、匹配机制、误报或速率限制，因此只列为待读候选；最小下一步是恢复 README 后核对这些边界。
10. **[tokio-rs/topcoat](https://github.com/tokio-rs/topcoat)**（+192 星）：README 将它描述为 Rust 全栈 Web 框架，包含服务端渲染和将 Rust 表达式编译为浏览器 JavaScript 的响应式页面机制，也支持服务端局部刷新。项目明确处于早期阶段，可能发生破坏性变化；认证、后台任务、静态导出和部署文档仍在路线图中。[本地 README](../raw/2026-11-11/github-trending-readmes/tokio-rs__topcoat.md)

### X/Twitter 推主主题摘要

以下按 topic brief 的高分条目选取，时间覆盖本轮滚动窗口，包含北京时间 11 月 10 日的背景帖子。帖子均来自公开 `twitterapi.io` 读取并标为 `direct-x`；个人体验、转发、融资或性能陈述仍需独立核验。

| 主题 | 代表内容与证据边界 |
| --- | --- |
| LLM / 前沿模型 | [kloss_xyz](https://x.com/kloss_xyz/status/2120233739985006746) 讨论智能体应获准访问哪些对象，并称 Inkbox.ai 获 530 万美元融资；资金信息与产品机制未独立核验。 |
| AI Agent / 工作流 | [kloss_xyz](https://x.com/kloss_xyz/status/2120233739985006746) 的帖子把权限范围作为智能体产品问题；[OpenAI](https://x.com/OpenAI/status/2119913172039868579) 的 Control Room 帖子是北京时间 11 月 10 日的背景内容，范围限于 OpenAI 研究基础设施。 |
| AI 编程 / 开发工具 | [Aaron Levie](https://x.com/levie/status/2119987129204047894) 认为编程、计算机操作和行业理解会扩大可自动化场景；这是企业软件从业者观点，不是效果统计。 |
| AI 治理 / 公共合法性 | [OpenAI](https://x.com/OpenAI/status/2119913172039868579) 介绍研究工作负载停止控制；[Anthropic](https://x.com/AnthropicAI/status/2119867707546071125) 在前一北京时间日宣布 Fable 5.2 / Mythos 5.2。该主题的简报内容主要是公司产品消息，不代表公共治理证据。 |
| AI 基础设施 / 开源 | [OpenAI](https://x.com/OpenAI/status/2119913172039868579) 的研究负载控制说明是高分条目；另有 [EXM7777 转发 Hedra Model Factory](https://x.com/EXM7777/status/2120208591168676303)，转发内容没有本轮独立验证。 |
| 独立创业 | [kloss_xyz](https://x.com/kloss_xyz/status/2120233739985006746) 提及 Inkbox.ai 融资；[Marc Lou](https://x.com/marclou/status/2120155404957311464) 宣布由其发起的 10 万美元创业黑客松。均为发帖者陈述，不构成商业结果验证。 |
| 产品 / 增长 | [Aaron Levie](https://x.com/levie/status/2119987129204047894) 分享对垂直自动化的观点；[Marc Lou](https://x.com/marclou/status/2120155404957311464) 分享创业活动方案，营销效果未知。 |
| AI 系统 / 自动化 | [kloss_xyz](https://x.com/kloss_xyz/status/2120233739985006746) 谈智能体的访问控制；[Peter Steinberger](https://x.com/steipete/status/2120228665946710248) 转述漏洞排查经历，数字和事件未独立核验。 |
| FDE / 企业 AI 部署 | 本轮 topic brief 没有匹配条目；这表示简报未选出内容，不证明该领域没有更新。 |

### 播客 / 长对话

follow-builders 本轮 **offered 1 集**，节目为 Latent Space，标题为“**What Frontier Labs Buy: A Data Deep Dive with Handshake AI — Garrett Lord & Team**”，GUID 为 `01a1c0f3-0e12-72e9-b44b-8ca8a4fe611d`。发布时间为 `2026-11-09T16:41:48Z`，即北京时间 11 月 10 日 00:41:48，属于目标日之外；因此 inside=0、outside=1、unknown=0。本轮没有窗口内 transcript，不生成内容洞察卡，也不能把 offered 1 集解释为所有节目均无更新。

Feed 快照与 transcript 已归档，transcript 状态 `ok`、canonical 单集链接状态 `ok`；上游 YouTube URL 是频道别名，本地采集器通过 GUID 与节目 RSS 精确匹配到单集页。该聚合 transcript 未标出 speaker 或 timestamp（两项覆盖均为 false），未做音频复核，证据等级固定为 `secondary-source`。

- [canonical 单集链接](https://lspace.beehiiv.com/podcast/s/latent_space_the_ai_engineer_podcast/what_frontier_labs_buy_a_data_deep_dive_with_handshake_ai_garrett_lord_team) · [上游频道别名](https://www.youtube.com/@LatentSpacePod)
- [本地 transcript](../raw/2026-11-11/podcasts/follow-builders/transcripts/what-frontier-labs-buy-a-data-deep-dive-with-handshake-ai-garrett-lord-amp-team-fba56ad73529.md)
- [follow-builders Feed 快照](../raw/2026-11-11/podcasts/follow-builders/feed-podcasts.json) · [播客状态与覆盖 JSON](../raw/2026-11-11/podcast-items.json)

## 来源证据表

| 来源 | 本轮覆盖 | 证据与边界 |
| --- | --- | --- |
| RSS / Atom | 33/33 源成功；58/58 匹配或一手重点正文可读 | `dwarkesh-patel` 等本轮无失败源；具体条目以 [RSS 原始归档](../raw/2026-11-11/rss-items.json) 为准。 |
| AIHOT 精选 RSS | 最新 50 条；16 条在目标日，10 条主题匹配且 10/10 原文可读，6 条不相关跳过；34 条窗口外 | AIHOT 标题/摘要保留为 `secondary-source`，记录 station URL、GUID、Feed 快照与原始链接。[Feed 快照](../raw/2026-11-11/rss-feeds/aihot-selected.xml) · [条目状态](../raw/2026-11-11/rss-items.json) |
| GitHub Releases | 7/7 feed；一手重点正文 4/10 可读、6/10 `limited` | Codex 五条和 Claude Code 最新一条只有短片段；GitHub API `skipped`，使用 Atom。[原始条目](../raw/2026-11-11/github-items.json) |
| GitHub Trending | 10 个 repo、description 10/10、README 9/10 | `sherlock-project/sherlock` README 缺失；上榜仅是 `secondary-source` 发现信号。[项目状态](../raw/2026-11-11/github-trending.json) |
| 官方页面 | 4/5 成功；Anthropic Engineering 解析 0 张有效卡片并标记 `limited` | 0 卡片不代表当天没有文章。[归档](../raw/2026-11-11/official-pages.json) |
| X/Twitter | `twitterapi.io` 50/50 账号请求成功；894 条原始记录、271 条保留为 `direct-x` | 公开 API 读取；不承诺完整时间线，也不把零返回解释为无更新。[API 原始结果](../raw/2026-11-11/twitterapi-io-results.json) · [主题简报](../raw/2026-11-11/twitter-topic-brief.json) |
| follow-builders 播客 | 状态 `ok`；offered/allowed/inside/outside/unknown = 1/1/0/1/0；transcript/link = 1/1 ok | 单集在窗口外；中央 Feed offered 不等于逐节目覆盖，transcript 是未做音频复核的二手材料。[播客状态](../raw/2026-11-11/podcast-items.json) · [Feed 快照](../raw/2026-11-11/podcasts/follow-builders/feed-podcasts.json) |

## X/Twitter 覆盖说明

本轮只通过公开 `twitterapi.io` 读取接口抓取配置账号，50/50 请求成功，894 条原始记录中 271 条进入主题简报并标为 `direct-x`。其中 `rryssf_`、`Yangyixxxx`、`zhaogua61654931`、`lidang` 返回 0 条原始记录；另有 8 个账号有返回但筛选后为 0 条。账号返回受 API 窗口、分页和主题筛选影响，不能据此断言其没有发帖。本轮没有使用登录态 X 浏览、Exa 或写入/互动接口。

## 不确定性与待验证项

- Anthropic Engineering index 抓取成功但没有有效文章卡片，状态 `limited`；需要后续重新确认解析能力，不能把它写成零更新。
- AIHOT 只提供最新 50 条。本轮 10 条匹配项均成功读取原始链接，但 Feed 标题和摘要仍是二手发现证据；NVIDIA / Megaspeed 指控未独立核验，Stripe 收购 OpenRouter 的 X 链接只返回 404，二者不作为事实。
- OpenAI Codex 5/5、Claude Code 最新 `v2.1.322` 的发布正文受限；仅按版本标签和短 Atom 摘要说明，不推断未显示的改动。
- GitHub Trending 的 Sherlock README 缺失，不能写机制总结；其余 9 份 README 只支持对项目自述机制的归纳，不代表实测。
- Google、Cursor、OpenRouter 的模型能力、榜单、成本和量化数字来自各自发布者或有限样本测试；需要更广样本或独立复现。
- 5 个官方链接候选均有本地正文：OpenAI Business 与 Cyber 活动的官方 X 帖子在北京时间 11 月 11 日；Control Room、Claude Fable 5.2 提示文档和 Anthropic IPO roadshow 的链接帖子在北京时间 11 月 10 日，作为背景而非当日新增。Anthropic roadshow 页面仍表示 SEC 注册文件尚未生效，不能写成 IPO 已完成；Claude 提示文档没有可用发布日期，效果数字是 Anthropic 自报测试。
- 播客只报告 follow-builders 本轮实际 offered 1 集；该集窗口外，transcript 无 speaker/timestamp 标注且未做音频复核。它不能证明其他节目没有更新。
- X/Twitter 的 API 账号请求成功不等于获取完整历史；零原始记录与零主题匹配分别保留为覆盖边界。

## 当天产物

- [运行汇总](../raw/2026-11-11/run-summary.json) · [状态 manifest](../raw/2026-11-11/manifest.json) · [signals](../raw/2026-11-11/signals.json) · [阅读清单](../raw/2026-11-11/report-reading-list.json)
- [RSS / AIHOT 原始条目](../raw/2026-11-11/rss-items.json) · [AIHOT Feed 快照](../raw/2026-11-11/rss-feeds/aihot-selected.xml) · [GitHub Releases](../raw/2026-11-11/github-items.json) · [GitHub Trending](../raw/2026-11-11/github-trending.json) · [官方页面](../raw/2026-11-11/official-pages.json)
- [播客条目](../raw/2026-11-11/podcast-items.json) · [follow-builders 完整 Feed 快照](../raw/2026-11-11/podcasts/follow-builders/feed-podcasts.json) · [本地 transcript](../raw/2026-11-11/podcasts/follow-builders/transcripts/what-frontier-labs-buy-a-data-deep-dive-with-handshake-ai-garrett-lord-amp-team-fba56ad73529.md)
- [X/Twitter API 结果](../raw/2026-11-11/twitterapi-io-results.json) · [推主主题简报](../raw/2026-11-11/twitter-topic-brief.json) · [官方链接候选与正文目录](../raw/2026-11-11/official-link-candidates.json) · [候选审计](../reviews/2026-11-11-candidate-audit.json)
- [GitHub Trending README 归档目录](../raw/2026-11-11/github-trending-readmes/) · [release 正文归档目录](../raw/2026-11-11/github-release-fulltext/)

## 边界与验证

本报告区分原始页面、AIHOT 二手发现、公开 X 结构化记录、README 自述和 API 窗口边界。候选审计共 140 条，31 条由正文覆盖，109 条均有明确处置；严格报告校验通过。README 缺失、release `limited`、Anthropic Engineering 解析受限、AIHOT 窗口边界和播客 outside 状态均按实际状态记录。
