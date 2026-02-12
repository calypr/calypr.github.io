---
title: Quick Start Guide
---

# CALYPR Quick Start Guide

Welcome to CALYPR! This guide will walk you through the essential workflow for managing and analyzing genomic data on the CALYPR platform.

## What is CALYPR?

CALYPR is a genomic data science platform that combines the best of cloud-based data commons with familiar version control tools. Think of it as "Git for genomic data" — you can version, track, and collaborate on massive datasets while maintaining full reproducibility.

**Key Benefits:**

- **Version Control**: Track genomic data files like you track code
- **Interoperability**: Built on GA4GH standards (DRS, TES) for seamless data sharing
- **Scalability**: From a few samples to petabyte-scale cohorts
- **Reproducibility**: Every analysis tied to specific versions of data and metadata

## What You'll Learn

This guide covers the essential CALYPR workflow:

1. **Getting access** to the CALYPR platform
2. **Uploading data files** with Git-DRS
3. **Adding metadata** with Forge
4. **Running analyses** with Funnel (optional)
5. **Querying data** with GRIP (optional)

## Prerequisites

Before you begin, make sure you have:

- **Git** installed on your system ([download](https://git-scm.com))
- **Access to CALYPR** - contact your project administrator for an account
- **Basic command-line experience** - familiarity with terminal/shell commands

---

## The CALYPR Workflow

### Step 1: Get Your API Credentials

To interact with CALYPR, you need API credentials from the Gen3 data commons. You'll download these from your profile page on the CALYPR portal as a JSON file.

API credentials expire after 30 days, so you'll need to download fresh credentials regularly.

**Learn More:** [Download Gen3 API Credentials](../tools/git-drs/quickstart.md#download-gen3-api-credentials) — Step-by-step instructions with screenshots

---

### Step 2: Upload Your Data Files (Git-DRS)

**Git-DRS** is CALYPR's data file management tool. It extends Git LFS to version and track large genomic files while automatically registering them with the DRS (Data Repository Service).

Git-DRS lets you:
- Version large data files (BAM, FASTQ, VCF, etc.) like you version code
- Track file lineage and share data with collaborators
- Automatically register files with DRS for global discovery

When you push files, Git-DRS uploads them to S3, registers DRS records in Gen3, and stores only lightweight pointer files in your Git repository.

**Learn More:** [Git-DRS Complete Documentation](../tools/git-drs/quickstart.md) — Installation, setup, and detailed workflows

---

### Step 3: Add Metadata (Forge)

**Forge** is CALYPR's metadata management tool. It validates and publishes structured metadata about your samples, making your data discoverable and queryable.

Forge helps you:
- Validate metadata against Gen3 data models
- Publish metadata to make your data searchable
- Manage relationships between samples, subjects, and files

While you can upload files before metadata, adding metadata early maximizes the value of your data by making it discoverable and queryable.

**Learn More:** [Forge Documentation](../tools/forge/index.md) — Installation, validation, and publishing workflows

---

### Step 4: Run Analysis Workflows (Funnel) — Optional

**Funnel** is CALYPR's task execution service. It runs computational workflows across cloud and HPC environments using the GA4GH Task Execution Service (TES) standard.

Funnel enables you to:
- Execute containerized workflows (Docker/Singularity)
- Manage resources across AWS, GCP, and HPC clusters
- Track task status and integrate with workflow engines (Nextflow, WDL)

Funnel is typically used for production pipelines and large-scale analysis. For exploratory work, you might run analyses locally first.

**Learn More:** [Funnel Documentation](../tools/funnel/index.md) — Task definitions, execution, and cluster integration

---

### Step 5: Query Your Data (GRIP) — Optional

**GRIP** (Graph Resource Integration Platform) enables powerful graph-based queries across integrated datasets.

GRIP allows you to:
- Query relationships between samples, subjects, and files
- Perform complex graph traversals and aggregations
- Run federated queries across data commons

GRIP is most useful after you've integrated metadata and established relationships between entities.

**Learn More:** [GRIP Documentation](../tools/grip/index.md) — Query syntax, graph traversals, and examples

---

## Next Steps

Now that you understand the basic CALYPR workflow, here are some recommended next steps:

### 📚 Dive Deeper

- **[Data Management](data-management/git-drs.md)** - Advanced Git-DRS workflows
- **[Metadata Guide](data-management/metadata.md)** - Data modeling and metadata best practices
- **[Project Management](project-management/create-project.md)** - Creating and managing CALYPR projects

### 🔧 Tool Documentation

- **[Git-DRS Complete Guide](../tools/git-drs/quickstart.md)** - Comprehensive Git-DRS documentation
- **[Forge Reference](../tools/forge/index.md)** - Metadata validation and publishing
- **[Funnel Workflows](../tools/funnel/index.md)** - Task execution and pipeline management
- **[GRIP Queries](../tools/grip/index.md)** - Graph-based data queries

### 🆘 Get Help

- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions
- **[Platform Overview](index.md)** - Learn more about CALYPR architecture

### 💬 Community

CALYPR is in active development. Have questions or feedback? Reach out to the CALYPR team or your project administrator.

---

## Summary

You've learned the essential CALYPR workflow:

✅ **Access** - Get Gen3 API credentials  
✅ **Upload** - Use Git-DRS to version and track data files  
✅ **Annotate** - Use Forge to add and validate metadata  
✅ **Analyze** - Use Funnel to run computational workflows (optional)  
✅ **Query** - Use GRIP to explore data relationships (optional)

Each tool builds on the previous step, creating a complete data lifecycle from upload to analysis. Start with the basics (access, upload, annotate) and add advanced features as your needs grow.

Happy analyzing! 🧬
