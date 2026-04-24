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

---

## Editing Configuration

The configuration is a standard JSON file. It contains two top-level sections: `sharedFilters` and `explorerConfig`.

```json
{
  "sharedFilters": {
    "defined": {
      "project_id": [
        { "index": "research_subject", "field": "project_id" },
        { "index": "specimen", "field": "project_id" }
      ]
    }
  },
  "explorerConfig": [
    {
       "tabTitle": "Files",
       "guppyConfig": { ... },
       "filters": { ... },
       "table": { ... },
       "charts": { ... },
       "buttons": [ ... ],
       "preFilters": { ... }
    }
  ]
}
```

### `explorerConfig` (Tabs)

The `explorerConfig` is an array of objects where each object represents one tab in the Explorer UI.

#### `guppyConfig` (Backend Mapping)

Connects the tab to a specific database index.

*   `dataType`: The Gen3 node type (e.g., `document_reference`, `specimen`).
*   `nodeCountTitle`: Display label for the record count.
*   `accessibleFieldCheckList`: Array of fields used for access control (usually `["project_id"]`).
*   `accessibleValidationField`: (Optional) Field used for more granular access validation.
*   `manifestMapping`: Maps fields for file download manifests.
    *   `resourceIndexType`: The index for file resources.
    *   `resourceIdField`: The unique ID field (e.g., `_id` or `guid`).
    *   `resourceNodeType`: (Optional) Filters the manifest to specific node types.
    *   `referenceIdFieldInResourceIndex`: Cross-linking field in the resource index.
    *   `referenceIdFieldInDataIndex`: Cross-linking field in the data index.

#### `filters` (Sidebar facets)

Groups faceted filters on the left side of the explorer.

*   `tabs`: Array of filter groups (TabConfigs).
    *   `title`: Label for the filter group.
    *   `fields`: List of database fields to display as filters.
    *   `fieldsConfig`: Detailed mapping for filter labels and types.
        *   `label`: Friendly display name for the filter.
        *   `type`: Filter type. Supported: `enum`, `range`, `text`, `number`, `boolean`, `date`, `datetime`.

#### `table` (Main data view)

Configures the columns and behavior of the main results table.

*   `enabled`: Whether the table is visible.
*   `selectableRows`: (Boolean) Enable checkboxes for bulk actions.
*   `fields`: Database fields to fetch for the table.
*   `columns`: Mapping of field names to column settings.
    *   `title`: Column header name.
    *   `accessorPath`: (Optional) JSON path for nested data.
    *   `type`: Data type hint (`string`, `number`, `date`, `array`, `link`, `boolean`, `paragraphs`).
    *   `cellRenderFunction`: Name of the frontend renderer to use. Commonly used:
        *   `HumanReadableSize`: Formats bytes into KB/MB/GB.
        *   `ArrayCell`: Renders arrays as a list of badges.
        *   `NegativePositive`: Special badge coloring for 'Positive'/'Negative' values.
        *   `LinkCell`: Renders values as clickable hyperlinks.
    *   `params`: (Optional) Static parameters passed to the renderer (e.g., `{ "baseURL": "/files/" }`).
    *   `width`: CSS width (e.g., `"150px"`).
    *   `sortable`: (Boolean) Enable column sorting.
*   `detailsConfig`: Configures the side-panel view when a row is clicked.
    *   `mode`: Interaction type (`click`, `doubleclick`, `expand`, `none`).
    *   `panel`: The registered panel name (e.g., `FileDetailsPanel`).
    *   `panelContainer`: Display style (`modal` or `drawer`).
    *   `idField`: The field to use as the unique ID for the panel query.
    *   `title`: Header text for the panel.
    *   `nodeType`: (Optional) The specific Gen3 node type for the detail view.

#### `charts` (Analytics)

Defines histograms/pie charts displayed at the top of the tab.

*   Keyed by the database field name.
*   `chartType`: `fullPie`, `bar`, or `donut`.
*   `title`: Label for the chart.

#### `buttons` (Actions)

Adds action buttons to the table header.

*   `type`: Button category (`export`, `action`, `dropdown`).
*   `action`: The internal function name (e.g., `downloadManifest`, `exportToWorkspace`).
*   `title`: Button text.
*   `leftIcon` / `rightIcon`: Icon names for the button.
*   `actionArgs`: Configuration for the specific action function.

#### `preFilters`

Hard-coded filters applied to this tab. Useful for isolating data to a specific project or assay.

```json
"preFilters": {
  "project_id": ["PROJECT-A"]
}
```

---

## Example: Full Tab Config

This example demonstrates a comprehensive "Files" tab with manifest mapping, custom buttons, side-panel details, and pre-filters.

```json
{
  "tabTitle": "Files",
  "guppyConfig": {
    "dataType": "document_reference",
    "nodeCountTitle": "Files",
    "accessibleFieldCheckList": ["project_id"],
    "manifestMapping": {
      "resourceIndexType": "document_reference",
      "resourceIdField": "_id",
      "referenceIdFieldInResourceIndex": "file_id",
      "referenceIdFieldInDataIndex": "file_id"
    }
  },
  "preFilters": {
    "project_id": ["CALYPR-DEMO"]
  },
  "filters": {
    "tabs": [
      {
        "title": "Properties",
        "fields": ["project_id", "assay", "file_format"],
        "fieldsConfig": {
          "assay": { "label": "Assay Type" },
          "file_format": { "label": "Format" }
        }
      }
    ]
  },
  "table": {
    "enabled": true,
    "selectableRows": true,
    "fields": ["project_id", "assay", "file_name", "file_size"],
    "columns": {
      "file_name": { "title": "Name", "sortable": true },
      "file_size": { "title": "Size", "type": "number", "cellRenderFunction": "HumanReadableSize" }
    },
    "detailsConfig": {
      "mode": "click",
      "panel": "FileDetailsPanel",
      "panelContainer": "drawer",
      "idField": "file_id",
      "title": "File Metadata"
    }
  },
  "charts": {
    "assay": {
       "chartType": "bar",
       "title": "Assay Distribution"
    },
    "file_format": {
       "chartType": "donut",
       "title": "Formats"
    }
  },
  "buttons": [
    {
      "enabled": true,
      "type": "export",
      "action": "downloadManifest",
      "title": "Download Manifest",
      "actionArgs": {
        "resourceIndexType": "document_reference",
        "resourceIdField": "file_id"
      }
    }
  ],
  "dropdowns": {},
  "loginForDownload": true
}
```

## Validation

After editing your configuration, always validate it to ensure there are no syntax errors or invalid structures.

```bash
forge validate config --path CONFIG/my-project.json
```
