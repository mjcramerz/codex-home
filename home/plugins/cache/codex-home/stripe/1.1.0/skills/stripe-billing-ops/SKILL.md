---
name: stripe-billing-ops
description: Stripe billing operations, invoicing, and customer-impact reviews
metadata:
  version: '1.0'
  short-description: Stripe Billing Ops
  tags:
  - plugin
  - stripe
  - billing
  - ops
---

# Stripe Billing Ops

Use this skill when the active task maps cleanly to the `stripe-billing-ops` bundle.

- Clarify whether the task is customer-facing billing logic or internal operations first.
- Separate payment authorization, invoicing, and entitlement state changes.
- Document the rollback and customer-impact plan for any billing mutation.

## References
- [Stripe Billing](https://docs.stripe.com/billing)
- [Stripe webhooks](https://docs.stripe.com/webhooks)
