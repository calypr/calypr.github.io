# CALYPR Tool Ecosystem

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

### [Forge](forge/index.md)
**Project formatting**
Forge scans a data repository to build an integrated FHIR based graph of samples and all the files connected to the project. It is responsible for schema checking and database loading. You can use it client side to verify and debug your project and on the server side, it is used to load databases.

### [Data Client](data-client/index.md)
A client command line interface for interfacing with the Calypr system.

### [Sifter](sifter/index.md)
**Data Transformation**
Sifter is a tool for rapid data extraction and transformation. 


---

!!! tip "Getting Started"
    If you are new to the platform, we recommend starting with the [Quick Start Guide](../calypr/quick-start.md) to install the necessary binaries and set up your first workspace.
