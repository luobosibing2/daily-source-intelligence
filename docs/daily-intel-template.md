# YYYY-MM-DD Daily Source Intelligence

> 写作规则：中文优先。大多数行业术语、概念词、功能名和机制名直接翻译成自然中文，不默认堆英文原词，也不要写成大量“中文（English）”双语括注。只有需要精确指代或方便回溯检索时才保留英文，例如公司/产品/模型名、账号、repo、API/协议名、命令、文件路径、原文标题、股票代码，以及 `direct-x` 等证据标签。

## 0. 采集范围

- 时间窗口：
- 配置来源：
- 生成时间：
- 原始归档目录：
- 流程状态：[run-summary.json](../raw/YYYY-MM-DD/run-summary.json)
- 正文阅读清单：[report-reading-list.json](../raw/YYYY-MM-DD/report-reading-list.json)
- GitHub Trending：覆盖状态、解析 repo 数、Trending description 覆盖数、README 归档成功/失败数、是否 limited/failed

## 1. 今日高信号

每条高信号用 1-2 句简单介绍说明：这个信号是什么、为什么今天值得看、证据等级或边界是什么。保持简短，不展开成完整项目分析。

| 等级 | 主题 | 标题/信号 | 来源 | 证据等级 | 链接 | 为什么重要 |
| --- | --- | --- | --- | --- | --- | --- |

## 2. 按主题分组摘要

### 一手重点源 / First-party OpenAI & Claude Code

- 必须优先检查 `intelligence_department` 为 `first-party-openai` 或 `first-party-claude-code` 的 RSS/release Atom 条目。
- 这些来源配置为 `fulltext_policy: always`，不按普通 topic match 跳过；但仍要标注 `fulltext_status`、`fulltext_method` 和本地归档路径。

### X/Twitter 推主主题摘要

- 读取 [twitter-topic-brief.json](../raw/YYYY-MM-DD/twitter-topic-brief.json)，按 [config/topics.yaml](../config/topics.yaml) 的主题 label 汇总 priority 推主 tweet。
- 每个有内容的主题默认写 1-3 条最高分 tweet；保留 tweet 链接、`direct-x` 证据等级、推主 handle 和边界说明。
- `twitterapi.io` skipped/failed 或部分账号 failed/skipped 时，必须写成覆盖失败或缺失，不得写成“账号无更新”。

### LLM / Frontier Models

### AI Governance / Public Legitimacy

- 只收“AI lab / 核心人物 + 公共权威、政策机构、高影响治理文本”的组合，不收泛泛伦理文章。
- 优先检查 `official-link-candidates.json` 中的 priority X account 官方链接候选；抓取失败的候选必须进入“不确定性与待验证项”。

### AI Agent / Agentic Workflow

### AI Coding / Developer Tools

### AI Infrastructure / Open Source

### Forward Deployed Engineering / Enterprise AI Deployment

### GitHub Trending / Daily Repos

- 只作为 `secondary-source` discovery signal；上榜不等于官方发布、质量背书或长期趋势。
- 每个 repo 必须写成读者能看懂的项目介绍，不要只写标签、黑话或一句抽象定位。
- 每段至少交代：它到底是什么；解决什么具体问题；给谁用或怎么用；README 能确认的核心机制、功能边界或部署形态；为什么今天值得记录；还有哪些风险或待验证点。
- 项目归纳必须把 Trending description 和 README 合成一段人话总结。不要写成 `Trending description:` / `README 归纳:` 这种字段式拆分，也不要把 `agent-native / workflow / harness / infra` 等术语堆成一句话就结束。
- 金融、交易、浏览器绕检测、凭据路由、自动执行、隐私或安全敏感项目必须单独写风险边界。
- README 缺失的项目只列为待读候选，不写机制总结，并说明缺失原因和下一步最小验证路径。

## 3. 来源证据表

| 来源 | 类型 | 原文链接 | 本地归档 | 证据等级 | 备注 |
| --- | --- | --- | --- | --- | --- |

- RSS/Atom 高信号必须引用 `rss-items.json` 中的 `fulltext_status` 和本地 fulltext 归档；`limited` / `failed` / `skipped` 不能写成已读原文。
- OpenAI / Claude Code 一手重点源还要引用 `intelligence_department` 与 `relevance_status=always_read`；release Atom 正文归档在 `github-release-fulltext/<source-id>/`。
- `opencli-read` 是 `curl` 失败或 limited 后的公开网页读取 fallback；在备注中保留该方法名和剩余边界。

## 4. X/Twitter 覆盖说明

- 本日报通过 `twitterapi.io` 收集 X/Twitter 直接证据，不使用官方 X API，不使用 Exa MCP。
- `direct-x` 可作为直接证据；`secondary-source` 为可信媒体、博客、GitHub issue 或官方页面转述。
- 如果 `twitterapi.io` skipped/failed，必须写成覆盖失败或缺失，不得写成“账号无更新”。
- priority X account 中带官方域名链接的高分或强 governance 关键词 tweet，必须检查 `../raw/YYYY-MM-DD/official-link-candidates.json`；若未进入高信号，需在 candidate audit 或不确定性中说明。

## 5. 不确定性与待验证项

- official-link candidates 抓取失败/limited：
- candidate audit 中仍为 `missed` 的高分候选：

## 6. 运行统计

- 新增条目：
- 高信号条目：
- 重复跳过：
- 失败来源：
- twitter-topic-brief：
- report-reading-list：
- official-link candidates：
- candidate audit：

## 7. 完成审计

- 日报已写入：
- trend report 已写入：
- 更新过的 trend topic 文件已逐个列出：
- no-new-signal / skipped trend 已列出 topic 或 marker 路径：
- candidate audit 已检查：
- report-reading-list 已用于正文阅读：
- enabled trends 已检查：
- trend raw 已归档或 skipped 原因已写清：
