# Containers plan

Use this plan when you following `$CODEX_HOME/docs/workflows/containers.md`. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when following `$CODEX_HOME/docs/workflows/containers.md`.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- `$CODEX_HOME/docs/workflows/containers.md`

## Scope

- In: steps defined in the containers workflow.
- Out: unrelated workflows or virtualization-only work.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items

- [ ] Read `$CODEX_HOME/docs/workflows/containers.md` and related references.
- [ ] Collect required inputs (services, ports, storage, network requirements).
- [ ] Decide engine/mode (Docker vs Podman; rootless vs rootful; container user root vs non-root).
- [ ] Decide build tooling (Buildx for Docker, Buildah for Podman) when multi-arch or rootless builds are required.
- [ ] Execute workflow steps in order (Dockerfile, Compose with Podman/root overrides when needed, rootless test, dev container if needed).
- [ ] Validate outputs (Docker + Podman, online + offline) and document results.

## Testing and validation

- Build and run with rootless and rootful contexts.
- Validate online + offline compose modes.
- When Podman is in scope, validate `podman compose` or `podman-compose`.
- Ensure Podman uses the same Dockerfile + compose files as Docker.
- Validate Buildx or Buildah builds when multi-arch or rootless builders are required.

## Security checkpoints

- Confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- Validate input bounds, timeout/retry limits, and failure behavior for risky operations.
- Record any approved exception, owner, and expiry before proceeding.

## Testing checkpoints

- Define fast-path and deep validation commands before making changes.
- Capture expected outcomes and acceptance criteria for each validation step.
- Re-run impacted checks after major changes and before final handoff.

## Deployment checkpoints

- Document rollout order, blast-radius controls, and rollback conditions.
- Confirm migration/backfill or feature-flag sequencing when applicable.
- Record post-deploy verification owners and evidence.

## Multi-agent handoff

- When coordinating, hand off scope, constraints, and stop condition with the target entrypoint.
- When executing, report touched files, commands run, evidence, blockers, and next action.
- When receiving work, acknowledge handoff completeness before continuing execution.

## Risks and edge cases

- Rootless networking or port binding constraints.
- Volume permission mismatches with non-root users.

## Examples

- Example objective: "Execute the containers workflow for the current repository scope."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
