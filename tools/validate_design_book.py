from __future__ import annotations

from copy import deepcopy
import re
import sys
from pathlib import Path
from typing import Any

from PIL import Image

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.design_book_common import (
    MACRO_PATTERN,
    REQUIRED_TOPICS,
    UKRAINIAN_PATTERN,
    build_page_documents,
    load_yaml,
    parse_page,
    repository_root,
    sha256_file,
)
from tools.validate_prompt_dsl import validate_prompt_package


def _normalize_recipe_id(value: Any) -> str:
    return str(value).zfill(3)


def _load_state(book_root: Path) -> dict[str, Any]:
    repository = repository_root(book_root)
    manifest = load_yaml(book_root / "manifest.yaml")
    pages: dict[str, dict[str, Any]] = {}
    for item in manifest.get("pages", []):
        path = book_root / item["source"]
        if path.is_file():
            metadata, body = parse_page(path)
            pages[str(item["id"]).zfill(2)] = {"metadata": metadata, "body": body}
    inventory_path = repository / manifest["publication"]["accepted_raster_inventory"]
    report_path = book_root / manifest["publication"]["build"]["report"]
    return {
        "manifest": manifest,
        "terminology": load_yaml(book_root / "terminology.yaml"),
        "provenance": load_yaml(book_root / "provenance.yaml"),
        "raster_inventory": load_yaml(inventory_path),
        "pages": pages,
        "build_report": load_yaml(report_path)
        if report_path.is_file()
        else {
            "deterministic": True,
            "overflow_pages": [],
            "missing_glyph_pages": [],
            "contrast_checks": {"text": {"passes": True}},
        },
    }


def _validate_state(book_root: Path, state: dict[str, Any], check_report: bool) -> list[str]:
    errors: list[str] = []
    repository = repository_root(book_root)
    manifest = state["manifest"]
    publication = manifest.get("publication", {})
    pages = manifest.get("pages", [])
    declared_count = publication.get("page_count")

    if not isinstance(declared_count, int) or not 25 <= declared_count <= 40:
        errors.append("publication page_count must be between 25 and 40")
    if declared_count != len(pages):
        errors.append("publication page_count must match manifest pages")
    expected_ids = [f"{index:02d}" for index in range(1, len(pages) + 1)]
    actual_ids = [str(page.get("id", "")).zfill(2) for page in pages]
    if actual_ids != expected_ids:
        errors.append("publication page ids must be sequential and ordered")
    if publication.get("editorial_language") != "uk" or publication.get("terminology_language") != "en":
        errors.append("publication bilingual language contract must be uk editorial and en terminology")
    if publication.get("public_release") is not False:
        errors.append("publication must not claim a public release")
    format_contract = publication.get("format", {})
    if (format_contract.get("width_mm"), format_contract.get("height_mm")) != (297, 210):
        errors.append("publication format must remain ISO A4 landscape")

    declared_topics = manifest.get("required_topics", [])
    for topic in REQUIRED_TOPICS:
        if topic not in declared_topics:
            errors.append(f"required topic missing: {topic}")
    covered_topics = {topic for page in pages for topic in page.get("topics", [])}
    for topic in REQUIRED_TOPICS:
        if topic not in covered_topics:
            errors.append(f"required topic has no page coverage: {topic}")

    state_pages = state["pages"]
    for item in pages:
        page_id = str(item.get("id", "")).zfill(2)
        source = book_root / item.get("source", "")
        if not source.is_file():
            errors.append(f"publication page source does not exist: {item.get('source')}")
            continue
        document = state_pages.get(page_id)
        if not document:
            errors.append(f"publication page {page_id} cannot be parsed")
            continue
        metadata, body = document["metadata"], document["body"]
        if str(metadata.get("id", "")).zfill(2) != page_id:
            errors.append(f"page {page_id} front matter id must match manifest")
        if metadata.get("editorial_language") != "uk":
            errors.append(f"page {page_id} must declare Ukrainian editorial language")
        if metadata.get("terminology_language") != "en":
            errors.append(f"page {page_id} must declare English terminology language")
        if not UKRAINIAN_PATTERN.search(body):
            errors.append(f"page {page_id} must contain Ukrainian editorial content")
        if "{{" in body and "}}" not in body:
            errors.append(f"page {page_id} contains a malformed publication macro")

    terminology = state["terminology"]
    component_manifest = load_yaml(repository / publication["component_manifest"])
    expected_components = [item["name"] for item in component_manifest["components"]]
    actual_components = [item.get("name") for item in terminology.get("components", [])]
    if actual_components != expected_components or len(actual_components) != 15:
        errors.append("terminology component registry must match D-029 exactly")
    recipe_manifest = load_yaml(repository / publication["recipe_manifest"])
    expected_recipes = [(_normalize_recipe_id(item["id"]), item["name"]) for item in recipe_manifest["recipes"]]
    actual_recipes = [(_normalize_recipe_id(item.get("id")), item.get("name")) for item in terminology.get("recipes", [])]
    if actual_recipes != expected_recipes or len(actual_recipes) != 23:
        errors.append("terminology recipe registry must match D-030 exactly")
    prompt_schema = load_yaml(repository / publication["prompt_dsl_schema"])
    if terminology.get("prompt_dsl_package_fields") != prompt_schema["allowed_package_fields"]:
        errors.append("Prompt DSL package fields must match v0.5 exactly")
    if terminology.get("registry", {}).get("canonical_identifiers_are_translated") is not False:
        errors.append("canonical identifiers must not be translated")
    if terminology.get("retired_or_forbidden_public_names") != ["Container"]:
        errors.append("retired Container alias must remain outside public vocabulary")

    provenance = state["provenance"]
    allowed_classes = set(provenance.get("provenance", {}).get("claim_classes", []))
    if set(provenance.get("pages", {})) != set(expected_ids):
        errors.append("provenance must cover every publication page exactly once")
    for entries in provenance.get("pages", {}).values():
        for entry in entries:
            path = repository / entry.get("path", "")
            if not path.is_file():
                errors.append(f"provenance source does not exist: {entry.get('path')}")
            if entry.get("class") not in allowed_classes:
                errors.append("provenance claim class must be declared")

    inventory = state["raster_inventory"]
    if inventory.get("file_count") != 60 or len(inventory.get("files", [])) != 60:
        errors.append("accepted raster inventory must contain exactly 60 files")
    for item in inventory.get("files", []):
        path = repository / item.get("path", "")
        if not path.is_file() or sha256_file(path) != item.get("sha256"):
            errors.append("accepted raster hash changed")
            break

    analytical = load_yaml(repository / publication["analytical_manifest"])
    if analytical["library"].get("prompt_dsl_compatibility") != "0.5":
        errors.append("Analytical Mode must preserve Prompt DSL v0.5")
    if analytical["library"].get("public_component_count") != 15 or analytical["library"].get("public_recipe_count") != 23:
        errors.append("Analytical Mode must preserve public vocabulary counts")
    if len(analytical.get("family_order", [])) != 10:
        errors.append("Analytical Mode must retain ten families")
    accessibility = load_yaml(repository / publication["accessibility_manifest"])
    if accessibility.get("profile_order") != ["light", "night", "monochrome", "projector"]:
        errors.append("Accessibility v0.1 must retain four canonical profiles")
    if accessibility["library"].get("prompt_dsl_compatibility") != "0.5":
        errors.append("Accessibility v0.1 must preserve Prompt DSL v0.5")

    prompt_path = repository / "recipes/recipe-library-v0.5/proofs/packages/01-editorial.yaml"
    prompt_errors = validate_prompt_package(
        prompt_path, repository / "recipes/recipe-library-v0.5", require_complete=False
    )
    if prompt_errors:
        errors.append("complete Prompt DSL example must validate against v0.5")

    if check_report:
        report = state["build_report"]
        if report.get("deterministic") is not True:
            errors.append("publication build must be deterministic")
        if report.get("overflow_pages"):
            errors.append("publication contains clipped or overflowing content")
        if report.get("missing_glyph_pages"):
            errors.append("publication contains missing glyphs")
        if any(not check.get("passes") for check in report.get("contrast_checks", {}).values()):
            errors.append("publication text contrast must pass")
    return errors


def validate_design_book(book_root: Path, require_outputs: bool = True) -> list[str]:
    book_root = book_root.resolve()
    state = _load_state(book_root)
    errors = _validate_state(book_root, state, check_report=require_outputs)
    if errors or not require_outputs:
        if not errors:
            try:
                documents = build_page_documents(book_root)
                expanded = "\n".join(document["expanded_markdown"] for document in documents)
                if MACRO_PATTERN.search(expanded):
                    errors.append("publication contains unresolved macros")
            except (KeyError, ValueError) as error:
                errors.append(str(error))
        return errors

    manifest = state["manifest"]
    publication = manifest["publication"]
    build = publication["build"]
    required_paths = [
        book_root / build["assembled_markdown"],
        book_root / build["index"],
        book_root / build["pdf"],
        book_root / build["contact_sheet"],
        book_root / build["extracted_text"],
        book_root / build["report"],
    ]
    for path in required_paths:
        if not path.is_file():
            errors.append(f"publication output missing: {path.relative_to(book_root)}")
    if errors:
        return errors

    page_paths = sorted((book_root / "output/pages").glob("*.png"))
    grayscale_paths = sorted((book_root / "output/grayscale").glob("*.png"))
    if len(page_paths) != publication["page_count"] or len(grayscale_paths) != publication["page_count"]:
        errors.append("publication must render every page in color and grayscale")
    expected_size = (publication["format"]["render_width_px"], publication["format"]["render_height_px"])
    for path in page_paths + grayscale_paths:
        with Image.open(path) as image:
            if image.size != expected_size or image.mode != "RGB":
                errors.append("publication page render dimensions or color mode are invalid")
                break
    with Image.open(book_root / build["contact_sheet"]) as contact:
        if contact.size != (3840, 2160) or contact.mode != "RGB":
            errors.append("publication contact sheet must be 3840x2160 RGB")

    pdf = (book_root / build["pdf"]).read_bytes()
    if not pdf.startswith(b"%PDF-1.7"):
        errors.append("publication PDF header is invalid")
    if len(re.findall(rb"/Type /Page\b", pdf)) != publication["page_count"]:
        errors.append("publication PDF page count must match manifest")
    if b"/ToUnicode" not in pdf or b"/Lang (uk-UA)" not in pdf or b"3 Tr" not in pdf:
        errors.append("publication PDF must contain an ordered Unicode text layer")

    report = state["build_report"]
    if report.get("page_count") != publication["page_count"]:
        errors.append("publication build report page count must match manifest")
    if report.get("accepted_raster_count") != 60 or report.get("accepted_raster_mismatches") != []:
        errors.append("publication build report must preserve all accepted rasters")
    if report.get("generated_raster_authority") is not False:
        errors.append("publication review renders must not become raster authority")
    if report.get("public_release") is not False:
        errors.append("publication build report must not claim a public release")
    if report.get("pdf_sha256") != sha256_file(book_root / build["pdf"]):
        errors.append("publication PDF digest must match build report")
    if report.get("contact_sheet_sha256") != sha256_file(book_root / build["contact_sheet"]):
        errors.append("publication contact-sheet digest must match build report")
    extracted = (book_root / build["extracted_text"]).read_text(encoding="utf-8")
    for page_id in [f"{index:02d}" for index in range(1, publication["page_count"] + 1)]:
        if f"PAGE {page_id}\n" not in extracted:
            errors.append("publication extracted text must preserve page reading order")
            break
    assembled = (book_root / build["assembled_markdown"]).read_text(encoding="utf-8")
    if MACRO_PATTERN.search(assembled):
        errors.append("generated publication Markdown contains unresolved macros")
    return errors


def _set_path(document: Any, path: list[Any], value: Any) -> None:
    target = document
    for part in path[:-1]:
        target = target[part]
    target[path[-1]] = value


def validate_negative_fixture(fixture_path: Path, book_root: Path) -> str:
    state = _load_state(book_root.resolve())
    fixture = load_yaml(fixture_path)
    mutation = fixture["mutation"]
    document_name = mutation["document"]
    if document_name.startswith("page:"):
        document = state["pages"][document_name.split(":", 1)[1]]
    else:
        document = state[document_name]
    _set_path(document, mutation["path"], deepcopy(mutation["value"]))
    errors = _validate_state(book_root.resolve(), state, check_report=True)
    if not errors:
        raise AssertionError(f"negative fixture produced no error: {fixture_path}")
    return errors[0]


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_design_book.py <book-root>", file=sys.stderr)
        return 2
    errors = validate_design_book(Path(sys.argv[1]), require_outputs=True)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("design book valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
