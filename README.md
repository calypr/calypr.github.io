# CALYPR Docs

This Zensical-based codebase deploys documentation to [calypr.org](https://calypr.org).

<a href="https://calypr.org">![CALYPR Homepage](./docs/images/website_header.png)</a>

## Local Development

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
make serve
```

The local build contract is:

- `make prepare` stages repo-authored docs plus imported upstream tool docs into `.generated/docs`
- `make build` runs a clean Zensical build
- `make serve` stages the docs and starts the local Zensical server

If you prefer the raw commands:

```sh
python scripts/prepare_docs.py
zensical serve
```

## Publishing to [calypr.org](https://calypr.org)

The site is automatically built and published on every push to `main` using the GitHub Actions workflow in [publish.yml](.github/workflows/publish.yml). Netlify uses the same Zensical build pipeline.

To skip CI for a commit, add `[skip ci]` (or any [equivalent variation](https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs)) to the commit message.
