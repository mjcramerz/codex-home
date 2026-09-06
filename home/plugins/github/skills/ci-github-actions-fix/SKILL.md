---
name: ci-github-actions-fix
description: Debug failing GitHub Actions checks by inspecting PR statuses and logs with gh,
  then propose and implement fixes after approval. Use when the user asks why GitHub PR CI
  failed or wants failing Actions checks fixed.
metadata:
  version: '1.0'
  short-description: Fix failing GitHub Actions checks
  tags:
  - github
  - gh
  - ci
  - actions
  - debugging
interface:
  display-name: CI-GitHub Actions Fix
  short-description: Fix failing GitHub Actions checks
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC327F'
  default-prompt: Act as the "CI-GitHub Actions Fix" specialist for "Fix failing GitHub Actions
    checks". Deliver focused, deterministic results with minimal, reviewable changes and explicit
    assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks,
    and report concrete actions, evidence, and residual risks.
---

# CI-GitHub Actions Fix

## Use this skill when
- a GitHub PR has failing checks and you need root cause + safe remediation.
- a workflow is flaky/intermittent and you need evidence before proposing fixes.

## Inputs
- `repo`: repository path (default `.`)
- `pr`: PR number or URL (optional; current-branch PR by default)
- `gh` authentication with access to checks and workflow logs

## Scope and boundaries
- Do not treat external providers as actionable GitHub Actions failures.
- Do not broad-rerun unrelated workflows to “green” CI.
- Keep fixes minimal and scoped to the failing cause.

## Workflow
1) Verify `gh` auth and resolve the target PR.
2) Run `scripts/inspect_pr_checks.py` first (`--json` optional), then use manual `gh` fallback only if fields/logs are unavailable.
3) Isolate failing workflow/job, capture the smallest useful snippet, and include check name + run URL.
4) Separate external/non-GitHub-Actions checks from actionable workflow failures.
5) Propose a minimal, reversible fix plan; implement after approval.
6) Re-run the narrowest checks and confirm status via `gh pr checks`.

## Manual fallback commands
- `gh pr checks <pr> --json name,state,bucket,link,startedAt,completedAt,workflow`
- `gh run view <run_id> --json name,workflowName,conclusion,status,url,event,headBranch,headSha`
- `gh run view <run_id> --log`
- `gh api "/repos/<owner>/<repo>/actions/jobs/<job_id>/logs" > <path>`

## Agent orchestration
- Delegate log collection and inventory only.
- Keep diagnosis, fix strategy, and risk sign-off centralized.

## Validation and testing
- Bound log size/time (`--max-lines`, `--context`) and avoid noisy full-log dumps.
- Confirm reproducibility before editing and capture the failing command/check identifier.
- Run only the checks required to prove the fix, then re-check status with `gh pr checks`.

## Outputs
- Failure summary with evidence (check, run URL, snippet).
- Minimal fix plan with impact/risk notes.
- Verification notes showing before/after check state.

## References
- `scripts/inspect_pr_checks.py`
- `$CODEX_HOME/docs/workflows/github-actions.md`
- `$CODEX_HOME/docs/workflows/ci-cd.md`
- Use skill ci-github-actions.
