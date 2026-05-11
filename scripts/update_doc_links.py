#!/usr/bin/env python3
"""
Update links in the docs that point to GitHub repos to use a chosen branch for each repo.

This script looks for occurrences of URLs like:
 - https://github.com/calypr/<repo>/tree/<branch>/...
 - https://github.com/calypr/<repo>/blob/<branch>/...
 - https://raw.githubusercontent.com/calypr/<repo>/<branch>/...

It queries the remote repository for available branches (via `git ls-remote --heads`) and
selects the preferred branch according to a priority list (development, develop, main, master).
It then updates markdown/html files under `docs/` and `overrides/` replacing the branch segment
with the selected branch.

Usage: python3 scripts/update_doc_links.py

Exit codes: 0 on success, non-zero on error.
"""
import json
import re
import subprocess
import sys
from pathlib import Path


# Default configuration (used if no config file is present)
DEFAULT_REPOS = {
    "git-drs": ["development", "develop", "main", "master"],
    "syfon": ["development", "develop", "main", "master"],
}

ROOT = Path(__file__).resolve().parents[1]
DOC_PATHS = [ROOT / "docs", ROOT / "overrides"]
CONFIG_PATHS = [ROOT / "scripts" / "branch_config.json", ROOT / "branch_config.json"]

def get_remote_branches(repo: str):
    """Return a set of branch names available in the remote repo.
    Uses `git ls-remote --heads` to avoid needing GitHub API tokens.
    """
    repo_url = f"https://github.com/calypr/{repo}.git"
    try:
        out = subprocess.check_output(["git", "ls-remote", "--heads", repo_url], text=True)
    except subprocess.CalledProcessError as e:
        # Return None to indicate an unexpected failure querying the remote
        print(f"ERROR: failed to query remote for {repo}: {repr(e)}")
        return None
    except Exception as e:
        print(f"ERROR: unexpected error querying remote for {repo}: {repr(e)}")
        return None
    branches = set()
    for line in out.splitlines():
        parts = line.strip().split()
        if len(parts) >= 2 and parts[1].startswith("refs/heads/"):
            branches.add(parts[1][len("refs/heads/"):])
    return branches

def choose_branch(available: set, preferred: list):
    for p in preferred:
        if p in available:
            return p
    # fallback: pick 'main' if present, else first available
    if "main" in available:
        return "main"
    return sorted(available)[0] if available else None

def update_file(path: Path, repo: str, branch: str):
    text = path.read_text(encoding="utf-8")
    orig = text

    # replace github.com links with tree/blob branch updated
    # patterns: /tree/<old>/, /blob/<old>/, raw.githubusercontent.com/<repo>/<old>/
    pattern1 = re.compile(rf"(https://github\.com/calypr/{re.escape(repo)}/(?:tree|blob)/)([^/\s]+)")
    text = pattern1.sub(rf"\1{branch}", text)

    # Handle raw.githubusercontent links in a single pass for both:
    #  - .../{repo}/refs/heads/<branch>/...  (sometimes used)
    #  - .../{repo}/<branch>/...
    # Using one pattern avoids treating the literal "refs" path segment as a branch name.
    pattern_raw = re.compile(
        rf"(https://raw\.githubusercontent\.com/calypr/{re.escape(repo)}/)(?:refs/heads/)?([^/\s]+)"
    )
    text = pattern_raw.sub(rf"\1{branch}", text)

    # Also replace bare repository links (exact) to point to the chosen branch tree view
    # but only when the link is the repo root (no trailing path)
    pattern3 = re.compile(rf"(https://github\.com/calypr/{re.escape(repo)})(?![\w\-/])")
    text = pattern3.sub(rf"https://github.com/calypr/{repo}/tree/{branch}", text)

    if text != orig:
        # choose a unique backup filename
        i = 0
        while True:
            suffix = ".bak" if i == 0 else f".bak{i}"
            backup = path.with_suffix(path.suffix + suffix)
            if not backup.exists():
                break
            i += 1
        # write backup and new file
        backup.write_text(orig, encoding="utf-8")
        path.write_text(text, encoding="utf-8")
        print(f"Updated {path} (backup at {backup.name})")
        return True
    return False

def find_files(root: Path):
    for p in root.rglob("*.md"):
        yield p
    for p in root.rglob("*.html"):
        yield p

def main():
    any_changes = False
    any_errors = False
    # Load configuration from JSON if present
    repos = DEFAULT_REPOS
    for p in CONFIG_PATHS:
        if p.exists():
            try:
                repos = json.loads(p.read_text(encoding="utf-8"))
                print(f"Loaded config from {p}")
            except Exception as e:
                print(f"Warning: failed to load config {p}: {e}. Using defaults.")
            break

    for repo, prefs in repos.items():
        print(f"Processing repo: {repo}")
        branches = get_remote_branches(repo)
        if branches is None:
            # get_remote_branches logged the error already
            any_errors = True
            print(f"  Error: remote branch query failed for {repo}; skipping")
            continue
        if not branches:
            print(f"  Warning: no remote branches found for {repo}; skipping")
            continue
        chosen = choose_branch(branches, prefs)
        if not chosen:
            print(f"  Warning: couldn't choose branch for {repo}; skipping")
            continue
        print(f"  Selected branch: {chosen}")

        # scan files
        for docroot in DOC_PATHS:
            if not docroot.exists():
                continue
            for f in find_files(docroot):
                try:
                    changed = update_file(f, repo, chosen)
                    any_changes = any_changes or changed
                except Exception as e:
                    any_errors = True
                    print(f"  ERROR updating file {f}: {repr(e)}")

    if any_changes:
        print("Done. Files were modified. Review .bak files created next to edited files.")
    else:
        print("Done. No changes necessary.")

    if any_errors:
        print("Completed with errors. See messages above.")
        return 2
    return 0

if __name__ == '__main__':
    sys.exit(main())

