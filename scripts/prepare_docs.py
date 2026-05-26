#!/usr/bin/env python3
"""Stage the Zensical docs tree with fetched upstream tool docs."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from importlib.resources import files as _pkg_files

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

VALID_PERSONAS = {
    "data-steward",
    "platform-engineer",
    "researcher-bioinformatician",
    "security-compliance-reviewer",
    "standards-architecture-lead",
    "workflow-engineer",
}

VALID_SOLUTIONS = {
    "manage-data",
    "manage-compute",
    "integrate-data",
    "manage-models",
}

VALID_TOOLS = {
    "git-drs",
    "syfon",
    "funnel",
    "forge",
    "grip",
    "sifter",
    "data-client",
}


def load_branch_preferences() -> dict[str, list[str]]:
    """Load branch preferences from the branch configuration file.

    Reads branch preferences from scripts/branch_config.json, which maps repository
    names to an ordered list of preferred branch names. If the config file does not
    exist, returns an empty dictionary.

    Returns:
        dict[str, list[str]]: A mapping of repository names to lists of preferred
                             branch names, in order of preference. Returns {} if
                             the config file doesn't exist.
    """
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
    """Execute a git command and return its output.

    Runs a git command with the specified arguments in the given working directory.
    The command is run with error checking enabled, so a non-zero exit code will
    raise an exception.

    Args:
        *args (str): Command arguments to pass to git (e.g., "ls-remote", "--heads").
        cwd (Path | None): Working directory for the git command. If None, uses the
                          current working directory. Defaults to None.

    Returns:
        str: The standard output from the git command.

    Raises:
        subprocess.CalledProcessError: If the git command returns a non-zero exit code.
    """
    completed = subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=True,
        text=True,
        capture_output=True,
    )
    return completed.stdout


def copy_source_docs() -> None:
    """Copy the source documentation tree to the generated directory.

    Removes any existing generated documentation and creates a fresh copy of all
    files from the SOURCE_DOCS directory (docs/) to GENERATED_DOCS (.generated/docs).
    Skips hidden files and directories (those starting with a dot).

    This prepares a clean workspace for documentation imports and asset generation.
    """
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
    """Check if local repositories should be preferred over remote ones.

    Reads the CALYPR_IMPORT_PREFER_LOCAL environment variable to determine whether
    to prefer local repository clones over fetching from remote. Defaults to True.

    Returns:
        bool: True if local repos should be preferred, False otherwise.
              Treats "0", "false", "no", and "off" (case-insensitive) as False;
              all other values (including empty string) are treated as True.
    """
    value = os.environ.get(PREFER_LOCAL_ENV, "1").strip().lower()
    return value not in {"0", "false", "no", "off"}


def local_repo_path(repo_name: str, repo_config: dict) -> Path | None:
    """Resolve the local path to a repository, with environment variable override.

    Checks for a repository path in this order:
    1. An environment variable named CALYPR_IMPORT_<REPO_NAME>_DIR (with hyphens
       converted to underscores and uppercased).
    2. The local_dir specified in repo_config.

    Returns the first path that exists, or None if neither exists.

    Args:
        repo_name (str): The repository name (e.g., "git-drs", "syfon").
        repo_config (dict): The repository configuration dictionary containing
                           the "local_dir" key.

    Returns:
        Path | None: The absolute path to the local repository if it exists,
                    or None if no valid path is found.
    """
    env_name = f"CALYPR_IMPORT_{repo_name.upper().replace('-', '_')}_DIR"
    override = os.environ.get(env_name)
    if override:
        candidate = Path(override).expanduser().resolve()
        return candidate if candidate.exists() else None
    candidate = Path(repo_config["local_dir"]).resolve()
    return candidate if candidate.exists() else None


def choose_remote_branch(repo_name: str, repo_url: str, preferences: dict[str, list[str]]) -> str:
    """Select the best remote branch based on preferences.

    Queries the remote repository for available branches and selects the first one
    that matches the preference list for the given repository. If no preferred branch
    is found and "main" exists, returns "main". Otherwise returns the alphabetically
    first branch name.

    Args:
        repo_name (str): The repository name.
        repo_url (str): The full repository URL.
        preferences (dict[str, list[str]]): Mapping of repo names to preference lists.

    Returns:
        str: The selected branch name.

    Raises:
        RuntimeError: If no remote branches are found for the repository.
    """
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
    """Copy a file from source repository to the generated docs directory.

    Copies a single file specified by source_relative (relative to source_root)
    to destination_relative (relative to GENERATED_DOCS). Creates parent directories
    as needed.

    Args:
        source_root (Path): The root path of the source repository.
        source_relative (str): The relative path to the source file within the repo.
        destination_relative (str): The relative path where the file should be copied
                                    within the generated docs directory.

    Raises:
        FileNotFoundError: If the source file does not exist.
    """
    source = source_root / source_relative
    if not source.exists():
        raise FileNotFoundError(f"missing source import: {source}")
    destination = GENERATED_DOCS / destination_relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def rewrite_imported_markdown(repo_name: str) -> None:
    """Rewrite markdown links in imported documentation files.

    Updates relative links in imported markdown files according to the MARKDOWN_REWRITES
    mapping. This handles converting links from the upstream repository format to the
    local documentation structure. Only processes files that exist and have .md extension.

    Args:
        repo_name (str): The repository name to filter rewrites for.
    """
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
    """Import documentation from a locally cloned repository.

    Copies all files specified in the repo_config mappings from the local repository
    to the generated docs directory, then applies any markdown rewrites.

    Args:
        repo_name (str): The repository name.
        repo_root (Path): The absolute path to the local repository.
        repo_config (dict): The repository configuration dictionary containing
                           the "mappings" key.

    Returns:
        dict[str, str]: A metadata dictionary with mode "local" and the source path.
    """
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
    """Import documentation from a remote repository.

    Clones the remote repository using sparse checkout to only fetch the files
    specified in repo_config mappings, then copies them to the generated docs
    directory and applies any markdown rewrites.

    Uses git clone with --depth 1, --sparse, and --filter=blob:none for efficiency.
    The repository is cloned into a temporary directory and deleted after import.

    Args:
        repo_name (str): The repository name.
        repo_url (str): The remote repository URL.
        repo_config (dict): The repository configuration dictionary containing
                           the "mappings" key.
        preferences (dict[str, list[str]]): Mapping of repo names to branch preferences.

    Returns:
        dict[str, str]: A metadata dictionary with mode "remote", source URL,
                       and selected branch name.
    """
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
    """Write Termynal CSS and JavaScript assets to the generated docs directory.

    Writes default termynal stylesheet and script files from the termynal library
    to the generated docs directory. These files enable terminal animations in the
    documentation.
    """
    assets = _pkg_files("termynal") / "assets"
    (GENERATED_DOCS / "termynal.css").write_bytes((assets / "termynal.css").read_bytes())
    (GENERATED_DOCS / "termynal.js").write_bytes((assets / "termynal.js").read_bytes())


def parse_front_matter_lists(markdown: str) -> dict[str, list[str]]:
    """Parse front matter list fields from markdown content.

    Extracts named lists from YAML front matter blocks (between "---" markers).
    Parses "personas", "solutions", and "related_tools" lists, filtering out any
    values that are not in the respective VALID_* sets.

    Args:
        markdown (str): The full markdown content including front matter.

    Returns:
        dict[str, list[str]]: A dictionary with keys "personas", "solutions", and
                             "related_tools", each mapping to a list of valid values.
                             Returns empty lists for missing or invalid fields.
    """
    if not markdown.startswith("---\n"):
        return {"personas": [], "solutions": [], "related_tools": []}

    end = markdown.find("\n---\n", 4)
    if end == -1:
        return {"personas": [], "solutions": [], "related_tools": []}

    front_matter = markdown[4:end].splitlines()
    data = {"personas": [], "solutions": [], "related_tools": []}

    for key in ("personas", "solutions", "related_tools"):
        collecting = False
        for line in front_matter:
            if line.startswith(f"{key}:"):
                collecting = True
                continue
            if collecting:
                if line.startswith("  - "):
                    value = line.removeprefix("  - ").strip()
                    if value:
                        data[key].append(value)
                    continue
                break

    data["personas"] = [value for value in data["personas"] if value in VALID_PERSONAS]
    data["solutions"] = [value for value in data["solutions"] if value in VALID_SOLUTIONS]
    data["related_tools"] = [value for value in data["related_tools"] if value in VALID_TOOLS]
    return data


def markdown_to_route(markdown_path: Path) -> str:
    """Convert a markdown file path to its documentation URL route.

    Transforms absolute markdown file paths to relative URL routes for the website.
    Special cases:
    - index.md at the root → "/"
    - index.md in subdirectories → "/path/to/folder/"
    - Other files → "/path/to/file/"

    Args:
        markdown_path (Path): The absolute path to the markdown file.

    Returns:
        str: The corresponding URL route string.
    """
    relative = markdown_path.relative_to(GENERATED_DOCS).as_posix()
    if relative == "index.md":
        return "/"

    if relative.endswith("/index.md"):
        return f"/{relative.removesuffix('index.md')}"

    return f"/{relative.removesuffix('.md')}/"


def write_page_taxonomy_manifest() -> None:
    """Generate and write a JSON manifest of page metadata.

    Scans all markdown files in the generated docs directory, extracts front matter
    metadata (personas, solutions, related_tools) from each file, and writes a
    JSON manifest to javascripts/page-taxonomy.json.

    The manifest maps URL routes to taxonomic metadata, enabling filtering and
    categorization of documentation pages. Only includes pages with at least one
    taxonomy field populated.
    """
    taxonomy: dict[str, dict[str, list[str]]] = {}

    for markdown_file in GENERATED_DOCS.rglob("*.md"):
        parsed = parse_front_matter_lists(markdown_file.read_text(encoding="utf-8"))
        if not parsed["personas"] and not parsed["solutions"] and not parsed["related_tools"]:
            continue

        route = markdown_to_route(markdown_file)
        taxonomy[route] = parsed

    destination = GENERATED_DOCS / "javascripts" / "page-taxonomy.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(taxonomy, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    """Main entry point for preparing and staging documentation.

    Orchestrates the complete documentation preparation workflow:
    1. Copies source docs to generated directory
    2. Loads branch preferences from config
    3. Imports each configured repository (local or remote)
    4. Writes termynal assets for terminal animations
    5. Generates page taxonomy manifest
    6. Writes import metadata to .generated/imports.json

    Returns:
        int: Exit code (0 for success).
    """
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
    write_page_taxonomy_manifest()
    GENERATED_ROOT.mkdir(parents=True, exist_ok=True)
    (GENERATED_ROOT / "imports.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"[prepare-docs] staged docs at {GENERATED_DOCS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
