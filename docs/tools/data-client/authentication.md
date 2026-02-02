---
title: Authentication & Access
---

# Authentication & Access (Fence)

The `data-client` uses the **Fence** service to manage authentication and user access privileges.

## Authentication Setup

Authentication is handled via the `configure` command using an API Key credential file. See [Configuration](index.md#configuration) for details.

When you run a command, the `data-client`:
1.  Validates your API Key.
2.  Requests a temporary Access Token from Fence.
3.  Uses this Access Token for subsequent API calls.

If your Access Token has expired, the client automatically refreshes it using your API Key.

## Checking Privileges

You can verify your current access privileges and see which projects/resources you have access to using the `auth` command.

### Command

```bash
./data-client auth --profile=<profile-name>
```

### Example Usage

```bash
./data-client auth --profile=mycommons
```

### Output

The command lists the resources (projects) you can access and the specific permissions you have for each (e.g., read, write, delete).

```text
You have access to the following resource(s) at https://data.mycommons.org:

/programs/program1/projects/projectA [read, read-storage, write-storage]
/programs/program1/projects/projectB [read]
```
