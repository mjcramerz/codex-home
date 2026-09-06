---
name: shell-zsh
description: Write and review zsh-specific shell code, wrappers, and runtime integrations.
  Use when the confirmed runtime is zsh or when wrapper semantics, completion behavior,
  globbing, or zsh startup files matter.
metadata:
  version: "1.0"
  short-description: Write robust zsh scripts, wrappers, and shell integrations
  tags:
  - zsh
  - shell
  - scripting
  - wrappers
  - terminal
interface:
  display-name: SHELL-Zsh
  short-description: Write robust zsh scripts, wrappers, and shell integrations
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#6F32CC'
  default-prompt: Act as the "SHELL-Zsh" specialist for "Write robust zsh scripts, wrappers,
    and shell integrations". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

# SHELL-Zsh

## When to use
Use this skill whenever you need to:
- write or modify zsh scripts, startup files, aliases, functions, or wrappers
- debug zsh runtime behavior, option handling, completion flows, or prompt hooks
- reason about zsh-vs-bash differences before changing shared shell assets
- validate login-vs-non-login behavior for zsh-specific execution paths
- confirm the runtime first with `$CODEX_HOME/AGENTS.md` and then use `$CODEX_HOME/UNIX.md`

## Non-negotiables
- Invoke `zsh` explicitly for zsh-sensitive validation and reproduction.
- Keep zsh assumptions explicit; do not rely on bash-compatible behavior by accident.
- Prefer deterministic commands, bounded output, and minimal reproductions.
- Avoid mutating user startup files unless the request explicitly requires it.
- Validate shared shell assets in every claimed runtime before finalizing.

## Workflow
1) Confirm the runtime is actually zsh and identify whether login semantics matter.
2) Inspect wrapper boundaries, shell options, and process invocation shape before editing.
3) Localize option changes with `emulate -L zsh` or careful `setopt` scoping when appropriate.
4) Validate word splitting, globbing, arrays, and completion behavior explicitly.
5) Run the narrowest relevant checks and report any runtime-specific caveats.

## Zsh-specific guidance
- Prefer `[[ ... ]]` for tests and `typeset`/`local` for scoped variables.
- Be explicit about `setopt` / `unsetopt`; do not assume inherited shell options.
- Treat glob qualifiers and extended glob syntax as zsh-only.
- Do not assume bash array semantics, completion loading, or startup file order.
- Prefer `zsh -n path/to/file.zsh` for syntax validation.

## Shared-shell safety
- If the asset must work in Bash too, validate both `zsh -n` and `bash -n`.
- If the asset must work in `/bin/sh`, stop and switch to `shell-sh`.
- Keep login-shell usage intentional; prefer non-login execution for deterministic subprocesses.

## Validation and testing
- Validate critical inputs and bound external I/O before applying changes.
- Run the narrowest relevant checks that prove behavior.
- Include edge-case validation for shell options, globbing, and wrapper arguments.
- Report exact validation commands and any remaining zsh-specific risks.

## Outputs
- Robust zsh scripts and wrappers with explicit runtime assumptions.
- Clear notes about zsh-only behavior, compatibility boundaries, and validation coverage.

## References
- `$CODEX_HOME/UNIX.md`
- `$CODEX_HOME/docs/style/bash.md`
- `$CODEX_HOME/docs/style/sh.md`
