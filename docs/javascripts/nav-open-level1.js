document$.subscribe(() => {
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
});
