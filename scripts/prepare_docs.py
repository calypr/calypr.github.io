#!/usr/bin/env python3
"""Stage the Zensical docs tree with fetched upstream tool docs."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from termynal.markdown import get_default_css, get_default_js


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DOCS = ROOT / "docs"
GENERATED_ROOT = ROOT / ".generated"
GENERATED_DOCS = GENERATED_ROOT / "docs"
BRANCH_CONFIG = ROOT / "scripts" / "branch_config.json"

DEFAULT_BRANCH_PREFERENCES = ["development", "develop", "main", "master"]
PREFER_LOCAL_ENV = "CALYPR_IMPORT_PREFER_LOCAL"

REPO_IMPORTS = {
    "git-drs": {
        "repo_url": "https://github.com/calypr/git-drs.git",
        "local_dir": ROOT.parent / "git-drs",
        "mappings": [
            ("docs/quickstart.md", "tools/git-drs/quickstart.md"),
            ("docs/getting-started.md", "tools/git-drs/getting-started.md"),
            ("docs/installation.md", "tools/git-drs/installation.md"),
            ("docs/commands.md", "tools/git-drs/commands.md"),
            ("docs/troubleshooting.md", "tools/git-drs/troubleshooting.md"),
            ("docs/bucket-mapping.md", "tools/git-drs/docs/bucket-mapping.md"),
            ("docs/git-lfs.md", "tools/git-drs/docs/git-lfs.md"),
            ("docs/developer-guide.md", "tools/git-drs/docs/developer-guide.md"),
            ("docs/remove-files.md", "tools/git-drs/docs/remove-files.md"),
            ("docs/troubleshooting.md", "tools/git-drs/docs/troubleshooting.md"),
        ],
    },
    "syfon": {
        "repo_url": "https://github.com/calypr/syfon.git",
        "local_dir": ROOT.parent / "syfon",
        "mappings": [
            ("docs/index.md", "tools/syfon/index.md"),
            ("docs/quickstart.md", "tools/syfon/quickstart.md"),
            ("docs/configuration.md", "tools/syfon/configuration.md"),
            ("docs/deployment.md", "tools/syfon/deployment.md"),
            ("docs/kubernetes-deployment.md", "tools/syfon/kubernetes-deployment.md"),
            ("docs/local-deployment.md", "tools/syfon/local-deployment.md"),
            ("docs/encryption.md", "tools/syfon/encryption.md"),
            ("docs/troubleshooting.md", "tools/syfon/troubleshooting.md"),
            ("docs/images/syfon-logo.png", "tools/syfon/images/syfon-logo.png"),
        ],
    },
}

MARKDOWN_REWRITES: dict[tuple[str, str], list[tuple[str, str]]] = {
    ("git-drs", "tools/git-drs/getting-started.md"): [
        ("(remove-files.md)", "(docs/remove-files.md)"),
    ],
    ("git-drs", "tools/git-drs/docs/bucket-mapping.md"): [
        ("(getting-started.md)", "(../getting-started.md)"),
        ("(commands.md)", "(../commands.md)"),
        ("(troubleshooting.md)", "(../troubleshooting.md)"),
    ],
    ("git-drs", "tools/git-drs/docs/troubleshooting.md"): [
        ("(getting-started.md)", "(../getting-started.md)"),
        ("(commands.md)", "(../commands.md)"),
    ],
}


def load_branch_preferences() -> dict[str, list[str]]:
    if not BRANCH_CONFIG.exists():
        return {}
    with BRANCH_CONFIG.open(encoding="utf-8") as handle:
        data = json.load(handle)
    return {
        name: [str(branch) for branch in branches]
        for name, branches in data.items()
        if isinstance(branches, list)
    }


def run_git(*args: str, cwd: Path | None = None) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=True,
        text=True,
        capture_output=True,
    )
    return completed.stdout


def copy_source_docs() -> None:
    if GENERATED_ROOT.exists():
        shutil.rmtree(GENERATED_ROOT)
    GENERATED_DOCS.mkdir(parents=True, exist_ok=True)

    for source in SOURCE_DOCS.rglob("*"):
        relative = source.relative_to(SOURCE_DOCS)
        if any(part.startswith(".") for part in relative.parts):
            continue
        destination = GENERATED_DOCS / relative
        if source.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def prefer_local_repos() -> bool:
    value = os.environ.get(PREFER_LOCAL_ENV, "1").strip().lower()
    return value not in {"0", "false", "no", "off"}


def local_repo_path(repo_name: str, repo_config: dict) -> Path | None:
    env_name = f"CALYPR_IMPORT_{repo_name.upper().replace('-', '_')}_DIR"
    override = os.environ.get(env_name)
    if override:
        candidate = Path(override).expanduser().resolve()
        return candidate if candidate.exists() else None
    candidate = Path(repo_config["local_dir"]).resolve()
    return candidate if candidate.exists() else None


def choose_remote_branch(repo_name: str, repo_url: str, preferences: dict[str, list[str]]) -> str:
    preferred = preferences.get(repo_name, DEFAULT_BRANCH_PREFERENCES)
    output = run_git("ls-remote", "--heads", repo_url)
    branches: set[str] = set()
    for line in output.splitlines():
        parts = line.split()
        if len(parts) != 2 or not parts[1].startswith("refs/heads/"):
            continue
        branches.add(parts[1].removeprefix("refs/heads/"))

    for branch in preferred:
        if branch in branches:
            return branch
    if "main" in branches:
        return "main"
    if not branches:
        raise RuntimeError(f"no remote branches found for {repo_name}")
    return sorted(branches)[0]


def copy_mapping(source_root: Path, source_relative: str, destination_relative: str) -> None:
    source = source_root / source_relative
    if not source.exists():
        raise FileNotFoundError(f"missing source import: {source}")
    destination = GENERATED_DOCS / destination_relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def rewrite_imported_markdown(repo_name: str) -> None:
    for (rewrite_repo, destination_relative), replacements in MARKDOWN_REWRITES.items():
        if rewrite_repo != repo_name:
            continue
        destination = GENERATED_DOCS / destination_relative
        if not destination.exists() or destination.suffix.lower() != ".md":
            continue
        content = destination.read_text(encoding="utf-8")
        updated = content
        for old, new in replacements:
            updated = updated.replace(old, new)
        if updated != content:
            destination.write_text(updated, encoding="utf-8")


def import_from_local_repo(repo_name: str, repo_root: Path, repo_config: dict) -> dict[str, str]:
    print(f"[prepare-docs] importing {repo_name} from local repo {repo_root}")
    for source_relative, destination_relative in repo_config["mappings"]:
        copy_mapping(repo_root, source_relative, destination_relative)
    rewrite_imported_markdown(repo_name)
    return {"mode": "local", "source": str(repo_root)}


def import_from_remote_repo(
    repo_name: str,
    repo_url: str,
    repo_config: dict,
    preferences: dict[str, list[str]],
) -> dict[str, str]:
    branch = choose_remote_branch(repo_name, repo_url, preferences)
    sparse_paths = sorted({source for source, _ in repo_config["mappings"]})
    print(f"[prepare-docs] importing {repo_name} from {repo_url} branch {branch}")

    with tempfile.TemporaryDirectory(prefix=f"calypr-docs-{repo_name}-") as tmpdir:
        clone_root = Path(tmpdir) / repo_name
        subprocess.run(
            [
                "git",
                "clone",
                "--branch",
                branch,
                "--depth",
                "1",
                "--filter=blob:none",
                "--sparse",
                repo_url,
                str(clone_root),
            ],
            check=True,
        )
        subprocess.run(
            ["git", "sparse-checkout", "set", "--no-cone", *sparse_paths],
            cwd=clone_root,
            check=True,
        )
        for source_relative, destination_relative in repo_config["mappings"]:
            copy_mapping(clone_root, source_relative, destination_relative)
        rewrite_imported_markdown(repo_name)

    return {"mode": "remote", "source": repo_url, "branch": branch}


def write_termynal_assets() -> None:
    (GENERATED_DOCS / "termynal.css").write_text(get_default_css(), encoding="utf-8")
    (GENERATED_DOCS / "termynal.js").write_text(get_default_js(), encoding="utf-8")


def main() -> int:
    copy_source_docs()
    branch_preferences = load_branch_preferences()
    manifest: dict[str, dict[str, str]] = {}

    for repo_name, repo_config in REPO_IMPORTS.items():
        repo_root = local_repo_path(repo_name, repo_config) if prefer_local_repos() else None
        if repo_root is not None:
            manifest[repo_name] = import_from_local_repo(repo_name, repo_root, repo_config)
            continue
        manifest[repo_name] = import_from_remote_repo(
            repo_name,
            repo_config["repo_url"],
            repo_config,
            branch_preferences,
        )

    write_termynal_assets()
    GENERATED_ROOT.mkdir(parents=True, exist_ok=True)
    (GENERATED_ROOT / "imports.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"[prepare-docs] staged docs at {GENERATED_DOCS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
