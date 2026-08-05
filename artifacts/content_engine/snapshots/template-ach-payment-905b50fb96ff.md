# ACH Payment Integration Template

## SDK Models Used

- `CreatePaymentRequest` — Main payment request object
- `Ptsv2paymentsClientReferenceInformation` — Order reference
- `Ptsv2paymentsOrderInformation` — Order details
- `Ptsv2paymentsOrderInformationAmountDetails` — Amount and currency
- `Ptsv2paymentsOrderInformationBillTo` — Billing address
- `Ptsv2paymentsPaymentInformation` — Payment method
- `Ptsv2paymentsPaymentInformationBank` — Bank account details
- `Ptsv2paymentsPaymentInformationBankAccount` — Bank account structure

## SDK Model Property Reference

### Ptsv2paymentsPaymentInformationBank
| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `account_type` | string | Yes | CHECKING or SAVINGS |
| `account_number` | string | Yes | Bank account number |
| `routing_number` | string | Yes | 9-digit routing number |
| `bank_name` | string | No | Bank name |
| `account_holder_name` | string | No | Name on the account |
| `account_holder_type` | string | No | PERSON or BUSINESS |

### Ptsv2paymentsPaymentInformationBankAccount
| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `account_type` | string | Yes | CHECKING, SAVINGS, or LOAN |
| `account_number` | string | Yes | Bank account number |
| `routing_number` | string | Yes | 9-digit ABA routing number |
| `name_on_account` | string | No | Name on the account |
| `account_holder_type` | string | No | PERSON or BUSINESS |

## Bank Transfers by Region

### US (ACH)
| Field | Format |
|-------|--------|
| Routing Number | 9 digits (0-9) |
| Account Number | 8-17 digits (0-9) |
| Account Type | CHECKING or SAVINGS |

### EU (SEPA)
| Field | Format |
|-------|--------|
| IBAN | 15-34 alphanumeric characters |
| BIC/SWIFT | 8 or 11 characters |
| Account Number | Varies by country |

### UK (BACS)
| Field | Format |
|-------|--------|
| Sort Code | 6 digits (XX-XX-XX) |
| Account Number | 8 digits (0-9) |

## Required Fields for ACH

- `paymentInformation.bank.accountType` — must be `CHECKING` or `SAVINGS`
- `paymentInformation.bank.accountNumber` — bank account number
- `paymentInformation.bank.routingNumber` — 9-digit routing number
- `orderInformation.billTo.firstName` — customer first name
- `orderInformation.billTo.lastName` — customer last name
- `orderInformation.amountDetails.totalAmount` — order total
- `orderInformation.amountDetails.currency` — ISO 3-character currency code
- `clientReferenceInformation.code` — merchant reference

## Error Recovery

| Error | Recovery |
|-------|----------|
| `INVALID_DATA` | Check routing number format (must be 9 digits), account number length |
| `AUTH_FAILED` | Verify auth credentials |
| `ACCOUNT_CLOSED` | Prompt customer for different account |
| `INSUFFICIENT_FUNDS` | Prompt customer for different account |
| `NETWORK_ERROR` | Implement retry with exponential backoff |

## ACH-Specific Gotchas

1. **Routing numbers must be 9 digits** — not 8, not 10, exactly 9
2. **Account numbers are 8-17 digits** for most processors
3. **ACH takes 3-5 business days** to settle — unlike cards which are instant
4. **SEPA requires IBAN format** — not just account number
5. **BACS requires sort code** — 6 digits in XX-XX-XX format
6. **Name on account must match** the billing address name
7. **ACH cannot be reversed instantly** — requires separate reversal flow
