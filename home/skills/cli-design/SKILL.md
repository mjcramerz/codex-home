---
name: cli-design
description: Use this skill to design and refactor CLI commands, flags, subcommands,
  help text, and exit-code semantics with deterministic contracts. Use when the user
  asks for command-line UX, parser refactors, or safer automation interfaces.
metadata:
  version: '1.0'
  short-description: Design CLI contracts, flags, and exit semantics cleanly
  tags:
  - cli
  - argparse
  - ux
  - automation
interface:
  display-name: CLI-Design
  short-description: Design CLI contracts, flags, and exit semantics cleanly
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#DC2626'
  default-prompt: Act as the "CLI-Design" specialist for "Design CLI contracts, flags,
    and exit semantics cleanly". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.
---

# Cli Design

## Workflow

1. Identify supported invocations, exit codes, stdout/stderr contracts and compatibility requirements. Read automation callers before changing flags.

2. Define unambiguous subcommands and mutually exclusive options; reject missing, repeated or invalid values with actionable errors.

3. Keep data output deterministic and separate from diagnostics. Handle cancellation, broken pipes and noninteractive environments.

4. Use direct argument lists and inspect command side effects; check the changed parse and execution paths using existing fixtures.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
