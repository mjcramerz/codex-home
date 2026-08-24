# Planning workflow
Purpose: provide the canonical planning workflow for this pack for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

You must start with `$CODEX_HOME/plans/workflows/workflow-planning.md` before executing this workflow.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Required routing contract
- `$CODEX_HOME/AGENTS.md`
- `$CODEX_HOME/memories/` when the task is repo-aware or ambiguous
- `$CODEX_HOME/INDEX.md`
- `$CODEX_HOME/index/pack/plans.md` + `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/pack/skills.md`
- follow `$CODEX_HOME/docs/style/shell-runtime.md` before running commands

## Runtime-state boundary
- You must use `$CODEX_HOME/memories/` for context only when prior decisions matter.
- You must treat runtime memory as generated state and only inspect it when the live `$CODEX_HOME/memories/` directory already exists for the task.
- You must keep plans grounded in stable installed pack surfaces and avoid repository-source paths in final guidance.

## Plan selection (quick guide)
- **Workflow-specific work**: use `$CODEX_HOME/plans/workflows/` (for example `workflow-<name>.md`).
- **Skill-driven work**: use `$CODEX_HOME/plans/skills/` (for example `skill-<name>.md`).
- **General engineering tasks**: use `$CODEX_HOME/plans/frameworks/` (feature, bugfix, refactor, security, perf, infra, docs).

## Plan schema (required sections)
A plan should include:
- **Objective**
- **Scope**
- **Constraints / Non-goals**
- **Current state (inventory)**
- **Plan (steps)**
- **Validation (tests & checks)**
- **Risks / Rollback**
- **References**

## Creation rules
- Non-trivial tasks and any multi-file refactor require a plan.
- If no template fits, create a new template in the correct plan family and list it in the relevant overview in the same change.
- When a plan touches external repos or delivery contracts, list those repos explicitly in the inventory section.

## Security checkpoints
- You must add threat assumptions and privileged operations to the plan before implementation begins.
- Attach input bounds/timeouts to steps that touch I/O, parsing, or remote systems.
- You must record waiver owner and expiry for every planned security exception.

## Testing checkpoints
- Every step includes a concrete verify command plus pass/fail expectation.
- For bugfix or hardening work, require at least one failing or abuse test in the plan.
- You must define fast-path versus full-suite checkpoints for incremental validation.

## Deployment checkpoints
- Include rollout, rollback, and migration/flag steps when runtime behavior changes.
- Mark go/no-go gates and required evidence before staging/release promotion.
- Identify who confirms post-deploy health and where evidence is stored.

## References
- `overview.md`
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/core/plan.md`
