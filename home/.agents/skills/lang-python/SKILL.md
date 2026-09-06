---
name: lang-python
description: Build and refactor Python modules, CLIs, automation, and packaging with typing, testing, and safe I/O defaults. Use when the user asks for Python implementation, refactoring, packaging, or runtime-automation changes.
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
  default-prompt: Act as the "LANG-Python" specialist for "Build Python code with typing, testing, and packaging defaults". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---
## Use this skill when
- the active task matches this skill's description and needs deterministic implementation guidance

## Workflow
1) Confirm the package, module, or entrypoint boundary first.
2) Model inputs and outputs explicitly before touching parsing or I/O paths.
3) Add the narrowest validation command, tests, or py_compile checks that prove the change.

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
- [Python documentation](https://docs.python.org/3/)
- [Packaging Python projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [pytest documentation](https://docs.pytest.org/)
