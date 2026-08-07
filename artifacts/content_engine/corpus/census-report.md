# Corpus census

- When: `2026-08-07T06:43:27+00:00`
- Corpus: `/home/badari/workspace/poornima/visa-relay-bench/cybersource-docs`
- Documents classified: **359**
- Eligible for ingestion: **190**
- Quarantined (policy): **169**

## Counts by kind

| Kind | Count | Share | Quarantined by policy? |
| --- | ---: | ---: | --- |
| API reference (`api_reference`) | 12 | 3.3% | no |
| How-to guide (`how_to_guide`) | 123 | 34.3% | no |
| Release note (`release_note`) | 64 | 17.8% | yes |
| Index / navigation (`index_navigation`) | 105 | 29.2% | yes |
| Legal (`legal`) | 0 | 0.0% | yes |
| Marketing (`marketing`) | 8 | 2.2% | no |
| Other / unclassified (`other`) | 47 | 13.1% | no |

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
| `en-us_additional-amount-types_reference_all_na_additional-amount-types.md.md` | api_reference | high | filename matches API reference pattern |
| `en-us_airline_developer_all_rest_airline_airline-ref-intro.md.md` | index_navigation | high | filename looks like intro/index and content is navigation-heavy |
| `en-us_airline_developer_all_rest_airline_home-merch.md.md` | marketing | medium | filename matches marketing pattern |
| `en-us_api-fields_reference_all_rest_api-fields.md.md` | api_reference | high | filename matches API reference pattern |
| `en-us_api-fields_reference_all_so_api-fields.md.md` | api_reference | high | filename matches API reference pattern |
| `en-us_apple-pay_developer_all_rest_applepay.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_apple-pay_developer_all_rest_applepay_applepay-cfg.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_apple-pay_developer_all_rest_applepay_applepay-getting-started.md.md` | how_to_guide | medium | filename matches how-to / task guide |
| `en-us_apple-pay_developer_all_rest_applepay_applepay-intro.md.md` | index_navigation | medium | filename looks like intro/index and content is navigation-heavy |
| `en-us_apple-pay_developer_all_rest_applepay_applepay-txns-intro.md.md` | index_navigation | medium | filename looks like intro/index and content is navigation-heavy |
| `en-us_avs-codes_reference_all_na_avs-codes.md.md` | api_reference | high | filename matches API reference pattern |
| `en-us_batch_user_all_so_batch-upload_batch-files-managing.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_batch_user_all_so_batch-upload_batch-results-email-notifs.md.md` | other | low | no strong filename/content signal |
| `en-us_batch_user_all_so_batch-upload_batch-results-file-response.md.md` | other | low | no strong filename/content signal |
| `en-us_batch_user_all_so_batch-upload_batch-results-txns-response.md.md` | other | low | no strong filename/content signal |
| `en-us_batch_user_all_so_batch-upload_batch-results-txns-rpt-request.md.md` | other | low | no strong filename/content signal |
| `en-us_batch_user_all_so_batch-upload_batch-results-txns-rpt-submission-details.md.md` | other | low | no strong filename/content signal |
| `en-us_batch_user_all_so_batch-upload_batch-uploading-ebc.md.md` | other | low | no strong filename/content signal |
| `en-us_batch_user_all_so_batch-upload_c_Using_Java_Sample_Code_to_Upload_Files.md.md` | index_navigation | medium | tiny stub without procedural content |
| `en-us_batch_user_all_so_batch-upload_home-merch.md.md` | marketing | medium | filename matches marketing pattern |
| `en-us_bin-lookup_developer_all_rest_bin-lookup.md.md` | how_to_guide | medium | procedural how-to signals in content |
| `en-us_bin-lookup_developer_all_rest_bin-lookup_bin-lookup-intro.md.md` | index_navigation | medium | filename looks like intro/index and content is navigation-heavy |
| `en-us_bin-lookup_developer_all_rest_bin-lookup_bin-lookup-payouts-req-task.md.md` | how_to_guide | medium | filename matches how-to / task guide |
| `en-us_bin-lookup_developer_all_rest_bin-lookup_bin-lookup-reference-intro.md.md` | index_navigation | high | filename looks like intro/index and content is navigation-heavy |
