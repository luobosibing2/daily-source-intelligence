# 通过 follow-builders 接入播客 transcript

- Lifecycle: `implemented`
- Class: `architecture`
- Owner: Daily Source Intelligence maintainers
- Implemented: 2026-09-04
- Requirements: `REQ-POD-001`–`REQ-POD-017`
- Supersession: partially supersedes the podcast/feed non-goal in [`anthropic-engineering-and-x-source-expansion.md`](../feature/anthropic-engineering-and-x-source-expansion.md); its Anthropic Engineering and X decisions remain current.

## Problem

DSI 原有 RSS、X、GitHub 和官方页面链路不能表达 episode GUID、聚合 transcript、speaker/timestamp 覆盖和播客覆盖分母。把 follow-builders 的公开 JSON 当普通 RSS 正文，还会把它最多提供一集的编辑策略误写成六个节目的完整覆盖。

## Decision

DSI 将 `podcasts` 作为一等稳定通道。它从 follow-builders 公共 `feed-podcasts.json` 下载已经生成的 transcript，先归档完整原始 feed，再按本地允许节目和 GUID 生成单集 identity、metadata 和独立 transcript。实现见[播客采集器](../../../../scripts/collect-podcasts.py)和[来源配置](../../../../config/sources.yaml)。

节目 RSS 只按 GUID 精确补 canonical episode link，不做标题匹配、不请求 enclosure；Latent Space 直接使用发布方 RSS，不经过 pod2txt feed proxy。采集链不运行 pod2txt transcript API、不下载音频、不调用 ASR。

可读且处于北京时间目标日窗的 transcript 以 `podcast-transcript`、`secondary-source` 进入 signals、reading list、candidate audit、日报和可选 trend。完整 transcript 只留在 raw；报告遵循 [`runbook.md`](../../../../runbook.md) 的播客洞察卡合同，默认中文转述并保留 speaker/timestamp、说话人归属和聚合文本边界。

## Alternatives

1. **作为普通 RSS fulltext。** 没有采用，因为会丢失 GUID、provider、episode coverage、链接 fallback 和重试语义。
2. **复制 follow-builders 的 pod2txt 生成链。** 没有采用，因为用户要求直接消费现成内容且不要 ASR，也会引入 credential 和异步生成依赖。
3. **动态执行上游 podcast prompt。** 没有采用，因为远程 main 会静默改变 DSI 报告合同，并且其强制 direct quote 规则不满足本仓证据边界。

## Consequences

- 无需新增 transcript credential，即可把长对话接入既有报告链。
- 覆盖受 follow-builders 中央 feed 的选择和可用性限制；manifest 与日报只陈述实际 `offered` 数量，不声称逐节目完整。
- 第三方 transcript 可能包含听写和说话人误差，因此始终是 `secondary-source`；即使路径或内容出现公司名称，trend 也不能升级为官方来源。
- GUID 是稳定身份；playlist/channel 只保留为 alias。RSS 补链失败不丢 transcript，但必须暴露 `link_status=limited`。
- 上游未来新增节目不会自动进入本地允许集合。

## Durable boundaries

- 不调用 ASR、pod2txt transcript API 或音频下载。
- 不把 follow-builders 的 14 天窗口替代 DSI 北京时间日窗。
- 不把完整 transcript 复制进公开 Markdown/HTML bundle。
- 不强制直接引语，不猜测 transcript 未明确提供的人物身份、职位或事实归属。
- 不新增独立播客日报或发布路径。

## Verification obtained

- 67 个播客及下游定向测试通过，覆盖 feed/RSS 采集、重复 GUID 最长 transcript、SHA 一致性、CLI、signals、state、audit、strict validation 和 trend。
- 全仓 `python3 -m unittest discover -s tests -v` 共 101 个测试通过。
- Python 编译检查与 `git diff --check` 通过。
- 真实 follow-builders feed smoke test 返回 HTTP 200：`offered=1`、`allowed=1`、`inside=1`、`transcript_ok=1`、`link_ok=1`；43,857 字 transcript 的文件 SHA 与 metadata 一致。
- 真实 playlist URL 通过官方 RSS GUID 匹配为 Spotify 单集页面，并产生一个 GUID signal 和一个 reading-list entry，证据等级为 `secondary-source`。
