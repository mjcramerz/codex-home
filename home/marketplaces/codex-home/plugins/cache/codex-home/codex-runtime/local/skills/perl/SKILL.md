---
name: perl
description: Write and review Perl for deterministic runtime helpers, CLI tools, and data transforms with strict validation and minimal shell exposure. Use when the user asks about Perl code beyond hook-specific modules.
metadata:
  version: '1.0'
  short-description: Perl runtime, CLI, and text-transform safety guidance
  tags:
  - perl
  - runtime
  - cli
  - validation
interface:
  display-name: Perl
  short-description: Perl runtime, CLI, and text-transform safety guidance
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#7C3AED'
  default-prompt: Act as the "Perl" specialist for "Perl runtime, CLI, and text-transform safety guidance". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- writing or reviewing deterministic Perl CLIs or text/config transforms
- checking payload validation, subprocess safety, or output parsing in Perl code
- aligning Perl helpers with repo-local validation and runtime boundaries

## Workflow
1) Confirm the Perl entrypoint, expected inputs, and external process boundaries first.
2) Prefer pure Perl parsing and rendering helpers over shell-outs when they are practical.
3) Keep untrusted input validation and output normalization explicit at module boundaries.
4) Validate with `perl -c` plus the narrowest relevant repo-local test harness.

## Agent orchestration
- Delegate read-only discovery only.
- Keep one owner for final edits and verification output.

## Validation and testing
- Reparse structured config after mutation.
- Run repo-local lint/test/build commands when the touched surface ships them.
- Record residual gaps when external credentials or infrastructure are required for deeper verification.

## Outputs
- Reviewable changes with explicit validation evidence.
- A concise contract summary, the files or jobs touched, and the remaining rollout risks.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-home/codex-runtime/local/skills/perl/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/codex-runtime/local/skills/perl/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/lang/perl.md
- $CODEX_HOME/docs/style/perl.md
- $CODEX_HOME/index/domains/lang/perl.md
