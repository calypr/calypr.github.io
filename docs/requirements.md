---
title: Requirements
---

# Requirements

## 1. Download gen3-client

gen3-client to upload and download files to the [gen3 platform](https://gen3.org/). Since the CALYPR is built on gen3, gen3-client is used in calypr_admin for the same purpose. See the instructions below for how to download gen3-client for your operating system.

### Installation Instructions


=== "macOS"
    1. Download the [macOS version](https://github.com/CALYPR/cdis-data-client/releases/latest/download/gen3-client-macos.pkg) of the gen3-client.
    2. Run the gen3-client pkg, following the instructions in the installer.
    3. Open a terminal window.
    4. Create a new gen3 directory: `mkdir ~/.gen3`
    5. Move the executable to the gen3 directory: `mv /Applications/gen3-client ~/.gen3/gen3-client`
    6. Change file permissions: `chown $USER ~/.bash_profile`
    7. Add the gen3 directory to your PATH environment variable: `echo 'export PATH=$PATH:~/.gen3' >> ~/.bash_profile`
    8. Refresh your PATH: `source ~/.bash_profile`
    9. Check that the program is downloaded: run `gen3-client`


=== "Linux"
    1. Download the [Linux version](https://github.com/CALYPR/cdis-data-client/releases/latest/download/gen3-client-linux-amd64.zip) of the gen3-client.
    2. Unzip the archive.
    3. Open a terminal window.
    4. Create a new gen3 directory: `mkdir ~/.gen3`
    5. Move the unzipped executable to the gen3 directory: `~/.gen3/gen3-client`
    6. Change file permissions: `chown $USER ~/.bash_profile`
    7. Add the gen3 directory to your PATH environment variable: `echo 'export PATH=$PATH:~/.gen3' >> ~/.bash_profile`
    8. Refresh your PATH: `source ~/.bash_profile`
    9. Check that the program is downloaded: run `gen3-client`

=== "Windows"
    1. Download the [Windows version](https://github.com/CALYPR/cdis-data-client/releases/latest/download/gen3-client-windows-amd64.zip) of the gen3-client.
    2. Unzip the archive.
    3. Add the unzipped executable to a directory, for example: `C:\Program Files\gen3-client\gen3-client.exe`
    4. Open the Start Menu and type "edit environment variables".
    5. Open the option "Edit the system environment variables".
    6. In the "System Properties" window that opens up, on the "Advanced" tab, click on the "Environment Variables" button.
    7. In the box labeled "System Variables", find the "Path" variable and click "Edit".
    8.  In the window that pops up, click "New".
    9.  Type in the full directory path of the executable file, for example: `C:\Program Files\gen3-client`
    10. Click "Ok" on all the open windows and restart the command prompt if it is already open by entering cmd into the start menu and hitting enter.

## 2. Configure a gen3-client Profile with Credentials

To use the gen3-client, you need to configure  `gen3-client` with API credentials downloaded from the [Profile page](https://calypr.ohsu.edu.org/Profile).

![Gen3 Profile page](images/profile.png)

Log into the website. Then, download the access key from the portal and save it in the standard location `~/.gen3/credentials.json`

![Gen3 Credentials](images/credentials.png)

From the command line, run the gen3-client configure command:

=== "Example Command"
    ```sh
    gen3-client configure \
        --profile=<profile_name> \
        --cred=<credentials.json> \
        --apiendpoint=https://calypr.ohsu.edu.org
    ```

=== "Mac/Linux"
    ```sh
    gen3-client configure \
        --profile=calypr \
        --cred=~/Downloads/credentials.json \
        --apiendpoint=https://calypr.ohsu.edu.org
    ```
=== "Windows"
    ```sh
    gen3-client configure \
        --profile=calypr \
        --cred=C:\Users\demo\Downloads\credentials.json \
        --apiendpoint=https://calypr.ohsu.edu.org
    ```

Run the `gen3-client auth` command to confirm you configured a profile with the correct authorization privileges. Then, to list your access privileges for each project in the commons you have access to:

```sh
gen3-client auth --profile=calypr

# 2023/12/05 15:07:12
# You have access to the following resource(s) at https://calypr.ohsu.edu.org:
# 2023/12/05 15:07:12 /programs/calypr/projects/myproject...
```

## 3. Install calypr_admin

The `calypr_admin` tool requires a working Python 3 installation no older than [Python 3.12](https://www.python.org/downloads/release/python-3120/). Check your version with `python3 --version`. If needed, download a compatible version of [Python 3](https://www.python.org/downloads/).

Optionally, create a virtual environment using venv or conda for calypr_admin. We will use [venv](https://docs.python.org/3/library/venv.html) in the instructions.

```
python3 -m venv venv; source venv/bin/activate
```

Run the following in your working directory to install the latest version of calypr_admin from the Python Package Index:

```sh
pip install calypr_admin
```

You can verify the installation was successful by then running the `calypr_admin` command with the expected output being the [latest version](https://pypi.org/project/calypr_admin/#history):

```sh
calypr_admin --version
```

### Upgrading calypr_admin

This version should match the latest version on the [PyPi page](https://pypi.org/project/calypr_admin/). If it is out of date, run the following to upgrade your local version:

```sh
pip install -U calypr_admin
```

### Configuration

calypr_admin uses the [gen3-client](https://gen3.org/resources/user/gen3-client/#2-configure-a-profile-with-credentials) configuration flow.

After configuration, you can either specify the `--profile` or set the `CALYPR_PROFILE=profile-name` environmental variable.

### Testing the configuration

The command `calypr_admin ping` will confirm that the access key and gen3-client have been configured correctly

```sh
calypr_admin --profile calypr ping
```

A successful ping will output something like:

> msg: 'Configuration OK: Connected using profile:calypr'
>
> endpoint: https://calypr.ohsu.edu.org
>
> username: someone@example.com
>
> bucket_programs:
>
>   ...
> 
> your_access:
>
>   ...

With calypr_admin completely set up, see the [Quickstart Guide](/workflows/quick-start-guide) for how to upload and download data to a project.
