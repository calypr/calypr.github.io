---
title: Access & Collaboration
---

# Access & Collaboration

The current collaborator command is `collaborators`, not `collaborator`.

Use it to list requests, add users to projects, remove users, and approve pending requests.

## Managing Collaborators

### Add a User to One Project

```bash
./data-client collaborators add mycommons user@example.org program project
```

Useful flags:

- `--write` or `-w`: request write access as well as read access
- `--guppy` or `-g`: include Guppy-related permissions
- `--approve` or `-a`: immediately approve the generated requests if your account is allowed to do that

### Add a User to Multiple Projects

```bash
./data-client collaborators bulk-add \
  mycommons \
  user@example.org \
  /programs/program1/projects/projectA \
  /programs/program1/projects/projectB
```

`bulk-add` also accepts `organization/project` resource forms and turns them into the project requests internally.

### Remove a User

```bash
./data-client collaborators rm mycommons user@example.org program project
```

`--approve` works here too when you want to create and sign the revoke requests in one step.

## Managing Requests

### List Requests

```bash
./data-client collaborators ls mycommons
```

Useful flags:

| Flag | Meaning |
| --- | --- |
| `--mine` | Show requests associated with the current user |
| `--active` | Show only active requests |
| `--username` | Filter for a specific user |

### List Pending Requests

```bash
./data-client collaborators pending mycommons
```

### Approve a Request

```bash
./data-client collaborators approve mycommons <request-id>
```

Project administrators can use this to sign a pending request after reviewing it.
