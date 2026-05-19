---
title: Git-DRS
lead: "Git-DRS is the Git-facing data workflow for Syfon-backed repositories."
personas:
  - data-steward
  - platform-engineer
  - security-compliance-reviewer
solutions:
  - manage-data
related_tools:
  - git-drs
  - syfon
---

# Git-DRS

Git-DRS is the Git-facing data workflow for Syfon-backed repositories. It keeps large research files out of normal Git history while still letting a repository push, pull, and delete those files in a scoped, DRS-aware way.

What Git-DRS does:

- stores pointer files in Git instead of large binary contents
- connects a repository to a scoped Syfon / Gen3 remote
- uploads, registers, and hydrates tracked objects
- reconciles tracked-file deletes correctly for the current scope

## Start Here

Use the page that matches your goal:

- [Quick Start](quickstart/) for the shortest path to a working machine and repository
- [Getting Started](getting-started/) for the workflow model after first setup
- [Installation Guide](installation/) if you only need install or source-build details
- [Commands Reference](commands/) if you already know the workflow and need exact syntax
- [Troubleshooting](troubleshooting/) if a real workflow is failing

## Suggested Path

For a new user:

1. [Quick Start](quickstart/)
2. [Getting Started](getting-started/)
3. [Commands Reference](commands/) only when you need exact flags or edge-case behavior

## Reference

Deeper detail lives under the reference section:

- [Bucket Mapping](docs/bucket-mapping/)
- [Removing Files](docs/remove-files/)
- [How It Works](docs/)
- [Developer Guide](docs/developer-guide/)
