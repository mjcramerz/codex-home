---
title: infra-kubernetes reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-kubernetes
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-25'
---
# infra-kubernetes reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: `web.search` + `web.open` + Context7 library docs (`resolve-library-id`, `get-library-docs`) on vendor-owned sources.
- Fetch note: `mcp__fetch__fetch` was attempted in this environment and currently fails with `npm install` exit 243; references were validated via `web` + Context7 instead.

## Skill purpose
Build and validate Kubernetes manifests with safe defaults.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Checkpoint gates
- Agent orchestration
- Validation and testing
- Outputs
- Local resources
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/kubernetes/local/skills/infra-kubernetes/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/kubernetes/local/skills/infra-kubernetes/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/kubernetes/local/skills/infra-kubernetes/scripts/skill_helper.py`

## Reference files in this directory
- `latest-sources.md`
- `operations-checklist.md`
- `risk-register.md`
- `rollout-runbook.md`
- `workload-security-baseline.md`

## Context7 coverage
- `/kubernetes/website`

## Web verification targets
- `https://kubernetes.io/docs/concepts/security/pod-security-standards/`
- `https://kubernetes.io/docs/reference/kubectl/`

## External references
- [Kubernetes Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) - Baseline/Restricted controls for workload admission and runtime hardening.
- [Kubernetes Deployment docs](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) - Rollout, surge/unavailable behavior, and rollback mechanics.
- [kubectl reference](https://kubernetes.io/docs/reference/kubectl/) - Validation, diff, apply, and rollout command semantics.

## Proof-of-concept prompts
- Build a minimum viable runbook for `infra-kubernetes` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `infra-kubernetes` before finalizing changes.
