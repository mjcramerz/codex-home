---
title: quality-code-review reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- quality-code-review
- references
- latest-sources-md
- latest-sources
- admin
updated: '2026-02-25'
---
# quality-code-review reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
High-rigor code review skill: intent alignment, correctness, security, performance, and reproducibility checks with actionable output.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Review output format
- Review heuristics
- Security and reliability checks (quick)
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_SKILLS/quality-code-review/SKILL.md`
- `$CODEX_SKILLS/quality-code-review/agents/openai.yaml`

## External references
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) - Secure defaults and implementation guidance.
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) - Application security verification requirements.
- [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) - Secure software development baseline controls.
- [Code review best practices](https://google.github.io/eng-practices/review/) - Review standards for correctness and maintainability.

## Proof-of-concept prompts
- Build a minimum viable runbook for `quality-code-review` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `quality-code-review` before finalizing changes.
