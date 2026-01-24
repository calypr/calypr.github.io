---
title: graphBuild
render_macros: false
---

# Output: graphBuild

Build graph elements from JSON objects using the JSON Schema graph extensions.


# example
```yaml
      - graphBuild:
          schema: "{{params.allelesSchema}}"
          title: Allele
```