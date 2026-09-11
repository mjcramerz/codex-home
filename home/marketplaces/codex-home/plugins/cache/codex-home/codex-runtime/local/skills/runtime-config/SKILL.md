---
name: runtime-config
description: Inspect rendered config, instruction rewrites, and home sync behavior.
metadata:
  version: '2.0'
  short-description: Runtime Config
  tags:
  - plugin
  - runtime-config
---

# Runtime Config

## Execute the scoped task

1. Identify the active Codex executable/version, CODEX_HOME, selected profile and effective configuration layers. Inspect only the keys involved; do not print credentials or load the entire schema into context.

2. Compare the requested change with the selected release's public schema and feature registry. Preserve existing keys, custom model IDs and instruction paths; keep mutually exclusive or credential-dependent alternatives inactive until their prerequisites are real.

3. Keep home/config.toml changes separate from an out-of-scope etc/config.toml mirror. Do not invent generator behavior or Makefile targets; read the actual synchronization owner before using it.

4. Parse the edited file and check the affected client contract. Report syntax, client acceptance, deployed paths, authentication and live behavior separately.

## Task-specific details and resources

- Start with the installed runtime surfaces `$CODEX_HOME/config.toml`, `$CODEX_USER_DIR/instructions/metadata.json`, and the active runtime hook/config compiler behavior.
- Reconcile checked-in intent against rendered runtime paths before suggesting changes.
- Call out placeholder expansion, overlay append order, and config drift explicitly.
