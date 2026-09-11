# Cloudflare Workers task routing

Read this plugin only when its listed skills match the current task. Discover the actual client tools, account access and permission requirements before invoking anything. Treat this directory as bundled source, not proof of an installed or authenticated integration.

## Select one entrypoint

| Skill | Apply it to |
| --- | --- |
| [cloudflare](skills/cloudflare/SKILL.md) | Use this skill for comprehensive Cloudflare platform skill covering Workers, Pages, storage (KV, D1, R2), AI (Workers AI, Vectorize, Agents SDK), networking (Tunnel, Spectrum), security (WAF, DDoS), and infrastructure-as-code (Terraform, Pulumi) |
| [cloudflare-r2](skills/cloudflare-r2/SKILL.md) | Operate Cloudflare R2-backed publication and artifact delivery paths with explicit bucket, prefix, credential, and immutability rules |
| [durable-objects](skills/durable-objects/SKILL.md) | Create and review Cloudflare Durable Objects |
| [sandbox-sdk](skills/sandbox-sdk/SKILL.md) | Build sandboxed applications for secure code execution |
| [web-perf](skills/web-perf/SKILL.md) | Use this skill for analyzes web performance using Chrome DevTools MCP |
| [workers-best-practices](skills/workers-best-practices/SKILL.md) | Use this skill for reviews and authors Cloudflare Workers code against production best practices |

## Preserve the integration boundary

Read only the references required by the selected skill. Inspect bundled scripts before execution; retain their argument and output contracts. Keep credentials and private payloads out of examples, logs and ambient hook context.

Do not install, enable, trust, publish or update a remote integration merely because you edit these files. Keep canonical and authorized bundled mirrors coherent, preserve existing resource paths and license notices, and report the checks you actually performed. Local packaging does not assert vendor endorsement.
