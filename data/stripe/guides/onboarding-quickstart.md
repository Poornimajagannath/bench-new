---
source_url: https://docs.stripe.com/connect/onboarding/quickstart
title: Connect onboarding quickstart
---

# Connect onboarding quickstart

Goal: create a connected account and send the user through hosted onboarding via an Account Link.

## Prerequisites

- Connect enabled on your platform in test mode.
- Platform test secret key.
- Public `return_url` and `refresh_url` you control.

## Steps

1. Create an Express (or chosen type) account with country and requested capabilities.
2. Create an Account Link of type `account_onboarding` for that account id.
3. Redirect the user to the Account Link `url`.
4. When they return, retrieve the account and check `details_submitted`.

## Expected outcome

You have an `acct_...` id and the connected account completed (or started) onboarding through Stripe-hosted flow.

## Common errors

- Missing `type`, `refresh_url`, or `return_url` on Account Links → 400.
- Creating Account Links with a non-platform key → 401.
