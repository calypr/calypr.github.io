# Creating and Uploading Metadata

### Create Metadata

The recommended approach is to use git-drs to generate metadata automatically:

```bash
# Add files with metadata associations
git-drs add *.cram --patient P001 --specimen P001-BM

# Generate FHIR metadata
git-drs meta init
```

This creates metadata files in the `META/` directory:
- `ResearchStudy.ndjson` - Project description
- `DocumentReference.ndjson` - File information
- Additional resources based on specified flags (Patient, Specimen, etc.)

### Retrieve Existing Metadata

Retrieve metadata from existing projects:

```bash
# Export current metadata from the graph
grip dump <graph-name> --vertex > vertices.txt
grip dump <graph-name> --edge > edges.txt

# Or export specific resource types
grip query <graph-name> 'V().hasLabel("DocumentReference")'
```

### Integrate Your Data

For custom data integration workflows:

1. **Convert tabular data to FHIR format**
2. **Validate the FHIR resources**
3. **Load into the graph database**

```bash
# Validate FHIR metadata
git-drs meta validate META/

# Check reference integrity
git-drs meta check-edge META/
```

### Alternative: Direct Graph Loading

For advanced users who prefer working directly with the graph database:

```bash
# Load vertices and edges directly
grip load <graph-name> --vertex vertices.txt --edge edges.txt

# Validate graph integrity
grip info <graph-name>
```

### Publishing Data

Make your data visible in the CALYPR platform:

```bash
# Commit and push to register metadata
git-drs commit -m "Add project metadata"
git-drs push
```

## View the Files

This final step uploads the metadata and makes the files visible on the [CALYPR Explorer page](https://calypr.ohsu.edu/explorer).

<a href="https://calypr.ohsu.edu/explorer">![CALYPR File Explorer](../../portal/explorer.png)</a>

---
*Last reviewed: January 2026*
