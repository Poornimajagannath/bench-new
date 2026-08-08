# C3 — payments still-dropped re-ingest (merged)

**Status: MERGED.** Improvement-loop candidate C3 trusted and executed.
Class: safest proposal — re-run already-fetched pages; no new content; no
invention; re-checked before offer.

## Action

```
python3 pipelines/run_ingestion_snapshot.py \
  --docs-dir data/products/payments/guides \
  --openapi data/content_engine/specs/cybersource-payments.openapi.json \
  --recall-baseline evals/evidence/wave1-payments/top-20-drops.md
```

## Result (source: `artifacts/content_engine/payments/ingestion-report.json`)

| Metric | Value |
| --- | ---: |
| Docs fetched | 29 |
| Claims extracted | 6813 |
| Prior `no_schema_match` baseline | 20 |
| Recovered | **8** |
| Still dropped | 12 |

**C3 target recovered:** `en-us_tms_developer_all_rest_tms_tms-bin-lookup-service.md.md`
— **12** `endpoint_fact` claims (backticked full-URL TMS BIN Lookup endpoints).

## Still-dropped siblings (11 from C3 list + 1 prior-baseline peer)

Checked for thin-intro vs second schema gap (template-matrix pattern).

| Page | Bytes | Verdict |
| --- | ---: | --- |
| `payments-processing-basic-intro` | 229 | **Thin** — one-sentence TOC shell |
| `tms-wallet-tkn` | 210 | **Thin** — one-sentence product blurb |
| `tms-cust-tkn` | 230 | **Thin** — definition + child pointer |
| `tms-cust-pi-tkn` | 316 | **Thin** — definition shell |
| `tms-ship-tkn` | 448 | **Thin** — definition shell |
| `payments-debit-prepaid-process-intro` | 688 | **Thin** — section intro, no ops/fields |
| `tms-onboarding` | 783 | **Thin** — pure child-link TOC |
| `payments-intro` | 914 | **Thin** — overview intro |
| `sandbox.md` | 622 | **Thin / off-corpus** — signup marketing page |
| `tms-pi-tkn` (baseline peer) | (prior set) | **Thin** — token-type intro |
| `tms-ii-tkn` | 1693 | **Concept prose, not a matrix gap** — feature associations and definitions; no endpoints/tables/constraint sentences the current schemas accept. A `concept`/`overview` schema would be a product decision, not a missed table shape. |
| `pa2-ccdc-intro` | 2452 | **Soft schema gap (prerequisite prose)** — load-bearing “must contact acquirer / notify account rep / prerequisites” sentences. `_PREREQUISITE_PATTERN` only matches `prerequisite|must have|you must include|requires that|must be in the format`, so “Before you can… must contact” and “This implementation requires…” miss. Not a template-matrix (no tables); next schema/tune candidate, recorded here. |

**Summary:** nine pages are genuinely thin TOC/intros. One is concept overview.
One (`pa2-ccdc-intro`) is a small prerequisite-pattern miss — worth a follow-on
extractor tune, not a silent drop, and not the same class as `field_table`.
