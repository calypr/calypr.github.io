---
title: Removing Files
---

## Removing Files

There are two different questions when you remove a file from a `git-drs` repository:

1. Do you just want to remove the path from Git?
2. Do you also want the pushed deletion to reconcile remote DRS state for that object?

For tracked `git-drs` files, the recommended command is `git drs rm`.

## Which Command To Use

### Use `git drs rm` for tracked `git-drs` or Git LFS files

```bash
git drs rm DATA/subject-123/vcf/sample1.vcf.gz
```

Use this when you want the supported Git-DRS delete workflow.

What it does immediately:

- validates that the path is a tracked `git-drs` / Git LFS file
- removes the path from the worktree and index
- stages the deletion through normal Git

What happens later, when the deletion is committed and pushed:

- `git-drs` derives deleted pointers from the pushed Git commit delta
- if the object is still live somewhere else in the pushed repo state, only the local path deletion is reconciled
- if the scoped record has exactly one `controlled_access` resource, the remote record is deleted
- if that record is the last scoped owner, storage can be purged along with the record
- if the record has multiple `controlled_access` resources, only the current `organization/project` resource is removed and the shared record/object is preserved

This is the safer option because it refuses to operate on paths that are not actually tracked by `git-drs`.

### Use `git rm` for ordinary Git-managed files

```bash
git rm README.md
```

Use this for files that are not tracked by `git-drs` or Git LFS.

### Important nuance about `git rm` on tracked pointers

If you use plain `git rm` on a tracked pointer file, the later `git drs push` delete reconciliation can still observe that committed pointer deletion and mutate remote DRS state.

So the difference is not that `git rm` is "local only." The difference is that `git drs rm` is the explicit, validated workflow for tracked data objects.

## Typical Tracked-File Removal Flow

### 1. Remove the tracked file

Use `git drs rm`:

```bash
git drs rm DATA/subject-123/vcf/sample1.vcf.gz
```

### 2. Review Changes

After removing files, check the status of your project to see the staged changes:

```bash
git status
```

This shows the staged pointer deletion and any other affected files.

### 3. Update Metadata

If the removed file is referenced from repository metadata, update that metadata explicitly. If you regenerate metadata from repository state, `forge meta init` is one option:

```bash
forge meta init
```

!!! note
    Regeneration can rebuild `META/` from current repository state.
    If you maintain customized metadata, you may need to remove or edit the affected `DocumentReference` entries manually instead of blindly regenerating everything.

### 4. Commit Changes

Once you've reviewed the changes, commit them to your local repository:

```bash
git commit -m "Removed sample1.vcf.gz and updated associated metadata"
```

---

## 🚀 Pushing Updates to the Platform

After committing the deletion, push it.

### 1. Push the committed delete

Use the normal Git workflow:

```bash
git push
```

Or run the DRS stage directly:

```bash
git drs push
```

That is when remote delete reconciliation happens.

## Removal Levels

From least opinionated to most opinionated:

- `rm` or filesystem delete: removes a local file only; Git and DRS do not know what you intended
- `git rm`: stages deletion in Git, but does not validate that the target is a tracked `git-drs` object
- `git drs rm`: stages deletion in Git and asserts that you are deleting a tracked `git-drs` / LFS object
- `git drs rm` + commit + `git drs push`: applies the full scoped remote cleanup workflow

## Best Practice

For data objects managed by `git-drs`, prefer:

```bash
git drs rm <path>
git commit -m "Remove tracked object"
git drs push
```

Use plain `git rm` for non-DRS project files.

---

## 📌 Best Practices

- Prefer `git drs rm` for tracked data objects.
- Update or regenerate metadata after file removal when those files are referenced in `META/`.
- Review the resulting commit before push so you know exactly which pointers are being removed.
- Verify remote state after push if the deletion was intended to remove project ownership or purge the final record.

---

By following this flow, you keep Git state, metadata, and remote DRS ownership semantics aligned. 
