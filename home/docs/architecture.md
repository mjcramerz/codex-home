# Runtime-pack architecture
Purpose: explain how the codex-manager source tree, the runtime-home pack, hook runtime, and adjacent repos fit together for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Primary surfaces
- **Compiled runtime configuration**: `$CODEX_HOME/config.toml`, `$CODEX_AGENTS/*.toml`, `/etc/codex/config.toml`, `/etc/codex/requirements.toml`
- **Runtime-home pack**: `$CODEX_HOME/**`
- **Hook runtime source of truth**: `$CODEX_HOME/hooks/scripts/lib/Codex/Hook/**`
- **Runtime skill catalog**: `$CODEX_HOME/.agents/skills/**`
- **Plugin bundles and marketplace**: `$CODEX_HOME/plugins/cache/**` plus `$CODEX_HOME/.agents/plugins/marketplace.json`

## Adjacent repository map
- `debian-preseed-di` — unattended Debian install tree, storage/profile/rendering contract
- `cf-aptly-r2` — Cloudflare Worker front-end for Aptly content in R2
- `cf-git-cicd-worker` — GitHub App webhook dispatcher Worker with DO/D1 controls
- `delivery` — shared GitLab CI/CD templates for Cloudflare, salsa, and OBS flows
- `codex-mcp` — Podman-backed MCP stack renderer/launcher
- `codex-manager` — this installer/runtime-pack source repo

## Sync boundary
- The repo is the source of truth for installable pack content.
- Runtime state stays on the installed target and never syncs back into source control.
- Agent-facing pack guidance should stay on stable installed surfaces:
  - `$CODEX_HOME/docs/**`
  - `$CODEX_HOME/index/**`
  - `$CODEX_HOME/plans/**`
  - `$CODEX_HOME/templates/**`
  - `$CODEX_HOME/snippets/**`
  - `$CODEX_HOME/plugins/cache/**`
  - `$CODEX_HOME/.agents/plugins/marketplace.json`
  - `$CODEX_HOME/.agents/skills/**`

## Why the boundary matters
- Installed runtime paths stay coherent after the pack is rendered into `$CODEX_HOME`.
- Agent guidance stays fast to route when it points at stable docs, plans, skills, templates, snippets, and plugin metadata.
- Avoiding repository-source paths in runtime docs keeps the installed pack self-contained.

## Source-pack operating shape
1. Route through `INDEX.md` and the `index/**` entrypoints.
2. Use `$CODEX_HOME/memories/` when prior decisions actually matter.
3. Update docs, plans, templates, skills, and manifest links together when entrypoints change.
4. Validate syntax and contract tests before handoff.
