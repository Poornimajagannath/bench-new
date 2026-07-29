---
artifact_contract: ce-unified-plan/v1
artifact_readiness: implementation-ready
execution: code
product_contract_source: ce-plan-bootstrap
created: 2026-07-29
---

# Plan: Candidates Artifact Freshness

## Goal

Keep `artifacts/candidates.json` in sync with the output from
`pipelines/synthesize_candidates.py`.

## Problem

`relay_bench/pm_gate.py` now writes richer candidate suggestion metadata:

- `approved_workflow_id`
- `original_suggested_workflow_ids`
- `remapped_from_suggestion`

But the checked-in `artifacts/candidates.json` still has the old shape. A local
run rewrites the file. That makes the proof artifact stale.

## Requirements

- R1: Regenerate `artifacts/candidates.json` from the current pipeline code.
- R2: Add a test that fails when `artifacts/candidates.json` is stale.
- R3: Keep the test deterministic and credential-free.
- R4: Keep existing task packs, hidden truth, verifier results, and PM report
  behavior unchanged unless generation requires an intentional update.

## Key Decisions

- KTD1: Test freshness in Python, not with a shell-only check.
  Reason: unit tests already run in this repo and can compare the structured
  payload without adding a new tool.

- KTD2: Compare the synthesized payload to the checked-in JSON object.
  Reason: this catches shape drift and value drift.

## Implementation Units

### U1. Refresh Candidate Artifact

Files:

- `artifacts/candidates.json`

Work:

- Run `python3 pipelines/synthesize_candidates.py`.
- Commit the regenerated `artifacts/candidates.json`.

Tests:

- `python3 pipelines/synthesize_candidates.py`
- `git status --short` must not show `artifacts/candidates.json` after the
  final generated file is committed.

### U2. Add Freshness Test

Files:

- `tests/test_discovery.py`

Work:

- Add a test that loads `artifacts/candidates.json`.
- Generate the expected payload with `synthesize_candidates_payload()`.
- Assert the two JSON objects are equal.

Tests:

- `python3 -m unittest discover -s tests`

## Verification

Run:

```bash
python3 -m unittest discover -s tests
python3 pipelines/synthesize_candidates.py
python3 pipelines/run_demo.py --workflow flex-token-lifecycle
python3 pipelines/run_demo.py --workflow http-signature-debug
python3 pipelines/run_demo.py --workflow microform-payer-auth-state-machine
python3 pipelines/run_bench_v0.py --workflow microform-payer-auth-state-machine
git diff --check HEAD
git status --short
```
