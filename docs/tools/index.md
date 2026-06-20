---
lead: "This is the technical reference area for the CALYPR toolchain."
personas:
  - data-steward
  - platform-engineer
  - workflow-engineer
  - researcher-bioinformatician
  - standards-architecture-lead
solutions:
  - manage-data
  - manage-compute
  - integrate-data
  - manage-models
related_tools:
  - git-drs
  - syfon
  - funnel
  - forge
  - grip
  - sifter
  - data-client
---
# Open-Source Tool Docs

This is the technical reference area for the CALYPR toolchain. It is intentionally behind the product and solution pages so non-technical readers do not have to start with implementation detail.

## Data Lake Tools

### [Git-DRS](/tools/git-drs/)

Git-DRS provides Git-style versioning for large DRS-backed research data. Use it when teams need reproducible data references without committing large binaries to Git.

### [Syfon](/tools/syfon/)

Syfon is the DRS and storage mediation service. It handles object registration, presigned upload and download URLs, bucket routing, and server-side storage access.

## Workflow And Discovery

### [Funnel](/tools/funnel/)

Funnel implements the GA4GH Task Execution Service API for portable workflow execution across distributed compute environments.

### [GRIP](/tools/grip/)

GRIP provides graph database and query capabilities for complex biomedical relationships and integrated project data.

## Data Preparation And Operations

### [Forge](/tools/forge/)

Forge validates, publishes, and harmonizes project metadata before it is loaded into shared research systems.

### [Sifter](/tools/sifter/)

Sifter supports data extraction and transformation workflows.

### [Data Client](/tools/data-client/)

The data client provides command-line operations for CALYPR data workflows, authentication, and project interactions.
