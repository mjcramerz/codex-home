# Perl
Purpose: guide Perl work in Codex hook/runtime modules, installer helpers, and safe text/config transforms for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Use this guide when
- editing hook or runtime modules under the installed Codex hook tree
- writing small deterministic Perl helpers for install, runtime, or text-transform tasks
- reviewing Perl code that touches hooks, JSON payloads, config rendering, or guarded subprocesses

## Baseline
- Enable `strict` and `warnings` by default.
- Keep side effects at the boundary; keep parsing and rendering functions testable.
- Prefer explicit data validation for payloads, files, env vars, and user-controlled input.
- Avoid shell-outs when Perl built-ins or modules can do the job safely.
- When you must call a shell, avoid login-shell wrappers and keep argv explicit; prefer direct process invocation or list-form `system`.

## Validation
- Syntax check: `perl -c path/to/file.pm`
- Test suite: `prove -lr t` or the repo-local equivalent when present
- Config/output validation: reparse generated JSON, TOML, or YAML after mutation

## After that, you must check related files
- `$CODEX_HOME/docs/style/perl.md`
- `$CODEX_HOME/docs/workflows/codex-manager.md`
- `$CODEX_HOME/templates/perl/codex-hook-module/`
- `$CODEX_HOME/index/domains/lang/perl.md`
