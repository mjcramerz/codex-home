---
name: cli-design
description: Design and refactor CLI commands, flags, subcommands, help text, and exit-code semantics with deterministic contracts. Use when the user asks for command-line UX, parser refactors, or safer automation interfaces.
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
  default-prompt: Act as the "CLI-Design" specialist for "Design CLI contracts, flags, and exit semantics cleanly". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---
## Use this skill when
- the active task matches this skill's description and needs deterministic implementation guidance

## Workflow
1) Define command nouns, verbs, and exit codes before changing parser code.
2) Keep flags explicit, orthogonal, and machine-friendly.
3) Verify help text, error messages, and one negative-path invocation before finishing.

## Agent orchestration
- Confirm ownership, validation scope, and whether another skill or plugin should be combined before editing.
- Delegate only bounded scouting or independent verification work.

## Validation and testing
- Run the narrowest syntax, parser, or unit checks that prove the change.
- Explicitly call out skipped checks and why they remain out of scope.

## Outputs
- Minimal, reviewable edits aligned to the skill contract.
- Concrete validation commands and residual risks.

## References
- [argparse](https://docs.python.org/3/library/argparse.html)
- [Click documentation](https://click.palletsprojects.com/)
- [clap](https://docs.rs/clap/latest/clap/)
