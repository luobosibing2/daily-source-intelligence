# Daily Source Intelligence Trend

本目录是 Daily Source Intelligence 的长期趋势分析层。

日报负责每天的发现、筛选和按主题归纳；`trend/` 负责把用户长期关注的主题沉淀成跨日判断、时间线、证据链和后续验证问题。日报正文不写 trend 小节，trend 在日报完成后单独更新。

## 文件结构

| 路径 | 作用 |
| --- | --- |
| [`../config/trends.yaml`](../config/trends.yaml) | 长期关注主题配置。`enabled: true` 的主题每天必须检查。 |
| [`reports/`](reports/) | 每日趋势分析报告目录，输出文件不随流程配置 commit。 |
| `memory-dream.md` | Memory & Dream 长期专题报告输出路径，包含时间线、阶段判断、证据强度和待验证问题。 |
| `financial-agents.md` | Financial Agents 长期专题报告输出路径，包含时间线、阶段判断、证据强度和待验证问题。 |
| `forward-deployed-engineering.md` | Forward Deployed Engineering 长期专题报告输出路径，包含企业 AI 落地、现场工程、产品反馈回路和服务化边界判断。 |
| `enterprise-delivery-system.md` | Enterprise Delivery System 长期专题报告输出路径，包含 AI agent 进入企业软件交付、治理门禁、上线质量、组织吞吐和跨团队交接的趋势判断。 |
| `codex-feature-watch.md` | Codex Feature Watch 长期专题报告输出路径，按功能面记录 OpenAI Codex 最近新增/强化了什么，版本号只作为证据锚点。 |
| `claude-code-feature-watch.md` | Claude Code Feature Watch 长期专题报告输出路径，按功能面记录 Claude Code 最近新增/强化了什么，版本号只作为证据锚点。 |
| `codex-claude-usage-tactics.md` | Codex & Claude Code Usage Tactics 长期专题报告输出路径，记录官方与高质量 practitioner 的使用技巧、prompt framing、repo-local memory、review/bug-hunt 方法和多 session 操作战术。 |
| [`raw/`](raw/) | trend 扩充搜索归档材料。 |

## 与其它目录的关系

- [`../docs/`](../docs/)：每日情报正文，不写长期趋势小节。
- [`../raw/`](../raw/)：每日采集 raw，是 trend 的输入证据之一。
- [`../importance/`](../importance/)：用户明确要求单独深挖的重要材料。trend 可以链接 importance，但不复制整篇研究报告。
- [`../config/watch.md`](../config/watch.md)：总关注面。`trends.yaml` 是长期专题配置，不替代 watch。

## 每日更新规则

1. 先完成当天日报。
2. 读取 [`../config/trends.yaml`](../config/trends.yaml)。
3. 从当天日报和 raw 中筛出命中 enabled trend 的高信号。
4. 对高信号补充官方页、官方 docs、GitHub repo、release body 或 README。
5. 把扩充材料写入 `raw/YYYY-MM-DD/<trend-id>/`。
6. 写当天 [`reports/`](reports/) 下的 trend report。
7. 更新对应专题报告：以 [`../config/trends.yaml`](../config/trends.yaml) 中 enabled trend 的 `timeline` 字段为准。
   - trend report 和专题报告中文优先：大多数行业术语、概念词、功能名和机制名直接翻译成自然中文；只有需要精确指代或方便回溯检索时才保留英文。
8. 中文译读阶段已退役；主 trend 产物完成后没有后置翻译步骤，不设置翻译相关环境变量，也不要生成 `translations/YYYY-MM-DD/` manifest、index、shard 或 `.zh.md` 派生产物。完成条件以 trend report、enabled topic 更新、trend raw marker 和 `run-trend-stage.py --check` 为准。

如果当天某个 enabled trend 没有新信号，trend report 必须写 `no-new-signal`；如果日报或 raw 缺失，必须写 `skipped` 和原因。

## 多重归类规则

同一条材料可以同时归入多个 trend。功能专题回答“这个产品最近新增/强化了哪些功能面”，主题专题回答“这个改动说明了什么长期趋势”。例如 Codex `0.134.0` 可以同时进入 Codex Feature Watch 和 Memory & Dream；Claude Code `v2.1.152` 可以同时进入 Claude Code Feature Watch、Memory & Dream 和 Enterprise Delivery System。多重归类时必须保留各自证据边界，不把 secondary-source 或 direct-x 升级成 official-source。
