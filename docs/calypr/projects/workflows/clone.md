
# Cloning a Project


The `git-drs clone` command is used to clone a project from the remote repository. Here's a brief explanation of what happens when you use git-drs clone:

* A subdirectory is created for the project, it is named after the `project_id`.
* The project is initialized locally, including the `.drs` and `META` directories.
* The current metadata is downloaded from the remote repository.  
* By default, data files are not downloaded by default

```sh
git-drs clone --help
Usage: git-drs clone [OPTIONS] PROJECT_ID

  Clone meta and files from remote.

Options:
  --help  Show this message and exit.
```
