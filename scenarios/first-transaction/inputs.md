# First Transaction — Inputs

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
- **Billing name:** Test User

## Sandbox Endpoint

- **URL:** `https://apitest.cybersource.com`
- **API version:** Latest (check developer portal)
- **Payment endpoint:** `/pts/v2/payments` (or similar — agent needs to find this)

## Documentation Source

- **Portal:** `developer.cybersource.com`
- **LLMs.txt:** `developer.cybersource.com/llms.txt`
- **Payment docs path:** `/docs/payments` or `/docs/api-reference` (agent needs to find this)

## Expected Request Shape

A payment auth request should look like:
```json
{
  "clientReferenceInformation": {
    "code": "TCR123456789"
  },
  "orderInformation": {
    "amountInformation": {
      "amount": "10.00",
      "currency": "USD"
    },
    "billTo": {
      "firstName": "Test",
      "lastName": "User",
      "address1": "123 Test St",
      "address2": "Apt 1",
      "locality": "Seattle",
      "region": "WA",
      "postalCode": "98101",
      "country": "US",
      "email": "test@example.com"
    }
  },
  "processingInformation": {
    "commerceIndicator": "internet"
  },
  "paymentInformation": {
    "card": {
      "number": "4111111111111111",
      "expirationMonth": "12",
      "expirationYear": "2031",
      "cvv": "123"
    }
  }
}
```

## Gotchas (for reference, NOT shown to agent)

- `billTo` is required but documented nowhere in the CyberSource docs — this is a known gap
- Locality, lastName, email, address1, country are required fields
- Card expiry must be a future year (2031, not 2025)
- Payment endpoint path may vary by API version
