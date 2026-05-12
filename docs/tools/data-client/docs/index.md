---
title: Data Client
---

# Data Client

`data-client` is the Gen3-facing CLI for three common tasks:

- configure a profile for a commons
- upload or download data
- manage collaborator access requests

The current docs below are organized around the commands that exist in the binary today, not the older Gen3 client workflow.

## Typical Flow

1. Configure a profile with credentials and API endpoint.
2. Check what access that profile has.
3. Upload or download data.
4. Manage collaborator requests when project access needs to change.

## Command Areas

- [Authentication](authentication.md): profile setup and access checks
- [Data Management](data_management.md): upload, multipart upload, retry, and download commands
- [Access Requests](access_requests.md): collaborator request workflows

## First-Time Setup

Profiles are stored in `~/.gen3/gen3_client_config.ini`.

```bash
./data-client configure \
  --profile=mycommons \
  --cred=credentials.json \
  --apiendpoint=https://data.mycommons.org
```

After that, most commands just need `--profile=mycommons`.
