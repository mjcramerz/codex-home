---
title: desktop-thorium reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- desktop-thorium
- references
- latest-sources-md
- latest-sources
- user
- default
updated: '2026-02-20'
---
# desktop-thorium reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Plan and validate Thorium Browser builds.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/web-browser-linux/local/skills/desktop-thorium/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/web-browser-linux/local/skills/desktop-thorium/agents/openai.yaml`

## External references
- [Freedesktop Desktop Entry Specification](https://specifications.freedesktop.org/desktop-entry-spec/latest/) - Desktop launcher schema and semantics.
- [Wayland project](https://wayland.freedesktop.org/) - Wayland protocol and compositor context.
- [Mozilla Policy Templates](https://mozilla.github.io/policy-templates/) - Browser enterprise hardening policy options.
- [Thorium release repository](https://github.com/Alex313031/thorium/releases) - Version and release validation.

## Proof-of-concept prompts
- Build a minimum viable runbook for `desktop-thorium` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `desktop-thorium` before finalizing changes.

