
# Working with Large Projects

How to work efficiently with Git LFS repositories that track thousands of files.

## Overview

Large Calypr projects can contain **thousands to hundreds of thousands** of LFS-tracked files—VCFs, BAMs, images, and other genomic assets across many samples. Working with a repository this size requires a different approach than smaller projects.

The most common issue analysts encounter is that standard LFS enumeration becomes very slow:

```bash
git lfs ls-files --json
```

On a large repository, this can take **several minutes** and is not practical for day-to-day work. The sections below describe the patterns that work well at scale.

---

## What Works: Sparse Checkout

If you only need a subset of the repository—for example, files from a single study or cohort—use Git's sparse checkout to avoid downloading the entire working tree. This is especially valuable when working with large project mirrors (such as a GDC mirror) where the full dataset is far larger than what you need for a given analysis.

### Initial setup

```bash
# Clone without checking out any files
git clone --no-checkout https://github.com/your-org/your-project.git
cd your-project

# Enable sparse checkout in cone mode (faster, path-based)
git sparse-checkout init --cone

# Check out only the cohorts or studies you need, plus any metadata
git sparse-checkout set data/TCGA-BRCA data/TCGA-LUAD
```

After this, only LFS pointer files under `data/TCGA-BRCA/` and `data/TCGA-LUAD/` will be present in your working tree. Git LFS objects themselves are downloaded on demand.

### Selectively pulling LFS objects

After sparse checkout, pull only the LFS objects for your checked-out paths:

```bash
# Pull LFS objects for the paths you've checked out
git lfs pull --include "data/TCGA-BRCA/**"
git lfs pull --include "data/TCGA-LUAD/**"
```

This avoids downloading LFS objects for the rest of the repository.

### Adding more paths later

```bash
git sparse-checkout add data/TCGA-KIRC
git lfs pull --include "data/TCGA-KIRC/**"
```

### Scoping LFS commands to your checkout

When working within a sparse checkout, scope LFS introspection to the paths you care about:

```bash
# Fast: only examines files in your scoped paths
git lfs ls-files --include "data/TCGA-BRCA/**" --json

# Slow: scans all pointer files across the full repo history
git lfs ls-files --json
```

Structuring your data directory around project subtrees (`data/studyA/`, `data/studyB/`, etc.) makes all path-scoped operations faster and more predictable.

### Restoring the full working tree

```bash
git sparse-checkout disable
```

---

## What Works: Path-Scoped LFS Commands

When you do need to use Git LFS commands directly, scope them to a specific path or study:

```bash
# Instead of scanning everything:
git lfs ls-files --json

# Scope to a specific study or cohort:
git lfs ls-files --include "data/StudyX/**" --json
```

This keeps operations fast and predictable as the repository grows.

---

## What Works: Incremental Updates

To identify only the files that changed between two commits (useful for ETL pipelines and sync jobs):

```bash
git diff --name-only <old-commit> <new-commit>
```

This avoids scanning the entire repository on every run. Use the resulting list to pull only the LFS objects that changed:

```bash
# Pull LFS objects for each changed path prefix
git diff --name-only <old-commit> <new-commit> | while read -r path; do
    git lfs pull --include "$path"
done
```

---

## Working on Network-Mounted Storage (NFS / HPC)

If your project repository or working tree lives on a network-mounted drive (NFS, GPFS, Lustre, or similar shared storage common in HPC environments), you will experience significantly worse performance than on a local disk. This is because Git and Git LFS make many small metadata reads and writes that are fast on local SSDs but slow over a network filesystem.

### Recommended: Keep `.git` local, use NFS only for data

The best setup is to keep the Git internals on a local disk and use NFS only for your working data:

```bash
# Clone to local scratch storage on your compute node
git clone https://github.com/your-org/your-project.git /local/scratch/my-project
cd /local/scratch/my-project

# Enable sparse checkout—only pull the data you need
git sparse-checkout init --cone
git sparse-checkout set data/TCGA-BRCA

# Pull LFS objects into a local LFS cache
git lfs pull --include "data/TCGA-BRCA/**"
```

If you need results to persist on NFS, copy only the outputs:

```bash
cp -r results/ /nfs/shared/project-results/
```

### If `.git` must live on NFS: redirect LFS storage locally

You can configure Git LFS to store large object files on a local path even when `.git` itself is on NFS. This means binary files are cached locally while pointer blobs remain on NFS:

```bash
# Create the local storage directory first
mkdir -p /local/scratch/lfs-storage

# In .lfsconfig or via git config
git config lfs.storage /local/scratch/lfs-storage
```

Or set it in `.lfsconfig` in the repo root:

```ini
[lfs]
    storage = /local/scratch/lfs-storage
```

Git objects (pointer blobs) may still be on NFS, but large binaries live locally—which is usually where the bulk of the I/O cost is.

### Scope commands aggressively on NFS

On NFS, treat `git lfs ls-files` as a slow indexer and avoid running it over the full repository:

```bash
# Avoid this on NFS—scans every pointer file
git lfs ls-files --json

# Prefer scoped commands
git lfs ls-files --include "data/TCGA-BRCA/**"
git lfs ls-files --include "data/TCGA-BRCA/**" --json
```

### Tune NFS mount options (if you control them)

If you have access to NFS mount options, these settings can reduce latency for Git workloads. Discuss with your storage or infrastructure team:

- **`noatime`** — avoids extra write operations when reading files (Git reads many files)
- **`rsize`/`wsize`** — increase to allow larger I/O chunks (e.g., `rsize=1048576,wsize=1048576`)
- **`actimeo`** — for a mostly read-only `.git` directory, you can often afford more aggressive attribute caching without breaking consistency

### Use a local mirror for automation

For CI jobs or automated pipelines that run on shared NFS storage:

1. Clone the repository to ephemeral local storage at the start of the job.
2. Run all Git and LFS operations locally.
3. Write only the results back to NFS.

```bash
# At the start of a CI/automation job
git clone https://github.com/your-org/your-project.git /tmp/job-workspace
cd /tmp/job-workspace
git sparse-checkout init --cone
git sparse-checkout set data/TCGA-BRCA
git lfs pull --include "data/TCGA-BRCA/**"

# ... do your analysis ...

# Write results back to NFS
cp -r results/ /nfs/shared/outputs/
```

---

## What Doesn't Work at Scale

| Pattern | Why it's slow | What to do instead |
|---|---|---|
| `git lfs ls-files --json` on the full repo | Scans every LFS pointer | Use `--include` to scope by path |
| Running LFS validation on every CI push | Reads the full LFS object list each time | Diff between commits; run full checks on a schedule |
| Downloading all LFS objects at clone time | Pulls every large file regardless of need | Use sparse checkout + `git lfs pull` for specific paths |
| Running Git commands on NFS without scoping | NFS amplifies metadata I/O cost | Clone to local scratch; use sparse checkout; scope all commands |

---

## CI/CD Recommendations

- **Lint/validate**: Spot-check a small sample of LFS pointers scoped to recently changed paths.
- **Publish/sync steps**: Use `git diff` between the last deployed commit and the current one to identify only changed LFS files.
- **Full integrity checks**: Schedule as a periodic job (nightly or weekly) rather than running on every push.
