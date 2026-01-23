---
title: Create Tabular Metadata
---

{% include '/note.md' %}

## Creating Tabular Data
`TODO - rewrite for git-drs`

On the Explorer page on the data platform, FHIR metadata gets flattened out from a graph structure to a tabular format so that it is more easily visualized by users. For complex use cases, you might want to see what the flattened version of the metadata looks like before submitting the data through `g3t push`. This can be done using `g3t meta dataframe`

```sh
Usage: g3t meta dataframe [OPTIONS] {Specimen|DocumentReference|ResearchSubjec
                          t|MedicationAdministration|GroupMember}
                          [DIRECTORY_PATH] [OUTPUT_PATH]

  Render a metadata dataframe.

  DIRECTORY_PATH: The directory path to the metadata.
  OUTPUT_PATH: The output path for the dataframe. Optional, defaults to "{Specimen|DocumentReference|ResearchSubject|MedicationAdministration|GroupMember}.csv"

Options:
  --dtale  Open the graph in a browser using the dtale package for interactive
           data exploration. Requires pip install dtale
  --debug
  --help   Show this message and exit
```
