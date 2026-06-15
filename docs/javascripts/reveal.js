// Keep header nav active state in sync with instant navigation
if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    const path = window.location.pathname;
    document.querySelectorAll(".md-header__nav-item").forEach((item) => {
      const link = item.querySelector(".md-header__nav-link");
      if (!link) return;
      const href = new URL(link.href, location.origin).pathname;
      const active = href !== "/" && path.startsWith(href);
      item.classList.toggle("md-header__nav-item--active", active);
    });
  });
}

(() => {
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      }
    },
    { threshold: 0, rootMargin: "0px 0px -40px 0px" }
  );

  const observe = () => {
    document.querySelectorAll("[data-reveal]").forEach((el) => {
      const rect = el.getBoundingClientRect();
      const alreadyVisible = rect.top < window.innerHeight && rect.bottom > 0;
      if (alreadyVisible) {
        el.classList.add("is-visible");
      } else {
        observer.observe(el);
      }
    });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", observe);
  } else {
    observe();
  }
})();
