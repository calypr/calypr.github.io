---
title: query

menu:
  main:
    parent: commands
lead: "Run a query on a graph."
personas:
  - data-steward
  - platform-engineer
  - researcher-bioinformatician
  - standards-architecture-lead
solutions:
  - integrate-data
related_tools:
  - grip
---

```
grip query <graph> <query>
```

Run a query on a graph.

Examples
```bash
grip query pc12 'V().hasLabel("Pathway").count()'
```

