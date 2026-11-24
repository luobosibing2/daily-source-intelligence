# 每日情报｜2026-11-25

## 直接答案

本轮有 **4 条高信号**：OpenAI 报告 GPT-6 系列蛋白设计实验结果；两位业余天文学家使用 Codex 与 Astra 从公开望远镜数据中筛出待核查信号；Claude Code 团队成员称 MCP 服务器现在可以随附技能；ChatGPT 开始向少量 Pro 用户试行 Chat 与 Work 合并体验。前两项分别有 OpenAI 研究文章和官方 X 帖子支撑，但实验结果仍有明确边界；后两项目前只有 `direct-x` 产品消息，未在本轮实测。

统一采集与状态准备新增 **49 条去重记录**。正文阅读清单有 20 项：8 项有可读本地正文，12 项是 X 结构化记录或受限正文边界。follow-builders 本轮状态 `ok`，上游 feed offered 0 集；feed 文件有效且为空，不代表所有已配置节目都没有更新。[manifest](../raw/2026-11-25/manifest.json) · [run summary](../raw/2026-11-25/run-summary.json) · [正文阅读清单](../raw/2026-11-25/report-reading-list.json) · [播客状态](../raw/2026-11-25/podcast-items.json)

## 采集范围

- 运行日期为 `2026-11-25`（Asia/Shanghai）。使用完整统一入口 `DAILY_INTEL_OPENCLI_PROFILE=t26bdsv2 python3 scripts/dsi.py run --date 2026-11-25`，采集与状态准备均成功。[运行摘要](../raw/2026-11-25/run-summary.json)
- 普通 RSS/Atom：33 个源中 32 个成功；50/50 条主题匹配或一手重点正文可读，另 155 条按规则跳过。`dwarkesh-patel` 解析失败，错误为 `junk after document element: line 1, column 48`。[RSS 条目](../raw/2026-11-25/rss-items.json)
- AIHOT 精选：本轮读取最新 50 条；北京时间窗口内/窗外/时间未知为 4/46/0。4 条窗口内记录中，3 条匹配主题并读取了链接原始页面，正文均为 `ok`；1 条不相关，未读取原文。50 条都有 feed 发布时间和原始链接。AIHOT 是有界二手发现源；条目保留 GUID、AIHOT 站内页、原始链接与 feed 快照。[RSS 记录](../raw/2026-11-25/rss-items.json) · [AIHOT feed 快照](../raw/2026-11-25/rss-feeds/aihot-selected.xml)
- GitHub Releases：7/7 个 Atom 源成功；Codex 与 Claude Code 一手重点正文共尝试 10 条，6 条可读、4 条受限。4 条受限项是 Codex Atom 正文仅含版本标签。[发布记录](../raw/2026-11-25/github-items.json) · [正文归档](../raw/2026-11-25/github-release-fulltext/)
- GitHub Trending：解析 10 个项目，Trending 描述与 README 均为 10/10 可读。榜单和 README 只作为项目发现证据，没有运行或独立验证项目。[Trending 记录](../raw/2026-11-25/github-trending.json) · [README 归档](../raw/2026-11-25/github-trending-readmes/)
- 官方页面：5 个来源中 4 个成功、1 个受限。Anthropic Engineering 索引只抓到页面，未解析出文章卡片；这不能证明该站当天没有文章。[页面记录](../raw/2026-11-25/official-pages.json)
- X/Twitter：`twitterapi.io` 的 50 个账号均成功请求，收到 848 条原始帖子，筛选保留 221 条 `direct-x`（来源接口覆盖 36 小时）；其中 49 条落在本地 11 月 25 日窗口。主题 brief 按配置主题整理代表帖子；本轮没有登录态浏览器、Exa 或写入操作。[API 结果](../raw/2026-11-25/twitterapi-io-results.json) · [推主主题摘要](../raw/2026-11-25/twitter-topic-brief.json)
- 播客 / 长对话：follow-builders HTTP 200、状态 `ok`、上游错误 0；offered/inside/outside/unknown 为 0/0/0/0，transcript `ok/limited` 为 0/0，单集链接 `ok/limited` 为 0/0。原始 feed 更新时间为 `2026-11-24T06:30:05.159Z`，快照中的 `podcasts` 为空；没有单集 transcript。[播客状态](../raw/2026-11-25/podcast-items.json) · [feed 快照](../raw/2026-11-25/podcasts/follow-builders/feed-podcasts.json)

## 今日高信号

1. **GPT-6 系列展示蛋白结构与序列设计能力的早期实验结果。** OpenAI 文章报告，在 5 个靶点的 322 个候选 minibinder 中有 35 个观察到结合；对 107 条新序列的另一组实验中有 14 条结合。论文仍依赖专用模型完成部分序列生成与候选筛选；“结合”不等于生物功能、疗效或安全，结果也没有证明端到端零样本设计。[OpenAI 研究文章](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) · [本地全文](../raw/2026-11-25/official-link-candidates/openai-2125334383490105601-gpt-6-models-demonstrate-intrinsic-protein-design-capabilities.opencli.md) · [论文发现记录](https://aihot.news/items/vld1kqsp7wkz3o3qo1ubc9sg9)
2. **Codex 与 Astra 帮助天文爱好者筛查公开望远镜数据。** OpenAI 文章称，两位业余研究者从 Kepler 与 TESS 数据中提出待跟进候选信号；另一位 SETI 研究者独立找到相同的两个候选。它们仍是候选信号，不是新行星的确认结果。[OpenAI 文章](https://openai.com/index/searching-for-distant-planets-with-astra/) · [当日 OpenAI 帖子](https://x.com/OpenAI/status/2125305606685053416) · [本地全文](../raw/2026-11-25/rss-fulltext/openai-blog/openai-blog-searching-for-distant-planets-with-astra-f3aa9260f1.opencli.md)
3. **Claude Code 的 MCP 服务器可随附技能。** Boris Cherny 的帖子称，MCP 服务器现在可以打包自身技能，让 Claude Code 安装后即知道如何使用。帖子是 `direct-x` 产品信息，本轮没有对应文档、权限检查或运行验证。[Boris Cherny 帖子](https://x.com/bcherny/status/2125292098165612585)
4. **ChatGPT 开始小范围试行 Chat 与 Work 合并体验。** Thibault Sottiaux 表示会先向少量 Pro 用户开放，以收集反馈后再扩大范围；帖子没有说明具体功能、权限或后续开放时间。[Thibault Sottiaux 帖子](https://x.com/thsottiaux/status/2125284868414394550)

<!-- dsi-candidate-audit: covered=20 missed=80 -->

## 按主题分组摘要

### 一手重点源 / OpenAI 与 Claude Code

- **OpenAI 官方博客：**5 条博客 feed 项均早于本地 11 月 25 日窗口。11 月 24 日的《Searching for distant planets with Astra》当日另有 OpenAI 官方 X 帖子，因此已列入今日高信号；文章中的行星线索仍是候选。另两篇客户案例《How Intentful uses dots to make more time for growth》和《How iFood scales coding agents across 15,000 repositories》报告了单一客户的自动化经验，未作独立测量：iFood 案例自述覆盖 15,000 多个仓库、完成 25,000 多次运行，平均每次约 0.04 美元。11 月 23 日的 Shirudo 文章描述用 eBPF 在服务运行时部署临时防护；法律团队活动页仅有简短议程摘要，不能当作完整演讲或运行结果。[RSS 条目](../raw/2026-11-25/rss-items.json) · [OpenAI 正文目录](../raw/2026-11-25/rss-fulltext/openai-blog/)
- **Codex 与 Claude Code：**当日可读的 Claude Code release notes 共 5 条，最新 `v2.1.331` 更新时间为 11 月 23 日 UTC，早于本地日期窗口。Codex 的 `0.174.0-alpha.2` 与 `0.174.0-alpha.3` 更新时间落在本地 11 月 25 日，但 Atom 正文只有版本标签；另有 2 条 Codex 正文受限，总计 4/10 条受限。不能从这些版本标签推断功能变化。[GitHub 记录](../raw/2026-11-25/github-items.json) · [Codex 正文目录](../raw/2026-11-25/github-release-fulltext/openai-codex/) · [Claude Code 正文目录](../raw/2026-11-25/github-release-fulltext/anthropics-claude-code/)
- **其他 OpenAI 链接候选：**OpenAI 与 Cisco 的 Shirudo 页面写有 11 月 23 日日期，描述 eBPF 临时防护方案和受控演示；OpenWorks 页面只有 Sign Badgers 一个客户案例；《A Thousand Fewer Paths to Root》正文日期为 11 月 4 日，X 候选抓取元数据与正文日期不一致。这些均不能当作 11 月 25 日新发布。[候选记录](../raw/2026-11-25/official-link-candidates.json) · [Shirudo 正文](../raw/2026-11-25/official-link-candidates/openai-2124980590717911527-introducing-shirudo.opencli.md) · [OpenWorks 正文](../raw/2026-11-25/official-link-candidates/openai-2124922133545714160-openworks.opencli.md) · [Linux 漏洞研究正文](../raw/2026-11-25/official-link-candidates/openai-2125007927098699827-a-thousand-fewer-paths-to-root.opencli.md)

### 大模型、智能体与应用

- **Google Workspace MCP 与 `gwscli`：**AIHOT 最新 50 条中，GUID `nm8mi41auemid3iivue4tel3d` 的窗口内条目指向 Philipp Schmid 的 X 帖子。帖子称个人模式无需企业计划、含 8 个 Workspace 产品服务器、每个产品每日 5,000 次请求，并称发送或分享需要人工确认。这些细节来自 AIHOT 发现的公开 X 内容，按 `secondary-source` 记录；本轮没有读取或核对 Google 官方文档。[AIHOT 站内项](https://aihot.news/items/nm8mi41auemid3iivue4tel3d) · [原始 X 帖子](https://x.com/_philschmid/status/2125296446459056156) · [本地页面快照](../raw/2026-11-25/rss-fulltext/aihot-selected/aihot-selected-google-workspace-mcp-servers-gwscli-personal-ba1740ee44.extracted.md)
- **GPT-6.2 Astra 的历史研究案例：**Simon Willison 与 AIHOT 都转述历史学者 Mark Humphries 关于一册 1808 年匿名素描本作者线索的案例；Humphries 称 GPT-6.2 Astra 约 22 分钟内找到一条可继续调查的档案线索。两篇材料讲的是同一事件，不构成独立复核；没有完整可复现轨迹，仍属 `secondary-source`。[Simon Willison 文章](https://simonwillison.net/2026/Nov/24/astra-historical-mystery/) · [AIHOT 站内项](https://aihot.news/items/eb9lfibaf8fpouyw0x3vh63st) · [原始 X 帖子](https://x.com/gdb/status/2125305172721320165) · [本地 AIHOT 正文](../raw/2026-11-25/rss-fulltext/aihot-selected/aihot-selected-gpt-6.2-astra-22-1808-84fff7ad88.extracted.md)
- **蛋白质设计论文的发现链：**AIHOT GUID `vld1kqsp7wkz3o3qo1ubc9sg9` 在北京时间窗口内指向 OpenAI 的 X 帖子，feed 时间为 `2026-11-25 05:02:58 +08:00`。AIHOT X 快照仍是 `secondary-source`；实验数字和限制以已读取的 OpenAI 原文为依据。[AIHOT 站内项](https://aihot.news/items/vld1kqsp7wkz3o3qo1ubc9sg9) · [OpenAI 原文](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) · [本地 AIHOT 正文](../raw/2026-11-25/rss-fulltext/aihot-selected/aihot-selected-openai-preprint-gpt-6-987066bdf5.extracted.md)

### GitHub Trending 项目

本轮 10 个项目的 Trending 描述与 README 均可读。下面的用途来自 README；热度只表示发现信号，不证明质量、采用率、效果或安全性。本轮没有安装或运行项目。

- [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) 为 Claude Code 提供漏洞侦察、排序、测试和报告技能，覆盖外部 Web/API 与企业身份系统等场景。README 自述包含 84 项技能和授权范围检查；只能用于自有资产或明确获授权的目标，实际测试效果未验证。[README](../raw/2026-11-25/github-trending-readmes/elementalsouls__Claude-BugHunter.md)
- [obra/superpowers](https://github.com/obra/superpowers) 把需求澄清、设计确认、工作区隔离、分步计划、测试驱动开发、审查与收尾组织成编程 Agent 技能流程。README 说明需按宿主分别安装；实际遵循程度取决于宿主行为。[README](../raw/2026-11-25/github-trending-readmes/obra__superpowers.md)
- [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) 从软件源码为现有桌面或专业软件生成 Agent 可调用的 CLI，再用 CLI-Hub 管理。README 描述七阶段流程、JSON 输出和测试；生成结果仍依赖模型与目标软件本机安装情况。[README](../raw/2026-11-25/github-trending-readmes/HKUDS__CLI-Anything.md)
- [jingyaogong/minimind](https://github.com/jingyaogong/minimind) 用 PyTorch 教学小型语言模型的预训练、微调、LoRA、强化学习、工具调用与评测。README 明确指出小模型事实知识和泛化有限，示例能力不代表生产水平。[README](../raw/2026-11-25/github-trending-readmes/jingyaogong__minimind.md)
- [cursor/plugins](https://github.com/cursor/plugins) 是 Cursor 官方插件仓库，插件可携带技能、规则和 MCP 配置，覆盖开发及多类 SaaS 工作流。部分插件能发消息、更新记录、发布或预订；部署前需要逐个核对权限与副作用。[README](../raw/2026-11-25/github-trending-readmes/cursor__plugins.md)
- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) 提供网页抓取、爬取、站点映射和结构化提取，可本地运行或自托管。README 说明本地抓取失败时可能回退到云端；敏感资料要核对路由，且须遵守 robots.txt 和站点条款。[README](../raw/2026-11-25/github-trending-readmes/firecrawl__firecrawl.md)
- [nginx/nginx](https://github.com/nginx/nginx) 是 Web 服务器，也可作反向代理、负载均衡器、API 网关与缓存系统。它进入当日榜单，但 README 未显示新的 AI 功能或当日版本变化。[README](../raw/2026-11-25/github-trending-readmes/nginx__nginx.md)
- [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) 用于模型转换、推理优化和部署，支持多个模型框架及 Intel CPU、GPU、NPU 场景。具体兼容性与性能需要按模型和硬件重测；README 还描述了可选择退出的遥测。[README](../raw/2026-11-25/github-trending-readmes/openvinotoolkit__openvino.md)
- [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) 是将描述转为 HTML/SVG 图表的 Agent Skill，也能导入多个既有图表格式后重绘。README 提供保真记录以追踪合并或省略的结构；生成质量需人工复核，持续用 Git 比较的图表仍建议 Mermaid。[README](../raw/2026-11-25/github-trending-readmes/cathrynlavery__diagram-design.md)
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) 并行检索多种公开来源，按相关性、时间与互动排序并生成带来源的近期简报。部分来源需要 API 密钥、CLI 或浏览器会话；启用推理 API 会把主题和内容片段发送给模型提供方，`--publish` 会公开生成内容。[README](../raw/2026-11-25/github-trending-readmes/mvanhorn__last30days-skill.md)

### X/Twitter 推主主题摘要

以下仅列本地 11 月 25 日窗口中的代表帖子；每条为 `direct-x`。未检出代表项的主题明确标出。主题标签是配置匹配结果，不等于对内容的独立判断。

| 主题 | 代表帖子 | 边界 |
|---|---|---|
| 大模型 / 前沿模型 | [OpenAI：蛋白质设计预印本](https://x.com/OpenAI/status/2125334383490105601) · [OpenAI：Astra 搜索候选行星信号](https://x.com/OpenAI/status/2125305606685053416) · [kloss_xyz：Astra 生成单文件 HTML 场景的个人演示](https://x.com/kloss_xyz/status/2125293653195415776) | 官方研究按文章边界表述；HTML 场景是个人发帖者的使用经验，未复现。 |
| 智能体 / 智能体工作流 | [Boris Cherny：MCP 服务器可附带技能](https://x.com/bcherny/status/2125292098165612585) · [Thibault Sottiaux：Chat 与 Work 向少量 Pro 用户试行合并体验](https://x.com/thsottiaux/status/2125284868414394550) · [OpenAI：Astra 搜索候选信号](https://x.com/OpenAI/status/2125305606685053416) | 产品信息来自帖子；未做运行验证。 |
| AI 编码 / 开发工具 | [Boris Cherny：Claude Code 使用服务器随附技能](https://x.com/bcherny/status/2125292098165612585) · [OpenAI：使用 Codex 与 Astra 分析公开数据](https://x.com/OpenAI/status/2125305606685053416) · [kloss_xyz：Astra 单文件 HTML 场景演示](https://x.com/kloss_xyz/status/2125293653195415776) | OpenAI 帖子链接到官方文章；其他产品行为与生成结果未在本轮核验。 |
| AI 治理 / 公共合法性 | 本日匹配项主要是模型与产品消息，没有形成治理结论。 | 主题标签匹配不等于治理内容。 |
| AI 基础设施 / 开源 | 本窗口的主题 brief 无代表帖子。 | 36 小时接口仍有其他条目；此处不据此判断该领域没有更新。 |
| 独立开发 / 单人创业 | [levelsio：关于其账号遭攻击与举报的个人陈述](https://x.com/levelsio/status/2125308828011131033) | `direct-x` 仅证明发帖者陈述，不是平台侧调查结果。 |
| 产品 / 增长 / 市场进入 | [Thibault Sottiaux：ChatGPT Business 的 reset 与 fast mode 优惠至 12 月 31 日](https://x.com/thsottiaux/status/2125299248782778588) · [EXM7777：分享其多来源研究技能](https://x.com/EXM7777/status/2125260960441290974) | 优惠条件以帖子为限；个人研究流程未复现。 |
| AI 系统 / 自动化 | [kloss_xyz：提醒检查 Claude Artifacts 桌面应用权限](https://x.com/kloss_xyz/status/2125321109969174590) · [Amjad Masad：智能体形态变化与算力需求的个人判断](https://x.com/amasad/status/2125287538911072753) · [kloss_xyz 转发 Grok Bot 本机远程执行演示](https://x.com/kloss_xyz/status/2125268499115425801) | 权限说法和算力判断均是发帖者观点；转帖中的执行行为未验证。 |
| 前沿部署工程 / 企业 AI 部署 | 本窗口没有代表帖子。 | 不从窗口内缺少匹配项推断行业无更新。 |

完整主题记录见[推主主题摘要](../raw/2026-11-25/twitter-topic-brief.json)。帖子窗口与去重规则会影响保留项；未保留不能解释为账号没有更新，也不代表完整时间线。

### 播客 / 长对话

follow-builders 上游状态为 `ok`，本轮 offered 0 集，窗口内/窗外/未知均为 0；transcript 与单集链接均为 `0 ok / 0 limited`，上游错误为 0。feed HTTP 200，生成时间为 `2026-11-24T06:30:05.159Z`，本地快照有效但 `podcasts` 数组为空；没有可读的窗口内转录，因此没有播客洞察卡。该数量只描述中央 feed 实际提供的内容，不代表所有已配置节目均无更新。该渠道属于二手聚合源。[podcast-items.json](../raw/2026-11-25/podcast-items.json) · [feed 快照](../raw/2026-11-25/podcasts/follow-builders/feed-podcasts.json)

## 来源证据表

| 来源 | 本轮状态与数量 | 证据与限制 | 本地材料 |
|---|---|---|---|
| 普通 RSS/Atom | 33 源中 32 成功；50/50 命中或一手重点正文可读；155 条跳过 | `dwarkesh-patel` 解析失败；成功源不补足该源覆盖。 | [RSS 条目](../raw/2026-11-25/rss-items.json) |
| AIHOT 精选 | 最新 50 条；窗口内/窗外/未知 4/46/0；主题匹配 3 条，正文 3/3 `ok` | 二手发现。4 条窗口内记录均有发布时间和原始链接；1 条不相关未读原文，46 条窗外未读原文。 | [RSS 记录](../raw/2026-11-25/rss-items.json) · [feed 快照](../raw/2026-11-25/rss-feeds/aihot-selected.xml) |
| GitHub Releases | 7/7 Atom 源成功；一手重点正文 6/10 可读、4/10 受限 | 受限 Codex 条目只有版本标签；Claude Code 的 5 条可读版本记录均不在本地日期窗口。 | [发布记录](../raw/2026-11-25/github-items.json) · [正文目录](../raw/2026-11-25/github-release-fulltext/) |
| GitHub Trending | 10 个项目，10/10 描述与 README 可读 | `secondary-source` 发现信号；没有运行项目或验证 README 自述。 | [Trending 记录](../raw/2026-11-25/github-trending.json) · [README 目录](../raw/2026-11-25/github-trending-readmes/) |
| 官方页面 | 4/5 成功；Anthropic Engineering `limited`，0 张文章卡片 | 未解析到文章不等于该站没有更新；OpenAI News 可读内容也只有短索引文本。 | [页面记录](../raw/2026-11-25/official-pages.json) |
| X 官方链接候选 | 4 个 OpenAI 链接均归档可读 | 链接页面的实际日期不一；Shirudo 与 root 研究的抓取元数据和正文日期有冲突，OpenWorks 无发布日期。 | [候选记录](../raw/2026-11-25/official-link-candidates.json) · [归档目录](../raw/2026-11-25/official-link-candidates/) |
| X/Twitter API | 50/50 账号成功；848 原始、221 保留；49 条保留推文在本地日期窗口 | 仅公开只读 `twitterapi.io` 数据；不是完整时间线。 | [API 结果](../raw/2026-11-25/twitterapi-io-results.json) · [主题摘要](../raw/2026-11-25/twitter-topic-brief.json) |
| follow-builders 播客 | `ok`；offered/inside/outside/unknown 0/0/0/0；transcript 与链接均 0/0；错误 0 | 有效空 feed；没有 transcript，不代表全部配置节目无更新。材料属于聚合二手来源。 | [播客状态](../raw/2026-11-25/podcast-items.json) · [feed 快照](../raw/2026-11-25/podcasts/follow-builders/feed-podcasts.json) |

## X/Twitter 覆盖说明

`twitterapi.io` 按配置请求 50 个账号，全部成功。接口在 36 小时范围收到 848 条原始帖子，保留 221 条；其中 49 条落在本地 11 月 25 日日期窗口。主题 brief 与正文阅读清单对代表帖子再次筛选，因此各数值口径不同。未保留的帖子不能解释为账号无更新，本轮也不承诺覆盖完整时间线。只使用公开读取数据，没有使用登录态浏览器、Exa 或 X 写操作。[API 结果](../raw/2026-11-25/twitterapi-io-results.json) · [主题 brief](../raw/2026-11-25/twitter-topic-brief.json)

## 不确定性与待验证项

- `dwarkesh-patel` RSS 连续 24 次失败；本次错误为 XML 根元素之后仍有内容。其余 32 个 RSS 源成功不能替代该源的本轮覆盖。[RSS 条目](../raw/2026-11-25/rss-items.json)
- AIHOT 只返回当前 feed 最新 50 条，是有界二手发现。样本中 46 条窗外、4 条窗口内；3 条匹配原文并完成读取，1 条因主题不相关跳过。没有缺失发布时间或原始链接，但这不表示完整 AI 新闻覆盖。[AIHOT feed 快照](../raw/2026-11-25/rss-feeds/aihot-selected.xml) · [条目记录](../raw/2026-11-25/rss-items.json)
- Google Workspace MCP 与 `gwscli` 的个人模式、配额及人工确认细节来自 AIHOT 链接到的 X 帖子，尚未核对 Google 官方文档；AIHOT 站内标题与摘要不作为原始官方证据。[AIHOT 站内项](https://aihot.news/items/nm8mi41auemid3iivue4tel3d) · [原始 X 帖子](https://x.com/_philschmid/status/2125296446459056156)
- 两条 Codex 窗口内 release 只有版本标签，不能据此推断功能。Anthropic Engineering 索引只解析到页面、没有文章卡片；该站本日覆盖未知。[GitHub 记录](../raw/2026-11-25/github-items.json) · [官方页面记录](../raw/2026-11-25/official-pages.json)
- OpenAI 的 Shirudo 候选正文写 11 月 23 日，但归档顶部日期为 11 月 6 日；《A Thousand Fewer Paths to Root》候选顶部元数据写 11 月 24 日，正文日期却是 11 月 4 日。OpenWorks 案例正文没有发布日期。上述页面均不按候选元数据推为本日新发布。[候选记录](../raw/2026-11-25/official-link-candidates.json) · [Shirudo 正文](../raw/2026-11-25/official-link-candidates/openai-2124980590717911527-introducing-shirudo.opencli.md) · [root 研究正文](../raw/2026-11-25/official-link-candidates/openai-2125007927098699827-a-thousand-fewer-paths-to-root.opencli.md)
- OpenAI 的 iFood、Intentful 案例来自公司客户故事；feed 时间和页面正文日期一致，但正文顶部抓取元数据分别显示为 2026 年 5 月与 2025 年 10 月。它们是窗口外材料，数字未经第三方验证。[OpenAI RSS 记录](../raw/2026-11-25/rss-items.json) · [正文目录](../raw/2026-11-25/rss-fulltext/openai-blog/)
- follow-builders 本轮 offered 0 集；没有单集 transcript、说话人或时间戳可供阅读。该 feed 的空列表不能说明全部已配置节目没有更新。[podcast-items.json](../raw/2026-11-25/podcast-items.json) · [feed 快照](../raw/2026-11-25/podcasts/follow-builders/feed-podcasts.json)
- Trending README 中的实现、数量、遥测和权限描述均是项目自述；没有运行或独立核验。Claude-BugHunter、Cursor 插件和 last30days-skill 都涉及权限、外部数据或有副作用的操作，使用前需逐项检查目标授权、插件范围与数据传输。[README 目录](../raw/2026-11-25/github-trending-readmes/)

## 当天产物

- 采集与状态：[manifest](../raw/2026-11-25/manifest.json) · [run summary](../raw/2026-11-25/run-summary.json) · [signals](../raw/2026-11-25/signals.json) · [report-reading-list](../raw/2026-11-25/report-reading-list.json)
- AIHOT 发现与原文：[RSS 条目](../raw/2026-11-25/rss-items.json) · [feed 快照](../raw/2026-11-25/rss-feeds/aihot-selected.xml) · [原文归档目录](../raw/2026-11-25/rss-fulltext/aihot-selected/)
- 播客状态与材料：[podcast-items.json](../raw/2026-11-25/podcast-items.json) · [follow-builders feed 快照](../raw/2026-11-25/podcasts/follow-builders/feed-podcasts.json) · 本轮没有单集 transcript。
- 候选审计：[candidate audit JSON](../reviews/2026-11-25-candidate-audit.json) · [candidate audit Markdown](../reviews/2026-11-25-candidate-audit.md)
- 趋势报告：[2026-11-25 trend report](../trend/reports/2026-11-25-trend-report.md)
- 派生日报包：[JSON index](2026-11-25-daily-intel.index.json) · [HTML view](2026-11-25-daily-intel.html) · [docs index](index.html)

## 边界与验证

本日报覆盖 `2026-11-25` Asia/Shanghai 日期窗口和各来源自身的抓取上限。X、AIHOT、GitHub Trending 与 follow-builders 都不能用于推断未返回内容不存在；AIHOT 摘要、个人 X 帖子与 Trending README 保留各自证据边界。蛋白质设计结果是论文/官方文章所报的早期实验，Astra 天文案例给出的是候选信号。所有本地正文均按其来源和发布时间使用；播客无可读单集，未写成“零更新”。
