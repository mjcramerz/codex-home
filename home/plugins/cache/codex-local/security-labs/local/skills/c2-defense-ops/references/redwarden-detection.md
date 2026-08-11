---
title: RedWarden-style redirector detection
status: active
owner: Matthew Cramer
tags:
- skills
- all
- c2-defense-ops
- references
- redwarden-detection-md
- redwarden-detection
- user
- security-labs
updated: '2026-02-20'
---
# RedWarden-style redirector detection

## Objective
Assess whether defensive telemetry can identify resilient redirector behavior.

## Defensive checks
- suspicious redirect patterns and fake-response behavior
- mismatched host/header patterns in ingress traffic
- known bad source ranges and enrichment logic quality
- replay/mutated request detection effectiveness

## Reference sources
- https://attack.mitre.org/techniques/T1090/
- https://www.cisa.gov/news-events/cybersecurity-advisories
- https://www.sans.org/white-papers/39605/
