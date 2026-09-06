# Multi-Agent Context Checkpoint

Create a precise handoff for the coordinating or successor coding agent. The
summary must preserve ownership, evidence, and merge safety rather than repeat
the conversation.

Output Markdown with these exact sections:

## Objective and Authority
- User outcome, acceptance criteria, non-goals, and active instruction,
  workflow, plan, permission, and repository constraints.

## Coordination State
- Coordinator identity or role, active agents, each agent's owned files,
  objective, stop condition, and current status.
- Completed handoffs, unresolved dependencies, conflicts, and any work that
  must not be duplicated.

## Verified Work
- Decisions and rationale.
- Files changed or inspected, including the owner and validation evidence.
- Commands run, key outputs, revisions, environment limits, and user changes
  that must remain intact.

## Integration State
- Exact current plan step, canonical source of truth, pending merges or
  reconciliations, and validation still required.
- Risks, blockers, security or permission boundaries, and unverified claims.

## Next Actions
1. The single next action on the critical path, including its command or file.
2. Ordered follow-up actions, owners, and success criteria.
3. Any specific user decision required to proceed.

Rules:
- State facts, not impressions; label inference and incomplete work.
- Never fabricate agent status, command results, or file ownership.
- Keep secret material and private reasoning out of the checkpoint.
- Do not assign new work in the summary; report the existing coordination plan.
