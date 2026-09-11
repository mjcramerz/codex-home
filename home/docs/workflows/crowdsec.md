# CrowdSec workflow

Use this guide when you review authentication, authorization, trust boundaries or defensive security controls. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-crowdsec.md` before executing this workflow.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Plan

- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- Keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Execute the selected workflow

1. **Scope**: log sources, threat model, remediation policy.
2. **Configure**: `acquis.yaml` and minimal collections.
3. **Validate**: parsing and scenario detection (no remediation).
4. **Apply**: enable bouncers and remediation.
5. **Verify**: ensure whitelists and overrides are correct.

## Safety rules

- Start in alert‑only mode and monitor noise.
- Keep API keys scoped to the minimal bouncer set.

## Security checkpoints

- Scope `acquis.yaml` inputs explicitly and avoid collecting unnecessary sensitive logs.
- Restrict bouncer/API credentials to minimal privileges and rotate keys on schedule.
- Review whitelists and ban scopes to avoid blocking trusted internal ranges.

## Testing checkpoints

- Run parser and scenario tests before enabling live remediation.
- Replay benign and malicious samples to measure false-positive behavior.
- Verify ban and unban paths work for each configured bouncer type.

## Deployment checkpoints

- Start in detection-only mode, then enable remediation in staged host groups.
- Maintain an emergency disable path for bouncers during incident response.
- Track decision retention, legal/compliance constraints, and owner sign-off.

## Multi-agent handoff

- Coordinator provides source log map, whitelist policy, and ban-duration targets.
- Executor shares active collections, parser/scenario results, and remediation state.
- Receiver monitors early alert volume and drives tuning for noisy scenarios.
See also:
- `overview.md`
- `../observability/crowdsec.md`
- `$CODEX_HOME/templates/observability/crowdsec-skeleton/`
- `$CODEX_HOME/snippets/crowdsec/acquis.yaml`
- Read the `secops-crowdsec` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/observability/crowdsec.md`
