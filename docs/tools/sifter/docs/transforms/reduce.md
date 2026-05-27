---
title: reduce
menu:
  main:
    parent: transforms
lead: "Using key from rows, reduce matched records into a single entry"
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

# reduce

Using key from rows, reduce matched records into a single entry

## Parameters

| name | Type | Description |
| --- | --- | --- |
| field | string (field path) | Field used to match rows | 
| method | string | Method name |
| python | string | Python code string |
| gpython | string | Python code string run using (https://github.com/go-python/gpython) |
| init | `map[string]any` | Data to use for first reduce | 

## Example

```yaml
    - reduce:
        field: dataset_name
        method: merge
        init: { "compounds" : [] }
        gpython: |

          def merge(x,y):
            x["compounds"] = list(set(y["compounds"]+x["compounds"]))
            return x
```