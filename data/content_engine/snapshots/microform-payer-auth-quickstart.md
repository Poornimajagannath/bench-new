# Microform + Payer Authentication Quickstart

Audience: developer
Product: CyberSource / Visa Acceptance
Freshness: 2026-08-04

Goal: Sequence Microform tokenization with Payer Authentication enrollment, challenge or frictionless handling, validation, and authorization.

## Overview

Microform tokenization captures card data in the browser. It is **not** itself a completed Payer Authentication / 3DS step. After tokenize, you still need enrollment and either challenge or frictionless handling before authorization.

## Prerequisites

- Sandbox merchant credentials available as environment variables (never hardcode)
- Microform client integrated on the checkout page
- Payer Authentication enabled for the sandbox MID

## Steps

### 1. Tokenize with Microform

Capture the payment fields with Microform and obtain a transient token.

Requires: microform_client
Outcome: transient_token_available
Evidence: "Microform tokenization captures card data in the browser."

### 2. Run Payer Auth setup

Create the Payer Authentication setup request using the tokenized payment data.

Requires: transient_token_available
Outcome: payer_auth_setup_complete
Evidence: "After tokenize, you still need enrollment"

### 3. Check enrollment

Call enrollment check. Expect FRICTIONLESS, CHALLENGE, or UNAVAILABLE.

Requires: payer_auth_setup_complete
Outcome: enrollment_path_known
Failure modes: skipping enrollment and authorizing immediately
Evidence: "Expect FRICTIONLESS, CHALLENGE, or UNAVAILABLE"

### 4. Handle challenge or frictionless

Branch on the enrollment path. Do not collapse both into one success branch.

Requires: enrollment_path_known
Outcome: authentication_result_ready
Evidence: "Branch on the enrollment path"

### 5. Validate authentication

Validate the authentication result before payment.

Requires: authentication_result_ready
Outcome: auth_refs_ready
Evidence: "Validate the authentication result before payment"

### 6. Authorize with authentication references

Submit authorization including authentication transaction references when 3DS was performed.

Requires: auth_refs_ready
Outcome: authorization_submitted
Failure modes: authorizing with only the Flex/Microform token and no auth refs
Evidence: "including authentication transaction references when 3DS was performed"

## Validation checks

- Confirm enrollment ran before authorization
- Confirm challenge and frictionless paths are both handled
- Confirm authorization carries authentication references when required

## Warnings

- Do not treat Microform tokenize as completed 3DS
- Do not log raw PAN, shared secrets, or credential material

## Next steps

- Add support-safe evidence collection for failed enrollments
- Wire a VAP CLI workflow verifier for this contract
