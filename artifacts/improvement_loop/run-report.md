# Improvement loop — run report

- When: `2026-08-08T05:00:26+00:00`
- Code path taken: **local_spark_qwen_draft** — called local Spark Qwen `nvidia/Qwen3.6-35B-A3B-NVFP4` at `http://127.0.0.1:8000/v1` (Hermes provider spark-qwen).
- Requested path: `local-llm`
- LLM called: `True`
- Cloud corpus egress: `forbidden`
- Spend: $0.00 of $2.00 (local Qwen is $0; limiter is tokens/time)
- PR cap: 3
- Completion-token budget: 8000
- Timeout: 180s

No-invention rule: The loop may rephrase, restructure, and assemble existing claims, and may never author a fact absent from the claim set. A step with no stated outcome must receive a gap marker, not an invented result.

| Candidate | Status | Re-check | Evidence |
| --- | --- | --- | --- |
| C1-endpoint-url-style: Extend endpoint_fact extraction to match CyberSource's backticked full-URL endpo | discarded | fail: endpoint_facts=2 url_line=True — defect no longer reproduces | evals/evidence/WAVE2-CLOSEOUT.md — remaining-48 shape list; artifacts/content_engine/boarding/ingestion-report |
| C2-step-anchor-noise: Strip trailing {#anchor} tokens from quickstart_step titles/text at extraction s | discarded | fail: no anchored residual steps remain | artifacts/content_engine/boarding/composition-report.json — mega_residual_samples |
| C3-payments-still-dropped: Re-run payments ingestion: extractor upgrades since Wave 1 close (constraint cla | discarded | fail: already merged — recovered 3 claiming page(s); see c3-payments-reingest.md | evals/evidence/wave1-payments/extraction-recall-fix.md — still-dropped names; evals/evidence/wave1-payments/c3 |
| C4-missing-outcomes: Author expected outcomes for 220 steps | discarded | n/a | artifacts/content_engine/boarding/gap-report.md — headline 1 |
| C5-llms-txt-defect: Fix llms.txt omission and merchant-boarding.md HTTP 500 | discarded | n/a | artifacts/content_engine/boarding/gap-report.md — headline 3; artifacts/content_engine/boarding/toc-fetch-repo |
| L2-prerequisite-prose-extractor: Create a new `prerequisite_prose` schema/extractor to capture load-bearing prere | discarded | fail: prerequisite pattern already expanded (L1) | evals/evidence/wave1-payments/c3-payments-reingest.md — pa2-ccdc-intro soft schema gap (prerequisite prose) wh |
| L2-endpoint-required-fields-augment: Augment the `endpoint_fact` extractor or create a companion `endpoint_constraint | proposed | pass: 2 evidence path(s) resolve; proposal is non-inventive | evals/evidence/WAVE2-CLOSEOUT.md — Soft-gap findings: 57/176 matched Endpoint sections omit Required Fields li |
| L2-boarding-step-outcome-gap-marker: Add a gap marker for the 222 boarding workflow steps that lack stated outcomes.  | proposed | pass: 2 evidence path(s) resolve; proposal is non-inventive | evals/evidence/WAVE2-CLOSEOUT.md — Boarding gap report: 222 of 277 sequence steps have no stated outcome; eval |
