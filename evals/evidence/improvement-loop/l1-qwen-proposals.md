# L1 proposals from Spark Qwen — implemented

**Status: MERGED.** Generative half of the improvement loop ran against local
Spark Qwen (`nvidia/Qwen3.6-35B-A3B-NVFP4` at `http://127.0.0.1:8000/v1`).
Both proposed candidates that passed re-check were implemented.

## L1-prereq-pattern-tune

**Proposal:** expand `_PREREQUISITE_PATTERN` for “Before you can…”, “must
contact”, “This implementation requires…”, “requires the use of”, and
“Notify your account representative”.

**Evidence:** `evals/evidence/wave1-payments/c3-payments-reingest.md`
(`pa2-ccdc-intro` soft schema gap).

**Result:** `pa2-ccdc-intro` now yields **3** `prose_claim` / `prerequisite`
claims (was 0). Tests in `tests/test_triage.py`.

## L1-rest-example-json

**Proposal:** extract fenced JSON on standalone REST Example pages as
`rest_example` claims (role + top-level keys + compact body). No invention.

**Evidence:** `evals/evidence/WAVE2-CLOSEOUT.md` remaining-48 shape list.

**Result:** among boarding `no_schema_match` drops that contain JSON fences,
**16 / 16** now yield `rest_example` claims. Schema added to
`CLAIM_SCHEMAS`. Tests in `tests/test_rest_example.py`.

## Discarded by the same LLM run (correct)

- `L1-field-table-schema` — already shipped in Wave 2 closeout.
