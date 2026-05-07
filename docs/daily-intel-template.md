# YYYY-MM-DD Daily Source Intelligence

## 0. 采集范围

- 时间窗口：
- 配置来源：
- 生成时间：
- 原始归档目录：
- GitHub Trending：覆盖状态、解析 repo 数、Trending description 覆盖数、README 归档成功/失败数、是否 limited/failed

## 1. 今日高信号

| 等级 | 主题 | 标题/信号 | 来源 | 证据等级 | 链接 | 为什么重要 |
| --- | --- | --- | --- | --- | --- | --- |

## 2. 按主题分组摘要

### LLM / Frontier Models

### AI Agent / Agentic Workflow

### AI Coding / Developer Tools

### AI Infrastructure / Open Source

### GitHub Trending / Daily Repos

- 只作为 `secondary-source` discovery signal；上榜不等于官方发布、质量背书或长期趋势。
- 项目归纳必须把 Trending description 和 README 合成一段人话总结：先说它解决什么问题，再说 README 能确认的功能边界、使用场景或机制。不要写成 `Trending description:` / `README 归纳:` 这种字段式拆分。README 缺失的项目只列为待读候选，不写机制总结。

## 3. 来源证据表

| 来源 | 类型 | 原文链接 | 本地归档 | 证据等级 | 备注 |
| --- | --- | --- | --- | --- | --- |

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
