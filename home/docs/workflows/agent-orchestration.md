# Agent orchestration workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-agent-orchestration.md` before executing this workflow.
Purpose: coordinate multi-agent execution with explicit ownership, deterministic handoffs, and bounded risk for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## You must use this file when
- the task is large enough to justify multiple roles
- discovery, implementation, review, and testing can be split into independent slices
- you need explicit ownership and reconciliation before final verification

## You must use this role model
- You must use `$CODEX_HOME/AGENTS.md` to choose the role mix.
- `manager` and `planner` decompose and gate.
- `orchestrator` and `delegator` control active child-thread lifecycle and handoff packaging.
- `explorer` and `hunter` gather evidence.
- `worker` and `coder` implement bounded slices.
- `analyst` compares child outputs and resolves conflicts.
- `synthesizer` merges converged child outputs into one parent-owned artifact.
- `reviewer` and `tester` close the loop with findings and verification.

## You must follow this workflow
1. Decompose the task into independent slices with clear acceptance criteria, validation commands, and stop conditions.
2. Assign each slice one owner, one entrypoint, and one explicit thread-lifecycle plan: spawn, resume, wait, or close.
3. Require each owner to report commands run, files touched, evidence gathered, and remaining risks.
4. Use `analyst` when child outputs conflict or leave evidence gaps; use `synthesizer` only after the evidence converges.
5. Reconcile findings before any final patch or validation pass.
6. Run final verification under one coordinating owner.

## You must hand off this information
- Objective
- Owned files or surfaces
- Required entrypoint
- Commands or checks already run
- Outstanding blockers or risks

## You must enforce these guardrails
- You must keep overlapping file ownership to a minimum.
- Do not hand off destructive or release-sensitive steps without explicit approval and rollback notes.
- You must prefer role-oriented guidance over tool-specific control names unless the active runtime explicitly provides them.

## After that, you must check related files
- `$CODEX_HOME/AGENTS.md`
- `$CODEX_HOME/docs/workflows/planning.md`
- `$CODEX_HOME/docs/workflows/repo-ops.md`
- `$CODEX_HOME/docs/workflows/code-review.md`
- `$CODEX_HOME/index/core/plan.md`
- `$CODEX_HOME/index/core/testing.md`
- You must use skill `workflow-plans`.
