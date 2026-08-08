# Developer corpus build report

Generated: 2026-08-08T15:42:55+00:00
Stamp date: `2026-08-08`

## Discovery (denominator)

Source: `llms.txt_derived_roots`

Corpus denominator is the deduped set of family-root paths derived from llms.txt subtopic URLs (plus docs.md supplements). Unfetchable roots remain in the denominator. Unfetchable reasons split derivation_error (ours) from site_defect (theirs).

- llms.txt `.md` URLs: **475**
- llms.txt `.pdf` URLs: **0** (recorded unfetchable)
- Roots discovered (denominator): **175**
- From llms.txt: **175**
- docs.md-only supplements: **0**

## Derivation rule accuracy

Separate success rates for family-repeat vs guide-dir fallback.

| Rule | Discovered | Fetched OK | Unfetchable | Success rate |
|---|---:|---:|---:|---:|
| `already_root` | 47 | 43 | 4 | 91.5% |
| `compendium` | 2 | 2 | 0 | 100.0% |
| `family_repeat` | 19 | 19 | 0 | 100.0% |
| `guide_dir` | 74 | 64 | 10 | 86.5% |
| `listed_root` | 33 | 29 | 4 | 87.9% |

## Unfetchable roots (split buckets)

404 on a constructed URL is **derivation_error** (ours). 500 on an exposed URL is **site_defect** (theirs). **empty_200** and **html_only** are distinct diagnoses. **hub_page** paths are structural, not family guides.

| Bucket | Count |
|---|---:|
| ours | 9 |
| theirs | 9 |

| Reason | Count |
|---|---:|
| `derivation_error` | 4 |
| `empty_200` | 8 |
| `html_only` | 1 |
| `site_defect` | 5 |

### Unfetchable detail

- `/api/reference.md` — **empty_200** (theirs) derivation=`guide_dir` HTTP 200
- `/docs/barclays/en-us/hosted-fields/quick-start-guide/all/na/barclays-hosted-fields-qsg.md` — **unresolved_derivation** (ours) derivation=`guide_dir` HTTP 200
- `/docs/barclays/en-us/platform/overview/all/na/barclays-solution.md` — **unresolved_derivation** (ours) derivation=`guide_dir` HTTP 200
- `/docs/barclays/en-us/webhooks/implementation/all/rest/webhooks.md` — **unresolved_derivation** (ours) derivation=`family_repeat` HTTP 200
- `/docs/cybs/en-us/apple-pay/developer/all/rest.md` — **derivation_miss** (ours) derivation=`guide_dir` HTTP 404
- `/docs/cybs/en-us/boarding-template-management/user/all/ada.md` — **empty_200** (ours) derivation=`guide_dir` HTTP 200
- `/docs/cybs/en-us/boarding/user/all/ebc.md` — **derivation_miss** (ours) derivation=`guide_dir` HTTP 404
- `/docs/cybs/en-us/currency-codes/reference/ctv/na.md` — **empty_200** (ours) derivation=`guide_dir` HTTP 200
- `/docs/cybs/en-us/doc-rel/relnote/all/na.md` — **derivation_miss** (ours) derivation=`guide_dir` HTTP 404
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/April-2025.md` — **site_defect** (theirs) derivation=`guide_dir` HTTP 500
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/August-2025.md` — **empty_200** (ours) derivation=`guide_dir` HTTP 200
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/December-2025.md` — **empty_200** (ours) derivation=`guide_dir` HTTP 200
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/February-2025.md` — **site_defect** (theirs) derivation=`guide_dir` HTTP 500
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/February-2026.md` — **empty_200** (ours) derivation=`guide_dir` HTTP 200
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/January-2025.md` — **site_defect** (theirs) derivation=`guide_dir` HTTP 500
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/January-2026.md` — **empty_200** (ours) derivation=`guide_dir` HTTP 200
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/July-2025.md` — **empty_200** (ours) derivation=`guide_dir` HTTP 200
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/June-2025.md` — **site_defect** (theirs) derivation=`guide_dir` HTTP 500
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/March-2025.md` — **site_defect** (theirs) derivation=`guide_dir` HTTP 500
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/March-2026.md` — **empty_200** (ours) derivation=`guide_dir` HTTP 200
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/May-2025.md` — **site_defect** (theirs) derivation=`guide_dir` HTTP 500
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/November-2025.md` — **empty_200** (ours) derivation=`guide_dir` HTTP 200
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/October-2025.md` — **empty_200** (ours) derivation=`guide_dir` HTTP 200
- `/docs/cybs/en-us/doc-rel/relnote/all/na/doc-release-notes/doc-release-notes-intro/September-2025.md` — **empty_200** (ours) derivation=`guide_dir` HTTP 200
- `/docs/cybs/en-us/ebc/gettingstarted/all/rest.md` — **site_defect** (theirs) derivation=`guide_dir` HTTP 500
- `/docs/cybs/en-us/echeck/user/all/rest.md` — **derivation_miss** (ours) derivation=`guide_dir` HTTP 404
- `/docs/cybs/en-us/google-pay/developer/ctv/rest.md` — **empty_200** (ours) derivation=`guide_dir` HTTP 200
- `/docs/cybs/en-us/isv-plugins/admin/all/na.md` — **derivation_miss** (ours) derivation=`guide_dir` HTTP 404
- `/docs/cybs/en-us/isv-plugins/get-started/all/na.md` — **derivation_miss** (ours) derivation=`guide_dir` HTTP 404
- `/docs/cybs/en-us/llm/get-started/all/na.md` — **derivation_miss** (ours) derivation=`guide_dir` HTTP 404
- … and 51 more (see corpus-report.json)

## Deep link spot check

Checked: **5** — anchors found: **4** / 5 — FAIL

- `boarding` #boarding-intro-overview → ok (HTML 200)
- `payments` #payments-intro → ok (HTML 200)
- `tms` #tms-overview → ok (HTML 200)
- `security-keys` #keys-intro → ok (HTML 200)
- `unified-checkout` #uc-getting-started → MISSING (HTML 200)

## Fetch

- Roots fetched OK: **131** / 175 (source: `raw/2026-08-08/`)
- Total bytes: **19504453**

## Per product

| Product | Root fetched | Bytes | Sections | Quarantined | Code blocks | TOC topics | TOC covered | TOC missed |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Introduction | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accept-device-acq-implementation | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accept-devices-acq-dist-integ | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| additional-amount-types | yes | 15330 | 1 | 0 | 0 | 0 | 0 | 0 |
| agent-toolkit | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| airline | yes | 161840 | 118 | 2 | 44 | 0 | 0 | 0 |
| api-fields | yes | 3181637 | 7731 | 2 | 26 | 0 | 0 | 0 |
| applepay | yes | 191492 | 82 | 2 | 34 | 0 | 0 | 0 |
| auto-fuel | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| avs-codes | yes | 20343 | 5 | 0 | 0 | 0 | 0 | 0 |
| barclays-hosted-fields-qsg | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| barclays-solution | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| batch-upload | yes | 486586 | 83 | 2 | 40 | 0 | 0 | 0 |
| bin-lookup | yes | 47644 | 22 | 2 | 18 | 0 | 0 | 0 |
| boarding | yes | 268904 | 137 | 2 | 57 | 109 | 109 | 0 |
| boarding-template-mgmt | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| boarding-user | yes | 184102 | 102 | 2 | 2 | 0 | 0 | 0 |
| built-by-them | yes | 1006 | 1 | 0 | 0 | 0 | 0 | 0 |
| built-by-us | yes | 1490 | 1 | 0 | 0 | 0 | 0 | 0 |
| click-to-pay | yes | 523897 | 314 | 5 | 86 | 0 | 0 | 0 |
| contact-us | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| country-codes | yes | 14148 | 1 | 0 | 0 | 0 | 0 | 0 |
| cp-retail | yes | 387909 | 226 | 2 | 108 | 0 | 0 | 0 |
| credentials | yes | 405947 | 179 | 2 | 94 | 0 | 0 | 0 |
| currency-codes | yes | 26692 | 1 | 0 | 0 | 0 | 0 | 0 |
| currency-codes-ctv | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dcc-merchant | yes | 37111 | 30 | 3 | 14 | 0 | 0 | 0 |
| dcc-merchant-errors | yes | 167 | 1 | 0 | 0 | 0 | 0 | 0 |
| dcc-merchant-use-cases | yes | 488 | 1 | 0 | 0 | 0 | 0 | 0 |
| digital-accept-flex | yes | 989174 | 503 | 4 | 207 | 0 | 0 | 0 |
| doc-release-notes | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| doc101_ebc | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| echeck-user-guide | yes | 124021 | 77 | 3 | 10 | 0 | 0 | 0 |
| endpoints | yes | 11998 | 1 | 0 | 0 | 0 | 0 | 0 |
| ev-charging | yes | 71598 | 43 | 2 | 12 | 0 | 0 | 0 |
| faqs | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| googlepay | yes | 36096 | 33 | 2 | 15 | 0 | 0 | 0 |
| healthcare | yes | 11777 | 11 | 2 | 2 | 0 | 0 | 0 |
| healthcare-processing-intro | yes | 186 | 1 | 0 | 0 | 0 | 0 | 0 |
| home-acq | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| installment-plans | yes | 135069 | 136 | 2 | 24 | 0 | 0 | 0 |
| invoicing | yes | 242256 | 95 | 2 | 42 | 0 | 0 | 0 |
| isv-getting-started | yes | 23871 | 18 | 1 | 2 | 0 | 0 | 0 |
| isv-plugin-o | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| klarna | yes | 132264 | 68 | 2 | 23 | 0 | 0 | 0 |
| language-codes | yes | 1294 | 1 | 0 | 0 | 0 | 0 | 0 |
| level-2-3 | yes | 121897 | 58 | 2 | 12 | 0 | 0 | 0 |
| llm-getting-started | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| lodging | yes | 70290 | 41 | 2 | 10 | 0 | 0 | 0 |
| mandates-april-2023 | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mandates-april-2024 | yes | 20146 | 19 | 2 | 0 | 0 | 0 | 0 |
| mandates-oct-2024 | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mandates-october-2023 | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mass-transit | yes | 401764 | 171 | 2 | 53 | 0 | 0 | 0 |
| oauth | yes | 39139 | 16 | 2 | 11 | 0 | 0 | 0 |
| pax-a35 | yes | 63261 | 58 | 2 | 0 | 0 | 0 | 0 |
| pax-a3700 | yes | 48450 | 47 | 2 | 0 | 0 | 0 | 0 |
| pax-a77 | yes | 50446 | 49 | 2 | 0 | 0 | 0 | 0 |
| pax-a920 | yes | 51487 | 49 | 2 | 0 | 0 | 0 | 0 |
| pax-a920max | yes | 51810 | 49 | 2 | 0 | 0 | 0 | 0 |
| pax-a920pro | yes | 51982 | 49 | 2 | 0 | 0 | 0 | 0 |
| pax-all-in-one | yes | 204530 | 187 | 2 | 1 | 0 | 0 | 0 |
| pax-im30 | yes | 49766 | 47 | 2 | 0 | 0 | 0 | 0 |
| pay-by-bank | yes | 48051 | 28 | 2 | 10 | 0 | 0 | 0 |
| pay-by-bank-payto | yes | 58580 | 47 | 2 | 9 | 0 | 0 | 0 |
| pay-by-bank-payto-process-trxn | yes | 188 | 1 | 0 | 0 | 0 | 0 | 0 |
| paybybank-intro-services | yes | 466 | 1 | 0 | 0 | 0 | 0 | 0 |
| paybylink | yes | 52427 | 37 | 2 | 16 | 0 | 0 | 0 |
| payer-auth | yes | 703162 | 333 | 2 | 108 | 0 | 0 | 0 |
| payer-auth-vpp | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| payments | yes | 397466 | 266 | 2 | 82 | 0 | 0 | 0 |
| payments-acq | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| payouts-aft-dev | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| payouts-dev | yes | 219718 | 59 | 2 | 18 | 0 | 0 | 0 |
| paypal | yes | 126421 | 77 | 2 | 27 | 0 | 0 | 0 |
| paze | yes | 53098 | 30 | 3 | 9 | 0 | 0 | 0 |
| pin-debit | yes | 133352 | 89 | 2 | 35 | 0 | 0 | 0 |
| processor-names | yes | 49730 | 2 | 0 | 0 | 0 | 0 | 0 |
| product-notes | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| reason-codes-so | yes | 15988 | 1 | 0 | 0 | 0 | 0 | 0 |
| reason-codes-so-ap | yes | 13218 | 1 | 0 | 0 | 0 | 0 | 0 |
| recurring-billing-dev | yes | 103589 | 80 | 2 | 53 | 0 | 0 | 0 |
| recurring-billing-user | yes | 37705 | 23 | 2 | 0 | 0 | 0 | 0 |
| reporting | yes | 211920 | 59 | 1 | 22 | 0 | 0 | 0 |
| reporting-ug | yes | 471158 | 149 | 2 | 0 | 0 | 0 | 0 |
| response-codes | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rest-api-sdks | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rest-getting-started | yes | 208574 | 97 | 6 | 22 | 0 | 0 | 0 |
| rn-2025-06-06 | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rn-2025-06-13 | yes | 8283 | 10 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-06-20 | yes | 6319 | 5 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-06-27 | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rn-2025-07-03 | yes | 7313 | 6 | 1 | 0 | 0 | 0 | 0 |
| rn-2025-07-11 | yes | 9210 | 6 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-07-18 | yes | 6726 | 5 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-07-25 | yes | 9517 | 6 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-08-01 | yes | 8816 | 6 | 1 | 0 | 0 | 0 | 0 |
| rn-2025-08-08 | yes | 9865 | 6 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-08-15 | yes | 11445 | 6 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-08-22 | yes | 7310 | 6 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-08-29 | yes | 11114 | 6 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-09-05 | yes | 4468 | 6 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-09-12 | yes | 8688 | 7 | 1 | 0 | 0 | 0 | 0 |
| rn-2025-09-19 | yes | 12659 | 8 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-09-26 | yes | 2499 | 6 | 1 | 0 | 0 | 0 | 0 |
| rn-2025-10-03 | yes | 4300 | 5 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-10-10 | yes | 3309 | 6 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-10-17 | yes | 8506 | 7 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-10-24 | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rn-2025-10-31 | yes | 6181 | 6 | 2 | 0 | 0 | 0 | 0 |
| rn-2025-11-07 | yes | 4592 | 6 | 3 | 0 | 0 | 0 | 0 |
| rn-2025-11-14 | yes | 3458 | 6 | 3 | 0 | 0 | 0 | 0 |
| rn-2025-11-21 | yes | 5387 | 6 | 3 | 0 | 0 | 0 | 0 |
| rn-2025-12-05 | yes | 927 | 6 | 0 | 0 | 0 | 0 | 0 |
| rn-2025-12-12 | yes | 3440 | 6 | 2 | 0 | 0 | 0 | 0 |
| rn-2026-01-02 | yes | 2218 | 6 | 1 | 0 | 0 | 0 | 0 |
| rn-2026-01-09 | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rn-2026-01-16 | yes | 3695 | 6 | 2 | 0 | 0 | 0 | 0 |
| rn-2026-01-23 | yes | 3337 | 6 | 2 | 0 | 0 | 0 | 0 |
| rn-2026-01-30 | yes | 5464 | 6 | 3 | 0 | 0 | 0 | 0 |
| rn-2026-02-06 | yes | 5825 | 6 | 2 | 0 | 0 | 0 | 0 |
| rn-2026-02-13 | yes | 2355 | 6 | 1 | 0 | 0 | 0 | 0 |
| rn-2026-02-20 | yes | 3309 | 6 | 3 | 0 | 0 | 0 | 0 |
| rn-2026-02-27 | yes | 4863 | 7 | 2 | 0 | 0 | 0 | 0 |
| rn-2026-03-06 | yes | 5710 | 7 | 3 | 0 | 0 | 0 | 0 |
| rn-2026-03-13 | yes | 6942 | 7 | 1 | 0 | 0 | 0 | 0 |
| rn-2026-03-20 | yes | 8427 | 7 | 3 | 0 | 0 | 0 | 0 |
| rn-2026-03-27 | yes | 1611 | 5 | 2 | 0 | 0 | 0 | 0 |
| rn-2026-04-02 | yes | 9575 | 8 | 2 | 0 | 0 | 0 | 0 |
| rn-2026-04-10 | yes | 9782 | 10 | 1 | 0 | 0 | 0 | 0 |
| rn-2026-04-17 | yes | 15185 | 18 | 2 | 0 | 0 | 0 | 0 |
| rn-2026-04-24 | yes | 15798 | 18 | 3 | 0 | 0 | 0 | 0 |
| rn-2026-05-01 | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| sa-checkout | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| sa-hosted | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| samsungpay | yes | 69061 | 71 | 3 | 27 | 0 | 0 | 0 |
| sandbox | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| secure-acceptance | yes | 373573 | 129 | 2 | 17 | 0 | 0 | 0 |
| security-keys | yes | 101843 | 49 | 2 | 5 | 0 | 0 | 0 |
| sis-pax | yes | 651334 | 323 | 2 | 191 | 0 | 0 | 0 |
| so-conversion | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| state-codes | yes | 6628 | 1 | 0 | 0 | 0 | 0 | 0 |
| tap-to-pay-ios | yes | 59198 | 66 | 2 | 3 | 0 | 0 | 0 |
| tap-to-phone | yes | 134915 | 170 | 2 | 4 | 0 | 0 | 0 |
| tap-to-phone-sis | yes | 428988 | 240 | 2 | 114 | 0 | 0 | 0 |
| tax-calculation | yes | 94315 | 56 | 2 | 12 | 0 | 0 | 0 |
| test-data | yes | 155387 | 39 | 0 | 4 | 0 | 0 | 0 |
| testing-guide | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time-zones | yes | 9462 | 1 | 0 | 0 | 0 | 0 | 0 |
| tink | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| tms | yes | 453187 | 361 | 4 | 102 | 0 | 0 | 0 |
| tms-acq | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| tms-cust-tkn | yes | 230 | 1 | 0 | 0 | 0 | 0 | 0 |
| txn-batch | yes | 8915 | 11 | 0 | 3 | 0 | 0 | 0 |
| txn-search | yes | 43732 | 16 | 1 | 3 | 0 | 0 | 0 |
| txn_batch_api_intro | yes | 211 | 1 | 0 | 0 | 0 | 0 | 0 |
| uc-acq | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| uc-qsg | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| unified-checkout | yes | 509657 | 220 | 5 | 72 | 0 | 0 | 0 |
| unified-click-to-pay | yes | 324160 | 92 | 5 | 36 | 0 | 0 | 0 |
| user_management_api_intro | yes | 649 | 1 | 0 | 0 | 0 | 0 | 0 |
| via-qsg | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| visa-bank-accoun-val | no | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| webhooks | yes | 146916 | 124 | 2 | 36 | 0 | 0 | 0 |

## TOC completeness

- Products checked: **1** / 1
- TOC topics: **109**
- Covered: **109** / 109
- Missed: **0**

## Sanitize

- Sections total: **20661**
- Sections clean: **20433** / 20661
- Code blocks preserved: **2382**

| Quarantine kind | Sections |
|---|---:|
| `about_guide_boilerplate` | 137 |
| `revision_history` | 81 |
| `support_center` | 10 |

## Source files

- Discovery: `artifacts/content_engine/corpus_build/discovery.json`
- Raw: `raw/2026-08-08/`
- Cleaned: `cleaned/2026-08-08/`
- Quarantine: `quarantine/2026-08-08/`
- TOC checkpoint: `artifacts/content_engine/corpus_build/toc-checkpoint/`
