document$.subscribe(() => {
  const primaryNav = document.querySelector(".md-sidebar .md-nav--primary");
  if (!primaryNav) return;

  const activeBranch = primaryNav.querySelector(
    ".md-nav__item--active > .md-nav > .md-nav__list"
  );
  if (!activeBranch) return;

  activeBranch
    .querySelectorAll(":scope > .md-nav__item--nested > input.md-nav__toggle")
    .forEach((toggle) => {
      toggle.checked = true;
    });
});
