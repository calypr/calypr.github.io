---
template: home.html
hide:
  - navigation
  - toc
  - header
---

<!-- Hides the title -->
<style>
  .md-content h1 {
    display: none;
  }
</style>

<div style="text-align: center; margin: 4rem auto; max-width: 800px;">
  <h1 style="font-size: 2.5rem; font-weight: 700; margin-bottom: 1rem;">CALYPR Platform</h1>
  <p style="font-size: 1.2rem; line-height: 1.6; color: var(--md-default-fg-color--light); text-align: justify;">
    A scalable, hybrid cloud infrastructure designed for the demands of modern genomics research. 
    Built on open-source standards, CALYPR provides GA4GH-compliant tools for seamless data integration, analysis, and biological insights. Based on the <a style="color: var(--md-primary-fg-color);" href="https://gen3.org">Gen3</a> Data Commons architecture, CALYPR empowers analysts to manage large-scale genomic datasets and integrate data to build new predictive models.
  </p>
  <div style="margin-top: 2rem;">
    <a href="/calypr/quick-start/" class="md-button md-button--primary" style="font-size: 1.1rem; padding: 0.8rem 2rem; border-radius: 8px;">🚀 Get Started Quickly</a>
  </div>
</div>

<hr style="border: none; border-top: 3px solid var(--md-default-fg-color--lightest); width: 100px; margin: 4rem auto;">


<div style="text-align: center; margin: 3rem auto 5rem; max-width: 800px;">
  <p style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1rem; color: var(--md-default-fg-color--light); margin-bottom: 2rem;">Built on Open Standards</p>
  <div style="display: flex; justify-content: center; gap: 4rem; flex-wrap: wrap;">
    <div style="display: flex; flex-direction: column; align-items: center;">
      <div style="font-weight: 700; font-size: 1.25rem; color: var(--md-primary-fg-color);">TES</div>
      <div style="font-size: 0.5rem; color: var(--md-default-fg-color--light);">Task Execution Service. A GA4GH standard for distributed task execution to enable federated computing.</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <div style="font-weight: 700; font-size: 1.25rem; color: var(--md-primary-fg-color);">DRS</div>
      <div style="font-size: 0.5rem; color: var(--md-default-fg-color--light);">Data Reference System. A GA4GH standard for data discovery and access.</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <div style="font-weight: 700; font-size: 1.25rem; color: var(--md-primary-fg-color);">FHIR</div>
      <div style="font-size: 0.5rem; color: var(--md-default-fg-color--light);">Healthcare Interoperability. Exchanging patient health information.</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <div style="font-weight: 700; font-size: 1.25rem; color: var(--md-primary-fg-color);">JSON Hyper-Schema</div>
      <div style="font-size: 0.5rem; color: var(--md-default-fg-color--light);">JSON-Schema + Graph data. Represent complex and high quality data.</div>
    </div>
  </div>
  
</div>

<hr style="border: none; border-top: 3px solid var(--md-default-fg-color--lightest); width: 100px; margin: 4rem auto;">

<div class="product-grid">
  <!-- CALYPR -->
  <div class="product-card product-card--featured">
    <div class="product-card__image-wrap">
      <img src="assets/calypr_family.png" alt="CALYPR" class="product-card__image" />
    </div>
    <div class="product-card__content">
      <p class="product-card__summary">Scalable genomics data science platform for biological insights.</p>
      <p class="product-card__description">Next-generation genomics data science platform with scalable cloud / on-prem hybrid infrastructure, streamlining the journey from raw data to discovery.</p>
      <a href="calypr/" class="product-card__link">Learn more <i>→</i></a>
    </div>
  </div>

  <!-- GRIP -->
  <div class="product-card">
    <div class="product-card__image-wrap">
      <img src="assets/grip.png" alt="GRIP" class="product-card__image" />
    </div>
    <div class="product-card__content">
      <h2 class="product-card__title">GRIP</h2>
      <p class="product-card__summary">Graph-based data integration for complex research datasets.</p>
      <p class="product-card__description">High-performance graph query engine that provides a unified interface across MongoDB, SQL, and key-value stores. Ideal for complex relational discovery in genomics.</p>
      <a href="tools/grip/" class="product-card__link">Learn more <i>→</i></a>
    </div>
  </div>

  <!-- Funnel -->
  <div class="product-card">
    <div class="product-card__image-wrap">
      <img src="assets/funnel.png" alt="Funnel" class="product-card__image" />
    </div>
    <div class="product-card__content">
      <h2 class="product-card__title">Funnel</h2>
      <p class="product-card__summary">Distributed task execution for petabyte-scale pipelines.</p>
      <p class="product-card__description">Standardized batch computing using the GA4GH TES API. Run Docker-based tasks seamlessly across AWS, Google Cloud, and Kubernetes at any scale.</p>
      <a href="tools/funnel/" class="product-card__link">Learn more <i>→</i></a>
    </div>
  </div>

  <!-- Git-DRS -->
  <div class="product-card">
    <div class="product-card__image-wrap">
      <img src="assets/git-drs.png" alt="Git-DRS" class="product-card__image" />
    </div>
    <div class="product-card__content">
      <h2 class="product-card__title">Git-DRS</h2>
      <p class="product-card__summary">Secure data repository system with version control.</p>
      <p class="product-card__description">Manage large-scale genomic data with integrated versioning and metadata management, ensuring reproducibility and data integrity throughout research cycles.</p>
      <a href="tools/git-drs/" class="product-card__link">Learn more <i>→</i></a>
    </div>
  </div>
</div>

<hr style="border: none; border-top: 1px solid var(--md-default-fg-color--lightest); width: 100px; margin: 4rem auto;">

<div style="text-align: center; margin: 4rem auto; max-width: 600px;">
  <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">Join the Beta</h2>
  <p style="font-size: 1.1rem; color: var(--md-default-fg-color--light); text-align: justify; ">
    CALYPR is currently in <strong>private beta</strong>. If you are interested in early access or a demonstration of the platform, please reach out to us at 
    <a style="color: var(--md-primary-fg-color);" href="mailto:sales@calypr.com">sales@calypr.com</a>. In the meantime, you can explore our <a style="color: var(--md-primary-fg-color);" href="https://github.com/calypr">GitHub repository</a> and get access to all of our open source tools.
  </p>
</div>
