# CALYPR Platform

Welcome to the **CALYPR Platform**. CALYPR is a next-generation genomic data science ecosystem designed to bridge the gap between massive, centralized data commons and the agile, distributed workflows of modern researchers.


## The CALYPR Philosophy

Traditional data repositories often create data silos where information is easy to store but difficult to move, version, or integrate with external tools. CALYPR breaks these silos by embracing **Interoperability**, **Reproducibility**, and **Scalability**.

### 1. Interoperability (GA4GH Standards)
CALYPR is built from the ground up on [GA4GH](https://www.ga4gh.org/) standards. By using the **Data Repository Service (DRS)** and **Task Execution Service (TES)**, CALYPR ensures that your data and workflows can move seamlessly between different cloud providers and on-premises high-performance computing (HPC) clusters. 
The data system is based on the Fast Healthcare Interoperability Resources (FHIR) standard.

### 2. Reproducibility (Git-like Data Management)
The core of the CALYPR experience is **Git-DRS**. We believe that data management should feel as natural as code management. Git-DRS allows you to track, version, and share massive genomic datasets using the familiar `git` commands, ensuring that every analysis is backed by a specific, immutable version of the data.

### 3. Scalability (Hybrid Cloud Infrastructure)
Whether you are working with a few genomes or petabyte-scale cohorts, CALYPR's architecture—powered by **Gen3**—scales to meet your needs. Our hybrid cloud approach allows for secure data storage in AWS while leveraging your local compute resources when necessary.

---

## How it Works: The Connected Commons

CALYPR acts as the "connective tissue" between your research environment and the cloud:

*   **Data Commons ([Gen3](https://gen3.org)):** Provides the robust backend for metadata management, indexing, and authentication.
*   **Version Control ([Git-DRS](../tools/git-drs/index.md)):** Manages the check-in and check-out operations for large files, allowing you to treat remote DRS objects as local files.
*   **Metadata Orchestration ([Forge](../tools/forge/index.md)):** Streamlines the validation, publishing, and harmonizing of genomic metadata.
*   **Compute ([Funnel](../tools/funnel/index.md)):** Executes complex pipelines across distributed environments using standardized task definitions.
*   **Graph Insights ([GRIP](../tools/grip/index.md)):** Enables high-performance queries across heterogeneous datasets once integrated.

---

!!! info "Private Beta"
    CALYPR platform is currently in a private beta phase. We are actively working with a select group of research partners to refine the platform. If you encounter any issues or have feature requests, please reach out to the team. The individual [tools](../tools/index.md) are available for public use.

---

## Next Steps
To get started:

1.  **[Quick Start Guide](quick-start.md):** The fastest way to install tools and start tracking data.
2.  **[Data & Metadata](data-management/meta-data.md):** Learn how to associate your biological metadata with the files you've uploaded.