
# Integrating your data

Converting tabular data (CSV, TSV, spreadsheet, database table) into FHIR (Fast Healthcare Interoperability Resources) involves mapping your data to FHIR's resource structure. This guide walks you through the integration process from data preparation to validation.

## Overview

When you create and upload files, you can tag them with identifiers to establish an initial skeleton graph. You can then retrieve that data using the [git-drs](../../tools/git-drs/index.md) command line tool and enhance the metadata using [forge](../../tools/forge/index.md) to create a more complete graph representing your study.

You may work with data in its "native" JSON format or convert it to a tabular format for integration. The system automatically re-converts tabular data back to JSON for submission.

## Integration process

The process of integrating your data into the graph involves six key steps:

### Step 1: Identify Data and FHIR Resources

Before mapping, understand what data you have and which FHIR resources it should map to.

* **Inventory your tabular data**: Review your spreadsheet to understand the types of data it contains (e.g., patient demographics, lab results, medications, specimen information).
* **Understand relevant FHIR resources**: Familiarize yourself with FHIR resources that match your data types (e.g., [Patient](https://hl7.org/fhir/patient.html), [Observation](https://hl7.org/fhir/observation.html), [Specimen](https://hl7.org/fhir/specimen.html), [DocumentReference](https://hl7.org/fhir/documentreference.html)).

### Step 2: Map Spreadsheet Columns to FHIR Fields

Create a mapping between your data columns and FHIR resource fields.

* **Analyze your columns**: Systematically map each column to corresponding FHIR resource fields. For example, if you have a `biopsy_anatomical_location` field with values like "Prostate needle biopsies", map it to the appropriate FHIR Specimen fields such as `collection.method` and `collection.bodySite`.
* **Handle relationships**: Identify how different data pieces relate to each other and map them to FHIR resource references (e.g., linking Patient resources to their Observation resources).
 
### Step 3: Transform and Structure Your Data

Prepare your data to comply with FHIR standards.

* **Ensure consistency**: Validate data formats, especially dates (ISO 8601 format), codes (use appropriate code systems), and identifiers. Remove duplicates and address missing values.
* **Normalize into resources**: Split your spreadsheet data into separate FHIR resources. For example, separate patient demographics into Patient resources and test results into Observation resources.

### Step 4: Use FHIR Tooling and Validation

Leverage provided tools to convert and validate your data.

* **Convert your data**: Use `forge meta` to transform your data into FHIR-compliant JSON format.
* **Validate compliance**: Use `forge validate` to check that your transformed data conforms to FHIR specifications. This catches errors before submission and ensures your data is valid.

### Step 5: Commit and Deploy Your Data

Submit your validated data to the system.

* **Version and commit**: Use `git commit` to track your changes with descriptive messages.
* **Deploy**: Use `git push` to submit your data. Verify that your data appears correctly in the portal and analysis tools after deployment.

### Step 6: Iterate and Improve

Refine your data based on feedback and validation results.

* **Review and validate**: Check for discrepancies or issues in how your data appears in the system. Review user feedback.
* **Refine mappings**: Make adjustments to your data transformations and FHIR mappings as needed to improve accuracy and completeness.


## Ontologies

Ontologies within FHIR serve as a formal representation of concepts, their relationships, and properties within the healthcare domain. They provide a shared vocabulary and framework that enable consistent interpretation and exchange of healthcare data among different systems and entities.

FHIR utilizes ontologies in various ways:

* Terminology Binding: Ontologies help define and bind standardized terminologies to FHIR resources. This ensures that data elements, such as diagnoses or procedures, are uniformly understood across different studies or submissions.

* Code Systems: FHIR employs standardized code systems (like SNOMED CT, LOINC, or RxNorm) within its resources. These code systems are essentially ontologies that define concepts and relationships, allowing for precise identification and categorization of medical information.

* Mapping and Alignment: Ontologies assist in mapping data between different standards and formats. They facilitate the alignment of disparate data representations by providing a common reference point, making it easier to convert and interpret information accurately across systems.

* Semantic Interoperability: By using ontologies, FHIR promotes semantic interoperability. This means that not only can systems exchange data but also understand the meaning behind the exchanged information, enhancing communication and reducing ambiguity in healthcare data exchange.

* Consistency and Reusability: Ontologies establish a consistent and reusable framework for defining healthcare concepts. This consistency aids in data integration, analytics, and the development of applications or systems that can leverage shared knowledge.

In essence, ontologies in FHIR serve as the backbone for standardization, enabling effective communication and interpretation of healthcare data among various stakeholders, systems, and applications.

### Example: SNOMED CT

The [Specimen resource in FHIR](https://hl7.org/fhir/specimen.html) represents a sample or specimen collected during a healthcare event and contains details about its origin, type, and processing.

Mapping a [SNOMED body part](https://bioportal.bioontology.org/ontologies/SNOMEDCT?p=classes&conceptid=442083009) to a FHIR Specimen involves linking the anatomical or body site specified in SNOMED CT to the relevant information within a FHIR Specimen resource.

<img src="/images/snomed-bodypart.png" width="100%">

The mapping process typically involves several steps:

* Identification of SNOMED CT Body Part: SNOMED CT contains a comprehensive hierarchy of anatomical structures and body parts. This could include specific codes representing organs, tissues, or body sites.

* Mapping to FHIR Specimen: In FHIR, the Specimen resource includes fields like specimen type, collection details, container, and possibly body site information.

* Matching Concepts: The SNOMED CT code representing the body part or anatomical site needs to be correlated with the relevant field(s) in the FHIR Specimen resource. For instance, the FHIR Specimen resource has a field called "collection.bodySite" that can be used to capture the anatomical location from which the specimen was obtained.

## Identifiers

[Identifiers in FHIR](https://hl7.org/fhir/datatypes.html#Identifier) are strings (typically numeric or alphanumeric) that uniquely identify an object or entity within a system. They are essential for connecting resources within FHIR to external systems and maintaining data integrity across platforms.

Identifiers have two key components:

* **System**: The namespace or system to which the identifier belongs. The default namespace is `http://calypr-public.ohsu.edu/<project-id>`. This ensures your identifiers don't conflict with identifiers from other systems.
* **Value**: The actual identifier string (e.g., a subject ID like "SUBJ-001" or a specimen ID like "SPEC-12345").

**Example**: A patient identifier might be represented as:
- System: `http://calypr-public.ohsu.edu/study-123`
- Value: `PAT-00542`



## References

By using [identifiers in references](https://hl7.org/fhir/references.html), FHIR ensures that data can be accurately linked, retrieved, and interpreted across different systems and contexts within the healthcare domain, promoting interoperability and consistency in data exchange.

> Many of the defined elements in a resource are references to other resources. Using these references, the resources combine to build a web of information about healthcare.


## Key resources

### ResearchStudy
A [scientific study](https://hl7.org/fhir/researchstudy.html) of nature that sometimes includes processes involved in health and disease.

### ResearchSubject
A [ResearchSubject](https://hl7.org/fhir/researchsubject.html) is a participant or object which is the recipient of investigative activities in a research study.


### Patient 
A [Patient](https://hl7.org/fhir/patient.html) connects to Demographics and other administrative information about an individual or animal receiving care or other health-related services.

### Specimen

A [Specimen](https://hl7.org/fhir/specimen.html) represents a sample collected during a healthcare event and used for analysis or testing. It includes information about the sample type, collection method, and processing.

### DocumentReference
A [DocumentReference](https://hl7.org/fhir/documentreference.html) is a reference to a document of any kind for any purpose.


## Next steps

With your data integrated into FHIR format, you can now manage and enhance your metadata. See the [data management section](managing-metadata.md) for detailed guidance on creating, updating, and maintaining your metadata.

For more information on ontologies and how SNOMED CT codes enhance your data, see the [Ontologies](#ontologies) section above.
