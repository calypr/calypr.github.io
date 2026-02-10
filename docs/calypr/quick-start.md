---
title: Quick Start Guide
---

!!! info "Private Beta"
    CALYPR platform is currently in a private beta phase. We are actively working with a select group of research partners to refine the platform. If you encounter any issues or have feature requests, please reach out to the team. The individual [tools](../tools/index.md) are available for public use.

# Quick Start Guide

To get started with CALYPR, you will need to install [git-lfs](https://git-lfs.github.com/) and [git-drs](https://github.com/calypr/git-drs), a "git" like command line tool for uploading and downloading files to the [gen3 platform](https://gen3.org/).

### Git-LFS Installation Instructions

To use CALYPR, you must first install [Git Large File Storage (LFS)](https://git-lfs.github.com/) on your system. This allows Git to efficiently handle the large genomic data files.

=== "macOS"
    **Install using Homebrew**
    ```bash
    brew install git-lfs
    ```

=== "Linux"
    **Install via Package Manager**

    === "Debian/Ubuntu"
        `sudo apt-get install git-lfs`

    === "RHEL/CentOS"
        `sudo yum install git-lfs`

    === "Fedora"
        `sudo dnf install git-lfs`

=== "Windows"
    **Download and Run Installer**
    Download the latest [Git LFS Windows installer](https://github.com/git-lfs/git-lfs/releases/latest) and follow the setup instructions.


**Initialize Git LFS**
Run the following command in your terminal to complete the setup:
```bash
git lfs install --skip-smudge
```

## Project Setup

You first need to set up a project and initialize it:

```
mkdir MyNewCalyprProject
cd MyNewCalyprProject
git init
git drs init
```

Now that you have initialized your project you have created a very primitive Git Large File Support (LFS) backed git repository.

## Download Gen3 API Credentials

To use the git-drs, you need to configure `git-drs` with API credentials downloaded from the [Profile page](https://calypr-public.ohsu.edu/Profile).

![Gen3 Profile page](../images/profile.png)

Log into the website. Then, download the access key from the portal and save it in the standard location `~/.gen3/credentials.json`

![Gen3 API Key](../images/api-key.png)

![Gen3 Credentials](../images/credentials.png)

### Configure a git-drs repository with a Gen3 Credential.

Now that you have a Gen3 API credential, you can attach the credential to your git-drs
repository by adding it as a drs remote.

git-drs requires a bucket name and a project id to defined in this command.

The bucket name is the name of the s3 bucket that you plan to upload your data to. This bucket must be configured inside the calypr instance. contact <fillinthisemailaddres> to setup a calypr bucket.

the project id must be in the form ORGANIZATION-PROJECTNAME.

From the command line from within your new porject, run the git-drs remote add command:

=== "Example Command"
    ```sh
    git-drs remote add gen3 <profile_name> \
        --cred=<path_to_credential.json> \
        --project <project_name>
        --bucket <bucket_name>
    ```

=== "Mac/Linux"
    ```sh
    git-drs remote add gen3 cbds \
        --cred=~/Downloads/credentials.json \
        --project testProgram-testProject \
        --bucket testBucket

    ```
=== "Windows"
    ```sh
    git-drs remote add gen3 cbds \
        --cred=C:\Users\demo\Downloads\credentials.json \
        --project testProgram-testProject \
        --bucket testBucket
    ```

You can confirm your configuration and access by listing your remotes:

```sh
git drs remote list
```

This will show your configured profiles and the projects you have access to.


## Remaining Execution

From this point forward, git-drs functions exactly like git-lfs, see [git-lfs documentation](https://github.com/git-lfs/git-lfs/tree/main/docs?utm_source=gitlfs_site&utm_medium=docs_link&utm_campaign=gitlfs) for more in depth documentation.

An example of uploading a file to calypr and downloading it can be viewed below:

### Upload Files 

```
# Track files
git lfs track "*.bam"
git add .gitattributes

# Add and commit files
git add my-file.bam
git commit -m "Add data file"
git push
```
### Downloading existing files

```
git clone mylfsrepo
cd mylfsrepo
git drs init
git drs remote add gen3 myProfile --cred ~/.gen3/credentials.json --project cbds-my_lfs_repo --bucket cbds
git lfs pull -I "*.bam"
```
