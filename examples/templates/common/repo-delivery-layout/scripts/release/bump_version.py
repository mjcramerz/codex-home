#!/usr/bin/env python3
"""Set an application or release version in common project files.

Supported formats:
- auto (default): infer from file name/extension
- plain: replace first non-empty line
- json: write dotted key path (default: version)
- toml: update common dotted key paths in-place
- yaml: update simple key: value lines
- regex: replace first capture group from --pattern
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import tomllib
from typing import Any

MAX_FILE_BYTES = 2_000_000
MAX_VERSION_LEN = 128
SEMVER_PATTERN = r"([0-9]+\.[0-9]+\.[0-9]+(?:[-+][0-9A-Za-z.-]+)?)"
DEFAULT_CANDIDATES = (
    "VERSION",
    ".version",
    "package.json",
    "pyproject.toml",
    "Cargo.toml",
    ".gitlab-ci.yml",
    ".gitlab-ci.yaml",
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Set app/release version in project files")
    parser.add_argument("--version", required=True, help="Version value to set")
    parser.add_argument("--file", help="Target file to modify")
    parser.add_argument(
        "--format",
        choices=("auto", "plain", "json", "toml", "yaml", "regex"),
        default="auto",
        help="Input format (default: auto)",
    )
    parser.add_argument(
        "--key",
        help="Dotted key for json/toml/yaml formats (defaults depend on file type)",
    )
    parser.add_argument(
        "--pattern",
        default=SEMVER_PATTERN,
        help="Regex pattern used by regex mode (must include one capture group)",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root used to discover default candidate files",
    )
    parser.add_argument(
        "--replace-file",
        action="append",
        default=[],
        help="Optional additional files for old->new token replacement",
    )
    return parser.parse_args(argv)


def read_text_bounded(path: Path) -> str:
    size = path.stat().st_size
    if size > MAX_FILE_BYTES:
        raise ValueError(f"{path} exceeds {MAX_FILE_BYTES} bytes")
    return path.read_text(encoding="utf-8")


def normalize_version(raw: str) -> str:
    value = raw.strip().strip("\"'").strip()
    if not value:
        raise ValueError("version value is empty")
    if len(value) > MAX_VERSION_LEN:
        raise ValueError(f"version value exceeds {MAX_VERSION_LEN} chars")
    if any(char in value for char in ("\x00", "\n", "\r")):
        raise ValueError("version value contains control characters")
    return value


def detect_format(path: Path, requested: str) -> str:
    if requested != "auto":
        return requested
    name = path.name.lower()
    suffix = path.suffix.lower()
    if suffix == ".json":
        return "json"
    if suffix == ".toml":
        return "toml"
    if suffix in (".yml", ".yaml"):
        return "yaml"
    if name in {"version", ".version"}:
        return "plain"
    return "regex"


def get_nested(mapping: Any, key_path: str) -> Any:
    current: Any = mapping
    for part in key_path.split("."):
        if not isinstance(current, dict) or part not in current:
            raise KeyError(key_path)
        current = current[part]
    return current


def set_nested(mapping: Any, key_path: str, value: str) -> bool:
    current: Any = mapping
    parts = key_path.split(".")
    for part in parts[:-1]:
        if not isinstance(current, dict) or part not in current:
            raise KeyError(key_path)
        current = current[part]
    if not isinstance(current, dict):
        raise KeyError(key_path)
    leaf = parts[-1]
    old = current.get(leaf)
    if not isinstance(old, str):
        raise ValueError(f"key is not a string: {key_path}")
    if old == value:
        return False
    current[leaf] = value
    return True


def toml_key_paths(path: Path, key: str | None) -> list[str]:
    if key:
        return [key]
    if path.name == "Cargo.toml":
        return ["workspace.package.version", "package.version"]
    if path.name == "pyproject.toml":
        return ["project.version", "tool.poetry.version"]
    return ["project.version", "package.version", "version"]


def yaml_keys(key: str | None) -> list[str]:
    if key:
        return [key]
    return ["RELEASE_VERSION", "APP_VERSION", "VERSION", "version"]


def extract_yaml(text: str, keys: list[str]) -> tuple[str, str]:
    for key in keys:
        pattern = re.compile(
            rf"^\s*{re.escape(key)}\s*:\s*['\"]?([^'\"#\n]+)['\"]?\s*(?:#.*)?$"
        )
        for line in text.splitlines():
            match = pattern.match(line)
            if match:
                return key, normalize_version(match.group(1))
    raise ValueError(f"no matching yaml version key found (tried: {', '.join(keys)})")


def extract_plain(text: str, pattern: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" in stripped:
            _, right = stripped.split("=", 1)
            candidate = right.strip()
            if candidate:
                return normalize_version(candidate)
        return normalize_version(stripped)

    match = re.search(pattern, text)
    if match:
        group = match.group(1) if match.lastindex else match.group(0)
        return normalize_version(group)

    raise ValueError("no plain-text version value found")


def extract_regex(text: str, pattern: str) -> tuple[str, tuple[int, int]]:
    match = re.search(pattern, text)
    if not match:
        raise ValueError("regex pattern did not match")
    if not match.lastindex:
        raise ValueError("regex pattern must include one capture group")
    group = normalize_version(match.group(1))
    return group, match.span(1)


def find_default_file(repo_root: Path) -> Path:
    for rel in DEFAULT_CANDIDATES:
        candidate = repo_root / rel
        if candidate.is_file():
            return candidate
    names = ", ".join(DEFAULT_CANDIDATES)
    raise ValueError(f"no default version file found in {repo_root} (checked: {names})")


def read_current_version(path: Path, mode: str, key: str | None, pattern: str) -> str:
    text = read_text_bounded(path)
    if mode == "json":
        data = json.loads(text)
        value = get_nested(data, key or "version")
        if not isinstance(value, str):
            raise ValueError(f"json key is not a string: {key or 'version'}")
        return normalize_version(value)
    if mode == "toml":
        data = tomllib.loads(text)
        for key_path in toml_key_paths(path, key):
            try:
                value = get_nested(data, key_path)
            except KeyError:
                continue
            if isinstance(value, str):
                return normalize_version(value)
        raise ValueError("no matching toml version key found")
    if mode == "yaml":
        _, value = extract_yaml(text, yaml_keys(key))
        return value
    if mode == "plain":
        return extract_plain(text, pattern)
    if mode == "regex":
        value, _ = extract_regex(text, pattern)
        return value
    raise ValueError(f"unsupported format: {mode}")


def update_json(path: Path, key_path: str, new_version: str) -> bool:
    text = read_text_bounded(path)
    data = json.loads(text)
    changed = set_nested(data, key_path, new_version)
    if not changed:
        return False
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    return True


def update_toml(path: Path, key_paths: list[str], new_version: str) -> bool:
    text = read_text_bounded(path)
    lines = text.splitlines()

    for key_path in key_paths:
        parts = key_path.split(".")
        section = ".".join(parts[:-1]) if len(parts) > 1 else ""
        field = parts[-1]
        current_section = ""

        for index, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith("[") and stripped.endswith("]"):
                current_section = stripped[1:-1].strip()
                continue
            if current_section != section:
                continue
            if not stripped.startswith(field):
                continue
            match = re.match(rf'(\s*{re.escape(field)}\s*=\s*")([^\"]+)(".*)$', line)
            if not match:
                continue
            old_value = normalize_version(match.group(2))
            if old_value == new_version:
                return False
            lines[index] = f"{match.group(1)}{new_version}{match.group(3)}"
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return True

    joined = ", ".join(key_paths)
    raise ValueError(f"no matching toml key line found (tried: {joined})")


def update_yaml(path: Path, keys: list[str], new_version: str) -> bool:
    text = read_text_bounded(path)
    lines = text.splitlines()

    for key in keys:
        pattern = re.compile(
            rf'^(\s*{re.escape(key)}\s*:\s*)(["\']?)([^"\'#\n]+)(["\']?)(\s*(?:#.*)?)$'
        )
        for index, line in enumerate(lines):
            match = pattern.match(line)
            if not match:
                continue
            old_value = normalize_version(match.group(3))
            if old_value == new_version:
                return False
            quote = match.group(2) if match.group(2) == match.group(4) else ""
            lines[index] = f"{match.group(1)}{quote}{new_version}{quote}{match.group(5)}"
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return True

    joined = ", ".join(keys)
    raise ValueError(f"no matching yaml key line found (tried: {joined})")


def update_plain(path: Path, new_version: str, pattern: str) -> bool:
    text = read_text_bounded(path)
    lines = text.splitlines()

    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        old_value = extract_plain(line + "\n", pattern)
        if old_value == new_version:
            return False
        if "=" in line:
            left, _ = line.split("=", 1)
            lines[index] = f"{left.strip()}={new_version}"
        else:
            lines[index] = new_version
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return True

    raise ValueError("no plain-text version value found")


def update_regex(path: Path, new_version: str, pattern: str) -> bool:
    text = read_text_bounded(path)
    old_value, span = extract_regex(text, pattern)
    if old_value == new_version:
        return False
    updated = text[: span[0]] + new_version + text[span[1] :]
    path.write_text(updated, encoding="utf-8")
    return True


def replace_tokens(path: Path, old_version: str, new_version: str) -> bool:
    text = read_text_bounded(path)
    token = re.compile(rf"(?<![0-9A-Za-z._+-]){re.escape(old_version)}(?![0-9A-Za-z._+-])")
    updated = token.sub(new_version, text)
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    try:
        new_version = normalize_version(args.version)

        if args.file:
            path = Path(args.file)
            if not path.exists() or not path.is_file():
                raise ValueError(f"missing file: {path}")
        else:
            repo_root = Path(args.repo_root)
            if not repo_root.exists() or not repo_root.is_dir():
                raise ValueError(f"missing repo root: {repo_root}")
            path = find_default_file(repo_root)

        mode = detect_format(path, args.format)
        old_version = read_current_version(path, mode, args.key, args.pattern)

        changed_files: list[str] = []
        changed = False

        if mode == "json":
            changed = update_json(path, args.key or "version", new_version)
        elif mode == "toml":
            changed = update_toml(path, toml_key_paths(path, args.key), new_version)
        elif mode == "yaml":
            changed = update_yaml(path, yaml_keys(args.key), new_version)
        elif mode == "plain":
            changed = update_plain(path, new_version, args.pattern)
        elif mode == "regex":
            changed = update_regex(path, new_version, args.pattern)
        else:
            raise ValueError(f"unsupported format: {mode}")

        if changed:
            changed_files.append(str(path))

        for raw in args.replace_file:
            extra = Path(raw)
            if not extra.exists() or not extra.is_file():
                raise ValueError(f"replace file missing: {extra}")
            if replace_tokens(extra, old_version, new_version):
                changed_files.append(str(extra))

    except (json.JSONDecodeError, OSError, tomllib.TOMLDecodeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if changed_files:
        print("Updated files:")
        for item in changed_files:
            print(f" - {item}")
    else:
        print("No changes needed")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
