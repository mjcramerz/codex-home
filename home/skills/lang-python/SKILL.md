---
name: lang-python
description: Use this skill to build and refactor Python modules, CLIs, automation,
  and packaging with typing, testing, and safe I/O defaults. Use when the user asks
  for Python implementation, refactoring, packaging, or runtime-automation changes.
metadata:
  version: '1.0'
  short-description: Build Python code with typing, testing, and packaging defaults
  tags:
  - python
  - backend
  - automation
  - cli
interface:
  display-name: LANG-Python
  short-description: Build Python code with typing, testing, and packaging defaults
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#3776AB'
  default-prompt: Act as the "LANG-Python" specialist for "Build Python code with
    typing, testing, and packaging defaults". Deliver focused, deterministic results
    with minimal, reviewable changes and explicit assumptions. Validate untrusted
    inputs and bounded I/O, run the narrowest relevant checks, and report concrete
    actions, evidence, and residual risks.
---

# Lang Python

## Workflow

1. Read pyproject.toml, interpreter constraints, lockfiles and the affected callers. Reuse the project's environment and package manager; do not upgrade the system interpreter or globally install dependencies for a local code change.

2. Define types at public boundaries and validate external data before constructing domain objects. Separate parsing, pure transformations and side effects; use explicit exceptions rather than blanket catch-and-continue.

3. Use pathlib for paths, context managers for resources, subprocess argument lists with shell=False, explicit encodings, bounded reads and timeouts. Avoid eval, unsafe deserialization and module imports from untrusted working directories.

4. Use module loggers and structured context. Redact tokens and payloads, preserve exception causes, and avoid logging the same failure at every layer.

5. Check the narrow changed contract using existing lint, type and test commands. Compiling source proves syntax only; it does not validate imports, optional dependencies, live services or runtime behavior.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
