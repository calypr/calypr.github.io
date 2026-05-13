# Open-Source Tool Docs

This is the technical reference area for the CALYPR toolchain. It is intentionally behind the product and solution pages so non-technical readers do not have to start with implementation detail.

## Data Lake Tools

### [Git-DRS](git-drs/index.md)

Git-DRS provides Git-style versioning for large DRS-backed research data. Use it when teams need reproducible data references without committing large binaries to Git.

### [Syfon](syfon/index.md)

Syfon is the DRS and storage mediation service. It handles object registration, presigned upload and download URLs, bucket routing, and server-side storage access.

## Workflow And Discovery

### [Funnel](funnel/index.md)

Funnel implements the GA4GH Task Execution Service API for portable workflow execution across distributed compute environments.

### [GRIP](grip/index.md)

GRIP provides graph database and query capabilities for complex biomedical relationships and integrated project data.

## Data Preparation And Operations

### [Forge](forge/index.md)

Forge validates, publishes, and harmonizes project metadata before it is loaded into shared research systems.

### [Sifter](sifter/index.md)

Sifter supports data extraction and transformation workflows.

### [Data Client](data-client/index.md)

The data client provides command-line operations for CALYPR data workflows, authentication, and project interactions.
