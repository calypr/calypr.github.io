---
title: Configuration
---

# Forge Configuration

Forge manages the configuration for the CALYPR Explorer UI. This configuration defines how data is displayed, filtered, and accessed in the web interface.

## Creating a Configuration

You can generate a starter configuration template for your project using the `forge config` command.

```bash
forge config --remote <remote-name>
```

This command:
1.  Reads the Project ID from your specified remote (or default remote).
2.  Creates a `CONFIG` directory if it doesn't exist.
3.  Generates a template JSON file named `<project_id>.json` inside `CONFIG/`.

**Example:**

```bash
forge config --remote production
```

If your project ID is `my-project`, this creates `CONFIG/my-project.json`.

## Editing Configuration

The configuration is a standard JSON file. You can edit it with any text editor.

### Top-Level Structure

The configuration is an array of objects, where each object represents a **Tab** in the data explorer (e.g., "Patients", "Samples", "Files").

```json
{
  "ExplorerConfig": [
    {
      "tabTitle": "Research Subject",
      "filters": { ... },
      "table": { ... },
      "guppyConfig": { ... }
    }
  ]
}
```

### Key Components

#### `tabTitle`
The display name of the tab in the UI.

#### `guppyConfig`
Defines the connection to the backend index (Guppy).

-   `dataType`: The index type in Guppy (e.g., "patient", "file").
-   `nodeCountTitle`: Label for the count of items (e.g., "Patients").
-   `accessibleFieldCheckList`: Fields to check for access control (usually `["project_id"]`).

#### `table`
Configures the data table displayed in the tab.

-   `enabled`: Set to `true` to show the table.
-   `fields`: Array of field names to include in the table data.
-   `columns`: Dictionary defining how each field is rendered.
    -   `title`: Column header text.
    -   `cellRenderFunction`: Optional custom renderer (e.g., "HumanReadableString" for file sizes).

#### `filters`
Configures the faceted search filters on the left sidebar.

-   `tabs`: Grouping of filters.
    -   `fields`: List of fields to show as filters.
    -   `fieldsConfig`: Custom labels for the filters.

## Example Configuration

Here is a simplified example configuration for a "Research Subject" tab:

```json
{
  "ExplorerConfig": [
    {
      "tabTitle": "Research Subject",
      "guppyConfig": {
        "dataType": "researchsubject",
        "nodeCountTitle": "Research Subjects",
        "accessibleFieldCheckList": ["project_id"]
      },
      "filters": {
        "tabs": [
          {
            "fields": ["project_id", "gender", "race"],
            "fieldsConfig": {
              "project_id": { "label": "Project" },
              "gender": { "label": "Gender" }
            }
          }
        ]
      },
      "table": {
        "enabled": true,
        "fields": ["project_id", "submitter_id", "gender", "race"],
        "columns": {
          "project_id": { "title": "Project" },
          "submitter_id": { "title": "ID" },
          "gender": { "title": "Gender" },
          "race": { "title": "Race" }
        }
      }
    }
  ]
}
```

## Validation

After editing your configuration, always validate it to ensure there are no syntax errors or invalid structures.

```bash
forge validate config --path CONFIG/my-project.json
```
