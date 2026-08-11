---
name: rustup
description: Manage Rust toolchains through rustup with explicit channels, components, and per-repo overrides. Use when the user asks about toolchain installation, overrides, or keeping CI/local toolchains aligned.
metadata:
  version: '1.0'
  short-description: Pinned toolchains, components, and override policy
  tags:
  - rust
  - rustup
  - toolchain
  - components
interface:
  display-name: rustup
  short-description: Pinned toolchains, components, and override policy
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#C2410C'
  default-prompt: Act as the "rustup" specialist for "Pinned toolchains, components, and override policy". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- pinning or updating Rust channels and components
- reviewing repo-local toolchain overrides versus user-global defaults
- checking how toolchain selection affects Cargo or rustc validation paths

## Workflow
1) Confirm the desired toolchain channel, target set, and required components first.
2) Keep per-repo overrides in `rust-toolchain.toml` or equivalent tracked config instead of ad-hoc shell init.
3) Avoid mutating a user-global toolchain when a repo-local override is sufficient.
4) Validate by showing the resolved toolchain and rerunning the narrowest affected Cargo or rustc check.

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
- `$CODEX_HOME/plugins/cache/codex-local/codex-repo/local/skills/rustup/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/codex-repo/local/skills/rustup/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/rust-toolchain.md
- $CODEX_HOME/docs/lang/rustup.md
- $CODEX_HOME/index/domains/lang/rustup.md
