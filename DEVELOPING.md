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

The canonical Funnel reference pages live in the `docs/`
directory on [Funnel's `develop` branch](https://github.com/calypr/funnel/tree/develop/docs).
A scheduled workflow checks that branch daily and opens or updates a pull request
with changed pages and generated navigation. Review and merge the pull request
to publish the update. The workflow also runs the sync tests and builds the site.

The Funnel landing and download pages remain CALYPR site content. Reference
pages, section overviews, navigation, and documentation assets come from Funnel.
The public installer is copied from Funnel's `install.sh`.

The sync reads page titles from Markdown headings and keeps the existing
Overview URL by importing `docs/README.md` as `docs/docs.md`. Repository-source
links are rewritten to the imported commit on GitHub. Retired pages are removed,
including Elasticsearch. Private `docs/internal/` content and hidden files are
excluded. Unknown sections and Hugo shortcodes stop the sync before publication.

The earlier exceptions for the GCP Batch, Kubernetes, and S3 guides have been
removed: their reconciled content is now in Funnel `develop`.

To run the sync locally against a Funnel checkout:

```sh
python scripts/sync_funnel_docs.py /path/to/funnel --revision "$(git -C /path/to/funnel rev-parse HEAD)"
python -m unittest discover -s tests -v
make build
```

Generated Funnel pages and the marked Funnel navigation block should be changed
in the Funnel repository, not edited manually here. The sync branch is reused
while an update PR is open. If the Funnel revision is unchanged, no PR is created.

The workflow needs both the organization policy and the repository setting that
allow GitHub Actions to create pull requests, plus `contents: write` and
`pull-requests: write` job permissions.
GitHub places PR workflows created with `GITHUB_TOKEN` in an approval-required
state. The sync workflow runs its own tests and site build before creating the
PR; a repository writer can approve the PR workflows separately.
