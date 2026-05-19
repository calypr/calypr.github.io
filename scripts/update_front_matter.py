#!/usr/bin/env python3
"""Populate lead/personas/solutions/related_tools front matter for markdown pages.

This script is intentionally conservative:
- it preserves any existing front matter keys
- it inserts lead/personas/solutions if missing
- it creates front matter for files that do not yet have it
"""

from __future__ import annotations

from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PERSONA_ORDER = [
    "data-steward",
    "platform-engineer",
    "workflow-engineer",
    "researcher-bioinformatician",
    "security-compliance-reviewer",
    "standards-architecture-lead",
]
SOLUTION_ORDER = ["manage-data", "manage-compute", "integrate-data", "manage-models"]
TOOL_ORDER = ["git-drs", "syfon", "funnel", "forge", "grip", "sifter", "data-client"]


def relpath(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def strip_front_matter(text: str):
    if text.startswith("---\n"):
        match = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
        if match:
            return match.group(1), match.group(2)
    return None, text


TARGETED_FRONT_MATTER_KEYS = {"lead", "personas", "solutions", "related_tools"}


def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^]]+)]\(([^)]*)\)", r"\1", text)
    text = re.sub(r"!\[([^]]*)]\(([^)]*)\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def first_sentence(text: str) -> str:
    text = clean_text(text)
    if not text:
        return ""
    match = re.search(r"^(.+?[.!?])(?:\s|$)", text)
    return (match.group(1) if match else text).strip()


def extract_lead(body: str) -> str:
    body = body.lstrip("\n")
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block:
            continue
        if block.startswith(("```", "~~~", "#", "![(")):
            continue
        if block.startswith("!["):
            continue
        if block.startswith("<"):
            paras = re.findall(r"<p[^>]*>(.*?)</p>", block, re.S)
            for para in paras:
                sentence = first_sentence(para)
                if len(clean_text(sentence).split()) >= 4 and len(clean_text(sentence)) >= 25:
                    return sentence
            for para in paras:
                sentence = first_sentence(para)
                if sentence:
                    return sentence
        sentence = first_sentence(block)
        if len(clean_text(sentence).split()) >= 4 and len(clean_text(sentence)) >= 20:
            return sentence

    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith(("#", "```", "![")):
            continue
        return first_sentence(line)
    return ""


def dedupe_in_order(items, order):
    seen = set()
    result = []
    for item in order:
        if item in items and item not in seen:
            result.append(item)
            seen.add(item)
    return result


def infer_solutions(path: Path, body: str):
    rel = relpath(path)
    if rel in {
        "README.md",
        "DEVELOPING.md",
        "scripts/README.md",
        "docs/index.md",
        "docs/products/index.md",
        "docs/solutions/index.md",
        "docs/developers/index.md",
        "docs/platform/index.md",
        "docs/platform/open-platform.md",
    }:
        return SOLUTION_ORDER[:]
    if rel == "docs/platform/data-governance.md":
        return ["manage-data", "integrate-data"]
    if rel == "docs/platform/research-workflows.md":
        return ["manage-data", "manage-compute"]
    if rel == "docs/solutions/manage-data.md":
        return ["manage-data"]
    if rel == "docs/solutions/manage-compute.md":
        return ["manage-compute"]
    if rel == "docs/solutions/integrate-data.md":
        return ["integrate-data"]
    if rel == "docs/solutions/manage-models.md":
        return ["manage-models"]
    if rel.startswith("docs/calypr/data/"):
        return ["manage-data", "integrate-data"]
    if rel.startswith("docs/calypr/analysis/"):
        return ["manage-compute"]
    if rel.startswith("docs/calypr/project-management/calypr-admin/"):
        return ["manage-data"]
    if rel.startswith("docs/calypr/project-management/"):
        return ["manage-data", "manage-compute", "integrate-data"]
    if rel.startswith("docs/calypr/website/"):
        return ["manage-data"]
    if rel == "docs/calypr/index.md":
        return ["manage-data", "manage-compute", "integrate-data"]
    if rel == "docs/calypr/quick-start.md":
        return ["manage-data", "manage-compute"]
    if rel == "docs/calypr/troubleshooting.md":
        return ["manage-data", "manage-compute"]
    if rel.startswith("docs/tools/git-drs/"):
        return ["manage-data"]
    if rel.startswith("docs/tools/funnel/"):
        return ["manage-compute"]
    if rel.startswith("docs/tools/forge/"):
        return ["integrate-data"]
    if rel.startswith("docs/tools/grip/"):
        return ["integrate-data"]
    if rel.startswith("docs/tools/data-client/"):
        return ["manage-data"]
    if rel.startswith("docs/tools/sifter/"):
        return ["integrate-data", "manage-compute"]
    if rel == "docs/tools/index.md":
        return SOLUTION_ORDER[:]

    low = (rel + "\n" + body).lower()
    solutions = []
    if any(k in low for k in ("model", "benchmark")):
        solutions.append("manage-models")
    if any(k in low for k in ("workflow", "task", "tes", "compute", "execution")):
        solutions.append("manage-compute")
    if any(k in low for k in ("metadata", "graph", "fhir", "schema", "validation", "query")):
        solutions.append("integrate-data")
    if any(k in low for k in ("data", "dataset", "drs", "upload", "download", "access", "govern")):
        solutions.append("manage-data")
    return dedupe_in_order(solutions, SOLUTION_ORDER)


def infer_related_tools(path: Path, body: str):
    rel = relpath(path)
    if rel in {"README.md", "DEVELOPING.md", "scripts/README.md", "docs/index.md", "docs/products/index.md", "docs/solutions/index.md", "docs/developers/index.md", "docs/platform/index.md", "docs/personas/index.md", "docs/tools/index.md"}:
        return TOOL_ORDER[:]
    if rel == "docs/platform/data-governance.md":
        return ["git-drs", "syfon", "data-client", "forge", "grip"]
    if rel == "docs/platform/research-workflows.md":
        return ["funnel", "git-drs", "data-client"]
    if rel == "docs/platform/open-platform.md":
        return ["git-drs", "syfon", "funnel", "forge", "grip", "sifter", "data-client"]
    if rel == "docs/solutions/manage-data.md":
        return ["git-drs", "syfon", "data-client"]
    if rel == "docs/solutions/manage-compute.md":
        return ["funnel", "git-drs"]
    if rel == "docs/solutions/integrate-data.md":
        return ["forge", "grip", "sifter"]
    if rel == "docs/solutions/manage-models.md":
        return ["grip", "funnel", "forge"]
    if rel == "docs/personas/data-steward.md":
        return ["data-client", "git-drs", "syfon", "forge", "grip"]
    if rel == "docs/personas/platform-engineer.md":
        return TOOL_ORDER[:]
    if rel == "docs/personas/workflow-engineer.md":
        return ["funnel", "git-drs", "syfon"]
    if rel == "docs/personas/researcher-bioinformatician.md":
        return ["grip", "sifter", "funnel", "forge"]
    if rel == "docs/personas/security-compliance-reviewer.md":
        return ["data-client", "git-drs", "syfon"]
    if rel == "docs/personas/standards-architecture-lead.md":
        return TOOL_ORDER[:]
    if rel == "docs/calypr/data/introduction.md" or rel.startswith("docs/calypr/data/"):
        return ["git-drs", "syfon", "forge", "grip", "data-client"]
    if rel == "docs/calypr/analysis/query.md" or rel.startswith("docs/calypr/analysis/"):
        return ["funnel", "grip", "sifter", "forge"]
    if rel.startswith("docs/calypr/project-management/calypr-admin/"):
        return ["data-client"]
    if rel.startswith("docs/calypr/project-management/"):
        return ["data-client", "git-drs", "syfon", "forge"]
    if rel.startswith("docs/calypr/website/"):
        return ["data-client"]
    if rel.startswith("docs/tools/git-drs/"):
        return ["git-drs", "syfon"]
    if rel.startswith("docs/tools/syfon/"):
        return ["syfon"]
    if rel.startswith("docs/tools/funnel/"):
        return ["funnel"]
    if rel.startswith("docs/tools/forge/"):
        return ["forge"]
    if rel.startswith("docs/tools/grip/"):
        return ["grip"]
    if rel.startswith("docs/tools/sifter/"):
        return ["sifter"]
    if rel.startswith("docs/tools/data-client/"):
        return ["data-client"]

    low = (rel + "\n" + body).lower()
    tools = []
    if any(k in low for k in ("drs", "git-drs", "bucket", "object storage", "transfer", "upload", "download", "govern", "access", "profile", "repo")):
        tools.extend(["git-drs", "syfon", "data-client"])
    if any(k in low for k in ("workflow", "task", "tes", "compute", "execution", "analysis", "portable", "reproducible")):
        tools.extend(["funnel", "git-drs"])
    if any(k in low for k in ("metadata", "graph", "fhir", "schema", "validation", "query", "discovery", "integration")):
        tools.extend(["forge", "grip", "sifter"])
    if any(k in low for k in ("project", "admin", "request", "collaborator", "auth", "security", "compliance")):
        tools.append("data-client")
    return dedupe_in_order(tools, TOOL_ORDER)


def infer_personas(path: Path, body: str, solutions):
    rel = relpath(path)
    if rel in {"README.md", "DEVELOPING.md", "scripts/README.md"}:
        personas = ["platform-engineer", "standards-architecture-lead"]
    elif rel in {"docs/index.md", "docs/products/index.md"}:
        personas = ["data-steward", "platform-engineer", "security-compliance-reviewer", "standards-architecture-lead"]
    elif rel == "docs/solutions/index.md":
        personas = ["data-steward", "platform-engineer", "workflow-engineer", "standards-architecture-lead"]
    elif rel == "docs/developers/index.md":
        personas = ["platform-engineer", "workflow-engineer", "standards-architecture-lead", "researcher-bioinformatician"]
    elif rel in {"docs/platform/index.md", "docs/platform/open-platform.md"}:
        personas = ["platform-engineer", "standards-architecture-lead", "security-compliance-reviewer"]
    elif rel == "docs/platform/data-governance.md":
        personas = ["data-steward", "platform-engineer", "security-compliance-reviewer"]
    elif rel == "docs/platform/research-workflows.md":
        personas = ["workflow-engineer", "platform-engineer", "standards-architecture-lead"]
    elif rel == "docs/solutions/manage-data.md":
        personas = ["data-steward", "platform-engineer", "security-compliance-reviewer"]
    elif rel == "docs/solutions/manage-compute.md":
        personas = ["workflow-engineer", "platform-engineer"]
    elif rel == "docs/solutions/integrate-data.md":
        personas = ["data-steward", "platform-engineer", "standards-architecture-lead"]
    elif rel == "docs/solutions/manage-models.md":
        personas = ["researcher-bioinformatician", "workflow-engineer", "standards-architecture-lead"]
    elif rel.startswith("docs/calypr/data/"):
        personas = ["data-steward", "platform-engineer", "standards-architecture-lead"]
    elif rel.startswith("docs/calypr/analysis/"):
        personas = ["workflow-engineer", "researcher-bioinformatician", "platform-engineer"]
    elif rel.startswith("docs/calypr/project-management/calypr-admin/"):
        personas = ["data-steward", "platform-engineer", "security-compliance-reviewer"]
    elif rel.startswith("docs/calypr/project-management/"):
        personas = ["data-steward", "platform-engineer", "security-compliance-reviewer"]
    elif rel.startswith("docs/calypr/website/"):
        personas = ["data-steward", "platform-engineer"]
    elif rel in {"docs/calypr/index.md", "docs/calypr/quick-start.md", "docs/calypr/troubleshooting.md"}:
        personas = ["data-steward", "platform-engineer", "security-compliance-reviewer"]
    elif rel.startswith("docs/tools/git-drs/"):
        personas = ["data-steward", "platform-engineer", "security-compliance-reviewer"]
    elif rel.startswith("docs/tools/funnel/"):
        personas = ["workflow-engineer", "platform-engineer"]
    elif rel.startswith("docs/tools/forge/"):
        personas = ["data-steward", "platform-engineer", "standards-architecture-lead"]
    elif rel.startswith("docs/tools/grip/"):
        personas = ["standards-architecture-lead", "researcher-bioinformatician", "platform-engineer"]
    elif rel.startswith("docs/tools/data-client/"):
        personas = ["data-steward", "platform-engineer", "security-compliance-reviewer"]
    elif rel.startswith("docs/tools/sifter/"):
        personas = ["workflow-engineer", "data-steward", "platform-engineer", "standards-architecture-lead"]
    elif rel == "docs/tools/index.md":
        personas = ["platform-engineer", "workflow-engineer", "standards-architecture-lead", "data-steward"]
    else:
        personas = []
        low = (rel + "\n" + body).lower()
        if any(k in low for k in ("troubleshooting", "authentication", "admin", "access_requests", "approve-requests", "add-users")):
            personas.append("security-compliance-reviewer")
        if any(k in low for k in ("workflow", "task", "tes", "compute", "execution")):
            personas.append("workflow-engineer")
        if any(k in low for k in ("analysis", "query", "benchmark", "model")):
            personas.append("researcher-bioinformatician")
        personas.append("platform-engineer")

    for sol in solutions:
        if sol == "manage-data":
            personas.extend(["data-steward", "platform-engineer"])
        elif sol == "manage-compute":
            personas.extend(["workflow-engineer", "platform-engineer"])
        elif sol == "integrate-data":
            personas.extend(["data-steward", "standards-architecture-lead", "platform-engineer"])
        elif sol == "manage-models":
            personas.extend(["researcher-bioinformatician", "workflow-engineer", "standards-architecture-lead"])

    return dedupe_in_order(personas, PERSONA_ORDER)


def rewrite_front_matter(existing_fm: str, lead: str, personas, solutions, related_tools):
    lines = existing_fm.splitlines()
    cleaned: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        match = re.match(r"^([A-Za-z0-9_-]+):", line)
        if match and match.group(1) in TARGETED_FRONT_MATTER_KEYS:
            i += 1
            while i < len(lines) and not re.match(r"^[A-Za-z0-9_-]+:", lines[i]):
                i += 1
            continue
        cleaned.append(line)
        i += 1

    extras = [
        f"lead: {json.dumps(lead)}",
        "personas:",
        *[f"  - {p}" for p in personas],
        "solutions:",
        *[f"  - {s}" for s in solutions],
        "related_tools:",
        *[f"  - {t}" for t in related_tools],
    ]
    return "\n".join(cleaned + extras)


changed = []
for path in [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and ".generated" not in p.parts and "site" not in p.parts]:
    text = path.read_text(encoding="utf-8")
    existing_fm, body = strip_front_matter(text)
    lead = extract_lead(body)
    solutions = infer_solutions(path, body)
    personas = infer_personas(path, body, solutions)
    related_tools = infer_related_tools(path, body)

    if existing_fm is None:
        front_matter = [
            "---",
            f"lead: {json.dumps(lead)}",
            "personas:",
            *[f"  - {p}" for p in personas],
            "solutions:",
            *[f"  - {s}" for s in solutions],
            "related_tools:",
            *[f"  - {t}" for t in related_tools],
            "---",
            "",
        ]
        new_text = "\n".join(front_matter) + body.lstrip("\n")
    else:
        new_fm = rewrite_front_matter(existing_fm, lead, personas, solutions, related_tools)
        if new_fm == existing_fm:
            continue
        new_text = "---\n" + new_fm + "\n---\n" + body

    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        changed.append(relpath(path))

print(f"changed {len(changed)} files")
for rel in changed[:80]:
    print(rel)
if len(changed) > 80:
    print("...")

