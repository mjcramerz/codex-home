---
name: repo-ops
description: Plan and implement safe repository operations, git automation, release workflows,
  and CI helper tooling with deterministic contracts. Use when the user asks for repo automation,
  release hygiene, branch promotion, or tooling that touches git state.
metadata:
  version: '1.0'
  short-description: Drive safe repo automation, branch promotion, release flows, and git hygiene
  tags:
  - git
  - repo
  - automation
  - release
  - ci
  - workflow
interface:
  display-name: REPO-Ops
  short-description: Drive safe repo automation, branch promotion, release flows, and git hygiene
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#327FCC'
  default-prompt: Act as the "REPO-Ops" specialist for "Drive safe repo automation, branch promotion,
    release flows, and git hygiene". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O,
    run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- automating git workflows, branch promotion, release tagging, or repo maintenance tasks
- adding or hardening CI helper tooling that reads or mutates repository state
- designing operator-safe repo runbooks, dry-run flows, and rollback contracts
- reviewing repo hygiene controls around clean worktrees, protected refs, or deterministic delivery order
- coordinating repo automation where the implementation language may vary but git safety rules stay constant

## Inputs
- target repository, working tree expectations, and branch/tag policy (`mcr/*`, mirrors, protected refs)
- required operation type (read-only audit, sync, release prep, patch application, branch promotion, cleanup, or automation script change)
- implementation substrate (shell, Python, CI YAML, Make target, or existing repo helper)
- confirmation model (`--dry-run`, `--yes`, explicit operator approval, rollback contract)
- expected operator output format (concise text, JSON, or CI-friendly logs)

## Scope and boundaries
- Default to read-only inspection until repo root, branch, remote, and worktree preconditions are verified.
- Require explicit confirmation and a dry-run path for mutating repo operations when the surface supports it.
- Never rewrite shared history, delete refs, or force-push by default.
- Treat mirror refs and promotion branches as policy-controlled surfaces; preserve the documented order.
- Keep implementation language choices secondary to operator safety: prefer the smallest deterministic change that matches the repo runtime.
- When shell is the correct implementation substrate, confirm the runtime with the command in `$CODEX_HOME/AGENTS.md`, then pair this skill with `$CODEX_HOME/UNIX.md`, `shell-bash`, `shell-zsh`, or `shell-sh` based on the confirmed runtime.

## Workflow
1) Validate repository context (`git rev-parse --show-toplevel`, expected remote, branch namespace, clean or intentionally dirty worktree state).
2) Classify the operation (audit, sync, release, patch, automation change) and identify protected refs or policy gates.
3) Define the operator contract up front: dry-run behavior, confirmation path, rollback notes, and expected output.
4) Implement the smallest deterministic change in the repo's native tooling surface.
5) Preserve delivery sequencing (`checkout -> true sync -> version bump -> patch apply -> push`, protected tag rules, promotion order) when the workflow is release-sensitive.
6) Validate failure modes separately from the happy path, especially ambiguous branch state, dirty worktrees, and protected ref checks.
7) Report touched refs, required follow-up commands, and residual risk before handoff.

## Implementation guidance
- Git safety:
  - verify repo root and current HEAD before mutating anything
  - prefer `--ff-only`, explicit ref names, and machine-readable git output where available
  - record source and target SHAs for branch promotions and release tags
- Automation surface:
  - shell helpers should use arrays and avoid shell-string interpolation
  - CI helpers should avoid implicit branch detection when the ref can be passed explicitly
  - Make or wrapper commands should surface underlying git intent clearly
- Operator UX:
  - dry-run output should describe the exact refs, files, or commands that would change
  - destructive actions must require explicit opt-in and name the rollback path
  - logs should redact secrets and avoid dumping entire environments
- Pairing:
  - use `repo-bash-ops` only when the implementation must stay Bash-specific

## Agent orchestration
- Delegate only read-only discovery (ref inventory, workflow catalog audit, CI surface mapping).
- Keep one owner for final automation edits so branch, tag, and rollback semantics stay coherent.

## Validation and testing
- Validate input shape, protected-ref checks, and failure paths before mutating repo state.
- Exercise dry-run and confirm-mode paths separately when the tooling supports both.
- Run the narrowest script or workflow checks that prove the updated repo operation behaves as expected.
- Confirm clean-worktree enforcement and protected branch or tag guards still fire.
- Report skipped validations explicitly when credentials or remotes are unavailable.

## Outputs
- Reviewable repo automation diffs with explicit safety gates and rollback notes.
- Clear operator contract for ref selection, dry-run behavior, and approval requirements.
- Verification evidence covering both policy checks and command behavior.

## References
- `$CODEX_HOME/docs/workflows/repo-ops.md`
- `$CODEX_HOME/docs/workflows/release.md`
- `$CODEX_HOME/index/core/repo-ops.md`
- `$CODEX_HOME/docs/style/bash.md`
