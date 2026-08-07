# Agent Readiness Testing — Inputs

## Environment Variables

| Variable | Value | Source |
|----------|-------|--------|
| `CYBS_MERCHANT_ID` | `YOUR_MERCHANT_ID` | CyberSource developer portal |
| `CYBS_KEY_ID` | `YOUR_KEY_ID` | CyberSource developer portal |
| `CYBS_SHARED_SECRET` | `YOUR_SHARED_SECRET` | CyberSource developer portal |
| `CYBS_ENVIRONMENT` | `sandbox` | Must be sandbox for testing |

## Test Cards (Multiple Payment Methods)

### Card Payments
| Field | Value |
|-------|-------|
| Card Number | `4111111111111111` |
| Expiry | `12/2031` |
| CVV | `123` |
| Type | `001` |

### Bank Transfers (ACH)
| Field | Value |
|-------|-------|
| Routing Number | `123456789` |
| Account Number | `1234567890` |
| Account Type | `CHECKING` |

## Currency Test Set

| Currency | Code | Example Amount |
|----------|------|----------------|
| US Dollar | `USD` | `10.00` |
| Euro | `EUR` | `10.00` |
| British Pound | `GBP` | `10.00` |
| Canadian Dollar | `CAD` | `10.00` |
| Japanese Yen | `JPY` | `1000` |

## Sandbox Endpoint

| Property | Value |
|----------|-------|
| URL | `https://apitest.cybersource.com` |
| API Version | v2 (PTS) |
| Auth Type | `HTTP_Signature` |

## Required SDK Model Properties

### Payment Request (pts/v2/payments POST)

**ClientReferenceInformation:**
- `code` (string, required) — Merchant-generated order reference

**OrderInformation.AmountDetails:**
- `total_amount` (string, required) — Grand total amount
- `currency` (string, required) — ISO 3-character currency code

**OrderInformation.BillTo:**
- `first_name` (string) — Customer's first name
- `last_name` (string) — Customer's last name
- `email` (string) — Customer's email
- `country` (string, required) — ISO 2-character country code
- `administrative_area` (string) — State/province

**PaymentInformation.Card:**
- `number` (string, required) — Card number (PAN)
- `expiration_month` (string, required) — Two-digit month (MM)
- `expiration_year` (string, required) — Four-digit year (YYYY)
- `type` (string, required) — Three-digit card type code

## Test Scenarios

### Scenario 1: Basic Auth
- Use test credentials
- Test SDK installation
- Test auth field name resolution

### Scenario 2: Card Payment
- Use Relay test card
- Test card model structure
- Test currency handling

### Scenario 3: Multi-Currency
- Test USD, EUR, GBP, CAD, JPY
- Test locale handling
- Test tax configuration

### Scenario 4: Error Handling
- Test invalid card numbers
- Test expired cards
- Test missing required fields
- Test wrong currency codes

## Gotchas (NOT shown to agent)

- SDK auth type must be `HTTP_Signature` (capitalized), not `http_signature`
- SDK field names differ from docs: `merchantKeyId`/`merchantsecretKey` vs `keyId`/`secretKey`
- Card expiry must be future year (2031, not 2025)
- CyberSource sandbox is rate-limited
- `type` field is required for card payments
- `total_amount` and `currency` are required in `amountDetails`
- `code` is required in `clientReferenceInformation`
