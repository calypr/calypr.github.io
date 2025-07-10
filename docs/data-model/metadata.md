# Creating and Uploading Metadata

### Create Metadata

Create basic, minimal metadata for the project:

```sh
gen3_util meta create /tmp/$PROJECT_ID

ls -1 /tmp/$PROJECT_ID
DocumentReference.ndjson
Observation.ndjson
Patient.ndjson
ResearchStudy.ndjson
ResearchSubject.ndjson
Specimen.ndjson
Task.ndjson
```

### Retrieve existing metadata
Retrieve the existing metadata from the portal.

```sh

gen3_util meta cp

TODO
```

### Integrate your data

Convert the FHIR data to tabular form.

```sh
TODO
```

Convert the tabular data to FHIR.

```sh
TODO
```

Validate the data

```sh
$ gen3_util meta validate --help
Usage: gen3_util meta validate [OPTIONS] DIRECTORY

  Validate FHIR data in DIRECTORY.

```



### Publish the Metadata

```text
# copy the metadata to the bucket and publish the metadata to the portal
gen3_util meta publish /tmp/$PROJECT_ID
```

## View the Files

This final step uploads the metadata associated with the project and makes the files visible on the [Explorer page](https://aced-idp.org/explorer).

<a href="https://aced-idp.org/explorer">![Gen3 File Explorer](./explorer.png)</a>
