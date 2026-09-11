# IaC task routing

Read this plugin only when its listed skills match the current task. Discover the actual client tools, account access and permission requirements before invoking anything. Treat this directory as bundled source, not proof of an installed or authenticated integration.

## Select one entrypoint

| Skill | Apply it to |
| --- | --- |
| [iac-ansible](skills/iac-ansible/SKILL.md) | Use this skill for author or refactor idempotent Ansible playbooks, roles, inventories, and handlers with safe defaults |
| [iac-terraform](skills/iac-terraform/SKILL.md) | Use this skill for plan, review, and modify Terraform configurations with safe state handling, module hygiene, and deterministic workflows |

## Preserve the integration boundary

Read only the references required by the selected skill. Inspect bundled scripts before execution; retain their argument and output contracts. Keep credentials and private payloads out of examples, logs and ambient hook context.

Do not install, enable, trust, publish or update a remote integration merely because you edit these files. Keep canonical and authorized bundled mirrors coherent, preserve existing resource paths and license notices, and report the checks you actually performed. Local packaging does not assert vendor endorsement.
