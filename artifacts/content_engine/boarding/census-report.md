# Corpus census

- When: `2026-08-07T22:56:28+00:00`
- Corpus: `data/products/boarding/guides`
- Documents classified: **236**
- Eligible for ingestion: **190**
- Quarantined (policy): **46**

## Counts by kind

| Kind | Count | Share | Quarantined by policy? |
| --- | ---: | ---: | --- |
| API reference (`api_reference`) | 6 | 2.5% | no |
| How-to guide (`how_to_guide`) | 93 | 39.4% | no |
| Release note (`release_note`) | 0 | 0.0% | yes |
| Index / navigation (`index_navigation`) | 46 | 19.5% | yes |
| Legal (`legal`) | 0 | 0.0% | yes |
| Marketing (`marketing`) | 0 | 0.0% | no |
| Other / unclassified (`other`) | 91 | 38.6% | no |

## Policy (exclusions on paper)

Kinds excluded from ingestion by policy:

- `index_navigation` — Index / navigation
- `legal` — Legal
- `release_note` — Release note

_Rationale:_ Pre-ingestion policy: release notes, legal, and index/navigation pages are quarantined so they cannot silently enter the claim pipeline. How-to guides, API reference, and marketing remain eligible until a later policy amendment. Amend this file and re-run pipelines/run_corpus_census.py to change the decision record.

## Sample classifications (first 25)

| Path | Kind | Confidence | Reasons |
| --- | --- | --- | --- |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt.md.md` | api_reference | medium | heading/body indicates field reference |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-about-guide.md.md` | index_navigation | medium | filename looks like intro/index and content is navigation-heavy |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-about.md.md` | other | low | no strong filename/content signal |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-about_templates-components.md.md` | other | low | no strong filename/content signal |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-about_templates-products.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-doc-rev.md.md` | index_navigation | low | revision/history shell without procedural content |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro.md.md` | index_navigation | high | filename looks like intro/index and content is navigation-heavy |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-au.md.md` | other | low | no strong filename/content signal |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-card.md.md` | index_navigation | medium | tiny stub without procedural content |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-card_templates-matrix-card-config.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-card_templates-matrix-card-fields.md.md` | api_reference | medium | heading/body indicates field reference |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-customer-invoicing.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-echeck.md.md` | other | low | no strong filename/content signal |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-fme.md.md` | how_to_guide | medium | constraint facts (TTL/PCI/header/reuse/encryption) — eligible regardless of length |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-gift-card.md.md` | other | low | no strong filename/content signal |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-pa.md.md` | other | low | no strong filename/content signal |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-pay-by-link.md.md` | other | low | no strong filename/content signal |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-sa.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-tms.md.md` | other | low | no strong filename/content signal |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-unified-checkout.md.md` | other | low | no strong filename/content signal |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-matrix-intro_templates-matrix-vt.md.md` | other | low | no strong filename/content signal |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-tasks.md.md` | index_navigation | medium | tiny stub without procedural content |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-tasks_templates-adding.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-tasks_templates-default.md.md` | other | low | no strong filename/content signal |
| `en-us_boarding-template-management_user_all_ada_boarding-template-mgmt_templates-tasks_templates-deleting.md.md` | other | low | no strong filename/content signal |
