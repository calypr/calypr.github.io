---
title: graphBuild
render_macros: false
lead: "Build graph elements from JSON objects using the JSON Schema graph extensions."
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

# Output: graphBuild

Build graph elements from JSON objects using the JSON Schema graph extensions.


# example
```yaml
      - graphBuild:
          schema: "{{params.allelesSchema}}"
          title: Allele
```