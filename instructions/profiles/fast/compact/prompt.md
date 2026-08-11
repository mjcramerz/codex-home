# Fast Context Checkpoint

Create the shortest complete handoff that allows another coding agent to take
the next safe action immediately.

Output these sections:

## Goal
- User outcome, scope limit, and one-line acceptance criterion.

## State
- Active instructions or constraints, current file or command, verified result,
  and existing user changes to preserve.

## Done
- Decisions, files changed, and validation actually run.

## Next
1. The exact next command or file action.
2. The focused check that proves completion.
3. Only material blocker, risk, or user question.

Rules:
- Use terse factual bullets; omit background the next agent can rediscover.
- Mark uncertainty explicitly and do not claim unrun validation.
- Never include secrets, large logs, or private reasoning.
