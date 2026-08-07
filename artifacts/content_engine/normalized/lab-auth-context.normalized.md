# Authentication Context

## Credential Loading

Load credentials from environment variables ONLY. Never hardcode or commit secrets.

## Required Environment Variables

- `PGW_MERCHANT_ID` — Sandbox merchant ID from developer.example.com
- `PGW_KEY_ID` — HTTP Signature key ID
- `PGW_SHARED_SECRET` — Shared secret paired with PGW_KEY_ID
- `PGW_ENVIRONMENT` — Must be "sandbox"

## Auth Error Taxonomy

| Error | Likely Cause | Fix |
|-------|-------------|-----|
| 401 Unauthorized | Wrong credentials | Verify PGW_KEY_ID and PGW_SHARED_SECRET |
| 403 Forbidden | Invalid merchant ID | Check PGW_MERCHANT_ID |
| 400 Bad Request | Wrong field names | Use `merchantKeyId` and `merchantsecretKey` NOT `keyId` and `secretKey` |
| Network Error | Wrong endpoint | Use sandbox endpoint: `https://apitest.example.com` |

## SDK Field Names (Known Gap)

The Payment Gateway SDK expects:
- `merchantKeyId` (NOT `keyId`)
- `merchantsecretKey` (NOT `secretKey`)

This is documented incorrectly in some places. Verify in the SDK source.
