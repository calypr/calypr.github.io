# CALYPR Docs

This mkdocs-based codebase deploys documentation to [calypr.github.io](https://calypr.github.io)

<a href="https://calypr.github.io">![Main landing page for CALYPR](./docs/images/main-page.png)</a>

It is built using [mkdocs-material](https://squidfunk.github.io/mkdocs-material/reference/) and [mkdocs-macros-plugin](https://mkdocs-macros-plugin.readthedocs.io/en/latest/)

# Local Development

```shell
# setup local environment
python -m venv venv
source venv/bin/activate
# install dependencies
pip install -r requirements.txt
```

To start the documentation server run the `mkdocs serve` command:

```sh
➜ mkdocs serve

INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.25 seconds
INFO     -  [13:45:40] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [13:45:40] Serving on http://127.0.0.1:8000/
```

Running on a port other than 8000 is possible with the `--dev-addr <IP:PORT>` flag (e.g. `mkdocs serve --dev-addr 8181` will start the server on localhost:8181).

# Publishing to [calypr.github.io](https://calypr.github.io)

The site is automatically built and published on every push to the main branch (using the Github Actions workflow file in [publish.yml](.github/workflows/publish.yml)).

To skip this workflow add `[skip ci]` (or any [equivalent variation](https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs)) anywhere in the commit message.

To manually update the site run the `mkdocs gh-deploy --force` command:

```sh
➜ mkdocs gh-deploy --force

INFO     -  Cleaning site directory
INFO     -  Building documentation to directory: /Users/beckmanl/code/calypr.github.io/site
INFO     -  Documentation built in 0.49 seconds
INFO     -  Copying '/Users/beckmanl/code/calypr.github.io/site' to 'gh-pages' branch and pushing to GitHub.
INFO     -  Your documentation should shortly be available at: https://calypr.github.io/
```

## Terminal Image Sources

- [CALYPR Upload](https://app.codeimage.dev/c8c39d33-c9d3-440f-9680-f4f7976676d9)
- [CALYPR Download](https://app.codeimage.dev/d1c80a2d-cded-432e-9d2e-825a0e058996)
