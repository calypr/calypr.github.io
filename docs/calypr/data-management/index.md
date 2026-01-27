
# CALYPR Data Management

CALYPR uses Fast Healthcare Interoperability Resources (FHIR) as a standardized data model to enable seamless integration and analysis of healthcare and experimental data. This guide introduces the data management workflow for research analysts and describes how to work with FHIR resources using CALYPR's tool suite.

## CALYPR Tool Ecosystem

CALYPR provides a comprehensive suite of tools for data management:

- **git-drs**: Git-based data management system that extends Git LFS with scalable, standards-based data access
- **grip**: Graph Resource Integration Platform for querying and analyzing FHIR data
- **funnel**: Workflow execution engine for distributed computing
- **sifter**: Data transformation and processing framework

## Data Management Workflow

The typical data management workflow follows these stages:

1. **File Management**: Use `git-drs` to add, version, and track large data files
2. **Metadata Creation**: Generate FHIR-compliant metadata for your files
3. **Validation**: Validate metadata and ensure compliance with FHIR standards
4. **Query & Analysis**: Use `grip` to query and analyze your integrated data
5. **Customization**: Configure explorer views and custom data presentations

## FHIR Data Model Overview

FHIR resources in CALYPR form a graph-like structure that captures complex relationships:

### Core Resource Types

- **ResearchStudy**: Defines the research project or study
- **ResearchSubject**: Links participants to studies
- **Patient**: Demographics and administrative information
- **Specimen**: Biological samples and their processing information
- **DocumentReference**: Links to actual data files (genomic data, images, etc.)
- **Observation**: Measurements, lab results, and clinical findings
- **Task**: Provenance information about data creation processes

### Resource Relationships

FHIR resources are interconnected through references, creating a rich graph that captures:

- Files linked to patients and specimens
- Measurements connected to specific samples
- Provenance tracking through task relationships
- Study-level organization of all resources

### Example Workflow

When you add a genomic sequencing file using `git-drs`:

```bash
git-drs add sample.cram --patient P001 --specimen P001-BM --task P001-SEQ
```

This creates relationships where:
- `sample.cram` (DocumentReference) points to Patient P001
- The file is associated with Specimen P001-BM  
- Task P001-SEQ provides provenance about how the file was created

## Getting Started

To begin working with CALYPR data management:

1. **Install tools**: See [git-drs installation](../../tools/git-drs/installation.md)
2. **Initialize your project**: [Getting started guide](../../tools/git-drs/getting-started.md)
3. **Add files and metadata**: [Managing metadata](managing-metadata.md)
4. **Query your data**: [Data querying](analysis/query.md)

<img src="/images/fhir-graph-model.png" width="100%">

---
*Last reviewed: January 2026*

