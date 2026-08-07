---
source_url: https://docs.stripe.com/api/account_links
title: Account Links
---

# Account Links

Account Links are single-use URLs for Stripe-hosted onboarding or account updates.

## Required parameters

- `account` — connected account id
- `type` — `account_onboarding` or `account_update`
- `refresh_url` — where to send the user if the link expires
- `return_url` — where to send the user after they finish

## Sequencing advice

Create the Account **before** the Account Link. Do not invent account ids.

## Gotcha

Links expire quickly. If the user returns after expiry, create a new Account Link with the same account id and send them to `refresh_url` handling.
