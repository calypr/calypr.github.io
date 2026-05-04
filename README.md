# CALYPR Docs

This mkdocs-based codebase deploys documentation to [calypr.org](https://calypr.org)

<a href="https://calypr.org">![CALYPR Homepage](./docs/images/website_header.png)</a>

## Local Development

```sh
➜ python -m venv venv

➜ source venv/bin/activate

➜ pip install -r requirements.txt

➜ mkdocs serve

INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.25 seconds
INFO     -  [13:45:40] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [13:45:40] Serving on http://127.0.0.1:8000/
```

Running on a port other than 8000 is possible with the `--dev-addr <IP:PORT>` flag (e.g. `mkdocs serve --dev-addr 8181` will start the server on localhost:8181).

## Publishing to [calypr.org](https://calypr.org)

The site is automatically built and published on every push to the main branch (using the Github Actions workflow file in [publish.yml](.github/workflows/publish.yml)).

To skip this workflow add `[skip ci]` (or any [equivalent variation](https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs)) anywhere in the commit message.

To manually update the site run the `mkdocs gh-deploy --force` command:

```sh
➜ mkdocs gh-deploy --force

INFO     -  Cleaning site directory
INFO     -  Building documentation to directory: calypr.org/site
INFO     -  Documentation built in 0.49 seconds
INFO     -  Copying 'calypr.org/site' to 'gh-pages' branch and pushing to GitHub.
INFO     -  Your documentation should shortly be available at: https://calypr.org/
```
