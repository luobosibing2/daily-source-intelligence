# Anthropic Engineering and X source expansion

- Status: implemented
- Class: feature
- Owner: Daily Source Intelligence maintainers
- Related requirements: `REQ-AE-001` through `REQ-AE-007`; `REQ-XE-001` through `REQ-XE-007`

## Decision

Daily Source Intelligence collects `Anthropic Engineering` as a first-party official source. The collector archives the Engineering index, parses canonical dated article cards, treats a parseable index with no Beijing-current-day cards as a valid zero result, and marks an unreadable or unparseable index as limited or failed. Current-day articles follow the existing HTTP-first and `opencli web read` fallback path. Article provenance and body status propagate through source health, manifest, seen state, unified signals, reading list, candidate audit, strict report validation, and the runbook.

The 23 handles discovered through `follow-builders@e4efaac15dbd2154dc2f342a439c56cd267339e6` are active X sources. They are enabled, non-priority, and have no account-default topics. Their posts use the existing 36-hour read-only `twitterapi.io` collection path and must match current topic text/card rules to enter a topic. Active handles are validated for case-insensitive uniqueness before credentials or network access.

## Alternatives

- Configuration-only `Anthropic Engineering` was rejected because it would not archive article bodies or enter the reading-list and audit chain.
- Consuming `follow-builders` feeds as source truth was rejected because they are mutable derived snapshots with different coverage and provenance contracts.
- A 30-day candidate audit before enabling the 23 X accounts was superseded by the user's explicit decision to enable them directly.
- Marking all new accounts priority or assigning topics from their names was rejected because enablement does not establish a priority or topic contract.
- A second X provider or browser fallback was rejected; the workflow remains on read-only `twitterapi.io` with no Exa, logged-in X, or action endpoints.

## Consequences

- Report writers must cover an in-window Anthropic Engineering article or give its missed audit row a disposition and note before strict validation passes.
- Index parser drift is visible as limited coverage rather than a false zero-new result.
- Active X collection grows from 27 to 50 accounts, increasing read requests and the daily denominator. Per-account zero and failure states remain coverage boundaries.
- New X sources receive no priority bonus or default topic membership. Their posts may remain in raw while absent from topic summaries when content does not match configured topics.

## Durable boundaries

- Anthropic Engineering history is not backfilled; outside-window cards only establish successful index parsing.
- A zero-new Engineering run does not mark the index URL as seen.
- The 23 X sources are not subjected to a separate candidate audit or automatic priority/topic assignment.
- No second X provider, Exa, logged-in browser, X write/action endpoint, podcast, transcript ASR, delivery channel, or publication behavior is added.

## Verification

- `python3 -m unittest discover -s tests` passed all 86 tests.
- Focused collector, signal, candidate-audit, validator, state, pipeline, X-source, and topic-brief tests passed.
- `git diff --check` and Python bytecode compilation passed.
- Live `https://www.anthropic.com/engineering` verification parsed 25 unique article cards with zero unknown dates. The 2026-09-03 run produced `status=ok`, `index_status=ok`, `items=[]`, and a real index snapshot. Replaying the latest parsed publication date, 2026-05-25, produced one current item with curl-archived raw HTML and readable fulltext.
- `collect-twitterapi-io.py --dry-run` returned 50 unique active sources; all 23 additions were enabled, non-priority, and without default topics. No real X API request was made during verification.
