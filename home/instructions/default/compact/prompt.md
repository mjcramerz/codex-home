# Context Checkpoint

Create a durable handoff for the next coding agent. Preserve only information
that lets it continue safely without repeating broad discovery.

Output Markdown with these exact sections:

## Objective
- User-requested outcome and acceptance criteria.
- Scope boundaries, non-goals, and consequential assumptions.

## Authority and Context
- Active instruction files, workflow or plan, and relevant runtime/profile
  constraints.
- Repository, branch, worktree, permissions, environment, and external-system
  boundaries that affect the next action.

## Work Completed
- Decisions made and their rationale.
- Files changed, with a one-line purpose for each.
- Commands run and the relevant result; distinguish completed work from
  inspected-only evidence.

## Current State
- Exact plan step or task phase in progress.
- Important facts, identifiers, paths, revisions, errors, and reproduction
  details needed to resume.
- Existing user changes that must be preserved.

## Remaining Work
1. Ordered next actions with the first actionable command or file.
2. Required validation and success criteria.
3. Blockers, risks, unknowns, and any question that genuinely requires the
   user's decision.

Rules:
- Be concrete and compact; prefer verified facts over narrative.
- Clearly label inferences, failed attempts, and unverified claims.
- Never include secrets, tokens, full environment dumps, or private reasoning.
- Do not invent work, claim validation that did not run, or give the next agent
  generic advice that is already supplied by its instructions.
