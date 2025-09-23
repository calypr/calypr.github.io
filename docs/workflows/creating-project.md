---
title: Creating a Project
---

{% include '/note.md' %}

## CLI

`TODO - rewrite for git-drs`

```bash
$ g3t init --help

Usage: g3t init [OPTIONS] [PROJECT_ID]

  Initialize a new repository.

Options:
  --debug        Enable debug mode. G3T_DEBUG environment variable can also be used.
  --help         Show this message and exit.
```

## Overview
The `g3t init` command initializes a new project in your current working directory. It works with existing files in the directory and creates a couple important directories:

* `.g3t/`: a hidden directory within your project that houses the internal data structure required for version control.
* `META/`: a visible directory within your project that houses the FHIR metadata files.
* `MANIFEST/`: a visible directory within your project that houses additional file-specific metadata.

An initialized project will look something like this...

```
.
├── .g3t                                  // g3t project state
│   ├── config.yaml
│   └── state
├── .git                                  // git repository state
├── META                                  // metadata in FHIR format
├── MANIFEST
└── <your data here>                      // existing data files maintained
 └── ...
```

## Choosing a Project ID
A project ID initializes a unique project, taking the form of <program\>-<project\>. A project ID is significant because it determines the location of the remote repository, bucket storage, and access control. Project IDs have a set of constraints, particularly the program name is predefined by the institution, while the project name must be unique within the server and alphanumeric without spaces. Contact an admin for a list of supported program names.

### Authorization
While you can work with an initialized repository locally, **an authorized user will need to sign** the project request before you can push your project to the data platform. You can confirm your project authorization with `g3t ping`

## Next steps

- [Adding data to a project](add-files.md)