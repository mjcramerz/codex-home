---
name: stripe-payments
description: Use this skill for stripe payment flows, checkout, subscriptions, and webhooks.
metadata:
  version: '1.0'
  short-description: Stripe Payments
  tags:
  - plugin
  - stripe
  - payments
---

# Stripe Payments

## Execute the scoped task

1. Confirm the Stripe account, test/live mode, API version and exact payment or webhook flow. Inspect the integration and advertised tools without printing API keys or customer payment data.

2. Trace amount/currency validation, idempotency, authorization, webhook signature verification and duplicate/out-of-order event handling. Do not trust client-supplied prices or success redirects as settlement evidence.

3. Implement only the authorized change and use existing test-mode fixtures. Obtain explicit scope before creating charges, refunds, subscriptions or live webhook changes.

4. Report the changed integration boundary, observed test outcomes and untested live behavior. Do not claim a sandbox result moved real money.

## Task-specific details and resources

- Map the billing surface first: checkout, subscriptions, invoices, or webhooks.
- Keep secret handling, idempotency, and signature verification explicit.
- Pair implementation changes with webhook or API contract validation steps.

## References

- [Stripe docs](https://docs.stripe.com/)
- [Stripe API reference](https://docs.stripe.com/api)
