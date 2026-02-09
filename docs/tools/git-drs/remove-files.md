---
title: Removing Files
---

## 🗑️ Deleting Files and Updating Metadata

When removing data files from your project, it's crucial to also update the manifest and associated metadata to maintain consistency.

### 1. Remove File(s) Using `git rm`

Use the `git rm` command to delete files and automatically update the manifest and metadata:

```bash
git rm DATA/subject-123/vcf/sample1.vcf.gz
```

This command performs the following actions:

- Removes the corresponding `entry` from `MANIFEST/`.

!!! note
    It will not:

    - Delete the specified `data` file.
    - Update or remove related metadata in the `META/` directory.

### 2. Review Changes

After removing files, check the status of your project to see the staged changes:

```bash
git status
```

This will display the files marked for deletion and any updates to the manifest.

### 3. Update Metadata

If you need to regenerate the metadata after file deletions, use the `forge meta init` command:

```bash
forge meta init
```

!!! note
    This command rebuilds the `META/` directory based on the current state of the repository, ensuring that your metadata accurately reflects the existing data files.

    If you have customized the metadata, you will need to manually remove the affected DocumentReference entries before running this command to avoid conflicts or inconsistencies.

### 4. Commit Changes

Once you've reviewed the changes, commit them to your local repository:

```bash
git commit -m "Removed sample1.vcf.gz and updated associated metadata"
```

---

## 🚀 Pushing Updates to the Platform

After committing your changes, push them to the CALYPR platform.

### 1. Push Changes

Use the `git push` command (which triggers the `git-drs` transfer hooks) to upload your changes:

```bash
git push
```

If you need to perform metadata registration specifically, you can use `git drs push`.

---

## 📌 Best Practices

- Always use `git rm` to delete files to ensure that the Git state is properly updated.
- Use `forge meta init` to regenerate metadata when necessary, especially after significant changes to your data files.
- Regularly review your remote repository after pushing changes to confirm successful updates.

---

By following these steps, you can maintain a consistent and accurate state across your data, manifest, and metadata in your CALYPR project. 
