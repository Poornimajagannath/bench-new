---
source_url: https://docs.stripe.com/connect/authentication
title: Connect authentication
---

# Connect authentication

Authenticate platform API calls with your platform secret key as a Bearer token.

## Prerequisites

- Platform secret key from the Stripe Dashboard (test mode: `sk_test_...`).
- Never commit secret keys. Load them from environment variables.

## Common errors

- **401 Unauthorized** — missing `Authorization: Bearer sk_test_...` header or using a publishable key by mistake.
- Using a live key against flows you intended for test mode (or the reverse).

## Recommended pattern

1. Store `STRIPE_TEST_SECRET_KEY` in the environment.
2. Send `Authorization: Bearer $STRIPE_TEST_SECRET_KEY` on every platform request.
3. For requests on behalf of a connected account, also send `Stripe-Account: acct_...` when the API requires it.
