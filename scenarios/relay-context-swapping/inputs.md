# Relay — Context-Swapping Inputs

## Environment Variables

| Variable | Value | Source |
|----------|-------|--------|
| `CYBS_MERCHANT_ID` | `YOUR_MERCHANT_ID` | CyberSource developer portal |
| `CYBS_KEY_ID` | `YOUR_KEY_ID` | CyberSource developer portal |
| `CYBS_SHARED_SECRET` | `YOUR_SHARED_SECRET` | CyberSource developer portal |
| `CYBS_ENVIRONMENT` | `sandbox` | Must be sandbox for testing |

## Test Cards

### Relay
| Field | Value |
|-------|-------|
| Card Number | `4111111111111111` |
| Expiry | `12/2031` |
| CVV | `123` |
| Type | `001` |

### Mastercard
| Field | Value |
|-------|-------|
| Card Number | `5555555555554444` |
| Expiry | `12/2031` |
| CVV | `123` |
| Type | `002` |

### American Express
| Field | Value |
|-------|-------|
| Card Number | `378282246310005` |
| Expiry | `12/2031` |
| CVV | `1234` |
| Type | `003` |

### Discover
| Field | Value |
|-------|-------|
| Card Number | `6011111111111117` |
| Expiry | `12/2031` |
| CVV | `123` |
| Type | `004` |

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

## Payment Method Configurations

### Card Payments (Standard)
```json
{
  "paymentInformation": {
    "card": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "type": "001"
    }
  }
}
```

### Bank Transfers (ACH)
- Requires `paymentInformation.bank` object
- Must include bank routing number and account number
- Different model structure than card payments

### Digital Wallets (Google Pay)
- Uses `paymentInformation.tokenizedCard` instead of `card`
- Requires token from wallet provider
- Additional authentication flow required

## Currency Codes (ISO 4217)

| Currency | Code | Example |
|----------|------|---------|
| US Dollar | `USD` | `10.00` |
| Euro | `EUR` | `10.00` |
| British Pound | `GBP` | `10.00` |
| Canadian Dollar | `CAD` | `10.00` |
| Japanese Yen | `JPY` | `1000` |

## Gotchas (NOT shown to agent)

- SDK auth type must be `HTTP_Signature` (capitalized), not `http_signature`
- SDK field names differ from docs: `merchantKeyId`/`merchantsecretKey` vs `keyId`/`secretKey`
- Card expiry must be future year (2031, not 2025)
- CyberSource sandbox is rate-limited
- `type` field is required for card payments to avoid wrong card type processing
- `total_amount` and `currency` are required in `amountDetails`
- `code` is required in `clientReferenceInformation`
