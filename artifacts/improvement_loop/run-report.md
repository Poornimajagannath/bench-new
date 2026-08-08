# Improvement loop — run report

- When: `2026-08-08T04:56:04+00:00`
- Mode: **llm** — local Spark Qwen `nvidia/Qwen3.6-35B-A3B-NVFP4` at `http://127.0.0.1:8000/v1` (no cloud API key required).
- Spend: $0.00 of $2.00 budget
- PR cap: 3

| Candidate | Status | Re-check | Evidence |
| --- | --- | --- | --- |
| C1-endpoint-url-style: Extend endpoint_fact extraction to match CyberSource's backticked full-URL endpo | discarded | fail: endpoint_facts=2 url_line=True — defect no longer reproduces | evals/evidence/WAVE2-CLOSEOUT.md — remaining-48 shape list; artifacts/content_engine/boarding/ingestion-report |
| C2-step-anchor-noise: Strip trailing {#anchor} tokens from quickstart_step titles/text at extraction s | discarded | fail: no anchored residual steps remain | artifacts/content_engine/boarding/composition-report.json — mega_residual_samples |
| C3-payments-still-dropped: Re-run payments ingestion: extractor upgrades since Wave 1 close (constraint cla | discarded | fail: already merged — recovered 1 claiming page(s); see c3-payments-reingest.md | evals/evidence/wave1-payments/extraction-recall-fix.md — still-dropped names; evals/evidence/wave1-payments/c3 |
| C4-missing-outcomes: Author expected outcomes for 220 steps | discarded | n/a | artifacts/content_engine/boarding/gap-report.md — headline 1 |
| C5-llms-txt-defect: Fix llms.txt omission and merchant-boarding.md HTTP 500 | discarded | n/a | artifacts/content_engine/boarding/gap-report.md — headline 3; artifacts/content_engine/boarding/toc-fetch-repo |
| L1-prereq-pattern-tune: Update the `_PREREQUISITE_PATTERN` regex in the extractor to capture 'Before you | proposed | pass: 1 evidence path(s) resolve; proposal is non-inventive | evals/evidence/wave1-payments/c3-payments-reingest.md — pa2-ccdc-intro is a soft schema gap (prerequisite pros |
| L1-field-table-schema: Add a `field_table` schema to the extraction engine to parse template matrix tab | discarded | fail: field_table schema already implemented (WAVE2-CLOSEOUT + tests/test_field_table.py) | evals/evidence/WAVE2-CLOSEOUT.md — Decision: add a `field_table` schema so the tables extract. Implementation: |
| L1-rest-example-json: Extend the extraction pipeline to parse JSON code blocks within REST example pag | proposed | pass: 1 evidence path(s) resolve; proposal is non-inventive | evals/evidence/WAVE2-CLOSEOUT.md — Remaining 48 zero-claim docs... by shape: REST example pages whose facts ar |
