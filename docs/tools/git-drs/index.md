---
title: Git-DRS
---

# Git-DRS

Git-DRS is a Git extension for managing large files in a Gen3 Data Commons using the **Data Repository Service (DRS)** content-addressable storage model. It essentially serves as a Git-LFS (Large File Storage) replacement tailored for Gen3.

It allows you to:
- Track large files in your git repository without bloating it.
- Store the actual file contents in a Gen3 data commons (indexed via DRS).
- Seamlessly synchronize files between your local environment and the commons.

## Installation

Ensure `git-drs` is installed and in your PATH.

## Initialization

Initialize a repository to use Git-DRS. This sets up the necessary hooks and configuration.

```bash
git-drs init
```

## Basic Workflow

1.  **Add a file**: Track a large file with Git-DRS.
    ```bash
    git-drs add <filename>
    ```
    This replaces the large file with a small pointer file in your working directory.

2.  **Push**: Upload the tracked files to the Gen3 Commons.
    ```bash
    git-drs push
    ```

3.  **Fetch**: Download file contents (resolving pointer files) from the Commons.
    ```bash
    git-drs fetch
    ```

## Command Reference

### `init`
Initializes `git-drs` in the current git repository. Recommended to run at the root of the repo.

### `add <file>`
Tracks a file using Git-DRS. The file content is moved to a local cache, and replaced with a pointer file containing its hash and size.

### `push`
Uploads the contents of tracked files to the configured Gen3 Commons. This usually happens automatically during `git push` if hooks are configured, but can be run manually.

### `fetch`
Downloads the contents of tracked files from the Gen3 Commons, replacing the local pointer files with the actual data.

### `list`
Lists the files currently tracked by Git-DRS in the project.

### `remote`
Manage remote DRS server configurations.

```bash
git-drs remote add <name> <url>
git-drs remote list
git-drs remote set <name>
git-drs remote remove <name>
```
