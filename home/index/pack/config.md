# Pack configuration (entrypoint)

Use this route when you need pack configuration. Select the closest matching destination below, read only what the next action requires, and stop discovery when the implementation or check is clear.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/index/pack/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

Canonical content: `$CODEX_HOME/config.toml`

Use when:
- tuning runtime settings, models, or safety defaults
- syncing new schema keys from upstream Codex config schema
- refreshing local model catalog or credential-store bootstrap artifacts
- deciding whether a configuration change requires an instruction or catalog
  source/mirror update

<!-- BEGIN:related -->
Related:
- `$CODEX_HOME/models_catalog.json`
- `/data/codex/usr/instructions/manifest.json`
- `$CODEX_HOME/docs/operations/CONFIGURATION.md`
- `/data/codex/usr/examples/config-coverage.json`
<!-- END:related -->

## Model and instruction contract

`$CODEX_HOME/models_catalog.json` is the complete supplied catalog, selected by
`model_catalog_json`. Preserve all model entries, support models, capability
metadata, message fragments and compatibility fields. Model availability still
requires the appropriate account entitlement.

Canonical prompts live in `/data/codex/usr/instructions/`; `$CODEX_HOME/instructions/`
is their byte-identical runtime mirror. `manifest.json` maps every supported
instruction override to its file, selected model, provenance and hash. Keep
model-specific base prompts aligned with each profile and agent role.

The separately attached schema supports `instruction_overrides`; the supplied
Rust ZIP does not implement its loader. Use a binary that implements this schema
before relying on the new overrides. Native model, compact, developer and realtime
fields preserve the available compatibility paths. Offline validation cannot prove
acceptance by an unprovided binary.

Keymaps must use supported actions and normalized bindings. Avoid collisions within
a context and within overlays that route keys together; distinct contexts can
legitimately share a binding. Preserve the intentional Enter/Tab behavior.
