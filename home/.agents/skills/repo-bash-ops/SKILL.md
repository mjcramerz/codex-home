---
name: repo-bash-ops
description: Implement repository automation in Bash for safe git operations, release scripts,
  and CI helper tooling. Use when the user asks for shell-based repo ops, automation scripts,
  or release hygiene tasks.
metadata:
  version: '2.2'
  short-description: Automate repo operations safely with deterministic Bash workflows
  tags:
  - bash
  - git
  - repo
  - automation
  - ci
interface:
  display-name: REPO-Bash Ops
  short-description: Automate repo operations safely with deterministic Bash workflows
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#3282CC'
  default-prompt: Act as the "REPO-Bash Ops" specialist for "Automate repo operations safely
    with deterministic Bash workflows". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O,
    run the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

## Use this skill when
- implementing repo automation in Bash for git/release/CI operations
- adding guardrails around branch sync, tagging, and delivery scripts
- standardizing deterministic, auditable scripting patterns
- preserving Bash-specific repo tooling when the broader `repo-ops` skill would otherwise be too generic

## Inputs
- target scripts and command surfaces to change
- branch/tag policy (`mcr/*`, optional read-only `github/*` mirrors, protected release tags) and remote expectations
- required confirmation model (`--dry-run`, `--yes`, rollback behavior)
- expected operator output format (`--json` or concise text)

## Scope and boundaries
- Prefer `repo-ops` for new general repo automation work; keep this skill for explicitly Bash-bound implementations.
- Default to read-only operations until preconditions are verified.
- Require explicit confirmation (`--yes`) and `--dry-run` for mutating actions.
- Never rewrite shared history by default; no implicit force-push flows.
- Treat `github/*` as read-only mirrors when present.
- Disallow hidden destructive shortcuts (`git reset --hard`, `git clean -fd`, force push) unless explicitly requested.

## Workflow
1) Validate context (`git rev-parse --show-toplevel`, clean worktree, expected branch namespace).
2) Validate branch/remote policy (`origin` fetch/prune, `mcr/*` flow, protected promotion branches).
3) Implement script changes with deterministic behavior (bounded I/O, explicit retries/timeouts, stable parsing).
4) Preserve delivery sequencing (`checkout -> true sync -> version bump -> patch apply -> push`) and release-tag guards.
5) Keep rollback notes explicit for mutating release/sync actions.
6) Keep script output operator-friendly (`--json` or concise text summaries) and redact secrets.
7) Run narrow behavior checks and document residual risks.

## Agent orchestration
- Delegate only read-only discovery or command-inventory tasks.
- Reconcile findings before modifying shared automation scripts.

## Validation and testing
- Validate input shape/range and failure paths.
- Test `--dry-run` and confirm-mode paths separately.
- Verify clean-worktree enforcement and branch/tag safety checks.
- Run `shellcheck` plus the narrowest script-level checks needed to prove behavior.

## Outputs
- Reviewable Bash diffs with explicit safety guardrails.
- Clear operator contract (`--dry-run`, confirmation flags, failure messages).
- Verification evidence and next-step checks.

## References
- `$CODEX_HOME/docs/workflows/repo-ops.md`
- `$CODEX_HOME/docs/workflows/release.md`
- `$CODEX_HOME/snippets/bash/repo_ops_helpers.sh`
