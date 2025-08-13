
# FHIR for Researchers

Given all of the intricacies healthcare and experimental data, we use Fast Healthcare Interoperability Resources (FHIR) as a data model to ensure informaticians and analysts can concentrate on science, not data structures.  This document introduces model for Research Analysts and describes how an analyst can shape and query FHIR resources.

## What is FHIR?

In an era where healthcare information is abundant yet diverse and often siloed, FHIR emerges as a standard, empowering research analysts to navigate, aggregate, and interpret health data seamlessly. This guide aims to unravel the intricacies of FHIR, equipping research analysts with the knowledge and tools needed to harness the potential of interoperable healthcare data for insightful analysis and impactful research outcomes in the context of CALYPR collaborations.

## Graph Model

FHIR has certain aspects that can align with graph-like structures or facilitate graph-based analysis:

Resource Relationships: FHIR resources often have relationships with other resources. For instance, a Patient resource can be associated with multiple Observation resources, which in turn might be linked to Condition or Procedure resources. These relationships create a network-like structure, similar to a graph.

References and Linkages: FHIR resources utilize references to establish connections between related entities. These references can be leveraged to create graph-like representations when modeling relationships between patients, specimens, observations, etc.

### Example

The following "file focused" example illustrates how CALYPR uses FHIR resources a DocumentReference's ancestors within a study.

Examine [resource](https://www.hl7.org/fhir/resource.html) definitions [here](http://www.hl7.org/fhir/resource.html):

* Details on [uploaded files](https://calypr.ohsu.edu.github.io/workflows/upload/) are captured as [DocumentReference](http://www.hl7.org/fhir/documentreference.html)

* DocumentReference.[subject](https://www.hl7.org/fhir/documentreference-definitions.html#DocumentReference.subject) indicates who or what the document is about:  
  * Can simply point to the [ResearchStudy](https://hl7.org/fhir/researchstudy.html), to indicate the file is part of the study
  * Can point to [Patient](https://hl7.org/fhir/patient.html), or [Specimen](https://hl7.org/fhir/specimen.html), to indicate the file is based on them
* An [Observation](https://hl7.org/fhir/observation.html) can point to any entity    
* A [Task](https://hl7.org/fhir/task.html) can provide [provenance](https://en.wikipedia.org/wiki/Provenance#Data_provenance) on how the file was created 

Each resource has at least one study controlled [official](https://hl7.org/fhir/codesystem-identifier-use.html#identifier-use-official) [Identifier](https://hl7.org/fhir/datatypes.html#Identifier).  Child resources have [Reference](http://www.hl7.org/fhir/references.html) fields to point to their parent.


<img src="/images/fhir-graph-model.png" width="100%">

