# Commands Reference

This page documents the commands that exist in the current `git-drs` CLI.

> **Navigation:** [Getting Started](getting-started.md) -> **Commands Reference** -> [Troubleshooting](troubleshooting.md)

## Version and Setup

### `git drs version`

Print the installed version.

```bash
git drs version
```

### `git drs install`

Install global Git filter configuration.

```bash
git drs install
```

Use this when you explicitly want the global filter wiring. Normal repository onboarding is usually driven by `git drs remote add`, which bootstraps repo-local setup when needed.

### `git drs init`

Initialize or repair repository-local `git-drs` state.

```bash
git drs init
```

Use this mainly for explicit repair or manual setup. In the normal flow, `git drs remote add` usually makes this unnecessary.

### `git drs ping [remote-name]`

Inspect the currently configured remote state.

```bash
git drs ping
git drs ping production
```

Useful for checking resolved remote settings such as scope, bucket, and storage prefix.

## Remote Configuration

### `git drs remote add gen3 [remote-name] <organization/project>`

Add or refresh a Gen3-backed remote.

```bash
git drs remote add gen3 production HTAN_INT/BForePC --cred ~/.gen3/credentials.json
```

Key behavior:

- `organization/project` is one positional scope argument
- `--cred` or `--token` provides credentials
- repo-local hooks/config are bootstrapped automatically if missing
- bucket resolution is scope-driven and server-backed

### `git drs remote add local <remote-name> <url> <organization/project>`

Add a local Syfon/DRS remote.

```bash
git drs remote add local origin http://localhost:8080 calypr/end_to_end_test \
  --username drs-user \
  --password drs-pass
```

### `git drs remote list`

List configured remotes.

```bash
git drs remote list
```

### `git drs remote set <remote-name>`

Set the default `git-drs` remote.

```bash
git drs remote set production
```

### `git drs remote remove <remote-name>`

Remove a configured `git-drs` remote.

```bash
git drs remote remove production
git drs remote rm production
```

This affects `git-drs` config, not normal Git remotes.

## Tracking and Local Inventory

### `git drs track [pattern ...]`

Manage tracked file patterns.

```bash
git drs track "*.bam"
git drs track "data/**"
git drs track
```

With no arguments, it lists tracked patterns.

### `git drs untrack <pattern> [pattern ...]`

Remove tracked file patterns.

```bash
git drs untrack "*.bam"
```

### `git drs ls-files [pathspec...]`

List tracked files in the checkout.

```bash
git drs ls-files
git drs ls-files -l
git drs ls-files --drs
git drs ls-files -I "*.bam"
```

Important behavior:

- local-first by default
- `*` means hydrated/localized
- `-` means the worktree still contains a pointer
- `--drs` adds DRS registration checks

## Hydration and Push

### `git drs pull [remote-name]`

Hydrate tracked pointer files in the current checkout.

```bash
git drs pull
git drs pull production
git drs pull -I "*.bam"
```

Important:

- `git drs pull` does not run `git pull`
- it only hydrates tracked pointer files already present in the checkout
- use include filters when you want only a subset:

```bash
git drs pull -I "data/sample.bam"
git drs pull -I "*.vcf.gz"
```

### `git drs push [remote-name]`

Register/upload tracked objects and reconcile committed deletes.

```bash
git drs push
git drs push production
```

What it does:

- resolves local pointer/object metadata
- uploads local bytes when needed
- registers object metadata with the target Syfon instance
- reconciles committed deletes derived from the pushed Git ref delta

For tracked data changes, `git drs push` is the normal top-level push command.

## Removing Tracked Files

### `git drs rm <path>...`

Remove tracked `git-drs` / LFS files from the worktree and index.

```bash
git drs rm data/sample.bam
git drs rm data/sample1.bam data/sample2.bam
```

What it does immediately:

- validates that each path is a tracked `git-drs` / LFS file
- runs `git rm` on those paths

Remote cleanup happens later when the deletion is committed and pushed.

For the full removal decision tree, see [Removing Files](docs/remove-files.md).

## Referencing Existing Objects

### `git drs add-url <object-url-or-key> [path]`

Create a pointer and local metadata for an object that already exists in provider storage.

```bash
git drs add-url path/to/object.bin data/from-bucket.bin --scheme s3
git drs add-url s3://my-bucket/path/to/object.bin data/from-bucket.bin
git drs add-url s3://my-bucket/path/to/object.bin data/from-bucket.bin --sha256 <hex>
```

Important behavior:

- object-key mode resolves against the configured bucket scope
- explicit provider URL mode is also supported
- `--scheme` is required for object-key mode
- registration happens later on `git drs push`

### `git drs add-ref <drs_uri> <dst path>`

Create a local pointer file for an existing DRS object.

```bash
git drs add-ref drs://example/object-id data/object.bin
```

## Query and Metadata Copy

### `git drs query <drs_id>`

Query a DRS object by DRS ID.

```bash
git drs query drs://example/object-id
```

The current command also supports checksum-based lookup through its flags.

### `git drs copy-records [source-remote] <target-remote> <organization/project>`

Copy Syfon metadata records between remotes for one scope.

```bash
git drs copy-records dev prod HTAN_INT/BForePC
git drs copy-records prod HTAN_INT/BForePC
```

Behavior:

- copies metadata only, not object bytes
- with one remote arg, the configured default remote is the source
- with two remote args, the first is source and the second is target

## Bucket Management

These commands are usually steward/admin operations.

### `git drs bucket add [remote-name]`

Declare bucket credentials on the target server.

```bash
git drs bucket add production \
  --bucket cbds \
  --region us-east-1 \
  --access-key "$AWS_ACCESS_KEY_ID" \
  --secret-key "$AWS_SECRET_ACCESS_KEY" \
  --s3-endpoint https://s3.amazonaws.com
```

### `git drs bucket add-organization [remote-name]`

Map an organization to a bucket path.

```bash
git drs bucket add-organization production \
  --organization HTAN_INT \
  --path s3://cbds/htan-int
```

### `git drs bucket add-project [remote-name]`

Map a project to a bucket path.

```bash
git drs bucket add-project production \
  --organization HTAN_INT \
  --project BForePC \
  --path s3://cbds/bforepc
```

For the full mapping model, see [Bucket Mapping](docs/bucket-mapping.md).

## Administrative Deletes

### `git drs delete <hash-type> <oid>`

Delete a DRS object by identifier.

```bash
git drs delete sha256 <hex>
```

### `git drs delete-project <project_id>`

Delete project-scoped server state for a project.

```bash
git drs delete-project BForePC
```

## Internal Commands

There are also internal support commands in the binary, such as clean/smudge/filter and hook-preparation commands. Those are not part of the normal end-user workflow and are intentionally not documented here as primary commands.
