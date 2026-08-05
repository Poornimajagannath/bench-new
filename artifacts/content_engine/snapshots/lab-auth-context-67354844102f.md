# Authentication Context

## Credential Loading

Load credentials from environment variables ONLY. Never hardcode or commit secrets.

## Required Environment Variables

- `CYBS_MERCHANT_ID` — Sandbox merchant ID from developer.cybersource.com
- `CYBS_KEY_ID` — HTTP Signature key ID
- `CYBS_SHARED_SECRET` — Shared secret paired with CYBS_KEY_ID
- `CYBS_ENVIRONMENT` — Must be "sandbox"

## Auth Error Taxonomy

| Error | Likely Cause | Fix |
|-------|-------------|-----|
| 401 Unauthorized | Wrong credentials | Verify CYBS_KEY_ID and CYBS_SHARED_SECRET |
| 403 Forbidden | Invalid merchant ID | Check CYBS_MERCHANT_ID |
| 400 Bad Request | Wrong field names | Use `merchantKeyId` and `merchantsecretKey` NOT `keyId` and `secretKey` |
| Network Error | Wrong endpoint | Use sandbox endpoint: `https://apitest.cybersource.com` |

## SDK Field Names (Known Gap)

The CyberSource SDK expects:
- `merchantKeyId` (NOT `keyId`)
- `merchantsecretKey` (NOT `secretKey`)

This is documented incorrectly in some places. Verify in the SDK source.
