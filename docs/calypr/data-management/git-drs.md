
## **3.5: Commit and Upload you files** {#3.5:-commit-and-upload-you-files}

\# Commit files (creates DRS records via pre-commit hook)  
git commit \-m "Add genomic data files"

\# Upload to object store  
git push

What happens during push:

1. Git-DRS creates DRS records for each tracked file  
2. Files are uploaded to the configured S3 bucket  
3. DRS URIs are registered in the Gen3 system  
4. Pointer files are committed to the repository

## 

### 3.5.1 Verifying upload {#3.5.1-verifying-upload}

git lfs ls-files

Files should now show \* prefix (localized/uploaded):

\* data/sample1.bam  
\* data/sample2.bam  
\* results/analysis.vcf.gz

The \- prefix means files are staged but not yet committed.

After completing the workflow:

*  Files visible in Git repository (as LFS pointers)  
*  DRS records created (check .drs/ logs)  
*  Files accessible via git lfs pull  
*  Can share DRS URIs with collaborators  
*  Files NOT searchable in CALYPR web interface (expected)

## 4.5: Committing Changes {#4.5:-committing-changes}

\# Stage all changes  
git add .

\# Commit (triggers forge precommit hook)  
git commit \-m "Register S3 files with custom FHIR metadata"

\# Push to register DRS records  
git push

What happens during push:

1. Git-DRS creates DRS records pointing to S3  
2. DRS URIs are registered  
3. No file upload occurs  
4. Pointer files committed to repository