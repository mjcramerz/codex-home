# Runtime Instructions (entrypoint)
Purpose: route instruction, model-catalog, and runtime configuration work to
the one authoritative operating contract for the Codex runtime pack.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/index/pack/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

Canonical content: `$CODEX_HOME/docs/instruction-system.md`

Use when:
- changing model instructions, collaboration-mode prompts, or instruction
  overrides
- adding or refreshing `model_catalog_json` metadata
- determining whether a path is source, fallback mirror, generated reference,
  or installed runtime output
- validating default instruction parity and routing links

<!-- BEGIN:related -->
Related:
- `$CODEX_HOME/config.toml`
- `$CODEX_HOME/.models/default_catalog.json`
- `$CODEX_HOME/docs/architecture.md`
- `$CODEX_HOME/docs/workflows/runtime-pack-maintenance.md`
- `$CODEX_HOME/plans/workflows/workflow-runtime-pack-maintenance.md`
- `scripts/validate_model_catalogs.py`
- `scripts/validate_runtime_pack_assets.py`
<!-- END:related -->
