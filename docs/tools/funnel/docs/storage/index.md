---
title: Storage
lead: "Funnel storage backends handle downloading task inputs and uploading task outputs."
personas:
  - platform-engineer
  - workflow-engineer
solutions:
  - manage-compute
related_tools:
  - funnel
---

# Storage

Funnel storage backends handle downloading task inputs and uploading task outputs.
Each input/output URL in a task is resolved by its URL scheme (for example `s3://`,
`gs://`, or `file://`).

### Choosing a storage backend

- Use [Local](/tools/funnel/docs/storage/local/) for files on worker-accessible disks.
- Use [HTTP(S)](/tools/funnel/docs/storage/http/) for public URLs and presigned object links.
- Use [FTP](/tools/funnel/docs/storage/ftp/) for FTP-hosted files.
- Use [S3](/tools/funnel/docs/storage/s3/) for Amazon S3 and S3-compatible object stores.
- Use [OpenStack Swift](/tools/funnel/docs/storage/swift/) for Swift object storage.
- Use [Google Storage](/tools/funnel/docs/storage/google-storage/) for Google Cloud Storage.

### URL schemes

| Backend | URL scheme |
| --- | --- |
| Local | `file://` |
| HTTP(S) | `http://`, `https://` |
| FTP | `ftp://` |
| S3 | `s3://` |
| OpenStack Swift | `swift://` |
| Google Storage | `gs://` |

### Notes

- Most cloud/object backends can load credentials from the environment, but each backend page includes explicit config options.
- Storage clients can be enabled/disabled in worker configuration.
- The worker process performs all transfer operations before and after executor commands run.
