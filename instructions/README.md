# Select instruction assets

Use `default/`, `agents/` or the selected `profiles/<name>/` set. Each complete
set covers every file-backed field in the attached `instruction_overrides`
schema, including the fully qualified tool-description map. `roles/` contains
role-specific developer guidance; `policies/` and `workflows/` retain pack guidance.

`manifest.json` records each file's selected model, source and SHA-256. Preserve
upstream template variables, JSON output contracts and literal catalog text.
Tool-description overrides change steering text; they do not change parameter
schemas, handlers, permissions, tool availability or MCP server advertisements.

Keep this canonical tree and `$CODEX_HOME/instructions/` byte-identical. The only
model catalog is `$CODEX_HOME/models_catalog.json`; it retains all supplied models
and metadata. Read the selected instructions instead of preloading the tree.

The attached schema and Rust source ZIP differ: the ZIP has no
`instruction_overrides` loader. A matching binary is required for those new
fields. Native base, compact, developer and realtime settings remain wired for
the supported compatibility paths; this does not emulate the missing loader.
