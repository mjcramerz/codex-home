---
name: shell-bash
description: Use this skill to write production-grade Bash scripts using Bash-specific
  features (arrays, [[ tests ]], pipefail) with robust error handling. Use when the
  runtime is Bash and the user needs Bash-focused automation or hardening.
metadata:
  version: '2.1'
  short-description: 'Write production-grade Bash: strict mode, safe subprocess usage,
    portability, robust error handling, and security hardening'
  tags:
  - bash
  - shell
  - security
  - portability
  - automation
interface:
  display-name: SHELL-Bash
  short-description: 'Write production-grade Bash: strict mode, safe subprocess usage,
    portability, robust error handling, and security hardening'
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC32AD'
  default-prompt: 'Act as the "SHELL-Bash" specialist for "Write production-grade
    Bash: strict mode, safe subprocess usage, portability, robust error handling,
    and security hardening". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.'
---

# Shell Bash

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
- `$CODEX_HOME/snippets/bash/strict.sh`
- `$CODEX_HOME/snippets/bash/script_skeleton.sh`
- `$CODEX_HOME/snippets/bash/logging.sh`
- `$CODEX_HOME/snippets/bash/argparse.sh`
- `$CODEX_HOME/docs/style/bash.md`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
