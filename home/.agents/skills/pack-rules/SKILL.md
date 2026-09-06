---
name: pack-rules
description: Create or update execpolicy rules and guidance under $CODEX_HOME/rules/.
  Use when adding new rule files, adjusting ordering, or updating execpolicy documentation
  and index links.
metadata:
  version: '1.0'
  short-description: Maintain execpolicy rules and guidance
  tags:
  - rules
  - execpolicy
  - security
  - pack
interface:
  display-name: PACK-Rules
  short-description: Maintain execpolicy rules and guidance
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#7F32CC'
  default-prompt: Act as the "PACK-Rules" specialist for "Maintain execpolicy rules and guidance".
    Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions.
    Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report
    concrete actions, evidence, and residual risks.
---

# PACK-Rules

## Use this skill when
- adding or updating rules in `$CODEX_HOME/rules/`
- changing execpolicy guidance or rule ordering
- wiring rule references into docs or index

## Inputs
- target rule files and expected policy effect
- ordering constraints (where the rule should execute in the chain)
- linked docs/index pages that must reflect the rule change

## Scope and boundaries
- Preserve deny-by-default and safety-critical guardrails unless explicitly requested.
- Keep rule ordering deterministic and documented.
- Avoid introducing bypass-oriented examples in docs or snippets.
- Require explicit rationale for any broadened allow-list or privilege expansion.
- Ensure every new rule has a clear rollback/remediation path.

## Workflow
1) Update rules in `$CODEX_HOME/rules/` and document intent in `$CODEX_HOME/rules/OVERVIEW.md`.
2) Ensure execpolicy docs reference new rules where needed.
3) Update `$CODEX_HOME/index/pack/rules.md` and `$CODEX_HOME/index/core/execpolicy.md` related links.

## Rule safety checklist
- Keep deny rules before broad allow rules when precedence matters.
- Prefer narrow command prefixes over broad wildcard-like coverage.
- Validate that rule examples do not encourage destructive defaults.
- Re-check compatibility with existing protected workflows and branch policies.

## Agent orchestration
- Delegate read-only policy inventory or ordering discovery only.
- Keep one owner for rule edits and verification output.

## Validation and testing
- Re-check rule ordering and linked docs/index references after edits.
- Capture policy interactions or follow-up checks in the handoff notes.

## Outputs
- Rule/docs diffs with explicit ordering and intent notes.
- Verification evidence from pack checks.
- Residual risk notes for any rule interactions requiring follow-up.

## References
- `$CODEX_HOME/rules/OVERVIEW.md`
- `$CODEX_HOME/rules/00-core.rules`
- `$CODEX_HOME/rules/10-vcs.rules`
- `$CODEX_HOME/rules/12-scripting.rules`
- `$CODEX_HOME/rules/20-network.rules`
- `$CODEX_HOME/rules/25-packages.rules`
- `$CODEX_HOME/rules/30-system.rules`
- `$CODEX_HOME/rules/35-crypto.rules`
- `$CODEX_HOME/rules/40-infra.rules`
- `$CODEX_HOME/rules/90-forbidden.rules`
- `$CODEX_HOME/docs/workflows/execpolicy.md`
- `$CODEX_HOME/index/pack/rules.md`
