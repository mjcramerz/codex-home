#!/usr/bin/env python3
"""
Generate or update a TOC in an Obsidian Markdown file.

Defaults:
- Inserts between <!-- TOC START --> and <!-- TOC END --> markers if present.
- Otherwise inserts after YAML frontmatter or at top of file.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


MAX_BYTES = 1_000_000


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    cleaned = re.sub(r"[\s_-]+", "-", cleaned)
    return cleaned


def parse_headings(lines: list[str], max_depth: int) -> list[tuple[int, str]]:
    headings = []
    in_code = False
    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not match:
            continue
        level = len(match.group(1))
        if level > max_depth:
            continue
        title = match.group(2).strip()
        headings.append((level, title))
    return headings


def build_toc(headings: list[tuple[int, str]]) -> list[str]:
    toc_lines = []
    for level, title in headings:
        indent = "  " * (level - 1)
        toc_lines.append(f"{indent}- [{title}](#{slugify(title)})")
    return toc_lines


def split_frontmatter(lines: list[str]) -> tuple[list[str], list[str], list[str]]:
    if not lines or lines[0].strip() != "---":
        return [], lines, []
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return lines[: idx + 1], lines[idx + 1 :], []
    return [], lines, []


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate TOC for Obsidian Markdown")
    parser.add_argument("--file", required=True, help="Path to Markdown file")
    parser.add_argument("--max-depth", type=int, default=3, help="Max heading depth")
    parser.add_argument("--dry-run", action="store_true", help="Print TOC only")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        raise SystemExit(f"Missing file: {path}")
    if path.stat().st_size > MAX_BYTES:
        raise SystemExit("File too large for safe TOC generation.")

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    headings = parse_headings(lines, args.max_depth)
    toc_lines = build_toc(headings)

    if args.dry_run:
        print("\n".join(toc_lines))
        return 0

    start_marker = "<!-- TOC START -->"
    end_marker = "<!-- TOC END -->"

    if start_marker in text and end_marker in text:
        pre = text.split(start_marker, 1)[0]
        post = text.split(end_marker, 1)[1]
        new_block = "\n".join([start_marker] + toc_lines + [end_marker])
        updated = pre + new_block + post
    else:
        frontmatter, rest, _ = split_frontmatter(lines)
        insertion = [start_marker] + toc_lines + [end_marker, ""]
        updated_lines = []
        if frontmatter:
            updated_lines.extend(frontmatter)
            updated_lines.append("")
        updated_lines.extend(insertion)
        updated_lines.extend(rest)
        updated = "\n".join(updated_lines).rstrip() + "\n"

    path.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
