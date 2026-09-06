---
name: shell-sh
description: Write portable POSIX sh scripts that run correctly under `/bin/sh`,
  `dash`, and BusyBox `ash`. Use when portability and minimal shell assumptions matter.
metadata:
  version: "1.0"
  short-description: Write portable POSIX sh scripts with safe defaults
  tags:
  - sh
  - posix
  - busybox
  - shell
  - scripting
interface:
  display-name: SHELL-sh
  short-description: Write portable POSIX sh scripts with safe defaults
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: "#CC323D"
  default-prompt: Act as the "SHELL-sh" specialist for "Write portable POSIX sh scripts with safe defaults". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## When to use
Use this skill whenever you need to:
- write or modify `/bin/sh`, `dash`, or BusyBox `ash` scripts
- harden portable installer, init, CI, or recovery scripts
- remove bashisms from shared shell assets
- confirm strict portability and minimal dependency expectations
- use `$CODEX_HOME/UNIX.md` after `$CODEX_HOME/AGENTS.md` confirms sh-compatible work

## Non-negotiables
- Stay inside POSIX syntax unless the request explicitly targets a richer shell.
- Prefer `set -eu`; only use `pipefail` after proving the target shell supports it.
- Avoid arrays, `[[ ... ]]`, brace expansion, process substitution, and shell-specific flags.
- Validate inputs, quote expansions, and keep subprocess usage deterministic.
- Prefer simple external tools and portable flags; call out GNU/BSD differences when relevant.

## Workflow
1) Confirm the script must be portable and identify the target `/bin/sh` implementation.
2) Inspect for bashisms, non-POSIX options, and unsafe subprocess patterns.
3) Use the smallest portable construct that solves the problem.
4) Validate with `dash -n` or `sh -n`, then run the narrowest behavioral check.
5) Report compatibility assumptions, remaining portability risks, and follow-up checks.

## Portability guidance
- Prefer `command -v` over shell-specific lookup helpers.
- Prefer `printf` over `echo` when formatting matters.
- Use `mktemp` plus `trap` for temporary files when available; otherwise document the portability tradeoff.
- Keep `find`, `xargs`, `sed`, `awk`, and `date` usage portable or explicitly guarded.
- If the confirmed runtime is Bash or zsh, consider `shell-bash` or `shell-zsh` instead.

## Validation and testing
- Validate critical inputs and bound external I/O before applying changes.
- Run the narrowest relevant checks that prove behavior.
- Prefer `dash -n path/to/script.sh` and `sh -n path/to/script.sh`.
- Include a negative-path or edge-case check for parsing, quoting, or file handling.

## Outputs
- POSIX-compliant shell scripts with minimal dependencies.
- Clear runtime assumptions, failure modes, and portability notes.

## References
- `$CODEX_HOME/UNIX.md`
- `$CODEX_HOME/docs/style/sh.md`
- `$CODEX_HOME/snippets/sh/`
