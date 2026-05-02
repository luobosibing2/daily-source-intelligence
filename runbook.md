# Daily Source Intelligence Runbook

## 目标

每天收集过去 24 小时内与 `config/watch.md` 相关的公开资讯，优先覆盖官方博客、RSS、GitHub 发布，以及 `twitterapi.io` 能返回的结构化 X/Twitter 数据。第一版不使用官方 X API，不使用 Exa MCP，不承诺完整抓取某个 X 账号的所有推文。

输出必须符合本仓库的主题归档规则：

- 原始材料写入 `daily-source-intelligence/raw/YYYY-MM-DD/`
- 可读日报写入 `daily-source-intelligence/docs/YYYY-MM-DD-daily-intel.md`
- 去重和源健康状态写入 `daily-source-intelligence/state/`

## 每日流程

1. 读取配置
   - 读取 `config/watch.md` 理解关注方向和高信号定义。
   - 读取 `config/topics.yaml` 获取主题、关键词、排除词和输出分组。
   - 读取 `config/sources.yaml` 获取 RSS、GitHub、官方页面、`twitterapi_io` 配置和 X/Twitter handles。
   - 读取 `state/seen.json`，避免重复记录已经处理过的 URL、tweet id 或 GitHub release id。

2. 采集稳定来源
   - 优先运行 `daily-source-intelligence/scripts/collect-stable-sources.py`，统一写出 `rss-items.json`、`github-items.json`、`official-pages.json`。
   - 脚本会在代理环境变量缺失时默认补上 `http_proxy=http://127.0.0.1:7890`、`https_proxy=http://127.0.0.1:7890`、`all_proxy=socks5://127.0.0.1:7890`；如需临时禁用，设置 `DAILY_INTEL_DISABLE_DEFAULT_PROXY=1`。
   - RSS/Atom：读取 `rss` sources 中启用的 feed，收集过去 24 小时的新条目。
   - GitHub：第一版无 `GITHUB_TOKEN` 时优先读取 `https://github.com/{repo}/releases.atom`；REST API 只作为增强路径。若 REST API 返回 rate limit 或 403，不视为整体失败，降级到 Atom feed 并写入 `source-health.json`。
   - 官方页面：读取 `official_pages`，优先发现新 blog、changelog、release note 或 docs update。

3. 使用 twitterapi.io 采集 X/Twitter 直接证据
   - 运行 `daily-source-intelligence/scripts/collect-twitterapi-io.py`。脚本优先读取环境变量 `TWITTERAPI_IO_KEY`；如果不存在，再尝试从 macOS Keychain 的 `service=twitterapi.io`、`account=$USER` 读取。
   - 脚本同样会在代理环境变量缺失时补上本机默认代理；如需临时禁用，设置 `DAILY_INTEL_DISABLE_DEFAULT_PROXY=1`。
   - 默认读取 `x_accounts` 中启用的账号，调用 `GET https://api.twitterapi.io/twitter/user/last_tweets`。
   - 默认 `includeReplies=false`，避免日报被回复流刷屏；如需完整上下文，再按 tweet id 追加 thread/context。
   - 付费 key 默认用并发采集；`TWITTERAPI_IO_MAX_WORKERS` 控制并发数，`TWITTERAPI_IO_REQUEST_INTERVAL_SECONDS` 控制可选节流。
   - 每个账号保留过去 24-36 小时内的 tweet，写入 `raw/YYYY-MM-DD/twitterapi-io-results.json`。
   - 每条直接来自该 API 的 tweet 证据等级标为 `direct-x`。
   - 如果环境变量和 Keychain 都没有 key，写入 skipped 状态；这不代表账号没有更新。

4. 不使用 Exa MCP
   - 本 workflow 不使用 Exa MCP 作为补漏层。
   - 如果 `twitterapi.io` credential 缺失、API 失败或账号覆盖失败，只记录 skipped/failed 状态，不用 Exa 搜索替代。
   - 如果稳定来源和 `twitterapi.io` 都失败，当天日报仍要生成，并把失败源、失败原因和缺失覆盖范围写清楚。

5. 归档 raw
   - 当天目录：`raw/YYYY-MM-DD/`
   - 保存一份 `manifest.json`，记录采集时间、查询范围、来源、命中数量、失败来源。
   - 保存稳定来源条目为 `rss-items.json`、`github-items.json`、`official-pages.json`。
   - 保存 twitterapi.io 结果为 `twitterapi-io-results.json`；若没有 `TWITTERAPI_IO_KEY`，也要写入 skipped 文件。
   - 对高信号原文，尽量保存 HTML、Markdown 或文本提取文件；无法归档时在日报“不确定性与待验证项”说明。

6. 去重和评分
   - 去重键优先级：`tweet_id` > canonical URL > normalized title + source。
   - 已存在于 `state/seen.json` 的条目不重复写入日报，除非有新的重要后续。
   - 评分只用于排序，不用于删除高优先级来源：
     - priority source: +3
     - direct official source: +3
     - direct X link: +2
     - cross-source confirmation: +3
     - recency under 24h: +2
     - strong match to `watch.md`: +3
     - secondary-source only: -1

7. 生成日报
   - 写入 `docs/YYYY-MM-DD-daily-intel.md`。
   - 日报语言使用中文；保留英文产品名、账号、repo、API 名称。
   - 结构必须包含：
     - 采集范围
     - 今日高信号
     - 按主题分组摘要
     - 来源证据表
     - X/Twitter 覆盖说明
     - 不确定性与待验证项
   - 每条 X/Twitter 相关内容必须标注证据等级：
     - `direct-x`
     - `secondary-source`

8. 更新状态
   - 优先运行 `daily-source-intelligence/scripts/update-state.py`，根据当天 raw 文件生成/更新 `manifest.json`、`state/source-health.json` 和 `state/seen.json`。
   - `seen.json` 的脚本更新采用保守策略：稳定来源只记录日报窗口内条目；X/Twitter 只记录强关键词或互动明显的 direct-x 条目，默认最多自动记录 40 条；人工已有记录不覆盖标题。

9. 自动化结果摘要
   - 输出短摘要即可：新增条目数、高信号条目数、失败来源、生成的日报路径。
   - 如果没有高相关新增内容，也要生成当天日报，记录采集范围和“无高信号新增内容”。

## 第一版边界

- 不使用登录态抓取网页。
- 不使用官方 X API 或非官方账号密码自动化。
- 不使用 Exa MCP 作为 fallback discovery layer。
- `twitterapi.io` 仅使用 read endpoints；不使用发帖、点赞、关注、DM 等 action endpoints。
- 不承诺完整 Twitter/X 时间线覆盖。
- 不自动发送 Discord、Telegram 或邮件。
- 不把未验证的二手线索写成确定事实。

## 后续升级触发条件

满足任一条件时，考虑把 `twitterapi.io` 从每日轮询升级为 stream/webhook，或改用官方 `X_BEARER_TOKEN`：

- 某个高优先级 X 账号连续 3 天只得到二手来源或无结果。
- 需要完整列出指定账号过去 24 小时全部原帖。
- 需要稳定记录 tweet id、engagement metrics、thread context。
- 需要为长期研究保留更严格、可审计的原始数据。
