---
title: Create a Project
---

# Create a Project

!!! info "Admin-assisted setup"
    Project creation is currently handled by the CALYPR team. Submit a request and they will provision your project and send you the details you need to get started.

## Step 1 — Request a Project

Email `support@calypr.org` with:

- Your CALYPR account email
- A short project name and description
- The institution or program it belongs to

The team will respond with:

| Detail | Example |
|---|---|
| GitHub repository URL | `https://github.com/calypr/my-project` |
| Project ID | `SEQ-MyProject` |
| DRS server URL | `https://calypr-public.ohsu.edu` |
| S3 bucket name | `calypr-my-project` |

---

## Step 2 — Install Git DRS

If you haven't already, install Git LFS and Git DRS.

**Initialize Git LFS** (once per machine):

```bash
git lfs install --skip-smudge
```

**Install Git DRS:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/calypr/git-drs/refs/heads/main/install.sh)"
```

Add Git DRS to your PATH:

```bash
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bash_profile
source ~/.bash_profile
```

---

## Step 3 — Clone and Initialize

Clone the repository provided by the CALYPR team:

```bash
git clone https://github.com/calypr/my-project.git
cd my-project
git drs init
```

`git drs init` configures the Git hooks needed for DRS-backed file uploads.

---

## Step 4 — Configure the DRS Remote

Use the project details from Step 1:

```bash
git drs remote add gen3 production \
    --cred ~/.gen3/credentials.json \
    --url https://calypr-public.ohsu.edu \
    --project SEQ-MyProject \
    --bucket calypr-my-project
```

Verify the remote was added:

```bash
git drs remote list
```

```
* production  gen3    https://calypr-public.ohsu.edu
```

The `*` marks your default remote.

---

## Next Steps

- [Upload & Download Files](upload-download.md) — add your first data files
- [Manage Collaborators](collaborators.md) — invite team members
