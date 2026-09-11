---
name: setup-audit
description: Audit installer behavior, rollout state, and verification coverage.
metadata:
  version: '2.0'
  short-description: Setup Audit
  tags:
  - plugin
  - setup-audit
---

# Setup Audit

## Execute the scoped task

1. Resolve the source checkout, deployed CODEX_HOME, identity, executable versions and intended filesystem layout. Do not assume the supplied absolute paths exist.

2. Check the relevant configuration paths, instruction mirrors, hook entrypoint and MCP transport declarations without reading credentials or invoking arbitrary repository code.

3. Distinguish absent files, mismatched configuration, inactive services, missing authentication and unavailable model entitlement. Do not repair unrelated systems during a read-only audit.

4. Return concrete paths and evidence with a bounded remediation plan. Label parser checks, fixtures and live host observations separately.

## Task-specific details and resources

- Inspect install, home, admin, and verify flows before drawing conclusions.
- Prefer the narrowest proof command for each claim.
- Highlight permission boundaries, preserved state, and cleanup semantics.
