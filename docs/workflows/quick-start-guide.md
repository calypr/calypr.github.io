
# Quickstart Guide

{% include '/note.md' %}

## About

gen3 tracker, or g3t, is a command line tool for the CALYPR platform. It provides a set of utilities for users to upload data to and download data from the platform. The following tutorial will walk you through the steps for two different use cases:

1. Uploading files for a new project to the platform
2. Downloading an existing project from the platform

Each step will outline the command to execute followed by a brief description of the command's functionality.

## Requirements

Please ensure you have completed the following setup from the [Requirements](/requirements) page:

1. Installed gen3-client
2. Configured a gen3-client profile with credentials
3. Installed gen3-tracker


To confirm all dependencies are set up as expected, run

```sh
g3t --profile <your_g3t_profile_name> ping
```

You should get a message like this

> msg: 'Configuration OK: Connected using profile:calypr'
endpoint: https://calypr.ohsu.edu
username: someone@example.com

along with the set of projects you have been provided access to.

## General Usage

```sh
g3t [OPTIONS] COMMAND [ARGS]...
```

g3t is built on git, so many commands behave similarly to git with some key differences. These differences will be outlined for each step in the submission process.

## 1. Upload Data to a Newly Approved Project

The first use case we will cover is how to add data to a new project on the CALYPR.

!!! note
    The following examples will use the `calypr` program with a project called `myproject` and an `calypr` g3t profile.

### Check Project Permissions

To start, check what projects you have access to using the command

```sh
g3t projects ls
```

Check that you have permission to edit `calypr-myproject`. This is what allows you to push data up to the platform. If you do not have the correct permissions, please contact a system administrator.

### Specify a gen3 Profile

For most g3t commands, you need to specify the gen3-client profile you want to use. This ensures that you are uploading projects to the right platform with the right credentials. There are two ways to set your profile...

To set a profile using an environmental variable:
```sh
export G3T_PROFILE=calypr
```

To pass the profile as a flag to the `ping` command for example:

```sh
g3t --profile calypr ping
```

For the rest of the tutorial, we will assume you have exported a `G3T_PROFILE` environment variable so we don't have to use the `--profile` flag each time.

### Initialize a new project

To initialize your new project locally, you can use `g3t init`

```bash
mkdir calypr-myproject
cd calypr-myproject
g3t init calypr-myproject
```

* Similar to `git init`, this command creates a new project in the current directory
* Within the project, there are a couple important directories...
    * `MANIFEST/`: stores file metadata entries
    * `META/`: stores metadata converted into the [FHIR](https://hl7.org/fhir/) standard
    * `.g3t/`: hidden, stores and manages g3t state for the project
* The project ID is `calypr-myproject` made from the program name `calypr` and project name `myproject`. Specifically,
    * **Program name:** is predefined by the institution, defining what remote data buckets and endpoints you have access to
    * **Project name:** must be unique within the server, be alphanumeric, and contain no spaces or hyphens
* For more information, see [creating a project](creating-project.md)

### Add files to the manifest

Once your project is initialized, you can add files to the project's manifest. For example, let's say you have tsv files in a `folder/` directory within your current repository. Each of the tsv files are associated with a particular subject, say `patient_1` and `patient_2`. To add them using `g3t add`,

```bash
g3t add folder/file.tsv --patient patient_1
g3t add folder/file2.tsv --patient patient_2
```

* Each `g3t add` above creates a metadata entry for the specified data file, automatically calculating metadata like the file's md5sum, type, date modified, size, and path.
    - Just as a ship's manifest is an inventory of its cargo, the `MANIFEST/` directory is an inventory for each file's metadata
    - Each metadata entry is stored as a  `.dvc` file in the `MANIFEST` directory, where the dvc file path mirrors the original file path
    - **Example:** `folder/file.tsv` creates a `MANIFEST/folder/file.tsv.dvc` entry
* Using the patient flag is one way to associate a file with a particular subject, in this case associating each file with a specified patient identifier.
* `g3t add` varies from `git add`, as the `.dvc` file is what gets staged rather than the potentially large data file
* Multiple files can be added at the same time by wrapping a wildcard string in quotes, for example, `g3t add "*.csv"`.
* For more information on usage, such as adding entries for remote files or how to associate files with a sample, see [adding files](add-files.md)


### Create metadata

Now that your files have been staged with metadata entries, you can create FHIR-compliant metadata using the `g3t meta init` command

```bash
g3t meta init
```

* Using the file metadata entries created by the `g3t add` command, `g3t meta init` creates FHIR-compliant metadata files in the `META/` directory, where each file corresponds to a [FHIR resource](https://build.fhir.org/resourcelist.html). At a minimum, the directory will contain:

| File                     | Contents                   |
|--------------------------|----------------------------|
| ResearchStudy.ndjson     | Description of the project |
| DocumentReference.ndjson | File information           |

- Additional metadata files for patient, specimen, and other entities will be generated based on options provided to the `add` command.

| File                   | Contents               |
|------------------------|------------------------|
| Patient.ndjson         | Patient information    |
| ResearchSubject.ndjson | Enrollment information |
| Specimen.ndjson        | Sample information     |

- `meta init` is a good example of where g3t differs from git! While you might go from `git add` straight to `git commit` in a git workflow, we have to do `g3t add` > `g3t meta init` > `g3t commit` to track both the files and each file's metadata in g3t.
- `meta init` focuses on creating metadata specific to the files you added. For your particular use case, you may also want to supply your own FHIR data, see [adding FHIR metadata](metadata.md)

### Check that the metadata is valid

To ensure that the FHIR data has been properly formatted, you can call `g3t meta validate`.

```bash
g3t meta validate
```

- The system will print summary counts and informative messages if the metadata is invalid.


### Check that the expected files are queued for upload

You can double-check that all of your files have been staged with `g3t status`

```bash
g3t status
```

### Commit files

With all checks complete, you can commit the metadata we created using `g3t commit`.

```bash
g3t commit -m "adding tsv metadata"
```

- Like git, this command bundles the staged files into a single set of changes.
  - The `-m` flag adds a commit message to the changes 
  - If the commit is successful, you will see a summary of the changes logged
- As a reminder, the files that are committed to git are the FHIR metadata in META/ and the .dvc entries in MANIFEST/, not the data files themselves
- See [publishing a project](commit-push.md) for more info

### Push to CALYPR

To submit the files and metadata to the data platform, we can use `g3t push`

```bash
g3t push
```

* This command launches a job to upload project data to the specified data platform.
* Specifically, it...
    1. Checks that all files are committed before pushing
    1. Checks that the `META/` metadata is valid
    2. Indexes the data files using the file metadata in the `MANIFEST/` directory
    3. Uploads the FHIR metadata in the `META/` directory into our databases
* A push will fail if no new files are being submitted. If you need to update existing files in the manifest or update the FHIR metadata, use the `--overwrite` option to force an upload.
* A job is successful if you get a green success message.
* For other publishing options and specialized use cases, see [publishing a project](commit-push.md)

### View the Data on the Platform

Congratulations, you have submitted data to the platform! To check that your data was uploaded, login and navigate to the Exploration page on [calypr.ohsu.edu](https://calypr.ohsu.edu)!

## 2. Bulk Download Data from a Project on CALYPR

Sometimes you might want the most recent version of a data project that has already been published to the platform. To download the metadata for an existing project, use the `g3t clone` command.

```sh
g3t clone calypr-myproject
```

- The clone command will download the metadata associated with the project into a new directory
- Specifically, it downloads the metadata `.dvc` entries in `MANIFEST/` and the FHIR-compliant metadata in `META/` 

To retrieve the actual data files described by manifest as opposed to just the file metadata, use the pull command.

```bash
g3t clone calypr-myproject
cd calypr-myproject
g3t pull
```

- The pull command will retrieve the actual data files associated with the metadata.


To download only a subset of files, refer to the downloads [page](https://calypr.github.io/workflows/portal-download/). For more information on other commands or use cases, see the Use Cases & Workflows section.