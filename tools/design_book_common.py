from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

import yaml


REQUIRED_TOPICS = [
    "philosophy",
    "constructive-signal",
    "quiet-modular",
    "expression-levels",
    "semantic-color",
    "typography",
    "visual-grammar",
    "components",
    "recipes",
    "prompt-dsl-v0.5",
    "analytical-mode-v0.1",
    "accessibility",
    "reference-hierarchy",
    "provenance",
    "why-do-dont",
    "publishing-preflight",
]

MACRO_PATTERN = re.compile(r"\{\{([^{}]+)\}\}")
UKRAINIAN_PATTERN = re.compile(r"[А-Яа-яІіЇїЄєҐґ]")


def repository_root(book_root: Path) -> Path:
    return book_root.resolve().parents[1]


def load_yaml(path: Path) -> dict[str, Any]:
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict):
        raise ValueError(f"expected YAML mapping: {path}")
    return document


def dump_yaml(value: Any) -> str:
    return yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=120)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def parse_page_text(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("page must begin with YAML front matter")
    try:
        front, body = text[4:].split("\n---\n", 1)
    except ValueError as error:
        raise ValueError("page front matter must end with ---") from error
    metadata = yaml.safe_load(front)
    if not isinstance(metadata, dict):
        raise ValueError("page front matter must be a mapping")
    return metadata, body.strip() + "\n"


def parse_page(path: Path) -> tuple[dict[str, Any], str]:
    return parse_page_text(path.read_text(encoding="utf-8"))


def _normalize_id(value: Any, width: int) -> str:
    return str(value).zfill(width)


def _component_catalog(argument: str, repository: Path) -> str:
    start_text, end_text = argument.split("-", 1)
    start, end = int(start_text), int(end_text)
    manifest = load_yaml(repository / "components/component-library-v0.1/manifest.yaml")
    lines: list[str] = []
    for item in manifest["components"]:
        identifier = int(item["id"])
        if start <= identifier <= end:
            lines.extend(
                [
                    f"## {_normalize_id(item['id'], 2)} · `{item['name']}`",
                    f"**Purpose.** {item['purpose']}",
                    f"**Meaning.** {item['semantic_meaning']}",
                    "",
                ]
            )
    return "\n".join(lines).rstrip()


def _ingredient_summary(record: dict[str, Any]) -> str:
    values = []
    for status in ("required", "optional"):
        for item in record["ingredients"].get(status, []):
            minimum, maximum = item["min"], item["max"]
            count = str(minimum) if minimum == maximum else f"{minimum}–{maximum}"
            suffix = " optional" if status == "optional" else ""
            values.append(f"`{item['component']}` × {count}{suffix}")
    return "; ".join(values)


def _level_summary(record: dict[str, Any]) -> str:
    labels = {"allowed": "yes", "conditional": "conditional", "forbidden": "no"}
    return " · ".join(
        f"{level}: {labels[data['status']]}"
        for level, data in record["expression_levels"].items()
    )


def _recipe_catalog(argument: str, repository: Path) -> str:
    start_text, end_text = argument.split("-", 1)
    start, end = int(start_text), int(end_text)
    root = repository / "recipes/recipe-library-v0.5"
    manifest = load_yaml(root / "manifest.yaml")
    lines: list[str] = []
    for item in manifest["recipes"]:
        identifier = int(item["id"])
        if start <= identifier <= end:
            record = load_yaml(root / item["record"])
            lines.extend(
                [
                    f"## {_normalize_id(item['id'], 3)} · `{item['name']}`",
                    f"{record['problem']}",
                    f"**Ingredients.** {_ingredient_summary(record)}",
                    f"**Levels.** {_level_summary(record)}",
                    "",
                ]
            )
    return "\n".join(lines).rstrip()


def _semantic_tokens(repository: Path) -> str:
    contract = load_yaml(repository / "accessibility/night-mode-v0.1/contracts/tokens.yaml")
    lines = ["| Profile | Background | Ink | Primary signal | Text / non-text |", "|---|---|---|---|---|"]
    for name, profile in contract["profiles"].items():
        tokens = profile["tokens"]
        thresholds = profile["thresholds"]
        lines.append(
            f"| `{name}` | `{tokens['background.base']}` | `{tokens['ink.primary']}` | "
            f"`{tokens['signal.primary']}` | {thresholds['text']}:1 / {thresholds['non_text']}:1 |"
        )
    return "\n".join(lines)


def _prompt_dsl_fields(repository: Path) -> str:
    schema = load_yaml(repository / "recipes/recipe-library-v0.5/prompt-dsl-v0.5.schema.yaml")
    lines = ["| Field | Contract |", "|---|---|"]
    descriptions = {
        "language": "exactly CSDL",
        "version": "exactly 0.5",
        "kind": "generation-package",
        "id": "stable package identity",
        "recipe": "id, slug, version",
        "semantic_intent": "problem, scenario, main_idea, mechanism",
        "content": "source and exact bindings",
        "component_instances": "D-029 components only",
        "relations": "declared subject, type, object",
        "generation_constraints": "expression through hard exclusions",
        "provenance": "recipe evidence and source outline",
    }
    for field in schema["required_package_fields"]:
        lines.append(f"| `{field}` | {descriptions[field]} |")
    return "\n".join(lines)


def _flow(value: Any) -> str:
    return yaml.safe_dump(value, default_flow_style=True, allow_unicode=True, width=1000).strip()


def _prompt_dsl_example(repository: Path) -> str:
    package = load_yaml(repository / "recipes/recipe-library-v0.5/proofs/packages/01-editorial.yaml")
    lines = [
        "```yaml",
        f"language: {package['language']}",
        f"version: '{package['version']}'",
        f"kind: {package['kind']}",
        f"id: {package['id']}",
        f"recipe: {_flow(package['recipe'])}",
        f"semantic_intent: {_flow(package['semantic_intent'])}",
        "content:",
        f"  source: {package['content']['source']}",
        f"  bindings: {_flow(package['content']['bindings'])}",
        "component_instances:",
    ]
    lines.extend(f"  - {_flow(item)}" for item in package["component_instances"])
    lines.append("relations:")
    lines.extend(f"  - {_flow(item)}" for item in package["relations"])
    constraints = package["generation_constraints"]
    lines.extend(
        [
            "generation_constraints:",
            f"  expression: {constraints['expression']}",
            f"  density: {constraints['density']}",
            f"  canvas: {_flow(constraints['canvas'])}",
            f"  presentation: {_flow(constraints['presentation'])}",
            f"  typography: {_flow(constraints['typography'])}",
            f"  palette: {_flow(constraints['palette'])}",
            f"  output: {_flow(constraints['output'])}",
            f"  hard_exclusions: {_flow(constraints['hard_exclusions'])}",
            f"provenance: {_flow(package['provenance'])}",
            "```",
        ]
    )
    return "\n".join(lines)


def _analytical_families(repository: Path) -> str:
    contract = load_yaml(repository / "analytics/analytical-mode-v0.1/contracts/families.yaml")
    lines = ["| Family | Owning precision rule |", "|---|---|"]
    for name, family in contract["families"].items():
        lines.append(f"| `{name}` | {family['precise_rules'][0]} |")
    return "\n".join(lines)


def _accessibility_profiles(repository: Path) -> str:
    contract = load_yaml(repository / "accessibility/night-mode-v0.1/contracts/tokens.yaml")
    lines: list[str] = []
    for name, profile in contract["profiles"].items():
        lines.extend([f"## `{name}`", profile["description"], ""])
    return "\n".join(lines).rstrip()


def _reference_hierarchy(repository: Path) -> str:
    authority = load_yaml(repository / "patterns/visual-dna-sprint-01/visual-authority.yaml")
    lines = ["## Primary visual authority"]
    for index, item in enumerate(authority["primary_visual_authority"], 1):
        lines.append(f"{index}. `{item['path']}` — {item['role']}.")
    lines.append("\n## Secondary execution reference")
    for item in authority["secondary_execution_reference"]:
        lines.append(f"- `{item['path']}` — {item['role']}.")
    return "\n".join(lines)


def expand_macros(body: str, repository: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        expression = match.group(1)
        if expression.startswith("component_catalog:"):
            return _component_catalog(expression.split(":", 1)[1], repository)
        if expression.startswith("recipe_catalog:"):
            return _recipe_catalog(expression.split(":", 1)[1], repository)
        if expression == "semantic_tokens":
            return _semantic_tokens(repository)
        if expression == "prompt_dsl_fields":
            return _prompt_dsl_fields(repository)
        if expression == "prompt_dsl_example:01-editorial":
            return _prompt_dsl_example(repository)
        if expression == "analytical_families":
            return _analytical_families(repository)
        if expression == "accessibility_profiles":
            return _accessibility_profiles(repository)
        if expression == "reference_hierarchy":
            return _reference_hierarchy(repository)
        raise ValueError(f"unknown publication macro: {expression}")

    return MACRO_PATTERN.sub(replace, body)


def strip_inline_markdown(value: str) -> str:
    value = re.sub(r"!\[([^]]*)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    value = value.replace("**", "").replace("__", "").replace("`", "")
    return value.strip()


def markdown_to_plain_text(markdown: str) -> str:
    lines: list[str] = []
    in_code = False
    for raw in markdown.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            in_code = not in_code
            continue
        if not line:
            if lines and lines[-1] != "":
                lines.append("")
            continue
        if not in_code and re.match(r"^\|?\s*:?-{3,}", line):
            continue
        if not in_code and line.startswith("|"):
            cells = [strip_inline_markdown(cell) for cell in line.strip("|").split("|")]
            lines.append(" · ".join(cell for cell in cells if cell))
            continue
        line = re.sub(r"^#{1,6}\s+", "", line)
        line = re.sub(r"^[-*]\s+", "• ", line)
        lines.append(strip_inline_markdown(line))
    return "\n".join(lines).strip() + "\n"


def build_page_documents(book_root: Path) -> list[dict[str, Any]]:
    repository = repository_root(book_root)
    manifest = load_yaml(book_root / "manifest.yaml")
    documents: list[dict[str, Any]] = []
    for page in manifest["pages"]:
        source_path = book_root / page["source"]
        metadata, body = parse_page(source_path)
        expanded = expand_macros(body, repository)
        documents.append(
            {
                **page,
                "metadata": metadata,
                "body": body,
                "expanded_markdown": expanded,
                "plain_text": markdown_to_plain_text(expanded),
                "source_sha256": sha256_file(source_path),
                "expanded_sha256": sha256_bytes(expanded.encode("utf-8")),
            }
        )
    return documents


def derive_index(book_root: Path, documents: list[dict[str, Any]]) -> dict[str, Any]:
    manifest = load_yaml(book_root / "manifest.yaml")
    repository = repository_root(book_root)
    component_manifest = load_yaml(repository / manifest["publication"]["component_manifest"])
    recipe_manifest = load_yaml(repository / manifest["publication"]["recipe_manifest"])
    return {
        "publication": manifest["publication"]["id"],
        "version": manifest["publication"]["version"],
        "page_count": len(documents),
        "format": manifest["publication"]["format"]["name"],
        "editorial_language": manifest["publication"]["editorial_language"],
        "terminology_language": manifest["publication"]["terminology_language"],
        "component_count": len(component_manifest["components"]),
        "recipe_count": len(recipe_manifest["recipes"]),
        "pages": [
            {
                "id": document["id"],
                "source": document["source"],
                "section": document["section"],
                "kind": document["kind"],
                "title_uk": document["metadata"]["title_uk"],
                "source_sha256": document["source_sha256"],
                "expanded_sha256": document["expanded_sha256"],
            }
            for document in documents
        ],
    }


def assemble_markdown(book_root: Path, documents: list[dict[str, Any]]) -> str:
    manifest = load_yaml(book_root / "manifest.yaml")
    lines = [
        "---",
        f"title: {manifest['publication']['title']}",
        f"version: {manifest['publication']['version']}",
        f"page_count: {len(documents)}",
        "generated: true",
        "canonical_sources: pages/*.md",
        "---",
        "",
    ]
    for index, document in enumerate(documents):
        if index:
            lines.extend(["", "<!-- page-break -->", ""])
        lines.append(f"<!-- page {document['id']} · source {document['source']} -->")
        lines.append(document["expanded_markdown"].rstrip())
    return "\n".join(lines).rstrip() + "\n"
