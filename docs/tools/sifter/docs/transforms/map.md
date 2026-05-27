---
title: map
menu:
  main:
    parent: transforms
lead: "Run function on every row"
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

# map

Run function on every row

## Parameters

| name | Description |
| --- | --- |
| method | Name of function to call |
| python | Python code to be run |
| gpython | Python code to be run using GPython| 

## Example

```yaml
    - map:
        method: response
        gpython: |
          def response(x):
            s = sorted(x["curve"].items(), key=lambda x:float(x[0]))
            x['dose_um'] = []
            x['response'] = []
            for d, r in s:
              try:
                dn = float(d)
                rn = float(r)
                x['dose_um'].append(dn)
                x['response'].append(rn)
              except ValueError:
                pass
            return x
```