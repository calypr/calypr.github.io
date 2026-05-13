---
body_class: marketing-page
hide:
  - navigation
  - toc
---

<section class="solution-hero">
  <div>
    <p class="eyebrow">Products</p>
    <h1>Products designed for how research programs actually operate.</h1>
    <p class="solution-hero__lead">
      CALYPR packages the underlying data, workflow, and metadata infrastructure into four products that buyers can evaluate and teams can adopt without first becoming experts in the implementation.
    </p>
    <div class="business-actions">
      <a href="#product-catalog" class="md-button md-button--primary">Browse products</a>
      <a href="../solutions/" class="md-button">See solutions</a>
    </div>
  </div>
  <div class="solution-hero__aside">
    <span>Product model</span>
    <strong>Four products. One governed research platform.</strong>
  </div>
</section>

<section id="product-catalog" class="product-banners product-banners--solutions">
  <article class="product-banner product-banner--data">
    <div class="product-banner__copy">
      <p class="eyebrow">Data product</p>
      <h2>Manage Data</h2>
      <p>Give teams governed access to large research datasets, durable data references, and controlled data movement.</p>
      <div class="product-banner__links">
        <a href="manage-data/">Product overview</a>
      </div>
    </div>
    <img src="../assets/solutions/manage-data.svg" alt="Manage Data product illustration" />
  </article>

  <article class="product-banner product-banner--compute">
    <div class="product-banner__copy">
      <p class="eyebrow">Compute product</p>
      <h2>Manage Compute</h2>
      <p>Run reproducible workflows across cloud, cluster, and local environments without rebuilding the way research teams work.</p>
      <div class="product-banner__links">
        <a href="manage-compute/">Product overview</a>
      </div>
    </div>
    <img src="../assets/solutions/manage-compute.svg" alt="Manage Compute product illustration" />
  </article>

  <article class="product-banner product-banner--integrate">
    <div class="product-banner__copy">
      <p class="eyebrow">Integration product</p>
      <h2>Integrate Data</h2>
      <p>Turn fragmented clinical, omics, and project metadata into structured context that teams can search, govern, and reuse.</p>
      <div class="product-banner__links">
        <a href="integrate-data/">Product overview</a>
      </div>
    </div>
    <img src="../assets/solutions/integrate-data.svg" alt="Integrate Data product illustration" />
  </article>

  <article class="product-banner product-banner--models">
    <div class="product-banner__copy">
      <p class="eyebrow">Model product</p>
      <h2>Manage Models</h2>
      <p>Carry governed data, workflow provenance, and benchmark context into model-driven research operations.</p>
      <div class="product-banner__links">
        <a href="manage-models/">Product overview</a>
      </div>
    </div>
    <img src="../assets/solutions/manage-models.svg" alt="Manage Models product illustration" />
  </article>
</section>

<section class="solution-section">
  <p class="eyebrow">Product foundations</p>
  <h2>Each product stands on standards and services your platform team can verify.</h2>
  <div class="value-grid">
    <article>
      <h3>Open standards</h3>
      <p>The platform already leans on GA4GH DRS for data access, GA4GH TES for task execution, and FHIR-oriented metadata structures for research entities and relationships.</p>
    </article>
    <article>
      <h3>Project operations</h3>
      <p>CALYPR adds project-centered collaboration, collaborator request handling, profile setup, and workflow structure around those lower-level services.</p>
    </article>
    <article>
      <h3>Operational product surface</h3>
      <p>Each product packages those standards into a clearer operating surface so teams can evaluate adoption in terms of workflows, governance, and delivery instead of raw components.</p>
    </article>
  </div>
</section>

<section class="solution-section">
  <p class="eyebrow">Product system</p>
  <h2>Each product handles a different layer of the research operating surface.</h2>
  <div class="product-system">
    <article class="product-system__card">
      <span>Govern</span>
      <h3>Manage Data</h3>
      <p>Owns object registration, versioning, access control boundaries, and controlled data movement.</p>
      <ul>
        <li>DRS-native object lifecycle</li>
        <li>Scoped remotes and durable references</li>
        <li>Presigned and multipart transfer paths</li>
      </ul>
    </article>
    <article class="product-system__card">
      <span>Execute</span>
      <h3>Manage Compute</h3>
      <p>Owns portable task execution and workflow operations across cloud, cluster, and local environments.</p>
      <ul>
        <li>TES-style execution model</li>
        <li>Portable workflow routing</li>
        <li>Run history tied to governed inputs</li>
      </ul>
    </article>
    <article class="product-system__card">
      <span>Connect</span>
      <h3>Integrate Data</h3>
      <p>Owns metadata mapping, validation, publication, and graph-oriented discovery.</p>
      <ul>
        <li>FHIR-shaped resource structures</li>
        <li>Validation and publication workflows</li>
        <li>Queryable graph relationships</li>
      </ul>
    </article>
    <article class="product-system__card">
      <span>Carry forward</span>
      <h3>Manage Models</h3>
      <p>Owns the model-facing lifecycle built on the same governed data and workflow foundation.</p>
      <ul>
        <li>Benchmark-aware model packaging</li>
        <li>Provenance linked to workflow history</li>
        <li>Model assets grounded in governed data</li>
      </ul>
    </article>
  </div>
</section>

<section class="solution-section product-dev-links">
  <p class="eyebrow">For technical teams</p>
  <h2>When evaluation turns into implementation, each product hands off to the tool docs behind it.</h2>
  <div class="product-dev-links__grid">
    <article class="product-dev-links__card">
      <strong>Manage Data</strong>
      <p>Start with Git-DRS and the versioned object-pointer workflow used to move governed research data.</p>
      <a href="../tools/git-drs/index.md">Git-DRS docs</a>
    </article>
    <article class="product-dev-links__card">
      <strong>Manage Compute</strong>
      <p>Go directly to Funnel and the TES-based execution layer used to run portable analysis.</p>
      <a href="../tools/funnel/index.md">Funnel docs</a>
    </article>
    <article class="product-dev-links__card">
      <strong>Integrate Data</strong>
      <p>Start with Forge and the validation and publication workflow used to shape reusable metadata context.</p>
      <a href="../tools/forge/index.md">Forge docs</a>
    </article>
    <article class="product-dev-links__card">
      <strong>Manage Models</strong>
      <p>Start with GRIP and the graph-oriented context used to compare research assets against the data and workflows that produced them.</p>
      <a href="../tools/grip/index.md">GRIP docs</a>
    </article>
  </div>
</section>
