#!/usr/bin/env python3
"""Create or overwrite a plan markdown file in $CODEX_HOME/plans."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from plan_utils import (
    get_save_plans_dir,
    list_templates,
    load_template,
    validate_plan_name,
)


def read_body(args: argparse.Namespace) -> str | None:
    if args.body_file:
        body_path = Path(args.body_file).expanduser()
        if not body_path.is_file():
            raise SystemExit(f"Body file not found: {body_path}")
        return body_path.read_text(encoding="utf-8")
    if args.template:
        return load_template(args.template)
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a plan file under $CODEX_HOME/plans."
    )
    parser.add_argument("--name", help="Plan name (lower-case, hyphen-delimited).")
    parser.add_argument("--description", help="Short plan description.")
    parser.add_argument(
        "--short-description",
        help="Short description for metadata (defaults to description).",
    )
    parser.add_argument(
        "--tags",
        help="Comma-separated tag list for metadata (default: plan).",
    )
    parser.add_argument(
        "--version",
        default="1.0",
        help="Metadata version (default: 1.0).",
    )
    parser.add_argument(
        "--body-file",
        help="Path to markdown body (without frontmatter). If omitted, read from stdin.",
    )
    parser.add_argument(
        "--template",
        help=(
            "Template kind: implementation|overview|framework:<name>|"
            "workflow:<name>|skill:<name>|path:<relative>"
        ),
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite the plan file if it already exists.",
    )
    parser.add_argument(
        "--list-templates",
        action="store_true",
        help="List available templates and exit.",
    )
    args = parser.parse_args()

    if args.list_templates:
        try:
            templates = list_templates()
        except ValueError as exc:
            raise SystemExit(str(exc))
        for item in templates:
            print(item)
        return 0

    if not args.name or not args.description:
        raise SystemExit("Provide --name and --description (or use --list-templates).")
    name = args.name.strip()
    description = args.description.strip()
    validate_plan_name(name)
    if not description or "\n" in description:
        raise SystemExit("Description must be a single line.")

    short_description = (args.short_description or description).strip()
    tags = [tag.strip() for tag in (args.tags or "plan").split(",") if tag.strip()]
    if not short_description or "\n" in short_description:
        raise SystemExit("Short description must be a single line.")
    if not tags:
        raise SystemExit("At least one metadata tag is required.")

    try:
        body = read_body(args)
    except (FileNotFoundError, ValueError) as exc:
        raise SystemExit(str(exc))
    if body is None:
        raise SystemExit("Provide --body-file, stdin, or --template to supply plan content.")

    body = body.strip()
    if not body:
        raise SystemExit("Plan body cannot be empty.")
    if body.lstrip().startswith("---"):
        raise SystemExit("Plan body should not include frontmatter.")

    try:
        plans_dir = get_save_plans_dir()
    except ValueError as exc:
        raise SystemExit(str(exc))
    if not plans_dir.is_absolute():
        raise SystemExit("Resolved plans dir must be absolute.")
    plans_dir.mkdir(parents=True, exist_ok=True)
    plan_path = plans_dir / f"{name}.md"

    if plan_path.exists() and not args.overwrite:
        raise SystemExit(f"Plan already exists: {plan_path}. Use --overwrite to replace.")

    tags_yaml = "\n".join([f"  - {tag}" for tag in tags])
    content = (
        "---\n"
        f"name: {name}\n"
        f"description: {description}\n"
        "metadata:\n"
        f"  version: \"{args.version}\"\n"
        f"  short-description: {short_description}\n"
        "  tags:\n"
        f"{tags_yaml}\n"
        "---\n\n"
        f"{body}\n"
    )
    plan_path.write_text(content, encoding="utf-8")
    print(str(plan_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
