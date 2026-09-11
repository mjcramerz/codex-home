---
name: schema-diff
description: Compare checked-in config against upstream schema and release snapshots.
metadata:
  version: '2.0'
  short-description: Schema Diff
  tags:
  - plugin
  - schema-diff
---

# Schema Diff

## Execute the scoped task

1. Use this skill only for an explicit configuration-schema or version-compatibility comparison. Identify both exact release tags and obtain the primary schema and feature registry for each.

2. Compare added/removed keys, type changes, enum values, defaults, aliases and feature lifecycle. Treat schema acceptance and actual runtime support as separate evidence.

3. Produce a minimal affected-key migration plan. Preserve original settings; do not activate mutually exclusive alternatives, populate fake IDs or strip custom-client fields merely because stock upstream lacks them.

4. Keep schemas out of normal hook context. Check the edited TOML and relevant client behavior, and state exactly which release combinations were not executed.

## Task-specific details and resources

- Prefer `src/misc/codex_schema_tool.py` and upstream schema sources over manual key counting.
- Separate schema additions, stale keys, and installer-only overlays.
- Keep example and diff outputs deterministic and easy to review.
