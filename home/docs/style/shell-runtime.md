# Shell runtime guidance
Purpose: define the common shell execution rules for shell-sensitive work in the runtime pack for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Choose the matching shell
- You must use `zsh` for zsh-sensitive commands and zsh assets.
- You must use `bash` for Bash-sensitive commands and Bash assets.
- You must use `sh`/`dash` for POSIX-portable assets.
- You must validate shell-specific files with the shell they claim to support.
- You must prefer `bash -c` over `bash -lc` for Bash execution unless login-shell startup files are the explicit subject of the work.

## Deterministic execution defaults
- You must prefer `LC_ALL=C` and `TZ=UTC` for reproducible command output.
- You must prefer machine-readable flags (`--json`, `--porcelain`, `--null`, `--color=never`) when available.
- You must prefer read-only discovery first, then the smallest deterministic change.
- Avoid interactive flows and fuzzy parsing.

## Safe command shape
- Refuse destructive operations on empty paths, `/`, or ambiguous globs.
- You must use `--` before untrusted positionals where supported.
- You must prefer explicit arrays or direct argv execution over shell-string construction.
- Avoid `eval`, avoid command strings built from untrusted fragments, and do not reach for login shells just to make commands work.
- Reparse structured files after mutation.

## Documentation scope
- You must keep shell guidance focused on shell choice, reproducibility, validation, and command safety.
- You must route plugin, skill, and workflow ownership questions through the matching pack entrypoints instead of shell guidance.

## After that, you must check related files
- `$CODEX_HOME/docs/style/bash.md`
- `$CODEX_HOME/docs/style/sh.md`
- `$CODEX_HOME/index/style/overview.md`
