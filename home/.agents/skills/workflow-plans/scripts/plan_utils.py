#!/usr/bin/env python3
"""Shared helpers for plan scripts."""

from __future__ import annotations

import os
import re
from pathlib import Path

_NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

def _get_absolute_env_path(name: str) -> Path | None:
    value = os.environ.get(name)
    if not value:
        return None
    resolved = Path(value).expanduser()
    if not resolved.is_absolute():
        raise ValueError(f"{name} must be absolute: {resolved}")
    return resolved.resolve(strict=False)


def _require_absolute_env_path(name: str) -> Path:
    resolved = _get_absolute_env_path(name)
    if resolved is None:
        raise ValueError(f"{name} must be set to an absolute path")
    return resolved


def get_codex_home_pack() -> Path:
    """Return CODEX_HOME for source save/update paths."""
    return _require_absolute_env_path("CODEX_HOME")


def get_codex_home_runtime() -> Path:
    """Return CODEX_HOME for read/list/template discovery paths.

    Falls back to CODEX_HOME when CODEX_HOME is not set.
    """
    runtime = _get_absolute_env_path("CODEX_HOME")
    if runtime is not None:
        return runtime
    pack = _get_absolute_env_path("CODEX_HOME")
    if pack is not None:
        return pack
    raise ValueError("CODEX_HOME (or fallback CODEX_HOME) must be set to an absolute path")


def get_read_plans_dir() -> Path:
    """Return CODEX_HOME/plans for listing/reading (fallback: CODEX_HOME/plans)."""
    return get_codex_home_runtime() / "plans"


def get_save_plans_dir() -> Path:
    """Return CODEX_HOME/plans for saving."""
    return get_codex_home_pack() / "plans"


def validate_plan_name(name: str) -> None:
    if not name or not _NAME_RE.match(name):
        raise ValueError(
            "Invalid plan name. Use short, lower-case, hyphen-delimited names "
            "(e.g., codex-rate-limit-overview)."
        )


def parse_frontmatter(path: Path) -> dict:
    """Parse YAML frontmatter from a markdown file without reading the body."""
    with path.open("r", encoding="utf-8") as handle:
        first = handle.readline()
        if first.strip() != "---":
            raise ValueError("Frontmatter must start with '---'.")

        data: dict[str, str] = {}
        for line in handle:
            if line[:1].isspace():
                continue
            stripped = line.strip()
            if stripped == "---":
                return data
            if not stripped or stripped.startswith("#"):
                continue
            if ":" not in line:
                raise ValueError(f"Invalid frontmatter line: {line.rstrip()}")
            key, value = line.split(":", 1)
            key = key.strip()
            if not key or " " in key or "\t" in key:
                raise ValueError(f"Invalid frontmatter key: {key!r}")
            if key in data:
                raise ValueError(f"Duplicate frontmatter key: {key}")
            value = value.strip()
            if value and len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
                value = value[1:-1]
            data[key] = value

    raise ValueError("Frontmatter must end with '---'.")


def load_plan_template(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    text = path.read_text(encoding="utf-8")
    if text.lstrip().startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].lstrip("\n")
    return text


def _safe_template_rel(rel: str) -> Path:
    root = get_codex_home_runtime()
    candidate = (root / rel).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError("Template path must stay within the pack root") from exc
    return candidate


def load_template(kind: str) -> str:
    root = get_codex_home_runtime()
    if kind == "implementation":
        return load_plan_template(root / "plans" / "frameworks" / "plan-feature-delivery.md")
    if kind == "overview":
        return load_plan_template(root / "plans" / "frameworks" / "plan-docs-and-runbook.md")
    if kind.startswith("framework:"):
        key = kind.split(":", 1)[1]
        return load_plan_template(root / "plans" / "frameworks" / f"{key}.md")
    if kind.startswith("workflow:"):
        key = kind.split(":", 1)[1]
        return load_plan_template(root / "plans" / "workflows" / f"workflow-{key}.md")
    if kind.startswith("skill:"):
        key = kind.split(":", 1)[1]
        return load_plan_template(root / "plans" / "skills" / f"skill-{key}.md")
    if kind.startswith("path:"):
        rel = kind.split(":", 1)[1]
        return load_plan_template(_safe_template_rel(rel))
    raise ValueError(f"Unknown template kind: {kind}")


def list_templates() -> list[str]:
    root = get_codex_home_runtime()
    items = ["implementation", "overview"]
    for p in (root / "plans" / "frameworks").glob("*.md"):
        if p.name != "overview.md":
            items.append(f"framework:{p.stem}")
    for p in (root / "plans" / "workflows").glob("workflow-*.md"):
        items.append(f"workflow:{p.stem.replace('workflow-', '')}")
    for p in (root / "plans" / "skills").glob("skill-*.md"):
        items.append(f"skill:{p.stem.replace('skill-', '')}")
    return items
