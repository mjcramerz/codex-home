---
name: lang-perl
description: Use this skill to build Perl modules, hook handlers, and deterministic
  CLI helpers with strict validation and testing guidance.
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
  default-prompt: Act as the "LANG-Perl" specialist for "Build Perl modules and hook
    scripts safely". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run
    the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

# Lang Perl

## Workflow

1. Identify the minimum Perl version, module search path, package namespace and entrypoint contract. Enable strict and warnings; keep package initialization free of external side effects.

2. Validate JSON shapes, string lengths, paths and encodings before use. Use lexical handles and three-argument open; check open, print, close and rename failures when the operation matters.

3. Use list-form system or exec with an explicit executable. Do not construct shell commands from input, use string eval for data, or treat a successful spawn as a successful child exit.

4. Keep stdout reserved for the documented machine-readable result. Send bounded, redacted diagnostics to stderr; preserve exit status and distinguish malformed input, tool failure and policy denial.

5. Run perl -c with the intended trusted library paths, then the narrow existing tests or fixture calls. Remember that compile-time BEGIN blocks can execute even during syntax checking; inspect unfamiliar modules first.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/docs/lang/perl.md`
- `$CODEX_HOME/docs/style/perl.md`
- `$CODEX_HOME/templates/perl/codex-hook-module/`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
