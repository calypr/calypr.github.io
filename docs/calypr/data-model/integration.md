
# Integrating your data

Converting tabular data (CSV, TSV, spreadsheet, database table) into FHIR (Fast Healthcare Interoperability Resources) involves several steps to map the data in the spreadsheet to FHIR's resource structure. Here is what you need to know to get started:

As you create a upload files, you can tag them with identifiers which by default will create minimal, skeleton graph.

You can retrieve that data using the g3t command line tool, and update the metadata to create a more complete graph representing your study.

You may choose to work with the data in it's "native" json format, or convert it to a tabular format for integration.  The system will re-convert tabular data back to json for submittal.

The process of integrating your data into the graph involves several steps:

* Step 1: Identify Data and FHIR Resources
    * Inventory tabular data: Review the spreadsheet to understand the types of data it contains (e.g., patient demographics, lab results, medications).
    * Understand FHIR Resources: Familiarize yourself with FHIR resources relevant to the data in your spreadsheet (e.g., Patient, Observation, Specimen, etc.).

* Step 2: Mapping Spreadsheet Columns to FHIR Fields
    * Analyze Columns: Map each column in the spreadsheet to corresponding fields in FHIR resources. For instance, you may have a field called biopsy_anatomical_location with content of "Prostate needle biopsies", that would map to Specimen.collection.method and Specimen.collection.bodySite.
    * Handle Relationships: Identify how different pieces of data relate to each other and how they map to FHIR resource relationships (e.g., linking patients to their observations).
 
* Step 3: Data Transformation and Structure
    * Prepare Data: Ensure data consistency and format alignment. Dates, codes, and identifiers should comply with FHIR standards.
    * Normalize Data: Split the spreadsheet data into FHIR-compliant resources.

* Step 4: Utilize provided FHIR Tooling or Libraries
    * FHIR Tooling: Use `g3t  meta dataframe ` and associated libraries to support data conversion and validation.
    * Validation: Use `g3t  meta validate` to validate the transformed data against FHIR specifications to ensure compliance and accuracy.

* Step 5: Import into FHIR-Compatible System
    * Load Data: Use `g3t commit` to load the transformed data into the calypr system.
    * Testing and Verification: Use `g3t push` to ensure your data appears correctly in the portal and analysis tools.

* Step 6: Iterate and Refine
    * Review and Refine: Check for any discrepancies or issues during the import process. Refine the conversion process as needed.
    * Feedback Loop: Gather feedback from users or stakeholders to improve the mapping and conversion process.


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

Identifiers in FHIR references typically include the following components: [see more](https://hl7.org/fhir/datatypes.html#Identifier)

> A string, typically numeric or alphanumeric, that is associated with a single object or entity within a given system. Typically, identifiers are used to connect content in resources to external content available in other frameworks or protocols.

System: Indicates the system or namespace to which the identifier belongs. By default the namespace is `http://calypr-public.ohsu.edu/<project-id>`.

Value: The actual value of the identifier within the specified system. For instance, a lab controlled subject identifier or a specimen identifier.



## References

By using identifiers in references, FHIR ensures that data can be accurately linked, retrieved, and interpreted across different systems and contexts within the healthcare domain, promoting interoperability and consistency in data exchange. [see more](https://hl7.org/fhir/references.html)

> Many of the defined elements in a resource are references to other resources. Using these references, the resources combine to build a web of information about healthcare.


## Key resources

### ResearchStudy
> A scientific study of nature that sometimes includes processes involved in health and disease. [see more](https://hl7.org/fhir/researchstudy.html)

### ResearchSubject
> A ResearchSubject is a participant or object which is the recipient of investigative activities in a research study. [see more](https://hl7.org/fhir/researchsubject.html)


### Patient 
> Demographics and other administrative information about an individual or animal receiving care or other health-related services. [see more](https://hl7.org/fhir/patient.html)

### Specimen

> A sample to be used for analysis. [see more](https://hl7.org/fhir/specimen.html)

### DocumentReference
> A reference to a document of any kind for any purpose. [see more](https://hl7.org/fhir/documentreference.html)


See the [data management section](../data-management/meta-data.md) for more information on how to create and upload metadata.
