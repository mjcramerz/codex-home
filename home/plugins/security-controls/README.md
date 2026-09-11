# Security Controls task routing

Read this plugin only when its listed skills match the current task. Discover the actual client tools, account access and permission requirements before invoking anything. Treat this directory as bundled source, not proof of an installed or authenticated integration.

## Select one entrypoint

| Skill | Apply it to |
| --- | --- |
| [appsec-hardening](skills/appsec-hardening/SKILL.md) | Apply application security hardening controls such as input validation, authn/authz checks, safe subprocess patterns, security headers, and abuse-rate defenses |
| [bws-local](skills/bws-local/SKILL.md) | Use this skill for install, configure, and rotate Bitwarden Secrets Manager CLI (bws) for local Debian systems with keyring-backed secret storage |
| [secops-aide](skills/secops-aide/SKILL.md) | Configure AIDE file-integrity monitoring rules, baselines, and scheduled verification runs |
| [secops-auditd](skills/secops-auditd/SKILL.md) | Configure auditd rules and log capture policies with safe performance tradeoffs and compliance alignment |
| [secops-crowdsec](skills/secops-crowdsec/SKILL.md) | Configure CrowdSec collections, parser sources, and bouncer integration with safe enforcement defaults |
| [secops-supply-chain](skills/secops-supply-chain/SKILL.md) | Harden software supply-chain controls through dependency pinning, lockfile discipline, SBOM generation, and CI enforcement |
| [secops-usbguard](skills/secops-usbguard/SKILL.md) | Configure USBGuard device authorization policies and rule sets for USB attack surface reduction |
| [security-best-practices](skills/security-best-practices/SKILL.md) | Perform language and framework specific security best-practice reviews and suggest improvements |
| [security-ownership-map](skills/security-ownership-map/SKILL.md) | Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization |
| [security-threat-model](skills/security-threat-model/SKILL.md) | Use this skill for repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model |

## Preserve the integration boundary

Read only the references required by the selected skill. Inspect bundled scripts before execution; retain their argument and output contracts. Keep credentials and private payloads out of examples, logs and ambient hook context.

Do not install, enable, trust, publish or update a remote integration merely because you edit these files. Keep canonical and authorized bundled mirrors coherent, preserve existing resource paths and license notices, and report the checks you actually performed. Local packaging does not assert vendor endorsement.
