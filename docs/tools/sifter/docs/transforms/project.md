---
title: project
render_macros: false
lead: "Populate row with templated values"
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

# project

Populate row with templated values


# parameters

| name | Type | Description |
| --- | --- | --- |
| mapping | map[string]any | New fields to be generated from template |
| rename | map[string]string | Rename field (no template engine) |


# Example

```yaml
    - project:
        mapping:
          type: sample
          id: "{{row.sample_id}}"
```