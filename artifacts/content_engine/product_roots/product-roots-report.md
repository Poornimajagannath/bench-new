# Product-root corpus report

Generated: 2026-08-08T03:06:34+00:00

Denominator source: `product_root`

Coverage denominator is the product root mega-guide fetched verbatim from the vendor site. The family HTML TOC is a cross-check only: report TOC pages whose content does not appear in the root.

## Derivation probe

docs.md links point at intro subtopics. Root = guide directory as `.md` at its parent (family name repeated when guide folder == family).

| Product | Derivation | Root | HTTP | Bytes | Resolves |
|---|---|---|---:|---:|---|
| Accept Payments | family_repeat | `/docs/cybs/en-us/payments/developer/ctv/rest/payments.md` | 200 | 397466 | yes |
| Authentication | family_repeat | `/docs/cybs/en-us/security-keys/user/all/ada/security-keys.md` | 200 | 101843 | yes |
| Pay by Link | family_repeat | `/docs/cybs/en-us/paybylink/developer/all/rest/paybylink.md` | 200 | 52427 | yes |
| Token Management | family_repeat | `/docs/cybs/en-us/tms/developer/all/rest/tms.md` | 200 | 776173 | yes |
| eCheck | guide_dir | `/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide.md` | 200 | 124021 | yes |
| ACH | not_md | `—` | — | 0 | no |
| Recurring Billing | guide_dir | `/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev.md` | 200 | 103589 | yes |
| Invoicing | family_repeat | `/docs/cybs/en-us/invoicing/developer/all/rest/invoicing.md` | 200 | 242256 | yes |
| Payouts | guide_dir | `/docs/cybs/en-us/payouts/developer/ctv/rest/payouts-dev.md` | 200 | 219718 | yes |
| Webhooks | family_repeat | `/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks.md` | 200 | 146916 | yes |
| Click to Pay | family_repeat | `/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.md` | 200 | 499260 | yes |
| Microform | family_repeat | `/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.md` | 200 | 989174 | yes |
| Unified Checkout | family_repeat | `/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.md` | 200 | 509657 | yes |
| Retail | family_repeat | `/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail.md` | 200 | 387909 | yes |
| Transit | guide_dir | `/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit.md` | 200 | 401764 | yes |
| Tap to Pay | family_repeat | `/docs/cybs/en-us/tap-to-phone/integration/all/rest/tap-to-phone.md` | 200 | 134915 | yes |
| Boarding REST | family_repeat | `/docs/cybs/en-us/boarding/developer/all/rest/boarding.md` | 200 | 268904 | yes |

Unresolved: **1** / 17
- ACH: intro `/content/dam/new-documentation/documentation/en/e-checks/developer/all/so/e-checks-so.pdf` (family_repeat=`None`, guide_dir=`None`, how=not_md)

## Per product

| Product | Root fetched | Bytes | Sections | Code fences | TOC topics | TOC covered | TOC gaps |
|---|---|---:|---:|---:|---:|---:|---:|
| Accept Payments | `/docs/cybs/en-us/payments/developer/ctv/rest/payments.md` | 397466 | 266 | 82 | 82 | 82 | 0 |
| Authentication | `/docs/cybs/en-us/security-keys/user/all/ada/security-keys.md` | 101843 | 49 | 5 | 39 | 39 | 0 |
| Pay by Link | `/docs/cybs/en-us/paybylink/developer/all/rest/paybylink.md` | 52427 | 37 | 16 | 14 | 14 | 0 |
| Token Management | `/docs/cybs/en-us/tms/developer/all/rest/tms.md` | 776173 | 538 | 271 | 216 | 216 | 0 |
| eCheck | `/docs/cybs/en-us/echeck/user/all/rest/echeck-user-guide.md` | 124021 | 77 | 10 | 53 | 53 | 0 |
| ACH | `—` | 0 | 0 | 0 | 0 | 0 | 0 |
| Recurring Billing | `/docs/cybs/en-us/recurring-billing/developer/all/rest/recurring-billing-dev.md` | 103589 | 80 | 53 | 49 | 49 | 0 |
| Invoicing | `/docs/cybs/en-us/invoicing/developer/all/rest/invoicing.md` | 242256 | 95 | 44 | 40 | 40 | 0 |
| Payouts | `/docs/cybs/en-us/payouts/developer/ctv/rest/payouts-dev.md` | 219718 | 59 | 18 | 46 | 46 | 0 |
| Webhooks | `/docs/cybs/en-us/webhooks/implementation/all/rest/webhooks.md` | 146916 | 124 | 36 | 44 | 44 | 0 |
| Click to Pay | `/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.md` | 499260 | 298 | 83 | 137 | 135 | 2 |
| Microform | `/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.md` | 989174 | 503 | 246 | 274 | 274 | 0 |
| Unified Checkout | `/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.md` | 509657 | 220 | 72 | 146 | 146 | 0 |
| Retail | `/docs/cybs/en-us/cp-retail/integration/ctv/rest/cp-retail.md` | 387909 | 226 | 109 | 75 | 75 | 0 |
| Transit | `/docs/cybs/en-us/urban-mobility/developer/ctv/rest/mass-transit.md` | 401764 | 171 | 76 | 66 | 66 | 0 |
| Tap to Pay | `/docs/cybs/en-us/tap-to-phone/integration/all/rest/tap-to-phone.md` | 134915 | 170 | 4 | 33 | 33 | 0 |
| Boarding REST | `/docs/cybs/en-us/boarding/developer/all/rest/boarding.md` | 268904 | 137 | 57 | 109 | 109 | 0 |

## TOC pages not covered by root (real gaps)

### Click to Pay (`click-to-pay`)

- `/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-uc-integration-methods-intro`
- `/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay/ctp-uc-integration-methods-intro/uc-integration-methods-components`

## Totals

- Products listed: 17
- Roots resolved: 16
- Roots fetched: 16
- Bytes: 5355992
- Sections split: 3050
- TOC topics checked: 1423 (covered 1421, gaps 2)
