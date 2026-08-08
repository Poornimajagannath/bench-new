# Wave 2 boarding — step 4 report (pages composed; PR for human approval)

## The one-line answer to the prose question

Before this step: **18/134 prose claims were constraint-kind (13%), all
`ttl_or_validity` — the detector was near-blind on boarding's own constraint
class.** After adding the boarding classes (`id_format_rule`,
`hierarchy_limit`, `status_transition`, `prerequisite`) to the shared triage
detector — sentence-level *and* page-level, with tests: **90/214 constraint-kind
(42%)**: 38 prerequisite, 22 id_format_rule, 18 ttl_or_validity, 12
hierarchy_limit. The prose-primary path now sees the class it was built for.

Extending the page-level detector also un-quarantined 8 intro pages that carry
those constraints (census eligible 182 → **190** of 236; source:
census-report.json regenerated this run).

## Composition (all numbers with denominator + source)

| Number | Value | Denominator | Source |
| --- | ---: | --- | --- |
| Docs ingested | 190 | 190 census-eligible | ingestion-report.json (guard passed) |
| Claims | 1248 | 190 docs | normalized/2026-08-08-boarding.claims.json |
| — quickstart_step / prose / error | 969 / 214 / 65 | 1248 | same |
| Docs yielding claims | 122 | 190 | claims file |
| Zero-claim eligible docs | 68 | 190 | drop log (kept) |
| Claims used after prefer-child dedupe | 619 | 1248 | composition-report.json |
| Mega residuals | **19** | 1248 | composition-report.json |
| Pages generated | 6 | 6 workflows | content/boarding/workflows/ |
| Fact-hash guard | pass ×6 | 6 pages | compose_boarding_pages.py (humanize + assert_facts_unchanged) |

Pages: create-merchant-organization (31 steps), extend-hierarchy (33),
enable-configure-products (178), search-organizations (10),
change-organization-status (3), send-registration-email (2). Every step
carries actor / action / expected outcome (or a stated gap) and its claim id;
constraints and failure modes cite claim id + source pointer. Composition
reads `normalized/` only.

## Prefer-child dedupe (per ruling: no hash tie-breaks)

Child page always wins on matching normalized text. Residual analysis
(41 before the page-level detector fix, **19 after**):

- **~5 genuinely unique API facts that exist only in the mega-guide:**
  `boardingFlow` has two values `ENTERPRISE`/`SMB`; the `mode` field is *not
  currently supported*; `configurable` must be `true` for merchant orgs and
  `false` for transacting; `/registrations` is one-time (modifications via
  other services). These are constraint-grade facts with no child-page home —
  added to the gap report.
- **~14 step variants** (anchored `{#…}` texts and Business Center step
  phrasings) that differ slightly from child text — flagged for a child-ingest
  check, not merged.

**Census-kind verdict:** mega-guides are *not* pure aggregations (unique API
facts above), so no new census kind; residual reporting stays at composition,
as ruled.

## Standing items before Wave 2 closes (not blocked by this PR)

1. **Template-matrix decision (the 68 zero-claim docs, 36% of eligible):**
   named decision required — field-table schema so they extract, or a dated
   exclusion with reason. This is the product boarding template reference;
   load-bearing for partners. Not resolved in this PR.
2. Gap report updated with the mega-guide-only API facts (boardingFlow /
   mode / configurable) — prose that specifies field semantics in exactly one
   non-navigable place.
