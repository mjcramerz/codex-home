---
name: stripe-billing-ops
description: Use this skill for stripe billing operations, invoicing, and customer-impact reviews.
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

## Execute the scoped task

1. Confirm account, mode, customer/subscription/invoice identifiers and the exact requested billing operation. Use a relevant read to resolve ambiguity without exposing private customer data.

2. Inspect proration, billing-cycle anchors, taxes, retries and downstream entitlement effects before mutation. Distinguish a draft invoice, finalized invoice, attempted payment and settled payment.

3. Perform only the explicitly authorized operation, with idempotency and an identified recovery path where supported. Do not bulk-modify customers or retry a charge blindly.

4. Return the actual resulting IDs/statuses and any unresolved customer-impact risk, with test-mode results clearly distinguished from live operations.

## Task-specific details and resources

- Clarify whether the task is customer-facing billing logic or internal operations first.
- Separate payment authorization, invoicing, and entitlement state changes.
- Document the rollback and customer-impact plan for any billing mutation.

## References

- [Stripe Billing](https://docs.stripe.com/billing)
- [Stripe webhooks](https://docs.stripe.com/webhooks)
