---
name: runtime-config
description: Inspect rendered config, instruction rewrites, and home sync behavior
metadata:
  version: "2.0"
  short-description: Runtime Config
  tags: [plugin, runtime-config]
---

# Runtime Config

Use this skill when the active task maps cleanly to the `runtime-config` bundle.

- Start with the installed runtime surfaces `$CODEX_HOME/config.toml`, `$CODEX_USER_DIR/instructions/metadata.json`, and the active runtime hook/config compiler behavior.
- Reconcile checked-in intent against rendered runtime paths before suggesting changes.
- Call out placeholder expansion, overlay append order, and config drift explicitly.
