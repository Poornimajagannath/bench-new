# Sandbox Rules

## Test Cards

- **Card Number:** `4111111111111111`
- **Expiry:** `12/2031`
- **CVV:** `123`
- **Billing:** 123 Test St, Seattle, WA 98101, USA

## Sandbox Behavior

- Sandbox simulates production but with test data only
- Never use production endpoints or credentials
- Sandbox is rate-limited — allow retries
- Sandbox returns predictable responses for testing

## What Sandbox Simulates

- Payment processing
- Authentication
- Error responses
- Transaction IDs

## What Sandbox Does NOT Simulate

- Production-level fraud detection
- Real card issuer responses
- Actual fund transfers
