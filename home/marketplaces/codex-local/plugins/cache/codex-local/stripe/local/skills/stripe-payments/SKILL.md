---
name: stripe-payments
description: Stripe payment flows, checkout, subscriptions, and webhooks
metadata:
  version: '1.0'
  short-description: Stripe Payments
  tags:
  - plugin
  - stripe
  - payments
---

# Stripe Payments

Use this skill when the active task maps cleanly to the `stripe-payments` bundle.

- Map the billing surface first: checkout, subscriptions, invoices, or webhooks.
- Keep secret handling, idempotency, and signature verification explicit.
- Pair implementation changes with webhook or API contract validation steps.

## References
- [Stripe docs](https://docs.stripe.com/)
- [Stripe API reference](https://docs.stripe.com/api)
