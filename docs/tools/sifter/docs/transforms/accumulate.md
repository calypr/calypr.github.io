---
title: accumulate
menu:
  main:
    parent: transforms
lead: "Gather sequential rows into a single record, based on matching a field"
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

# accumulate

Gather sequential rows into a single record, based on matching a field

## Parameters

| name | Type | Description |
| --- | --- | --- |
| field | string (field path) | Field used to match rows | 
| dest | string | field to store accumulated records |

## Example

```
  - accumulate:
      field: model_id
      dest: rows   
```
