---
name: lang-go
description: Build and maintain Go modules with idiomatic structure, dependency management,
  testing, and secure defaults. Use when the user asks for Go implementation, refactoring,
  or module/tooling fixes.
metadata:
  version: '1.0'
  short-description: Build Go modules with safe defaults and testing guidance
  tags:
  - go
  - backend
  - cli
interface:
  display-name: LANG-Go
  short-description: Build Go modules with safe defaults and testing guidance
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#96CC32'
  default-prompt: Act as the "LANG-Go" specialist for "Build Go modules with safe defaults
    and testing guidance". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- scaffolding or reviewing Go code

## Workflow
1) Set module path and layout.
2) Add tests and basic tooling.
3) Verify with `go test` and `go vet`.

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

- Actionable steps or artifacts aligned to the skill.
- References to relevant files, commands, or templates.

## References
- `$CODEX_HOME/docs/lang/go.md`
- `$CODEX_HOME/docs/style/go.md`
- `$CODEX_HOME/templates/go/cli-app/`
- `$CODEX_HOME/snippets/go/main.go`
- `$CODEX_HOME/docs/prompt-writing.md`
