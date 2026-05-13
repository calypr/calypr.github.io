---
title: Data Management
---

# Data Management

The current `data-client` transfer workflow is built around `upload`, `download-single`, and `download-multiple`. Those are the commands most users need.

## Uploading Data

Use `upload` for normal file, directory, or glob uploads.

```bash
./data-client upload --profile=mycommons --upload-path=data/sample.bam
```

Common patterns:

```bash
./data-client upload --profile=mycommons --upload-path=data/
./data-client upload --profile=mycommons --upload-path='data/*.bam'
./data-client upload --profile=mycommons --upload-path=data/ --batch --numparallel=5
```

Useful flags:

| Flag | Meaning |
| --- | --- |
| `--upload-path` | File path, directory path, or glob to upload |
| `--batch` | Enable parallel uploads |
| `--numparallel` | Number of concurrent uploads when `--batch` is enabled |
| `--include-subdirname` | Preserve subdirectory names in uploaded object names |
| `--metadata` | Look for `[filename]_metadata.json` sidecar files and upload metadata too |
| `--bucket` | Override the target bucket |

`--metadata` is only useful in environments that expose the Shepherd API.

## Multipart Uploads

Use `upload-multipart` when you want to upload one large file explicitly with the multipart path.

```bash
./data-client upload-multipart --profile=mycommons --file-path=./large.bam
./data-client upload-multipart --profile=mycommons --file-path=./large.bam --guid=existing-guid
```

Useful flags:

| Flag | Meaning |
| --- | --- |
| `--file-path` | Local file to upload |
| `--guid` | Reuse an existing GUID instead of creating a new one |
| `--bucket` | Override the target bucket |

## Retrying Failed Uploads

If you already have a failed upload log from a previous run, retry it with:

```bash
./data-client retry-upload --profile=mycommons --failed-log-path=/path/to/failed_log.json
```

## Downloading Data

Use `download-single` for one GUID and `download-multiple` for a manifest.

### Download One File

```bash
./data-client download-single \
  --profile=mycommons \
  --guid=206dfaa6-bcf1-4bc9-b2d0-77179f0f48fc \
  --download-path=./downloads
```

### Download From a Manifest

```bash
./data-client download-multiple \
  --profile=mycommons \
  --manifest=manifest.json \
  --download-path=./downloads \
  --numparallel=4
```

The manifest is expected to contain objects with `guid` fields. `download-multiple` reads those GUIDs and downloads them in parallel.

## Legacy Commands

The binary still contains `upload-single` and `upload-multiple`, but the main docs should treat `upload` as the normal upload entrypoint.
