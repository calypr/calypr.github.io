---
title: distinct
render_macros: false
lead: "| name | Type | Description | | --- | --- | --- | | value | string | Key used for distinct value |"
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

# distinct
Using templated value, allow only the first record for each distinct key

## Parameters

| name | Type | Description |
| --- | --- | --- |
| value | string | Key used for distinct value |

## Example

```yaml
    - distinct:
        value: "{{row.key}}"
```