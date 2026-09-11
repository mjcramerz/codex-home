---
title: DNS defense operations (Pi-hole + Unbound)
status: active
owner: Matthew Cramer
tags:
- skills
- all
- offsec-defense
- references
- dns-defense-pihole-unbound-md
- dns-defense-pihole-unbound
- user
- security-labs
updated: '2026-02-20'
---
# DNS defense operations (Pi-hole + Unbound)

## Objective
Harden recursive DNS and ad/malware blocking with deterministic operations.

## Architecture baseline
- Pi-hole handles policy, blocklists, and query visibility.
- Unbound provides local recursive resolution with DNSSEC validation.
- Internal clients use Pi-hole as their resolver.

## Security checks
1) Confirm recursion is restricted to trusted clients.
2) Confirm DNSSEC validation is enabled and monitored.
3) Validate upstream privacy posture (DoT/DoH or strict upstream policy).
4) Review blocklist update provenance and cadence.
5) Validate backup/restore for gravity lists and local DNS records.

## Operational checks
- Query success rate and latency
- Blocked domain volume and false-positive trends
- Unbound cache hit ratio and timeout rates
- Alerting for resolver failures and service restarts

## References
- Pi-hole documentation: https://docs.pi-hole.net/
- Unbound documentation: https://nlnetlabs.nl/projects/unbound/about/
- DNS security best practices: https://www.cisa.gov/resources-tools/resources/securing-domain-name-system-dns
