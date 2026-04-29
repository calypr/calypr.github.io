---
title: Data Management
---

# Data Management

The `data-client` facilitates secure data transfer between your local environment and the Gen3 Data Commons using the **Indexd** (indexing) and **Fence** (authentication) services.

## Uploading Data

You can upload files or directories for registration and storage in the Data Commons. The process handles:
1.  Registering the file with `Indexd` (creating a GUID).
2.  Obtaining a presigned URL from `Fence`.
3.  Uploading the file content to object storage (e.g., S3).

### Command

```bash
./data-client upload --profile=<profile-name> --upload-path=<path>
```

### Options

- `--upload-path`: Path to a single file, a folder, or a glob pattern (e.g., `data/*.bam`).
- `--batch`: Enable parallel uploads for better performance.
- `--numparallel`: Number of parallel uploads (default: 3).
- `--bucket`: Target bucket (if not using default).
- `--metadata`: Look for `[filename]_metadata.json` sidecar files to upload metadata alongside the file.

### Example

Upload a single file:
```bash
./data-client upload --profile=mycommons --upload-path=data/sample.bam
```

Upload a directory with parallel processing:
```bash
./data-client upload --profile=mycommons --upload-path=data/ --batch --numparallel=5
```

## Downloading Data

You can download data using their GUIDs (Globally Unique Identifiers).

### Command

```bash
./data-client download --profile=<profile-name> --guid=<guid>
```

### Options

- `--guid`: The GUID of the file to download.
- `--no-prompt`: Skip overwrite confirmation prompts.
- `--dir`: Target directory for download (default: current directory).

To download multiple files, you can use the `download-multiple` functionality (often via manifest, check `./data-client download --help` for specific usages as they may vary).

### Example

```bash
./data-client download --profile=mycommons --guid=dg.1234/5678-abcd
```
