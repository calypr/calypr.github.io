---
title: Funnel
---

# Funnel

Funnel provides task execution and workflow orchestration around the GA4GH TES model.

It is designed to streamline distributed batch processing by exposing a simple task API and a set of components that can be adapted to different compute and storage backends.

## Connect to a remote server

Use `-S` to point a command at a Funnel server, or set `FUNNEL_SERVER` for your shell:

```sh
funnel -S https://funnel.example.com task list
export FUNNEL_SERVER=https://funnel.example.com
funnel task list
```

The `-S` flag takes precedence over `FUNNEL_SERVER` when both are set.

## Read Next

- [Architecture Overview](docs/docs.md)
- [Download & Installation](docs/download.md)
- [Tasks](docs/tasks.md)
