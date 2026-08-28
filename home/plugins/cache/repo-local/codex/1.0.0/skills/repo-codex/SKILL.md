---
name: repo-codex
description: Work in the Codex source repository across the Rust workspace, CLI, SDKs, configuration types, generated schema, implementation, review, debugging, and validation.
---

# Codex repository workflow

## Start

1. Resolve the current Git root; do not assume a machine-local clone path.
2. Confirm the root contains `AGENTS.md`, `codex-rs/`, `justfile`, and `package.json`.
3. Read the root `AGENTS.md` and every deeper `AGENTS.md` governing the touched path.
4. Require branch `mcr/main` before authored edits.
5. Inspect `git status --short --branch` and preserve unrelated user changes.

## Source and generated boundaries

- Treat the nearest code, tests, and local instructions as the source of truth.
- Keep Rust changes scoped to the owning crate under `codex-rs/`.
- Treat checked-in generated configuration schema as a derivative of Rust configuration types.
- When configuration types change, run `just write-config-schema` and review the generated diff.
- Preserve established boundaries among `codex-rs/`, `codex-cli/`, `sdk/`, `docs/`, and packaging surfaces.
- Do not add compatibility branches, feature flags, or cross-workspace refactors unless the requested behavior requires them.

## Workflow

1. Identify the smallest crate, command, schema, or client surface that owns the requested behavior.
2. Read the focused tests before changing behavior.
3. Apply the smallest source change and update directly owned docs or generated artifacts.
4. Keep error handling, formatting, naming, and dependency use consistent with the owning crate.

## Validation

- Run `just fmt` after source edits.
- For Rust changes, use `just fix -p <crate>` when automatic fixes are appropriate.
- Run the narrowest relevant `just test -p <crate>` or repository-defined focused test.
- Use `just test` when the changed contract is workspace-wide or the root instructions require the broader suite.
- Never substitute direct `cargo test` for the repository's `just test` contract.
- Run `just write-config-schema` when configuration types or schema-bearing fields change.

## Handoff

Report the owning crate or surface, source and generated files changed, exact `just` commands run, and any known validation gap.
