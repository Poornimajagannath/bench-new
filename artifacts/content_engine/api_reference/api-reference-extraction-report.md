# API-reference extraction report

Denominator: product roots in `raw/product-roots/`.

## Before / after endpoint_fact counts

| Product | Before (thin verb+URL) | After (all endpoint_fact) | Of which api_reference |
|---|---:|---:|---:|
| boarding | 9 | 42 | 42 |
| click-to-pay | 21 | 34 | 34 |
| cp-retail | 10 | 90 | 90 |
| digital-accept-flex | 31 | 53 | 51 |
| echeck-user-guide | 4 | 4 | 0 |
| invoicing | 18 | 30 | 27 |
| mass-transit | 22 | 66 | 66 |
| paybylink | 11 | 11 | 0 |
| payments | 14 | 76 | 76 |
| payouts-dev | 4 | 16 | 16 |
| recurring-billing-dev | 34 | 34 | 0 |
| security-keys | 0 | 0 | 0 |
| tap-to-phone | 2 | 2 | 0 |
| tms | 208 | 577 | 525 |
| unified-checkout | 23 | 25 | 25 |
| webhooks | 27 | 27 | 0 |
| **Total** | **438** | **1087** | **952** |

## Pattern match vs skip

- Endpoint headings seen: 176
- Matched (verb+URL line present): 176
- Matched with Required Fields: 119
- Matched with REST Example: 159
- Claims emitted from pattern: 952
- Hard skips (no claims): 0

### Soft gaps (matched, claim emitted, enrichment missing)

- `matched_without_required_fields`: 57
- `matched_without_rest_example`: 17

