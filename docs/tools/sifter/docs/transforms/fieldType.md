---
title: fieldType
menu:
  main:
    parent: transforms
lead: "Set field to specific type, ie cast as float or integer"
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

# fieldType

Set field to specific type, ie cast as float or integer



# example
```yaml

    - fieldType:
        t_depth: int
        t_ref_count: int
        t_alt_count: int
        n_depth: int
        n_ref_count: int
        n_alt_count: int
        start: int

```