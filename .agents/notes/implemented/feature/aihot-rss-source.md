## 直接答案

AIHOT 提供官方 RSS 和匿名 REST API，无需账号或 API Key。DSI 采用精选摘要 RSS `https://aihot.news/feed.xml`，来源 ID 为 `aihot-selected`，配置为启用、非 priority 的二手发现源。标题和摘要保留 AIHOT 的归属，正文沿明确的原文链接读取。

- Class: `feature`
- Lifecycle: `implemented`
- Owner: Daily Source Intelligence maintainers
- 验证日期：2026-10-08，北京时间。
- 日常采集使用 `develop` 中的来源配置和现有每日入口，无需新增调度任务。

## 可用入口与选择依据

| 入口 | 官方说明 | 本次实测 |
| --- | --- | --- |
| [精选摘要 RSS](https://aihot.news/feed.xml) | 最新 50 条精选，摘要含原文入口 | HTTP 200，50 条，49 条有发布时间 |
| [精选全文 RSS](https://aihot.news/feed/full.xml) | 同一批精选；只对获准转载的来源内联正文 | 已核对官方说明，未请求该 feed |
| [全部动态 RSS](https://aihot.news/feed/all.xml) | 最近 7 天公开动态，按原文发布时间倒序 | HTTP 200，本轮返回 50 条，均有发布时间 |
| [日报 RSS](https://aihot.news/feed/daily.xml) | 每天北京时间 08:00 发布，保留 30 期 | HTTP 200，30 期 |
| [周报 RSS](https://aihot.news/feed/weekly.xml) | 每周一 10:00 发布，保留 12 期 | HTTP 200，12 期 |
| [月报 RSS](https://aihot.news/feed/monthly.xml) | 每月 1 日 10:30 发布，保留 12 期 | HTTP 200，本轮 5 期 |

依据为官方 [RSS 接入页](https://aihot.news/agent?tab=rss)及[本地 HTML 原文](../../../../raw/2026-10-08/aihot-source-research/agent-rss.html)、[llms.txt](https://aihot.news/llms.txt)及[本地原文](../../../../raw/2026-10-08/aihot-source-research/llms.txt)。HTTP 核验和字段抽取见[探测记录](../../../../raw/2026-10-08/aihot-source-research/probe.json)。

默认选择精选摘要以减少聚合噪声，并复用既有 RSS 通道。全部动态可以提供更宽的发现范围，但本轮返回条数不能证明完整覆盖最近 7 天。日报、周报和月报是再次汇总后的期刊，未同时加入每日采集，避免重复阅读同一批资讯。RSS 建议刷新间隔为 30 分钟，现有每天采集一次的节奏无需调整。

## 采集与证据路径

普通 RSS parser 默认只取前 5 条，且会去掉 description 内的 HTML 链接；直接加入 URL 会漏掉部分候选，并把 AIHOT 站内摘要当成正文目标。AIHOT 的独立解析路径读取最多 50 条，保存原始 feed 与 SHA，保留标题、摘要、GUID、站内阅读 URL 和原文 URL。

实际 [精选 XML](../../../../raw/2026-10-08/aihot-source-research/feed-main.xml) 的 `<link>` 指向 AIHOT；description 中标为“阅读原文”的链接才是正文目标。缺少明确原文链接时，不回退到 AIHOT 站内摘要作为全文。只对 feed `pubDate` 落在北京时间目标日、且命中既有主题关键词的条目尝试原文抓取；日期未知和窗口外条目保留在 raw 并写出边界。`pubDate` 是聚合站提供的发布时间，不能作为独立核实原文日期的证据。

AIHOT provenance 始终为 `secondary-source`。原文 canonical URL 用于既有去重；与独立官方来源重合时保留双方出处，官方证据来自独立官方来源自身。原文指向 X 时只使用公开 HTTP 读取，受限后不调用可能使用登录态的浏览器 fallback，不升级为 `direct-x`。`seen` 表示处理和去重，是否有可读正文仍以 `fulltext_status` 和本地正文路径为准。

实现入口为[来源配置](../../../../config/sources.yaml)、[稳定源采集器](../../../../scripts/collect-stable-sources.py)和[signals 派生器](../../../../scripts/dsi_signals.py)；完整流程遵循[运行手册](../../../../runbook.md)。定向采集使用统一入口：

```bash
python3 scripts/dsi.py run --date 2026-10-08 --channel rss --source rss:aihot-selected
```

## RSS 以外的抓取方式

官方 REST API 可直接取结构化 JSON：

```bash
curl --compressed 'https://aihot.news/api/v1/items?mode=selected&window=24h&by=published&limit=50'
```

读取 `items[].links.original`、`links.aihot`、`publishedAt`、`discoveredAt`，以及 `page.hasMore` 和 `page.nextCursor`。`by=published` 按原文发布时间定义滚动窗口；该时间缺失时，API 允许回退到收到时间。它的滚动 24 小时与 DSI 的北京时间目标日不是同一窗口。API 可用于未来分页或更宽覆盖，本次没有新增 API、MCP 或 Skill 采集通道。

依据为 [OpenAPI](https://aihot.news/openapi-v1.json)及[本地 JSON 原文](../../../../raw/2026-10-08/aihot-source-research/openapi-v1.json)、[实际 API 响应](../../../../raw/2026-10-08/aihot-source-research/selected-24h.json)和[API 接入页原文](../../../../raw/2026-10-08/aihot-source-research/agent-api.html)。

## 边界与验证

官方入口可访问及样本字段结构有明确原始响应支撑。本次精选快照有 3 条处于 2026-10-08 北京时间日窗、46 条窗口外、1 条时间未知；它只证明本轮返回情况，不证明来源完整性、日后稳定性或摘要事实正确。

公开采集用于本地研究；聚合摘要保留来源归属，重要判断回到原文核对。完整 raw 不进入公开日报 bundle。站点的[公开使用规则](https://aihot.news/terms)及[本地原文](../../../../raw/2026-10-08/aihot-source-research/terms.html)区分个人及内部使用与公开镜像、批量再分发等用途；本次接入未进行公开再分发。

57 项定向测试通过，覆盖 AIHOT/普通 RSS 解析、北京时间边界、正文读取与 fallback、canonical 去重、独立官方证据合并、provenance、统一 CLI、流水线、state 和 candidate audit；Python 编译检查与 `git diff --check` 通过。源码判断可定位到[AIHOT 解析](../../../../scripts/collect-stable-sources.py#L513)、[日窗与原文读取](../../../../scripts/collect-stable-sources.py#L406)和[signals 合并与出处](../../../../scripts/dsi_signals.py#L225)。

实际执行上述统一入口的定向采集后：来源状态 `ok`；50 条中 3 条日窗内、46 条窗口外、1 条时间未知；2 条命中主题，两篇原文均以公开 `curl` 读取，生成 2 项可读清单且保留 `secondary-source`。原始 feed SHA 与归档文件一致，X 原文没有触发浏览器 fallback。相关产物为[RSS 记录](../../../../raw/2026-10-08/aihot-source-research/live-smoke/raw/2026-10-08/rss-items.json)、[原始 feed](../../../../raw/2026-10-08/aihot-source-research/live-smoke/raw/2026-10-08/rss-feeds/aihot-selected.xml)、[signals](../../../../raw/2026-10-08/aihot-source-research/live-smoke/raw/2026-10-08/signals.json)、[阅读清单](../../../../raw/2026-10-08/aihot-source-research/live-smoke/raw/2026-10-08/report-reading-list.json)和[运行摘要](../../../../raw/2026-10-08/aihot-source-research/live-smoke/raw/2026-10-08/run-summary.json)。产物里的相对路径以 `live-smoke/` 为根。这是单源接入验证；未运行当天全来源日报、趋势归档或公开发布，归档不替代日常 raw 或主工作区 state。
