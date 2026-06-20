---
title: from
menu:
  main:
    parent: transforms
lead: "Start a pipeline from a named input or another pipeline."
personas:
  - data-steward
  - platform-engineer
  - workflow-engineer
  - standards-architecture-lead
solutions:
  - integrate-data
  - manage-compute
related_tools:
  - sifter
---

# from

Start a pipeline from a named input or another pipeline.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | Name of the input or pipeline to start from |

## Example

```yaml
pipelines:
  profileProcess:
    - from: profileReader
```