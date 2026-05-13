# Developing CALYPR Docs

This repo now uses a Zensical-only build pipeline. MkDocs, `.nav.yml`, and the old multirepo plugin are gone.

The main thing to understand is that the published site is built from a generated docs tree, not directly from `docs/`.

## Mental Model

- `docs/` contains repo-authored source content.
- `.generated/docs/` is the staged build input that Zensical actually reads.
- `site/` is the rendered output from `zensical build`.
- `zensical.toml` is the only navigation source of truth.

The build pipeline is:

1. Copy repo-authored docs from `docs/` into `.generated/docs/`
2. Import selected upstream docs from `git-drs` and `syfon`
3. Apply a few link rewrites needed for imported pages
4. Add generated assets like `termynal.css` and `termynal.js`
5. Run Zensical against `.generated/docs`

## Core Commands

From the repo root:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
make serve
```

Useful commands:

- `make prepare`: rebuild `.generated/docs`
- `make build`: run a clean Zensical build
- `make serve`: prepare docs and start the local server
- `make update-branches`: update GitHub source links in authored docs to the preferred upstream branches

If you want the raw commands:

```bash
python scripts/prepare_docs.py
zensical build --clean
zensical serve
```

## Where Navigation Lives

Navigation is fully defined in [zensical.toml](./zensical.toml).

If you want to:

- rename a sidebar label
- move a section
- add a new page to the nav
- change the Tools grouping

edit the `nav = [...]` structure in `zensical.toml`.

There are no `.nav.yml` files anymore. If you add a page under `docs/` and do not add it to `zensical.toml`, it will not appear in the intended nav structure.

## Source of Truth Rules

### Repo-authored pages

These live in `docs/` and should be edited directly there.

Examples:

- `docs/index.md`
- `docs/calypr/...`
- `docs/tools/index.md`
- `docs/tools/funnel/...`
- `docs/tools/grip/...`

### Imported tool pages

These are not authored in this repo anymore.

Current imported repos:

- `git-drs`
- `syfon`

Their imported file mappings live in [scripts/prepare_docs.py](./scripts/prepare_docs.py) under `REPO_IMPORTS`.

If you need to:

- add a new imported page
- stop importing a page
- change where an imported page lands under `tools/...`

update `REPO_IMPORTS` and usually also update `zensical.toml`.

Do not hand-edit imported pages under `.generated/docs`. They are build artifacts and will be replaced on the next `make prepare`.

## How Upstream Imports Work

The importer prefers local sibling repos by default:

- `../git-drs`
- `../syfon`

So on a typical local machine, the imported content comes from whatever is currently checked out in those repos.

If local sibling repos are unavailable, the importer falls back to GitHub and picks the first available branch from [scripts/branch_config.json](./scripts/branch_config.json).

Current branch preference order:

- `development`
- `develop`
- `main`
- `master`

The last import decision is written to `.generated/imports.json`.

Environment overrides:

- `CALYPR_IMPORT_PREFER_LOCAL=0`: force remote import mode
- `CALYPR_IMPORT_GIT_DRS_DIR=/path/to/git-drs`: override local `git-drs` source
- `CALYPR_IMPORT_SYFON_DIR=/path/to/syfon`: override local `syfon` source

## When You Add or Change Pages

### Adding a repo-authored page

1. Create the file under `docs/`
2. Add it to `zensical.toml`
3. Run `make serve` or `make build`

### Adding an imported tool page

1. Add the file mapping in `scripts/prepare_docs.py`
2. Add the page to `zensical.toml`
3. If the imported markdown links break after relocation, add a targeted rewrite in `MARKDOWN_REWRITES`
4. Run `make prepare`
5. Run `make build`

## Styling and Overrides

Site-level assets still come from the repo:

- custom CSS: `docs/stylesheets/extra.css`
- custom JS: `docs/javascripts/nav-open-level1.js`
- theme overrides: `overrides/`

Those are copied into `.generated/docs` during preparation and then used by Zensical.

## Deployment Behavior

Deployment uses the same pipeline as local builds:

- GitHub Pages runs `python scripts/prepare_docs.py` and then `zensical build --clean`
- Netlify does the same

That means deployment now depends on the import step succeeding. In CI, the importer will usually use remote GitHub repos rather than local sibling repos.

## Files You Should Usually Ignore

- `.generated/`
- `site/`
- `.cache/`

These are build/runtime artifacts.

## Known Caveat

Zensical currently reports some warnings from imported and legacy docs content, especially around bracketed literals like:

- `[SIGNED]`
- `[0]`
- `[]string`
- `map[string]string`

Those are content/rendering warnings, not a sign that the Zensical migration is broken.
