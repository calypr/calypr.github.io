document$.subscribe(() => {
  const slugToLabel = (slug) =>
    slug
      .split("-")
      .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
      .join(" ");

  const normalizePath = (path) => {
    let value = path || "/";
    value = value.replace(/index\.html$/, "");
    if (!value.startsWith("/")) value = `/${value}`;
    if (!value.endsWith("/")) value = `${value}/`;
    return value;
  };

  const loadTaxonomyMap = async () => {
    if (!window.__calyprPageTaxonomyPromise) {
      const taxonomyUrl = `${__md_scope.pathname}javascripts/page-taxonomy.json`;
      window.__calyprPageTaxonomyPromise = fetch(taxonomyUrl)
        .then((response) => (response.ok ? response.json() : {}))
        .catch(() => ({}));
    }
    return window.__calyprPageTaxonomyPromise;
  };

  const upsertPageTaxonomyNav = async () => {
    const taxonomyMap = await loadTaxonomyMap();
    const route = normalizePath(window.location.pathname);
    const pageTaxonomy = taxonomyMap[route] || {};
    const personas = Array.isArray(pageTaxonomy.personas)
      ? pageTaxonomy.personas.filter(Boolean)
      : [];
    const solutions = Array.isArray(pageTaxonomy.solutions)
      ? pageTaxonomy.solutions.filter(Boolean)
      : [];
    const relatedTools = Array.isArray(pageTaxonomy.related_tools)
      ? pageTaxonomy.related_tools.filter(Boolean)
      : [];

    document
      .querySelectorAll(".calypr-page-taxonomy-nav")
      .forEach((node) => node.remove());
    if (!personas.length && !solutions.length && !relatedTools.length) return;

    const secondaryNav = document.querySelector(".md-sidebar--secondary .md-nav");
    const secondaryList = secondaryNav?.querySelector(".md-nav__list");
    const primaryList = document.querySelector(".md-sidebar--primary .md-nav__list");
    const navList = secondaryList || primaryList;
    if (!navList) return;

    const appendGroup = (title, items, hrefBuilder) => {
      if (!items.length) return;

      const headingItem = document.createElement("li");
      headingItem.className =
        "md-nav__item calypr-page-taxonomy-nav calypr-page-taxonomy-nav--heading";

      const headingLabel = document.createElement("span");
      headingLabel.className = "md-nav__link";
      headingLabel.textContent = title;
      headingItem.appendChild(headingLabel);
      navList.appendChild(headingItem);

      items.forEach((slug) => {
        const item = document.createElement("li");
        item.className = "md-nav__item calypr-page-taxonomy-nav";

        const link = document.createElement("a");
        link.className = "md-nav__link";
        link.href = hrefBuilder(slug);
        link.textContent = slugToLabel(slug);

        item.appendChild(link);
        navList.appendChild(item);
      });
    };

     appendGroup("Solutions", solutions, (slug) => `/solutions/${slug}/`);
     appendGroup("Audience", personas, (slug) => `/personas/${slug}/`);
     appendGroup("Tools", relatedTools, (slug) => `/tools/${slug}/`);
  };

  const isDeveloperDocsRoute = [
    "/developers/",
    "/calypr/",
    "/tools/",
  ].some((prefix) => window.location.pathname.startsWith(prefix));

  document.body.classList.toggle("developer-docs-route", isDeveloperDocsRoute);

  const primaryNav = document.querySelector(".md-sidebar .md-nav--primary");
  if (!primaryNav) return;

  primaryNav
    .querySelectorAll(".md-nav__item--active > input.md-nav__toggle")
    .forEach((toggle) => {
      toggle.checked = true;
    });

  upsertPageTaxonomyNav();
});
