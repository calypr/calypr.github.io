# Git-DRS

!!! note
    The tools listed here are under development and may be subject to change.

## Overview

Use case: As an analyst, in order to share data with collaborators, I need a way to create a project, upload files and associate those files with metadata. The system should be capable of adding files in an incremental manner.

The following guide details the steps a data contributor must take to submit a project to the CALYPR data commons.

### Core Concepts

> In a Gen3 data commons, a semantic distinction is made between two types of data: "data files" and "metadata". [more](https://gen3.org/resources/user/dictionary/#understanding-data-representation-in-gen3)

*   **Data File**: Information like tabulated data values in a spreadsheet or a fastq/bam file containing DNA sequences. The contents are not exposed to the API as queryable properties.
*   **Metadata**: Variables that help to organize or convey additional information about corresponding data files so they can be queried.

## 1. Setup

CALYPR project management is handled using standard Git workflows. you will need the **Large File Storage (LFS)** plugin to track genomic data files and the **Git-DRS** plugin to interface with CALYPR's storage and indexing systems.

Visit the [Quick Start Guide](../../quick-start.md) for detailed, OS-specific installation instructions for these tools.

| Tool | Purpose |
| :--- | :--- |
| **git-drs** | Manages large file tracking, storage, and DRS indexing. |
| **forge** | Handles metadata validation, transformation (ETL), and publishing. |
| **data-client** | Administrative tool for managing [collaborators and access requests](../../tools/data-client/access_requests.md). |
{: .caption }

## 2. Initialize Project

Once tools are installed and credentials are configured (see [Quick Start](../../quick-start.md)), initialize your project.

### Formatting a new project

If you are creating a new project, you may need to initialize some of the storage parameters. These define how the DRS system stores files related to your project.

```bash
# Clone new repository
git clone https://github.com/your-org/new-calypr-repo.git
cd new-calypr-repo

# Initialize with full configuration
git drs init --profile calypr \
             --url https://calypr-public.ohsu.edu/ \
             --cred ~/Downloads/calypr-credentials.json \
             --project my-project-id \
             --bucket my-bucket-name
```
*Get project details from your data coordinator if needed.*

### Directory Structure

An initialized project will look something like this:

```
<project-root>/
├── .gitattributes
├── .gitignore
├── META/
│   ├── ResearchStudy.ndjson
│   ├── DocumentReference.ndjson
│   └── <Other FHIR>.ndjson
├── data/
│   ├── file1.bam
│   └── file2.fastq.gz
```

### Verify configuration

You'll want to double check your storage settings, to ensure you know where files are being stored. Use the DRS remote list command:

```bash
git drs remote list
```

## 3. Manage Files

By using git-lfs and git-drs you will have a number of different options to add new files to a project.

### 3.1: Configure File Tracking

You'll need check which files LFS is tracking. If LFS doesn't track a file, it might be uploaded to Github directly, which should be avoided for large files.

```bash
# View current tracking
git lfs track

# Track specific file extensions
git lfs track "*.bam"
git lfs track "*.vcf.gz"

# Commit tracking configuration
git add .gitattributes
git commit -m "Configure LFS file tracking"
git push
```

### 3.2: Add Local Files

```bash
# Add data files
git add data/sample1.bam
git add data/sample2.bam
git add results/analysis.vcf.gz

# Verify LFS is tracking them (should show * prefix for staged LFS files)
git lfs ls-files
```

### 3.3: Register S3 Files

If you have files that are already on S3, you can register them without downloading them.

```bash
# Register file with inline credentials
git drs add-url s3://bucket-name/path/to/file.bam \
  --sha256 abc123def456... \
  --aws-access-key "your-access-key" \
  --aws-secret-key "your-secret-key"
```

## 4. Commit and Upload

Once files are added or registered, commit your changes to sync with the CALYPR platform.

```bash
# Commit files (creates DRS records via pre-commit hook)
git commit -m "Add genomic data files"

# Upload to object store and register DRS records
git push
```

**What happens during push:**
1.  Git-DRS creates DRS records for each tracked file.
2.  Files are uploaded to the configured S3 bucket.
3.  DRS URIs are registered in the Gen3 system.
4.  Pointer files are committed to the repository.

### Verifying upload

```bash
git lfs ls-files
```

Files should now show `*` prefix (localized/uploaded). After completing the workflow:
*   Files are visible in Git repository (as LFS pointers)
*   DRS records are created
*   Files are accessible via `git lfs pull`
*   You can share DRS URIs with collaborators