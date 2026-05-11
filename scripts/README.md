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
or automatic commits), reply with the desired behavior and I will implement it.

