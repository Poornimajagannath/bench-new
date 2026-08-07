---
title: "Stripe Connect proof — ingest OpenAPI + Connect guides, generate quickstart, eval gate"
date: 2026-08-07
artifact_contract: ce-unified-plan/v1
artifact_readiness: implementation-ready
product_contract_source: ce-plan-bootstrap
execution: code
origin: user /lfg stripe connect (after Connect proof recommendation)
---

# Stripe Connect proof — ingest OpenAPI + Connect guides, generate quickstart, eval gate

## Goal Capsule

Prove the content engine on a real public API: ingest a Stripe Connect–scoped OpenAPI slice plus Connect prose guides, generate fact pages and a backend quickstart into `content/`, and ship an eval harness whose gate is “connected account + Account Link created in Stripe test mode” (live only when a test secret is present; offline mock otherwise).

Authority: user-directed Connect proof > build-spec v2 lanes > existing content-engine honesty labels.

Stop conditions: no live keys in git; no full Stripe corpus ingest; no claim of Stripe endorsement; unittest stays network-free by default.

## Product Contract

### Summary

Add a parallel Stripe Connect source lane beside the existing gateway-docs lab. Scope is one track: platform creates a connected account and an Account Link for onboarding. Fact pages come from OpenAPI; sequencing/gotchas come from Connect prose with source pointers. An eval agent (or deterministic harness) proves the docs by attempting that flow.

### Problem Frame

The engine was proven only on a debranded fixture corpus. Outsiders need a recognizable API. Stripe publishes OpenAPI and Connect guides; Connect is multi-step enough to stress prose vs spec without boiling the ocean.

### Requirements

- R1. Vendor a Connect-scoped OpenAPI fixture under `data/stripe/openapi-connect.fixture.json` (Accounts, Account Links, and related Connect paths only — not the full Stripe spec in-repo).
- R2. Vendor a small set of Connect prose guides under `data/stripe/guides/` (how Connect works, authentication, onboarding quickstart, Account Links) with source URLs in frontmatter.
- R3. Register Stripe sources in `data/content_engine/source_registry.json` (product: `stripe`, `stripe-connect`).
- R4. Run source-mix + ingestion for the Stripe corpus into `raw/` + `normalized/`, producing Connect-specific reports under `artifacts/content_engine/stripe/`.
- R5. Generate `content/` markdown: one page per selected OpenAPI operation + `content/connect-quickstart.md` from a quickstart step schema (goal, prerequisites, numbered actions, expected outcome, common errors, ≤300 words/step).
- R6. Portal lists/serves the new pages; empty-state still honest when content absent on other branches.
- R7. `evals/run_connect_eval.py`: default `--mode mock` records a passing local proof from fixtures; `--mode live` uses `STRIPE_TEST_SECRET_KEY` (test-mode only) to create Account + Account Link and writes `evals/runs/*.json` + `evals/latest.md`.
- R8. Unit tests cover fixture parse, fact render, quickstart schema, mock eval; CI remains green without Stripe secrets.

### Scope Boundaries

In scope: Connect onboarding proof lane (Accounts + Account Links), offline fixtures, mock+live eval harness, content generation into `content/`.

Out of scope: full Stripe OpenAPI commit, payouts/subscriptions, live CI without secrets, Stripe branding claims, nightly improvement loop for Stripe.

### Acceptance Examples

- AE1. `python3 pipelines/run_stripe_connect_proof.py` writes reports, normalized claims, and `content/connect-quickstart.md` plus endpoint pages.
- AE2. Portal serves `/connect-quickstart` when content exists.
- AE3. `python3 evals/run_connect_eval.py --mode mock` exits 0 and writes `evals/latest.md` with gate=pass.
- AE4. With `STRIPE_TEST_SECRET_KEY=sk_test_...`, `--mode live` creates a test Account and Account Link (or records a clear auth failure without leaking the key).

## Planning Contract

### Key Technical Decisions

- KTD1. session-settled: Use Stripe Connect (not the fictional gateway corpus) as the public proof lane.
  Rejected: Prove only on debranded gateway-docs.
  Reason: User approved Connect proof after recommendation.

- KTD2. session-settled: Scope to Accounts + Account Links onboarding track.
  Rejected: Ingest all Stripe docs/OpenAPI.
  Reason: Buildable first proof; Connect complexity without unbounded corpus.

- KTD3. session-settled: Test-mode only for live eval; mock mode is the CI default.
  Rejected: Require live Stripe in every CI run.
  Reason: Repo is public; secrets optional; unittest must stay network-free.

- KTD4. Vendor a trimmed OpenAPI fixture extracted from stripe/openapi rather than submodule the whole repo.
  Rejected: Commit full `spec3.json`.
  Reason: Size and noise; Connect proof only needs a path subset.

- KTD5. Deterministic harness first (curl/urllib against Stripe API), not Claude Agent SDK, for V0 live mode.
  Rejected: Full Agent SDK eval in this PR.
  Reason: Proves the gate (docs → sandbox success) with fewer moving parts; Agent SDK is a follow-on (B1).

### Assumptions

- A1. Stripe public OpenAPI and Connect markdown docs may be fetched once to build fixtures; committed fixtures make CI offline.
- A2. Account Link creation in test mode is a sufficient gate for V0 (full Express Dashboard completion is out of band).

### Technical Design

```text
data/stripe/openapi-connect.fixture.json
data/stripe/guides/*.md
  -> pipelines/run_stripe_connect_proof.py
      -> source mix report
      -> ingest raw/ + normalized/
      -> render content/*.md (facts + quickstart)
  -> evals/run_connect_eval.py (mock | live)
  -> portal serves content/
```

### Sequencing

U1 fixtures → U2 proof pipeline → U3 eval → U4 tests/docs.

## Implementation Units

### U1. Stripe Connect fixtures and registry

Files: `data/stripe/openapi-connect.fixture.json`, `data/stripe/guides/*.md`, `data/content_engine/source_registry.json`, `scripts/build_stripe_connect_fixture.py` (optional fetch helper)

- Trim OpenAPI to Connect-relevant paths; include security schemes and components used by those paths.
- Four short guide fixtures with source_url frontmatter.
- Registry entries for openapi + guides.

### U2. Proof pipeline: mix, ingest, render content

Files: `relay_bench/content_engine/stripe_connect.py`, `pipelines/run_stripe_connect_proof.py`, `artifacts/content_engine/stripe/*`, `content/*.md`

- Reuse source_mix + ingest modules against Stripe paths.
- Render endpoint fact pages and `connect-quickstart.md`.
- Quickstart steps must mention platform secret key + Account + Account Link; no invented fields.

### U3. Connect eval harness

Files: `evals/run_connect_eval.py`, `evals/runs/.gitkeep`, `evals/latest.md`, `tests/test_stripe_connect.py`

- Mock mode: validate generated content contains required sections; emit pass gate.
- Live mode: POST Account + Account Link with test key; redact secrets in traces; gitleaks-safe output.

### U4. Wiring and docs

Files: `README.md`, `.gitignore` if needed, CI already covers unittest

## Verification Contract

```bash
python3 -m unittest discover -s tests
python3 pipelines/run_stripe_connect_proof.py
python3 evals/run_connect_eval.py --mode mock
PORT=8799 node portal/server.js  # /connect-quickstart
```

## Definition of Done

- [ ] Fixtures + registry present
- [ ] Proof pipeline writes reports + content pages
- [ ] Mock eval gate passes in CI
- [ ] Live mode documented (env `STRIPE_TEST_SECRET_KEY`)
- [ ] PR opened; unit + gitleaks green

## Appendix

Settled decisions from invoking LFG conversation:

| Decision | Class | Rejected | Reason |
|---|---|---|---|
| Stripe Connect as proof corpus | user-directed | Gateway-only proof | User: Yes /lfg stripe connect |
| Accounts + Account Links scope | user-approved | Full Stripe ingest | Prior recommendation accepted |
| Test-mode / mock-default CI | user-approved | Live CI always | Public repo safety |
