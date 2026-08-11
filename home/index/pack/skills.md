# Skills hub (entrypoint)
Purpose: route to reusable skill playbooks and the runtime skill catalog for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/index/pack/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

Canonical content: runtime skill roots under `$CODEX_HOME/.agents/skills`, plugin skills under the managed runtime plugin root, and `$CODEX_HOME/.agents/plugins/marketplace.json` for marketplace mapping.

## You must use this file when
- the task maps directly to a reusable skill
- you are maintaining skill instructions, metadata, support files, or routing
- you need to verify how a skill should be triggered or validated

## Current focus areas
- Pack-maintenance skills: docs, index, prompts, rules, snippets, templates
- Repo/runtime skills: `codex-manager`, `codex-mcp`, `perl-hooks`, `perl`, `rust-cargo`, `cargo`, `rustc`, `rustup`
- Cloudflare/delivery skills: `cloudflare`, `cloudflare-git-delivery`, `aptly-r2`, `aptly`, `cloudflare-r2`, `gitlab-cicd`, `gitlab-runner`, `gitops`, `bazel`, `buildbuddy`
- Debian install skills: `os-debian-preseed`, `debian-preseed`
- Desktop stack skills: `desktop-wayland`, `crystal-dock`, `labwc`, `waybar`, `wofi`
- Language skills: `lang-perl`, `lang-rust`

## After that, you must check related files
<!-- BEGIN:related -->
- `$CODEX_HOME/docs/OVERVIEW.md`
- `$CODEX_HOME/docs/workflows/overview.md`
- `$CODEX_HOME/index/pack/plans.md`
- `$CODEX_HOME/snippets/OVERVIEW.md`
- `$CODEX_HOME/.agents/skills`
- the managed admin skill root
- `$CODEX_HOME/.agents/plugins/marketplace.json`
<!-- END:related -->
