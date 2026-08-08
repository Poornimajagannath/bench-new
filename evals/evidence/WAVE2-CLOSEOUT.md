# Wave 2 (boarding) — closeout

**Status: CLOSED** (template-matrix decision resolved below).

## Template-matrix decision (the named decision)

**Decision: add a `field_table` schema so the tables extract.** Not a dated
exclusion — these pages are the product boarding template reference, how a
partner learns which products can be enabled and how they are configured.
Load-bearing content cannot be out of scope.

Implementation: one `field_table` claim per data row (field, value, table
heading as context; `#` and setext headings both carried). Tests in
`tests/test_field_table.py`.

## Result (denominator 190 census-eligible; source: ingestion-report.json / claims file)

| Metric | Before | After |
| --- | ---: | ---: |
| Zero-claim eligible docs | 68 / 190 | **48 / 190** |
| Docs yielding claims | 122 / 190 | **142 / 190** |
| Claims total | 1248 | **2360** |
| — field_table | 0 | **1112** |

Remaining 48 zero-claim docs (kept in the drop log with bytes + heading), by
shape: REST example pages whose facts are JSON code blocks, required-fields
stubs whose endpoint lines use the backticked full-URL style the
`endpoint_fact` extractor does not match, and diagram pages. That is the next
schema gap, recorded here — not silently dropped, not blocking closure.

## Wave 2 ledger

- Corpus: 236 pages from the site TOC (denominator source: family HTML TOC);
  llms.txt demoted to hint (27 vs 236).
- One corpus definition: census-eligible set drives ingestion;
  `CorpusMismatchError` + parity tests.
- Extraction: boarding constraint classes added (90/214 prose constraint-kind);
  nav-as-steps fixed; ids unique; field_table schema (this note).
- Pages: 6 workflow pages in `content/boarding/workflows/`, fact-hash guard
  pass, merged via PR #32 after human review.
- Gap report headlines: 220/257 steps lack stated outcomes; API boarding path
  has 24/257 procedural steps (create-merchant: 0); llms.txt/.md 500 defect.
