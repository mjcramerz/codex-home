---
name: shell-bash
description: Write production-grade Bash scripts using Bash-specific features (arrays, [[
  tests ]], pipefail) with robust error handling. Use when the runtime is Bash and the user
  needs Bash-focused automation or hardening.
metadata:
  version: '2.1'
  short-description: 'Write production-grade Bash: strict mode, safe subprocess usage, portability,
    robust error handling, and security hardening'
  tags:
  - bash
  - shell
  - security
  - portability
  - automation
interface:
  display-name: SHELL-Bash
  short-description: 'Write production-grade Bash: strict mode, safe subprocess usage, portability,
    robust error handling, and security hardening'
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC32AD'
  default-prompt: 'Act as the "SHELL-Bash" specialist for "Write production-grade Bash: strict
    mode, safe subprocess usage, portability, robust error handling, and security hardening".
    Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions.
    Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report
    concrete actions, evidence, and residual risks.'
---

## When to use
Use this skill whenever you need to:
- write or modify Bash scripts (CI scripts, repo tooling, installers)
- orchestrate processes safely
- interact with files/directories in a robust way
- wrap other tools (git, cargo, pytest, npm) in automation
- confirm the runtime first with the command in `$CODEX_HOME/AGENTS.md` and `$CODEX_HOME/UNIX.md`

## Non-negotiables
- Start scripts with strict mode (see `$CODEX_HOME/snippets/bash/strict.sh`).
- No `eval`.
- Quote expansions; use arrays for commands.
- Prefer `bash -c` over `bash -lc` unless login-shell startup files are the explicit subject of the task.
- Validate inputs; enforce usage/help; refuse ambiguous state.
- Use `mktemp` + `trap` for temp files/dirs.
- Never run network downloads without explicit approval + verification.
- Provide `--dry-run` for mutating operations and `--yes`/`ASSUME_YES=1` for automation.
- Avoid parsing human output; prefer machine-readable flags.

## Workflow
1) Confirm the target runtime is Bash and identify any compatibility boundaries with zsh or `/bin/sh`.
2) Inspect current script entrypoints, subprocess usage, and mutation surfaces before editing.
3) Apply strict-mode, array-safe subprocess, and input-validation patterns deliberately.
4) Validate with `bash -n`, `shellcheck` when available, and the narrowest behavior check that proves the change.

## Skeleton
Use this as the baseline shape for scripts:

1) strict mode + IFS
2) `usage()` function
3) `log_*` helpers
4) argument parsing with `getopts`/manual parsing
5) `main()` function
6) `trap` cleanup
7) exit codes documented

See: `$CODEX_HOME/snippets/bash/script_skeleton.sh`

## Safe subprocess patterns
### Prefer arrays
```bash
cmd=(git status --porcelain=v1)
"${cmd[@]}"
```

### Never interpolate untrusted strings into a shell
BAD:
```bash
bash -lc "rg ${pattern} ${path}"
```

GOOD:
```bash
rg --fixed-string -- "$pattern" "$path"
```

## Filesystem safety
- Refuse to operate on `/` or empty paths.
- Use `realpath` or a portable equivalent to normalize.

## Portability tips (macOS/Linux)
- Prefer `python3 -c` for portable helpers (JSON, hashing) when necessary.
- Be careful with BSD vs GNU `sed`, `stat`, `xargs`, `date`.
- Detect platform when needed:
  - `uname -s` → `Darwin` vs `Linux`

## Testing / validation
- Run `shellcheck` if available.
- Add a `--dry-run` mode for scripts that mutate state.
- Add `set -x` gated by `--debug`.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Validate critical inputs and bound external I/O (size, retries, and timeouts) before applying changes.
- Run the narrowest relevant checks that prove behavior (tests, lint, or build as applicable).
- Include risk-based negative or edge-case coverage for security-sensitive, parsing, or automation changes.
- Report verification commands, outcomes, and any follow-up checks that remain.

## Outputs
- Scripts that default to strict mode and safe subprocess usage.
- Deterministic, portable CLI behavior with clear usage/help.

## References in this pack
- `$CODEX_HOME/snippets/bash/strict.sh`
- `$CODEX_HOME/snippets/bash/logging.sh`
- `$CODEX_HOME/snippets/bash/argparse.sh`
- `$CODEX_HOME/snippets/bash/script_skeleton.sh`
- `$CODEX_HOME/docs/style/bash.md`
