---
title: Forge
---

# Forge

Forge is the CALYPR metadata management tool. It streamlines the validation, publishing, and management of data dictionaries and metadata schemas for Gen3 Data Commons.

## Core Features

- **Validation**: Validate your data and schemas against the Gen3 data model.
- **Publishing**: Publish schemas and metadata to a Gen3 instance.
- **Metadata Management**: Tools to query and manipulate metadata.

## Commands

### `validate`

The `validate` command suite is used to ensure your data and configurations are correct before submission.

- **`forge validate config <file>`**: Validates a configuration file.
- **`forge validate data <file>`**: Validates data files (e.g., JSON, TSV) against the schema.
- **`forge validate edge <file>`**: Validates relationships (edges) between data nodes.

### `publish`

Manage the publishing lifecycle of your data schemas.

- **`forge publish`**: Publish the current schema/metadata to the configured environment.
- **`forge publish status`**: Check the status of a publishing job.
- **`forge publish list`**: List available publication resources.
- **`forge publish output`**: Retrieve the output of a publication process.

### `meta`

Tools for handling metadata directly.

```bash
forge meta [subcommand]
```

### `config`

Manage Forge configuration settings.

```bash
forge config
```
