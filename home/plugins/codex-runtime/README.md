# Codex Runtime task routing

Read this plugin only when its listed skills match the current task. Discover the actual client tools, account access and permission requirements before invoking anything. Treat this directory as bundled source, not proof of an installed or authenticated integration.

## Select one entrypoint

| Skill | Apply it to |
| --- | --- |
| [perl](skills/perl/SKILL.md) | Use this skill for write and review Perl for deterministic runtime helpers, CLI tools, and data transforms with strict validation and minimal shell exposure |
| [runtime-config](skills/runtime-config/SKILL.md) | Inspect rendered config, instruction rewrites, and home sync behavior. |
| [runtime-sandbox](skills/runtime-sandbox/SKILL.md) | Review Bubblewrap-backed Codex runtime isolation and ephemeral session state. |
| [schema-diff](skills/schema-diff/SKILL.md) | Compare checked-in config against upstream schema and release snapshots. |
| [setup-audit](skills/setup-audit/SKILL.md) | Audit installer behavior, rollout state, and verification coverage. |

## Preserve the integration boundary

Read only the references required by the selected skill. Inspect bundled scripts before execution; retain their argument and output contracts. Keep credentials and private payloads out of examples, logs and ambient hook context.

Do not install, enable, trust, publish or update a remote integration merely because you edit these files. Keep canonical and authorized bundled mirrors coherent, preserve existing resource paths and license notices, and report the checks you actually performed. Local packaging does not assert vendor endorsement.
