---
title: Git Large Data Repository System (Git DRS)
description: Overview of Git DRS architecture and its role in extending Git LFS for scalable data
---

# Why Git DRS?

Git DRS exists to **extend Git LFS with a scalable, standards-based data access layer**
without changing the Git user experience.

At a high level, every data flow follows the same model:

> **Git → Git LFS → Git DRS → Object Store**

```text
+-----+      +---------+      +---------+      +------------+
| Git | ---> | Git LFS | ---> | Git DRS | ---> | Object     |
|     |      |         |      |         |      | Store      |
+-----+      +---------+      +---------+      +------------+
  ^             |               |                  |
  |             | pointers       | auth + resolve   | blobs
  |             v               v                  v
 commits     transfer queue   signed URLs / DRS   S3/GCS/Azure/on-prem
```

```mermaid
flowchart LR
  A[Git\n(commits + pointers)] --> B[Git LFS\n(clean/smudge + transfers)]
  B --> C[Git DRS\n(resolve + authorize)]
  C --> D[Object Store\n(S3/GCS/Azure/on‑prem)]
```

This separation of concerns is intentional.

---

## The Problem Git DRS Solves

Git LFS solves *how* large files integrate with Git, but it intentionally does **not** define:

- How objects are globally identified beyond a repository
- How access is authorized across organizations and environments
- How storage backends are abstracted (S3, GCS, Azure, on‑prem)
- How metadata, lineage, and reuse are tracked at scale

Git DRS fills these gaps while remaining fully compatible with Git LFS.

---

## Architecture Overview

### 1. Git (Source Control)
- Tracks commits, branches, and history
- Stores **Git LFS pointer files** in the repository
- Remains unaware of large object storage details

### 2. Git LFS (User Experience Layer)
- Replaces large files with SHA‑256 pointer files
- Manages clean/smudge filters
- Schedules uploads and downloads
- Invokes a **custom transfer adapter**

Git LFS defines *when* data moves — not *where* or *how it is authorized*.

### 3. Git DRS (Resolution & Authorization)
- Implements a **Git LFS custom transfer adapter**
- Resolves SHA‑256 OIDs to **DRS objects**
- Enforces authorization and access policy
- Issues signed URLs or delegated credentials
- Records metadata and lineage when required

Git DRS is where platform policy lives.

### 4. Object Store (Persistence)
- Stores immutable, content‑addressed blobs
- Typically S3, GCS, Azure Blob, or on‑prem equivalents
- Optimized for durability and throughput, not Git semantics

---

## Why This Matters

This layered design enables:

- **Content‑addressed deduplication** across repos and projects
- **Cross‑environment portability** (dev → staging → prod)
- **Standards alignment** with GA4GH DRS
- **Clear security boundaries** between Git users and storage credentials
- **Future extensibility** without breaking Git workflows

Most importantly, it preserves the developer experience:

> From the user’s perspective, it’s still just `git add`, `git commit`, and `git push`.

---

## Summary

Git DRS is not a replacement for Git or Git LFS.

It is the missing architectural layer that allows Git LFS to operate safely,
portably, and at scale in regulated and multi‑tenant environments.

**Git → Git LFS → Git DRS → Object Store** is the contract.
