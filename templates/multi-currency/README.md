# Multi-Currency Integration Template

## SDK Models Used

- `CreatePaymentRequest` — Main payment request object
- `Ptsv2paymentsClientReferenceInformation` — Order reference
- `Ptsv2paymentsOrderInformation` — Order details
- `Ptsv2paymentsOrderInformationAmountDetails` — Amount and currency
- `Ptsv2paymentsOrderInformationAmountDetailsCurrencyConversion` — DCC conversion
- `Ptsv2paymentsProcessingInformation` — Processing options

## SDK Model Property Reference

### Ptsv2paymentsOrderInformationAmountDetails (Multi-Currency)
| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `total_amount` | string | Yes | Grand total in merchant currency |
| `currency` | string | Yes | ISO 3-character currency code |
| `original_amount` | string | No | Original amount before conversion |
| `original_currency` | string | No | Original currency code |
| `exchange_rate` | string | No | Exchange rate (4 decimal places) |
| `exchange_rate_time_stamp` | string | No | Format: YYYYMMDD HH:MM |
| `foreign_amount` | string | No | Converted foreign amount |
| `foreign_currency` | string | No | Foreign currency code |

### Ptsv2paymentsOrderInformationAmountDetailsCurrencyConversion
| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `exchange_rate` | string | No | DCC exchange rate |
| `converted_amount` | string | No | Amount after conversion |
| `converted_currency` | string | No | Currency after conversion |
| `provider` | string | No | DCC provider name |

## Currency Codes (ISO 4217)

| Currency | Code | Example Amount | Locale |
|----------|------|----------------|--------|
| US Dollar | USD | 10.00 | en-US |
| Euro | EUR | 10,00 | de-DE |
| British Pound | GBP | 10.00 | en-GB |
| Canadian Dollar | CAD | 10.00 | en-CA |
| Japanese Yen | JPY | 1000 | ja-JP |
| Chinese Yuan | CNY | 10.00 | zh-CN |
| Australian Dollar | AUD | 10.00 | en-AU |
| Swiss Franc | CHF | 10.00 | de-CH |

## DCC (Dynamic Currency Conversion)

### When to Use DCC
- International customers want to pay in their home currency
- Merchant wants to avoid FX risk
- Customer explicitly requests conversion

### DCC Flow
1. Customer selects currency on checkout
2. DCC provider returns exchange rate
3. Merchant includes rate and converted amount in payment request
4. CyberSource processes with DCC flags
5. Response includes DCC details for receipt

### DCC Required Fields
- `amountDetails.originalAmount` — original amount
- `amountDetails.originalCurrency` — original currency
- `amountDetails.foreignAmount` — converted amount
- `amountDetails.foreignCurrency` — converted currency
- `amountDetails.exchangeRate` — exchange rate
- `amountDetails.exchangeRateTimeStamp` — rate timestamp

## Multi-Currency Gotchas

1. **All amounts must be strings** — never use floats (floating point precision issues)
2. **Currency codes are 3 characters** — ISO 4217 standard (USD, EUR, GBP, etc.)
3. **Decimal places vary by currency** — JPY has 0, USD has 2, KRW has 0
4. **Exchange rates must be from certified DCC providers** — not random rates
5. **DCC rates expire** — typically within minutes of request
6. **Some processors don't support all currencies** — check with your provider
7. **Tax/jurisdiction config must match merchant's legal entity** — not customer's location
8. **Multi-currency transactions require additional risk checks** — higher fraud rates

## Exchange Rate Handling

### Best Practices
```python
# CORRECT: Use strings with fixed precision
amount = "10.00"  # USD
rate = "1.1500"   # 4 decimal places
timestamp = "20260721 14:30"  # YYYYMMDD HH:MM format

# WRONG: Using floats
amount = 10.00  # floating point precision issues
rate = 1.15  # insufficient precision
```

### Exchange Rate Source
- Use DCC provider rates — not Google/XE rates
- DCC providers are certified under PCI standards
- Store rate timestamps for audit compliance

## Error Recovery

| Error | Recovery |
|-------|----------|
| `INVALID_DATA` | Check currency code format (must be 3 chars) |
| `INVALID_CURRENCY` | Check if processor supports requested currency |
| `RATE_EXPIRED` | Re-fetch exchange rate from DCC provider |
| `DCC_NOT_SUPPORTED` | Fall back to merchant currency |
| `NETWORK_ERROR` | Implement retry with exponential backoff |

## Multi-Currency Checklist

- [ ] Integrate DCC provider API
- [ ] Configure supported currencies
- [ ] Set up exchange rate caching
- [ ] Implement rate expiration handling
- [ ] Add currency conversion display in UI
- [ ] Configure tax/jurisdiction rules per currency
- [ ] Test with multiple currencies
- [ ] Verify PCI compliance for DCC flow
- [ ] Set up audit logging for rate changes
- [ ] Configure fallback to merchant currency
