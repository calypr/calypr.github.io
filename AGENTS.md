---
lead: "This is a Zensical-based documentation site for calypr.org."
personas:
  - data-steward
  - platform-engineer
  - workflow-engineer
solutions:
  - manage-data
  - manage-compute
related_tools:
  - git-drs
  - syfon
  - funnel
  - data-client
---

# AGENTS.md — CALYPR Docs

This is a Zensical-based documentation site for [calypr.org](https://calypr.org). The published site merges repo-authored docs with pages imported from upstream tool repos.

## Architecture: Two-Stage Build

**Never edit `.generated/` directly — it is a build artifact.**

```
docs/              ← repo-authored source (edit here)
scripts/prepare_docs.py
        ↓
.generated/docs/   ← staged build input (Zensical reads this)
        ↓
zensical build
        ↓
site/              ← rendered output (build artifact)
```

- `docs/` is the only source of truth for repo-authored pages.
- `git-drs` and `syfon` tool docs are imported from sibling repos (or GitHub fallback) into `.generated/docs/tools/`.
- Import mappings live in `REPO_IMPORTS` inside `scripts/prepare_docs.py`.
- `zensical.toml` is the **only** navigation source of truth — no `.nav.yml` files exist. An unregistered page will not appear in the nav.

## Developer Workflows

```bash
# First-time setup
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # installs: zensical, termynal

# Local development loop
make serve          # prepare .generated/docs + start live server
make build          # prepare + one-shot build
make prepare        # rebuild .generated/docs only

# Maintenance
make update-front-matter   # infer/update lead/personas/solutions/related_tools front matter
make update-branches       # rewrite GitHub links to preferred upstream branches
```

Raw equivalents: `python scripts/prepare_docs.py` then `zensical serve`.

## Front Matter Convention

Every markdown file carries YAML front matter:

```yaml
---
lead: "One-sentence description of this page."
personas:
  - data-steward
  - platform-engineer
solutions:
  - manage-data
related_tools:
  - git-drs
---
```

Run `python3 scripts/update_front_matter.py --check` in CI to verify front matter is up to date (exits non-zero if changes are needed). It is deterministic and idempotent.

## Navigation Changes

All nav edits go in `zensical.toml` under the `nav = [...]` array. Audience-based structure:
- `Solutions` / `Products` → business-facing front
- `Developers` → technical back; contains CALYPR Product Docs + Open Source Tool Docs

## Adding Pages

**Repo-authored page:** create under `docs/`, add entry to `zensical.toml`, run `make serve`.

**Imported tool page:** add a `(source, dest)` tuple to `REPO_IMPORTS` in `scripts/prepare_docs.py`, register in `zensical.toml`, add link rewrites to `MARKDOWN_REWRITES` if needed, then run `make prepare && make build`.

## Upstream Import Behavior

By default the importer prefers local sibling repos (`../git-drs`, `../syfon`). Override with env vars:

```bash
CALYPR_IMPORT_PREFER_LOCAL=0                    # force remote fetch
CALYPR_IMPORT_GIT_DRS_DIR=~/my-git-drs          # override local path
CALYPR_IMPORT_SYFON_DIR=~/my-syfon
```

Branch preference order (from `scripts/branch_config.json`): `development → develop → main → master`.
Last import decision is recorded in `.generated/imports.json`.

## Key Files

| File | Purpose |
|------|---------|
| `zensical.toml` | Site config, **all navigation** |
| `scripts/prepare_docs.py` | Stage docs + import tool repos (`REPO_IMPORTS`, `MARKDOWN_REWRITES`) |
| `scripts/update_front_matter.py` | Infer/write front matter fields |
| `scripts/update_doc_links.py` | Rewrite GitHub branch links |
| `scripts/branch_config.json` | Branch preference order per repo |
| `docs/stylesheets/extra.css` | Custom CSS |
| `overrides/` | Zensical theme overrides |

## Ignore These Directories

`.generated/`, `site/`, `.cache/` — all build/runtime artifacts.

## Known Warnings

Zensical emits content warnings for bracketed literals from imported docs (`[SIGNED]`, `[]string`, `map[string]string`). These are benign rendering warnings, not build errors.

## Deployment

CI (GitHub Actions + Netlify) runs `python scripts/prepare_docs.py && zensical build --clean`. The import step must succeed — in CI, remote GitHub repos are used since local siblings are absent. Add `[skip ci]` to a commit message to skip the GitHub Actions build.

