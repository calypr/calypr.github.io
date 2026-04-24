---
title: Storage
menu:
	main:
		parent: docs
---

# Storage

Funnel storage backends handle downloading task inputs and uploading task outputs.
Each input/output URL in a task is resolved by its URL scheme (for example `s3://`,
`gs://`, or `file://`).

### Choosing a storage backend

- Use [Local](./local.md) for files on worker-accessible disks.
- Use [HTTP(S)](./http.md) for public URLs and presigned object links.
- Use [FTP](./ftp.md) for FTP-hosted files.
- Use [S3](./s3.md) for Amazon S3 and S3-compatible object stores.
- Use [OpenStack Swift](./swift.md) for Swift object storage.
- Use [Google Storage](./google-storage.md) for Google Cloud Storage.

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
