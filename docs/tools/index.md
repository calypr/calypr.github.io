# CALYPR Tools Ecosystem

The CALYPR platform provides a suite of powerful, open-source tools designed to handle every stage of the genomic data lifecycle—from ingestion and versioning to distributed analysis and graph-based discovery.

---

### [Git-DRS](git-drs/index.md)
**The Version Control Layer.**  
Git-DRS is a specialized extension for Git that manages massive genomic datasets using the GA4GH Data Repository Service (DRS) standard. It allows researchers to track, version, and share petabyte-scale files as easily as code, replacing heavy binaries with lightweight pointer files that resolve to immutable cloud objects.

### [Funnel](funnel/index.md)
**The Compute Layer.**  
Funnel is a distributed task execution engine that implements the GA4GH Task Execution Service (TES) API. It provides a standardized way to run Docker-based analysis pipelines across diverse environments—including Kubernetes, AWS, and Google Cloud—ensuring that your workflows are portable and independent of the underlying infrastructure.

### [GRIP](grip/index.md)
**The Discovery Layer.**  
GRIP (Graph Resource Integration Platform) is a high-performance graph database and query engine designed for complex biological data. It enables analysts to integrate heterogeneous datasets into a unified knowledge graph and perform sophisticated queries that reveal deep relational insights across multi-omic cohorts.


---

## Choosing the Right Tool

| If you want to... | Use this tool |
| --- | --- |
| Version and share large genomic files | **Git-DRS** |
| Run batch analysis or Nextflow pipelines | **Funnel** |
| Query complex relationships between datasets | **GRIP** |
| Access Gen3 data from the command line | **Data Client** |

---

!!! tip "Getting Started"
    If you are new to the platform, we recommend starting with the [Quick Start Guide](../calypr/quick-start.md) to install the necessary binaries and set up your first workspace.
