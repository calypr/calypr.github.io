---
title: Removing Files
---

## 🗑️ Deleting Files and Updating Metadata

When removing data files from your project, it's crucial to also update the manifest and associated metadata to maintain consistency.

### 1. Remove File(s) Using `git-drs rm`

Use the `git-drs rm` command to delete files and automatically update the manifest and metadata:

```bash
git-drs rm DATA/subject-123/vcf/sample1.vcf.gz
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
git-drs status
```

This will display the files marked for deletion and any updates to the manifest and metadata.

### 3. Update Metadata

If you need to regenerate the metadata after file deletions, use the `git-drs meta init` command:

```
git-drs meta init
```

!!! note
    This command rebuilds the `META/` directory based on the current state of the `MANIFEST/`, ensuring that your metadata accurately reflects the existing data files.
    
    This command will re-create all metadata in the `META/` directory.
    
    If you have customized the metadata, you will need to manually remove the affected DocumentReference entries before running this command to avoid conflicts or inconsistencies.

### 4. Commit Changes

Once you've reviewed the changes, commit them to your local repository:

```bash
git-drs commit -m "Removed sample1.vcf.gz and updated associated metadata"
```
This command records the deletion of the file and the updates to the manifest and metadata.

---

## 🚀 Pushing Updates to the Platform

After committing your changes, push them to the CALYPR platform to update the remote repository.

### 1. Push Changes

Use the `git-drs push` command to upload your changes:

```bash
git-drs push
```

This command performs the following actions:

- Validates the updated manifest and metadata.
- Uploads the changes to the remote repository.
- Provides logs detailing the outcome of the push operation.

### 2. Using the `--bundle` and `--overwrite` Option

If you have previously pushed changes and want to ensure that the metadata is up-to-date, you can use the `--bundle` option with the `git-drs push` command:

```bash
git-drs push --bundle --overwrite
```

---

## 🧾 Reviewing Logs

After pushing your changes, review the logs to confirm that the operation was successful:

- Logs are stored in the `.drs/` directory.
- Each log entry is a JSON object detailing the status of the submission (e.g., success or error).
- Example of a successful deletion log entry:

---

## 📌 Best Practices

- Always use `git-drs rm` to delete files to ensure that the manifest and metadata are properly updated.
- Use `git-drs meta init` to regenerate metadata when necessary, especially after significant changes to your data files.
- Utilize the `--bundle` option with `git-drs push` when you need to create a cohesive, versioned set of changes for distribution or archival purposes.
- Regularly review logs after pushing changes to confirm successful updates.

---

By following these steps, you can maintain a consistent and accurate state across your data, manifest, and metadata in your CALYPR project. 
