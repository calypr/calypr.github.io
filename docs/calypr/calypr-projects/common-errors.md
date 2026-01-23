# Common Errors

`TODO - rewrite for git-drs`

## .ndjson is out of date
**Error:** After `git-drs` adding and committing a file, when you go to submit your data, "DocumentReference.ndjson is out of date",
```sh
$ git add file.txt
$ git commit -m "adding file.txt"
$ git push
Please correct issues before pushing.
Command `g3t status` failed with error code 1, stderr: WARNING: DocumentReference.ndjson is out of date 1969-12-31T16:00:00. The most recently changed file is MANIFEST/file.txt.dvc 2025-02-28T09:24:46.283870.  Please check DocumentReferences.ndjson
No data file changes.
```

**Resolution:** As well as checking that all files are committed, `g3t status` also ensures that FHIR metadata in `META/` is up to date. This means that you likely missed a crucial step in the process, updating the FHIR metadata using the file manifest! The general flow for adding file metadata is `g3t add` > `g3t meta init` > `g3t commit`. To resolve this, update and commit the FHIR metadata:

```sh
$ g3t meta init
Updated 2 metadata files.
resources={'summary': {'DocumentReference': 1, 'ResearchStudy': 1}} exceptions=[]

$ g3t push
```

To better understand the process of adding file metadata through the manifest, see [adding file metadata](add-files.md) and [adding FHIR metadata](metadata.md).

## No new files to index

**Error:**
```sh
$ g3t push
No new files to index.  Use --overwrite to force
```

**Resolution:** When pushing data, `g3t` checks the manifest (`MANIFEST/` directory) to see if there are any files to update, including new files or modified files. If no files have been modified, then the push will not go through. To push up the same file data or push up new FHIR metadata (`META/`), use `g3t push --overwrite`

## Uncommitted changes

**Error:** On the subsequent rounds of adding files, updating FHIR metadata, and committing the changes, you are unable to push up those new changes
```
$ g3t add hello.txt
$ g3t meta init
$ g3t commit -m "add hello file"

$ g3t push
Uncommitted changes found.  Please commit or stash them first.

$ g3t status
No data file changes.
On branch main
Changes not staged for commit:
 ...
 modified:   META/DocumentReference.ndjson
```

**Resolution:** This happened because the update FHIR metadata created in the META init was not staged for commit. To stage and commit the FHIR metadata, do:

```sh
$ git add META/
$ g3t commit -m "update DocumentReference.json"
$ g3t push
```

Note that `git add` is used here rather than `g3t add` because `git add` will update the project's FHIR metadata while `g3t add` only updates the project's manifest. If you want to commit multiple file changes, you can also use `g3t commit -am "update all files"`, where all changes get committed to the project.