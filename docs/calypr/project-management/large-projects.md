
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

## What Works: Query the Project Index

Each Calypr project maintains a metadata index file—typically `META/lfs_index.tsv`—that tracks all LFS-managed files with their key attributes:

```text
path                oid_sha256   size    tags    logical_id
data/a.bam          1a2b3c...    12345   tumor   sample:XYZ
data/b.bam          4d5e6f...    67890   normal  sample:ABC
```

**Use this index instead of `git lfs ls-files`.** Querying `META/lfs_index.tsv` is nearly instant regardless of repository size:

```bash
# Find all VCF files in the index
awk -F'\t' '$1 ~ /\.vcf\.gz$/ {print $0}' META/lfs_index.tsv

# Find files tagged as tumor samples
awk -F'\t' '$4 == "tumor" {print $1}' META/lfs_index.tsv
```

Or in Python:

```python
import csv

with open("META/lfs_index.tsv") as f:
    for row in csv.DictReader(f, delimiter="\t"):
        if row["path"].endswith(".vcf.gz"):
            print(row["path"], row["logical_id"])
```

The index is version-controlled alongside the repository and updated automatically when new files are added.

---

## What Works: Sparse Checkout

If you only need a subset of the repository—for example, files from a single study or cohort—use Git's sparse checkout to avoid downloading the entire working tree:

```bash
# Enable sparse checkout
git sparse-checkout init --cone

# Specify only the paths you need
git sparse-checkout set data/StudyX data/StudyY META
```

This is particularly useful when working with a mirror of a large project (such as a GDC mirror) where downloading all files upfront is impractical. You can always add more paths later:

```bash
git sparse-checkout add data/StudyZ
```

To disable sparse checkout and restore the full working tree:

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

Then cross-reference with the index to get the full metadata for only those files. This avoids scanning the entire repository on every run.

---

## What Doesn't Work at Scale

| Pattern | Why it's slow | What to do instead |
|---|---|---|
| `git lfs ls-files --json` on the full repo | Scans every LFS pointer | Query `META/lfs_index.tsv` |
| Running LFS validation on every CI push | Reads the full LFS object list each time | Diff between commits; run full checks on a schedule |
| Downloading all LFS objects at clone time | Pulls every large file regardless of need | Use sparse checkout + `git lfs pull` for specific paths |

---

## Rebuilding the Index

If the project index is missing or you suspect it is out of sync, you can rebuild it explicitly. This is a **heavy operation** and should be run intentionally, not as part of routine workflows:

```bash
# Generate a fresh index from Git LFS metadata
git lfs ls-files --all --json > /tmp/lfs_files.json
# Transform into META/lfs_index.tsv (see project tooling for the rebuild script)
make rebuild-lfs-index
```

On a large repository this may take several minutes. Once complete, commit the updated index.

---

## CI/CD Recommendations

- **Lint/validate**: Operate on `META/*.tsv` and spot-check a small sample of LFS pointers.
- **Publish/sync steps**: Use `git diff` between the last deployed commit and the current one to identify only changed LFS files.
- **Full integrity checks**: Schedule as a periodic job (nightly or weekly) rather than running on every push.

