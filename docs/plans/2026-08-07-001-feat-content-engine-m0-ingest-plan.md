---
title: "Content Engine M0/M0.5/A1 — source mix, ingestion snapshot, portal from content/"
date: 2026-08-07
artifact_contract: ce-unified-plan/v1
artifact_readiness: implementation-ready
product_contract_source: legacy-requirements
execution: code
origin: build-spec-v2 (uploaded) + products/relay/integration-success-os-spec.md
---

# Content Engine M0/M0.5/A1 — source mix, ingestion snapshot, portal from content/

## Goal Capsule

Unblock build-spec v2 on the Integration Success OS branch by measuring where facts live (spec vs prose), standing up a clean-at-the-door ingestion store (`raw/` + `normalized/`), and replacing any hand-pasted serve path with a portal that reads only generated `content/*.md`.

Authority: uploaded `build-spec-v2` (replaces solo) > this plan > existing content-engine V0 honesty labels.

Stop conditions: do not call live sandbox APIs; do not write secrets/PAN; do not invent Fern/Speakeasy; do not auto-publish to main; do not claim real Tempo/Harbor.

## Product Contract

### Summary

Build-spec v2 keeps the Integration Success OS lane and adds a content engine with human approval plus tempo evals. This plan ships only the first week slice: Milestone 0 (source mix), Milestone 0.5 (ingestion snapshot), and A1 adapted to this repo (thin portal + CI). Later lanes (A2–A4, B1–B3) stay out of scope.

### Problem Frame

`cybersource-docs/` already holds ~360 llms.txt docs and the content engine already snapshots a few fixtures, but there is no durable source-mix decision, no immutable `raw/<date>/` + schema-gated `normalized/` store that serve layers must respect, and no portal that reads generated `content/*.md` (the v2-named `lib/quickstart-data.js` does not exist here — A1 must create the honest serve path rather than delete a missing file).

### Requirements

- R1. Produce `artifacts/content_engine/source-mix-report.md` classifying sampled guides/pages by fraction of facts regenerable from the OpenAPI fixture vs prose-only, with an overall split and the ten prose-only sections that matter most for a first integration.
- R2. Ingest docs into immutable `raw/<date>/` stamped with source URL + fetch date; never edit raw after write.
- R3. Extract only schema-matching claims into `normalized/` (quickstart steps, endpoint facts, error cases, prose claims with source pointer); drop non-matching content with a logged reason.
- R4. Emit `artifacts/content_engine/ingestion-report.md` (docs fetched, claims extracted, drop log).
- R5. Portal (and later MCP/evals) may read only `normalized/` and `content/`, never `raw/` or hand-pasted JS data modules.
- R6. Thin `portal/` serves `content/*.md` with real markdown rendering and an honest empty state when content is absent.
- R7. CI fails closed on gitleaks findings, raw markdown leak patterns in rendered HTML, and broken local content links.
- R8. Prefer offline replay from the existing `cybersource-docs/` corpus so unittest stays network-free; optional network fetch remains behind an explicit flag.

### Scope Boundaries

In scope: M0 report, M0.5 ingestion pipeline + report, A1 portal + content seed + CI.

Out of scope: A2 fact renderer PR loop, A3 humanizer, A4 nightly, B1–B3 tempo evals, GitHub Pages, company-scale risk tiers.

### Actors and Flows

- Developer/operator runs local pipelines and reviews reports.
- Portal serves approved markdown from `content/`.
- Future MCP/eval agents (Lane B) will read the same `normalized/` + `content/` contract.

### Acceptance Examples

- AE1. Opening `source-mix-report.md` shows a per-guide table, overall % split, and ten ranked prose-only sections.
- AE2. Running the ingestion pipeline without network populates `raw/<date>/` and `normalized/` and writes `ingestion-report.md` with a non-empty drop log.
- AE3. With empty `content/`, portal shows an empty state (no fake Auth Setup page). With a sample md file, portal renders it as HTML.
- AE4. `python3 -m unittest discover -s tests` passes; CI workflow files exist for gitleaks + content checks.

## Planning Contract

### Key Technical Decisions

- KTD1. Adapt A1 to this repo: create `portal/server.js` + `content/` instead of deleting nonexistent `lib/quickstart-data.js`.
  Rejected: Block LFG until a different portal branch appears.
  Reason: Files absent after search of local workspace and Poornimajagannath GitHub; headless LFG must ship the serve contract the spec requires.

- KTD2. Default ingestion is offline from `cybersource-docs/` (+ local OpenAPI fixture); `--fetch` may hit llms.txt when explicitly requested.
  Rejected: Always network-fetch in CI/tests.
  Reason: Repo README honesty: credential-free / network-free unittest proof.

- KTD3. Reuse content-engine schema types and extract heuristics; write normalized claims as JSON under `normalized/` with `source_pointer` back to `raw/<date>/...`.
  Rejected: New parallel schema language.
  Reason: Existing `relay_bench/content_engine/schemas.py` already models quickstart units and snapshots.

- KTD4. Cap M0 sampling to OpenAPI fixture ops + a stratified sample of cybersource-docs (auth/quickstart/payments/index-like) so the report finishes offline and stays reviewable.
  Rejected: Score all 360 docs line-by-line by hand.
  Reason: Decision rule needs a directional split, not exhaustive labeling.

- KTD5. session-settled: Build-spec v2 replaces the solo docs-autopilot as the product goal for this lane; solo `docs-autopilot` repo remains a separate personal scaffold and is not the implementation target of this PR.

### Assumptions

- A1. `data/content_engine/specs/cybersource-payments-core.openapi.json` is the authoritative local OpenAPI for M0 scoring.
- A2. Existing `cybersource-docs/` files are acceptable evidence for `raw/` when stamped with reconstructed source URLs from filename/index conventions.
- A3. Portal may be Node stdlib HTTP (no framework) to keep deps light.

### Technical Design

```text
cybersource-docs/ (+ optional llms fetch)
  -> raw/<YYYY-MM-DD>/... + meta.json (immutable)
  -> schema extract -> normalized/*.json (+ drop log)
  -> (later A2) content/*.md
  -> portal/server.js serves content/ only
```

M0 is a read-only analyzer writing a report artifact.
M0.5 is a pipeline script + library module + tests.
A1 is portal + sample content empty-state + GitHub Actions checks.

### Sequencing

U1 (source mix) can run before or after U2; U3 portal depends on `content/` directory existing (may be empty). CI lands with U3.

## Implementation Units

### U1. Source-mix inventory and report

Files: `pipelines/run_source_mix.py`, `relay_bench/content_engine/source_mix.py`, `tests/test_source_mix.py`, `artifacts/content_engine/source-mix-report.md`

- Score each sampled page: share of endpoint/auth/field/error facts that appear in OpenAPI vs prose-only (business rules, sequencing, gotchas).
- Emit markdown table per guide + overall split + top 10 prose-only sections for first integration.
- Test: fixture markdown + tiny OpenAPI produce deterministic percentages and include the top-10 section.

### U2. Ingestion snapshot (raw + normalized)

Files: `pipelines/run_ingestion_snapshot.py`, `relay_bench/content_engine/ingest.py`, `tests/test_ingest.py`, `artifacts/content_engine/ingestion-report.md`, `raw/` (generated), `normalized/` (generated)

- Offline default: stamp-copy from `cybersource-docs/` into `raw/<date>/` with `source_url` + `fetched_at`.
- Extract schema-matching claims only; log drops (index pages, revision histories, unmatched blobs).
- Refuse to modify existing raw files (second run uses new date dir or skips unchanged hashes).
- Test: temp corpus produces raw meta, normalized claims with pointers, and drop log entries; portal/MCP read paths documented to exclude raw.

### U3. Portal from content/ + fail-closed CI

Files: `portal/server.js`, `portal/package.json`, `content/.gitkeep`, `content/README.md`, `.github/workflows/content-ci.yml`, `scripts/check_content_render.py`, `tests/test_portal_contract.py`

- Serve `content/*.md` as HTML; empty dir → honest empty state (no Auth Setup fiction).
- CI: gitleaks, render check failing on leftover ` ``` ` / raw `#` leak patterns in HTML, local link check across content.
- Test: empty content contract; sample md renders without raw fence leaks.

## Verification Contract

```bash
python3 -m unittest discover -s tests
python3 pipelines/run_source_mix.py
python3 pipelines/run_ingestion_snapshot.py
node portal/server.js &  # smoke: curl localhost shows empty or content
```

Quality gates: no network in default unittest path; gitleaks workflow present; reports exist under `artifacts/content_engine/`.

## Definition of Done

- [ ] U1 report exists and documents overall split + top 10 prose-only sections
- [ ] U2 ingestion-report exists; raw immutable; normalized claims have source pointers; drops logged
- [ ] U3 portal empty-state + content render; CI workflow for gitleaks/link/md-leak
- [ ] All unit tests green
- [ ] PR opened from `cursor/content-engine-m0-ingest-0af3` (no direct main writes)

## Appendix

Settled decisions carried from the invoking LFG conversation:

| Decision | Class | Rejected | Reason |
|---|---|---|---|
| Execute build-spec v2 (not solo) | user-directed | Continue solo docs-autopilot as primary | Uploaded v2 says it replaces solo |
| Work on Integration Success OS / Relay bench | user-directed | Greenfield unrelated repo | Spec keeps that branch |
| Ship M0 + M0.5 + A1 first | user-directed | Jump to nightly/evals | Spec order of work |
| Adapt A1 when portal files missing | pipeline default | Block waiting for missing branch | Files not found after search |
