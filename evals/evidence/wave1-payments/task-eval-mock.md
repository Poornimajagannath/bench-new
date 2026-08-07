# Payments eval latest

- Mode: `mock`
- Gate: **pass**
- Source: `cybersource-payments-openapi`
- Denominator: **30** ops
- Exclusions: `[]`
- When: 2026-08-07T07:02:44+00:00
- Reason: agent can construct a valid sandbox payment request from generated pages

## Steps

| Step | Result | Detail |
| --- | --- | --- |
| reference_pages_complete | pass | 30/30 ops (source=cybersource-payments-openapi; excluded=[]) |
| construct_sandbox_payment | pass | built POST /pts/v2/payments body from createPayment.md |
| pan_guard | pass | page documents tokenized/no-raw-PAN guidance |
| eval_seeds_present | pass | 30 seeds in cybersource-payments-openapi.eval_seeds.json |
| no_raw_reads | pass | ok |
