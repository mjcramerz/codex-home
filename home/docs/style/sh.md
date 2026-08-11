# POSIX/BusyBox sh style guide
Purpose: tell the Codex coding agent how to use `docs/style/sh.md` as a runtime-pack surface and when to stop browsing.
This guide targets `/bin/sh`, BusyBox `ash`, `dash`, and other POSIX shells.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/style/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline
- You must use `#!/bin/sh` and avoid bashisms (`[[ ]]`, arrays, brace expansion, `$'...'`, process substitution).
- Quote variable expansions unless you explicitly need word splitting or globbing.
- You must prefer `printf` over `echo -e`.
- You must use `command -v` for dependency checks.
- You must prefer `getopts` for flags; avoid non-POSIX `getopt`.

## Strict mode
```
set -eu
(set -o pipefail 2>/dev/null) || true
IFS=$(printf '\n\t')
```

Notes:
- `pipefail` is not POSIX; guard it as shown.
- `set -e` does not trigger on every failure. Use explicit checks where needed.

## Functions and flow
- You must define functions as `name() { ...; }` and avoid `function` keyword.
- You must use `case` for branching; avoid regex-heavy `expr` or `grep` when possible.
- You must use `trap` for cleanup (`EXIT`, `INT`, `TERM`), not `ERR`.

## Files and temp paths
- You must use `umask 077` before writing secrets or private keys.
- You must prefer `mktemp` when available and verify it exists; fall back only when necessary.
- Avoid writing into world-writable locations without randomness.

## Portability checklist
- No `[[ ]]`, `local`, `source`, or arithmetic arrays.
- No `read -a`, `mapfile`, or process substitution.
- You must use `IFS= read -r` when reading lines.
- Avoid `sed -r` or `grep -P`; stick to POSIX flags.

See also:
- `overview.md`
- `$CODEX_HOME/snippets/sh/`
- You must use skill shell-sh.
- `$CODEX_HOME/templates/sh/posix-sh-script/`
- `$CODEX_HOME/index/pack/style.md`
- `$CODEX_HOME/index/style/sh.md`
