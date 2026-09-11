# Snippet catalog

Use this guide when the task concerns snippet catalog. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

## Navigation

<!-- BEGIN:nav -->
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Use this file when

- the target repo lacks an established implementation pattern
- you need a safe starting point for a script, service, config, or workflow helper
- you are maintaining snippet structure or deciding where a new snippet belongs

## How to use snippets

- Prefer snippets when they reduce boilerplate without fighting the target repo’s conventions.
- Adapt the snippet to the active repo instead of copying it blindly.
- Use the corresponding docs, workflow, or template guide when the snippet sits inside a larger operational flow.

## Major snippet families

- Bash and POSIX sh — shell baselines, repo helpers, and guarded automation
- Python, Go, TypeScript, Rust — language baselines and runtime-safe helpers
- systemd, CI, containers, infra, and observability — operational skeletons
- docs/process and prompts — reusable writing and contract fragments
- desktop, virtualization, and system hardening — host-focused configuration snippets

## Choose using these rules

- Shell-sensitive snippets require `$CODEX_HOME/docs/style/shell-runtime.md` and the matching shell runtime.
- Use snippets for patterns; use templates for larger skeletons; use skills or workflows for execution guidance.
- If a snippet becomes a multi-file scaffold, promote it to a template instead of extending the snippet indefinitely.

## Maintain this file by following these rules

- Keep snippet names descriptive and stable.
- Keep snippets minimal but safe-by-default.
- Document important assumptions inline in the snippet or its nearest doc.
- Validate syntax or parseability for the formats you edit.

## After that, check related files

- `$CODEX_HOME/index/pack/snippets.md`
- `$CODEX_HOME/docs/OVERVIEW.md`
- `$CODEX_HOME/templates/OVERVIEW.md`
- `$CODEX_HOME/plans/snippets-library.md`
