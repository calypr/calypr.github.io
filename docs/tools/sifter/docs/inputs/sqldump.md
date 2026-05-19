---
title: sqldump
render_macros: false
lead: "| Name | Type | Description | |-------|---|--------| | path | string | Path to the SQL dump file | | tables | []string | Names of tables to read out |"
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

# sqlDump
Scan file produced produced from sqldump. 

## Parameters

| Name | Type | Description |
|-------|---|--------|
| path | string | Path to the SQL dump file | 
| tables | []string | Names of tables to read out |

## Example

```yaml
inputs:
  database:
    sqldumpLoad:
      path: "{{params.sql}}"
      tables:
        - cells
        - cell_tissues
        - dose_responses
        - drugs
        - drug_annots
        - experiments
        - profiles
```
