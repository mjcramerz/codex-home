---
title: storage-filesystems reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- storage-filesystems
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-20'
---
# storage-filesystems reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Safe filesystem planning: partitioning, mkfs, mounting, and fstab with explicit confirmation and rollback.

## SKILL.md coverage checklist
- Use this skill when
- Safety rules (non-negotiable)
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/storage-filesystems/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/storage-filesystems/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/storage-filesystems/scripts/skill_helper.py`

## Reference files in this directory
- `latest-sources.md`
- `operations-checklist.md`
- `risk-register.md`

## External references
- [fstab man page](https://man7.org/linux/man-pages/man5/fstab.5.html) - Filesystem mount table schema and semantics.
- [mount man page](https://man7.org/linux/man-pages/man8/mount.8.html) - Mount options and lifecycle operations.

## Proof-of-concept prompts
- Build a minimum viable runbook for `storage-filesystems` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `storage-filesystems` before finalizing changes.
