#!/usr/bin/env python3
"""Validate core runtime-pack instruction parity and routing relationships."""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_PATHS = (
    Path("home/AGENTS.md"),
    Path("home/INDEX.md"),
    Path("home/config.toml"),
    Path("home/docs/architecture.md"),
    Path("home/docs/instruction-system.md"),
    Path("home/docs/workflows/runtime-pack-maintenance.md"),
    Path("home/index/manifest.yml"),
    Path("home/index/pack/config.md"),
    Path("home/index/pack/instructions.md"),
    Path("home/index/pack/overview.md"),
    Path("home/plans/workflows/workflow-runtime-pack-maintenance.md"),
    Path("schemas/config.schema.json"),
    Path("instructions/default/agents/hierarchical.md"),
    Path("instructions/default/models/base.md"),
    Path("instructions/default/modes/default.md"),
    Path("instructions/default/modes/plan.md"),
    Path("home/.models/instructions/agents/hierarchical.md"),
    Path("home/.models/instructions/models/base.md"),
    Path("home/.models/instructions/modes/default.md"),
    Path("home/.models/instructions/modes/plan.md"),
)

INTENTIONALLY_UNSET_ROOT_KEYS = frozenset(
    {
        "apps_mcp_product_sku",
        "compact_prompt",
        "experimental_realtime_webrtc_call_base_url",
        "experimental_realtime_ws_base_url",
        "experimental_realtime_ws_model",
        "experimental_thread_store",
        "experimental_use_unified_exec_tool",
        "forced_chatgpt_workspace_id",
        "ghost_snapshot",
        "instructions",
        "oss_provider",
        "profile",
        "responses_api_metadata",
        "sandbox_mode",
        "sandbox_workspace_write",
    }
)

DEFAULT_INSTRUCTION_MIRRORS = (
    (
        Path("instructions/default/models/base.md"),
        Path("home/.models/instructions/models/base.md"),
    ),
    (
        Path("instructions/default/agents/hierarchical.md"),
        Path("home/.models/instructions/agents/hierarchical.md"),
    ),
    (
        Path("instructions/default/modes/default.md"),
        Path("home/.models/instructions/modes/default.md"),
    ),
    (
        Path("instructions/default/modes/plan.md"),
        Path("home/.models/instructions/modes/plan.md"),
    ),
)

REQUIRED_REFERENCES = {
    Path("home/AGENTS.md"): (
        "$CODEX_HOME/docs/instruction-system.md",
        "$CODEX_HOME/index/pack/instructions.md",
    ),
    Path("home/INDEX.md"): (
        "$CODEX_HOME/index/pack/instructions.md",
        "$CODEX_HOME/docs/instruction-system.md",
    ),
    Path("home/index/pack/overview.md"): (
        "$CODEX_HOME/index/pack/instructions.md",
        "$CODEX_HOME/docs/instruction-system.md",
    ),
    Path("home/index/pack/config.md"): (
        "$CODEX_HOME/index/pack/instructions.md",
        "scripts/validate_model_catalogs.py",
    ),
    Path("home/docs/OVERVIEW.md"): ("$CODEX_HOME/docs/instruction-system.md",),
    Path("home/docs/architecture.md"): ("$CODEX_HOME/docs/instruction-system.md",),
    Path("home/docs/workflows/runtime-pack-maintenance.md"): (
        "$CODEX_HOME/docs/instruction-system.md",
        "scripts/validate_runtime_pack_assets.py",
    ),
    Path("home/plans/workflows/workflow-runtime-pack-maintenance.md"): (
        "$CODEX_HOME/docs/instruction-system.md",
        "scripts/validate_runtime_pack_assets.py",
    ),
}

MANIFEST_REFERENCES = (
    "  instructions:\n",
    "entrypoint: $CODEX_HOME/index/pack/instructions.md",
    "canonical: $CODEX_HOME/docs/instruction-system.md",
    "$CODEX_HOME/index/pack/instructions.md",
)


def relative(path: Path) -> str:
    return str(path.relative_to(REPOSITORY_ROOT)) if path.is_absolute() else str(path)


def validate_paths() -> list[str]:
    return [f"missing required path: {relative(path)}" for path in REQUIRED_PATHS if not path.exists()]


def validate_mirrors() -> list[str]:
    errors: list[str] = []
    for source, mirror in DEFAULT_INSTRUCTION_MIRRORS:
        if source.read_bytes() != mirror.read_bytes():
            errors.append(
                "default instruction mirror drift: "
                f"{relative(source)} != {relative(mirror)}"
            )
    return errors


def validate_references() -> list[str]:
    errors: list[str] = []
    for path, required_values in REQUIRED_REFERENCES.items():
        content = path.read_text(encoding="utf-8")
        for required_value in required_values:
            if required_value not in content:
                errors.append(
                    f"{relative(path)}: missing required reference "
                    f"{required_value!r}"
                )
    manifest = (REPOSITORY_ROOT / "home/index/manifest.yml").read_text(
        encoding="utf-8"
    )
    for required_value in MANIFEST_REFERENCES:
        if required_value not in manifest:
            errors.append(
                "home/index/manifest.yml: missing instruction-system wiring "
                f"{required_value!r}"
            )
    return errors


def validate_config_root_coverage() -> list[str]:
    try:
        schema = json.loads(
            (REPOSITORY_ROOT / "schemas/config.schema.json").read_text(
                encoding="utf-8"
            )
        )
        config = tomllib.loads(
            (REPOSITORY_ROOT / "home/config.toml").read_text(encoding="utf-8")
        )
    except (OSError, json.JSONDecodeError, tomllib.TOMLDecodeError) as error:
        return [f"cannot inspect home/config.toml root coverage: {error}"]

    properties = schema.get("properties")
    if not isinstance(properties, dict):
        return ["schemas/config.schema.json: expected root properties object"]

    actual_unset = set(properties) - set(config)
    if actual_unset == INTENTIONALLY_UNSET_ROOT_KEYS:
        return []

    errors: list[str] = []
    unclassified = sorted(actual_unset - INTENTIONALLY_UNSET_ROOT_KEYS)
    unexpectedly_assigned = sorted(INTENTIONALLY_UNSET_ROOT_KEYS - actual_unset)
    if unclassified:
        errors.append(
            "home/config.toml: schema root keys lack an active setting or "
            "intentional-unset classification: "
            + ", ".join(unclassified)
        )
    if unexpectedly_assigned:
        errors.append(
            "home/config.toml: intentional-unset policy is stale; these keys "
            "are now assigned and must leave the policy set: "
            + ", ".join(unexpectedly_assigned)
        )
    return errors


def main() -> int:
    errors = validate_paths()
    if not errors:
        errors.extend(validate_mirrors())
        errors.extend(validate_references())
        errors.extend(validate_config_root_coverage())

    if errors:
        print("Runtime-pack asset validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    print(
        "Runtime-pack asset validation passed: "
        f"{len(DEFAULT_INSTRUCTION_MIRRORS)} default mirrors and "
        f"{len(REQUIRED_REFERENCES)} cross-link contracts; "
        f"{len(INTENTIONALLY_UNSET_ROOT_KEYS)} schema root keys are "
        "intentionally unset."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
