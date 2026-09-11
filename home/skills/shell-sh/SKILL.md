---
name: shell-sh
description: Use this skill to write portable POSIX sh scripts that run correctly
  under `/bin/sh`, `dash`, and BusyBox `ash`. Use when portability and minimal shell
  assumptions matter.
metadata:
  version: '1.0'
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
  brand-color: '#CC323D'
  default-prompt: Act as the "SHELL-sh" specialist for "Write portable POSIX sh scripts
    with safe defaults". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run
    the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

# Shell Sh

## Workflow

1. Inspect the shebang and declared interpreter. Keep POSIX sh free of Bash or zsh extensions; select Bash explicitly when arrays or other Bash features are required.

2. Quote expansions, use -- before untrusted operands where supported, prefer argument arrays in Bash, and never use eval to dispatch user input. Avoid parsing ls or splitting filenames on whitespace.

3. Check failures explicitly around expected fallible operations. Do not assume set -e, pipelines or subshells give uniform error propagation across shells; isolate deliberate nonzero statuses.

4. Use private temporary directories and cleanup traps scoped to paths you created. Resolve and check destructive targets, reject empty paths, and preserve caller-owned files.

5. Keep stdout machine-readable when required, send redacted diagnostics to stderr and bound command duration. Run the matching interpreter's syntax check and existing ShellCheck/tests where available.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/AGENTS.md`
- `$CODEX_HOME/docs/style/sh.md`
- `$CODEX_HOME/snippets/sh/`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
