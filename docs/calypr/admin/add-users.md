# Add users

## Granting user access to a project

Once a project has been created you will have full access to it. 
The project owner can add additional users to the project using the `calypr_admin collaborators` commands.

```bash
$ calypr_admin collaborators add  --help
Usage: calypr_admin collaborators add [OPTIONS] USERNAME [RESOURCE_PATH]

  Add user to project.

Options:
  -w, --write / --no-write   Give user write privileges  [default: no-
                             write]
  -a, --approve              Approve the addition (privileged)
  --dry-run                  Dry run
  --debug                    Enable debug mode
  --format [yaml|json|text]  Result format. CALYPR_FORMAT  [default:
                             yaml]
  --project_id TEXT          Gen3 program-project
  --profile TEXT             Connection name. CALYPR_PROFILE See
                             https://bit.ly/3NbKGi4

```

There are two ways to request the addition additional users to the project:

## 1. Read and Write Access

To give another user full access to the project, run the following:

```sh
calypr_admin collaborators add --write  user-can-write@example.com
```

Alternatively, to give another user read access only (without the ability to upload to the project), run the following:
```sh
calypr_admin collaborators add user-read-only@example.com
```


## 2.  Approvals
In order to implement these requests, **an authorized user will need to sign** the request before the user can use the remote repository. See `calypr_admin collaborators approve --help
`
