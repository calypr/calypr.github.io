# Governed Data Access

Biomedical research data needs to be findable and usable, but it also needs to remain controlled. CALYPR treats data governance as part of the product experience rather than an afterthought bolted onto storage.

## What This Means

- Projects provide the boundary for collaboration.
- Metadata gives data stewards and analysts enough context to understand what a dataset represents.
- Access workflows keep users, approvals, and project permissions visible.
- DRS-native references avoid exposing raw storage implementation details as the primary user interface.

## Why It Matters

Without a platform layer, teams usually fall back to spreadsheets, bucket paths, manual approvals, and tribal knowledge. That works for a pilot. It does not scale across programs, institutions, or regulated data.

CALYPR keeps the technical machinery available, but puts a governed product surface in front of it.

## Related Technical Docs

- [Managing metadata](../calypr/data/managing-metadata.md)
- [Role based access control](../calypr/project-management/calypr-admin/approve-requests.md)
- [Syfon storage service](../tools/syfon/index.md)
- [Git-DRS data versioning](../tools/git-drs/index.md)
