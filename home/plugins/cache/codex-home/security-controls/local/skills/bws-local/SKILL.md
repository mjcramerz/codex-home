---
name: bws-local
description: Install, configure, and rotate Bitwarden Secrets Manager CLI (bws) for local
  Debian systems with keyring-backed secret storage. Use when the user asks for local
  BWS lifecycle operations outside CI/CD.
metadata:
  version: '1.0'
  short-description: Local Debian BWS lifecycle with secure keyring storage and sudo-bounded
    operations
  tags:
  - bws
  - bitwarden
  - secrets
  - keyring
  - debian
  - local
interface:
  display-name: BWS-Local
  short-description: Local Debian BWS lifecycle with secure keyring storage and sudo-bounded
    operations
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#3270CC'
  default-prompt: Act as the "BWS-Local" specialist for "Local Debian BWS lifecycle with secure
    keyring storage and sudo-bounded operations". Deliver focused, deterministic results with
    minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

## Use this skill when
- the task is local host setup for Bitwarden Secrets Manager CLI (`bws`)
- you need to store `BWS_ACCESS_TOKEN` and `BWS_PROJECT_ID` in local keyring
- you are rotating local credentials for local BWS state
- the user explicitly wants local-only flow (not CI/CD integrations)

## Scope guardrails
- Keep scope local to workstation/server operations.
- Do not add or modify CI/CD BWS wiring unless explicitly requested.
- Enforce non-root invocation and use sudo only for privileged filesystem/package actions.

## Workflow
1) Validate environment: Debian host, command dependencies, and trust boundaries.
2) Validate inputs: install path, release integrity values, token/project ID shape.
3) Install pinned `bws` binary and configure deterministic system PATH exposure.
4) Bootstrap keyring runtime and store/update `BWS_ACCESS_TOKEN` + `BWS_PROJECT_ID`.
5) Verify local behavior (`bws --version`, keyring status, keyring export/exec).
6) Rotate keyring entries and verify local read-path behavior after updates.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Validate critical inputs and bound external I/O (size, retries, and timeouts) before applying changes.
- Run the narrowest relevant checks that prove behavior (tests, lint, or build as applicable).
- Include risk-based negative or edge-case coverage for security-sensitive, parsing, or automation changes.
- Report verification commands, outcomes, and any follow-up checks that remain.

## Outputs
- Hardened local BWS install/update implementation.
- Local keyring lifecycle controls for token/project ID persistence and rotation.
- Verification transcript without exposing secret values.

## References
- `$CODEX_HOME/docs/security/bitwarden-secrets-local.md`
- `$CODEX_HOME/docs/workflows/bws-local.md`
- `$CODEX_HOME/index/domains/system/bws-local.md`
