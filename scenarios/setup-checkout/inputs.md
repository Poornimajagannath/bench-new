# Setup Checkout — Inputs

## Environment Variables

| Variable | Value | Source |
|----------|-------|--------|
| `CYBS_MERCHANT_ID` | `YOUR_MERCHANT_ID` | CyberSource developer portal |
| `CYBS_KEY_ID` | `YOUR_KEY_ID` | CyberSource developer portal |
| `CYBS_SHARED_SECRET` | `YOUR_SHARED_SECRET` | CyberSource developer portal |

## Test Card

- **Card number:** `4111111111111111`
- **Expiry:** `12/2031`
- **CVV:** `123`
- **Billing address:** 123 Test St, Seattle, WA 98101, USA

## Sandbox Endpoint

- **URL:** `https://apitest.cybersource.com`
- **API version:** Latest (check developer portal)

## Documentation Source

- **Portal:** `developer.cybersource.com`
- **LLMs.txt:** `developer.cybersource.com/llms.txt`
- **Checkout docs path:** `/docs/checkout` (or similar — agent needs to find this)

## Checkout Options

The agent may choose either:
- **Unified Checkout** — hosted checkout form
- **Flex Microcheckout** — lightweight checkout button

Both should return a transaction ID on success.

## Expected Response Shape

A successful checkout transaction returns:
```json
{
  "status": 200,
  "data": {
    "id": "TXN_1234567890",
    "status": "CAPTURED",
    // ... other fields
  }
}
```

## Gotchas (for reference, NOT shown to agent)

- Checkout config requires the test card number, expiry, CVV
- Checkout URL must point to sandbox
- Some checkout configs require additional merchant parameters
