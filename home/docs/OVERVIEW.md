# Documentation hub
Purpose: tell the Codex coding agent how to use the top-level documentation map for runtime-pack documentation and help the agent stop browsing quickly.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## You must use this file when
- you need a map of the documentation tree
- you are deciding which documentation area to open next
- you are maintaining docs and need to confirm the top-level structure

## Primary documentation areas
<!-- BEGIN:contents -->
- `$CODEX_HOME/docs/workflows/overview.md` — Operational workflows
- `$CODEX_HOME/docs/style/overview.md` — Shell and language conventions
- `$CODEX_HOME/docs/lang/overview.md` — Language-focused guidance
- `$CODEX_HOME/docs/templates/overview.md` — Template guidance
- `$CODEX_HOME/docs/architecture.md` — Runtime-pack architecture
- `$CODEX_HOME/docs/instruction-system.md` — Instruction, catalog, and rendered-runtime contract
- `$CODEX_HOME/docs/create-prompts.md` — Prompt-file design guide
- `$CODEX_HOME/docs/plugins.md` — Runtime plugins and marketplace guidance
<!-- END:contents -->

## Repo-aligned workflow shortcuts
- Codex installer/runtime repo -> `$CODEX_HOME/docs/workflows/codex-manager.md`
- Repo-aware memory routing -> `$CODEX_HOME/memories/`
- Podman MCP stack repo -> `$CODEX_HOME/docs/workflows/codex-mcp.md`
- Cloudflare + GitLab delivery repos -> `$CODEX_HOME/docs/workflows/cloudflare-delivery.md`
- Debian installer repo -> `$CODEX_HOME/docs/workflows/debian-preseed.md`
- Runtime-pack maintenance -> `$CODEX_HOME/docs/workflows/runtime-pack-maintenance.md`

## You must maintain this file by following these rules
- You must keep docs operational, concrete, and path-correct.
- You must use `$CODEX_HOME`, `$CODEX_AGENTS`, and `$CODEX_HOME/.agents/skills` runtime paths instead of repository-source paths unless the repo itself is the subject.
- You must keep prompt-file references centralized in `$CODEX_HOME/docs/create-prompts.md`.
- You must keep documentation focused on stable pack surfaces; route memory-specific work through `$CODEX_HOME/memories/` when needed.
