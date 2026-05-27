---
title: embedded
menu:
  main:
    parent: inputs
lead: "Load data from embedded structure"
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

# embedded
Load data from embedded structure


## Example

```yaml
inputs:
  data:
    embedded:
      - { "name" : "Alice", "age": 28 }
      - { "name" : "Bob", "age": 27 }
```