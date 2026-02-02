---
title: Access & Collaboration
---

# Access & Collaboration

The `data-client` includes tools to manage user access and collaboration through the **Requestor** service. This allows project administrators to invite users (collaborators) to projects and manage access requests.

## Managing Collaborators

The `collaborator` command suite is used to add or remove users from projects.

### Add a User

To give a user access to a project:

```bash
./data-client collaborator add [project_id] [username] --profile=<profile-name>
```

- **project_id**: Format `program-project` (e.g., `SEQ-Res`).
- **username**: The user's email address.

**Options:**
- `--write` (`-w`): Grant write access.
- `--approve` (`-a`): Automatically approve the request (if you have admin permissions).

### Remove a User

To revoke access:

```bash
./data-client collaborator rm [project_id] [username] --profile=<profile-name>
```

**Options:**
- `--approve` (`-a`): Automatically approve the revocation.

## Managing Requests

### List Requests

List access requests associated with you or a user.

```bash
./data-client collaborator ls --profile=<profile-name>
```

**Options:**
- `--mine`: List your requests.
- `--active`: List only active requests.
- `--username`: List requests for a specific user (admin only).

### List Pending Requests

See requests waiting for approval.

```bash
./data-client collaborator pending --profile=<profile-name>
```

### Approve a Request

If you are a project administrator, you can approve pending requests.

```bash
./data-client collaborator approve [request_id] --profile=<profile-name>
```
