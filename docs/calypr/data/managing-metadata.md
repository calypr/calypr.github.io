# Managing Metadata

Metadata in Calypr is represented as FHIR resources in newline-delimited JSON files (.ndjson).

If you are bringing your own FHIR metadata, create a `META/` directory at the root of your initialized `git-drs` repository and place your metadata files there.

The `META/` directory contains one resource file, with each file representing a single FHIR resource type. For example, `META/ResearchStudy.ndjson` should contain only `ResearchStudy` resources. Using one file per resource type keeps validation and troubleshooting straightforward.

For projects with Git LFS-managed data files, each data file must have a corresponding `DocumentReference` resource.

## META/ResearchStudy.ndjson

* The entry tree root in the portal is based on the first `ResearchStudy` record in this file.
* Auto-generated `DocumentReference` resources are linked to that first `ResearchStudy`.
* Additional `ResearchStudy` records may be preserved in metadata, but they are not used to build the default file tree root.
* Contains at least one FHIR ResearchStudy resource describing the project.  
* Defines project identifiers, title, description, and key attributes.

## META/DocumentReference.ndjson

* Contains one FHIR DocumentReference resource per Git LFS-managed file.  
* Each `DocumentReference.content.attachment.url` field:
  * Must exactly match the relative path of the corresponding file in the repository (for example, `data/file1.bam`).
  * Example:

```json
{
  "resourceType": "DocumentReference",
  "id": "docref-file1",
  "status": "current",
  "content": [
    {
      "attachment": {
        "url": "data/file1.bam",
        "title": "BAM file for Sample X"
      }
    }
  ]
}
```

Place your custom FHIR `.ndjson` files in the `META/` directory:

```bash
# Copy your prepared FHIR metadata
cp ~/my-data/patients.ndjson META/
cp ~/my-data/observations.ndjson META/
cp ~/my-data/specimens.ndjson META/
cp ~/my-data/document-references.ndjson META/
```

## Other FHIR Data

You can include additional resource types to represent subjects, specimens, assays, and measurements.

Common examples:

* `Patient.ndjson`: Participant records.
* `ResearchSubject.ndjson`: Participant enrollment in a study.
* `Specimen.ndjson`: Biological specimens.
* `Task.ndjson` or `ServiceRequest.ndjson`: Procedures, pipeline steps, or assay workflow context.
* `Observation.ndjson`: Measurements or results.
* Other valid FHIR resource types as required.

When these files are present, ensure references are internally consistent (for example, a `DocumentReference.subject.reference` should point to an existing `Patient`, `Specimen`, or `ResearchStudy` record).

### Important: `DocumentReference` URL Format

In a `git-drs` repository, `DocumentReference.content.attachment.url` should be the repository-relative file path, not a `drs://` URI.

Example:

```json
{
  "resourceType": "DocumentReference",
  "id": "doc-001",
  "status": "current",
  "content": [{
    "attachment": {
      "url": "data/sample1.bam",
      "title": "sample1.bam",
      "contentType": "application/octet-stream"
    }
  }],
  "subject": {
    "reference": "Patient/patient-001"
  }
}
```


---

## Validating Metadata

To ensure that the FHIR files you added are valid and graph-consistent, use [Forge validation](../../tools/forge/validation.md).

```bash
forge validate data --path META
```

Successful output:

✓ Validating META/patients.ndjson... OK  
✓ Validating META/observations.ndjson... OK  
✓ Validating META/specimens.ndjson... OK  
✓ Validating META/document-references.ndjson... OK  
All metadata files are valid.

Fix any validation errors and re-run until all files pass.


### Forge Data Quality Assurance Command Line Commands

If you provide your own FHIR resources, these two commands are the most useful checks before submission.

**Validate:**
```bash
forge validate data --path META
# or
forge validate data --path META/DocumentReference.ndjson
```
Validation checks if the provided directory or file will be accepted by the CALYPR data platform. It catches improper JSON formatting and FHIR schema errors.

**Check-edge:**
```bash
forge validate edge --path META
# or
forge validate edge --path META --out-dir tmp/graph-check
```
Check-edge ensures that references within your files (e.g., a Patient ID in an Observation) connect to known vertices and aren't "orphaned".

### Validation Process

#### 1\. Schema Validation

* Each .ndjson file in META/ (like ResearchStudy.ndjson, DocumentReference.ndjson, etc.) is read line by line.  
* Every line is parsed as JSON and checked against the corresponding FHIR schema for that resourceType.  
* Syntax errors, missing required fields, or invalid FHIR values trigger clear error messages with line numbers.

#### 2\. Mandatory Files Presence 

* Confirms that:  
  * ResearchStudy.ndjson exists and has at least one valid record.  
  * DocumentReference.ndjson exists and contains at least one record.  
* If either is missing or empty, validation fails.

#### 3\. One-to-One Mapping of Files to DocumentReference 

* Scans the working directory for Git LFS-managed files in expected locations (e.g., data/).  
* For each file, locates a corresponding DocumentReference resource whose content.attachment.url matches the file’s relative path.  
* Validates:  
  * All LFS files have a matching DocumentReference.  
  * All DocumentReferences point to existing files.

#### 4\. Project-level Referential Checks 

* Validates that DocumentReference resources reference the same ResearchStudy via relatesTo or other linking mechanisms.  
* If FHIR resources like Patient, Specimen, ServiceRequest, Observation are present, ensures:  
  * Their id fields are unique.  
  * DocumentReference correctly refers to those resources (for example, via `subject`).

#### 5\. Cross-Entity Consistency 

* If multiple optional FHIR .ndjson files exist:  
  * Confirms IDs referenced in one file exist in others.  
  * Detects dangling references (for example, a `DocumentReference.subject.reference` that points to a missing `Patient`).

---

#### ✅ Example Error Output

ERROR META/DocumentReference.ndjson line 4: url "data/some\_missing.bam" does not resolve to an existing file  
ERROR META/Specimen.ndjson line 2: id "specimen-123" referenced in Observation.ndjson but not defined

---

#### 🎯 Purpose & Benefits 

* Ensures all files and metadata are in sync before submission.  
* Prevents submission failures due to missing pointers or invalid FHIR payloads.  
* Enables CI integration, catching issues early in the development workflow.

---

#### Validation Requirements 

Automated tools or CI processes must:

* Verify presence of META/ResearchStudy.ndjson with at least one record.  
* Verify presence of META/DocumentReference.ndjson with one record per LFS-managed file.  
* Confirm every DocumentReference.url matches an existing file path.  
* Check proper .ndjson formatting.

---