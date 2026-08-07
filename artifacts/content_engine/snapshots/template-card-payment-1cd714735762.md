# Card Payment Integration Template

## SDK Models Used

- `CreatePaymentRequest` — Main payment request object
- `Ptsv2paymentsClientReferenceInformation` — Order reference
- `Ptsv2paymentsOrderInformation` — Order details
- `Ptsv2paymentsOrderInformationAmountDetails` — Amount and currency
- `Ptsv2paymentsOrderInformationBillTo` — Billing address
- `Ptsv2paymentsPaymentInformation` — Payment method
- `Ptsv2paymentsPaymentInformationCard` — Card details
- `Ptsv2paymentsProcessingInformation` — Processing options

## SDK Model Property Reference

### Ptsv2paymentsClientReferenceInformation
| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | string | Yes | Merchant-generated order reference |
| `transaction_id` | string | No | Custom transaction ID |
| `comments` | string | No | Brief order description |

### Ptsv2paymentsOrderInformationAmountDetails
| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total_amount` | string | Yes | Grand total (e.g., "10.00") |
| `currency` | string | Yes | ISO 3-character currency code (e.g., "USD") |
| `tax_amount` | string | No | Total tax amount |
| `freight_amount` | string | No | Shipping/handling charges |

### Ptsv2paymentsOrderInformationBillTo
| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `first_name` | string | No | Customer's first name |
| `last_name` | string | No | Customer's last name |
| `email` | string | No | Customer's email |
| `country` | string | Yes | ISO 2-character country code |
| `administrative_area` | string | No | State/province |
| `postal_code` | string | No | Postal code |

### Ptsv2paymentsPaymentInformationCard
| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `number` | string | Yes | Card number (PAN) |
| `expiration_month` | string | Yes | Two-digit month (MM) |
| `expiration_year` | string | Yes | Four-digit year (YYYY) |
| `type` | string | Yes | Three-digit card type code |
| `security_code` | string | No | CVV (optional for ecom) |

## Card Type Codes

| Type | Code |
|------|------|
| Card brand 001 | 001 |
| Mastercard | 002 |
| American Express | 003 |
| Discover | 004 |
| Diners Club | 005 |
| JCB | 007 |

## Error Recovery

| Error | Recovery |
|-------|----------|
| `INVALID_DATA` | Check card number format, expiry date, and required fields |
| `AUTH_FAILED` | Verify auth credentials and API key format |
| `CARD_DECLINED` | Prompt customer for different card or payment method |
| `NETWORK_ERROR` | Implement retry with exponential backoff |