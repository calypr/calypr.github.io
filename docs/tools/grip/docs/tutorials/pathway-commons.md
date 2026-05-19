---
lead: "Get Pathway Commons release curl -O http://www.pathwaycommons.org/archives/PC2/v10/PathwayCommons10.All.BIOPAX.owl.gz"
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
Get Pathway Commons release
```
curl -O http://www.pathwaycommons.org/archives/PC2/v10/PathwayCommons10.All.BIOPAX.owl.gz
```

Convert to Property Graph
```
grip rdf --dump --gzip pc PathwayCommons10.All.BIOPAX.owl.gz -m "http://pathwaycommons.org/pc2/#=pc:" -m "http://www.biopax.org/release/biopax-level3.owl#=biopax:"
```
