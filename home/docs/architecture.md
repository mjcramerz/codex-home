# Runtime-pack architecture
Purpose: explain the installed runtime-home pack, hook runtime, configuration,
catalog, and plugin boundaries for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Primary surfaces
- **Compiled runtime configuration**: `$CODEX_HOME/config.toml`, `$CODEX_AGENTS/*.toml`, `/etc/codex/config.toml`, `/etc/codex/requirements.toml`
- **Runtime-home pack**: `$CODEX_HOME/**`
- **Hook runtime entrypoints**: `$CODEX_HOME/.hooks/scripts/**`
- **Hook runtime modules**: `$CODEX_HOME/.hooks/modules/**`
- **Runtime skill catalog**: `$CODEX_HOME/.agents/skills/**`
- **Plugin bundles and marketplace**: `$CODEX_HOME/plugins/cache/**` plus `$CODEX_HOME/.agents/plugins/marketplace.json`

## Runtime boundary
- Runtime state stays under installed runtime paths and is never inferred from
  unrelated machine-local source trees.
- Agent-facing guidance stays on stable installed surfaces:
  - `$CODEX_HOME/docs/**`
  - `$CODEX_HOME/index/**`
  - `$CODEX_HOME/plans/**`
  - `$CODEX_HOME/templates/**`
  - `$CODEX_HOME/snippets/**`
  - `$CODEX_HOME/plugins/cache/**`
  - `$CODEX_HOME/.agents/plugins/marketplace.json`
    - `$CODEX_HOME/.agents/skills/**`

## Instruction and Model Catalog Flow

- Managed default, agent, and profile instruction assets live under
  `/data/codex/usr/instructions/**`.
- `$CODEX_HOME/.models/**` contains runtime-home catalog and compatibility
  instruction assets.
- `$CODEX_HOME/config.toml` identifies the active rendered catalog and
  instruction files. A `model_catalog_json` setting replaces, rather than
  extends, the bundled model catalog.

## Why the boundary matters
- Installed runtime paths stay coherent after the pack is rendered into `$CODEX_HOME`.
- Agent guidance stays fast to route when it points at stable docs, plans, skills, templates, snippets, and plugin metadata.
- Avoiding repository-source paths in runtime docs keeps the installed pack self-contained.

## Runtime operating shape
1. Route through `INDEX.md` and the `index/**` entrypoints.
2. Use `$CODEX_HOME/memories/` when prior decisions actually matter.
3. Update docs, plans, templates, skills, and manifest links together when entrypoints change.
4. Validate syntax and contract tests before handoff.
