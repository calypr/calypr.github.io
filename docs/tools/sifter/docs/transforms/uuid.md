---
title: uuid
render_macros: false
lead: "Generate a UUID for a field."
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

# uuid

Generate a UUID for a field.

## Parameters

| Name | Type | Description |
| --- | --- | --- |
| field | string | Destination field name for the UUID |
| value | string | Seed value used to generate the UUID |
| namespace | string | UUID namespace (optional) |

## Example

```yaml
    - uuid:
        field: id
        value: "{{row.name}}"
```