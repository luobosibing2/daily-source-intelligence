# Evening Review Runbook

## 目标

每天晚上 22:00 生成一份日终追问复盘，输出到 `reviews/YYYY-MM-DD-evening-review.md`。它不是第二份每日情报日报，而是把当天本地 Codex 互动整理成“今天追问了什么、哪些值得沉淀、明天可以直接派给 Agent 继续什么”。

本流程和早上的 [`runbook.md`](runbook.md) 明确分工：

- 早上 `Daily Source Intelligence` 负责采集外部公开信号，写入 `docs/YYYY-MM-DD-daily-intel.md` 与 `trend/reports/YYYY-MM-DD-trend-report.md`。
- 晚上 `Daily Evening Review` 只读本地 Codex session 摘要，弱引用当天日报或 trend report，不重新采集外部资讯。

## 输入

1. 读取当天本地 Codex sessions：
   - 来源目录：`~/.codex/sessions/YYYY/MM/DD/*.jsonl`
   - 提取命令：`python3 scripts/extract-codex-sessions.py --date YYYY-MM-DD`
   - 提取结果：`reviews/raw/YYYY-MM-DD/codex-sessions.json`

2. 可选弱引用当天报告：
   - `docs/YYYY-MM-DD-daily-intel.md`
   - `trend/reports/YYYY-MM-DD-trend-report.md`

3. 不读取、不采集、不调用：
   - 不读 ChatGPT 网页聊天。
   - 不碰登录态浏览器。
   - 不联网搜索。
   - 不重跑 [`scripts/collect-stable-sources.py`](scripts/collect-stable-sources.py)、[`scripts/collect-twitterapi-io.py`](scripts/collect-twitterapi-io.py) 或 [`scripts/update-state.py`](scripts/update-state.py)。
   - 不更新 `state/`、`raw/YYYY-MM-DD/`、`trend/` 专题报告或 `importance/` 深挖文档。

## 隐私边界

- `reviews/raw/` 是 ignored 目录，只保存本地 session 摘要，不进入 git。
- `reviews/YYYY-MM-DD-evening-review.md` 是可追踪沉淀文档，但正文应只写归纳，不复制长段聊天原文。
- 如 session 涉及私人事务、账号、医疗、财务、身份文件或其它敏感内容，只写抽象主题和下一步，不写可识别细节。
- 如果当天没有可用 Codex session，也要生成报告并写清 `no-session-data`。

## 每晚流程

1. 确定日期
   - 默认使用 Asia/Shanghai 当天日期。
   - 如果手动补跑，显式传入 `--date YYYY-MM-DD`。

2. 提取 session 摘要
   - 运行 `python3 scripts/extract-codex-sessions.py --date YYYY-MM-DD`。
   - 核对输出中的 `session_count` 和 `question_count`。
   - 如果 `question_count=0`，报告只写覆盖范围、无追问数据和下一步建议，不编造主题。

3. 读取当天弱链接材料
   - 如果当天 `docs/YYYY-MM-DD-daily-intel.md` 存在，只作为背景链接。
   - 如果当天 `trend/reports/YYYY-MM-DD-trend-report.md` 存在，只作为背景链接。
   - 不复述日报高信号，不补外部证据，不更新 trend 判断。

4. 写复盘报告
   - 输出路径：`reviews/YYYY-MM-DD-evening-review.md`
   - 语言使用中文，保留英文产品名、repo、API、文件名和命令。
   - 结构必须包含：
     - 今日追问地图
     - 反复出现的困惑
     - 可沉淀资产候选
     - 可直接派给 Agent 的下一批任务
     - Parent Research Handoff Notes
     - 明天继续的 3 件事
     - 和今日情报的弱链接
     - 边界与完成审计

5. 完成审计
   - 确认 `reviews/YYYY-MM-DD-evening-review.md` 已写入。
   - 确认 `reviews/raw/YYYY-MM-DD/codex-sessions.json` 已写入且被 `.gitignore` 忽略。
   - 确认没有修改 daily source 的 `raw/`、`state/`、`trend/` 专题报告或早上 automation。
   - 确认报告没有复制大段 session 原文或 ChatGPT 网页内容。

## 报告写法

### 今日追问地图

按主题聚合 3-7 条问题线。每条写：

- 你今天追问的核心问题是什么。
- 它属于工程、研究、自动化、写作、个人事务还是知识库维护。
- 目前已经得到什么结论。
- 还缺什么最小验证。

### 反复出现的困惑

只记录会复发、会消耗精力、适合转成规则或工具的问题。不要把一次性闲聊写成长期困惑。

### 可沉淀资产候选

每条候选必须说明建议沉淀成哪类资产：

- `importance/` 深挖
- skill
- AGENTS 规则
- automation
- runbook
- prompt/template

### 可直接派给 Agent 的下一批任务

给 3-5 条可以在第二天直接交给 Codex 执行的任务候选。它们是“可派单草稿”，不是本次晚间 automation 要立即执行的任务。

每条必须写清：

- 任务标题：一句话说明要推进什么。
- 输入：需要读取哪些本地报告、session 摘要、repo 文件或外部资料链接。
- 产出：应生成或修改哪个文档、报告、skill、runbook 或 checklist。
- 停止条件：做到什么程度就停，避免开放式发散。
- 边界：明确不做什么，例如不联网、不改 runtime code、不 push、不更新 trend 判断。

任务优先来自当天反复追问和可沉淀资产候选；如果当天问题很零散，可以只给 1-2 条高置信任务，不要凑数。

### Parent Research Handoff Notes

本节是给父级 [`../`](../) `research-docs` 的兜底 handoff 提醒，不是本次晚间 automation 要执行的任务，也不是 queue、registry 或 scheduled utility 输入。没有事项时写 `none`。

DSI live session 中如果用户说 `handoff 给父仓`、`丢到父仓分析`、`立即移交`、`开父仓继续`、`纳入长期计划`、`长期跟踪`、`短期看一看`、`先观察`、`移交父仓`、`立即处理`、`现在处理` 等，主路径是使用子仓本地 skill [`research-docs-handoff`](.agents/skills/research-docs-handoff/SKILL.md) 生成 handoff，并让用户在父仓手动接管。

晚间复盘只整理当天没有 live handoff 的遗留项。已经生成 live handoff 的事项，应在本节链接 `reviews/YYYY-MM-DD-live-handoffs.md`，不要重复生成完整 signal。

每条 handoff note 必须包含：

- `title`：一句话标题。
- `origin_question`：来自当天追问或复盘的原始问题。
- `source_artifacts`：可点击相对链接，至少包含本晚间复盘；如相关，链接当天日报、trend report 或 raw 证据。
- `topic_action`：`existing` 或 `new`。DSI 先扫描父仓 `README.md` 的 `## Topics` 表决定，不留给父仓重判。
- `topic_dir`：父仓要执行的目标 topic 目录。
- `target_doc`：父仓要创建或更新的目标研究文档。
- `desired_output`：希望父仓产出什么，例如 chat answer、topic doc、README update、source archive。
- `stop_condition`：做到什么程度停止。
- `boundary`：明确不做什么，例如不改 automation、不复制 DSI 正文、不直接创建父仓 topic。
- `handoff_status`：`live-handoff-created` 或 `candidate`。

状态含义：

- `live-handoff-created`：已经生成 handoff，父仓可直接读取 handoff 路径继续。
- `candidate`：值得父仓继续，但还没有 live handoff；等待用户手动触发。

常用映射：

- `纳入长期计划`、`长期跟踪`、`沉淀成长期研究`：如果用户在 live session 中提出，优先立刻生成 handoff；否则写 `candidate`。
- `短期看一看`、`先观察`、`不急`：只有当它明显需要父仓研究或归档时才写 `candidate`；普通观察留在 DSI trend。
- `立即处理`、`现在处理`、`马上做`、`手动启动`：优先立刻生成 handoff，并提醒用户去父仓可见 session 说 `接这个 handoff: <handoff_path>`。

DSI 只产生 live handoff、handoff notes 和 provenance，并负责给出 topic 判定。父仓只负责按 handoff 执行归档证据、写研究文档和同步根 `README.md` topic 表。晚间复盘不得直接创建父仓 topic 或修改父仓文件。

### 明天继续的 3 件事

只给 3 条，面向人的明日决策和检查动作。它和“可直接派给 Agent 的下一批任务”不同：这里回答“你明天最应该看什么、拍板什么、检查什么”，不要变成 Agent 派单列表的重复。

### 和今日情报的弱链接

只链接当天报告，例如：

- [`docs/YYYY-MM-DD-daily-intel.md`](docs/README.md)
- [`trend/reports/YYYY-MM-DD-trend-report.md`](trend/reports/README.md)

如果当天报告不存在，写清 `missing-daily-report` 或 `missing-trend-report`。

## 自动化摘要

自动化最终回复只需要短摘要：

- 读取的 session 数和追问数。
- 生成的 report 路径。
- 是否找到当天 daily/trend 弱链接。
- 是否有 ignored raw 摘要。
- 边界：未联网、未读 ChatGPT、未修改 daily/trend。
