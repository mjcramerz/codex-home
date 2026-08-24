# Cloudflare DDoS Protection

Autonomous, always-on protection against DDoS attacks across L3/4 and L7.

## Protection Types

- **HTTP DDoS (L7)**: Protects HTTP/HTTPS traffic, phase `ddos_l7`, zone/account level
- **Network DDoS (L3/4)**: UDP/SYN/DNS floods, phase `ddos_l4`, account level only
- **Adaptive DDoS**: Learns 7-day baseline, detects deviations, 4 profile types (Origins, User-Agents, Locations, Protocols)

## Plan Availability

| Feature | Free | Pro | Business | Enterprise | Enterprise Advanced |
|---------|------|-----|----------|------------|---------------------|
| HTTP DDoS (L7) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Network DDoS (L3/4) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Override rules | 1 | 1 | 1 | 1 | 10 |
| Custom expressions | ✗ | ✗ | ✗ | ✗ | ✓ |
| Log action | ✗ | ✗ | ✗ | ✗ | ✓ |
| Adaptive DDoS | ✗ | ✗ | ✗ | ✓ | ✓ |
| Alert filters | Basic | Basic | Basic | Advanced | Advanced |

## Actions & Sensitivity

- **Actions**: `block`, `managed_challenge`, `challenge`, `log` (Enterprise Advanced only)
- **Sensitivity**: `default` (high), `medium`, `low`, `eoff` (essentially off)
- **Override**: By category/tag or individual rule ID
- **Scope**: Zone-level overrides take precedence over account-level

## Reading Order

| File | Purpose | Start Here If... |
|------|---------|------------------|
| [configuration.md]($CODEX_HOME/plugins/cache/codex-home/cloudflare-workers/local/skills/cloudflare/references/ddos/configuration.md) | Dashboard setup, rule structure, adaptive profiles | You're setting up DDoS protection for the first time |
| [api.md]($CODEX_HOME/plugins/cache/codex-home/cloudflare-workers/local/skills/cloudflare/references/ddos/api.md) | API endpoints, SDK usage, ruleset ID discovery | You're automating configuration or need programmatic access |
| [patterns.md]($CODEX_HOME/plugins/cache/codex-home/cloudflare-workers/local/skills/cloudflare/references/ddos/patterns.md) | Protection strategies, defense-in-depth, dynamic response | You need implementation patterns or layered security |
| [gotchas.md]($CODEX_HOME/plugins/cache/codex-home/cloudflare-workers/local/skills/cloudflare/references/ddos/gotchas.md) | False positives, tuning, error handling | You're troubleshooting or optimizing existing protection |

## See Also
- [waf]($CODEX_HOME/plugins/cache/codex-home/cloudflare-workers/local/skills/cloudflare/references/waf/) - Application-layer security rules
- [bot-management]($CODEX_HOME/plugins/cache/codex-home/cloudflare-workers/local/skills/cloudflare/references/bot-management/) - Bot detection and mitigation
