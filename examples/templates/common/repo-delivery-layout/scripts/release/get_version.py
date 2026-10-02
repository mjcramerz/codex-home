#!/usr/bin/env python3
"""Read an application or release version from common project files.

Supported formats:
- auto (default): infer from file name/extension
- plain: first non-empty line, or regex fallback
- json: read dotted key path (default: version)
- toml: read dotted key path (common defaults)
- yaml: read key value from simple key: value lines
- regex: read first capture group from --pattern
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
    parser = argparse.ArgumentParser(description="Read app/release version from project files")
    parser.add_argument("--file", help="File to read version from")
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


def extract_json(text: str, key_path: str) -> str:
    data = json.loads(text)
    value = get_nested(data, key_path)
    if not isinstance(value, str):
        raise ValueError(f"json key is not a string: {key_path}")
    return normalize_version(value)


def toml_key_paths(path: Path, key: str | None) -> list[str]:
    if key:
        return [key]
    if path.name == "Cargo.toml":
        return ["workspace.package.version", "package.version"]
    if path.name == "pyproject.toml":
        return ["project.version", "tool.poetry.version"]
    return ["project.version", "package.version", "version"]


def extract_toml(text: str, key_paths: list[str]) -> str:
    data = tomllib.loads(text)
    for key_path in key_paths:
        try:
            value = get_nested(data, key_path)
        except KeyError:
            continue
        if isinstance(value, str):
            return normalize_version(value)
    raise ValueError(f"no matching toml version key found (tried: {', '.join(key_paths)})")


def yaml_keys(key: str | None) -> list[str]:
    if key:
        return [key]
    return ["RELEASE_VERSION", "APP_VERSION", "VERSION", "version"]


def extract_yaml(text: str, keys: list[str]) -> str:
    for key in keys:
        pattern = re.compile(
            rf"^\s*{re.escape(key)}\s*:\s*['\"]?([^'\"#\n]+)['\"]?\s*(?:#.*)?$"
        )
        for line in text.splitlines():
            match = pattern.match(line)
            if match:
                return normalize_version(match.group(1))
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


def extract_regex(text: str, pattern: str) -> str:
    match = re.search(pattern, text)
    if not match:
        raise ValueError("regex pattern did not match")
    group = match.group(1) if match.lastindex else match.group(0)
    return normalize_version(group)


def find_default_file(repo_root: Path) -> Path:
    for rel in DEFAULT_CANDIDATES:
        candidate = repo_root / rel
        if candidate.is_file():
            return candidate
    names = ", ".join(DEFAULT_CANDIDATES)
    raise ValueError(f"no default version file found in {repo_root} (checked: {names})")


def read_version(path: Path, fmt: str, key: str | None, pattern: str) -> str:
    text = read_text_bounded(path)
    mode = detect_format(path, fmt)
    if mode == "json":
        return extract_json(text, key or "version")
    if mode == "toml":
        return extract_toml(text, toml_key_paths(path, key))
    if mode == "yaml":
        return extract_yaml(text, yaml_keys(key))
    if mode == "plain":
        return extract_plain(text, pattern)
    if mode == "regex":
        return extract_regex(text, pattern)
    raise ValueError(f"unsupported format: {mode}")


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    try:
        if args.file:
            path = Path(args.file)
            if not path.exists() or not path.is_file():
                raise ValueError(f"missing file: {path}")
        else:
            repo_root = Path(args.repo_root)
            if not repo_root.exists() or not repo_root.is_dir():
                raise ValueError(f"missing repo root: {repo_root}")
            path = find_default_file(repo_root)

        version = read_version(path, args.format, args.key, args.pattern)
    except (json.JSONDecodeError, OSError, tomllib.TOMLDecodeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    print(version)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
