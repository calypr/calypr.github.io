---
title: Download
---

There are two main ways to download files:

1. Individually through the browser or through the command line with the `gen3-client`
2. Batch downloads through the command line with `g3t`

This guide will walk you through both methods below.

## Download a Single File

### Explorer Page

The easiest way to download a single file is through the [Explorer page](https://calypr.ohsu.edu/Explorer). This page will show all files belonging to projects that you have access to.

To download a single file:

1. Select the **File tab** and scroll down to the list of files
2. Select the row for the file of interest
3. Select **File Download** on the file page

### gen3-client

Alternatively, if you already know the GUID of the file of interest, simply pass it to the gen3-client:

```sh
gen3-client download-single --profile=calypr --guid=<GUID>
```

For example, to download the file with GUID `f623df8f-5dad-5bce-a8ca-a7b69b7805a5`:

```sh
gen3-client download-single --profile=calypr --guid=f623df8f-5dad-5bce-a8ca-a7b69b7805a5
```

### Download All Files

To retrieve the actual data files described by manifest as opposed to just the file metadata, use the pull command.

```bash
g3t clone calypr-myproject
cd calypr-myproject
g3t pull
```