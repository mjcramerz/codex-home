---
title: health-adhd-cbt reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- health-adhd-cbt
- references
- latest-sources-md
- latest-sources
- admin
updated: '2026-02-25'
---
# health-adhd-cbt reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Comprehensive ADHD planning and CBT-based (sometimes requested as "CBD") daily templates with PDF generation workflows. Use when generating printable ADHD/CBT worksheets, daily planners, impulse-control decision filters, emotion regulation check-ins, or when converting template content to PDF/HTML using the bundled scripts and assets.

## SKILL.md coverage checklist
- Use this skill when
- Overview
- Privacy and safety guardrails
- Quick start
- Workflow
- Template inventory
- Scripts
- Agent orchestration
- Validation and testing
- Outputs
- References
- Notes

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/health-planning/local/skills/health-adhd-cbt/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/health-planning/local/skills/health-adhd-cbt/agents/openai.yaml`

## External references
- [NIMH ADHD overview](https://www.nimh.nih.gov/health/topics/attention-deficit-hyperactivity-disorder-adhd) - High-level ADHD guidance and references.
- [CDC ADHD resources](https://www.cdc.gov/adhd/index.html) - Public-health information for ADHD planning context.
- [NIMH Psychotherapies](https://www.nimh.nih.gov/health/topics/psychotherapies) - Psychotherapy context and evidence framing.
- [NICE ADHD guidance](https://www.nice.org.uk/guidance/ng87) - Clinical guideline reference for checklist framing.
- [WHO mental health resources](https://www.who.int/health-topics/mental-health) - Global mental health context.
- [OWASP ASVS V5](https://owasp.org/www-project-application-security-verification-standard/) - Input validation and safe file processing controls for renderer scripts.

## Proof-of-concept prompts
- Build a minimum viable runbook for `health-adhd-cbt` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `health-adhd-cbt` before finalizing changes.
