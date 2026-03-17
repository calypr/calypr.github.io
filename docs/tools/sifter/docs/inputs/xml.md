---
title: xml
render_macros: false
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