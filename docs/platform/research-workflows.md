# Research Workflows

CALYPR connects data access, metadata, and workflow execution so research teams can move from question to reproducible result without rebuilding one-off infrastructure for every project.

## Workflow Goals

- Keep data references stable and auditable.
- Run compute through portable standards instead of environment-specific scripts.
- Let analysts work at the project level while platform teams retain control over deployment and operations.
- Preserve a path from product workflows into lower-level developer tooling.

## Where The Pieces Fit

- [Git-DRS](../tools/git-drs/index.md) handles large data versioning and DRS pointers.
- [Funnel](../tools/funnel/index.md) provides GA4GH TES workflow execution.
- [GRIP](../tools/grip/index.md) supports graph-based discovery over integrated datasets.
- [Forge](../tools/forge/index.md) validates and publishes structured metadata.

## Business Boundary

The platform pages explain what the workflow enables. The developer docs explain how to operate each component. Keeping those boundaries clear makes the site useful to both non-technical decision makers and engineers.
