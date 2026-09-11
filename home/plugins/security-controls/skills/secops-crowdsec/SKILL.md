---
name: secops-crowdsec
description: Configure CrowdSec collections, parser sources, and bouncer integration with safe enforcement defaults. Use when the user asks for CrowdSec detection or remediation setup.
metadata:
  version: '1.0'
  short-description: Configure CrowdSec collections, log sources, and bouncers safely
  tags:
  - crowdsec
  - security
  - observability
  - linux
interface:
  display-name: SECOPS-CrowdSec
  short-description: Configure CrowdSec collections, log sources, and bouncers safely
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC32B7'
  default-prompt: Act as the "SECOPS-CrowdSec" specialist for "Configure CrowdSec collections, log sources, and bouncers safely". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

# SKILL

## Execute the scoped task

1. State the authorized assets, threat model, entrypoints, sensitive data and trust boundaries. Distinguish a demonstrated exploit path from a theoretical concern.

2. Validate input at trust boundaries and enforce authorization on the server-side operation, not merely in the interface. Use parameterized queries and context-appropriate output encoding.

3. Keep secrets in approved stores, avoid credential dumps, and redact logs and examples. Preserve TLS verification, signature checks and explicit permission controls.

4. Prefer non-destructive inspection and minimal reproductions on authorized targets. Do not expand scanning or change production security settings to prove a finding.

5. Report the affected path, preconditions, impact, evidence and smallest effective fix. Verify the fix with the narrowest permitted existing checks and disclose remaining uncertainty.

## Task-specific details and resources

## Use this skill when

- configuring CrowdSec pipelines or bouncers
- tuning detections and whitelists

## Workflow

1. Scope log sources and threat model
2. Configure `acquis.yaml`
3. Validate parsing and detection
4. Enable remediation carefully

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

- `$CODEX_HOME/index/domains/observability/crowdsec.md`
- `$CODEX_HOME/docs/observability/crowdsec.md`
- `$CODEX_HOME/docs/workflows/crowdsec.md`
- `$CODEX_HOME/templates/observability/crowdsec-skeleton/`
- `$CODEX_HOME/snippets/crowdsec/acquis.yaml`
