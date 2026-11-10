#!/usr/bin/env python3
"""Copy Funnel's public Markdown documentation into the CALYPR site."""

import argparse
import json
import os
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

SITE = Path(__file__).resolve().parents[1]
DEST = SITE / "docs/tools/funnel/docs"
MANIFEST = SITE / "docs/tools/funnel/.funnel-docs.json"
NAV = SITE / "zensical.toml"
GROUPS = [
    ("Storage", "storage"), ("Compute", "compute"),
    ("Databases", "databases"), ("Security", "security"),
    ("Integrations", "integrations"), ("Events", "events"),
    ("Metrics", "metrics"), ("Development", "development"),
]
SITE_OWNED = {"download.md"}


def destination(path: Path) -> Path:
    return Path("docs.md") if path == Path("README.md") else path


def convert(text: str, page: Path, upstream: Path, revision: str) -> str:
    if re.search(r"\{\{[<%]", text):
        raise ValueError("Unconverted Hugo shortcode in " + str(page))
    source = upstream / "docs"
    parent = destination(page.relative_to(source)).parent

    def link(url: str) -> str:
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path or url.startswith("/"):
            return url
        target = (page.parent / parsed.path).resolve()
        if not target.is_file():
            return url
        if target.is_relative_to(source):
            relative = os.path.relpath(destination(target.relative_to(source)), parent)
            return urlunsplit(("", "", relative, parsed.query, parsed.fragment))
        if target.is_relative_to(upstream):
            repo_path = target.relative_to(upstream).as_posix()
            return urlunsplit(("https", "github.com", f"/calypr/funnel/blob/{revision}/{repo_path}", parsed.query, parsed.fragment))
        return url

    text = re.sub(r"(?m)(?<! ) $", "", text)
    text = re.sub(r"(\]\()([^\s)]+)(\))", lambda m: m[1] + link(m[2]) + m[3], text)
    return re.sub(r"(?m)^(\[[^\]]+\]:\s*)(\S+)", lambda m: m[1] + link(m[2]), text)


def title(path: Path) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", path.read_text(), re.MULTILINE)
    return match[1] if match else path.stem.replace("-", " ").title()


def sync(upstream: Path, revision: str) -> None:
    upstream = upstream.resolve()
    source = upstream / "docs"
    if not (source / "tasks.md").is_file() or not (source / "README.md").is_file():
        raise ValueError("Not a Funnel source checkout: docs/README.md or docs/tasks.md is missing")
    files = sorted(
        p for p in source.rglob("*")
        if p.is_file() and p.relative_to(source).parts[0] != "internal"
        and not any(part.startswith(".") for part in p.relative_to(source).parts)
    )
    pages = [p for p in files if p.suffix == ".md"]
    sections = {p.relative_to(source).parts[0] for p in pages if p.parent != source}
    unknown = sections - {folder for _, folder in GROUPS}
    if unknown:
        raise ValueError("Unknown Funnel documentation sections: " + ", ".join(sorted(unknown)))
    imported = {}
    for path in files:
        name = destination(path.relative_to(source)).as_posix()
        if name in SITE_OWNED:
            raise ValueError("Upstream page conflicts with site-owned content: " + name)
        imported[name] = (
            convert(path.read_text(), path, upstream, revision).encode()
            if path.suffix == ".md" else path.read_bytes()
        )

    nav = ["      # BEGIN GENERATED FUNNEL NAV", '      { "Funnel" = [',
           '        "tools/funnel/index.md",',
           '        { "Overview" = "tools/funnel/docs/docs.md" },',
           '        { "Download" = "tools/funnel/docs/download.md" },']

    def entry(page: Path, indent: str) -> str:
        target = "tools/funnel/docs/" + destination(page.relative_to(source)).as_posix()
        return indent + "{ " + json.dumps(title(page), ensure_ascii=False) + " = " + json.dumps(target) + " },"

    indexes = {folder + ".md" for _, folder in GROUPS}
    root_pages = [p for p in pages if p.parent == source and p.name not in indexes | {"README.md"}]
    priority = {"tasks.md": 0, "upgrading.md": 1}
    for page in sorted(root_pages, key=lambda p: (priority.get(p.name, 2), title(p).lower())):
        nav.append(entry(page, "        "))
    for label, folder in GROUPS:
        entries = sorted((p for p in pages if p.relative_to(source).parts[0] == folder), key=lambda p: title(p).lower())
        index = source / (folder + ".md")
        if not entries and not index.is_file():
            continue
        nav.append("        { " + json.dumps(label) + " = [")
        if index.is_file():
            nav.append('          "tools/funnel/docs/' + index.name + '",')
        nav.extend(entry(p, "          ") for p in entries)
        nav.append("        ] },")
    nav += ["      ] },", "      # END GENERATED FUNNEL NAV"]
    config = NAV.read_text()
    begin, end = "      # BEGIN GENERATED FUNNEL NAV", "      # END GENERATED FUNNEL NAV"
    if config.count(begin) != 1 or config.count(end) != 1 or config.index(begin) >= config.index(end):
        raise ValueError("Missing or invalid Funnel navigation markers")

    DEST.mkdir(parents=True, exist_ok=True)
    for path in DEST.rglob("*"):
        if path.is_file() and path.relative_to(DEST).as_posix() not in imported.keys() | SITE_OWNED:
            path.unlink()
    for name, content in imported.items():
        target = DEST / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    (SITE / "docs/tools/funnel/install.sh").write_bytes((upstream / "install.sh").read_bytes())
    NAV.write_text(config[:config.index(begin)] + "\n".join(nav) + config[config.index(end) + len(end):])
    MANIFEST.write_text(json.dumps({
        "source": "https://github.com/calypr/funnel", "branch": "develop",
        "source_directory": "docs", "revision": revision, "files": sorted(imported),
    }, indent=2) + "\n")
    print(f"Synced {len(pages)} Funnel pages from {revision}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("upstream", type=Path)
    parser.add_argument("--revision", required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"[a-f0-9]{40}", args.revision):
        parser.error("--revision must be a full Git commit SHA")
    sync(args.upstream.resolve(), args.revision)
