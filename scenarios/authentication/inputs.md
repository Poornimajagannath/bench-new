# Authentication — Inputs

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
- **API version:** Latest (check developer portal for current version)

## Documentation Source

- **Portal:** `developer.cybersource.com`
- **LLMs.txt:** `developer.cybersource.com/llms.txt`
- **Auth docs path:** `/docs/authentication` (or similar — agent needs to find this)

## Expected Response Shape

A successful auth/API call returns:
```json
{
  "status": 200,
  "data": {
    // Some valid response from the CyberSource API
  }
}
```

## Gotchas (for reference, NOT shown to agent)

- SDK auth field names are `merchantKeyId` and `merchantsecretKey` — NOT `keyId` and `secretKey`
- Card expiry must be a future year (2031, not 2025)
- CyberSource sandbox is rate-limited (allow retries)
