#!/usr/bin/env python3
"""Generate and verify exhaustive TOML examples from ``config.schema.json``.

This generator is intentionally self-contained under ``generate/``. It reads
only ``generate/schemas/`` and may write only ``generate/examples/``. Each
canonical setting receives one schema-valid representative value, while
deprecated aliases and finite alternatives that cannot coexist in one TOML
document remain comment-only. A machine-readable coverage ledger at the end of
the reference makes schema drift a check failure instead of a documentation
omission.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import re
import sys
import tomllib
from pathlib import Path
from typing import Any, Iterable


GENERATION_ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIRECTORY = GENERATION_ROOT / "schemas"
SCHEMA_PATH = SCHEMAS_DIRECTORY / "config.schema.json"
EXAMPLES_DIRECTORY = GENERATION_ROOT / "examples"
HOME_EXAMPLE_PATH = EXAMPLES_DIRECTORY / "config.home.toml"
AGENT_ROLE_EXAMPLE_PATH = EXAMPLES_DIRECTORY / "agent-role.toml"

DEFINITION_MARKER = "# schema-definition: "
ENTRY_MARKER = "# schema-entry: "
VARIANT_MARKER = "# schema-variant: "
OPTION_MARKER = "# schema-options: "
FINITE_OPTION_MARKER = "# schema-finite-option: "
EXAMPLE_MARKER = "# schema-example: "
_OMIT = object()

DEPRECATED_ROOT_ALIASES = frozenset({"experimental_use_unified_exec_tool"})
DEPRECATED_FEATURE_ALIASES = {
    "codex_hooks": "hooks",
    "collab": "multi_agent",
    "connectors": "apps",
    "enable_experimental_windows_sandbox": "experimental_windows_sandbox",
    "experimental_use_unified_exec_tool": "unified_exec",
    "memory_tool": "memories",
    "request_permissions": "exec_permission_approvals",
}
CANONICAL_FEATURE_KEYS = frozenset(DEPRECATED_FEATURE_ALIASES.values())

SUPPORTED_SCHEMA_KEYWORDS = frozenset(
    {
        "$ref",
        "$schema",
        "additionalProperties",
        "allOf",
        "anyOf",
        "const",
        "default",
        "definitions",
        "description",
        "enum",
        "format",
        "items",
        "maxItems",
        "maxLength",
        "maximum",
        "minItems",
        "minLength",
        "minimum",
        "not",
        "oneOf",
        "pattern",
        "properties",
        "required",
        "title",
        "type",
    }
)

INTEGER_FORMAT_RANGES = {
    "int32": (-(2**31), (2**31) - 1),
    "int64": (-(2**63), (2**63) - 1),
    "uint": (0, None),
    "uint16": (0, (2**16) - 1),
    "uint32": (0, (2**32) - 1),
    "uint64": (0, (2**64) - 1),
}


class GenerationError(ValueError):
    """Raised when the schema cannot be expressed as a safe TOML reference."""


def load_schema() -> dict[str, Any]:
    ensure_schema_path(SCHEMA_PATH)
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = unsupported_schema_keywords(schema)
    if errors:
        raise GenerationError("\n".join(errors))
    return schema


def definitions(schema: dict[str, Any]) -> dict[str, Any]:
    for key in ("$defs", "definitions"):
        value = schema.get(key)
        if isinstance(value, dict):
            return value
    raise GenerationError("config schema has neither $defs nor definitions")


def escape_pointer(segment: str) -> str:
    return segment.replace("~", "~0").replace("/", "~1")


def resolve_ref(schema: dict[str, Any], ref: str) -> Any:
    if not ref.startswith("#/"):
        raise GenerationError(f"external schema reference is unsupported: {ref}")
    node: Any = schema
    for part in ref[2:].split("/"):
        if not isinstance(node, dict):
            raise GenerationError(f"invalid schema reference: {ref}")
        try:
            node = node[part.replace("~1", "/").replace("~0", "~")]
        except KeyError as exc:
            raise GenerationError(f"unresolvable schema reference: {ref}") from exc
    return node


def unsupported_schema_keywords(schema: Any) -> list[str]:
    """Reject JSON-Schema features this generator cannot render and validate."""
    errors: list[str] = []

    def visit(node: Any, pointer: str) -> None:
        if node is True or node is False:
            return
        if not isinstance(node, dict):
            errors.append(f"{pointer}: schema node is not an object")
            return
        unknown = sorted(set(node) - SUPPORTED_SCHEMA_KEYWORDS)
        if unknown:
            errors.append(
                f"{pointer}: unsupported JSON Schema keywords: {', '.join(unknown)}"
            )
        definitions_map = node.get("definitions")
        if isinstance(definitions_map, dict):
            for name, child in definitions_map.items():
                visit(child, f"{pointer}/definitions/{escape_pointer(name)}")
        properties = node.get("properties")
        if isinstance(properties, dict):
            for name, child in properties.items():
                visit(child, f"{pointer}/properties/{escape_pointer(name)}")
        additional = node.get("additionalProperties")
        if isinstance(additional, dict):
            visit(additional, f"{pointer}/additionalProperties")
        items = node.get("items")
        if isinstance(items, dict) or isinstance(items, bool):
            visit(items, f"{pointer}/items")
        for union_name in ("allOf", "anyOf", "oneOf"):
            branches = node.get(union_name)
            if isinstance(branches, list):
                for index, child in enumerate(branches):
                    visit(child, f"{pointer}/{union_name}/{index}")
        not_schema = node.get("not")
        if isinstance(not_schema, dict) or isinstance(not_schema, bool):
            visit(not_schema, f"{pointer}/not")

    if not isinstance(schema, dict):
        return ["#: config schema root is not an object"]
    visit(schema, "#")
    return errors


def flattened_nodes(
    schema: dict[str, Any],
    node: Any,
    seen_refs: frozenset[str] = frozenset(),
) -> list[dict[str, Any]]:
    """Return the non-union fragments that constrain a schema value."""
    if node is True:
        return []
    if node is False:
        raise GenerationError("schema rejects a generated configuration value")
    if not isinstance(node, dict):
        raise GenerationError(f"schema node is not an object: {node!r}")
    if "$ref" in node:
        ref = node["$ref"]
        if ref in seen_refs:
            return []
        resolved = resolve_ref(schema, ref)
        siblings = {key: value for key, value in node.items() if key != "$ref"}
        return flattened_nodes(schema, resolved, seen_refs | {ref}) + (
            [siblings] if siblings else []
        )
    fragments = [{key: value for key, value in node.items() if key != "allOf"}]
    for branch in node.get("allOf", []):
        fragments.extend(flattened_nodes(schema, branch, seen_refs))
    return fragments


def union_branches(schema: dict[str, Any], node: Any) -> tuple[str | None, list[Any]]:
    """Return the first union present after references/allOf are considered."""
    if not isinstance(node, dict):
        return None, []
    if "$ref" in node:
        return union_branches(schema, resolve_ref(schema, node["$ref"]))
    for key in ("oneOf", "anyOf"):
        if key in node:
            branches = node[key]
            if not isinstance(branches, list) or not branches:
                raise GenerationError(f"{key} must contain at least one branch")
            return key, branches
    for branch in node.get("allOf", []):
        kind, branches = union_branches(schema, branch)
        if kind is not None:
            return kind, branches
    return None, []


def declared_types(schema: dict[str, Any], node: Any) -> set[str]:
    types: set[str] = set()
    for fragment in flattened_nodes(schema, node):
        value = fragment.get("type")
        if isinstance(value, str):
            types.add(value)
        elif isinstance(value, list):
            types.update(item for item in value if isinstance(item, str))
    return types


def property_schemas(schema: dict[str, Any], node: Any) -> dict[str, list[Any]]:
    properties: dict[str, list[Any]] = {}
    for fragment in flattened_nodes(schema, node):
        for name, child in fragment.get("properties", {}).items():
            properties.setdefault(name, []).append(child)
    return properties


def required_properties(schema: dict[str, Any], node: Any) -> set[str]:
    required: set[str] = set()
    for fragment in flattened_nodes(schema, node):
        value = fragment.get("required", [])
        if isinstance(value, list):
            required.update(item for item in value if isinstance(item, str))
    return required


def forbidden_required_groups(schema: dict[str, Any], node: Any) -> list[set[str]]:
    groups: list[set[str]] = []
    for fragment in flattened_nodes(schema, node):
        not_schema = fragment.get("not")
        if isinstance(not_schema, dict):
            required = not_schema.get("required")
            if isinstance(required, list) and all(isinstance(item, str) for item in required):
                groups.append(set(required))
    return groups


def combined_schema(nodes: Iterable[Any]) -> Any:
    materialized = list(nodes)
    if not materialized:
        return True
    if len(materialized) == 1:
        return materialized[0]
    return {"allOf": materialized}


def explicit_additional_schema(schema: dict[str, Any], node: Any) -> Any | None:
    additional: list[Any] = []
    for fragment in flattened_nodes(schema, node):
        if "additionalProperties" in fragment:
            additional.append(fragment["additionalProperties"])
    if not additional:
        return None
    if any(value is False for value in additional):
        return False
    materialized = [value for value in additional if isinstance(value, dict)]
    if materialized:
        return combined_schema(materialized)
    return True


def is_object_schema(schema: dict[str, Any], node: Any) -> bool:
    types = declared_types(schema, node)
    return (
        "object" in types
        or bool(property_schemas(schema, node))
        or explicit_additional_schema(schema, node) is not None
    )


def sample_string(node: Any) -> str:
    if isinstance(node, dict):
        default = node.get("default")
        if isinstance(default, str):
            return default
        pattern = node.get("pattern")
        if isinstance(pattern, str):
            candidates = (
                "example",
                "example-role",
                "example_role",
                "EXAMPLE",
                "https://example.invalid",
                "/absolute/path",
            )
            for candidate in candidates:
                if re.search(pattern, candidate):
                    return candidate
            raise GenerationError(
                f"cannot construct a deterministic sample for string pattern {pattern!r}"
            )
    return "example"


def numeric_sample(schema: dict[str, Any], node: Any, integer: bool) -> int | float:
    minimum: float | int | None = None
    maximum: float | int | None = None
    default: Any = None
    numeric_format: str | None = None
    for fragment in flattened_nodes(schema, node):
        if minimum is None and isinstance(fragment.get("minimum"), (int, float)):
            minimum = fragment["minimum"]
        if maximum is None and isinstance(fragment.get("maximum"), (int, float)):
            maximum = fragment["maximum"]
        if default is None and isinstance(fragment.get("default"), (int, float)):
            default = fragment["default"]
        if numeric_format is None and isinstance(fragment.get("format"), str):
            numeric_format = fragment["format"]
    if default is not None:
        candidate: int | float = int(default) if integer else float(default)
    elif minimum is not None:
        candidate = int(math.ceil(minimum)) if integer else float(minimum)
    elif numeric_format in INTEGER_FORMAT_RANGES:
        # A zero value is a practical reference default for signed and unsigned
        # integer formats when the schema has no stricter lower bound.
        candidate = 0
    else:
        candidate = 1 if integer else 1.0
    if maximum is not None and candidate > maximum:
        candidate = int(math.floor(maximum)) if integer else float(maximum)
    return candidate


def sample_key(existing: Any = None, *, base: str = "example") -> str:
    """Return a deterministic example map key absent from an existing mapping."""
    reserved = set(existing) if isinstance(existing, dict) else set()
    if base not in reserved:
        return base
    suffix = 2
    while f"{base}-{suffix}" in reserved:
        suffix += 1
    return f"{base}-{suffix}"


def sample_value(
    schema: dict[str, Any],
    node: Any,
    *,
    ref_stack: frozenset[str] = frozenset(),
    property_name: str | None = None,
    existing: Any = None,
    role_config_file: str = AGENT_ROLE_EXAMPLE_PATH.name,
) -> Any:
    """Create one TOML-serializable value accepted by ``node``."""
    if node is True:
        return "example"
    if node is False:
        raise GenerationError("schema rejects a generated configuration value")
    if not isinstance(node, dict):
        raise GenerationError(f"schema node is not an object: {node!r}")
    if "$ref" in node:
        ref = node["$ref"]
        if ref in ref_stack:
            return "example"
        resolved = resolve_ref(schema, ref)
        siblings = {key: value for key, value in node.items() if key != "$ref"}
        if siblings:
            resolved = {"allOf": [resolved, siblings]}
        return sample_value(
            schema,
            resolved,
            ref_stack=ref_stack | {ref},
            property_name=property_name,
            existing=existing,
            role_config_file=role_config_file,
        )

    union_kind, branches = union_branches(schema, node)
    if union_kind is not None:
        for branch in branches:
            try:
                return sample_value(
                    schema,
                    branch,
                    ref_stack=ref_stack,
                    property_name=property_name,
                    existing=existing,
                    role_config_file=role_config_file,
                )
            except GenerationError:
                continue
        raise GenerationError(f"no {union_kind} branch can produce a TOML value")

    fragments = flattened_nodes(schema, node, ref_stack)
    for fragment in fragments:
        if "const" in fragment:
            return copy.deepcopy(fragment["const"])
        enum = fragment.get("enum")
        if isinstance(enum, list) and enum:
            for value in enum:
                if value is not None:
                    return copy.deepcopy(value)

    if property_name == "config_file":
        return role_config_file

    types = declared_types(schema, node)
    if is_object_schema(schema, node):
        return sample_object(
            schema,
            node,
            ref_stack=ref_stack,
            existing=existing,
            role_config_file=role_config_file,
        )
    if "array" in types:
        items: Any = True
        for fragment in fragments:
            if "items" in fragment:
                items = fragment["items"]
                break
        item_existing = existing[0] if isinstance(existing, list) and existing else None
        return [
            sample_value(
                schema,
                items,
                ref_stack=ref_stack,
                existing=item_existing,
                role_config_file=role_config_file,
            )
        ]
    if "boolean" in types:
        for fragment in fragments:
            if isinstance(fragment.get("default"), bool):
                return fragment["default"]
        return True
    if "integer" in types:
        return numeric_sample(schema, node, integer=True)
    if "number" in types:
        return numeric_sample(schema, node, integer=False)
    if "string" in types or not types or types == {"null"}:
        for fragment in fragments:
            default = fragment.get("default")
            if isinstance(default, str):
                return default
            if isinstance(fragment.get("pattern"), str):
                return sample_string(fragment)
        return "example"
    raise GenerationError(f"unsupported TOML value types: {sorted(types)}")


def sample_object(
    schema: dict[str, Any],
    node: Any,
    *,
    ref_stack: frozenset[str],
    existing: Any = None,
    role_config_file: str = AGENT_ROLE_EXAMPLE_PATH.name,
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    forbidden = forbidden_required_groups(schema, node)
    properties = property_schemas(schema, node)
    is_feature_object = CANONICAL_FEATURE_KEYS <= properties.keys()

    for name in sorted(properties):
        if name in DEPRECATED_ROOT_ALIASES or (
            is_feature_object and name in DEPRECATED_FEATURE_ALIASES
        ):
            continue
        prospective = set(result) | {name}
        if any(group <= prospective for group in forbidden):
            continue
        child_existing = existing.get(name) if isinstance(existing, dict) else None
        result[name] = sample_value(
            schema,
            combined_schema(properties[name]),
            ref_stack=ref_stack,
            property_name=name,
            existing=child_existing,
            role_config_file=role_config_file,
        )

    missing = required_properties(schema, node) - set(result)
    if missing:
        skipped = ", ".join(sorted(missing))
        raise GenerationError(
            f"schema alternatives conflict with required object properties: {skipped}"
        )

    additional = explicit_additional_schema(schema, node)
    if isinstance(additional, dict):
        key = sample_key(existing)
        while key in result:
            key = sample_key(existing, base=f"{key}-value")
        result[key] = sample_value(
            schema,
            additional,
            ref_stack=ref_stack,
            role_config_file=role_config_file,
        )
    elif additional is True and not result:
        result[sample_key(existing)] = "example"
    return result


def toml_key(key: str) -> str:
    if re.fullmatch(r"[A-Za-z0-9_-]+", key):
        return key
    return json.dumps(key, ensure_ascii=False)


def toml_literal(value: Any) -> str:
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int) and not isinstance(value, bool):
        return str(value)
    if isinstance(value, float):
        if not math.isfinite(value):
            raise GenerationError("TOML reference cannot contain non-finite numbers")
        return repr(value)
    if isinstance(value, list):
        return "[" + ", ".join(toml_literal(item) for item in value) + "]"
    if isinstance(value, dict):
        pairs = (f"{toml_key(key)} = {toml_literal(child)}" for key, child in value.items())
        return "{ " + ", ".join(pairs) + " }"
    raise GenerationError(f"TOML reference cannot express {type(value).__name__} values")


def schema_options(schema: dict[str, Any], node: Any) -> list[str]:
    """Return every finite literal option represented by a schema node."""
    if node is True:
        return ["any TOML value"]
    if node is False or not isinstance(node, dict):
        return []
    if "$ref" in node:
        return schema_options(schema, resolve_ref(schema, node["$ref"]))
    kind, branches = union_branches(schema, node)
    if kind is not None:
        options: list[str] = []
        for branch in branches:
            try:
                option = toml_literal(sample_value(schema, branch))
            except GenerationError:
                option = "complex table"
            if option not in options:
                options.append(option)
        return options
    for fragment in flattened_nodes(schema, node):
        if "const" in fragment:
            return [toml_literal(fragment["const"])]
        enum = fragment.get("enum")
        if isinstance(enum, list) and enum:
            return [toml_literal(value) for value in enum]
    types = declared_types(schema, node)
    if types == {"boolean"}:
        return ["true", "false"]
    return []


def finite_options(
    schema: dict[str, Any],
    node: Any,
    *,
    ref_stack: frozenset[str] = frozenset(),
) -> list[Any]:
    """Return every TOML-expressible enum or constant accepted by ``node``."""
    if node is True or node is False or not isinstance(node, dict):
        return []
    if "$ref" in node:
        ref = node["$ref"]
        if ref in ref_stack:
            return []
        resolved = resolve_ref(schema, ref)
        siblings = {key: value for key, value in node.items() if key != "$ref"}
        resolved_node = {"allOf": [resolved, siblings]} if siblings else resolved
        return finite_options(schema, resolved_node, ref_stack=ref_stack | {ref})

    candidates: list[Any] = []
    union_kind, branches = union_branches(schema, node)
    if union_kind is not None:
        for branch in branches:
            candidates.extend(finite_options(schema, branch, ref_stack=ref_stack))
    else:
        for fragment in flattened_nodes(schema, node, ref_stack):
            if "const" in fragment:
                candidates.append(copy.deepcopy(fragment["const"]))
            enum = fragment.get("enum")
            if isinstance(enum, list):
                candidates.extend(copy.deepcopy(value) for value in enum)

    options: list[Any] = []
    for candidate in candidates:
        try:
            toml_literal(candidate)
        except GenerationError:
            continue
        if candidate not in options and not validate_value(schema, candidate, node):
            options.append(candidate)
    return options


def describe(node: Any) -> str | None:
    if isinstance(node, dict):
        value = node.get("description")
        if isinstance(value, str) and value:
            return " ".join(value.split())
    return None


def root_property_values(
    schema: dict[str, Any],
    *,
    existing: dict[str, Any] | None = None,
    role_config_file: str = AGENT_ROLE_EXAMPLE_PATH.name,
) -> tuple[dict[str, Any], dict[tuple[str, ...], list[str]]]:
    values: dict[str, Any] = {}
    comments: dict[tuple[str, ...], list[str]] = {}
    existing = existing or {}
    root_properties = schema.get("properties")
    if not isinstance(root_properties, dict):
        raise GenerationError("config schema root must define properties")
    permission_profile_name = sample_key(
        existing.get("permissions"),
        base="example-profile",
    )
    for name in sorted(root_properties):
        if name in DEPRECATED_ROOT_ALIASES:
            continue
        node = root_properties[name]
        property_comments: list[str] = []
        description = describe(node)
        if description:
            property_comments.append(f"# {description}")
        options = schema_options(schema, node)
        if len(options) > 1:
            property_comments.append(f"# alternatives: {' | '.join(options)}")
        if name == "default_permissions":
            values[name] = permission_profile_name
        elif name == "permissions":
            values[name] = {
                permission_profile_name: sample_value(
                    schema,
                    definitions(schema)["PermissionProfileToml"],
                    existing=existing.get(name),
                    role_config_file=role_config_file,
                )
            }
        else:
            values[name] = sample_value(
                schema,
                node,
                property_name=name,
                existing=existing.get(name),
                role_config_file=role_config_file,
            )
        if property_comments:
            comments[(name,)] = property_comments
    return values, comments


def toml_path(path: tuple[str, ...]) -> str:
    return ".".join(toml_key(segment) for segment in path)


def render_mapping(
    lines: list[str],
    value: dict[str, Any],
    *,
    path: tuple[str, ...] = (),
    comments: dict[tuple[str, ...], list[str]] | None = None,
) -> None:
    """Render a mapping with TOML tables instead of opaque nested inline tables."""
    comments = comments or {}
    table_values: list[tuple[str, Any]] = []
    for name, child in value.items():
        child_path = path + (name,)
        child_comments = comments.get(child_path, [])
        if isinstance(child, dict) or (
            isinstance(child, list) and child and all(isinstance(item, dict) for item in child)
        ):
            table_values.append((name, child))
            continue
        lines.extend(child_comments)
        lines.append(f"{toml_key(name)} = {toml_literal(child)}")

    if path and (value or not lines or lines[-1] != ""):
        lines.append("")
    if table_values and lines and lines[-1] != "":
        lines.append("")
    for name, child in table_values:
        child_path = path + (name,)
        lines.extend(comments.get(child_path, []))
        if isinstance(child, dict):
            lines.append(f"[{toml_path(child_path)}]")
            render_mapping(lines, child, path=child_path, comments=comments)
            continue
        for item in child:
            lines.append(f"[[{toml_path(child_path)}]]")
            render_mapping(lines, item, path=child_path, comments=comments)


def schema_entry_nodes(schema: dict[str, Any]) -> dict[str, Any]:
    """Return every value-bearing schema location keyed by its JSON pointer."""
    entries: dict[str, Any] = {}

    def visit(node: Any, pointer: str) -> None:
        if isinstance(node, dict):
            properties = node.get("properties")
            if isinstance(properties, dict):
                for name, child in properties.items():
                    child_pointer = f"{pointer}/properties/{escape_pointer(name)}"
                    entries[child_pointer] = child
                    visit(child, child_pointer)
            if "additionalProperties" in node:
                child = node["additionalProperties"]
                child_pointer = f"{pointer}/additionalProperties"
                entries[child_pointer] = child
                visit(child, child_pointer)
            if "items" in node:
                child = node["items"]
                child_pointer = f"{pointer}/items"
                entries[child_pointer] = child
                visit(child, child_pointer)
            for union_name in ("oneOf", "anyOf"):
                branches = node.get(union_name)
                if isinstance(branches, list):
                    for index, child in enumerate(branches):
                        visit(child, f"{pointer}/{union_name}/{index}")
            for index, child in enumerate(node.get("allOf", [])):
                visit(child, f"{pointer}/allOf/{index}")
        elif isinstance(node, list):
            for index, child in enumerate(node):
                visit(child, f"{pointer}/{index}")

    root_properties = schema.get("properties", {})
    if isinstance(root_properties, dict):
        for name, child in root_properties.items():
            pointer = f"#/properties/{escape_pointer(name)}"
            entries[pointer] = child
            visit(child, pointer)
    definition_key = "$defs" if "$defs" in schema else "definitions"
    for name, child in definitions(schema).items():
        visit(child, f"#/{definition_key}/{escape_pointer(name)}")
    return entries


def pointer_ledger(schema: dict[str, Any]) -> tuple[list[str], list[str], list[str]]:
    entries: set[str] = set(schema_entry_nodes(schema))
    variants: set[str] = set()

    def visit(node: Any, pointer: str) -> None:
        if isinstance(node, dict):
            for union_name in ("oneOf", "anyOf"):
                branches = node.get(union_name)
                if isinstance(branches, list):
                    for index, child in enumerate(branches):
                        child_pointer = f"{pointer}/{union_name}/{index}"
                        variants.add(child_pointer)
                        visit(child, child_pointer)
            properties = node.get("properties")
            if isinstance(properties, dict):
                for name, child in properties.items():
                    visit(child, f"{pointer}/properties/{escape_pointer(name)}")
            if "additionalProperties" in node:
                visit(node["additionalProperties"], f"{pointer}/additionalProperties")
            if "items" in node:
                visit(node["items"], f"{pointer}/items")
            for index, child in enumerate(node.get("allOf", [])):
                visit(child, f"{pointer}/allOf/{index}")
        elif isinstance(node, list):
            for index, child in enumerate(node):
                visit(child, f"{pointer}/{index}")

    definition_key = "$defs" if "$defs" in schema else "definitions"
    root_properties = schema.get("properties", {})
    if isinstance(root_properties, dict):
        for name, child in root_properties.items():
            visit(child, f"#/properties/{escape_pointer(name)}")
    for name, child in definitions(schema).items():
        visit(child, f"#/{definition_key}/{escape_pointer(name)}")
    return sorted(definitions(schema)), sorted(entries), sorted(variants)


def schema_option_summary(schema: dict[str, Any], node: Any) -> str:
    if node is False:
        return "not permitted"
    if node is True:
        return "any TOML value"
    options = schema_options(schema, node)
    if options:
        return " | ".join(options)
    types = declared_types(schema, node)
    if is_object_schema(schema, node):
        return "inline table; see child schema paths below"
    if "array" in types:
        return "array; see item schema path below"
    if types:
        return " or ".join(sorted(types))
    return "any TOML value"


def option_matrix_lines(schema: dict[str, Any]) -> list[str]:
    lines = [
        "",
        "# Option matrix: each schema entry is listed below. Finite alternatives",
        "# are summarized; object and array entries link to their child paths.",
    ]
    for pointer, node in sorted(schema_entry_nodes(schema).items()):
        lines.append(f"{OPTION_MARKER}{pointer} = {schema_option_summary(schema, node)}")
    return lines


def finite_option_entries(schema: dict[str, Any]) -> list[str]:
    """Return an exhaustive ledger of every finite TOML option in the schema."""
    entries: list[str] = []
    for pointer, node in sorted(schema_entry_nodes(schema).items()):
        for option in finite_options(schema, node):
            entries.append(f"{pointer} = {toml_literal(option)}")
    return entries


def finite_option_lines(schema: dict[str, Any]) -> list[str]:
    lines = [
        "",
        "# Finite option matrix: every TOML-expressible enum and constant is",
        "# listed independently so changing a schema option makes verification fail.",
    ]
    lines.extend(f"{FINITE_OPTION_MARKER}{entry}" for entry in finite_option_entries(schema))
    return lines


def definition_example_lines(schema: dict[str, Any]) -> list[str]:
    lines = [
        "",
        "# Definition examples: one schema-valid TOML value for every reusable",
        "# definition, including definitions reached only through untyped maps.",
    ]
    for name, node in sorted(definitions(schema).items()):
        value = sample_value(schema, node)
        errors = validate_value(schema, value, node, f"definition {name}")
        if errors:
            raise GenerationError("\n".join(errors))
        lines.append(f"{EXAMPLE_MARKER}{name} = {toml_literal(value)}")
    return lines


def coverage_ledger_lines(schema: dict[str, Any]) -> list[str]:
    definition_names, entries, variants = pointer_ledger(schema)
    lines = ["# Coverage ledger: every marker below is checked against ../schemas/config.schema.json."]
    lines.extend(f"{DEFINITION_MARKER}{name}" for name in definition_names)
    lines.extend(f"{ENTRY_MARKER}{pointer}" for pointer in entries)
    lines.extend(f"{VARIANT_MARKER}{pointer}" for pointer in variants)
    return lines


def render_home_example(schema: dict[str, Any]) -> str:
    lines = [
        "# Generated from ../schemas/config.schema.json; do not edit manually.",
        "#",
        "# This is an exhaustive user configuration reference, not an installable",
        "# default. Active canonical settings use one schema-valid representative",
        "# value. Deprecated aliases and mutually exclusive alternatives remain in",
        "# comment-only coverage metadata. Replace placeholders before using this.",
        "#",
        f"# The agents.example.config_file setting points to {AGENT_ROLE_EXAMPLE_PATH.name}.",
        "",
    ]
    root_values, root_comments = root_property_values(schema)
    render_mapping(lines, root_values, comments=root_comments)
    lines.extend(option_matrix_lines(schema))
    lines.extend(finite_option_lines(schema))
    lines.extend(definition_example_lines(schema))
    lines.append("")
    lines.extend(coverage_ledger_lines(schema))
    return "\n".join(lines).rstrip() + "\n"


def render_agent_role_example(schema: dict[str, Any], *, home_example_path: Path) -> str:
    role_schema = definitions(schema).get("AgentRoleToml")
    if not isinstance(role_schema, dict):
        raise GenerationError("config schema does not define AgentRoleToml")
    value = sample_value(schema, role_schema)
    if not isinstance(value, dict):
        raise GenerationError("AgentRoleToml must generate an object")
    value.pop("config_file", None)
    lines = [
        f"# Generated companion for {home_example_path.name} agents.<role>.config_file.",
        "# Copy this file and tailor it for each named agent role.",
        "",
    ]
    for name, child in value.items():
        lines.append(f"{toml_key(name)} = {toml_literal(child)}")
    lines.append("")
    lines.append(f"{DEFINITION_MARKER}AgentRoleToml")
    return "\n".join(lines).rstrip() + "\n"


def matches_type(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
    if expected == "null":
        return value is None
    return True


def validate_value(schema: dict[str, Any], value: Any, node: Any, path: str = "$") -> list[str]:
    """Small, dependency-free JSON Schema subset validator for generated output."""
    if node is True:
        return []
    if node is False:
        return [f"{path}: schema rejects this value"]
    if not isinstance(node, dict):
        return [f"{path}: malformed schema node"]
    if "$ref" in node:
        errors = validate_value(schema, value, resolve_ref(schema, node["$ref"]), path)
        siblings = {key: child for key, child in node.items() if key != "$ref"}
        return errors + (validate_value(schema, value, siblings, path) if siblings else [])

    errors: list[str] = []
    for branch in node.get("allOf", []):
        errors.extend(validate_value(schema, value, branch, path))
    if "not" in node and not validate_value(schema, value, node["not"], path):
        errors.append(f"{path}: value matches a forbidden schema")
    for union_name, exact in (("anyOf", False), ("oneOf", True)):
        if union_name not in node:
            continue
        branches = [validate_value(schema, value, branch, path) for branch in node[union_name]]
        matches = sum(not branch for branch in branches)
        if matches == 0 or (exact and matches != 1):
            qualifier = "exactly one" if exact else "at least one"
            errors.append(f"{path}: value does not match {qualifier} {union_name} branch")
            return errors
    if "const" in node and value != node["const"]:
        errors.append(f"{path}: expected constant {node['const']!r}")
    if "enum" in node and value not in node["enum"]:
        errors.append(f"{path}: value is not an allowed enum member")
    declared = node.get("type")
    if declared is not None:
        types = declared if isinstance(declared, list) else [declared]
        if not any(matches_type(value, expected) for expected in types):
            return errors + [f"{path}: expected type {declared!r}"]
    if isinstance(value, dict):
        required = node.get("required", [])
        for name in required if isinstance(required, list) else []:
            if name not in value:
                errors.append(f"{path}: missing required property {name!r}")
        properties = node.get("properties", {})
        pattern_properties = node.get("patternProperties", {})
        additional = node.get("additionalProperties", True)
        for name, child in value.items():
            child_path = f"{path}.{name}"
            if name in properties:
                errors.extend(validate_value(schema, child, properties[name], child_path))
                continue
            matches = [
                child_schema
                for pattern, child_schema in pattern_properties.items()
                if re.search(pattern, name)
            ]
            if matches:
                for child_schema in matches:
                    errors.extend(validate_value(schema, child, child_schema, child_path))
            elif additional is False:
                errors.append(f"{child_path}: additional property is not allowed")
            elif isinstance(additional, dict):
                errors.extend(validate_value(schema, child, additional, child_path))
    if isinstance(value, list):
        items = node.get("items")
        if items is not None:
            for index, child in enumerate(value):
                errors.extend(validate_value(schema, child, items, f"{path}[{index}]"))
        if isinstance(node.get("minItems"), int) and len(value) < node["minItems"]:
            errors.append(f"{path}: fewer than {node['minItems']} items")
        if isinstance(node.get("maxItems"), int) and len(value) > node["maxItems"]:
            errors.append(f"{path}: more than {node['maxItems']} items")
    if isinstance(value, str):
        if isinstance(node.get("minLength"), int) and len(value) < node["minLength"]:
            errors.append(f"{path}: string is too short")
        if isinstance(node.get("maxLength"), int) and len(value) > node["maxLength"]:
            errors.append(f"{path}: string is too long")
        if isinstance(node.get("pattern"), str) and re.search(node["pattern"], value) is None:
            errors.append(f"{path}: string does not match the required pattern")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if isinstance(node.get("minimum"), (int, float)) and value < node["minimum"]:
            errors.append(f"{path}: value is below its minimum")
        if isinstance(node.get("maximum"), (int, float)) and value > node["maximum"]:
            errors.append(f"{path}: value is above its maximum")
        numeric_format = node.get("format")
        if numeric_format in INTEGER_FORMAT_RANGES and isinstance(value, int):
            minimum, maximum = INTEGER_FORMAT_RANGES[numeric_format]
            if value < minimum or (maximum is not None and value > maximum):
                errors.append(f"{path}: value is outside the {numeric_format} range")
    return errors


def marker_values(content: str, prefix: str) -> set[str]:
    return {
        line.removeprefix(prefix)
        for line in content.splitlines()
        if line.startswith(prefix)
    }


def config_file_values(value: Any) -> set[str]:
    """Collect role-layer file names from generated config mappings."""
    if not isinstance(value, dict):
        return set()
    values: set[str] = set()
    for name, child in value.items():
        if name == "config_file" and isinstance(child, str):
            values.add(child)
        values.update(config_file_values(child))
    return values


def deprecated_alias_errors(value: Any, path: str = "$") -> list[str]:
    """Reject deprecated aliases from active generated TOML mappings."""
    if not isinstance(value, dict):
        return []

    errors: list[str] = []
    for name, child in value.items():
        child_path = f"{path}.{name}"
        if name in DEPRECATED_ROOT_ALIASES:
            errors.append(f"{child_path}: deprecated config alias is active")
        if name == "features" and isinstance(child, dict):
            for alias, replacement in DEPRECATED_FEATURE_ALIASES.items():
                if alias in child:
                    errors.append(
                        f"{child_path}.{alias}: use canonical feature {replacement!r}"
                    )
        errors.extend(deprecated_alias_errors(child, child_path))
    return errors


def validate_rendered_examples(
    schema: dict[str, Any],
    home_text: str,
    role_text: str,
) -> list[str]:
    errors: list[str] = []
    try:
        home = tomllib.loads(home_text)
        role = tomllib.loads(role_text)
    except tomllib.TOMLDecodeError as exc:
        return [f"generated TOML is invalid: {exc}"]

    errors.extend(validate_value(schema, home, schema))
    errors.extend(deprecated_alias_errors(home))
    role_schema = definitions(schema)["AgentRoleToml"]
    errors.extend(validate_value(schema, role, role_schema, "agent-role.toml"))
    role_file_values = config_file_values(home)
    if AGENT_ROLE_EXAMPLE_PATH.name not in role_file_values:
        errors.append(
            "config.home.toml does not reference its generated agent-role companion"
        )

    expected_definitions, expected_entries, expected_variants = pointer_ledger(schema)
    actual_definitions = marker_values(home_text, DEFINITION_MARKER)
    actual_entries = marker_values(home_text, ENTRY_MARKER)
    actual_variants = marker_values(home_text, VARIANT_MARKER)
    actual_options = marker_values(home_text, OPTION_MARKER)
    actual_finite_options = marker_values(home_text, FINITE_OPTION_MARKER)
    actual_examples = marker_values(home_text, EXAMPLE_MARKER)
    for label, expected, actual in (
        ("definition", set(expected_definitions), actual_definitions),
        ("entry", set(expected_entries), actual_entries),
        ("variant", set(expected_variants), actual_variants),
        ("option", set(expected_entries), {value.split(" = ", 1)[0] for value in actual_options}),
        ("definition example", set(expected_definitions), {value.split(" = ", 1)[0] for value in actual_examples}),
    ):
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        if missing:
            errors.append(f"coverage ledger is missing {label} markers: {', '.join(missing[:10])}")
        if extra:
            errors.append(f"coverage ledger has unknown {label} markers: {', '.join(extra[:10])}")
    expected_finite_options = set(finite_option_entries(schema))
    missing_finite_options = sorted(expected_finite_options - actual_finite_options)
    extra_finite_options = sorted(actual_finite_options - expected_finite_options)
    if missing_finite_options:
        errors.append(
            "coverage ledger is missing finite option markers: "
            + ", ".join(missing_finite_options[:10])
        )
    if extra_finite_options:
        errors.append(
            "coverage ledger has unknown finite option markers: "
            + ", ".join(extra_finite_options[:10])
        )
    return errors


def rendered_examples(schema: dict[str, Any]) -> dict[Path, str]:
    home = render_home_example(schema)
    role = render_agent_role_example(schema, home_example_path=HOME_EXAMPLE_PATH)
    errors = validate_rendered_examples(
        schema,
        home,
        role,
    )
    if errors:
        raise GenerationError("\n".join(errors))
    return {
        HOME_EXAMPLE_PATH: home,
        AGENT_ROLE_EXAMPLE_PATH: role,
    }


def ensure_schema_path(path: Path) -> None:
    generation_root = GENERATION_ROOT.resolve()
    schemas_root = SCHEMAS_DIRECTORY.resolve()
    try:
        schemas_root.relative_to(generation_root)
        path.resolve().relative_to(schemas_root)
    except ValueError as exc:
        raise GenerationError(
            f"refusing to read outside generate/schemas/: {path}"
        ) from exc


def ensure_example_path(path: Path) -> None:
    generation_root = GENERATION_ROOT.resolve()
    examples_root = EXAMPLES_DIRECTORY.resolve()
    try:
        examples_root.relative_to(generation_root)
        path.resolve().relative_to(examples_root)
    except ValueError as exc:
        raise GenerationError(
            f"refusing to write outside generate/examples/: {path}"
        ) from exc


def write_if_changed(path: Path, content: str) -> bool:
    ensure_example_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)
    return True


def run(write: bool) -> int:
    try:
        schema = load_schema()
        outputs = rendered_examples(schema)
    except (GenerationError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    drift: list[Path] = []
    for path, content in outputs.items():
        ensure_example_path(path)
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            drift.append(path)
    if drift and not write:
        print(
            "ERROR: generated examples are missing or stale; run "
            "python3 generate/scripts/config_toml_coverage.py --write",
            file=sys.stderr,
        )
        for path in drift:
            print(f"  generate/{path.relative_to(GENERATION_ROOT)}", file=sys.stderr)
        return 1

    changed = [path for path, content in outputs.items() if write_if_changed(path, content)] if write else []
    definition_names, entries, variants = pointer_ledger(schema)
    if changed:
        print("Generated config schema examples:")
        for path in changed:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
            print(f"  generate/{path.relative_to(GENERATION_ROOT)} ({digest})")
    print(
        "Config schema example coverage is valid: "
        f"{len(definition_names)} definitions, {len(entries)} entries, "
        f"and {len(variants)} explicit union variants."
    )
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--write",
        action="store_true",
        help="write only the generated files under generate/examples/",
    )
    mode.add_argument(
        "--check",
        action="store_true",
        help="verify generated examples without writing them (the default)",
    )
    args = parser.parse_args(argv)
    return run(write=args.write)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
