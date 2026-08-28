#!/usr/bin/env python3
"""Validate local plugin sources and their versioned runtime mirrors."""

from __future__ import annotations

import copy
import json
import re
import stat
import subprocess
import sys
import tomllib
from pathlib import Path, PurePosixPath
from typing import Any


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
HOME_ROOT = REPOSITORY_ROOT / "home"
CONFIG_PATH = HOME_ROOT / "config.toml"
MARKETPLACES_ROOT = HOME_ROOT / "marketplaces"
RUNTIME_CACHE_ROOT = HOME_ROOT / "plugins" / "cache"
MANAGED_MARKETPLACE_PATH = HOME_ROOT / ".agents" / "plugins" / "marketplace.json"
PROTECTED_HOME_PATHS = frozenset({HOME_ROOT / "auth.json"})
INSTALLED_HOME = PurePosixPath("/data/codex/usr/home")
VERSION_PATTERN = re.compile(r"^[0-9]+(?:\.[0-9]+){1,3}(?:[-+][A-Za-z0-9.-]+)?$")
PLUGIN_BINDING_PATTERN = re.compile(
    r"^([A-Za-z0-9._-]+)@([A-Za-z0-9._-]+)$"
)
RUNTIME_LOCAL_REFERENCE = re.compile(
    rb"(?:\$CODEX_HOME|/data/codex/usr/home)/plugins/cache/"
    rb"[^/\s`\"']+/[^/\s`\"']+/local(?:/|(?=[\s`\"']|$))"
)


class ValidationError(ValueError):
    """Raised when plugin metadata or a runtime mirror is inconsistent."""


def load_json_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"cannot parse JSON object {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValidationError(f"JSON root must be an object: {path}")
    return value


def safe_source_root(marketplace_root: Path, raw_path: Any) -> Path:
    if not isinstance(raw_path, str) or not raw_path.startswith("./"):
        raise ValidationError(f"marketplace source path must start with './': {raw_path!r}")
    relative = PurePosixPath(raw_path.removeprefix("./"))
    if relative.is_absolute() or ".." in relative.parts:
        raise ValidationError(f"unsafe marketplace source path: {raw_path!r}")
    source = marketplace_root.joinpath(*relative.parts)
    try:
        source.resolve().relative_to(marketplace_root.resolve())
    except ValueError as exc:
        raise ValidationError(f"marketplace source escapes its root: {raw_path!r}") from exc
    return source


def regular_file_inventory(root: Path) -> dict[PurePosixPath, tuple[bytes, int]]:
    if not root.is_dir() or root.is_symlink():
        raise ValidationError(f"plugin bundle root is missing or indirect: {root}")
    inventory: dict[PurePosixPath, tuple[bytes, int]] = {}
    for path in sorted(root.rglob("*")):
        relative = PurePosixPath(path.relative_to(root).as_posix())
        if path.is_symlink():
            raise ValidationError(f"plugin bundle contains a symlink: {root / relative}")
        if path.is_dir():
            continue
        if not path.is_file():
            raise ValidationError(f"plugin bundle contains a special file: {root / relative}")
        mode = stat.S_IMODE(path.stat().st_mode)
        inventory[relative] = (path.read_bytes(), mode)
    return inventory


def expected_managed_marketplace(
    source_metadata: dict[str, Any],
    versions: dict[str, str],
) -> dict[str, Any]:
    managed = copy.deepcopy(source_metadata)
    plugins = managed.get("plugins")
    if not isinstance(plugins, list):
        raise ValidationError("codex-home marketplace plugins must be an array")
    for entry in plugins:
        if not isinstance(entry, dict) or not isinstance(entry.get("name"), str):
            raise ValidationError("codex-home marketplace has an invalid plugin entry")
        name = entry["name"]
        source = entry.get("source")
        if not isinstance(source, dict) or name not in versions:
            raise ValidationError(f"codex-home marketplace source is invalid for {name}")
        source["path"] = f"./plugins/cache/codex-home/{name}/{versions[name]}"
    return managed


def validate_skill_metadata(source: Path) -> tuple[int, int]:
    skill_files = sorted(source.glob("skills/*/SKILL.md"))
    if not skill_files:
        raise ValidationError(f"plugin exposes no skills: {source}")
    metadata_files = []
    for skill_file in skill_files:
        metadata = skill_file.parent / "agents" / "openai.yaml"
        if not metadata.is_file() or metadata.is_symlink():
            raise ValidationError(f"skill metadata is missing or indirect: {metadata}")
        if not metadata.read_bytes().strip():
            raise ValidationError(f"skill metadata is empty: {metadata}")
        metadata_files.append(metadata)
    return len(skill_files), len(metadata_files)


def validate_runtime_references() -> int:
    failures: list[str] = []
    checked = 0
    try:
        listing = subprocess.run(
            [
                "git",
                "ls-files",
                "-z",
                "--cached",
                "--others",
                "--exclude-standard",
                "--",
                "home",
            ],
            cwd=REPOSITORY_ROOT,
            check=True,
            stdout=subprocess.PIPE,
        ).stdout
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ValidationError(f"cannot enumerate repository home files: {exc}") from exc

    paths: list[Path] = []
    for raw_path in listing.split(b"\0"):
        if not raw_path:
            continue
        try:
            relative = PurePosixPath(raw_path.decode("utf-8"))
        except UnicodeDecodeError as exc:
            raise ValidationError("repository contains a non-UTF-8 home path") from exc
        if (
            relative.is_absolute()
            or ".." in relative.parts
            or not relative.parts
            or relative.parts[0] != "home"
        ):
            raise ValidationError(f"unsafe repository home path: {relative}")
        paths.append(REPOSITORY_ROOT.joinpath(*relative.parts))

    for path in sorted(set(paths)):
        if path in PROTECTED_HOME_PATHS:
            continue
        if not path.is_file() or path.is_symlink():
            continue
        checked += 1
        try:
            content = path.read_bytes()
        except OSError as exc:
            failures.append(f"cannot read {path}: {exc}")
            continue
        if RUNTIME_LOCAL_REFERENCE.search(content):
            failures.append(f"runtime-facing local cache reference remains in {path}")
    if failures:
        raise ValidationError("\n".join(failures))
    return checked


def run() -> int:
    try:
        config = tomllib.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        configured_marketplaces = config.get("marketplaces", {})
        configured_plugins = config.get("plugins", {})
        if not isinstance(configured_marketplaces, dict):
            raise ValidationError("config.toml marketplaces must be a table")
        if not isinstance(configured_plugins, dict):
            raise ValidationError("config.toml plugins must be a table")

        enabled_plugin_marketplaces: dict[str, list[str]] = {}
        for binding, settings in sorted(configured_plugins.items()):
            match = PLUGIN_BINDING_PATTERN.fullmatch(binding)
            if match is None or not isinstance(settings, dict):
                raise ValidationError(f"invalid plugin binding in config.toml: {binding!r}")
            if settings.get("enabled") is not True:
                continue
            bundle, marketplace = match.groups()
            if marketplace not in configured_marketplaces:
                raise ValidationError(
                    f"enabled plugin references an unconfigured marketplace: {binding}"
                )
            enabled_plugin_marketplaces.setdefault(bundle, []).append(marketplace)
        ambiguous = {
            bundle: marketplaces
            for bundle, marketplaces in enabled_plugin_marketplaces.items()
            if len(marketplaces) != 1
        }
        if ambiguous:
            raise ValidationError(
                f"enabled plugin bundles must resolve to one marketplace: {ambiguous}"
            )

        plugin_count = 0
        skill_count = 0
        metadata_count = 0
        codex_home_metadata: dict[str, Any] | None = None
        codex_home_versions: dict[str, str] = {}
        local_bindings: set[str] = set()
        local_marketplaces: set[str] = set()

        for marketplace, settings in sorted(configured_marketplaces.items()):
            if not isinstance(settings, dict) or settings.get("source_type") != "local":
                continue
            local_marketplaces.add(marketplace)
            expected_source = str(INSTALLED_HOME / "marketplaces" / marketplace)
            if settings.get("source") != expected_source:
                raise ValidationError(
                    f"local marketplace {marketplace} must use {expected_source}"
                )
            marketplace_root = MARKETPLACES_ROOT / marketplace
            metadata_path = marketplace_root / ".agents" / "plugins" / "marketplace.json"
            metadata = load_json_object(metadata_path)
            if metadata.get("name") != marketplace:
                raise ValidationError(f"marketplace name mismatch in {metadata_path}")
            entries = metadata.get("plugins")
            if not isinstance(entries, list):
                raise ValidationError(f"marketplace plugins must be an array: {metadata_path}")

            seen: set[str] = set()
            expected_bundles: set[str] = set()
            for entry in entries:
                if not isinstance(entry, dict):
                    raise ValidationError(f"invalid marketplace plugin entry in {metadata_path}")
                name = entry.get("name")
                if not isinstance(name, str) or not name or name in seen:
                    raise ValidationError(f"invalid or duplicate plugin name in {metadata_path}: {name!r}")
                seen.add(name)
                expected_bundles.add(name)

                source_settings = entry.get("source")
                if not isinstance(source_settings, dict) or source_settings.get("source") != "local":
                    raise ValidationError(f"plugin {name}@{marketplace} must use a local source")
                expected_relative = f"./plugins/cache/{marketplace}/{name}/local"
                if source_settings.get("path") != expected_relative:
                    raise ValidationError(
                        f"plugin {name}@{marketplace} source must be {expected_relative}"
                    )
                source = safe_source_root(marketplace_root, source_settings.get("path"))
                manifest_path = source / ".codex-plugin" / "plugin.json"
                manifest = load_json_object(manifest_path)
                version = manifest.get("version")
                if manifest.get("name") != name:
                    raise ValidationError(f"manifest name mismatch: {manifest_path}")
                if not isinstance(version, str) or VERSION_PATTERN.fullmatch(version) is None:
                    raise ValidationError(f"invalid manifest version in {manifest_path}: {version!r}")
                skills_path = manifest.get("skills")
                if skills_path != "./skills":
                    raise ValidationError(f"manifest skills path must be './skills': {manifest_path}")

                binding = configured_plugins.get(f"{name}@{marketplace}")
                if not isinstance(binding, dict) or binding.get("enabled") is not True:
                    raise ValidationError(f"plugin is not enabled in config.toml: {name}@{marketplace}")
                local_bindings.add(f"{name}@{marketplace}")

                runtime_bundle = RUNTIME_CACHE_ROOT / marketplace / name
                if not runtime_bundle.is_dir() or runtime_bundle.is_symlink():
                    raise ValidationError(
                        f"runtime bundle root is missing or indirect: {runtime_bundle}"
                    )
                runtime_children = list(runtime_bundle.iterdir())
                invalid_children = sorted(
                    child.name
                    for child in runtime_children
                    if child.is_symlink() or not child.is_dir()
                )
                if invalid_children:
                    raise ValidationError(
                        f"runtime bundle contains invalid entries in {runtime_bundle}: "
                        f"{invalid_children}"
                    )
                installed_versions = {child.name for child in runtime_children}
                if installed_versions != {version}:
                    raise ValidationError(
                        f"runtime bundle versions for {name}@{marketplace} must be "
                        f"[{version!r}], found {sorted(installed_versions)}"
                    )
                runtime = runtime_bundle / version
                source_inventory = regular_file_inventory(source)
                runtime_inventory = regular_file_inventory(runtime)
                if source_inventory != runtime_inventory:
                    source_only = sorted(source_inventory.keys() - runtime_inventory.keys())
                    runtime_only = sorted(runtime_inventory.keys() - source_inventory.keys())
                    changed = sorted(
                        path
                        for path in source_inventory.keys() & runtime_inventory.keys()
                        if source_inventory[path] != runtime_inventory[path]
                    )
                    details = []
                    if source_only:
                        details.append(f"source-only={source_only[:5]}")
                    if runtime_only:
                        details.append(f"runtime-only={runtime_only[:5]}")
                    if changed:
                        details.append(f"changed={changed[:5]}")
                    raise ValidationError(
                        f"runtime mirror differs for {name}@{marketplace}: {'; '.join(details)}"
                    )

                skills, metadata_files = validate_skill_metadata(source)
                plugin_count += 1
                skill_count += skills
                metadata_count += metadata_files
                if marketplace == "codex-home":
                    codex_home_versions[name] = version

            runtime_marketplace = RUNTIME_CACHE_ROOT / marketplace
            runtime_entries = list(runtime_marketplace.iterdir())
            invalid_bundles = sorted(
                path.name
                for path in runtime_entries
                if path.is_symlink() or not path.is_dir()
            )
            if invalid_bundles:
                raise ValidationError(
                    f"runtime marketplace contains invalid entries in "
                    f"{runtime_marketplace}: {invalid_bundles}"
                )
            actual_bundles = {path.name for path in runtime_entries}
            if actual_bundles != expected_bundles:
                raise ValidationError(
                    f"runtime bundles in {runtime_marketplace} differ: "
                    f"expected={sorted(expected_bundles)}, "
                    f"actual={sorted(actual_bundles)}"
                )
            if marketplace == "codex-home":
                codex_home_metadata = metadata

        enabled_local_bindings = {
            f"{bundle}@{marketplaces[0]}"
            for bundle, marketplaces in enabled_plugin_marketplaces.items()
            if marketplaces[0] in local_marketplaces
        }
        if enabled_local_bindings != local_bindings:
            raise ValidationError(
                "enabled local plugin bindings differ from marketplace metadata: "
                f"configured={sorted(enabled_local_bindings)}, "
                f"catalog={sorted(local_bindings)}"
            )

        if codex_home_metadata is None:
            raise ValidationError("codex-home local marketplace is not configured")
        expected_managed = expected_managed_marketplace(
            codex_home_metadata,
            codex_home_versions,
        )
        actual_managed = load_json_object(MANAGED_MARKETPLACE_PATH)
        if actual_managed != expected_managed:
            raise ValidationError(
                f"managed marketplace metadata is stale: {MANAGED_MARKETPLACE_PATH}"
            )

        checked_files = validate_runtime_references()
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError, ValidationError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(
        "Plugin catalog coverage is valid: "
        f"{plugin_count} plugins, {skill_count} skills, "
        f"{metadata_count} agents/openai.yaml files, and "
        f"{checked_files} repository home files checked for stale runtime paths."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
