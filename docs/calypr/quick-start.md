---
title: Quick Start Guide
---

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

## Download Gen3 API Credentials

To use the git-drs, you need to configure `git-drs` with API credentials downloaded from the [Profile page](https://calypr-public.ohsu.edu/Profile).

![Gen3 Profile page](../images/profile.png)

Log into the website. Then, download the access key from the portal and save it in the standard location `~/.gen3/credentials.json`

![Gen3 API Key](../images/api-key.png)

![Gen3 Credentials](../images/credentials.png)

## Git DRS Workflows

For complete Git DRS documentation including setup, workflows, and S3 integration, see the [Git DRS Quick Start](../tools/git-drs/quickstart.md).
