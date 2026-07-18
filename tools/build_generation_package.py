from __future__ import annotations

import copy
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.select_recipe import select_recipe


SIGNAL_TOKENS = {
    "coral": "signal.primary",
    "data_blue": "signal.data",
    "ochre": "signal.attention",
    "mineral_green": "signal.positive",
}


def _instance_id(component: str, index: int, count: int) -> str:
    base = component.casefold().replace(" ", "-")
    return base if count == 1 else f"{base}-{index}"


def _instance_content(
    bindings: dict[str, Any], component: str, index: int
) -> dict[str, Any]:
    list_fields = [
        (field, value) for field, value in bindings.items() if isinstance(value, list)
    ]
    if component in {"Node", "Label"} and list_fields:
        field, values = list_fields[0]
        if values:
            return {"binding": field, "index": min(index - 1, len(values) - 1)}
    field = next(iter(bindings), "main_idea")
    return {"binding": field}


def _build_instances(
    recipe: dict[str, Any], bindings: dict[str, Any]
) -> tuple[list[dict[str, Any]], dict[str, list[str]]]:
    instances = []
    by_component: dict[str, list[str]] = defaultdict(list)
    for group in ("required", "optional"):
        for ingredient in recipe["ingredients"][group]:
            count = ingredient["default"]
            for index in range(1, count + 1):
                instance_id = _instance_id(ingredient["component"], index, count)
                by_component[ingredient["component"]].append(instance_id)
                role = (
                    "dominant"
                    if ingredient["component"] == "Signal"
                    else "primary"
                    if ingredient["component"] == "Anchor" and index == 1
                    else "peer"
                    if ingredient["component"] == "Anchor"
                    else ingredient["component"].casefold()
                )
                instances.append(
                    {
                        "id": instance_id,
                        "component": ingredient["component"],
                        "role": role,
                        "content": _instance_content(
                            bindings, ingredient["component"], index
                        ),
                    }
                )
    _attach_component_attributes(instances, by_component, recipe, bindings)
    return instances, by_component


def _content_ref(bindings: dict[str, Any], *preferred: str) -> str:
    field = next((field for field in preferred if field in bindings), next(iter(bindings)))
    return f"content.{field}"


def _attach_component_attributes(
    instances: list[dict[str, Any]],
    by_component: dict[str, list[str]],
    recipe: dict[str, Any],
    bindings: dict[str, Any],
) -> None:
    label_targets = (
        by_component["Node"]
        or by_component["Pulse"]
        or by_component["Axis"]
        or by_component["Anchor"]
    )
    directional_targets = by_component["Node"] or by_component["Field"]
    signal_targets = (
        by_component["Node"]
        or by_component["Pulse"]
        or by_component["Anchor"]
        or by_component["Field"]
        or by_component["Vector"]
        or by_component["Label"]
        or by_component["Frame"]
        or by_component["Axis"]
    )
    axis_modes = {
        "timeline": ["sequence"],
        "matrix": ["coordinate", "coordinate"],
        "kpi": ["support"],
        "table": ["lookup", "lookup"],
        "chart": ["sequence", "quantitative"],
        "dashboard": ["support", "sequence"],
    }
    quantitative = bindings.get("quantitative_contract", {})
    counters: dict[str, int] = defaultdict(int)
    for instance in instances:
        component = instance["component"]
        index = counters[component]
        counters[component] += 1
        attributes: dict[str, Any] = {}
        if component == "Signal" and signal_targets:
            attributes["target"] = signal_targets[-1]
        elif component == "Frame":
            attributes["scope"] = recipe["slug"]
        elif component == "Cluster":
            attributes["members"] = by_component["Node"] or by_component["Pulse"]
        elif component == "Vector" and directional_targets:
            attributes["source"] = directional_targets[min(index, len(directional_targets) - 1)]
            attributes["target"] = directional_targets[
                min(index + 1, len(directional_targets) - 1)
            ]
        elif component == "Divider":
            attributes["subjects"] = (by_component["Field"] or by_component["Anchor"])[:2]
        elif component == "Loop":
            attributes.update(
                {"members": by_component["Node"], "direction": "clockwise", "closed": True}
            )
        elif component == "Collision":
            attributes.update(
                {
                    "inputs": by_component["Anchor"][:2],
                    "result": _content_ref(bindings, "result", "supporting_copy"),
                }
            )
        elif component == "Bridge" and len(by_component["Node"]) >= 2:
            attributes.update(
                {
                    "source": by_component["Node"][min(index, len(by_component["Node"]) - 2)],
                    "target": by_component["Node"][min(index + 1, len(by_component["Node"]) - 1)],
                }
            )
        elif component == "Axis":
            modes = axis_modes.get(recipe["source_family"], ["sequence"])
            attributes.update(
                {
                    "mode": modes[min(index, len(modes) - 1)],
                    "direction": recipe["prompt_dsl"]["deterministic_defaults"][
                        "reading_path"
                    ],
                }
            )
            if quantitative:
                if attributes["mode"] == "sequence":
                    attributes["order"] = quantitative["order"]
                if attributes["mode"] == "quantitative":
                    attributes["domain"] = quantitative["domain"]
                    attributes["unit"] = quantitative["unit"]
        elif component == "Node" and quantitative:
            attributes.update(
                {
                    "value": quantitative["values"][index],
                    "unit": quantitative["unit"],
                    "period": quantitative["order"][index],
                }
            )
        elif component == "Pulse":
            attributes.update(
                {
                    "value": _content_ref(bindings, "value", "primary", "metrics"),
                    "label": by_component["Label"][0]
                    if by_component["Label"]
                    else _content_ref(bindings, "label", "headline"),
                }
            )
        elif component == "Label" and label_targets:
            attributes.update(
                {
                    "text": instance["content"],
                    "target": label_targets[min(index, len(label_targets) - 1)],
                }
            )
        elif component == "Legend":
            attributes.update(
                {
                    "items": [],
                    "reason_direct_labels_fail": "direct labels collide in the declared bounded analytical proof",
                }
            )
        if attributes:
            instance["attributes"] = attributes


def _expand_relation(
    template: dict[str, str], by_component: dict[str, list[str]]
) -> list[dict[str, str]]:
    subjects = by_component[template["subject"]]
    objects = by_component[template["object"]]
    if not subjects or not objects:
        return []
    relation_type = template["type"]
    if relation_type == "highlights":
        pairs = [(subjects[0], objects[-1])]
    elif len(subjects) == 1:
        pairs = [(subjects[0], object_id) for object_id in objects]
    elif len(objects) == 1:
        pairs = [(subject_id, objects[0]) for subject_id in subjects]
    else:
        pairs = list(zip(subjects, objects, strict=False))
    return [
        {"subject": subject, "type": relation_type, "object": object_}
        for subject, object_ in pairs
    ]


def build_generation_package(
    outline: dict[str, Any], root: Path
) -> dict[str, Any]:
    recipe = select_recipe(outline, root)
    schema = yaml.safe_load(
        (root / "prompt-dsl-v0.5.schema.yaml").read_text(encoding="utf-8")
    )
    defaults = copy.deepcopy(schema["defaults"])
    bindings = copy.deepcopy(outline.get("content", {}))
    if not isinstance(bindings, dict) or not bindings:
        raise ValueError("outline content must be a non-empty mapping")
    instances, by_component = _build_instances(recipe, bindings)
    relations = [
        relation
        for template in recipe["relations"]["allowed"]
        for relation in _expand_relation(template, by_component)
    ]
    recipe_defaults = recipe["prompt_dsl"]["deterministic_defaults"]
    expression = outline.get("expression", recipe_defaults["expression"])
    density = outline.get("density", recipe_defaults["density"])
    presentation = copy.deepcopy(defaults["presentation"])
    presentation["reading_path"] = recipe_defaults["reading_path"]
    presentation["negative_space_percent"] = copy.deepcopy(
        recipe["presentation"]["negative_space_percent"]
    )
    palette = copy.deepcopy(defaults["palette"])
    palette["primary_signal"] = SIGNAL_TOKENS[
        recipe["semantic_color"]["dominant_signal"]
    ]
    provenance: dict[str, Any] = {
        "recipe_evidence": recipe["specification"],
        "source_outline": str(outline.get("source_outline", outline.get("id", "inline"))),
    }
    if recipe["content_contract"]["data_contract"] != "none":
        provenance["dataset"] = recipe["content_contract"]["data_contract"]
    return {
        "language": "CSDL",
        "version": "0.5",
        "kind": "generation-package",
        "id": outline["id"],
        "recipe": {
            "id": recipe["id"],
            "slug": recipe["slug"],
            "version": recipe["version"],
        },
        "semantic_intent": {
            "problem": recipe["problem"],
            "scenario": outline["scenario"],
            "main_idea": outline["main_idea"],
            "mechanism": recipe["prompt_dsl"]["semantic_intent"],
        },
        "content": {
            "source": str(outline.get("content_source", "inline")),
            "bindings": bindings,
        },
        "component_instances": instances,
        "relations": relations,
        "generation_constraints": {
            "expression": expression,
            "density": density,
            "canvas": copy.deepcopy(defaults["canvas"]),
            "presentation": presentation,
            "typography": copy.deepcopy(defaults["typography"]),
            "palette": palette,
            "output": copy.deepcopy(defaults["output"]),
            "hard_exclusions": copy.deepcopy(recipe["hard_exclusions"]),
        },
        "provenance": provenance,
    }


def main() -> int:
    if len(sys.argv) != 4:
        print(
            "usage: python tools/build_generation_package.py "
            "OUTLINE RECIPE_LIBRARY_ROOT OUTPUT"
        )
        return 2
    try:
        outline = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8"))
        package = build_generation_package(outline, Path(sys.argv[2]))
        Path(sys.argv[3]).write_text(
            yaml.safe_dump(package, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )
    except (KeyError, OSError, ValueError, yaml.YAMLError) as error:
        print(f"ERROR: {error}")
        return 1
    print(f"generation package built: {sys.argv[3]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
