# Corpus census

- When: `2026-08-08T02:34:52+00:00`
- Corpus: `data/products/payments/guides`
- Documents classified: **38**
- Eligible for ingestion: **29**
- Quarantined (policy): **9**

## Counts by kind

| Kind | Count | Share | Quarantined by policy? |
| --- | ---: | ---: | --- |
| API reference (`api_reference`) | 0 | 0.0% | no |
| How-to guide (`how_to_guide`) | 26 | 68.4% | no |
| Release note (`release_note`) | 0 | 0.0% | yes |
| Index / navigation (`index_navigation`) | 9 | 23.7% | yes |
| Legal (`legal`) | 0 | 0.0% | yes |
| Marketing (`marketing`) | 0 | 0.0% | no |
| Other / unclassified (`other`) | 3 | 7.9% | no |

## Policy (exclusions on paper)

Kinds excluded from ingestion by policy:

- `index_navigation` — Index / navigation
- `legal` — Legal
- `release_note` — Release note

_Rationale:_ Pre-ingestion policy: release notes, legal, and index/navigation pages are quarantined so they cannot silently enter the claim pipeline. How-to guides, API reference, and marketing remain eligible until a later policy amendment. Amend this file and re-run pipelines/run_corpus_census.py to change the decision record.

## Sample classifications (first 25)

| Path | Kind | Confidence | Reasons |
| --- | --- | --- | --- |
| `credentials.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_digital-accept-flex_developer_all_rest_digital-accept-flex.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_ctp-intro.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_da-payments.md.md` | how_to_guide | medium | constraint facts (TTL/PCI/header/reuse/encryption) — eligible regardless of length |
| `en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_flex-api-2.md.md` | how_to_guide | medium | constraint facts (TTL/PCI/header/reuse/encryption) — eligible regardless of length |
| `en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_microform-integ-v2.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_payments_intro_digt_accpt_sec_intg.md.md` | how_to_guide | medium | constraint facts (TTL/PCI/header/reuse/encryption) — eligible regardless of length |
| `en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_uc-intro.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_payer-authentication_developer_all_rest_payer-auth.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_payer-authentication_developer_all_rest_payer-auth_pa-reports-intro.md.md` | how_to_guide | medium | constraint facts (TTL/PCI/header/reuse/encryption) — eligible regardless of length |
| `en-us_payer-authentication_developer_all_rest_payer-auth_pa-testing-intro.md.md` | index_navigation | high | filename looks like intro/index and content is navigation-heavy |
| `en-us_payer-authentication_developer_all_rest_payer-auth_pa2-ccdc-intro.md.md` | index_navigation | medium | filename looks like intro/index and content is navigation-heavy |
| `en-us_payer-authentication_developer_all_rest_payer-auth_pa2-intro-intro.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_payments_developer_ctv_rest_payments.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_payments_developer_ctv_rest_payments_payments-debit-prepaid-process-intro.md.md` | index_navigation | high | filename looks like intro/index and content is navigation-heavy |
| `en-us_payments_developer_ctv_rest_payments_payments-intro.md.md` | index_navigation | medium | filename looks like intro/index and content is navigation-heavy |
| `en-us_payments_developer_ctv_rest_payments_payments-processing-basic-intro.md.md` | index_navigation | high | filename looks like intro/index and content is navigation-heavy |
| `en-us_tms_developer_all_rest_tms.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_tms_developer_all_rest_tms_tms-bin-lookup-service.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_tms_developer_all_rest_tms_tms-card-art.md.md` | other | low | no strong filename/content signal |
| `en-us_tms_developer_all_rest_tms_tms-create-request.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_tms_developer_all_rest_tms_tms-cust-tkn.md.md` | index_navigation | medium | tiny stub without procedural content |
| `en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-cust-pi-tkn.md.md` | index_navigation | medium | tiny stub without procedural content |
| `en-us_tms_developer_all_rest_tms_tms-cust-tkn_tms-ship-tkn.md.md` | other | low | no strong filename/content signal |
| `en-us_tms_developer_all_rest_tms_tms-ii-tkn.md.md` | other | low | no strong filename/content signal |
