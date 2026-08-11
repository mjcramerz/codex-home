# Snippet catalog
Purpose: provide copy-ready hardened patterns for code, config, and operational workflows for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## You must use this file when
- the target repo lacks an established implementation pattern
- you need a safe starting point for a script, service, config, or workflow helper
- you are maintaining snippet structure or deciding where a new snippet belongs

## How to use snippets
- You must prefer snippets when they reduce boilerplate without fighting the target repo’s conventions.
- You must adapt the snippet to the active repo instead of copying it blindly.
- You must use the corresponding docs, workflow, or template guide when the snippet sits inside a larger operational flow.

## Major snippet families
- Bash and POSIX sh — shell baselines, repo helpers, and guarded automation
- Python, Go, TypeScript, Rust — language baselines and runtime-safe helpers
- systemd, CI, containers, infra, and observability — operational skeletons
- docs/process and prompts — reusable writing and contract fragments
- desktop, virtualization, and system hardening — host-focused configuration snippets

## You must choose using these rules
- Shell-sensitive snippets require `$CODEX_HOME/docs/style/shell-runtime.md` and the matching shell runtime.
- You must use snippets for patterns; use templates for larger skeletons; use skills or workflows for execution guidance.
- If a snippet becomes a multi-file scaffold, promote it to a template instead of extending the snippet indefinitely.

## You must maintain this file by following these rules
- You must keep snippet names descriptive and stable.
- You must keep snippets minimal but safe-by-default.
- You must document important assumptions inline in the snippet or its nearest doc.
- You must validate syntax or parseability for the formats you edit.

## After that, you must check related files
- `$CODEX_HOME/index/pack/snippets.md`
- `$CODEX_HOME/docs/OVERVIEW.md`
- `$CODEX_HOME/templates/OVERVIEW.md`
- `$CODEX_HOME/plans/snippets-library.md`
