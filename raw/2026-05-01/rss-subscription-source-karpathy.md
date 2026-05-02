# RSS Subscription Source - Karpathy RSS Post

## Source Links

- Karpathy X post: https://x.com/karpathy/status/2018043254986703167
- Public mirror used for readable text: https://twstalker.com/karpathy/status/2018043254986703167
- HN popular blogs OPML gist: https://gist.github.com/emschwartz/e6d2bf860ccc367fe37ff953ba6de66b
- Refactoring English source article: https://refactoringenglish.com/blog/2025-hn-top-5/

## Local Decision

The post recommends returning to RSS/Atom feeds for higher-signal longform sources and points to an OPML list of 92 blogs popular on Hacker News in 2025.

For this project, only a curated subset was added to `daily-source-intelligence/config/sources.yaml`, focused on:

- LLM / AI agent
- AI coding / developer tooling
- broad infrastructure / security / systems / ops
- indie founder / product growth

The full OPML was not imported to avoid flooding the daily digest with broad, low-priority content.

After scope adjustment, broad infra sources were retained. Non-target feeds such as Apple commentary, broad frontend writing, software-methods writing, and source-metadata feeds were removed from `config/sources.yaml`. The retained Karpathy/HN subset currently has 16 feeds.
