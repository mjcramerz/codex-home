---
name: installer-regression-audit
description: Use this skill to review install, home-sync, admin, upgrade, and cleanup
  flows for regressions, permission boundaries, and preserved-state drift. Use when
  the user asks for installer audits or rollout safety reviews.
metadata:
  version: '1.0'
  short-description: Audit installer flows for regressions and permission drift
  tags:
  - audit
  - installer
  - regression
  - permissions
interface:
  display-name: AUDIT-Installer Regression
  short-description: Audit installer flows for regressions and permission drift
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#2563EB'
  default-prompt: Act as the "AUDIT-Installer Regression" specialist for "Audit installer
    flows for regressions and permission drift". Deliver focused, deterministic results
    with minimal, reviewable changes and explicit assumptions. Validate untrusted
    inputs and bounded I/O, run the narrowest relevant checks, and report concrete
    actions, evidence, and residual risks.
---

# Installer Regression Audit

## Workflow

1. Trace source-to-target copy ownership, preserved state, permissions and rollback behavior. Identify canonical inputs rather than editing installed state by accident.

2. Inspect path normalization, symlink handling, temporary files, atomic replacement and ownership transitions. Flag traversal or recursive deletion risks.

3. Exercise the narrow existing staging or dry-run path only after checking its real side effects. Distinguish mocked service/engine calls from live deployment.

4. Report regressions with the affected path, transition, evidence and smallest corrective change; preserve credentials and session state.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
