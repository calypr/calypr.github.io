---
title: objectValidate
render_macros: false
lead: "Use JSON schema to validate row contents"
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

# objectValidate

Use JSON schema to validate row contents

# parameters

| name | Type | Description |
| --- | --- | --- |
| title | string | Title of object to use for validation |
| schema | string | Path to JSON schema definition |

# example

```
    - objectValidate:
        title: Aliquot
        schema: "{{params.schema}}"
```