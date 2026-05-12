---
title: Authentication & Access
---

# Authentication & Access

`data-client` uses named profiles. A profile stores the commons endpoint and the credentials needed to mint access tokens for later commands.

## Configure a Profile

```bash
./data-client configure \
  --profile=mycommons \
  --cred=credentials.json \
  --apiendpoint=https://data.mycommons.org
```

Required flags:

- `--profile`: local profile name to create or update
- `--cred`: path to the Gen3 credentials JSON
- `--apiendpoint`: base URL for the commons API

Useful optional flags:

- `--fenceToken`: use a token value instead of a credentials file
- `--use-shepherd`: enable Shepherd support when the commons provides it
- `--min-shepherd-version`: minimum Shepherd version to accept

Profiles are written to `~/.gen3/gen3_client_config.ini`.

## Check Access

Use `auth` to confirm that the profile works and to see what resources it can access.

```bash
./data-client auth --profile=mycommons
```

Useful variants:

```bash
./data-client auth --profile=mycommons --all
./data-client auth --profile=mycommons --json
```

What the flags do:

- `--all`: show every resource in each permission group instead of a shortened summary
- `--json`: emit raw access JSON instead of formatted text

## What To Expect

On success, `auth` reports the resource paths and the permission groups attached to them. Typical output includes project paths such as `/programs/program1/projects/projectA` along with permissions like read or write access.

```text
You have access to the following resource(s) at https://data.mycommons.org:

/programs/program1/projects/projectA [read, read-storage, write-storage]
/programs/program1/projects/projectB [read]
```

If a profile is missing or invalid, fix it by re-running `configure` with the right `--profile`, `--cred`, and `--apiendpoint` values.
