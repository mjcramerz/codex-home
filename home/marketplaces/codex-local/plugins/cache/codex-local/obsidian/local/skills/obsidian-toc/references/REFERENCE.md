---
title: Obsidian TOC Script Reference
status: active
owner: Matthew Cramer
tags:
- skills
- all
- obsidian-toc
- references
- reference-md
- reference
- user
- chatgpt
updated: '2026-02-20'
---
# Obsidian TOC Script Reference

## Usage
```
python scripts/generate_toc.py --file path/to/note.md --max-depth 3
```

## Behavior
- Updates the block between `<!-- TOC START -->` and `<!-- TOC END -->` if present.
- Inserts a TOC after YAML frontmatter if markers are missing.

## Options
- `--file`: required path to the Markdown file.
- `--max-depth`: maximum heading depth to include (default: 3).
- `--dry-run`: print the TOC without modifying the file.
