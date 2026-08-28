---
name: secops-aide
description: Configure AIDE file-integrity monitoring rules, baselines, and scheduled verification
  runs. Use when the user asks for host file integrity monitoring or tamper-detection setup.
metadata:
  version: '1.0'
  short-description: Configure AIDE file integrity monitoring
  tags:
  - aide
  - integrity
  - security
  - linux
interface:
  display-name: SECOPS-AIDE
  short-description: Configure AIDE file integrity monitoring
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32C9CC'
  default-prompt: Act as the "SECOPS-AIDE" specialist for "Configure AIDE file integrity monitoring".
    Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions.
    Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report
    concrete actions, evidence, and residual risks.
---

## Use this skill when
- setting up AIDE baselines
- reviewing integrity policies

## Workflow
1) Scope critical paths
2) Initialize baseline
3) Schedule checks
4) Review diffs and update baseline

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

- Actionable steps or artifacts aligned to the skill.
- References to relevant files, commands, or templates.

## References
- `$CODEX_HOME/index/domains/observability/aide.md`
- `$CODEX_HOME/docs/observability/aide.md`
- `$CODEX_HOME/docs/workflows/aide.md`
- `$CODEX_HOME/templates/observability/aide-skeleton/`
- `$CODEX_HOME/snippets/aide/aide.conf`
