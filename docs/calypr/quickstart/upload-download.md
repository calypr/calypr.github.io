---
title: Upload & Download Files
---

# Upload & Download Files

CALYPR supports two tools for transferring data files:

| | **Git DRS** | **data-client** |
|---|---|---|
| Best for | Version-controlled datasets, collaboration, reproducibility | Direct uploads without Git, scripted pipelines |
| Requires | Git repository initialized with `git drs init` | A configured `data-client` profile |
| Output | Files tracked in Git with DRS-backed pointer files | Files indexed in Gen3 (Indexd) with a GUID |

---

## Git DRS (recommended)

Git DRS integrates with your Git repository to track large files. Files are stored in S3 and registered with Gen3's DRS service — only lightweight pointer files live in Git.

### Upload

**1. Track the file type with Git LFS:**

```bash
git lfs track "*.bam"
git add .gitattributes
git commit -m "Track BAM files with Git LFS"
```

**2. Add, commit, and push:**

```bash
git add data/sample.bam
git commit -m "Add sample BAM file"
git push
```

On `git push`, Git DRS automatically:

1. Registers a DRS record in Gen3 (indexd)
2. Uploads the file to S3
3. Stores the pointer in the Git repository

You can verify tracked files at any time:

```bash
git lfs ls-files
```

A `*` next to a file means the content is present locally; `-` means only the pointer is checked out.

### Download

```bash
# Download all tracked files
git lfs pull

# Download by pattern
git lfs pull -I "*.bam"

# Download a specific directory
git lfs pull -I "data/**"
```

---

## data-client (direct transfer)

Use the `data-client` when you need to upload or download files outside of a Git workflow, or in batch/scripted scenarios.

### Configure a profile

If you haven't set up a profile yet:

```bash
./data-client configure --profile=mycommons
```

You'll be prompted for your Gen3 API endpoint and credentials path.

### Upload

Upload a single file:

```bash
./data-client upload --profile=mycommons --upload-path=data/sample.bam
```

Upload a directory in parallel:

```bash
./data-client upload --profile=mycommons --upload-path=data/ --batch --numparallel=5
```

Each uploaded file receives a **GUID** (Globally Unique Identifier) from Gen3. Save these GUIDs — they are required to download the files later.

### Download

```bash
./data-client download --profile=mycommons --guid=dg.1234/5678-abcd
```

To download to a specific directory:

```bash
./data-client download --profile=mycommons --guid=dg.1234/5678-abcd --dir=./downloads
```

---

## Next Steps

- [Manage Collaborators](collaborators.md) — share your project with team members
- [Git DRS Complete Guide](../../tools/git-drs/quickstart.md) — advanced workflows, multiple remotes, cross-remote promotion
- [data-client Authentication](../../tools/data-client/authentication.md) — profile setup and access verification
