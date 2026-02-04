# Adding FHIR metadata

## Background

Adding files to a project is a two-step process:

1. Adding file metadata entries to the manifest (see [adding files](add-files.md))
2. Creating FHIR-compliant metadata using the manifest

This page will guide you through the second step of generating FHIR metadata in your `git-drs` project. To understand the FHIR data model, see [FHIR for Researchers](../data-model/introduction.md)

## Generating FHIR Data using git-drs

To submit metadata from the manifest to the platform, that metadata needs to be converted into FHIR standard. We will use the file metadata entries we had created during the `git drs add` on our data files.

### Creating metadata files using the manifest

Using the file metadata entries created by the `git drs add` command, `forge meta init` creates FHIR-compliant metadata files in the `META/` directory, where each file corresponds to a [FHIR resource](https://build.fhir.org/resourcelist.html). At a minimum, this directory will create:

| File                     | Contents                   |
22: |--------------------------|----------------------------|
23: | ResearchStudy.ndjson     | Description of the project |
24: | DocumentReference.ndjson | File information           |


Depending on if a `patient` or `specimen` flag was specified, other resources can be added to the metadata files:

* subjects (ResearchSubject, Patient)
* specimens (Specimen)
* assays (Task)
* measurements (Observation)


* This command will create a skeleton metadata file for each file added to the project using the `patient`, `specimen`, `task`, and/or `observation` flags specified by the `git drs add` command.  
* You can edit the metadata to map additional fields.
* The metadata files can be created at any time, but the system will validate them before the changes are committed.
* **Note:** If an existing file is modified, it won't get automatically staged
  - For instance, if `DocumentReference.json` is already created and it has to be updated to reflect an additional file, this change is not automatically staged.
  - Make sure to either `git add META/` to ensure that your FHIR metadata changes are staged.

### Example
To add a cram file that's associated with a subject, sample, and particular task

```sh
git add myfile.cram  --patient P0 --specimen P0-BoneMarrow --task_id P0-Sequencing
```

This will produce metadata with the following relationships:

<img src="/images/create-meta-graph.png" width="100%">

When the project is committed, the system will validate new or changed records. You may validate the metadata on demand by:

```sh
$ forge meta validate --help
Usage: forge meta validate [OPTIONS] DIRECTORY

  Validate FHIR data in DIRECTORY.

```

## Rationale for the `META` directory

All FHIR metadata is housed in the `META/` directory. The convention of using a `META` directory for supporting files is common practice in data management. This directory is used to organize and store the metadata files of your project that describe the Study, Subjects, Specimens, Documents, etc. Here's a brief explanation of this convention:

* Separation of concerns: The `META` directory provides a clear separation between your metadata and other project files. This helps maintain a clean and organized project structure.
* Clarity and Readability: By placing metadata files in a dedicated directory, it becomes easier for researchers (including yourself and others) to locate and understand the main codebase. This improves overall project clarity and readability.
* Build Tools Integration: Many build tools and development environments are configured by default to recognize the `META` directory as the main metadata location. This convention simplifies the configuration process and ensures that tools can easily identify and analyze your data files.
* Consistency Across Projects: Adopting a common convention, such as using `META` for metadata files, promotes consistency across different projects. When researchers work on multiple projects, having a consistent structure makes it easier to navigate and understand each study.
* The 'META' directory will contain a file per FHIR resource with the extension [.ndjson](https://www.hl7.org/fhir/nd-json.html). e.g. `ResearchStudy.ndjson`  

## Supplying your own FHIR metadata

In some cases, it might be useful to supply your own FHIR metadata without using `git drs add` to create any file metadata. In that case, adding metadata would take on the following flow:

1. Initialize your project
2. Copy external FHIR data as `.ndjson` files to your `META/` directory
3. `git add META/`
4. `git commit -m "supplying FHIR metadata"`

This process would be useful for individuals who want to use the system to track relations between metadata but might not necessarily want to connect their actual data files to the system.

## Next Steps

See the [data management section](../data-management/meta-data.md) for more information on working with metadata and publishing.