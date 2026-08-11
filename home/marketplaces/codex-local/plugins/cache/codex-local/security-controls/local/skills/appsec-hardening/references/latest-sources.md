---
title: appsec-hardening reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- appsec-hardening
- references
- latest-sources-md
- latest-sources
- user
- security
updated: '2026-02-20'
---
# appsec-hardening reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Practical application security hardening: input validation, auth, safe subprocess, web security headers, and abuse resistance.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Hardening workflow
- Web/API defaults
- Subprocess safety
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-local/security-controls/local/skills/appsec-hardening/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-local/security-controls/local/skills/appsec-hardening/agents/openai.yaml`

## External references
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) - Secure defaults and implementation guidance.
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) - Application security verification requirements.
- [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) - Secure software development baseline controls.
- [CWE Top 25](https://cwe.mitre.org/top25/archive/2024/2024_key_insights.html) - Prioritized weakness classes for reviews.

## Proof-of-concept prompts
- Build a minimum viable runbook for `appsec-hardening` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `appsec-hardening` before finalizing changes.
