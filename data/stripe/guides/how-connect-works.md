---
source_url: https://docs.stripe.com/connect/how-connect-works
title: How Connect works
---

# How Connect works

Connect lets a platform create and manage connected accounts. You use your **platform secret key** to create accounts and to make requests on behalf of those accounts.

## Before you begin

- Create a Stripe account and enable Connect in test mode.
- Prefer test-mode keys (`sk_test_...`) while building.

## Sequence

1. Create a connected account with `POST /v1/accounts`.
2. Create an Account Link with `POST /v1/account_links` so the connected account can finish onboarding.
3. After `details_submitted` is true, you can charge and pay out according to your Connect configuration.

## Gotchas

- Platform keys and connected-account context are different. Do not use a connected account's keys to create Account Links.
- Account Links expire. Always set `refresh_url` and `return_url`.
