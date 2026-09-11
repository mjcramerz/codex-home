# Github actions plan

Use this plan when you following `$CODEX_HOME/docs/workflows/github-actions.md`. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when following `$CODEX_HOME/docs/workflows/github-actions.md`.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- `$CODEX_HOME/docs/workflows/github-actions.md`
- `$CODEX_HOME/index/core/ci-cd.md`

## Scope

- In: GitHub Actions wrapper/shared workflow contracts, trigger rules, and release-tag guards.
- Out: GitLab-only delivery behavior that is not consumed by GitHub workflows.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items

- [ ] Route through `$CODEX_HOME/index/core/ci-cd.md`, then execute `$CODEX_HOME/docs/workflows/github-actions.md`.
- [ ] Capture org allowlists, shared workflow refs, release-tag policy, and BWS secret boundaries.
- [ ] Validate wrapper dispatch inputs (`event-context`, `event-name`, `expected-event-action`, `target-org`, `shared-repo`, `shared-ref`) and allowed-event checks.
- [ ] Validate shared workflow pinning (reviewed tag/commit) and third-party action SHAs before updating workflows.
- [ ] Validate release guardrails (protected release tags plus tag-tip check against `mcr/release`) for publish paths.
- [ ] Validate worker dispatch coupling (`GH_WORKFLOW_REF`) and fork-mode read-only mirror sync branches (`github/mcr/main`, `github/mcr/staging`).
- [ ] Apply updates in reversible order and capture run evidence for every changed trigger path.

## Testing and validation

- Run workflow lint/syntax checks (for example, `actionlint`) for changed files.
- Exercise each changed trigger path (PR, push, tag, dispatch dry run).
- Accept only if triggers, permissions, and shared-ref pins match workflow guidance.

## Security checkpoints

- Keep default `permissions` read-only and justify each write scope.
- Ensure untrusted PR/fork paths cannot access deploy secrets.

## Testing checkpoints

- Define fast-path and deep-path checks with explicit pass criteria before edits.
- Re-run checks after trigger, rules, permission, or shared-ref changes.

## Deployment checkpoints

- Confirm protected environment approvals and release-tag guards before publish.
- Record rollback artifact/tag references and release owner in handoff notes.

## Multi-agent handoff

- When coordinating, hand off scope, target entrypoint, and stop condition.
- When executing, report touched files, commands, evidence, blockers, and next action.

## Risks and edge cases

- Wrapper/shared ref drift can dispatch the wrong workflow version.
- Missing tag-tip enforcement can publish artifacts from non-release commits.
