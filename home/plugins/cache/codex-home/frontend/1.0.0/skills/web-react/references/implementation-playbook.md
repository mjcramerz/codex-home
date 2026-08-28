---
title: Web React Implementation Playbook
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-react
- references
- implementation-playbook-md
- implementation-playbook
- user
- web
updated: '2026-02-25'
---
# Web React Implementation Playbook

## Scope and intent
Use this playbook for framework-neutral React work: components, hooks, client routing integrations, and performance-oriented refactors.

## Intake checklist
- Clarify whether request is feature, bug, refactor, or perf hardening.
- Identify critical screens and user journeys affected.
- Confirm state ownership and data source boundaries.
- Confirm acceptable performance and accessibility targets.

## Delivery sequence
1. Build component/state ownership map.
2. Identify side effects and move non-essential effects to render/event flow.
3. Apply prioritized rules from `react-performance-rules.md`.
4. Apply list/motion/interaction guidance from `react-native-web-adaptations.md`.
5. Run quality gates and targeted tests.
6. Return evidence, tradeoffs, and next-step recommendations.

## Decision rules
- Keep state minimal and derive computed values where possible.
- Prefer stable props and event handlers for memoized child trees.
- Treat async behavior as a design concern, not an afterthought.
- Avoid optimization churn without baseline evidence.
