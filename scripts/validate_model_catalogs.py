#!/usr/bin/env python3
"""Validate static model-catalog capability metadata and profile compatibility."""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path
from typing import Any


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CATALOG_RELATIVE_PATHS = (
    Path("instructions/models/default_catalog.json"),
    Path("instructions/default/models/default_catalog.json"),
    Path("instructions/agents/models/default_catalog.json"),
    Path("instructions/profiles/cyber/models/default_catalog.json"),
    Path("instructions/profiles/debug/models/default_catalog.json"),
    Path("instructions/profiles/fast/models/default_catalog.json"),
    Path("instructions/profiles/review/models/default_catalog.json"),
    Path("instructions/profiles/test/models/default_catalog.json"),
    Path("home/.models/default_catalog.json"),
    Path("home/.models/instructions/models/default_catalog.json"),
)
CATALOG_ROOTS = (
    Path("instructions"),
    Path("home/.models"),
)
CODE_MODE_MODELS = frozenset(
    {
        "gpt-5.6-sol",
        "gpt-5.6-terra",
        "gpt-5.6-luna",
    }
)
VALID_TOOL_MODES = frozenset({"direct", "code_mode", "code_mode_only"})
NON_CODE_MODE_PROFILE_CONFIGS = {
    Path("home/fast.config.toml"): "gpt-5.4-mini",
    Path("home/review.config.toml"): "gpt-5.4",
    Path("home/cyber.config.toml"): "gpt-5.5-cyber",
    Path("home/spark.config.toml"): "gpt-5.3-codex-spark",
}
CODE_MODE_FEATURES = (
    "code_mode",
    "code_mode_only",
    "code_mode_buffered_exec",
    "code_mode_host",
    "code_mode_interrupt",
)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"{path.relative_to(REPOSITORY_ROOT)}: {error}") from error


def catalog_relative_paths() -> tuple[Path, ...]:
    paths: set[Path] = set()
    for root in CATALOG_ROOTS:
        for path in (REPOSITORY_ROOT / root).rglob("*catalog.json"):
            if path.is_file():
                paths.add(path.relative_to(REPOSITORY_ROOT))
    return tuple(sorted(paths))


def validate_catalog(path: Path, *, require_code_mode_models: bool) -> list[str]:
    errors: list[str] = []
    try:
        catalog = load_json(path)
    except ValueError as error:
        return [str(error)]

    models = catalog.get("models") if isinstance(catalog, dict) else None
    if not isinstance(models, list) or not models:
        return [f"{path.relative_to(REPOSITORY_ROOT)}: expected a non-empty models array"]

    by_slug: dict[str, dict[str, Any]] = {}
    for index, model in enumerate(models):
        if not isinstance(model, dict):
            errors.append(
                f"{path.relative_to(REPOSITORY_ROOT)}: models[{index}] is not an object"
            )
            continue
        slug = model.get("slug")
        if not isinstance(slug, str) or not slug:
            errors.append(
                f"{path.relative_to(REPOSITORY_ROOT)}: models[{index}] has no slug"
            )
            continue
        if slug in by_slug:
            errors.append(
                f"{path.relative_to(REPOSITORY_ROOT)}: duplicate model slug {slug!r}"
            )
            continue
        by_slug[slug] = model
        tool_mode = model.get("tool_mode")
        if tool_mode is not None and tool_mode not in VALID_TOOL_MODES:
            errors.append(
                f"{path.relative_to(REPOSITORY_ROOT)}: {slug!r} has invalid "
                f"tool_mode {tool_mode!r}"
            )

    if require_code_mode_models:
        for slug in sorted(CODE_MODE_MODELS):
            model = by_slug.get(slug)
            if model is None:
                errors.append(
                    f"{path.relative_to(REPOSITORY_ROOT)}: missing required "
                    f"model {slug!r}"
                )
            elif model.get("tool_mode") != "code_mode_only":
                errors.append(
                    f"{path.relative_to(REPOSITORY_ROOT)}: {slug!r} must declare "
                    'tool_mode = "code_mode_only"'
                )
    return errors


def validate_non_code_mode_profile(path: Path, expected_model: str) -> list[str]:
    try:
        config = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        return [f"{path.relative_to(REPOSITORY_ROOT)}: {error}"]

    errors: list[str] = []
    if config.get("model") != expected_model:
        errors.append(
            f"{path.relative_to(REPOSITORY_ROOT)}: expected model {expected_model!r}"
        )
    features = config.get("features")
    if not isinstance(features, dict):
        return [
            *errors,
            f"{path.relative_to(REPOSITORY_ROOT)}: missing [features] override",
        ]
    for feature in CODE_MODE_FEATURES:
        if features.get(feature) is not False:
            errors.append(
                f"{path.relative_to(REPOSITORY_ROOT)}: features.{feature} "
                "must be false for a model that does not advertise Code Mode"
            )
    return errors


def main() -> int:
    errors: list[str] = []
    catalog_paths = catalog_relative_paths()
    expected_default_paths = set(DEFAULT_CATALOG_RELATIVE_PATHS)
    missing_default_paths = expected_default_paths - set(catalog_paths)
    for relative_path in sorted(missing_default_paths):
        errors.append(f"missing required default catalog: {relative_path}")
    for relative_path in catalog_paths:
        errors.extend(
            validate_catalog(
                REPOSITORY_ROOT / relative_path,
                require_code_mode_models=relative_path in expected_default_paths,
            )
        )
    for relative_path, model in NON_CODE_MODE_PROFILE_CONFIGS.items():
        errors.extend(validate_non_code_mode_profile(REPOSITORY_ROOT / relative_path, model))

    if errors:
        print("Model catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    print(
        "Model catalog validation passed: "
        f"{len(catalog_paths)} catalogs "
        f"({len(DEFAULT_CATALOG_RELATIVE_PATHS)} default catalogs) and "
        f"{len(NON_CODE_MODE_PROFILE_CONFIGS)} non-Code-Mode profiles."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
