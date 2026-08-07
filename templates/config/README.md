# Configuration Template

## Environment Variables

```bash
# Required
PGW_MERCHANT_ID=your_merchant_id_from_developer_portal
PGW_KEY_ID=your_http_signature_key_id
PGW_SHARED_SECRET=your_shared_secret
PGW_ENVIRONMENT=sandbox  # or "production"

# Optional
PGW_RUN_ID=run_identifier
PGW_SCENARIO=scenario_name
PGW_LANGUAGE=python  # or "node", "java", "typescript"
```

## Configuration Dictionary (Python SDK)

```python
configuration_dictionary = {
    "merchantid": os.environ["PGW_MERCHANT_ID"],
    "run_environment": "apitest.example.com",  # sandbox (Payment Gateway REST only)
    # "run_environment": "api.example.com",    # production
    "authentication_type": "HTTP_Signature",  # MUST be capitalized!
    "merchant_keyid": os.environ["PGW_KEY_ID"],
    "merchant_secretkey": os.environ["PGW_SHARED_SECRET"],
    "isSDK": True,  # Required by SDK
}
```

## Field Name Reference

### Docs vs SDK

| In Docs | In SDK | Correct? |
|---------|--------|----------|
| `keyId` | `merchant_keyid` | `merchant_keyid` ✅ |
| `secretKey` | `merchant_secretkey` | `merchant_secretkey` ✅ |
| `merchantId` | `merchantid` | `merchantid` ✅ |
| `runEnvironment` | `run_environment` | `run_environment` ✅ |
| `authType` | `authentication_type` | `authentication_type` ✅ |

### Auth Type Values

| Value | Use Case |
|-------|----------|
| `HTTP_Signature` | Production-ready, simpler setup |
| `jwt` | Requires P12 certificate, MLE support |

## Sandbox vs Production

| Property | Sandbox | Production |
|----------|---------|------------|
| `run_environment` | `apitest.example.com` | `api.example.com` |
| `authentication_type` | `HTTP_Signature` | `HTTP_Signature` or `jwt` |
| Test cards | `4111111111111111` | Real cards only |
| Response time | Fast (simulated) | Real processing time |

## SDK Installation

```bash
pip install payment-gateway-rest-client-python
```

## Version-Specific Gotchas

1. **SDK v0.0.77** — auth type must be `HTTP_Signature` (capitalized)
2. **SDK config validation** — `ast.literal_eval` crashes on JSON booleans (requires patch)
3. **SDK model names** — use `Ptsv2payments*` prefix, not `Payment*`
4. **SDK field casing** — snake_case in Python (e.g., `total_amount`, not `totalAmount`)

## Error Handling Template

```python
from Payment Gateway.rest import ApiException

try:
    api = PaymentsApi(client_config)
    return_data, status, body = api.create_payment(json.dumps(request_dict))
    print(f"Status: {status}")
    print(f"Response: {body}")
except ApiException as e:
    print(f"API Error {e.status}: {e.reason}")
    # Handle specific error codes
    if e.status == 400:
        # Invalid data — check request fields
        pass
    elif e.status == 401:
        # Auth failed — verify credentials
        pass
    elif e.status == 500:
        # Server error — implement retry
        pass
```

## Security Checklist

- [ ] Never hardcode credentials in source code
- [ ] Load all credentials from environment variables
- [ ] Never print secrets in logs (mask with `***`)
- [ ] Use sandbox for testing, production only when verified
- [ ] Rotate API keys regularly
- [ ] Use HTTPS for all API calls (Payment Gateway enforces this)
- [ ] Log all API calls for audit trail
- [ ] Implement rate limiting for sandbox testing
