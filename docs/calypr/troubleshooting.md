# Troubleshooting & FAQ

Common issues encountered when working with the CALYPR platform and its tools.

---

## Metadata is "out of date"

**Issue:** When attempting to push or validate, you receive a warning that `DocumentReference.ndjson` or other metadata files are out of date.

**Resolution:** This typically happens when you have added new data files using `git add` or `git-drs` but haven't updated the corresponding FHIR metadata to reflect these changes. 

1.  **Regenerate Metadata:** Use Forge to synchronize your metadata with the current repository state:
    ```bash
    forge meta init
    ```
2.  **Stage Changes:** Ensure the updated metadata files in the `META/` directory are staged:
    ```bash
    git add META/
    ```
3.  **Commit:**
    ```bash
    git commit -m "Update metadata for new files"
    ```

---

## No new files to index

**Issue:** Running `git push` or a registration command returns "No new files to index."

**Resolution:** This indicates that the current state of your files is already synchronized with the remote server. If you need to force an update to the metadata or re-register existing files, use the specific tool's overwrite flag (e.g., `git drs push --overwrite`).

---

## Uncommitted changes preventing push

**Issue:** You receive an error about "Uncommitted changes found" when trying to push data.

**Resolution:** Standard Git rules apply. If you've run commands that modify the `META/` directory, you must commit those changes before pushing.
```bash
git add META/
git commit -m "Refining metadata"
git push
```

---

## Authentication Errors

**Issue:** Commands fail with "Unauthorized" or "401" errors.

**Resolution:** 
1.  **Check Credentials:** Ensure your `credentials.json` is valid and hasn't expired. You can download a fresh key from the [CALYPR Profile Page](https://calypr-public.ohsu.edu/Profile).
2.  **Verify Configuration:** Run `git drs remote list` to ensure the correct endpoint and project ID are configured for your current profile.
3.  **Token Refresh:** If using temporary tokens, ensure they are still active.

---

!!! tip "Getting Help"
    If your issue isn't listed here, please reach out to our team at [support@calypr.org](mailto:support@calypr.org) or search the individual tool documentation in the [Tools Section](../tools/index.md).
