# CALYPR Tool Ecosystem

The CALYPR platform provides a suite of powerful, open-source tools designed to handle every stage of the genomic data lifecycle—from ingestion and versioning to distributed analysis and graph-based discovery.

---

### [Git-DRS](/tools/git-drs/)
**The Version Control Layer.**  
Git-DRS is a specialized extension for Git that manages massive genomic datasets using the GA4GH Data Repository Service (DRS) standard. It allows researchers to track, version, and share petabyte-scale files as easily as code, replacing heavy binaries with lightweight pointer files that resolve to immutable cloud objects.

### [Syfon](/tools/syfon/)
**The Data Service Layer.**  
Syfon is CALYPR's DRS and storage mediation service. It handles object registration, presigned upload and download URLs, bucket routing, authentication modes, and the server-side configuration that lets higher-level tools move data cleanly between repositories, commons services, and object storage.

### [Funnel](/tools/funnel/)
**The Compute Layer.**  
Funnel is a distributed task execution engine that implements the GA4GH Task Execution Service (TES) API. It provides a standardized way to run Docker-based analysis pipelines across diverse environments—including Kubernetes, AWS, and Google Cloud—ensuring that your workflows are portable and independent of the underlying infrastructure.

### [GRIP](/tools/grip/)
**The Discovery Layer.**  
GRIP (Graph Resource Integration Platform) is a high-performance graph database and query engine designed for complex biological data. It enables analysts to integrate heterogeneous datasets into a unified knowledge graph and perform sophisticated queries that reveal deep relational insights across multi-omic cohorts.

### [Forge](/tools/forge/)
**Project formatting**
Forge scans a data repository to build an integrated FHIR based graph of samples and all the files connected to the project. It is responsible for schema checking and database loading. You can use it client side to verify and debug your project and on the server side, it is used to load databases.

### [Data Client](/tools/data-client/)
A client command line interface for interfacing with the Calypr system.

### [Sifter](/tools/sifter/)
**Data Transformation**
Sifter is a tool for rapid data extraction and transformation. 
