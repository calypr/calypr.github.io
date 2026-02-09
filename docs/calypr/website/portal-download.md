---
title: Download
---

There are two main ways to download files:

1. Individually through the browser or through the command line with the `gen3-client`
2. Batch downloads through the command line with `git-drs` and `git-lfs`

This guide will walk you through both methods below.

---

### Batch Download with Git-DRS

To retrieve the actual data files described by a repository, you must clone the repository and use `git lfs pull`.

```bash
# 1. Clone the repository
git clone <GITHUB_REPO_URL>
cd <repository-name>

# 2. Initialize Git-DRS
git drs init

# 3. Add the DRS remote (see Quick Start for details)
git drs remote add gen3 calypr --project <project-id> --bucket <bucket-name> --cred ~/.gen3/credentials.json

# 4. Pull the files
git lfs pull
```