
# Cloning a Project

`TODO - rewrite for git-drs`

The `g3t clone` command is used to clone a project from the remote repository. Here's a brief explanation of what happens when you use g3t clone:

* A subdirectory is created for the project, it is named after the `project_id`.
* The project is initialized locally, including the `.g3t` and `META` directories.
* The current metadata is downloaded from the remote repository.  
* By default, data files are not downloaded by default

```sh
g3t clone --help
Usage: g3t clone [OPTIONS] PROJECT_ID

  Clone meta and files from remote.

Options:
  --help  Show this message and exit.
```
