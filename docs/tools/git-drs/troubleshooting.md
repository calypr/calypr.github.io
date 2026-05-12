# Troubleshooting

Common issues and solutions for the cleaned `git-drs` CLI.

> **Navigation:** [Getting Started](getting-started.md) -> [Commands Reference](commands.md) -> **Troubleshooting**

## Frequently Asked Questions

### How does repo-local setup happen now?

In the normal workflow, `git drs remote add ...` bootstraps the repo-local `git-drs` wiring if it is missing.

That means you generally should not need a separate setup command before everyday use. If a clone is missing hooks or repo-local config, the first `git drs remote add ...` is the right repair path.

## When to Use Which Tool

### Use `git-drs` for

- remote configuration
- tracking rules
- object hydration
- DRS/Syfon metadata-oriented workflows

Examples:

- `git drs remote add gen3 ...`
- `git drs remote remove ...`
- `git drs track`
- `git drs ls-files`
- `git drs pull`
- `git drs add-url`
- `git drs copy-records`

### Use normal Git for

- branch and commit movement
- staging and committing
- ordinary ref push/pull operations

Examples:

- `git add`
- `git commit`
- `git push`
- `git pull`

## First Principles

Before debugging behavior, keep the command split straight:

- `git pull`
  - updates commits, branches, and checkout state
- `git drs pull`
  - hydrates tracked pointer files already present in the current checkout
- `git drs ls-files`
  - shows tracked files and localization state

If you blur those together, the failure modes get confusing.

## Common Error Patterns

### Failed commit or pointer conversion issues

Check these in order:

1. confirm the file pattern was tracked before the add/commit flow

   ```bash
   git drs track
   ```

2. confirm `.gitattributes` was staged after changing tracking rules

   ```bash
   git status
   ```

3. confirm the file shows up in the tracked inventory

   ```bash
   git drs ls-files
   ```

4. inspect `.git/drs/` logs if the hook path failed

### Failed push: upload, register, or auth

Check:

```bash
git drs remote list
git drs ls-files --drs
```

Then retry with higher Git/HTTP verbosity if needed:

```bash
GIT_TRACE=1 GIT_CURL_VERBOSE=1 git push
```

### Failed clone or fresh checkout still has pointer files

That usually just means hydration has not happened yet.

Run:

```bash
git drs remote list
git drs pull
```

If the repo has never had a `git-drs` remote configured, run `git drs remote add ...` first. That command will also install the repo-local hooks/config.

### Network timeout during push or download

If you use SSH remotes, keepalives help:

```
Host github.com
    TCPKeepAlive yes
    ServerAliveInterval 30
```

## Common Problems

### `git drs pull` did not update my branch

That is expected.

`git drs pull` no longer runs `git pull`.

Use:

```bash
git pull
git drs pull
```

### `git drs ls-files` does not show my file

Check these in order:

1. is the path actually tracked?

```bash
git drs track
```

2. did you stage `.gitattributes` after adding the pattern?

```bash
git add .gitattributes
```

3. is the file part of the current checkout?

```bash
git ls-files -- path/to/file
```

4. inspect the local view:

```bash
git drs ls-files -l
```

### `git remote remove` did not remove my `git-drs` remote

That is expected.

Git remotes and `git-drs` remotes live in different config domains.

Use:

```bash
git drs remote list
git drs remote remove <name>
```

or:

```bash
git drs remote rm <name>
```

### `git drs pull` does nothing

That usually means one of these:

- the current checkout already has localized bytes
- there are no tracked pointer files matching your include filters
- the file is not tracked by `git-drs`

Check:

```bash
git drs ls-files
git drs ls-files -I "*.bam"
git drs pull --dry-run -I "*.bam"
```

### `git drs pull` still leaves pointer files

Check DRS registration status:

```bash
git drs ls-files --drs
```

If the object is not registered or not resolvable from the configured remote, hydration cannot succeed.

Also confirm the remote configuration:

```bash
git drs remote list
```

If needed, inspect the detailed logs:

```bash
ls -la .git/drs/
```

### `git drs remote add gen3` fails on bucket mapping

Current shape:

```bash
git drs remote add gen3 [remote-name] <organization/project> [--cred <file> | --token <token>]
```

If this fails, the likely cause is missing bucket mapping for that scope.

That mapping is usually steward/admin setup, not something the end user invents ad hoc.

### My credentials expired

Refresh by re-adding the remote with a new credential file or token:

```bash
git drs remote add gen3 production HTAN_INT/BForePC --cred /path/to/new-credentials.json
```

What `git-drs` does automatically:

- if the stored access token is expired but the stored API key is still valid, `git-drs` will attempt to refresh the access token
- if the API key itself is expired, revoked, or replaced, you need to re-run `git drs remote add gen3 ...`

How to think about recovery:

- token expired, key still valid:
  - often automatic
- key expired or replaced:
  - rerun `git drs remote add gen3 ... --cred ...` or `--token ...`

How to check what is in use:

```bash
git drs remote list
```

And for the underlying Gen3 profile data:

- inspect `~/.gen3/gen3_client_config.ini`

If you want the least surprising fix, just re-run `git drs remote add gen3 ...` with the current credential file. That updates the stored profile and repo token plumbing in one step.

### `git push` fails with upload or register errors

Check:

```bash
git drs remote list
git drs ls-files --drs
```

Typical root causes:

- expired credentials
- wrong remote selected
- missing server-side bucket mapping
- object registration or upload permissions missing for the target scope

### Files are not being tracked

Symptoms:

- large files were committed directly to Git
- `git drs ls-files` does not show the file

Recovery:

```bash
git drs track "*.bam"
git add .gitattributes
git rm --cached large-file.bam
git add large-file.bam
git commit -m "Track large file with git-drs"
```

### Cloned repo only has pointer files

That is normal.

After cloning:

```bash
git drs pull
```

Or hydrate only what you need:

```bash
git drs pull -I "*.bam"
```

## Debugging Workflow

When behavior is unclear, use this sequence:

```bash
git drs remote list
git drs track
git drs ls-files -l
git drs ls-files --drs
git drs pull --dry-run
```

That usually tells you whether the problem is:

- tracking
- hydration state
- DRS registration
- remote configuration

## Log and State Inspection

Useful checks:

```bash
git drs remote list
git drs track
git drs ls-files -l
git drs ls-files --drs
ls -la .git/drs/
```

## Removed Commands

If you see old notes mentioning these, ignore them:

- `git drs fetch`
- `git drs list`
- `git drs upload`
- `git drs download`

Those were removed from the cleaned CLI surface.
