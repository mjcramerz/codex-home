# Plan
Purpose: tell the Codex coding agent how to use `plans/workflows/workflow-containers.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when following `$CODEX_HOME/docs/workflows/containers.md`.

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
[ ] Read `$CODEX_HOME/docs/workflows/containers.md` and related references.
[ ] Collect required inputs (services, ports, storage, network requirements).
[ ] Decide engine/mode (Docker vs Podman; rootless vs rootful; container user root vs non-root).
[ ] Decide build tooling (Buildx for Docker, Buildah for Podman) when multi-arch or rootless builds are required.
[ ] Execute workflow steps in order (Dockerfile, Compose with Podman/root overrides when needed, rootless test, dev container if needed).
[ ] Validate outputs (Docker + Podman, online + offline) and document results.

## Testing and validation
- Build and run with rootless and rootful contexts.
- You must validate online + offline compose modes.
- When Podman is in scope, validate `podman compose` or `podman-compose`.
- Ensure Podman uses the same Dockerfile + compose files as Docker.
- You must validate Buildx or Buildah builds when multi-arch or rootless builders are required.

## Security checkpoints
- You must confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- You must validate input bounds, timeout/retry limits, and failure behavior for risky operations.
- You must record any approved exception, owner, and expiry before proceeding.

## Testing checkpoints
- You must define fast-path and deep validation commands before making changes.
- You must capture expected outcomes and acceptance criteria for each validation step.
- You must re-run impacted checks after major changes and before final handoff.

## Deployment checkpoints
- You must document rollout order, blast-radius controls, and rollback conditions.
- You must confirm migration/backfill or feature-flag sequencing when applicable.
- You must record post-deploy verification owners and evidence.

## Multi-agent handoff
- Coordinator hands off scope, constraints, and stop condition with the target entrypoint.
- Executor reports touched files, commands run, evidence, blockers, and next action.
- Receiving agent acknowledges handoff completeness before continuing execution.

## Risks and edge cases
- Rootless networking or port binding constraints.
- Volume permission mismatches with non-root users.

## Examples

- Example objective: "Execute the containers workflow for the current repository scope."
- Example validation: "Run the workflow's fast-path checks first, then the deeper verification commands if the risk profile requires them."

## Open questions
- None.
