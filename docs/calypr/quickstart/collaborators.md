---
title: Manage Collaborators
---

# Manage Collaborators

Project access in CALYPR uses a request-and-approve model. A project administrator adds a user, and a steward (someone with the `requestor` role at the institution level) approves the request before access is granted.

All collaborator management is done with the `data-client` tool.

---

## Add a Collaborator

```bash
./data-client collaborator add [project_id] [email] --profile=<profile-name>
```

Grant **read** access (default):

```bash
./data-client collaborator add SEQ-MyProject user@example.com --profile=mycommons
```

Grant **write** access:

```bash
./data-client collaborator add SEQ-MyProject user@example.com --profile=mycommons --write
```

If you have admin permissions, auto-approve the request in one step:

```bash
./data-client collaborator add SEQ-MyProject user@example.com --profile=mycommons --write --approve
```

---

## Remove a Collaborator

```bash
./data-client collaborator rm SEQ-MyProject user@example.com --profile=mycommons
```

Auto-approve the revocation (requires admin):

```bash
./data-client collaborator rm SEQ-MyProject user@example.com --profile=mycommons --approve
```

---

## View Pending Requests

See all requests waiting for approval:

```bash
./data-client collaborator pending --profile=mycommons
```

---

## Approve a Request

If you are a project administrator or steward, approve a pending request by its ID:

```bash
./data-client collaborator approve [request_id] --profile=mycommons
```

---

## List Active Collaborators

List access requests for your project:

```bash
# All active requests
./data-client collaborator ls --profile=mycommons --active

# Your own requests
./data-client collaborator ls --profile=mycommons --mine

# Requests for a specific user (admin only)
./data-client collaborator ls --profile=mycommons --username=user@example.com
```

---

## Roles Summary

| Role | Can add collaborators | Can approve requests |
|---|---|---|
| Project member | No | No |
| Project administrator | Yes | Yes (own project) |
| Institution steward | No | Yes (own institution) |

---

## Next Steps

- [Upload & Download Files](upload-download.md) — share data with your new collaborators
- [data-client Access & Collaboration](../../tools/data-client/access_requests.md) — full command reference
