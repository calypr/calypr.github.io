---
template: home.html
body_class: home business-home
hide:
  - navigation
  - toc
lead: "CALYPR is a research data management platform for translational teams."
personas:
  - data-steward
  - platform-engineer
  - workflow-engineer
  - researcher-bioinformatician
  - security-compliance-reviewer
  - standards-architecture-lead
solutions:
  - manage-data
  - manage-compute
  - integrate-data
  - manage-models
related_tools:
  - git-drs
  - syfon
  - funnel
  - forge
  - grip
  - sifter
  - data-client
---

<section class="business-hero" aria-label="CALYPR homepage hero">
  <div class="business-hero__copy">
    <p class="eyebrow">For translational researchers</p>
    <h1>Explore data, manage projects, and run reproducible workflows in one platform.</h1>
    <p class="business-hero__lead">
      CALYPR helps translational teams move from study intake to analysis output with governed data access, project-level controls, and execution history you can audit.
    </p>
    <div class="business-actions">
      <a href="products/" class="md-button md-button--primary">Explore products</a>
      <a href="developers/" class="md-button">See technical docs</a>
      <a href="solutions/" class="md-button">Match a use case</a>
    </div>
  </div>
  <div class="business-hero__panel" aria-label="CALYPR product interface preview">
    <img src="images/main-page.png" alt="CALYPR workspace showing project and data operations" loading="eager">
  </div>
</section>

<section class="solution-section" aria-label="Product workflow examples">
  <p class="eyebrow">Task walkthroughs</p>
  <h2>Common research tasks, demonstrated with synthetic projects.</h2>
  <div class="solution-strip solution-strip--page">
    <article class="usecase-panel">
      <h3>1) Explore and organize research data</h3>
      <p class="usecase-panel__meta">TRX-101 Lung Response Cohort</p>
      <p>Browse study files and metadata, then filter assets by cohort and assay type before analysis kickoff.</p>
      <img src="images/main-page.png" alt="Research project view for data exploration and project management" loading="lazy">
    </article>
    <article class="usecase-panel">
      <h3>2) Manage project collaborators and access</h3>
      <p class="usecase-panel__meta">TRX-204 AML Multi-site Registry</p>
      <p>Review project member context and enforce role-based access before exposing new datasets to partner labs.</p>
      <img src="images/profile.png" alt="Project profile and member management view" loading="lazy">
    </article>
    <article class="usecase-panel">
      <h3>3) Integrate new data drops</h3>
      <p class="usecase-panel__meta">TRX-318 Immunotherapy Biomarker Study</p>
      <p>Upload files from collaborating sites and register each drop with provenance and project metadata.</p>
      <img src="images/file-upload.png" alt="File upload workflow for governed data integration" loading="lazy">
    </article>
    <article class="usecase-panel">
      <h3>4) Execute workflows and retrieve outputs</h3>
      <p class="usecase-panel__meta">TRX-101 Lung Response Cohort</p>
      <p>Run a reproducible workflow, monitor status, and download artifacts for reporting and downstream modeling.</p>
      <img src="images/download.png" alt="Workflow output download view for execution results" loading="lazy">
    </article>
  </div>
</section>

<section class="solution-section" aria-label="Synthetic project catalog">
  <p class="eyebrow">Project catalog</p>
  <h2>These synthetic projects back the workflows above.</h2>
  <div class="usecase-grid">
    <article class="usecase-panel">
      <h3>TRX-101 Lung Response Cohort</h3>
      <p>Tracks longitudinal response across NSCLC participants with linked pathology files, omics outputs, and analysis runs.</p>
      <div class="usecase-panel__links">
        <a href="products/manage-data/">Data exploration workflow</a>
        <a href="products/manage-compute/">Workflow execution workflow</a>
      </div>
    </article>
    <article class="usecase-panel">
      <h3>TRX-204 AML Multi-site Registry</h3>
      <p>Demonstrates project governance with institution-specific access, collaborator onboarding, and cross-site portfolio tracking.</p>
      <div class="usecase-panel__links">
        <a href="products/manage-data/">Project management workflow</a>
        <a href="developers/">Technical implementation details</a>
      </div>
    </article>
    <article class="usecase-panel">
      <h3>TRX-318 Immunotherapy Biomarker Study</h3>
      <p>Shows governed file intake and metadata integration from collaborating wet-lab and clinical data partners.</p>
      <div class="usecase-panel__links">
        <a href="products/integrate-data/">Data integration workflow</a>
        <a href="products/manage-data/">Governed data operations</a>
      </div>
    </article>
  </div>
</section>

<section class="home-footer" aria-label="Time-to-Decision Toolkit">
  <div class="home-footer__inner">
    <p class="eyebrow">What you need before deciding</p>
    <h2>Complete a lightweight self-assessment in 20 minutes.</h2>
    <div class="home-footer__grid">
      <div class="home-footer__item">
        <h3>Governance readiness check</h3>
        <p>Clarifies your policy gaps and ensures CALYPR can support your compliance requirements without slowing researcher workflows.</p>
      </div>
      <div class="home-footer__item">
        <h3>Workflow portability audit</h3>
        <p>Tests your code environment and identifies how easily your existing scripts and workflows can execute on CALYPR infrastructure.</p>
      </div>
      <div class="home-footer__item">
        <h3>Data asset inventory template</h3>
        <p>Maps what you already manage and surfaces the immediate operational lift before your teams engage with implementation planning.</p>
      </div>
    </div>
    <div class="business-actions">
      <a href="#" class="md-button md-button--primary">Explore Tools</a>
      <a href="#" class="md-button">Examine sample datasets</a>
    </div>
  </div>
</section>
