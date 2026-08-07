---
title: Stripe Connect onboarding quickstart
generated: true
product: stripe-connect
---

# Stripe Connect onboarding quickstart

Backend track: create a connected account and an Account Link using your platform test secret key.
Facts below trace to the local Connect OpenAPI fixture and Connect prose guides.

## 1. Prepare platform test credentials

**Goal:** Authenticate as the Connect platform in test mode.

**Prerequisites**
- Stripe account with Connect enabled in test mode
- Environment variable STRIPE_TEST_SECRET_KEY=sk_test_...

**Actions**
1. Confirm the key prefix is sk_test_ (never sk_live_ for this proof).
2. Send Authorization: Bearer $STRIPE_TEST_SECRET_KEY on platform calls.

**Expected outcome:** API requests authenticate without 401.

**Common errors**
- 401 when using a publishable key or missing Bearer header

## 2. Create a connected account

**Goal:** Obtain an acct_... id for onboarding.

**Prerequisites**
- Platform test secret key

**Actions**
1. POST /v1/accounts with type (e.g. express) and country.
2. Request capabilities such as card_payments and transfers when required by your integration.
3. Store the returned account id.

**Expected outcome:** Response includes id starting with acct_.

**Common errors**
- 400 when type or country is missing
- 401 when the platform key is invalid

## 3. Create an Account Link

**Goal:** Send the connected account through Stripe-hosted onboarding.

**Prerequisites**
- Connected account id from step 2
- HTTPS return_url and refresh_url you control

**Actions**
1. POST /v1/account_links with account, type=account_onboarding, return_url, refresh_url.
2. Redirect the user to the url field in the response.
3. If the link expires, create a new Account Link for the same account.

**Expected outcome:** Response includes a single-use url and expires_at.

**Common errors**
- 400 when return_url/refresh_url/type are missing
- 401 when not using the platform secret key

## 4. Verify onboarding state

**Goal:** Confirm the connected account submitted details.

**Prerequisites**
- Account id

**Actions**
1. GET /v1/accounts/{account}.
2. Check details_submitted (and charges_enabled when relevant).

**Expected outcome:** Account object reflects onboarding progress.

**Common errors**
- 404 if the account id is wrong

<!-- section: generated -->
