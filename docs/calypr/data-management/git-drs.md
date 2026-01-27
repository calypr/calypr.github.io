---
title: Managing projects with git-drs
---

git-drs is used to manage project data. It connects git projects to the DRS datalake, allowing users to create new versions of projects, incorporating large scale data objects, without duplicating storage.

## Basic Workflow

### 1. Adding Files

Use git-drs to add files with metadata associations:

```bash
# Add a genomic file with patient and specimen associations
git-drs add sample.cram --patient P001 --specimen P001-BM --task P001-SEQ

# Add multiple files
git-drs add *.bam --patient P001
```

### 2. Generate Metadata

Create FHIR metadata from the file manifest:

```bash
git-drs meta init
```

This creates FHIR resources in the `META/` directory:
- `ResearchStudy.ndjson` - Project description
- `DocumentReference.ndjson` - File information
- Additional resources based on flags (Patient, Specimen, Task, etc.)

### 3. Commit and Upload

Commit files and metadata to create DRS records:

```bash
# Stage all changes (including metadata)
git add META/
git-drs commit -m "Add genomic data with FHIR metadata"
```

Upload to object store and register DRS records:

```bash
git-drs push
```

## What Happens During Push

1. **DRS Record Creation**: git-drs creates DRS records for each tracked file
2. **File Upload**: Files are uploaded to the configured S3 bucket
3. **URI Registration**: DRS URIs are registered in the CALYPR system
4. **Pointer Management**: LFS pointer files are committed to the repository

## Verifying Upload

Check the status of tracked files:

```bash
git lfs ls-files
```

Files show different prefixes:
- `*` prefix: Files are localized/uploaded
- `-` prefix: Files are staged but not yet committed

Example output:
```
* data/sample1.bam  
* data/sample2.bam  
* results/analysis.vcf.gz
```

## Working with Custom FHIR Metadata

If you have existing FHIR metadata, you can supply it directly:

```bash
# Copy your FHIR data to META directory
cp ~/my-data/patients.ndjson META/
cp ~/my-data/specimens.ndjson META/
cp ~/my-data/document-references.ndjson META/

# Stage and commit
git add META/
git-drs commit -m "Add custom FHIR metadata"
git-drs push
```

## Data Access After Upload

After completing the workflow:

- **Files** are visible in Git repository (as LFS pointers)  
- **DRS records** are created and accessible via CALYPR
- **Download** available via `git lfs pull`
- **Sharing** possible through DRS URIs with collaborators
- **Discovery** files become searchable in CALYPR web interface after processing

## Troubleshooting

Common issues are covered in the [Common Errors guide](common-errors.md).

---
*Last reviewed: January 2026*