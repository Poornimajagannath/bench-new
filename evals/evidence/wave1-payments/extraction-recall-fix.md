# Extraction recall fix — diagnosis and verification

## 1. Why three pages produced zero claims

| Page | Bytes | Root cause |
| --- | ---: | --- |
| **da-payments** | 340 | Prose extractor required line-start `You\|Developers\|Merchants` and ≤220 chars. Page is declarative TTL/reuse facts (“15 minutes”, “multiple times”) — no match. Census also mislabeled it `index_navigation` (“tiny stub &lt;400 bytes”), so a later quarantine pass skipped it before extraction. |
| **microform-integ-v2** | 1211 | PCI SAQ A, device-side encryption, and mandatory-header facts lived in longer “You can…” lines and an IMPORTANT callout. Old regex missed them → `no_schema_match`. (Census correctly kept it as how-to; extraction was the sole gap.) |
| **ctp-intro** | 2952 | Header requirement, limited-use keys, encryption — intro prose, not imperative list lines. Old extractor missed constraints; census then quarantined it as intro/index (`-intro` + size &lt;3500). |

**Summary:** zero claims were an extractor shape mismatch (constraint prose ≠ imperative short lines), compounded on two pages by census treating short/intro constraint pages as empty shells.

## 2. Extractor + census tuning

- `prose_claim` now pulls constraint sentences (TTL/validity, reuse/rate, PCI/SAQ, mandatory headers, device/E2E encryption) from any sentence; short pages are eligible.
- Guidance lines accept `After you` and up to 500 chars.
- Census: constraint signals count as substantive; no `index_navigation` / tiny-stub quarantine when present.
- Shell drops must carry **bytes** + **first heading**; report includes a 10-drop human-check sample (not filename labels).

## 3. Re-ingest results

Stamp: `2026-08-08` · docs fetched **29** · claims **2690** · drops **14**  
Baseline: prior Wave 1 top-20 `no_schema_match` (`evals/evidence/wave1-payments/top-20-drops.md`).

| Metric | Value |
| --- | ---: |
| Prior empty (`no_schema_match`) pages | 20 |
| Now yielding claims | **6** |
| Still empty / quarantined | 14 |

**All three target pages now yield claims:**

| Page | Claims | Kinds captured |
| --- | ---: | --- |
| da-payments | 3 | `ttl_or_validity`, `ttl_and_reuse`, `guidance` (15-minute TTL + reuse) |
| microform-integ-v2 | 3 | `pci_compliance`, `device_encryption`, `mandatory_header` |
| ctp-intro | 3 | `reuse_or_rate_limit` (limited-use keys), `device_encryption`, `mandatory_header` |

Also recovered (same prior set): `payments_intro_digt_accpt_sec_intg`, `uc-intro`, `pa2-intro-intro`.

## 4. Shell triage rule

Enforced in `render_ingestion_report`: every `shell` row includes **Bytes** and **First heading**; missing fields flagged.  
Quarantine skips also carry bytes + heading for triage.  
**Sampled human check (10 drops)** is required in every report — confirm shell vs missed claim; do not triage by filename alone.

Artifacts: `artifacts/content_engine/payments/ingestion-report.md`, `top-drops.md`.
