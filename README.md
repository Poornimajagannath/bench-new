# Content Bench (private) — CyberSource lane

Private configuration + CyberSource corpus. The **engine** is synced from public
[`content-bench`](https://github.com/Poornimajagannath/content-bench) tag
`v0.1-stripe-proof` — see [`ENGINE_UPSTREAM.md`](ENGINE_UPSTREAM.md).

**Standing rules**
- Engine fixes land in content-bench first, then sync here the same day.
- No private data, traces, or drop logs ever cross into content-bench.
- Serve layers read `content/` + `normalized/` only — never `raw/`.
- Gitleaks fail-closed in CI.

## Per-product registry

```text
registry/payments.json   # Wave 1 (enabled)
registry/boarding.json   # Wave 2 stub (disabled)
registry/lab.json        # local fixtures for unit tests
```

## Wave 1 — payments

```bash
python3 pipelines/run_source_mix.py
python3 pipelines/run_ingestion_snapshot.py --stamp-date YYYY-MM-DD
python3 pipelines/run_specs_to_docs_v0.py --source cybersource-payments-core-openapi
python3 pipelines/run_reference_pages_a2.py
python3 pipelines/write_prose.py && python3 pipelines/humanize.py
python3 evals/run_payments_eval.py --mode mock          # PR gate
python3 evals/run_cybersource_docs_compare.py --evidence  # never a PR gate
python3 -m unittest discover -s tests
cd mcp-server && npm install   # content-docs MCP → evals/manual-runs.jsonl
node portal/server.js
```

Reports: `artifacts/content_engine/payments/`  
Frozen evidence: `evals/evidence/wave1-payments/`  
Nightly parity → branch `evidence/cybersource-docs-parity`.

### Wave 1 gates

| Gate | Status |
| --- | --- |
| All unit tests green | required |
| Every payments operation has a page | 8/8 |
| Task eval mock pass | required |
| Parity report with score | evidence only |
| Zero reads from `raw/` | required |

Do not start boarding (Wave 2) until these gates pass and the architect reviews.
