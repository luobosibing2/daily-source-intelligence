# Daily Source Intelligence Runbook

## 目标

每天收集过去 24 小时内与 `config/watch.md` 相关的公开资讯，优先覆盖官方博客、RSS、GitHub 发布、GitHub 每日热门项目，以及 `twitterapi.io` 能返回的结构化 X/Twitter 数据。第一版不使用官方 X API，不使用 Exa MCP，不承诺完整抓取某个 X 账号的所有推文。

输出必须符合本仓库的主题归档规则：

- 原始材料写入 `daily-source-intelligence/raw/YYYY-MM-DD/`
- 可读日报写入 `daily-source-intelligence/docs/YYYY-MM-DD-daily-intel.md`
- 去重和源健康状态写入 `daily-source-intelligence/state/`

## 每日流程

推荐用 [`scripts/run-dsi-pipeline.py`](scripts/run-dsi-pipeline.py) 承担采集等待和确定性派生物生成，避免在长 Codex 会话里边等边读大 raw。常用入口：

```bash
RUN_DATE=YYYY-MM-DD python3 scripts/run-dsi-pipeline.py --date YYYY-MM-DD
```

该脚本会写入 `raw/YYYY-MM-DD/report-reading-list.json` 与 `raw/YYYY-MM-DD/run-summary.json`。`run-summary.json` 只用于流程状态与路径索引，不是日报证据正文；日报写作仍必须按 `report-reading-list.json` 读取其中列出的正文、README、release body、official-link fulltext 和 priority X direct evidence。

1. 读取配置
   - 读取 `config/watch.md` 理解关注方向和高信号定义。
   - 读取 `config/topics.yaml` 获取主题、关键词、排除词和输出分组。
   - 读取 `config/sources.yaml` 获取 RSS、GitHub releases、GitHub Trending、官方页面、`official_link_candidates`、`twitterapi_io` 配置和 X/Twitter handles。
   - 读取 `state/seen.json`，避免重复记录已经处理过的 URL、tweet id 或 GitHub release id。

2. 采集稳定来源
   - 优先运行 `daily-source-intelligence/scripts/collect-stable-sources.py`，统一写出 `rss-items.json`、`github-items.json`、`github-trending.json`、`official-pages.json`。
   - 脚本不再内置或自动补本机代理。网络路径优先使用系统/TUN 级代理；如需显式代理，运行前手动设置 `http_proxy`、`https_proxy` 或 `all_proxy`，`curl` 会自动读取这些环境变量。
   - RSS/Atom：读取 `rss` sources 中启用的 feed，收集过去 24 小时的新条目。脚本默认用 [`config/topics.yaml`](config/topics.yaml) 与每个 source 的 `topics` 判断 feed 条目是否命中关注方向；命中的 RSS 条目必须继续打开原文 URL，归档到 `raw/YYYY-MM-DD/rss-fulltext/<source-id>/`，并在 `rss-items.json` 条目上写入 `relevance_status`、`matched_topics`、`matched_keywords`、`fulltext_status`、`fulltext_method`、`fulltext_path`、`raw_html_path` 或失败原因。不能只凭 feed title/RSS summary 写强判断。
   - 一手重点源不走 topic 过滤。凡是 source 配置了 `fulltext_policy: always`，例如 `openai-blog`、`openai-codex`、`anthropics-claude-code`，只要 feed/release Atom 里出现条目就尝试提取正文，并写入 `relevance_status=always_read` 与 `intelligence_department`。日报里把这些条目放到“一手重点源 / First-party OpenAI & Claude Code”部门，不因关键词未命中而跳过。
   - RSS 原文抓取先用 `curl` 保存 HTML/提取文本；如果 `curl` 失败、返回 Cloudflare/JS challenge、正文太短或不可读，必须自动尝试 `opencli web read --url <url> --stdout true --download-images false -f md`。`opencli` 成功时将 Markdown 归档为 `.opencli.md`，证据方法标为 `opencli-read`；仍失败时标为 `limited`/`failed`，日报和 trend 只能写边界，不得把摘要升级成全文证据。
   - GitHub：第一版无 `GITHUB_TOKEN` 时优先读取 `https://github.com/{repo}/releases.atom`；REST API 只作为增强路径。若 REST API 返回 rate limit 或 403，不视为整体失败，降级到 Atom feed 并写入 `source-health.json`。配置了 `fulltext_policy: always` 的 release Atom 源必须保留 release Atom content 全文到 `raw/YYYY-MM-DD/github-release-fulltext/<source-id>/`；内容过短时标为 `limited`，不能假装读到了 release body。
   - GitHub Trending：读取 `github_trending` sources，默认采集 `https://github.com/trending?since=daily` 的前 10 个项目，写入 `github-trending.json`。每个 repo 必须保留 GitHub Trending 页面上的 `trending_description`，也必须继续打开并归档 README，保存到 `raw/YYYY-MM-DD/github-trending-readmes/`，并在 `github-trending.json` 中写入 `readme_status`、`readme_method`、`readme_path`、`readme_title` 和 `readme_excerpt`。README raw 抓取失败时尝试 `opencli web read`；Trending 页面自身若 curl 失败但 `opencli` 可读，只能归档诊断快照，仍不能替代 repo-card HTML 解析。Trending 只作为发现/研究线索，证据等级默认 `secondary-source`；不要把“上榜”写成官方发布、质量背书或长期趋势。
   - 官方页面：读取 `official_pages`，优先发现新 blog、changelog、release note 或 docs update。官方页面抓取失败、limited 或 challenge 时同样尝试 `opencli web read`，并把 `fetch_method` / `fulltext_method` 写入 `official-pages.json`。

3. 使用 twitterapi.io 采集 X/Twitter 直接证据
   - 运行 `daily-source-intelligence/scripts/collect-twitterapi-io.py`。脚本优先读取环境变量 `TWITTERAPI_IO_KEY`；如果不存在，再尝试从 macOS Keychain 的 `service=twitterapi.io`、`account=$USER` 读取。
   - 脚本同样不再内置或自动补本机代理；使用系统/TUN 级网络或运行环境中已有的 proxy env。
   - 默认读取 `x_accounts` 中启用的账号，调用 `GET https://api.twitterapi.io/twitter/user/last_tweets`。
   - 默认 `includeReplies=false`，避免日报被回复流刷屏；如需完整上下文，再按 tweet id 追加 thread/context。
   - 付费 key 默认用并发采集；`TWITTERAPI_IO_MAX_WORKERS` 控制并发数，`TWITTERAPI_IO_REQUEST_INTERVAL_SECONDS` 控制可选节流。
   - 每个账号保留过去 24-36 小时内的 tweet，写入 `raw/YYYY-MM-DD/twitterapi-io-results.json`。
   - 每条直接来自该 API 的 tweet 证据等级标为 `direct-x`。
   - 运行 `python3 scripts/official-link-candidates.py --date YYYY-MM-DD`，从 priority X account 的 tweet 中提取官方域名链接。若 tweet 分数达到 `official_link_candidates.min_score`，或命中强 governance/public-authority 关键词，则尝试抓取 expanded URL 正文，写入 `raw/YYYY-MM-DD/official-link-candidates.json` 与 `raw/YYYY-MM-DD/official-link-candidates/`。
   - official-link candidate 只作为待验证候选；抓取成功后可升级为 official-source/direct-x 组合证据，抓取 `limited`/`failed` 时必须在日报“不确定性与待验证项”里说明，不能把 X card metadata 当成已读官方原文。
   - 运行 [`scripts/build-twitter-topic-brief.py`](scripts/build-twitter-topic-brief.py) `--date YYYY-MM-DD`，从当天 `twitterapi-io-results.json` 生成 `raw/YYYY-MM-DD/twitter-topic-brief.json`。该文件按 [`config/topics.yaml`](config/topics.yaml) 的日报主题归类 priority 推主推文，`x_accounts[].topics` 作为账号默认主题，tweet 文本/card 命中关键词时补充更精确的主题和关键词。
   - 如果环境变量和 Keychain 都没有 key，写入 skipped 状态；这不代表账号没有更新。

4. 不使用 Exa MCP
   - 本 workflow 不使用 Exa MCP 作为补漏层。
   - 如果 `twitterapi.io` credential 缺失、API 失败或账号覆盖失败，只记录 skipped/failed 状态，不用 Exa 搜索替代。
   - 如果稳定来源和 `twitterapi.io` 都失败，当天日报仍要生成，并把失败源、失败原因和缺失覆盖范围写清楚。

5. 归档 raw
   - 当天目录：`raw/YYYY-MM-DD/`
   - 保存一份 `manifest.json`，记录采集时间、查询范围、来源、命中数量、失败来源。
   - 保存稳定来源条目为 `rss-items.json`、`github-items.json`、`github-trending.json`、`official-pages.json`。
   - 保存 RSS 命中关注方向的原文归档到 `rss-fulltext/<source-id>/`；`.html` 是 `curl` 原始响应，`.extracted.md` 是本地文本提取，`.opencli.md` 是 `opencli web read` 可读正文。
   - 保存一手 release Atom 全文归档到 `github-release-fulltext/<source-id>/`；`.atom.md` 是从 GitHub release Atom `<content>` 提取的可读正文。
   - 保存 GitHub Trending README 原文到 `github-trending-readmes/`；如果 README 缺失、raw URL 不可访问或下载失败，必须在 `github-trending.json` 和日报“不确定性与待验证项”里说明。
   - 保存官方页面 fallback 正文到 `official-page-text/`；如果只有 `curl` challenge HTML 或 `opencli` 也失败，必须在 `official-pages.json`、`manifest.json` 和日报“不确定性与待验证项”里说明。
   - 保存 twitterapi.io 结果为 `twitterapi-io-results.json`；若没有 `TWITTERAPI_IO_KEY`，也要写入 skipped 文件。
   - 保存 priority X 官方链接候选为 `official-link-candidates.json`；对应正文归档到 `official-link-candidates/`。如果候选抓取失败，保留 `fulltext_status=limited/failed` 和错误原因。
   - 保存 X/Twitter 推主主题摘要为 `twitter-topic-brief.json`；如果 twitterapi.io skipped/failed 或部分账号失败，摘要必须写入 coverage 边界，不能解释成账号无更新。
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

7. 更新状态
   - 优先运行 `daily-source-intelligence/scripts/update-state.py`，根据当天 raw 文件生成/更新 `manifest.json`、`state/source-health.json` 和 `state/seen.json`。
   - `seen.json` 的脚本更新采用保守策略：稳定来源只记录日报窗口内条目；GitHub Trending 用 `github-trending:{owner}/{repo}` 作为去重键并标记为 `secondary-source`；X/Twitter 只记录强关键词或互动明显的 direct-x 条目，默认最多自动记录 40 条；人工已有记录不覆盖标题。
   - 运行 [`scripts/run-dsi-pipeline.py`](scripts/run-dsi-pipeline.py) 或 `--skip-collection` 派生当天 `report-reading-list.json` 和 `run-summary.json`。`report-reading-list.json` 是正文阅读清单，不得替代正文阅读；`run-summary.json` 只记录流程状态、失败源、路径和候选数量。

8. 生成日报
   - 写入 `docs/YYYY-MM-DD-daily-intel.md`。
   - 写作前先读取 `raw/YYYY-MM-DD/report-reading-list.json`，按清单逐项读取 `local_body_path` 指向的正文文件；`local_body_path` 为空但 `fulltext_status=limited/failed/n/a` 的条目，只能写覆盖边界或 direct-X 结构化证据，不能写成已读正文。
   - 日报语言中文优先。大多数行业术语、概念词、功能名和机制名直接翻译成自然中文，不默认堆英文原词，也不要写成大量“中文（English）”双语括注。只有需要精确指代或方便回溯检索时才保留英文，例如公司/产品/模型名、账号、repo、API/协议名、命令、文件路径、原文标题、股票代码，以及 `direct-x` 等证据标签。
   - 结构必须包含：
     - 采集范围
     - 今日高信号
     - 按主题分组摘要
     - 来源证据表
     - X/Twitter 覆盖说明
     - 不确定性与待验证项
   - `今日高信号` 不要只列标题。每条用 1-2 句简单介绍说明：这个信号是什么、为什么今天值得看、证据等级或边界是什么；保持简短，不展开成完整项目分析。
   - 每条 X/Twitter 相关内容必须标注证据等级：
     - `direct-x`
     - `secondary-source`
   - 日报必须在“按主题分组摘要”中包含 `### X/Twitter 推主主题摘要`，读取 `raw/YYYY-MM-DD/twitter-topic-brief.json`，按 [`config/topics.yaml`](config/topics.yaml) 的主题 label 汇总推主推文。每个有内容的主题默认选 1-3 条最高分 tweet，保留 tweet 链接、`direct-x` 证据等级和边界说明。
   - 每条 RSS/Atom 高信号必须检查 `rss-items.json` 中对应条目的 `fulltext_status`。只有 `fulltext_status=ok` 且 `fulltext_path` 指向本地归档时，才能写成已读原文；`limited`、`failed` 或 `skipped` 只能按摘要/发现线索写边界。
   - 日报必须有“一手重点源 / First-party OpenAI & Claude Code”部门，优先汇总 `intelligence_department` 为 `first-party-openai` 或 `first-party-claude-code` 的条目；这些条目不受普通 topic match 限制，但仍必须写清 fulltext 是否 ok/limited。
   - GitHub Trending 每日热门项目必须单独说明覆盖状态、解析到的 repo 数、Trending description 覆盖状态、README 归档覆盖状态，以及它只是 discovery signal 的边界。
   - 每个 GitHub Trending repo 的项目归纳必须写成“读者能看懂的项目介绍”，不能只写标签、黑话或一句抽象定位。每段至少交代：
     - 这个项目到底是什么，不要只复述 repo slogan。
     - 它解决什么具体问题，或面向哪类使用者/场景。
     - README 能确认的核心机制、使用方式、功能边界或部署形态。
     - 为什么今天值得记录，以及它只是 discovery signal 的证据边界。
     - 如涉及金融、浏览器绕检测、凭据路由、自动执行、交易、隐私或安全敏感面，必须额外写风险和待验证点。
   - 项目归纳必须把 Trending description 和 README 原文/摘录合成一段自然语言总结。不要写成 `Trending description:` / `README 归纳:` 这种字段式拆分，不要把两份来源割裂成两段，也不要用 `agent-native / workflow / harness / infra` 等术语堆成一句话就结束。
   - 若 README 缺失，不能写机制总结，只能写“待读 README 的候选项目”，并说明缺失原因和下一步最小验证路径。
   - 日报初稿完成后运行 `python3 scripts/candidate-audit.py --date YYYY-MM-DD`，写入 `reviews/YYYY-MM-DD-candidate-audit.md`。凡是 `official-link-candidate` 或高分 direct-x/RSS 条目为 `missed`，必须在“今日高信号”或“不确定性与待验证项”中处理；若确认弱相关，可在 audit/review 中说明弱相关边界。

9. 更新长期 trend
   - 日报正文不新增 trend 小节；长期趋势分析写入 `trend/`。
   - 读取 `config/trends.yaml`，所有 `enabled: true` 的 trend 都必须在当天 trend report 中出现。
   - 输入范围为当天日报 `docs/YYYY-MM-DD-daily-intel.md` 与当天 raw `raw/YYYY-MM-DD/`；聊天中的未归档判断不能作为 trend 证据。
   - 只对明确命中 enabled trend 且有新信息量的高信号做扩充搜索。扩充来源优先级：官方页面、官方 docs、GitHub repo、GitHub release body、GitHub README；普通 web search 只用于定位原始官方材料。
   - 凡是被选入 trend 的 RSS / Atom / 官方博客 / 博文 / newsletter 条目，必须先下载并归档原文，再阅读原文后写入 trend 判断；不能只凭 feed title、RSS summary、站点 metadata 或聊天中的印象更新专题结论。优先复用当天 `raw/YYYY-MM-DD/rss-fulltext/` 中已归档的 fulltext；缺失时再补抓并归档到 trend raw。
   - 原文归档写入 `trend/raw/YYYY-MM-DD/<trend-id>/`，优先保存 HTML 原文、Markdown/文本提取版和一个简短 manifest；如果 `curl` 下载失败、付费墙、反爬、正文不可读或只有 RSS 摘要，必须尝试 `opencli web read`。`opencli` 仍失败时，在当天 trend report 中标为 `needs-fulltext` / `limited`，且不能把该条提升为强 trend 结论。
   - GitHub Trending / GitHub repo 信号必须至少读取并归档 README 或 release body；README 缺失或正文不可读时，只能列为 discovery candidate，不能写机制判断。
   - trend 扩充不得重跑 `twitterapi.io`，不得使用 X/Twitter 写操作、posting、liking、following 或 DM。公开网页正文可用 `opencli web read` 作为失败 fallback，但必须记录 `opencli-read` 方法和归档路径，不得把登录态社交内容当作替代证据。
   - 扩充得到的官方页面、docs、README、release body、摘录或 manifest 写入 `trend/raw/YYYY-MM-DD/<trend-id>/`。
   - 写入当天趋势分析报告：`trend/reports/YYYY-MM-DD-trend-report.md`。报告必须回答“今天这些情报对长期趋势意味着什么”，不能只写 audit 表。
   - trend report 和专题报告同样执行中文优先写作规则：大多数行业术语、概念词、功能名和机制名直接翻译成自然中文；只有需要精确指代或方便回溯检索时才保留英文。
   - Phase 2 启动前必须先做 marker preflight：每个 enabled trend 当天必须且只能有 `trend/raw/YYYY-MM-DD/<trend-id>/manifest.json` 或 `trend/raw/YYYY-MM-DD/<trend-id>/no-new-signal.json` 之一。缺 marker、两个 marker 同时存在、marker 内 `run_date` / `trend_id` 与路径不一致，或 `manifest.json` 引用的 `archive_path` 不存在时，直接 fail fast，不启动任何 topic consolidator。
   - Phase 2 必须更新当天 trend report；父脚本继续生成 `## 状态索引` 和 `## 更新日志` 作为审计区。只有存在 `new-signal`、`limited` 或 `needs-fulltext` claim 候选的专题才调度 LLM 重写主体正文；`no-new-signal` / `skipped` 专题保留现有主体正文，只刷新脚本拥有的审计区，并在更新日志中写明“已检查，无新增，未触发 LLM rewrite”。
   - 被调度的专题主体正文由父脚本调度 LLM 生成，父脚本负责校验和落盘；LLM 只读取 SQLite 派生 payload、`trend/raw/YYYY-MM-DD/<trend-id>/` 和现有 `trend/*.md`，不得重新联网或扩大证据范围。
   - 专题主体正文保留 `forward-deployed-engineering` 当前可读格式的逻辑，但不再包在旧 `## 自动专题正文` 外层下；必须包含 `## 本次更新`、`## 当前活跃判断`、`## 受限与待验证`、`## 已替代/削弱/过时判断`、`## 对长期趋势的含义`、`## 短时间线`、`## 证据入口`。`## 短时间线` 只保留短趋势含义和消息源：日期、claim id、证据链接、lifecycle status；不要继续堆长篇历史“延续判断”。
   - 旧判断可以重排、压缩和改写，但不能静默删除；过时、被替代、被削弱、受限或待验证的判断必须继续通过 SQLite `trend_claims` 和专题报告状态索引追溯。
   - 有新增趋势信号时，必须把对应 claim 合入专题主体正文，例如 `trend/memory-dream.md`、`trend/financial-agents.md`、`trend/forward-deployed-engineering.md`、`trend/ai-governance-legitimacy.md`；无新增时，专题正文不强制重写，当天 trend report 与对应 `no-new-signal.json` 必须标记已检查无新增。
   - `trend/` 的长期议题报告以 `config/trends.yaml` 中 enabled trend 的 `timeline` 为准。不要再生成跨主题总报告；跨日判断、关键转折、证据强度、不确定性和更新日志分别沉淀到对应专题报告里。

10. 自动化结果摘要
   - 输出短摘要即可：新增条目数、高信号条目数、失败来源、`run-summary.json` 路径、`report-reading-list.json` 路径、生成的日报路径、candidate audit 路径、trend report 路径、更新过的专题报告、无新增或 skipped 的 trend。
   - 更新过的专题报告不能只写 trend id 或 topic 名称；必须按 `config/trends.yaml` 中每个 enabled trend 的 `timeline` 逐个列出实际文件路径，并写成可点击 Markdown 文件链接。这样 Codex App 的文件列表能展示被改过的 `trend/*.md`，例如 [`trend/memory-dream.md`](trend/memory-dream.md)、[`trend/enterprise-delivery-system.md`](trend/enterprise-delivery-system.md)。
   - 无新增或 skipped 的 trend 也必须列出对应专题报告路径或 marker 路径，明确它是已检查但无新增，而不是遗漏。
   - 如果没有高相关新增内容，也要生成当天日报，记录采集范围和“无高信号新增内容”。
   - 声明完成前必须核对：日报已写入、candidate audit 已写入且 missed 候选已处理或解释、trend report 已写入、所有 enabled trend 均已检查、对应专题报告已更新或记录无新增、扩充 raw 已归档或 skipped 原因已写清。

## 第一版边界

- 不使用登录态抓取 X/Twitter 或其它需要账号权限的私有内容；公开网页、公开博客或公开文件在 `curl` 失败时可用 `opencli web read` 作为读取 fallback，并必须记录方法与限制。
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
