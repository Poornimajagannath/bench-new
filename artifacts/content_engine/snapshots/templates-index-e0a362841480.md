# Relay — Payment Templates

## Purpose

These templates show correct CyberSource SDK integration patterns for different payment methods. Agents should reference these when generating integration code.

## Files

| Template | Description |
|----------|-------------|
| `card-payment/` | Standard major card brands card payments |
| `ach-payment/` | Bank account (ACH/EFT) payments |
| `digital-wallet/` | Google Pay, Apple Pay, PayPal |
| `multi-currency/` | Multi-currency handling with DCC |
| `config/` | Authentication and configuration templates |

## Common Gotchas

1. **Auth type must be `HTTP_Signature`** (capitalized), NOT `http_signature`
2. **SDK field names differ from docs**: `merchantKeyId`/`merchantsecretKey` vs `keyId`/`secretKey`
3. **`type` field is required** for card payments to avoid wrong card type processing
4. **`total_amount` and `currency` are required** in `amountDetails`
5. **`code` is required** in `clientReferenceInformation`
6. **Card expiry must be future year** (2031, not 2025)
7. **CyberSource sandbox is rate-limited** — implement retry logic
