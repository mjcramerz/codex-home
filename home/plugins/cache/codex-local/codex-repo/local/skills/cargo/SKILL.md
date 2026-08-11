---
name: cargo
description: Review Cargo workspace configuration, dependency policy, and release command usage with deterministic lockfile and validation defaults. Use when the user asks about Cargo manifests, commands, or CI/release behavior.
metadata:
  version: '1.0'
  short-description: Cargo workspace, lockfile, and release command discipline
  tags:
  - rust
  - cargo
  - workspace
  - release
interface:
  display-name: Cargo
  short-description: Cargo workspace, lockfile, and release command discipline
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#C2410C'
  default-prompt: Act as the "Cargo" specialist for "Cargo workspace, lockfile, and release command discipline". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- reviewing Cargo workspace layout, lockfile, or dependency policy
- checking `cargo fmt`, `clippy`, `test`, `build`, or `publish` contract usage
- aligning CI or release flows with the correct Cargo command boundaries

## Workflow
1) Confirm the workspace root, manifest path, and whether the repo commits `Cargo.lock`.
2) Prefer explicit manifest paths and `--locked` behavior in CI or release flows when a lockfile exists.
3) Keep build, test, fmt, and clippy flags deterministic and repo-scoped.
4) Validate with the narrowest cargo subcommand set that proves the changed contract.

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
- `$CODEX_HOME/plugins/cache/codex-local/codex-repo/local/skills/cargo/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/codex-repo/local/skills/cargo/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/rust-toolchain.md
- $CODEX_HOME/docs/lang/cargo.md
- $CODEX_HOME/index/domains/lang/cargo.md
