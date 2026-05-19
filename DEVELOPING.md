# Developing CALYPR Docs

Zensical builds the site directly from `docs/`. Upstream tool docs (git-drs, syfon) are fetched from GitHub at build time via `mkdocs-multirepo-plugin`. Navigation is defined in `zensical.toml`.

## Setup

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
make serve
```

## Commands

```bash
make serve  # start local dev server
make build  # clean build to site/
```

## Navigation

All navigation is defined in `zensical.toml` under `nav = [...]`. A page not listed there will not appear in the sidebar.

## Adding pages

### Repo-authored page

```bash
# 1. create the file
vim docs/calypr/example.md

# 2. add it to nav in zensical.toml, then:
make serve
```

### Page from an imported repo (git-drs, syfon)

```bash
# 1. add and merge the file in the upstream repo (e.g. calypr/git-drs), then:

# 2. add the file path to the relevant imports list in zensical.toml:
#    [[plugins.multirepo.nav_repos]]
#    name = "git-drs"
#    imports = ["docs/my-new-page.md", ...]

# 3. add the page to nav in zensical.toml, then:
make serve  # plugin fetches it automatically
```

### New imported repo entirely

```bash
# 1. add a new block to zensical.toml:
#    [[plugins.multirepo.nav_repos]]
#    name = "my-tool"
#    import_url = "https://github.com/calypr/my-tool?branch=development"
#    imports = ["docs/index.md", ...]

# 2. add the pages to nav in zensical.toml, then:
make serve
```

## Styling and overrides

- Custom CSS: `docs/stylesheets/extra.css`
- Custom JS: `docs/javascripts/nav-open-level1.js`
- Theme overrides: `overrides/`

## Deployment

Netlify runs `zensical build --clean` directly. The multirepo plugin fetches upstream docs from GitHub during the build, so CI always gets the latest from the configured branches.

