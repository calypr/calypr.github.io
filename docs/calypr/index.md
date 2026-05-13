# CALYPR Product Guide

CALYPR is the product layer of the CALYPR open platform. It turns the underlying data, compute, metadata, and access-control tools into a workspace experience that research programs can understand and operate.

!!! info "Private Beta"
    CALYPR is currently in private beta. The platform is being refined with research partners. The underlying [open-source tools](../tools/index.md) remain available for public use.

## What The Product Adds

<div class="capability-grid">
  <article>
    <h3>Project-centered collaboration</h3>
    <p>Research programs need a shared place to organize datasets, metadata, users, approvals, and analysis context.</p>
  </article>
  <article>
    <h3>Governed data operations</h3>
    <p>CALYPR keeps controlled data movement visible through access workflows and DRS-native object references.</p>
  </article>
  <article>
    <h3>Technical depth when needed</h3>
    <p>Engineers can drop into Git-DRS, Syfon, Funnel, GRIP, Forge, and the data client without making those tools the default front door for everyone.</p>
  </article>
</div>

## Platform Foundation

CALYPR is built on standards-aligned components:

- **Gen3-compatible commons patterns** for metadata, indexing, and authentication.
- **GA4GH DRS** for data references and access.
- **GA4GH TES** for portable workflow execution.
- **FHIR-oriented metadata** for connecting research files to biological and clinical context.
- **Open-source CALYPR tools** for versioning, storage mediation, metadata publishing, graph querying, and workflow execution.

## Next Steps

1. Start with the [quick start guide](quick-start.md) if you are setting up or trying the platform.
2. Review [data and metadata](data/managing-metadata.md) if you are preparing datasets.
3. Use the [developer docs](../developers/index.md) when you need command references, deployment details, or component-level documentation.
