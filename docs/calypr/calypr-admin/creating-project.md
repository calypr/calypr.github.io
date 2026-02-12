---
title: Creating a Project
---

## CLI

```bash
$ git drs init --help

Usage: git drs init [OPTIONS] [PROJECT_ID]

  Initialize a new repository.

Options:
  --debug        Enable debug mode. G3T_DEBUG environment variable can also be used.
  --help         Show this message and exit.
```

## Overview
The `git drs init` command initializes a new project in your current working directory. It works with existing files in the directory and creates a couple important directories:

* `META/`: A visible directory within your project that houses the FHIR metadata files.
* `CONFIG/`: Any additional configurations that can be used to customize the gen3 data platform. 

An initialized project will look something like this...

```
.
├── .git                                  // git repository state
├── META                                  // metadata in FHIR format
├── CONFIG
└── <your data here>                      // existing data files maintained
 └── ...
```

## Choosing a Project ID

> In a Gen3 Data Commons, programs and projects are two administrative nodes in the graph database that serve as the most upstream nodes. A program must be created first, followed by a project. Any subsequent data submission and data access, along with control of access to data, is done through the project scope.
> [more](https://gen3.org/resources/operator/#6-programs-and-projects)

A project ID initializes a unique project, taking the form of program-project. A project ID is significant because it determines the location of the remote repository, bucket storage, and access control. Project IDs have a set of constraints, particularly the program name is predefined by the institution, while the project name must be unique within the server and alphanumeric without spaces. Contact an admin for a list of supported program names.

### Authorization
While you can work with an initialized repository locally, **an authorized user will need to sign** the project request before you can push your project to the data platform. You can confirm your project authorization with `git drs ping`

## Next steps

- [Adding data to a project](../data-management/git-drs.md)