# Evals (private CyberSource lane)

- **Task eval (PR gate):** `python3 evals/run_payments_eval.py --mode mock`
- **CyberSource docs parity (evidence only, never a PR gate):**
  `python3 evals/run_cybersource_docs_compare.py --evidence`
- **Humanizer fact guard (unit):** `python3 -m unittest tests.test_humanizer`

Parity reports are regenerable. The nightly workflow pushes them to
`evidence/cybersource-docs-parity` (not `main`).

**Standing rule:** no data, traces, or drop logs from this private repo ever
cross into public `content-bench`. Engine fixes port back the same day.
