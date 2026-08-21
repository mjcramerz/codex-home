#!/usr/bin/env python3
"""Validate exhaustive config-schema coverage without bloating installable TOML."""

from __future__ import annotations

import argparse
import itertools
import json
import math
import re
import sys
import tomllib
from collections import defaultdict
from pathlib import Path
from typing import Any


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPOSITORY_ROOT / "schemas" / "config.schema.json"
HOME_CONFIG_PATH = REPOSITORY_ROOT / "home" / "config.toml"
SYSTEM_CONFIG_PATH = REPOSITORY_ROOT / "etc" / "config.toml"
REQUIREMENTS_PATH = REPOSITORY_ROOT / "etc" / "requirements.toml"

HOME_BEGIN = "# BEGIN:generated-config-schema-user-reference"
HOME_END = "# END:generated-config-schema-user-reference"
SYSTEM_BEGIN = "# BEGIN:generated-config-schema-system-reference"
SYSTEM_END = "# END:generated-config-schema-system-reference"
REQUIREMENTS_BEGIN = "# BEGIN:generated-config-schema-requirements-reference"
REQUIREMENTS_END = "# END:generated-config-schema-requirements-reference"
GENERATED_MARKERS = {
    HOME_CONFIG_PATH: (HOME_BEGIN, HOME_END),
    SYSTEM_CONFIG_PATH: (SYSTEM_BEGIN, SYSTEM_END),
    REQUIREMENTS_PATH: (REQUIREMENTS_BEGIN, REQUIREMENTS_END),
}

# These settings are host-, organization-, authentication-, permission-, or
# telemetry-oriented. Everything else is documented in the user-layer config.
SYSTEM_ROOTS = {
    "allow_login_shell",
    "analytics",
    "approval_policy",
    "approvals_reviewer",
    "apps_mcp_product_sku",
    "chatgpt_base_url",
    "cli_auth_credentials_store",
    "default_permissions",
    "feedback",
    "forced_chatgpt_workspace_id",
    "forced_login_method",
    "ghost_snapshot",
    "log_dir",
    "mcp_oauth_callback_port",
    "mcp_oauth_callback_url",
    "mcp_oauth_credentials_store",
    "mcp_servers",
    "model_providers",
    "notice",
    "openai_base_url",
    "otel",
    "permissions",
    "responses_api_metadata",
    "sandbox_mode",
    "sandbox_workspace_write",
    "shell_environment_policy",
    "sqlite_home",
    "suppress_unstable_features_warning",
    "windows",
}

# requirements.toml has a different grammar from config.toml. This list
# documents every config-schema surface that its managed-policy controls can
# constrain without pretending arbitrary config keys are valid requirements.
REQUIREMENTS_ROOTS = {
    "agents",
    "approval_policy",
    "approvals_reviewer",
    "apps",
    "default_permissions",
    "features",
    "forced_chatgpt_workspace_id",
    "forced_login_method",
    "hooks",
    "mcp_servers",
    "memories",
    "model_providers",
    "permissions",
    "plugins",
    "sandbox_mode",
    "sandbox_workspace_write",
    "skills",
    "tools",
    "web_search",
}

REQUIREMENTS_ALLOWED_ROOTS = {
    "allow_appshots",
    "allow_login_shell",
    "allow_managed_hooks_only",
    "allow_remote_control",
    "allowed_approval_policies",
    "allowed_approvals_reviewers",
    "allowed_permission_profiles",
    "allowed_sandbox_modes",
    "allowed_web_search_modes",
    "apps",
    "check_for_update_on_startup",
    "computer_use",
    "default_permissions",
    "enforce_residency",
    "experimental_network",
    "features",
    "feedback",
    "guardian_policy_config",
    "hooks",
    "log_dir",
    "marketplaces",
    "mcp_servers",
    "model_catalog_json",
    "models",
    "permissions",
    "plugins",
    "remote_sandbox_config",
    "rules",
    "sqlite_home",
    "windows",
}

INTEGER_FORMAT_RANGES = {
    "int32": (-(2**31), (2**31) - 1),
    "int64": (-(2**63), (2**63) - 1),
    "uint": (0, None),
    "uint16": (0, (2**16) - 1),
    "uint32": (0, (2**32) - 1),
    "uint64": (0, (2**64) - 1),
}


def load_schema() -> dict[str, Any]:
    return json.loads(SCHEMA_PATH.read_text())


def resolve_ref(schema_root: dict[str, Any], ref: str) -> Any:
    if not ref.startswith("#/"):
        raise ValueError(f"external schema reference is unsupported: {ref}")
    node: Any = schema_root
    for part in ref[2:].split("/"):
        node = node[part.replace("~1", "/").replace("~0", "~")]
    return node


def expand_variants(
    schema_root: dict[str, Any],
    node: Any,
    seen_refs: frozenset[str] = frozenset(),
) -> list[Any]:
    if isinstance(node, bool):
        return [node]
    if not isinstance(node, dict):
        return []
    if "$ref" in node:
        ref = node["$ref"]
        if ref in seen_refs:
            return []
        return expand_variants(schema_root, resolve_ref(schema_root, ref), seen_refs | {ref})
    for key in ("anyOf", "oneOf"):
        if key in node:
            variants: list[Any] = []
            for branch in node[key]:
                variants.extend(expand_variants(schema_root, branch, seen_refs))
            return variants
    if "allOf" in node:
        variants = []
        for branch in node["allOf"]:
            variants.extend(expand_variants(schema_root, branch, seen_refs))
        siblings = {key: value for key, value in node.items() if key != "allOf"}
        if siblings:
            variants.append(siblings)
        return variants
    return [node]


def collect_entries(schema_root: dict[str, Any]) -> dict[str, list[Any]]:
    entries: dict[str, list[Any]] = defaultdict(list)

    def visit(node: Any, path: str = "", ref_stack: tuple[str, ...] = ()) -> None:
        if not isinstance(node, dict):
            return
        if "$ref" in node:
            ref = node["$ref"]
            if ref in ref_stack:
                return
            visit(resolve_ref(schema_root, ref), path, ref_stack + (ref,))
            return
        for key in ("allOf", "anyOf", "oneOf"):
            for branch in node.get(key, []):
                visit(branch, path, ref_stack)
        properties = node.get("properties")
        if isinstance(properties, dict):
            for name, child in properties.items():
                child_path = f"{path}.{name}" if path else name
                entries[child_path].append(child)
                visit(child, child_path, ref_stack)
        additional = node.get("additionalProperties")
        if isinstance(additional, dict):
            dynamic_path = f"{path}.<name>" if path else "<name>"
            entries[dynamic_path].append(additional)
            visit(additional, dynamic_path, ref_stack)
        items = node.get("items")
        if isinstance(items, dict):
            visit(items, f"{path}[]", ref_stack)

    visit(schema_root)
    return dict(entries)


def target_for(path: str) -> str:
    root = path.split(".", 1)[0].removesuffix("[]")
    if path.startswith("features.network_proxy"):
        return "system"
    return "system" if root in SYSTEM_ROOTS else "home"


def remove_generated_block(text: str, begin: str, end: str) -> str:
    pattern = re.compile(
        rf"(?ms)\n?^{re.escape(begin)}\n.*?^{re.escape(end)}(?:\n|$)"
    )
    return pattern.sub("\n", text).rstrip() + "\n"


def parse_toml(path: Path) -> dict[str, Any]:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def combine_schema_constraints(nodes: list[Any]) -> Any:
    constrained = [node for node in nodes if node is not True]
    if not constrained:
        return True
    if len(constrained) == 1:
        return constrained[0]
    return {"allOf": constrained}


def direct_child_schemas(
    schema_root: dict[str, Any],
    node: dict[str, Any],
    segment: str,
) -> list[Any]:
    declared = node.get("type")
    declared_types = (
        set(declared)
        if isinstance(declared, list)
        else {declared}
        if isinstance(declared, str)
        else set()
    )
    object_shaped = any(
        key in node for key in ("properties", "patternProperties", "additionalProperties")
    )
    array_shaped = "items" in node
    unconstrained_shape = not declared_types and not object_shaped and not array_shaped
    descendants: list[Any] = []

    if unconstrained_shape or "object" in declared_types or object_shaped:
        properties = node.get("properties", {})
        child_constraints: list[Any] = []
        if segment in properties:
            child_constraints.append(properties[segment])
        for pattern, child_schema in node.get("patternProperties", {}).items():
            if re.search(pattern, segment):
                child_constraints.append(child_schema)
        if child_constraints:
            descendants.append(combine_schema_constraints(child_constraints))
        else:
            additional = node.get("additionalProperties", True)
            if additional is True:
                descendants.append(True)
            elif isinstance(additional, dict):
                descendants.append(additional)

    if "array" in declared_types or array_shaped:
        descendants.extend(
            child_schema_alternatives(
                schema_root,
                node.get("items", True),
                segment,
            )
        )

    if unconstrained_shape and not descendants:
        descendants.append(True)
    return descendants


def child_schema_alternatives(
    schema_root: dict[str, Any],
    raw: Any,
    segment: str,
    seen_refs: frozenset[str] = frozenset(),
) -> list[Any]:
    if raw is True:
        return [True]
    if raw is False or not isinstance(raw, dict):
        return []
    if "$ref" in raw:
        ref = raw["$ref"]
        if ref in seen_refs:
            return []
        return child_schema_alternatives(
            schema_root,
            resolve_ref(schema_root, ref),
            segment,
            seen_refs | {ref},
        )

    sibling_schema = {
        key: value
        for key, value in raw.items()
        if key not in {"allOf", "anyOf", "oneOf", "not"}
    }
    mandatory_groups: list[list[Any]] = [
        direct_child_schemas(schema_root, sibling_schema, segment)
    ]

    for branch in raw.get("allOf", []):
        branch_children = child_schema_alternatives(
            schema_root,
            branch,
            segment,
            seen_refs,
        )
        if not branch_children:
            return []
        mandatory_groups.append(branch_children)

    for key in ("anyOf", "oneOf"):
        if key not in raw:
            continue
        branch_children: list[Any] = []
        for branch in raw[key]:
            branch_children.extend(
                child_schema_alternatives(
                    schema_root,
                    branch,
                    segment,
                    seen_refs,
                )
            )
        if not branch_children:
            return []
        mandatory_groups.append(branch_children)

    if any(not group for group in mandatory_groups):
        return []
    return [
        combine_schema_constraints(list(combination))
        for combination in itertools.product(*mandatory_groups)
    ]


def descend_schema_nodes(
    schema_root: dict[str, Any],
    nodes: list[Any],
    segment: str,
) -> list[Any]:
    descendants: list[Any] = []
    for node in nodes:
        descendants.extend(child_schema_alternatives(schema_root, node, segment))
    return descendants


def schema_path_allowed(schema_root: dict[str, Any], parts: list[str]) -> bool:
    nodes: list[Any] = [schema_root]
    for part in parts:
        nodes = descend_schema_nodes(schema_root, nodes, part)
        if not nodes:
            return False
    return True


def table_path_parts(content: str, array_table: bool) -> list[str]:
    header = f"[[{content}]]\n" if array_table else f"[{content}]\n"
    payload = tomllib.loads(header + "__coverage_probe__ = 1\n")
    parts: list[str] = []
    node: Any = payload
    while isinstance(node, dict) and "__coverage_probe__" not in node:
        if len(node) != 1:
            raise ValueError(f"ambiguous TOML table path: {content}")
        key = next(iter(node))
        parts.append(key)
        node = node[key]
        if isinstance(node, list):
            node = node[0]
    return parts


def assignment_path_parts(lhs: str) -> list[str]:
    payload = tomllib.loads(lhs + " = 1\n")
    parts: list[str] = []
    node: Any = payload
    while isinstance(node, dict):
        if len(node) != 1:
            raise ValueError(f"ambiguous TOML key path: {lhs}")
        key = next(iter(node))
        parts.append(key)
        node = node[key]
    return parts


def validate_config_examples(
    schema_root: dict[str, Any],
    path: Path,
) -> list[str]:
    """Reject active or commented config-like entries absent from the schema."""
    errors: list[str] = []
    active_table: list[str] = []
    comment_table: list[str] = []
    in_multiline = False
    multiline_quote = ""
    key_pattern = re.compile(
        r"((?:\"(?:\\.|[^\"\\])*\"|'(?:[^']|'')*'|[A-Za-z0-9_-]+)"
        r"(?:\s*\.\s*(?:\"(?:\\.|[^\"\\])*\"|'(?:[^']|'')*'|[A-Za-z0-9_-]+))*)"
        r"\s*="
    )

    for line_number, line in enumerate(path.read_text().splitlines(), 1):
        if in_multiline:
            if line.count(multiline_quote) % 2 == 1:
                in_multiline = False
            continue

        stripped = line.strip()
        if not stripped:
            comment_table = active_table.copy()
            continue

        commented = stripped.startswith("#")
        if commented:
            stripped = stripped[1:].lstrip()
            if not stripped or stripped.startswith("#") or stripped.startswith("schema-entry:"):
                continue
        else:
            for quote in ('"""', "'''"):
                if stripped.count(quote) % 2 == 1:
                    in_multiline = True
                    multiline_quote = quote
                    break

        array_match = re.fullmatch(r"\[\[(.+)\]\](?:\s*#.*)?", stripped)
        if array_match:
            try:
                parts = table_path_parts(array_match.group(1), array_table=True)
            except (ValueError, tomllib.TOMLDecodeError):
                continue
            if not schema_path_allowed(schema_root, parts):
                errors.append(
                    f"{path}:{line_number}: schema-absent table {'.'.join(parts)}"
                )
            if commented:
                comment_table = parts
            else:
                active_table = parts
                comment_table = parts
            continue

        table_match = re.fullmatch(r"\[(.+)\](?:\s*#.*)?", stripped)
        if table_match:
            try:
                parts = table_path_parts(table_match.group(1), array_table=False)
            except (ValueError, tomllib.TOMLDecodeError):
                continue
            if not schema_path_allowed(schema_root, parts):
                errors.append(
                    f"{path}:{line_number}: schema-absent table {'.'.join(parts)}"
                )
            if commented:
                comment_table = parts
            else:
                active_table = parts
                comment_table = parts
            continue

        key_match = key_pattern.match(stripped)
        if not key_match:
            continue
        try:
            key_parts = assignment_path_parts(key_match.group(1))
        except (ValueError, tomllib.TOMLDecodeError):
            continue
        parts = (comment_table if commented else active_table) + key_parts
        if not schema_path_allowed(schema_root, parts):
            errors.append(
                f"{path}:{line_number}: schema-absent entry {'.'.join(parts)}"
            )
        if not commented:
            comment_table = active_table.copy()
    return errors


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
        return (
            isinstance(value, (int, float))
            and not isinstance(value, bool)
            and math.isfinite(value)
        )
    if expected == "null":
        return value is None
    return True


def validate_value(
    schema_root: dict[str, Any],
    value: Any,
    node: Any,
    path: str = "$",
) -> list[str]:
    errors: list[str] = []
    if isinstance(node, bool):
        return errors if node else [f"{path}: schema rejects this value"]
    if not isinstance(node, dict):
        return errors
    if "$ref" in node:
        return validate_value(schema_root, value, resolve_ref(schema_root, node["$ref"]), path)
    for branch in node.get("allOf", []):
        errors.extend(validate_value(schema_root, value, branch, path))
    if "not" in node and not validate_value(schema_root, value, node["not"], path):
        errors.append(f"{path}: value matches a forbidden schema")
    if "anyOf" in node:
        branches = [validate_value(schema_root, value, branch, path) for branch in node["anyOf"]]
        if not any(not branch for branch in branches):
            errors.append(f"{path}: value does not match any allowed schema")
            return errors
    if "oneOf" in node:
        branches = [validate_value(schema_root, value, branch, path) for branch in node["oneOf"]]
        if sum(not branch for branch in branches) != 1:
            errors.append(f"{path}: value does not match exactly one allowed schema")
            return errors
    if "const" in node and value != node["const"]:
        errors.append(f"{path}: expected constant {node['const']!r}")
    if "enum" in node and value not in node["enum"]:
        errors.append(f"{path}: {value!r} is not an allowed value")
    declared = node.get("type")
    if declared is not None:
        types = declared if isinstance(declared, list) else [declared]
        if not any(matches_type(value, expected) for expected in types):
            errors.append(f"{path}: expected type {declared!r}")
            return errors
    if isinstance(value, dict):
        for required in node.get("required", []):
            if required not in value:
                errors.append(f"{path}: missing required property {required!r}")
        properties = node.get("properties", {})
        patterns = [
            (re.compile(pattern), child)
            for pattern, child in node.get("patternProperties", {}).items()
        ]
        additional = node.get("additionalProperties", True)
        for key, child_value in value.items():
            child_path = f"{path}.{key}"
            if key in properties:
                errors.extend(
                    validate_value(schema_root, child_value, properties[key], child_path)
                )
                continue
            matched = False
            for pattern, child_schema in patterns:
                if pattern.search(key):
                    matched = True
                    errors.extend(
                        validate_value(schema_root, child_value, child_schema, child_path)
                    )
            if matched:
                continue
            if additional is False:
                errors.append(f"{child_path}: additional property is not allowed")
            elif isinstance(additional, dict):
                errors.extend(
                    validate_value(schema_root, child_value, additional, child_path)
                )
    if isinstance(value, list):
        items = node.get("items")
        if items is not None:
            for index, child_value in enumerate(value):
                errors.extend(
                    validate_value(schema_root, child_value, items, f"{path}[{index}]")
                )
        if "minItems" in node and len(value) < node["minItems"]:
            errors.append(f"{path}: fewer than {node['minItems']} items")
        if "maxItems" in node and len(value) > node["maxItems"]:
            errors.append(f"{path}: more than {node['maxItems']} items")
    if isinstance(value, str):
        if "minLength" in node and len(value) < node["minLength"]:
            errors.append(f"{path}: string is too short")
        if "maxLength" in node and len(value) > node["maxLength"]:
            errors.append(f"{path}: string is too long")
        if "pattern" in node and re.search(node["pattern"], value) is None:
            errors.append(f"{path}: string does not match required pattern")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in node and value < node["minimum"]:
            errors.append(f"{path}: value is below minimum {node['minimum']}")
        if "maximum" in node and value > node["maximum"]:
            errors.append(f"{path}: value is above maximum {node['maximum']}")
        numeric_format = node.get("format")
        if numeric_format in INTEGER_FORMAT_RANGES and isinstance(value, int):
            minimum, maximum = INTEGER_FORMAT_RANGES[numeric_format]
            if value < minimum or (maximum is not None and value > maximum):
                errors.append(
                    f"{path}: value is outside the {numeric_format} range"
                )
    return errors


def validate_requirements(
    schema_root: dict[str, Any],
    requirements: dict[str, Any],
    system_config: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    unknown_roots = sorted(set(requirements) - REQUIREMENTS_ALLOWED_ROOTS)
    if unknown_roots:
        errors.append(
            "requirements contains unsupported top-level keys: "
            + ", ".join(unknown_roots)
        )

    policies = requirements.get("allowed_approval_policies")
    if not isinstance(policies, list) or not all(isinstance(item, str) for item in policies):
        errors.append("allowed_approval_policies must be a list of policy-name strings")
    allowed_policy_names = {"granular", "untrusted", "on-request", "never"}
    if isinstance(policies, list):
        unknown = sorted(set(policies) - allowed_policy_names)
        if unknown:
            errors.append(f"unsupported approval policies: {', '.join(unknown)}")

    reviewers = requirements.get("allowed_approvals_reviewers")
    allowed_reviewers = {"user", "auto_review"}
    if not isinstance(reviewers, list) or not all(
        isinstance(item, str) for item in reviewers
    ):
        errors.append(
            "allowed_approvals_reviewers must be a list of reviewer-name strings"
        )
    elif unknown := sorted(set(reviewers) - allowed_reviewers):
        errors.append(f"unsupported approval reviewers: {', '.join(unknown)}")

    web_modes = requirements.get("allowed_web_search_modes")
    expected_web_modes = set(resolve_ref(schema_root, "#/definitions/WebSearchMode")["enum"])
    if not isinstance(web_modes, list) or set(web_modes) != expected_web_modes:
        errors.append(
            "allowed_web_search_modes must contain every WebSearchMode schema value"
        )

    feature_schema = schema_root["properties"]["features"]["properties"]
    feature_requirements = requirements.get("features", {})
    if not isinstance(feature_requirements, dict):
        errors.append("requirements features must be a table")
    else:
        unknown_features = sorted(set(feature_requirements) - set(feature_schema))
        if unknown_features:
            errors.append(
                "requirements contains unknown feature keys: "
                + ", ".join(unknown_features)
            )
        non_boolean_features = sorted(
            name
            for name, value in feature_requirements.items()
            if not isinstance(value, bool)
        )
        if non_boolean_features:
            errors.append(
                "requirements feature pins must be booleans: "
                + ", ".join(non_boolean_features)
            )

    allowed_profiles = requirements.get("allowed_permission_profiles", {})
    if not isinstance(allowed_profiles, dict):
        errors.append("allowed_permission_profiles must be a table of booleans")
        allowed_profiles = {}
    non_boolean_profiles = sorted(
        name for name, value in allowed_profiles.items() if not isinstance(value, bool)
    )
    if non_boolean_profiles:
        errors.append(
            "permission-profile allowlist values must be booleans: "
            + ", ".join(non_boolean_profiles)
        )
    custom_profiles = {
        name
        for name, enabled in allowed_profiles.items()
        if enabled and isinstance(name, str) and not name.startswith(":")
    }
    defined_profiles = set(system_config.get("permissions", {}))
    missing_profiles = sorted(custom_profiles - defined_profiles)
    if missing_profiles:
        errors.append(
            "requirements references undefined permission profiles: "
            + ", ".join(missing_profiles)
        )

    default_permissions = requirements.get("default_permissions")
    if not isinstance(default_permissions, str):
        errors.append("default_permissions must be a profile-name string")
    elif allowed_profiles.get(default_permissions) is not True:
        errors.append(
            "default_permissions must name a profile explicitly allowed with true"
        )

    if not isinstance(requirements.get("allow_managed_hooks_only"), bool):
        errors.append("allow_managed_hooks_only must be a boolean")
    if requirements.get("enforce_residency") != "us":
        errors.append('enforce_residency must currently be "us"')

    def validate_identity(label: str, identity: Any) -> None:
        if not isinstance(identity, dict):
            errors.append(f"{label}.identity must be a table")
            return
        identity_keys = set(identity)
        if identity_keys not in ({"command"}, {"url"}):
            errors.append(
                f"{label}.identity must define exactly one of command or url"
            )
            return
        value = identity[next(iter(identity_keys))]
        if not isinstance(value, (str, dict)):
            errors.append(
                f"{label}.identity.{next(iter(identity_keys))} "
                "must be a string or matcher table"
            )

    mcp_requirements = requirements.get("mcp_servers", {})
    if not isinstance(mcp_requirements, dict):
        errors.append("mcp_servers requirements must be a table")
    else:
        for name, server in mcp_requirements.items():
            label = f"mcp_servers.{name}"
            if not isinstance(server, dict):
                errors.append(f"{label} must be a table")
                continue
            unknown = sorted(set(server) - {"identity"})
            if unknown:
                errors.append(f"{label} has unsupported keys: {', '.join(unknown)}")
            validate_identity(label, server.get("identity"))

    plugin_requirements = requirements.get("plugins", {})
    if not isinstance(plugin_requirements, dict):
        errors.append("plugins requirements must be a table")
    else:
        for plugin_name, plugin in plugin_requirements.items():
            plugin_label = f"plugins.{plugin_name}"
            if not isinstance(plugin, dict):
                errors.append(f"{plugin_label} must be a table")
                continue
            unknown = sorted(set(plugin) - {"mcp_servers"})
            if unknown:
                errors.append(
                    f"{plugin_label} has unsupported keys: {', '.join(unknown)}"
                )
            servers = plugin.get("mcp_servers", {})
            if not isinstance(servers, dict):
                errors.append(f"{plugin_label}.mcp_servers must be a table")
                continue
            for server_name, server in servers.items():
                label = f"{plugin_label}.mcp_servers.{server_name}"
                if not isinstance(server, dict):
                    errors.append(f"{label} must be a table")
                    continue
                unknown = sorted(set(server) - {"identity"})
                if unknown:
                    errors.append(
                        f"{label} has unsupported keys: {', '.join(unknown)}"
                    )
                validate_identity(label, server.get("identity"))

    app_requirements = requirements.get("apps", {})
    if not isinstance(app_requirements, dict):
        errors.append("apps requirements must be a table")
    else:
        for app_name, app in app_requirements.items():
            label = f"apps.{app_name}"
            if not isinstance(app, dict):
                errors.append(f"{label} must be a table")
                continue
            unknown = sorted(set(app) - {"enabled", "tools"})
            if unknown:
                errors.append(f"{label} has unsupported keys: {', '.join(unknown)}")
            if "enabled" in app and not isinstance(app["enabled"], bool):
                errors.append(f"{label}.enabled must be a boolean")
    return errors


def build_coverage_sets(
    entries: dict[str, list[Any]],
) -> tuple[set[str], set[str], set[str]]:
    home_paths = {path for path in entries if target_for(path) == "home"}
    system_paths = {path for path in entries if target_for(path) == "system"}
    requirements_paths = {
        path
        for path in entries
        if path.split(".", 1)[0].removesuffix("[]") in REQUIREMENTS_ROOTS
    }
    return home_paths, system_paths, requirements_paths


def validate_coverage_partition(
    entries: dict[str, list[Any]],
) -> list[str]:
    errors: list[str] = []
    home_paths, system_paths, requirements_paths = build_coverage_sets(entries)
    expected = set(entries)
    primary_paths = home_paths | system_paths
    missing = sorted(expected - primary_paths)
    extra = sorted(primary_paths - expected)
    duplicates = sorted(home_paths & system_paths)
    if missing:
        errors.append(f"unmapped config schema paths: {', '.join(missing[:20])}")
    if extra:
        errors.append(f"unknown mapped config schema paths: {', '.join(extra[:20])}")
    if duplicates:
        errors.append(
            "config schema paths mapped to both user and system layers: "
            + ", ".join(duplicates[:20])
        )

    expected_requirements = {
        path
        for path in expected
        if path.split(".", 1)[0].removesuffix("[]") in REQUIREMENTS_ROOTS
    }
    if requirements_paths != expected_requirements:
        missing_requirements = sorted(expected_requirements - requirements_paths)
        extra_requirements = sorted(requirements_paths - expected_requirements)
        if missing_requirements:
            errors.append(
                "requirements coverage mapping is missing: "
                + ", ".join(missing_requirements[:20])
            )
        if extra_requirements:
            errors.append(
                "requirements coverage mapping has unknown paths: "
                + ", ".join(extra_requirements[:20])
            )
    return errors


def run(write: bool) -> int:
    schema_root = load_schema()
    entries = collect_entries(schema_root)
    changed: list[Path] = []
    marker_errors: list[str] = []
    for path, (begin, end) in GENERATED_MARKERS.items():
        original = path.read_text()
        begin_count = original.count(begin)
        end_count = original.count(end)
        if begin_count != end_count:
            marker_errors.append(
                f"{path}: mismatched generated schema marker count "
                f"({begin_count} begin, {end_count} end)"
            )
            continue
        cleaned = remove_generated_block(original, begin, end)
        residual_entries = [
            line_number
            for line_number, line in enumerate(cleaned.splitlines(), start=1)
            if line.startswith("# schema-entry:")
        ]
        if residual_entries:
            marker_errors.append(
                f"{path}: obsolete schema-entry comments remain outside the "
                f"generated block at lines {', '.join(map(str, residual_entries[:20]))}"
            )
        if cleaned == original:
            continue
        if write:
            path.write_text(cleaned)
            changed.append(path)
        else:
            marker_errors.append(
                f"{path}: installable TOML contains a generated schema-entry block; "
                "run with --write to remove it"
            )

    errors: list[str] = marker_errors
    parsed: dict[Path, dict[str, Any]] = {}
    for path in (HOME_CONFIG_PATH, SYSTEM_CONFIG_PATH, REQUIREMENTS_PATH):
        try:
            parsed[path] = parse_toml(path)
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"{path}: invalid TOML: {exc}")

    for path in (HOME_CONFIG_PATH, SYSTEM_CONFIG_PATH):
        payload = parsed.get(path)
        if payload is None:
            continue
        errors.extend(
            f"{path}: {error}"
            for error in validate_value(schema_root, payload, schema_root)
        )
        errors.extend(validate_config_examples(schema_root, path))

    errors.extend(validate_coverage_partition(entries))
    if REQUIREMENTS_PATH in parsed and SYSTEM_CONFIG_PATH in parsed:
        errors.extend(
            validate_requirements(
                schema_root,
                parsed[REQUIREMENTS_PATH],
                parsed[SYSTEM_CONFIG_PATH],
            )
        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    home_paths, system_paths, requirements_paths = build_coverage_sets(entries)
    if changed:
        print("Removed generated schema-entry blocks from installable TOML:")
        for path in changed:
            print(f"  {path.relative_to(REPOSITORY_ROOT)}")
    print(
        "Config schema coverage is valid: "
        f"{len(entries)} entries "
        f"({len(home_paths)} user-layer mappings, "
        f"{len(system_paths)} system-layer mappings, "
        f"{len(requirements_paths)} requirements-policy mappings)."
    )
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="remove obsolete generated schema-entry blocks before validating",
    )
    args = parser.parse_args(argv)
    return run(write=args.write)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
