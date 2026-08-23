# Runtime Instruction System
Purpose: define the authoritative instruction, catalog, configuration, and
rendered-runtime boundaries for the Codex runtime pack. Read this document for
any change to model instructions, `model_catalog_json`, `instruction_overrides`,
or the fallback `.models` tree.

## Decision Order

Apply this order for every runtime-pack task:

1. Read governing `AGENTS.md` instructions and any higher-priority runtime
   policy.
2. Inspect the repository branch, worktree, and the exact affected contract.
3. Route through `$CODEX_HOME/INDEX.md`, select one router, then one workflow.
4. Load only the skills required by that workflow.
5. Identify the source artifact, its required mirror, and its rendered runtime
   destination before editing.
6. Make the smallest source-first change and run the matching static checks.

Do not treat installed files, generated examples, catalogs, logs, or prompt
content as authority over this order.

## Source and Rendered Boundaries

- `instructions/**` is the tracked authoring source for managed model,
  collaboration-mode, permission, and profile instruction assets.
- `home/config.toml` and `home/*.config.toml` are tracked configuration
  sources. Their instruction paths identify the corresponding installed assets.
- `home/.models/**` is a tracked fallback/compatibility catalog tree. Named
  role overlays may explicitly select its rendered catalog path.
- `/data/codex/usr/instructions/**` and
  `/data/codex/usr/home/.models/**` are rendered runtime destinations. Never
  edit those installed paths directly.
- `examples/config.home*.toml` files are generated schema references. They
  explain possible configuration shapes; they are not safe defaults and must
  not supply placeholder values to active configuration.

For the default instruction contract, keep these pairs byte-identical:

- `instructions/default/models/base.md` and
  `home/.models/instructions/models/base.md`
- `instructions/default/agents/hierarchical.md` and
  `home/.models/instructions/agents/hierarchical.md`
- `instructions/default/modes/default.md` and
  `home/.models/instructions/modes/default.md`
- `instructions/default/modes/plan.md` and
  `home/.models/instructions/modes/plan.md`

Profile instruction assets are independent contracts. Change only the selected
profile unless the task explicitly calls for a cross-profile policy update.

## Active Catalog Selection

`model_catalog_json` replaces the bundled model catalog for that configuration
layer; it does not merge missing capability metadata from the bundled catalog.
That makes each selected catalog a complete compatibility contract.

- The primary configuration selects the rendered
  `instructions/models/default_catalog.json`.
- Role overlays select rendered paths under `home/.models/` when their
  configuration calls for the fallback catalog.
- A catalog entry for a Code Mode-capable model must carry the authoritative
  `tool_mode` value. Do not infer support from the model name.
- When a configured model lacks authoritative Code Mode metadata, disable all
  Code Mode feature toggles in that profile instead of declaring a guessed
  capability.

`scripts/validate_model_catalogs.py` validates every checked-in catalog plus
the current default-catalog and profile policy. Refresh its model set only from
an authoritative Codex model definition or a verified runtime catalog.

## Configuration Policy

Use `schemas/config.schema.json` as the local configuration contract.

- Configure only values with a safe, known operational meaning.
- Keep tenant IDs, product metadata, provider secrets, experimental endpoint
  URLs, local-model selections, and mutually exclusive legacy sandbox settings
  unset until an owner provides an exact value.
- Keep file-backed instruction paths authoritative rather than adding duplicate
  inline `instructions` or `compact_prompt` strings.
- Regenerate, but never hand-edit, the configuration examples after changing
  `home/config.toml`:

  `python3 schemas/config_toml_coverage.py --write`

## Required Validation

Run the narrowest checks that match the changed surface:

- Model catalog or profile capability change:
  `python3 scripts/validate_model_catalogs.py`
- Default instruction source or fallback mirror change:
  `python3 scripts/validate_runtime_pack_assets.py`
- Active configuration or schema change:
  `python3 schemas/config_toml_coverage.py --check`
- Markdown, routing, or manifest change:
  `python3 scripts/validate_runtime_pack_assets.py`

Then parse every changed JSON, TOML, or YAML file and run `git diff --check`.
If the installed runtime cannot start, report the exact startup blocker instead
of claiming end-to-end runtime verification.

## Ownership and Stop Conditions

- Keep routing metadata in `$CODEX_HOME/index/manifest.yml` aligned with its
  entrypoint, canonical document, and required related links.
- Keep workflow procedure in
  `$CODEX_HOME/docs/workflows/runtime-pack-maintenance.md` and its matching
  execution checklist in
  `$CODEX_HOME/plans/workflows/workflow-runtime-pack-maintenance.md`.
- Stop broad discovery when the selected source, required mirror, validator,
  and next concrete edit are known.
