---
title: split
menu:
  main:
    parent: transforms
lead: "Split a field using string sep ## Parameters"
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

# split

Split a field using string `sep`
## Parameters

| name | Type | Description |
| --- | --- | --- |
| field | string | Field to the split |
| sep | string | String to use for splitting |

## Example

```yaml
    - split:
        field: methods
        sep: ";"
```