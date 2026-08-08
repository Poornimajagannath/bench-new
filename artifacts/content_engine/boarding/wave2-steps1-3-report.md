# Wave 2 boarding — steps 1–3 report (STOP point; no pages generated)

## Root cause, confirmed

Census read the corpus directory (`data/products/boarding/guides`, 236 files,
denominator: files on disk from the TOC fetch). The prior boarding ingestion
run was driven by the old 9-source slice recorded in `registry/boarding.json`
(the pre-TOC thin fetch): 9 files → 6 quarantined → **3 landing pages
ingested**, 645 claims, while 179 census-eligible docs were never read.
Census and ingest shared definitions (triage.py) but not an input.

## Step 1 — one corpus definition

**Choice: ingestion consumes the census eligible list directly**
(`select_ingest_sources_from_census`, `--census-report` flag).

Why this way and not registry-from-census: the census report is already the
decision record — kind, quarantine policy, and eligibility in one generated
artifact. Generating the registry from it would create a second ledger holding
the same roster, which is exactly the two-ledgers drift (registry said 9,
directory said 236) that caused this defect. The registry keeps its real job:
source metadata (canonical URLs, trust levels), not the corpus roster.

**Guard, in the spirit of the triage identity test:** `CorpusMismatchError` is
raised when the census `eligible_count` differs from the resolved ingestion
input count (e.g. corpus changed after the census). Tests:
`tests/test_corpus_parity.py` — eligible set == ingest roster (happy path),
mismatch fails loudly, quarantined docs appear as `quarantine_policy` drops.

## Step 2 — re-ingest, every number with denominator and source

Run: stamp `2026-08-08-boarding`, census `census-report.json`
(generated this run from the 236-file TOC corpus).

| Number | Value | Denominator | Source |
| --- | ---: | --- | --- |
| Corpus files | 236 | site HTML TOC, 3 families | `toc-fetch-report.json` |
| Census eligible | 182 | 236 corpus files | `census-report.json` |
| Quarantined (policy) | 54 | 236 corpus files | `census-report.json` (kinds: index_navigation) |
| **Docs ingested** | **182** | 182 eligible | `ingestion-report.json` (`ingest_input_count`, guard passed) |
| Claims extracted | **1160** | 182 docs | `normalized/2026-08-08-boarding.claims.json` |
| — quickstart_step | 961 | 1160 claims | same |
| — prose_claim | 134 | 1160 claims | same |
| — error_case | 65 | 1160 claims | same |
| — endpoint_fact | 0 | 1160 claims | same (no OpenAPI registered for boarding; endpoints in prose are full-URL style the extractor does not treat as `VERB /path`) |
| Docs yielding ≥1 claim | 105 | 182 ingested | claims file, by source_pointer |
| Docs ingested, zero claims (`no_schema_match`) | 77 | 182 ingested | `ingestion-report.json` drop log (kept, not replaced) |
| Claims per claiming doc | median 4, max 416 | 105 docs | claims file |

**Recall vs named baseline** (prior boarding run `2026-08-07-boarding`,
3 docs with claims, 645 claims): **102 newly claiming docs** (105 now vs 3
then; the 3 remain). The payments recall baseline is now auto-skipped for
boarding runs — a recall number against the wrong product's baseline is worse
than no number (`--recall-baseline` names the file explicitly).

**Honest notes, kept in the report:**
1. The 77 zero-claim eligible docs are dominated by template-matrix reference
   tables (e.g. "ACH Templates", "Gift Card Templates" — pure field tables).
   They carry facts but no current schema extracts table rows. That is a
   schema gap, not shells; their bytes + first heading are in the drop log.
2. The two family mega-guides (`boarding-user`, 416 claims; `boarding` REST,
   132) duplicate their child pages' content — the same step text appears
   from both the mega-guide and the child page. Composition (step 4) must
   dedupe by text hash or prefer child pages, or workflow pages will show
   doubled steps.

## Step 3 — quickstart_step quality check

Sampled 10 of 1065 steps (seed 2) from the first full-corpus run, each printed
with source pointer and source line (transcript in run log):

- **9/10 real procedural steps** — Business Center click-throughs
  ("Enter a unique name for the new card-processing template, and then click
  **Next**."), genuinely numbered instructions.
- **1/10 navigation** — `5. Configure products. See [Product Enablement …](…)`
  — a numbered cross-reference extracted as a step.
- The audit also exposed **claim-id collisions**: `doc_stem:step:{n}` is not
  unique when one doc holds many procedures (the sample's title/line mismatch).

**Fixes applied before any page generation:**
1. Numbered `See [link]` lines and link-only lines are no longer steps.
2. Step ids carry a per-occurrence hash (`:step:{n}:{sha8}`).
3. Repeated identical error snippets dedupe to one claim per doc.
   Tests: `test_navigation_lines_are_not_steps`,
   `test_step_ids_unique_across_sections`, `test_claim_ids_unique_within_doc`.

**Before / after:**

| Metric | Before fix | After fix |
| --- | ---: | ---: |
| quickstart_step (182-doc corpus) | 1065 | **961** (−104 nav/link lines) |
| quickstart_step (old 3-doc run, for scale) | 550 | — |
| error_case | 68 | 65 (dedupe) |
| Fresh 10-sample nav lines | 1/10 | **0/10** |
| Claim ids unique | no | **yes** |

## STOP

Pages are not generated. Step 4 (workflow pages with actor / precondition /
action / expected outcome / failure modes, humanizer with fact-hash guard,
gap-report update) waits on review of this report. The composition must
address honest-note 2 (mega-guide dedupe) as its first design decision.
