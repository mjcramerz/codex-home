---
name: devtools-vscode-extension
description: Develop and package VS Code extensions with secure defaults, activation events, commands, testing, and publishing setup. Use when the user asks to build, extend, debug, or release a VS Code extension.
metadata:
  version: '1.0'
  short-description: Develop VS Code extensions with secure defaults, packaging, and tests
  tags:
  - vscode
  - extension
  - node
  - typescript
  - packaging
interface:
  display-name: DEVTOOLS-VS Code Extension
  short-description: Develop VS Code extensions with secure defaults, packaging, and tests
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#8E32CC'
  default-prompt: Act as the "DEVTOOLS-VS Code Extension" specialist for "Develop VS Code extensions with secure defaults, packaging, and tests". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

# SKILL

## Execute the scoped task

1. Read pyproject.toml, interpreter constraints, lockfiles and the affected callers. Reuse the project's environment and package manager; do not upgrade the system interpreter or globally install dependencies for a local code change.

2. Define types at public boundaries and validate external data before constructing domain objects. Separate parsing, pure transformations and side effects; use explicit exceptions rather than blanket catch-and-continue.

3. Use pathlib for paths, context managers for resources, subprocess argument lists with shell=False, explicit encodings, bounded reads and timeouts. Avoid eval, unsafe deserialization and module imports from untrusted working directories.

4. Use module loggers and structured context. Redact tokens and payloads, preserve exception causes, and avoid logging the same failure at every layer.

5. Check the narrow changed contract using existing lint, type and test commands. Compiling source proves syntax only; it does not validate imports, optional dependencies, live services or runtime behavior.

## Task-specific details and resources

## Use this skill when

- creating a new VS Code extension
- adding commands, language features, or UI contributions
- preparing an extension for release

## Workflow

1. Define activation events and contributes in `package.json`
2. Implement extension entrypoint with strict input validation
3. Add unit and integration tests
4. Add packaging config (`vscode:prepublish`, `.vscodeignore`)
5. Verify CI lint/test and versioning

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

- A minimal, secure extension structure
- Reproducible build and release steps

## References

- `$CODEX_HOME/docs/workflows/vscode-extensions.md`
- `$CODEX_HOME/index/domains/vscode/vscode-extension.md`
- `$CODEX_HOME/index/domains/vscode/guidance.md`
