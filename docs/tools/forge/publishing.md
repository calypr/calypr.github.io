---
title: Publishing
---

# Publishing

The `forge` tool handles the lifecycle of publishing metadata to Gen3 Commons via the **Sower** service (for async job processing).

## Publishing Metadata

To start a new metadata publication job:

```bash
forge publish <github_personal_access_token> [flags]
```

This command submits a job to the Sower service.

**Arguments:**
- `<github_personal_access_token>`: A GitHub Personal Access Token (PAT) is required by the backend worker to access the repository containing the metadata schema.

**Flags:**
- `--remote`, `-r`: Target remote DRS server name (default: "default_remote").

**Output:**
Returns the Job UID, Name, and initial Status.

```text
Uid: 12345-abcde 	 Name: metadata-publish 	 Status: PENDING
```

## Monitoring Jobs

### List Jobs

View all jobs cataloged in Sower.

```bash
forge publish list [flags]
```

**Flags:**
- `--remote`, `-r`: Target remote DRS server.

### Check Status

Check the status of a specific job by its UID.

```bash
forge publish status <UID> [flags]
```

**Flags:**
- `--remote`, `-r`: Target remote DRS server.

### View Logs

Retrieve the output logs of a specific job.

```bash
forge publish output <UID> [flags]
```

**Flags:**
- `--remote`, `-r`: Target remote DRS server.

**Output:**
Displays the raw logs from the backend job execution, which is useful for debugging failures.
