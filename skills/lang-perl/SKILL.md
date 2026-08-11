---
name: lang-perl
description: Build Perl modules, hook handlers, and deterministic CLI helpers with strict validation and testing guidance.
metadata:
  version: '1.0'
  short-description: Build Perl modules and hook scripts safely
  tags:
  - perl
  - hooks
  - installer
  - runtime
interface:
  display-name: LANG-Perl
  short-description: Build Perl modules and hook scripts safely
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#8757D9'
  default-prompt: Act as the "LANG-Perl" specialist for "Build Perl modules and hook scripts safely". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

# LANG-Perl

## Use this skill when
- editing Perl modules or scripts
- working on Codex hook/runtime Perl code
- writing deterministic text/config transformation helpers

## Workflow
1) Validate input shape and path boundaries first.
2) Keep parsing and rendering logic separate from side effects.
3) Prefer direct Perl libraries over shell-outs when possible.
4) Reparse structured output and run syntax/tests before handoff.

## Agent orchestration
- Delegate read-only discovery only.
- Keep one owner for final code edits and validation output.

## Validation and testing
- Run `perl -c` on changed files.
- Run repo-local Perl tests (`prove`, `make test`, or equivalent) when available.
- Reparse JSON/TOML/YAML outputs produced by the changed code.

## Outputs
- Reviewable Perl changes with explicit validation evidence.

## References
- `$CODEX_HOME/docs/lang/perl.md`
- `$CODEX_HOME/docs/style/perl.md`
- `$CODEX_HOME/templates/perl/codex-hook-module/`
