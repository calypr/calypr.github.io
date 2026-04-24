---
title: Git-DRS
---

# Git-DRS

Git-DRS is a Git extension for managing large files using the **Data Repository Service (DRS)** content-addressable storage model.
It serves as a Git LFS (Large File Storage) replacement tailored for the GA4GH Data Repository Service specification.

It allows you to:

- Track large files in your Git repository without bloating it.
- Store the actual file contents in a Gen3 data commons (indexed via DRS).
- Seamlessly synchronize files between your local environment and the commons.

## Installation

Ensure `git-drs` is installed and available in your `PATH`.

## Initialization

Initialize a repository to use Git-DRS. This command sets up the necessary hooks and configuration.

```bash
git drs init
```

## Basic Workflow

1.  **Add a file**: Track a large file with Git-DRS.
    ```bash
    git drs add <filename>
    ```
    This replaces the large file with a small pointer file in your working tree.

2.  **Push**: Upload the tracked files to the DRS server.
    ```bash
    git drs push
    ```

3.  **Fetch**: Download file contents (resolving pointer files) from the DRS server.
    ```bash
    git drs fetch
    ```

## Command Reference

### `init`
Initialize `git-drs` in the current Git repository. Run this at the repository root.

### `add <file>`
Track a file using Git-DRS. The file contents are moved to a local cache and replaced with a pointer file containing its hash and size.

### `push`
Upload tracked file contents to the configured DRS server. This usually happens automatically during `git push` if hooks are configured, but you can run it manually.

### `fetch`
Download tracked file contents from the DRS server, replacing local pointer files with the actual data.

### `list`
List files currently tracked by Git-DRS in the project.

### `remote`
Manage remote DRS server configurations:

```bash
git drs remote add <name> <url>
git drs remote list
git drs remote set <name>
git drs remote remove <name>
```
