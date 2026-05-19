---
title: fieldParse
menu:
  main:
    parent: transforms
lead: "Parse a string field (e.g."
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

# fieldParse

Parse a string field (e.g. `key1=val1;key2=val2`) into individual keys.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| field | string | The field containing the string to be parsed |
| sep | string | Separator character used to split the string |

## Example

```yaml
    - fieldParse:
        field: attributes
        sep: ";"
```
