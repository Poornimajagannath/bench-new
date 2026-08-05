# Digital Wallet Integration Template

## SDK Models Used

- `CreatePaymentRequest` — Main payment request object
- `Ptsv2paymentsClientReferenceInformation` — Order reference
- `Ptsv2paymentsOrderInformation` — Order details
- `Ptsv2paymentsOrderInformationAmountDetails` — Amount and currency
- `Ptsv2paymentsOrderInformationBillTo` — Billing address
- `Ptsv2paymentsPaymentInformation` — Payment method
- `Ptsv2paymentsPaymentInformationTokenizedCard` — Tokenized card (wallet)
- `Ptsv2paymentsPaymentInformationWallet` — Wallet payment (PayPal, etc.)

## SDK Model Property Reference

### Ptsv2paymentsPaymentInformationTokenizedCard
| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `number` | string | Yes | Tokenized card number (from wallet) |
| `expiration_month` | string | Yes | Two-digit month (MM) |
| `expiration_year` | string | Yes | Four-digit year (YYYY) |
| `type` | string | Yes | Three-digit card type code |
| `brand` | string | No | Wallet brand identifier |

### Ptsv2paymentsPaymentInformationWallet
| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `wallet_type` | string | Yes | GOOGLE_PAY, APPLE_PAY, PAYPAL, etc. |
| `token_id` | string | Yes | Token from wallet provider |
| `provider` | string | No | Wallet provider identifier |

## Wallet Types

| Wallet | Type Value | Required Fields |
|--------|-----------|-----------------|
| Google Pay | `GOOGLE_PAY` | token_id, brand |
| Apple Pay | `APPLE_PAY` | token_id, brand |
| PayPal | `PAYPAL` | payer_id, provider |
| Amazon Pay | `AMAZON_PAY` | token_id, provider |

## Wallet-Specific Gotchas

1. **Google Pay requires `brand` field** — set to `GOOGLE_PAY` or wallet brand
2. **Apple Pay requires token from Apple's SDK** — cannot be hardcoded
3. **PayPal requires PayPal SDK integration** — different flow than cards
4. **Digital wallet tokens expire** — must refresh periodically
5. **Some processors require additional 3D Secure** for wallet payments
6. **Wallet payments cannot be voided** — must use capture/refund instead
7. **Wallet transactions have different fee structures** — check with processor

## 3D Secure for Wallets

Wallet payments often trigger 3D Secure authentication. The flow:

1. User initiates payment in wallet app
2. Wallet app authenticates user (biometrics, PIN, etc.)
3. Wallet app sends token to merchant
4. Merchant includes token in CyberSource payment request
5. CyberSource processes transaction with token

### 3D Secure Model Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authentication_status` | string | No | Y, N, U, A, R, C, D |
| `eci` | string | No | Electronic Commerce Indicator |
| `avs_result` | string | No | AVS result code |

## Error Recovery

| Error | Recovery |
|-------|----------|
| `INVALID_DATA` | Check token format and expiry |
| `TOKEN_EXPIRED` | Prompt user to re-authenticate with wallet |
| `AUTH_FAILED` | Verify auth credentials |
| `NETWORK_ERROR` | Implement retry with exponential backoff |
| `3D_SECURE_REQUIRED` | Redirect user for authentication |

## Wallet-Specific Errors

| Error | Meaning | Fix |
|-------|---------|-----|
| `INVALID_TOKEN` | Token is malformed or expired | Prompt user to re-authenticate |
| `TOKEN_NOT_FOUND` | Token not found on CyberSource side | Use fresh token from wallet provider |
| `3D_SECURE_FAILED` | Authentication failed | Redirect user to retry authentication |
| `WALLET_NOT_SUPPORTED` | Processor doesn't support this wallet | Fall back to card payment |
| `INSUFFICIENT_FUNDS` | Wallet balance insufficient | Prompt user for different payment method |

## Implementation Checklist

- [ ] Integrate wallet provider SDK (Google, Apple, PayPal, etc.)
- [ ] Configure wallet payment buttons in UI
- [ ] Handle token refresh flow
- [ ] Implement 3D Secure fallback
- [ ] Add error handling for expired tokens
- [ ] Test with wallet test cards
- [ ] Verify fee structure with processor
