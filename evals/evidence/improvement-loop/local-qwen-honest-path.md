# Improvement loop — honest local Spark Qwen path

**Status: RUN COMPLETE.**

## Wiring

- Default generative backend: local Spark Qwen at `http://127.0.0.1:8000/v1`
  (`nvidia/Qwen3.6-35B-A3B-NVFP4`, Hermes provider `spark-qwen`).
- Cloud keys optional but **forbidden for corpus-bearing prompts**
  (`cloud_corpus_egress: forbidden`). Loopback-only `chat_completion_local`.
- Report field is `code_path` (what actually ran), not a requested mode label.
  Values: `deterministic_rules` | `local_spark_qwen_draft` |
  `refused_local_unreachable`.
- Caps: `--max-prs 3`, `--max-completion-tokens 8000`, `--timeout-seconds 180`.

## No-invention guard

Rule text and helpers in `pipelines/run_improvement_loop.py`:
`NO_INVENTION_RULE`, `propose_for_missing_outcome`, `proposal_invents_facts`.
Tests: `tests/test_improvement_loop_no_invention.py` — a step with no stated
outcome must yield `[gap: no stated outcome in source claims]`, not an
invented result; C4-style “Author expected outcomes…” is discarded;
`change_type=gap_marker` is allowed.

## This run

See `artifacts/improvement_loop/run-report.json` for the full record.
