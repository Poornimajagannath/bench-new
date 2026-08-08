# Improvement loop — run report

- When: `2026-08-08T04:37:47+00:00`
- Mode: **deterministic** — no LLM API key present in the environment; the LLM path did not run and no key was extracted from credential stores.
- Spend: $0.00 of $2.00 budget
- PR cap: 3

| Candidate | Status | Re-check | Evidence |
| --- | --- | --- | --- |
| C1-endpoint-url-style: Extend endpoint_fact extraction to match CyberSource's backticked full-URL endpo | discarded | fail: endpoint_facts=2 url_line=True — defect no longer reproduces | evals/evidence/WAVE2-CLOSEOUT.md — remaining-48 shape list; artifacts/content_engine/boarding/ingestion-report |
| C2-step-anchor-noise: Strip trailing {#anchor} tokens from quickstart_step titles/text at extraction s | discarded | fail: no anchored residual steps remain | artifacts/content_engine/boarding/composition-report.json — mega_residual_samples |
| C3-payments-still-dropped: Re-run payments ingestion: extractor upgrades since Wave 1 close (constraint cla | proposed | pass: 1/12 previously dropped payments pages now yield claims under the current extractor | evals/evidence/wave1-payments/extraction-recall-fix.md — still-dropped names |
| C4-missing-outcomes: Author expected outcomes for 220 steps | discarded | n/a | artifacts/content_engine/boarding/gap-report.md — headline 1 |
| C5-llms-txt-defect: Fix llms.txt omission and merchant-boarding.md HTTP 500 | discarded | n/a | artifacts/content_engine/boarding/gap-report.md — headline 3; artifacts/content_engine/boarding/toc-fetch-repo |
