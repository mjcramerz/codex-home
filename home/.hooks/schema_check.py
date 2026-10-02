"""Offline validation for the assertion vocabulary in the supplied Codex schemas.

This is deliberately limited to the pinned Draft 7 snapshots. Unknown assertion
keywords and external references fail closed. Formats are annotations in Draft 7;
Rust integer ranges and deployment paths are checked separately by the tests.
No imports, downloads, schema-driven code execution, or data-bearing errors.
"""
from __future__ import annotations

import math
import re

KEYWORDS = frozenset({"$schema", "$ref", "title", "description", "definitions",
    "default", "format", "type", "enum", "const", "properties", "additionalProperties",
    "required", "items", "allOf", "anyOf", "oneOf", "not", "minimum", "maximum",
    "minLength", "maxLength", "pattern"})


class SchemaError(ValueError):
    """A schema contract failed; messages contain paths, never input values."""


def check_schema(node: object) -> None:
    if isinstance(node, bool):
        return
    if not isinstance(node, dict) or set(node) - KEYWORDS:
        raise SchemaError("unsupported schema vocabulary")
    for field in ("properties", "definitions"):
        for child in node.get(field, {}).values():
            check_schema(child)
    for field in ("allOf", "anyOf", "oneOf"):
        for child in node.get(field, []):
            check_schema(child)
    for field in ("not", "items", "additionalProperties"):
        if field in node:
            check_schema(node[field])
    ref = node.get("$ref")
    if ref is not None and not ref.startswith("#/"):
        raise SchemaError("external schema reference")


def json_equal(left: object, right: object) -> bool:
    # Python considers True == 1; JSON Schema does not.
    if isinstance(left, bool) != isinstance(right, bool):
        return False
    if isinstance(left, dict) and isinstance(right, dict):
        return left.keys() == right.keys() and all(json_equal(v, right[k]) for k, v in left.items())
    if isinstance(left, list) and isinstance(right, list):
        return len(left) == len(right) and all(json_equal(a, b) for a, b in zip(left, right))
    return left == right


def validate(schema: dict, value: object, node: object = None, path: str = "$", depth: int = 0) -> None:
    if depth > 128:
        raise SchemaError(path + ": nesting limit")
    if node is None:
        node = schema
    if node is True:
        return
    if node is False:
        raise SchemaError(path + ": disallowed value")
    if not isinstance(node, dict) or set(node) - KEYWORDS:
        raise SchemaError(path + ": unsupported schema vocabulary")
    if "$ref" in node:
        ref = node["$ref"]
        if not ref.startswith("#/"):
            raise SchemaError(path + ": external schema reference")
        target = schema
        try:
            for part in ref[2:].split("/"):
                target = target[part.replace("~1", "/").replace("~0", "~")]
        except (KeyError, TypeError):
            raise SchemaError(path + ": unresolved schema reference") from None
        # Draft 7 ignores siblings of $ref.
        validate(schema, value, target, path, depth + 1)
        return
    kind = node.get("type")
    if kind is not None:
        kinds = kind if isinstance(kind, list) else [kind]
        number = isinstance(value, (int, float)) and not isinstance(value, bool)
        matches = {"null": value is None, "boolean": isinstance(value, bool),
            "object": isinstance(value, dict), "array": isinstance(value, list),
            "string": isinstance(value, str), "number": number,
            "integer": number and (isinstance(value, int) or (math.isfinite(value) and value.is_integer()))}
        if not any(matches.get(k, False) for k in kinds):
            raise SchemaError(path + ": wrong type")
    if "enum" in node and not any(json_equal(value, choice) for choice in node["enum"]):
        raise SchemaError(path + ": unsupported enum")
    if "const" in node and not json_equal(value, node["const"]):
        raise SchemaError(path + ": wrong constant")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if isinstance(value, float) and not math.isfinite(value):
            raise SchemaError(path + ": non-finite number")
        if "minimum" in node and value < node["minimum"]:
            raise SchemaError(path + ": below minimum")
        if "maximum" in node and value > node["maximum"]:
            raise SchemaError(path + ": above maximum")
    if isinstance(value, str):
        if len(value) < node.get("minLength", 0) or len(value) > node.get("maxLength", len(value)):
            raise SchemaError(path + ": invalid length")
        if "pattern" in node and re.search(node["pattern"], value) is None:
            raise SchemaError(path + ": invalid pattern")
    if isinstance(value, dict):
        if any(k not in value for k in node.get("required", [])):
            raise SchemaError(path + ": missing required property")
        properties = node.get("properties", {})
        for key, child in value.items():
            if key in properties:
                validate(schema, child, properties[key], path + "." + key, depth + 1)
            elif "additionalProperties" in node:
                validate(schema, child, node["additionalProperties"], path + "." + key, depth + 1)
    if isinstance(value, list) and "items" in node:
        for index, child in enumerate(value):
            validate(schema, child, node["items"], path + f"[{index}]", depth + 1)
    for child in node.get("allOf", []):
        validate(schema, value, child, path, depth + 1)
    for field in ("anyOf", "oneOf"):
        if field not in node:
            continue
        successes = 0
        for child in node[field]:
            try:
                validate(schema, value, child, path, depth + 1)
                successes += 1
            except SchemaError:
                pass
        if successes == 0 or (field == "oneOf" and successes != 1):
            raise SchemaError(path + ": invalid " + field + " alternative")
    if "not" in node:
        try:
            validate(schema, value, node["not"], path, depth + 1)
        except SchemaError:
            pass
        else:
            raise SchemaError(path + ": incompatible properties")
