# Execpolicy workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-execpolicy.md` before executing this workflow.
Purpose: use execpolicy rules to prevent accidental high-risk command execution outside the sandbox for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- You must keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Recommended posture
- Default: do everything inside the sandbox.
- Outside sandbox: only allow narrowly-scoped commands that you fully understand.
- You must prefer sandboxed execution modes over unrestricted full access.

## Execpolicy behavior
- Rules load only when `features.exec_policy = true`; if disabled, Codex uses an empty policy.
- If no rule matches, Codex falls back to heuristics based on `approval_policy` and `sandbox_mode`.

## Tuning rules
- Start from `$CODEX_HOME/rules/OVERVIEW.md` and keep broad operational allows plus explicit hard-deny rules.
- You must add scoped policy coverage for commands that:
  - touch the network
  - install dependencies
  - write outside the workspace
  - use credentials
  - modify git remotes or tags

## Testing changes
- You must add `match`/`not_match` examples to each rule so the policy is self-tested.

## Security checkpoints
- You must prefer deny-by-default patterns for destructive commands, broad globs, and credential-bearing calls.
- Constrain `allow` rules by command, args, and path scope; avoid blanket shell passthrough.
- You must record rule owner, review date, and runtime assumptions (`approval_policy`, `sandbox_mode`) per change.

## Testing checkpoints
- You must add `match` and `not_match` examples for every edited rule plus one abuse-case command.
- Test behavior across the supported execution modes, including `approval_policy = "never"`.

## Deployment checkpoints
- Version policy files so operators can revert quickly to a known-good ruleset.
- Announce behavior changes that may block existing automation before enforcement.

## Multi-agent handoff
- Rule author hands diff, rationale, and affected command examples to reviewer and operator.
- Reviewer signs off expected false-positive/false-negative tradeoffs and rollback path.
- Operator confirms active config reload plus post-change log spot-check before closure.

## References
- `$CODEX_HOME/rules/OVERVIEW.md`
- Codex execpolicy quickstart: https://developers.openai.com/codex/local-config#rules-preview
- `overview.md`
- `$CODEX_HOME/index/pack/workflows.md`
