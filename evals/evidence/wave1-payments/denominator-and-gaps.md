# Wave 1 accounting — denominator, parity gaps, top drops

## 1. What file is the denominator of 8/8?

**File:** `data/content_engine/specs/cybersource-payments-core.openapi.json`  
(`payments-core.openapi.json` is a symlink to the same file.)

**Verdict: practice fixture, not production.**  
`info.title` = `CyberSource Payments Core (local Relay fixture)`  
`info.version` = `0.1.0-local`  
Registry `refresh_cadence` = `manual-fixture`.  
The gate’s `ops_coverage` check hard-codes the same eight operationIds.

So **8/8 means “all ops in the practice fixture have pages.”** It does **not** mean full payments API coverage.

### How many operations does the full payments spec contain?

Source of truth used for the comparison (public):  
`https://developer.cybersource.com/api-reference-assets/specs/cybs_merged.json`

| Scope | Operations |
| --- | ---: |
| Practice fixture (Wave 1 denominator) | **8** |
| Full merged REST (`cybs_merged.json`) | **223** |
| Payments REST under `/pts/` | **30** |

`/pts/` includes separate flows the fixture omitted: `refundPayment`, `voidPayment`, `authReversal`, `voidCapture`, `refundCapture`, `incrementAuth`, MIT void/reversal, payouts, pull-funds, etc.

Registry `canonical_url` pointed at `.../spec/payments.json`, but that URL currently returns HTML (SPA shell), not OpenAPI. The file on disk is the local fixture.

**Wave 1 is rehearsed against the fixture.** Closing Wave 1 as production coverage requires re-running A2 against the real `/pts/` surface (or an explicit scoped subset with a stated denominator).

## 2. Parity 95.8% — what did not pass?

Graded: 11 pass / **1 partial** / 0 fail (partial weighted 0.5 → 11.5/12 = 95.8%).

| Check | Result | Real doc gap or eval calibration? |
| --- | --- | --- |
| `rest_getting_started_aligned` | **partial** | **Eval calibration.** In `evals/run_cybersource_docs_compare.py` the check is hard-coded to return at best `partial` when REST getting-started fetches and auth/signature language appears in generated pages — it never returns `pass`. Not evidence of a missing upstream doc, and not a measured content miss beyond “we only claim high-level alignment.” |

No other graded check failed.

## 3. Top three drop log entries (Wave 1 payments ingestion)

All three: reason `no_schema_match` — intro/index-like pages with no extractable claim.

1. `en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_ctp-intro.md.md` — no quickstart/endpoint/error/prose claim extracted  
2. `en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_da-payments.md.md` — no quickstart/endpoint/error/prose claim extracted  
3. `en-us_digital-accept-flex_developer_all_rest_digital-accept-flex_microform-integ-v2.md.md` — no quickstart/endpoint/error/prose claim extracted  

(Full top-20: `evals/evidence/wave1-payments/top-20-drops.md`.)
