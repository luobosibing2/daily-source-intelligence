# TwitterAPI.io 接入说明

## 适用场景

`twitterapi.io` 是本 workflow 的 X/Twitter 直接证据来源。它返回结构化 tweet JSON，适合做每日账号监控、去重、证据等级标注和长期归档。

第一版只使用 read endpoints，不使用发帖、点赞、关注、DM 等 write/action endpoints。

## 凭证

不要把 API key 写进仓库。运行前在本机环境或 Codex 自动化环境中设置：

```bash
export TWITTERAPI_IO_KEY="..."
```

官方文档要求每个请求携带 `X-API-Key` / `x-api-key` header。

当前机器上的 Codex 沙箱无法直接访问本机 `127.0.0.1:7890` 代理；在 Codex 里真实请求该 API 时，需要使用非沙箱网络权限执行。普通终端里只要 proxy 环境变量可用即可。

更推荐的长期方式是把 key 放进 macOS Keychain：

```bash
bash daily-source-intelligence/scripts/setup-twitterapi-io-key.sh
```

脚本会隐藏输入，并写入 Keychain 的 `service=twitterapi.io`、`account=$USER`。采集脚本读取顺序是：

1. `TWITTERAPI_IO_KEY`
2. macOS Keychain：`service=twitterapi.io`、`account=$USER`

如果需要自定义 Keychain 条目，可设置：

```bash
export TWITTERAPI_IO_KEYCHAIN_SERVICE="twitterapi.io"
export TWITTERAPI_IO_KEYCHAIN_ACCOUNT="$USER"
```

## 第一版采集策略

默认使用：

- `GET https://api.twitterapi.io/twitter/user/last_tweets`
- 参数：`userName={handle}`
- 参数：`includeReplies=false`

该接口按账号取最近 tweets，每页最多返回 20 条。对我们每天 10 点跑一次的场景，第一版通常够用：每个重点账号每天取第一页，再按 `createdAt` 过滤过去 24-36 小时。

采集脚本支持并发。付费后默认使用 5 并发、0 秒账号间隔。可用下面的环境变量调整：

```bash
export TWITTERAPI_IO_MAX_WORKERS="5"
export TWITTERAPI_IO_REQUEST_INTERVAL_SECONDS="0"
```

如果遇到 rate limit，可临时降低 `TWITTERAPI_IO_MAX_WORKERS` 或增加 `TWITTERAPI_IO_REQUEST_INTERVAL_SECONDS`。

如果后续需要关键词级补漏，再使用：

- `GET https://api.twitterapi.io/twitter/tweet/advanced_search`
- query 示例：`(Codex OR "Claude Code" OR Cursor) since_time:{unix_ts} until_time:{unix_ts}`

注意：官方文档提示 advanced search 不建议依赖 pagination，应通过 `since_time` / `until_time` 控制每次返回不超过 20 条。

## 输出

脚本输出到当天 raw 目录：

- `twitterapi-io-results.json`

默认终端只打印摘要，完整 tweet JSON 写入 raw 文件。如果需要在终端打印完整 JSON：

```bash
export TWITTERAPI_IO_PRINT_FULL=1
```

日报中每条直接来自该 API 的 tweet 标为：

- `direct-x`

如果 API key 不存在或请求失败，日报不能写成“账号无更新”，只能写成“twitterapi.io 未覆盖/失败”；不要使用 Exa MCP 作为替代搜索来源。

## 后续升级

如果关注账号超过 20 个，或者需要接近实时监控，再考虑 stream/webhook 路线：

- `POST /oapi/x_user_stream/add_user_to_monitor_tweet`
- 或 webhook filter rule：`POST /oapi/tweet_filter/add_rule`

这类方式需要额外配置 webhook 接收端，不适合第一版日更日报。
