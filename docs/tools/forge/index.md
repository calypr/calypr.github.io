# Forge

Forge is the CALYPR metadata management tool. It streamlines the validation, publishing, and management of data dictionaries and metadata schemas for Gen3 Data Commons.

## Core Features

- **Validation**: Validate your data and schemas against the Gen3 data model.
- **Publishing**: Publish schemas and metadata to a Gen3 instance.
- **Metadata Management**: Tools to query and manipulate metadata.

## 🧬 High-Level Architecture

Forge acts as a bridge between your local research data repository (Git/LFS) and the Gen3 cloud environment. It automates the generation of FAIR-compliant metadata and ensures consistency across the platform.

### Identifier Management (Stable IDs)

Forge uses a deterministic ID generation strategy based on **UUIDv5**. Identifiers are derived from:
1.  **Namespace**: The target API endpoint (e.g., `https://calypr-commons.org`).
2.  **Context**: The Project ID and the logical path/name of the file or entity.

This ensures that IDs are **stable and predictable**. If you process the same file twice, or process it on different machines, it always receives the same ID, facilitating reproducible data linking.

### Incremental Metadata Sync (UPSERT Logic)

The `forge meta` command is built with an incremental workflow in mind. Instead of overwriting your metadata, it:
1.  **Reads Existing State**: Loads any existing `.ndjson` files from the `./META` directory.
2.  **Discovers Changes**: Compares local Git/LFS file states with the records currently indexed on the remote DRS server (e.g., `gecko`).
3.  **Merges**: Upserts technical updates (like new file versions or URLs) while **preserving** manually added rich metadata (like assay annotations or study descriptions).

### Metadata Command Pipeline

When you run `forge meta`, the following steps occur:
1.  **Local Discovery**: Identifies all files tracked by Git and Git-LFS.
2.  **Remote Fetch**: Efficiently retrieves indexing data from the DRS project list API.
3.  **FHIR Transformation**: Maps technical file records to FHIR `DocumentReference` resources.
4.  **Logical Hierarchy**: Automatically generates FHIR `Directory` resources to reconstruct your folder structure as a navigable tree in the UI.
5.  **Project Context**: Links everything to a `ResearchStudy` resource representing the project container.

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

Tools for generating and managing FHIR-compatible metadata.

```bash
forge meta [subcommand]
```
- **`forge meta`**: Generates full metadata set (`DocumentReference`, `Directory`, `ResearchStudy`).
- **`forge meta tree`**: Visualizes the logical directory structure of your generated metadata.

### `config`

Manage Forge configuration settings for your explorer UI.

```bash
forge config
```
