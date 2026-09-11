# Style guides

Use this guide when the task concerns style guides. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

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

- Prefer small, cohesive diffs; avoid drive-by refactors.
- Keep I/O at the edges; keep core logic testable and deterministic.
- Never log secrets. Prefer structured logs to stderr.
- Bound all I/O and resource usage.
- Treat external inputs as hostile.
