# Add users

## Granting user access to a project

Once a project has been created you will have full access to it. 
The project owner can add additional users to the project using the `g3t collaborator` commands.

There are two ways to request the addition additional users to the project:

## 1. Read and Write Access

To give another user full access to the project, run the following:

```sh
calypr-admin collaborator add --write  user-can-write@example.com
```

Alternatively, to give another user read access only (without the ability to upload to the project), run the following:
```sh
calypr-admin collaborator add user-read-only@example.com
```


## 2.  Approvals
In order to implement these requests, **an authorized user will need to sign** the request before the user can use the remote repository. See `g3t collaborator approve --help
`
