---
name: rustc
description: Reason about `rustc` compiler behavior, target triples, and code generation boundaries without hiding them behind ad-hoc shell wrappers. Use when the user asks about compiler flags, target support, or Rust build debugging.
metadata:
  version: '1.0'
  short-description: Compiler target, codegen, and toolchain-boundary guidance
  tags:
  - rust
  - rustc
  - compiler
  - targets
interface:
  display-name: rustc
  short-description: Compiler target, codegen, and toolchain-boundary guidance
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#C2410C'
  default-prompt: Act as the "rustc" specialist for "Compiler target, codegen, and toolchain-boundary guidance". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- debugging target triples, compiler flags, or linker/toolchain interactions
- reviewing `RUSTFLAGS`, target-specific CI jobs, or release artifact builds
- checking how compiler behavior affects reproducibility or artifact naming

## Workflow
1) Confirm the toolchain version, target triple, and linker/runtime assumptions first.
2) Keep compiler flags explicit; avoid hiding target or codegen changes behind opaque shell aliases.
3) Separate compile-only debugging from workspace-wide test or release actions.
4) Validate with the narrowest target-specific check or build that exercises the touched compiler boundary.

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
- `$CODEX_HOME/plugins/cache/codex-local/codex-repo/local/skills/rustc/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/codex-repo/local/skills/rustc/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/rust-toolchain.md
- $CODEX_HOME/docs/lang/rustc.md
- $CODEX_HOME/index/domains/lang/rustc.md
