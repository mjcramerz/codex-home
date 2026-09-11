---
name: lang-go
description: Use this skill to build and maintain Go modules with idiomatic structure,
  dependency management, testing, and secure defaults. Use when the user asks for
  Go implementation, refactoring, or module/tooling fixes.
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
  default-prompt: Act as the "LANG-Go" specialist for "Build Go modules with safe
    defaults and testing guidance". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.
---

# Lang Go

## Workflow

1. Read go.mod, go.sum and workspace settings, then trace the affected API and callers. Keep module paths, public interfaces and supported Go versions stable unless the task changes them.

2. Propagate context for cancellation and deadlines. Close response bodies and files, stop tickers, and ensure every goroutine has a termination path.

3. Return wrapped errors with useful context; distinguish cancellation, not-found and invalid input. Avoid panic for expected external failures.

4. Use structured logging without credentials, bound network and parser inputs, and protect shared state with clear ownership or synchronization.

5. Use existing gofmt, go vet and focused go test commands; run the race detector when relevant and available. Report coverage limitations for external dependencies and unsupported platforms.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/docs/lang/go.md`
- `$CODEX_HOME/docs/style/go.md`
- `$CODEX_HOME/templates/go/cli-app/`
- `$CODEX_HOME/snippets/go/main.go`
- `$CODEX_HOME/docs/prompt-writing.md`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
