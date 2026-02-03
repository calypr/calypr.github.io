
# Project Customization

## Dataframer Configuration

The dataframer is used to render the FHIR `.ndjson` files into the tabular space that is used in the explorer page table. If you want to customize your project’s explorer page you will need to specify database field names that are defined in the dataframer, thus you will need to run the dataframer on your data ahead of time in order to know these field names.

See below steps for setting up `git-drs` and running dataframer commands:

```bash
python -m venv venv
source venv/bin/activate
pip install gen3-tracker==0.0.7rc27
git-drs meta dataframe DocumentReference
```

The explorer config is a large JSON document. One of the keys of note is `guppyConfig`, which is used to specify what index is to be used for the explorer page tab that you have defined. Notice that when you run `git-drs meta dataframe` it outputs:

```text
Usage: git-drs meta dataframe [OPTIONS] {Specimen|DocumentReference|ResearchSubject|MedicationAdministration|GroupMember} [DIRECTORY_PATH] [OUTPUT_PATH]

Try 'git-drs meta dataframe --help' for help.
```

Where `Specimen`, `DocumentReference`, etc. are the supported indices that can be run in the dataframe and defined in the `explorerConfig` under the `guppyConfig` key.

Note that the `guppyConfig` index names use `snake_case` formatting whereas the dataframer uses uppercase for each word.

## 5.2 Explorer Page Configuration

Forge currently supports customization of explorer pages by routing to: `https://commons-url/Explorer/[program]-[project]`

Explorer Configs can be customized by running `forge config init` and then filling out the template configuration.

The explorer config is a JSON document with a top-level key called `explorerConfig` which can host a list of "tab" configs. The tabs (e.g., "Patient", "Specimen", and "File") each denote an element in this config.

In this example, the `guppyConfig.dataType` is set to `document_reference`. We ran the `DocumentReference` dataframer command earlier to select database field names from the generated output.

```json
{
  "explorerConfig": [
    {
      "tabTitle": "TEST",
      "guppyConfig": {
        "dataType": "document_reference",
        "nodeCountTitle": "file Count",
        "fieldMapping": []
      },
      "filters": {
        "tabs": [
          {
            "title": "Filters",
            "fields": [
              "document_reference_assay",
              "document_reference_creation",
              "project_id"
            ],
            "fieldsConfig": {
              "project_id": {
                "field": "project_id",
                "label": "Project Id",
                "type": "enum"
              },
              "assay": {
                "field": "document_reference_assay",
                "label": "Assay",
                "type": "enum"
              },
              "creation": {
                "field": "document_reference_creation",
                "label": "Creation",
                "type": "enum"
              }
            }
          }
        ]
      },
      "table": {
        "enabled": true,
        "fields": [
          "project_id",
          "document_reference_assay",
          "document_reference_creation"
        ],
        "columns": {
          "project_id": {
            "field": "project_id",
            "title": "Project ID"
          },
          "assay": {
            "field": "document_reference_assay",
            "title": "Assay"
          },
          "creation": {
            "field": "document_reference_creation",
            "title": "Creation"
          }
        }
      },
      "dropdowns": {},
      "buttons": [],
      "loginForDownload": false
    }
  ]
}
```

And here is what this config looks like in the frontend:

Note that since there is only one element in the `explorerConfig` there is only one tab called “TEST” in the explorer page which is housed as `tabTitle` in the config.

#### Filters

The next important section is the `filters` key. This defines the filters column on the left-hand side of the page. Within that block there is the `fields` key and the `fieldsConfig` key. The `fields` key is used to specify the names of the fields that you want to filter on. In order to get the names of the fields you will need to install `git-drs` via PyPI and run a dataframer command which essentially creates this explorer table dataframe, so that you can configure in the frontend what parts of this dataframe you want to be shown.

Now, going back to the configuration, these fields that were specified come directly from the column names at the top of the excel spreadsheet that are generated from running the dataframer command. You can choose any number / combination of these column names, but note that in any list that is specified in this config, the elements in the list are rendered in the frontend in that exact order that is specified.

The `fieldsConfig` key is a decorator dict that is optional but can be applied to every filter that is specified. Notice that the `label` key is used to denote the preferred display name that is to be used for the database key name that was taken from the dataframer excel spreadsheet.

#### Table

The last import section is the `table` key. Like with the filters structure, `fields` is used to denote all of the database column names that should be displayed in the explorer table. Also similar to the filters structure, `columns` is where you specify the label that you want displayed for the database field. In this case it is `field` is the db name and `title` is the label display name.

The rest of the config is templating that is needed for the explorer page to load, but not anything that is directly useful.

#### Shared Filters

Imagine you want to filter on multiple index facets, similar to a RESTFUL join operation. Like for example give me all of the PATIENTS who belong on this `project_id` that also have a specimen that matches this `project_id`.

This is known as “shared filtering” because you are making the assumption that you want to carry your filters over to the new node when you click a new tab. This only works if there exists an equivalent field on the other index/tab, so it must be configurable and is not applicable for all normal filterable fields.

It sounds complex but setting it up isn't that complex at all. Simply specify a filter that you want to do shared filtering on, ie: `project_id`, then specify the indices and the field names for each index that the field is shared on. For our purposes `project_id` is known as `project_id` on all indices but this may not always be the case, and proper inspection or knowledge of the dataset may be required to determine this.

Then you simply specify each “shared filter” as a JSON dictionary list element under the field that you have specified and you have successfully setup shared filtering on that field. In order to define additional shared filters, it is as simple as adding another key under the `defined` dictionary key and specifying a list of indices and fields that the shared filter can be joined on. See the example below for details.

```json
"sharedFilters": {
  "defined": {
    "project_id": [
      { "index": "research_subject", "field": "project_id" },
      { "index": "specimen", "field": "project_id" },
      { "index": "document_reference", "field": "project_id" }
    ]
  }
}
```

## 5.3 Configurator

Now that you have the basics down this frontend GUI might start to make some sense. Notice this is the exact same config that was shown earlier, except it is customizable via the GUI so that you don’t need to wrestle with the JSON to get a working, correctly formatted config. Notice also that there is a 3rd column here: Charts. Charts are defined very simply:

```json
"charts": {
  "specimen_collection": {
    "chartType": "fullPie",
    "title": "Metastasis Site"
  }
}
```

Just provide the DB column name as the parent key, and then the chart type and the label title of the chart. The chart will generate a binned histogram counts style chart. Currently only `fullPie`, `bar` or `donut` type charts are supported but in the future other chart types might be added.

As stated earlier, configs have a very specific naming convention: `[program]-[project].json` and will be rejected if you do not have write permissions on the program, project configuration that is specified or if the name of the configuration is not of that form. You can also load any configs that you have access to too, an edit them and then repost them.

All customizable explorer pages are viewable when routing to `/Explorer/[program]-[project]` assuming that all database fields that are specified exist in the db.

# **Advanced Docs**

---

# **🧬 Managing Identifiers with CALYPR Meta**

This guide explains how to manage dataset identifiers, both manually and through the command line, and how those identifiers integrate with Git-LFS and git-drs for reproducible, FAIR-compliant data management.

### 🧭 Introduction: Where This Fits in Your Research Data Lifecycle

This document applies once you’ve begun organizing data files for a research study and are ready to make their metadata machine-readable and FAIR-compliant. Researchers typically progress through several stages:

1. **Files only**: you start with a set of raw or processed data files associated with a research study.
2. **Files with identifiers**: each file is linked to key entities such as Patients, Specimens, or Assays using `META/identifiers.tsv`.
3. **Files with identifiers + attributes**: you begin adding structured tabular metadata (e.g., `Patient.tsv`, `Specimen.tsv`, `Observation.tsv`) describing those entities.
4. **Files with complete FHIR metadata**: you can now transform these TSVs into fully-formed FHIR resources (`Patient.ndjson`, `Specimen.ndjson`, etc.) suitable for sharing, indexing, and integration with clinical or genomic data platforms.

This guide focuses on stage 2, 3 — converting well-structured TSV metadata files into standard FHIR resources, while validating that every entity’s identifier corresponds to the entries defined in `META/identifiers.tsv`.

---