# YYYY-MM-DD Daily Source Intelligence

## 0. 采集范围

- 时间窗口：
- 配置来源：
- 生成时间：
- 原始归档目录：
- GitHub Trending：覆盖状态、解析 repo 数、Trending description 覆盖数、README 归档成功/失败数、是否 limited/failed

## 1. 今日高信号

每条高信号用 1-2 句简单介绍说明：这个信号是什么、为什么今天值得看、证据等级或边界是什么。保持简短，不展开成完整项目分析。

| 等级 | 主题 | 标题/信号 | 来源 | 证据等级 | 链接 | 为什么重要 |
| --- | --- | --- | --- | --- | --- | --- |

## 2. 按主题分组摘要

### LLM / Frontier Models

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
- `autocli-read` 是 `curl` 失败或 limited 后的公开网页读取 fallback；在备注中保留该方法名和剩余边界。

## 4. X/Twitter 覆盖说明

- 本日报通过 `twitterapi.io` 收集 X/Twitter 直接证据，不使用官方 X API，不使用 Exa MCP。
- `direct-x` 可作为直接证据；`secondary-source` 为可信媒体、博客、GitHub issue 或官方页面转述。
- 如果 `twitterapi.io` skipped/failed，必须写成覆盖失败或缺失，不得写成“账号无更新”。

## 5. 不确定性与待验证项

## 6. 运行统计

- 新增条目：
- 高信号条目：
- 重复跳过：
- 失败来源：
