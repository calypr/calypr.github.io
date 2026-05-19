---
title: xml
render_macros: false
lead: "| name | Description | | --- | --- | | path | Path to input file |"
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

# xml
Load an XML file

## Parameters

| name | Description |
| --- | --- |
| path | Path to input file |

## Example

```yaml
inputs:
  loader:
    xmlLoad:
      path: "{{params.xmlPath}}"
```