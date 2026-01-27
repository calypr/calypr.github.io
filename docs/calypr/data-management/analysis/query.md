
# Data Querying with GRIP

GRIP provides powerful querying capabilities for FHIR data stored in the CALYPR graph database. This guide covers how to query and analyze your integrated data.

## Overview ⚙️

GRIP supports API access to FHIR data, allowing users to download and query their data via the GRIP CLI and GRIPQL queries.

## Quick Start ⚡️

*Adapted from the [Gen3 SDK Quick Start page](https://github.com/uc-cdis/gen3sdk-python/blob/master/docs/tutorial/quickStart.md)*

## 1. Dependency and Credentials 

Prior to using GRIP, ensure you have proper authentication:

```bash
# Test connection to GRIP server
grip list
```

This will return a list of available graphs you have access to.

For new setup or credential refresh:
- Download API credentials from the [CALYPR Profile page](https://calypr.ohsu.edu/identity)
- Configure credentials according to GRIP documentation

![CALYPR Profile page](../../../images/api-key.png)
![GRIP Credentials](../../../images/credentials.png)

## 2. Install

GRIP is available for installation via package managers:

```bash
# Install via pip (if available)
pip install grip

# Or download binary from releases
# See GRIP documentation for installation instructions
```

## 3. Query

The following query examples provide a high-level overview on how to use GRIP to authenticate, fetch graph schema, retrieve entity information, and make complex queries. Each project would have a graph schema defined during data transformation and loading. The queries depend on your project's specific graph structure.

### 3.0 List Available Graphs

```bash
# List all graphs you have access to
grip list

# Get information about a specific graph
grip info <graph-name>
```

### 3.1 Basic GRIPQL Queries

GRIP uses GRIPQL (Gremlin-inspired query language) for graph traversals:

```bash
# Get all vertices with a specific label
grip query <graph-name> 'V().hasLabel("Patient")'

# Get vertices with specific properties
grip query <graph-name> 'V().hasLabel("Specimen").has("specimen_type","Primary Tumor")'

# Traverse relationships
grip query <graph-name> 'V().hasLabel("Patient").out("hasSpecimen")'
```
### 3.2 Get Graph Schema

```bash
# Get schema for entire graph
grip schema get <graph-name>

# Get schema for specific vertex types
grip schema get <graph-name> --label Patient
```

### 3.3 Example Query Patterns

#### Find Patients with Specific Conditions

```bash
grip query <graph-name> '
V().hasLabel("ResearchSubject")
  .has("condition_diagnosis","Infiltrating duct carcinoma, NOS")
  .out("hasPatient")
'
```

#### Find Specimens for Patients of Interest

```bash
# First get patient IDs of interest
grip query <graph-name> '
V().hasLabel("ResearchSubject")
  .has("condition_diagnosis","Infiltrating duct carcinoma, NOS")
  .out("hasPatient")
  .id()
' > patient_ids.txt

# Then find associated specimens
grip query <graph-name> '
V().hasLabel("Patient")
  .has("patient_id",IN("P001","P002","P003"))
  .out("hasSpecimen")
'
```

#### Find Files for Specific Specimens

```bash
grip query <graph-name> '
V().hasLabel("Specimen")
  .has("specimen_type","Primary Tumor")
  .out("hasDocumentReference")
  .has("content.attachment.url",CONTAINING(".cram"))
'
```

## Simple End-to-End Workflow

### Basic Data Exploration

```bash
# Get vertex and edge counts
grip info <graph-name>

# List all vertex types
grip query <graph-name> 'V().label().dedup()'

# Get sample data for each type
grip query <graph-name> 'V().hasLabel("Patient").limit(5)'
grip query <graph-name> 'V().hasLabel("DocumentReference").limit(5)'
grip query <graph-name> 'V().hasLabel("Specimen").limit(5)'
```

### Export Data for Analysis

```bash
# Export all vertices to file
grip dump <graph-name> --vertex > all_vertices.txt

# Export specific vertex types
grip query <graph-name> 'V().hasLabel("DocumentReference")' > documents.txt

# Export relationship data
grip dump <graph-name> --edge > all_edges.txt
```

## Additional Resources 📚

- [GRIP Documentation](../../tools/grip/index.md)
- [GRIP Query Guide](../../tools/grip/docs/commands/query.md)
- [GRIP Schema Documentation](../../tools/grip/docs/graphql/graph_schemas.md)
- [GRIP Commands Reference](../../tools/grip/docs/commands.md)

---
*Last reviewed: January 2026*
