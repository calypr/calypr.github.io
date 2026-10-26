# Developing CALYPR Docs

The site is built with Zensical from the content in `docs/`. Navigation is
configured in `zensical.toml`.

## Build locally

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
make build
```

Use `make serve` for local development. The rendered site is written to `site/`.
The [GitHub Pages workflow](.github/workflows/publish.yml) builds and publishes
when changes reach `main`.

## Funnel documentation

The canonical Funnel reference pages live in the `website/content/docs/`
directory on [Funnel's `develop` branch](https://github.com/calypr/funnel/tree/develop/website/content/docs).
A scheduled workflow checks that branch hourly and opens or updates a pull request
with changed pages and generated navigation. Review and merge the pull request
to publish the update. The workflow also runs the sync tests and builds the site.

The Funnel landing page, download page, and storage index remain CALYPR site
content. The installation script is copied from Funnel's `install.sh`. The sync
converts Funnel's Hugo shortcodes to Markdown compatible with this site and
rejects unknown shortcodes rather than publishing them verbatim.

Three pages are temporarily held at their existing CALYPR versions while newer
site guidance is reconciled with Funnel: the GCP Batch, Kubernetes, and S3
guides. Their expected upstream versions are recorded in
`docs/tools/funnel/.funnel-docs.json`. Once those exact versions reach `develop`,
the sync imports them and removes their exceptions automatically. If the
upstream content changes during review, update the expected hashes after
reconciling the differences.

To run the sync locally against a Funnel checkout:

```sh
python scripts/sync_funnel_docs.py /path/to/funnel --revision "$(git -C /path/to/funnel rev-parse HEAD)"
python -m unittest discover -s tests -v
make build
```

Generated Funnel pages and the marked Funnel navigation block should be changed
in the Funnel repository, not edited manually here. The sync branch is reused
while an update PR is open. If the Funnel revision is unchanged, no PR is created.

The workflow needs the repository setting that allows GitHub Actions to create
pull requests, plus `contents: write` and `pull-requests: write` job permissions.
GitHub places PR workflows created with `GITHUB_TOKEN` in an approval-required
state. The sync workflow runs its own tests and site build before creating the
PR; a repository writer can approve the PR workflows separately.
