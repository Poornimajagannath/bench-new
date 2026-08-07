# DocETL full pipeline run

- When: see `artifacts/full_docetl_run.json` → `started_at` / `finished_at`
- Command: `.venv-docetl/bin/python pipelines/run_full_docetl_pipeline.py --discovery docetl`
- Package: `docetl==0.3.0` (`requirements-docetl.txt`)
- Mode: **code_map** (no LLM)

## Honesty

| Field | Value |
| --- | --- |
| `honest_labels` | **`imported-code_map`** |
| Network | denied |
| LLM | not used |

DocETL actually executed — not style-only.

## Results

| Metric | Value |
| --- | ---: |
| Content sources promoted | **20** |
| Content sources blocked | **44** |
| Bench workflows OK | **3 / 3** |

Bench: `flex-token-lifecycle`, `http-signature-debug`, `microform-payer-auth-state-machine` — all exit 0 with `imported-code_map`.

Notable promote: `boarding-guide-…_boarding-user` (**401** units), Microform quickstart (**11**), several payments TOC intros, lab/scenario/template sources.

Blocked set is mostly boarding REST intro/template stubs and other registry sources that fail promotion gates (normalized but not promoted) — DocETL still ran `code_map` on extract where applicable.

Artifacts: `artifacts/full_docetl_run.json`, `artifacts/full_docetl_run.log`.
