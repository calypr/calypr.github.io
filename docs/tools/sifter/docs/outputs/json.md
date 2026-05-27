---
title: json
menu:
  main:
    parent: transforms
lead: "Send data to output file."
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

# Output: json

Send data to output file. The naming of the file is `outdir`/`path`

## Parameters

| name | Type | Description |
| --- | --- | --- |
| path | string | Path to output file |

## example

```yaml
output:
  outfile:
    json: 
      path: protein_compound_association.ndjson
```