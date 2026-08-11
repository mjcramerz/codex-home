# Style guides
Purpose: tell the Codex coding agent how to use `docs/style/overview.md` as a runtime-pack surface and when to stop browsing.
Follow repository-local conventions first. Use this pack as the default when a repo has no explicit style guide.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Contents
<!-- BEGIN:contents -->
- `$CODEX_HOME/docs/style/shell-runtime.md` — Shell execution and session guidance
- `$CODEX_HOME/docs/style/bash.md` — Bash style guide
- `$CODEX_HOME/docs/style/go.md` — Go style guide
- `$CODEX_HOME/docs/style/perl.md` — Perl style guide
- `$CODEX_HOME/docs/style/python.md` — Python style guide
- `$CODEX_HOME/docs/style/rust.md` — Rust style guide
- `$CODEX_HOME/docs/style/sh.md` — POSIX/BusyBox sh style guide
- `$CODEX_HOME/docs/style/typescript.md` — TypeScript style guide
<!-- END:contents -->

## Session guides
- Canonical shell runtime guidance: `$CODEX_HOME/docs/style/shell-runtime.md`

## Language guides
- Bash: `bash.md`
- POSIX sh: `sh.md`
- Perl: `perl.md`
- Python: `python.md`
- Rust: `rust.md`
- Go: `go.md`
- TypeScript: `typescript.md`

## Cross-language rules
- You must prefer small, cohesive diffs; avoid drive-by refactors.
- You must keep I/O at the edges; keep core logic testable and deterministic.
- Never log secrets. Prefer structured logs to stderr.
- Bound all I/O and resource usage.
- You must treat external inputs as hostile.
