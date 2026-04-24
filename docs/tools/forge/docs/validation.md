---
title: Validation
---

# Validation

The `forge validate` command suite ensures that your metadata and configuration files adhere to the expected formats and schemas. This is a critical step before publishing data to a Gen3 Commons.

## Validate Data

Validates FHIR-based metadata files (NDJSON format) against a JSON schema.

```bash
forge validate data [flags]
```

By default, it looks for files in a `META` directory or can be pointed to a specific file/directory.

**Flags:**
- `--path`, `-p`: Path to metadata file(s) or directory to validate (default: `META`).

**Behavior:**
- Checks if files are valid NDJSON.
- Validates each row against the corresponding JSON schema.
- Reports total files, rows, and errors found.

**Output Example:**
```text
File: META/Patient.ndjson
  Rows validated: 15
  Errors found: 0
---
Overall Totals
  Files validated: 1
  Rows validated: 15
  Errors: 0
```

## Validate Edge

Checks for integrity issues in the graph data, specifically looking for "orphaned edges"—relationships that point to non-existent vertices.

```bash
forge validate edge [flags]
```

**Flags:**
- `--path`, `-p`: Path to metadata files directory (default: `META`).
- `--out-dir`, `-o`: Directory to save generated vertices and edges files (JSON).

**Behavior:**
- Generates graph elements (vertices and edges) from the input NDJSON files.
- Verifies that every edge points to a valid destination vertex.
- Can optionally export the vertices and edges to disk.

**Output Example:**
```text
File: META/Patient.ndjson
  Rows processed: 15
  Vertices generated: 15
  Edges generated: 0
---
Orphaned Edges: 0
Overall Totals:
  Files processed: 1
  Rows processed: 15
  Vertices generated: 15
  Edges generated: 0
  Orphaned edges: 0
```

## Validate Config

Validates the explorer configuration file structure.

```bash
forge validate config [flags]
```

**Flags:**
- `--path`, `-p`: Path to config file to validate (default: `CONFIG`).
