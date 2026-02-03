## Install Git, Git-LFS, & Git-DRS

CALYPR project management is handled using standard Git workflows. You will need the **Large File Storage (LFS)** plugin to track genomic data files and the **Git-DRS** plugin to interface with CALYPR's storage and indexing systems.

Visit the [Quick Start Guide](../quick-start.md) for detailed, OS-specific installation instructions for these tools.

Once these elements are set up, you'll need to configure your API credentials.

# Initialize Git-DRS
```bash
git drs remote add gen3 calypr --cred ~/Downloads/credentials.json --url https://calypr-public.ohsu.edu --project <project-id> --bucket <bucket-name>
```

| Tool | Purpose |
| :--- | :--- |
| **git-drs** | Manages large file tracking, storage, and DRS indexing. |
| **forge** | Handles metadata validation, transformation (ETL), and publishing. |
| **data-client** | Administrative tool for managing [collaborators and access requests](../../tools/data-client/access_requests.md). |

Table: Core CALYPR Command-Line Tools

To ensure that you don't automatically download all the large files associated with the project (which could take a long time), ensure you use the `--skip-smudge` flag:

```bash
# Clone repository
git clone https://github.com/your-org/your-calypr-repo.git
cd your-calypr-repo

# Initialize Git LFS but skip downloading large files
git lfs install --skip-smudge
```

### Formatting a new project

If you are creating a new project, you may need to initialize some of the storage parameters. These define how the DRS system stores files related to your project. 

```
# Clone new repository
git clone https://github.com/your-org/new-calypr-repo.git  
cd new-calypr-repo

# Initialize with full configuration  
git drs init \--profile calypr \\  
             \--url https://calypr-public.ohsu.edu/ \\  
             \--cred \~/Downloads/calypr-credentials.json \\  
             \--project my-project-id \\  
             \--bucket my-bucket-name
```
Get project details from your data coordinator if needed.

#### Directory Structure
```
<project-root\>/  
├── .gitattributes  
├── .gitignore  
├── META/  
│   ├── ResearchStudy.ndjson  
│   ├── DocumentReference.ndjson  
│   ├── Patient.ndjson           (optional)  
│   ├── Specimen.ndjson          (optional)  
│   ├── ServiceRequest.ndjson    (optional)  
│   ├── Observation.ndjson       (optional)  
│   └── \<Other FHIR\>.ndjson      (optional)  
├── data/  
│   ├── file1.bam  
│   ├── file2.fastq.gz  
│   └── \<additional files\>
```

---

#### Example Minimal Project 
```
my-project/  
├── .gitattributes  
├── META/  
│   ├── ResearchStudy.ndjson      \# 1 record  
│   ├── DocumentReference.ndjson  \# 2 records, one per file below  
├── data/  
│   ├── sample1.bam  
│   ├── sample2.fastq.gz
```

## Verify configuration

You'll want to double check your storage settings, to ensure you know where files are being stored. Use the DRS remote list command:

```
git drs remote list
```

The expected output would be:

```
default_remote: origin
remotes:
  origin:
    gen3:
      endpoint: https://caliper-public.ohsu.edu
      project_id: cbds-git_drs_test
      bucket: cbds

```

Next you'll need check with files LFS is tracking. If LFS doesn't track a file, it could be uploaded to Github. This should be avoided because it isn't managed by the Calypr project access control system and it isn't designed to store large files. 

To view the current files that are being tracked:  
```
git lfs track
```

You can add more files to be tracked using the `git lfs track` command
```
# Track specific file extensions  
git lfs track "\*.bam"  
git lfs track "\*.vcf.gz"  
git lfs track "\*.fastq.gz"

# Track entire directories  
git lfs track "data/\*\*"

# Commit tracking configuration  
git add .gitattributes  
git commit \-m "Configure LFS file tracking"  
git push
```

---

## Add Your Files

By using git-lfs and git-drs you will have a number of different options to add new files to a project. You can 1\) add a file that exists within your workspace, 2\) Add a file that has already been uploaded to an S3 bucket and 3\) Add a file that has already been registered with DRS. 

### Add local files 
```
# Add data files  
git add data/sample1.bam  
git add data/sample2.bam  
git add results/analysis.vcf.gz

# Verify LFS is tracking them  
git lfs ls-files
```

Expected output:

```
- data/sample1.bam  
- data/sample2.bam  
- results/analysis.vcf.gz
```

### Register S3 Files 

Using Environment Variables  
```

# Set AWS credentials  
export AWS\_ACCESS\_KEY\_ID="your-access-key"  
export AWS\_SECRET\_ACCESS\_KEY="your-secret-key"  
# Register file  
git drs add-url s3://bucket-name/path/to/file.bam \
  --sha256 abc123def456…  
``` 

Using Command Flags  
```
# Register file with inline credentials  
git drs add-url s3://bucket-name/path/to/file.bam \
  --sha256 abc123def456... \
  --aws-access-key "your-access-key" \
  --aws-secret-key "your-secret-key"
```

Using AWS Profile  
\[WIP\]

📖 More details: [Git-DRS Add-URL Docs](https://github.com/calypr/git-drs/blob/main/docs/adding-s3-files.md)
