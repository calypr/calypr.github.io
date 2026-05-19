---
title: hash
render_macros: false
lead: "| name | Type | Description | | --- | --- | --- | | field | string | Field to store hash value | | value | string | Templated string of value to be hashed | | method | string | Hashing method: sha1/sha256/md5 |"
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

# hash


# Parameters

| name | Type | Description |
| --- | --- | --- |
| field | string | Field to store hash value |
| value | string | Templated string of value to be hashed |
| method | string | Hashing method: sha1/sha256/md5 |

# example

```yaml
   - hash:
      value: "{{row.contents}}"
      field: contents-sha1
      method: sha1
```
