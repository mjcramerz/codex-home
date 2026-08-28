---
name: schema-diff
description: Compare checked-in config against upstream schema and release snapshots
metadata:
  version: "2.0"
  short-description: Schema Diff
  tags: [plugin, schema-diff]
---

# Schema Diff

Use this skill when the active task maps cleanly to the `schema-diff` bundle.

- Prefer `src/misc/codex_schema_tool.py` and upstream schema sources over manual key counting.
- Separate schema additions, stale keys, and installer-only overlays.
- Keep example and diff outputs deterministic and easy to review.
