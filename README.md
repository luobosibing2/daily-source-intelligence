# Daily Source Intelligence

> 一套可审计、中文优先的每日公开信息采集与阅读工作流。

Daily Source Intelligence 会围绕预设主题，收集包括 Anthropic Engineering 在内的官方博客、RSS、follow-builders 播客 transcript、GitHub Releases、GitHub Trending 和公开 X/Twitter 信号，保留来源证据、生成阅读清单，并输出结构化中文日报。

[打开网页版（自动置顶最新一期）](https://luobosibing2.github.io/daily-source-intelligence/) · [浏览全部 Markdown 日报](docs/README.md) · [阅读完整运行手册](runbook.md)

## 它解决什么问题

每天的信息流很多，真正困难的不是“找到链接”，而是稳定地完成这条链路：

```text
公开来源 → 本地证据归档 → 去重与来源健康 → 阅读清单 → 中文日报
```

本项目把采集、证据边界和报告生成拆开：脚本负责确定性工作，日报负责解释“今天发生了什么、为什么值得关注、哪些判断仍需验证”。

## 核心特点

- **中文优先**：日报面向中文阅读，保留必要的英文标识符与原始链接。
- **证据可追溯**：重要判断回到官方正文、Release、README 或结构化公开数据。
- **失败不伪装**：抓取受限、凭据缺失或来源失败时明确记录覆盖边界。
- **来源分级**：区分官方来源、直接 X 证据，以及播客聚合 transcript、GitHub Trending 等二手或发现线索。
- **AIHOT 精选**：通过官方 RSS 补充 AI 资讯线索，沿原文链接归档正文，保留聚合出处并标为二手来源。接入方式和验证边界见 [AIHOT 来源说明](.agents/notes/implemented/feature/aihot-rss-source.md)。
- **播客长文本**：无额外 transcript key 读取 follow-builders 公共 feed；按 GUID 去重并保留说话人/时间戳，明确不做 ASR 和完整节目覆盖承诺。
- **可重复运行**：采集、状态更新、阅读清单和日报路径都有固定约定。

## 快速开始

要求：Python 3.10+、`curl`；如需网页正文 fallback，请安装 `opencli`。

```bash
python3 scripts/dsi.py run --date YYYY-MM-DD
```

已有当天采集结果时，可以只重建确定性派生物：

```bash
python3 scripts/dsi.py prepare --date YYYY-MM-DD
```

统一入口 [`scripts/dsi.py`](scripts/dsi.py#L1) 还提供 `check`、`publish`、`--dry-run`、`--resume`，并可用 `--channel rss|podcasts|github-releases|github-trending|official-pages|x` 定向运行；定向到单个来源时使用 `--source channel:id`。旧的独立脚本继续保留，便于诊断和兼容既有自动化。

播客通道只消费 follow-builders 已公开生成的 transcript，不运行 pod2txt/Supadata 或任何本地 ASR。完整 transcript 保存在本地 raw 供阅读和追溯，公开日报只输出中文洞察、必要短摘录与证据链接；中央 feed 本轮提供多少集就报告多少集，不把它解释为所有配置节目的完整检查。

## 分支与日报发布

主工作目录固定用于 `develop` 的功能开发。`main` 使用同一仓库旁边的独立 worktree，专门接收展示用的日期化日报；不要为了发布日报在主工作目录切换到 `main`。

首次准备发布 worktree：

```bash
git worktree add ../daily-source-intelligence-main main
```

每日流程完成并通过检查后，从 `develop` 工作目录运行统一入口：

```bash
python3 scripts/dsi.py publish --date YYYY-MM-DD --push
```

发布器兼容只含 Markdown 的旧日报；生成静态派生物后，则原子提交当天 Markdown、日期化 JSON 索引、日期化 HTML 和 `docs/index.html` 四件套，仍只显式推送 `origin/main`。它会拒绝不完整 bundle、脏的 main worktree、错误分支、不同的远端或包含其它文件的暂存区；功能代码从 `develop` 晋升到 `main` 仍是独立的稳定发布动作。底层兼容入口见 [`scripts/publish-daily-to-main.py`](scripts/publish-daily-to-main.py#L1)。

开始前建议先阅读 [运行手册](runbook.md)，并按需调整 [关注方向](config/watch.md)、[主题配置](config/topics.yaml) 与 [来源配置](config/sources.yaml)。

## X/Twitter 数据与凭据安全

X/Twitter 结构化数据通过 `twitterapi.io` 的只读接口采集。API key **不得写入配置、脚本、日报或任何提交文件**。采集脚本只从以下位置读取凭据：

1. 环境变量 `TWITTERAPI_IO_KEY`
2. macOS Keychain：`service=twitterapi.io`、`account=$USER`

没有凭据时，流程会记录 `skipped`，不会把“未采集到”误写成“账号没有更新”。详细说明见 [twitterapi.io 配置](config/twitterapi-io.md)。

## 仓库结构

| 路径 | 用途 |
| --- | --- |
| [`config/`](config/) | 关注主题、信息源与采集配置 |
| [`scripts/`](scripts/) | 采集、去重、派生与校验脚本 |
| [`tests/`](tests/) | 工作流核心行为测试 |
| [`docs/`](docs/) | 可读的每日情报日志 |
| [`runbook.md`](runbook.md) | 完整运行顺序、证据规则与失败边界 |

本仓库公开提交以代码、配置、运行手册和 `docs/` 日报为主；本地 raw 抓取、状态数据库、审计产物和长期趋势工作区不作为日常公开提交内容。

## 验证

```bash
python3 -m unittest discover -s tests -v
```

如果你只想了解项目产出，直接打开 [Daily Source Intelligence 网页版](https://luobosibing2.github.io/daily-source-intelligence/) 即可。
