---
lead: "This folder contains helper scripts related to the documentation site."
personas:
  - data-steward
  - platform-engineer
  - workflow-engineer
  - researcher-bioinformatician
  - standards-architecture-lead
solutions:
  - manage-data
  - manage-compute
  - integrate-data
  - manage-models
related_tools:
  - git-drs
  - syfon
  - funnel
  - forge
  - grip
  - sifter
  - data-client
---
Usage
-----

This folder contains helper scripts related to the documentation site. The main utility is
`update_doc_links.py` which updates GitHub links in the site documentation to point at the
current development branch for selected `calypr` repositories.

Quick start
-----------

From the repository root you can run the Makefile target:

```bash
make update-branches
```

Or run the script directly:

```bash
python3 scripts/update_doc_links.py
```

What the script does
--------------------

- Looks for markdown and HTML files under `docs/` and `overrides/`.
- For each repository configured, queries remote branches with `git ls-remote --heads`.
- Chooses a preferred branch according to the preference list and rewrites links such as:
  - `https://github.com/calypr/<repo>/tree/<branch>/...`
  - `https://github.com/calypr/<repo>/blob/<branch>/...`
  - `https://raw.githubusercontent.com/calypr/<repo>/<branch>/...`
- Creates a backup of any file it modifies; backups are named `.bak`, `.bak1`, `.bak2`, ...

Configuration
-------------

The script reads a JSON configuration mapping repository names to an ordered list of
preferred branch names. The script looks for a config in this order and uses the first
one it finds:

1. `scripts/branch_config.json`
2. `branch_config.json` at the repo root
3. Built-in defaults inside the script

Example `scripts/branch_config.json`:

```json
{
  "git-drs": ["development", "develop", "main", "master"],
  "syfon": ["development", "develop", "main", "master"]
}
```

Edit this JSON to add repositories or change branch priorities.

Notes & next steps
------------------

- The script is intentionally conservative; it will only update recognized URL forms.
- If you want a preview-only run, or automatic commits, we can add a `--dry-run` or
  `--commit` flag in a follow-up change.

Contact
-------

If you need changes to the update behavior (different URL patterns, different directories,
or automatic commits), open an issue or pull request describing the desired behavior so
the maintainers can review it.


prepare_docs.py - Documentation Preparation & Import
=====================================================

This script stages and prepares the documentation site by merging docs from upstream tool
repositories with the main documentation tree. It handles fetching remote docs, generating
asset files, and building metadata manifests.

Quick start
-----------

From the repository root, run:

```bash
# Using Makefile (if available)
make prepare-docs

# Or run directly with environment defaults (prefers local repos)
python3 scripts/prepare_docs.py

# Or force remote imports (skip local repos)
CALYPR_IMPORT_PREFER_LOCAL=0 python3 scripts/prepare_docs.py

# Or override local path for a specific repo
CALYPR_IMPORT_GIT_DRS_DIR=~/my-git-drs python3 scripts/prepare_docs.py
```

What the script does
--------------------

1. **Copies source docs**: Copies the main documentation tree from `docs/` to `.generated/docs/`,
   excluding hidden files.

2. **Imports tool documentation**: For each configured tool repository:
   - Prefers local clones if they exist (configurable via environment variable)
   - Falls back to remote cloning with sparse checkout for efficiency
   - Copies only specified files according to mappings
   - Rewrites relative links to match the local structure

3. **Generates assets**: Creates termynal CSS and JavaScript files for terminal animations
   in the documentation.

4. **Creates taxonomy manifest**: Scans all markdown files for front matter metadata
   (personas, solutions, related_tools) and generates a JSON manifest at
   `javascripts/page-taxonomy.json` for filtering and categorization.

5. **Records import metadata**: Writes `.generated/imports.json` documenting how each
   repository was imported (local path or remote URL/branch).

Configuration & Environment Variables
--------------------------------------

### Local Repository Preference

By default, the script prefers local clones of tool repositories over remote fetching:

```bash
# Explicitly prefer local repos (default)
export CALYPR_IMPORT_PREFER_LOCAL=1
python3 scripts/prepare_docs.py

# Force remote fetch (ignore local repos)
export CALYPR_IMPORT_PREFER_LOCAL=0
python3 scripts/prepare_docs.py

# Other accepted False values: "false", "no", "off"
```

### Override Local Repository Paths

Override the default local path for a specific repository using environment variables:

```bash
# For git-drs
export CALYPR_IMPORT_GIT_DRS_DIR=~/my-git-drs

# For syfon
export CALYPR_IMPORT_SYFON_DIR=~/my-syfon

# Pattern: CALYPR_IMPORT_<REPO_NAME>_DIR (hyphens → underscores, uppercase)
python3 scripts/prepare_docs.py
```

### Branch Preferences Configuration

The script chooses which branch to import from using preferences defined in
`scripts/branch_config.json`:

```json
{
  "git-drs": ["development", "develop", "main", "master"],
  "syfon": ["development", "develop", "main", "master"]
}
```

If the config doesn't exist, the built-in defaults are used. The script:
- Looks for each branch in order and uses the first one found
- Falls back to "main" if no preferred branch exists
- Uses the alphabetically first branch as a last resort
- Raises an error if no branches are found

Output Files
------------

After running successfully, the script generates:

- **`.generated/docs/`**: The complete prepared documentation tree
- **`.generated/docs/termynal.css`**: Styling for terminal animations
- **`.generated/docs/termynal.js`**: JavaScript for terminal animations
- **`.generated/docs/javascripts/page-taxonomy.json`**: Metadata index for page filtering
- **`.generated/imports.json`**: Record of how each repository was imported

Example imports.json:
```json
{
  "git-drs": {
    "branch": "main",
    "mode": "remote",
    "source": "https://github.com/calypr/git-drs.git"
  },
  "syfon": {
    "mode": "local",
    "source": "/Users/username/syfon"
  }
}
```

Troubleshooting
---------------

**"FileNotFoundError: missing source import"**
- A file specified in the repository mappings doesn't exist in the source repository.
- Check that the remote branch contains the expected files.
- Verify local repository paths are correct.

**"RuntimeError: no remote branches found"**
- The remote repository has no branches (very unusual).
- Check that the repository URL is correct and accessible.

**Import using wrong branch**
- Edit `scripts/branch_config.json` to adjust branch preferences.
- Clear `.generated/` and re-run to test changes.

**Use local repo instead of remote (or vice versa)**
- Set `CALYPR_IMPORT_PREFER_LOCAL` environment variable.
- Override specific repo paths with `CALYPR_IMPORT_<REPO_NAME>_DIR`.


