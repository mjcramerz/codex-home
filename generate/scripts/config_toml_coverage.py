#!/usr/bin/env python3
"""Convert supported configuration properties into real TOML examples.

Generated TOML contains settings, tables and arrays of tables, not JSON Schema
keywords, pointers, ledgers or definition dumps. Build-time coverage information
is written separately as JSON under generate/reports/. Nothing writes to home/,
etc/ or agents/. Examples contain placeholders and are never installed.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import os
import tempfile
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
REPORTS_DIRECTORY = GENERATION_ROOT / "reports"
COVERAGE_PATH = REPORTS_DIRECTORY / "config-coverage.json"
sys.path.insert(0, str(GENERATION_ROOT.parent / "scripts"))
from config_toml import clean_loads, dumps as config_dumps, render_mapping


_OMIT = object()

DEPRECATED_ROOT_ALIASES = frozenset({"experimental_use_unified_exec_tool", "ghost_snapshot"})
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
# The exact custom schema retains compatibility keys; examples must not activate
# removed/no-op flags merely because JSON Schema still accepts them.
FEATURE_POLICY = json.loads((GENERATION_ROOT / 'feature-policy.json').read_text())
OBSOLETE_FEATURE_KEYS = frozenset(FEATURE_POLICY['removed']) | frozenset(FEATURE_POLICY['deprecated']) | frozenset(FEATURE_POLICY['aliases']) | frozenset(FEATURE_POLICY.get('requirements_only', []))
DEPRECATED_FEATURE_ALIASES.update(FEATURE_POLICY['aliases'])

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
    content = SCHEMA_PATH.read_bytes()
    if hashlib.sha256(content).hexdigest() != FEATURE_POLICY['schema_sha256']:
        raise GenerationError('supplied schema checksum changed; review the schema pin first')
    schema = json.loads(content)
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
        # Prefer the table form of bool-or-table settings so nested configuration
        # keys are converted into named TOML tables, rather than disappearing
        # behind a boolean shorthand in the reference examples.
        branches = sorted(branches, key=lambda branch: (
            is_object_schema(schema, branch), len(property_schemas(schema, branch))
        ), reverse=True)
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
            is_feature_object and name in OBSOLETE_FEATURE_KEYS
        ):
            continue
        if {'filters', 'inherit', 'ignore_default_excludes'} <= properties.keys() and name in {'exclude', 'include_only'}:
            continue  # Prefer canonical keyed shell filters in generated examples.
        if name == 'usage_hint_enabled':
            continue  # The supplied schema calls this an ignored compatibility field.
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
        # Prefer the table form of bool-or-table settings so nested configuration
        # keys are converted into named TOML tables, rather than disappearing
        # behind a boolean shorthand in the reference examples.
        branches = sorted(branches, key=lambda branch: (
            is_object_schema(schema, branch), len(property_schemas(schema, branch))
        ), reverse=True)
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


def finite_option_entries(schema: dict[str, Any]) -> list[str]:
    """Return an exhaustive ledger of every finite TOML option in the schema."""
    entries: list[str] = []
    for pointer, node in sorted(schema_entry_nodes(schema).items()):
        for option in finite_options(schema, node):
            entries.append(f"{pointer} = {toml_literal(option)}")
    return entries


def render_home_example(schema: dict[str, Any]) -> str:
    values, comments = root_property_values(schema)
    # Keep mutually exclusive configurations in separate actual TOML files.
    for name in ('sandbox_mode', 'sandbox_workspace_write', 'compact_prompt'):
        values.pop(name, None)
    return config_dumps(values, comments=comments, header=[
        '# Configuration syntax examples only; NOT deployment defaults.',
        '# Replace example values before copying individual settings.',
        '# Never install this entire file as CODEX_HOME/config.toml.',
        '# Agent configuration layers use the companion agent-role.toml.',
    ])


def render_agent_role_example(schema: dict[str, Any], *, home_example_path: Path) -> str:
    # config_file points to a CONFIG LAYER, not an AgentRoleToml declaration.
    # description/nickname_candidates belong in [agents.<role>] in the parent.
    return config_dumps({
        'model_reasoning_effort': 'high',
        'developer_instructions': 'Complete the assigned bounded subtask and report verification evidence.',
    }, header=[
        f'# Companion configuration layer for {home_example_path.name}.',
        '# Role descriptions and nicknames belong in the parent [agents.<role>] table.',
    ])


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
            for alias in OBSOLETE_FEATURE_KEYS:
                replacement = DEPRECATED_FEATURE_ALIASES.get(alias, "removed/deprecated; omit")
                if alias in child:
                    errors.append(
                        f"{child_path}.{alias}: use canonical feature {replacement!r}"
                    )
        errors.extend(deprecated_alias_errors(child, child_path))
    return errors


def alternative_examples(schema: dict[str, Any]) -> dict[Path, str]:
    props = schema['properties']
    sandbox = {
        'sandbox_mode': 'workspace-write',
        'sandbox_workspace_write': sample_value(schema, props['sandbox_workspace_write']),
    }
    compact = {'compact_prompt': 'Preserve decisions, constraints, validation evidence and the remaining work.'}
    return {
        EXAMPLES_DIRECTORY / 'alternatives/sandbox-workspace.toml': config_dumps(sandbox, header=[
            '# Alternative to default_permissions and [permissions], not an additional layer.',
            '# Remove the permission-profile selector before using this older sandbox form.',
        ]),
        EXAMPLES_DIRECTORY / 'alternatives/inline-compaction.toml': config_dumps(compact, header=[
            '# Alternative to experimental_compact_prompt_file, not a second compaction source.',
            '# Remove the file-based compaction override before using this setting.',
        ]),
    }


def validate_rendered_examples(
    schema: dict[str, Any], home_text: str, role_text: str,
) -> list[str]:
    errors: list[str] = []
    try:
        home = clean_loads(home_text, 'config.home.toml')
        role = clean_loads(role_text, 'agent-role.toml')
    except (ValueError, tomllib.TOMLDecodeError) as exc:
        return [f'generated TOML is invalid: {exc}']
    errors.extend(validate_value(schema, home, schema))
    errors.extend(deprecated_alias_errors(home))
    errors.extend(validate_value(schema, role, schema, 'agent-role.toml'))
    if AGENT_ROLE_EXAMPLE_PATH.name not in config_file_values(home):
        errors.append('config.home.toml does not reference its generated agent-role companion')
    if 'sandbox_mode' in home and 'default_permissions' in home:
        errors.append('permission selectors must live in separate examples')
    if 'compact_prompt' in home and 'experimental_compact_prompt_file' in home:
        errors.append('compaction sources must live in separate examples')
    return errors


def coverage_report(schema: dict[str, Any], outputs: dict[Path, str]) -> dict[str, Any]:
    """All schema internals remain in JSON, never in a .toml file."""
    from jsonschema import Draft7Validator
    definition_names, entries, variants = pointer_ledger(schema)
    converted: dict[str, list[str]] = {}
    file_records: dict[str, Any] = {}
    for path, text in outputs.items():
        data = clean_loads(text, str(path))
        relative = str(path.relative_to(GENERATION_ROOT))
        file_records[relative] = {'sha256': hashlib.sha256(text.encode()).hexdigest(), 'root_keys': sorted(data)}
        # The companion config layer is validated separately and is not the
        # exhaustive root-settings catalog.
        if path == AGENT_ROLE_EXAMPLE_PATH:
            continue
        Draft7Validator(schema).validate(data)
        for name in data:
            converted.setdefault(name, []).append(relative)
    wanted = set(schema['properties']) - set(DEPRECATED_ROOT_ALIASES)
    missing = wanted - set(converted)
    if missing:
        raise GenerationError('unconverted configuration properties: ' + ', '.join(sorted(missing)))
    if set(converted) - wanted:
        raise GenerationError('unsupported or retired root configuration in generated TOML')
    samples = {}
    for name, node in sorted(definitions(schema).items()):
        value = sample_value(schema, node)
        errors = validate_value(schema, value, node, f'definition {name}')
        if errors:
            raise GenerationError('\n'.join(errors))
        Draft7Validator({'$ref': '#/definitions/' + name, 'definitions': definitions(schema)}).validate(value)
        samples[name] = value
    return {
        'format': 1,
        'purpose': 'Build-time accounting only; never install into CODEX_HOME or /etc/codex.',
        'schema_sha256': FEATURE_POLICY['schema_sha256'],
        'counts': {'root_properties': len(schema['properties']), 'converted_root_properties': len(converted),
                   'definitions': len(definition_names), 'entries': len(entries), 'union_variants': len(variants)},
        'root_properties': {name: {
            'status': 'retired-compatibility-only' if name in DEPRECATED_ROOT_ALIASES else 'converted-to-toml',
            'toml_files': converted.get(name, []),
        } for name in sorted(schema['properties'])},
        'files': file_records,
        'definitions': definition_names,
        'entries': entries,
        'union_variants': variants,
        'options': {pointer: schema_option_summary(schema, node) for pointer, node in sorted(schema_entry_nodes(schema).items())},
        'finite_options': finite_option_entries(schema),
        'definition_values': samples,
    }


def rendered_examples(schema: dict[str, Any]) -> dict[Path, str]:
    home = render_home_example(schema)
    role = render_agent_role_example(schema, home_example_path=HOME_EXAMPLE_PATH)
    errors = validate_rendered_examples(schema, home, role)
    if errors:
        raise GenerationError('\n'.join(errors))
    outputs = {HOME_EXAMPLE_PATH: home, AGENT_ROLE_EXAMPLE_PATH: role, **alternative_examples(schema)}
    report = coverage_report(schema, outputs)
    outputs[COVERAGE_PATH] = json.dumps(report, indent=2, ensure_ascii=True) + '\n'
    return outputs


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
    """Allow outputs only below the source-only examples/reports directories."""
    generation_root = GENERATION_ROOT.resolve()
    for allowed in (EXAMPLES_DIRECTORY, REPORTS_DIRECTORY):
        try:
            allowed.resolve().relative_to(generation_root)
            path.resolve().relative_to(allowed.resolve())
            if path.is_symlink():
                raise GenerationError(f'refusing symlink output: {path}')
            return
        except ValueError:
            continue
    raise GenerationError(f'refusing to write outside generate/examples/ or generate/reports/: {path}')


def write_if_changed(path: Path, content: str) -> bool:
    ensure_example_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding='utf-8') == content:
        return False
    fd, temporary = tempfile.mkstemp(prefix='.codex-example-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, 0o644)
        os.replace(temporary, path)
        directory_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return True


def run(write: bool) -> int:
    try:
        schema = load_schema()
        outputs = rendered_examples(schema)
    except (GenerationError, json.JSONDecodeError, OSError) as exc:
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
        print("Generated TOML settings examples and separate JSON coverage:")
        for path in changed:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
            print(f"  generate/{path.relative_to(GENERATION_ROOT)} ({digest})")
    print(
        "TOML conversion and external JSON coverage are valid: "
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
        help="write TOML under generate/examples/ and JSON under generate/reports/ only",
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
