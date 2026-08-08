# L2 Required Fields augment — shipped

**Status: MERGED** with the derivation contract stated in
`content_bench/content_engine/api_reference.py`.

## Contract

Recover fields only from:

1. `api_fields_link` — markdown-link DL term (usually into api-fields)
2. `required_fields_section` — plain DL term under a same-document Required Fields heading
3. `sibling_req_fields_page` — `{op}-req-fields` sibling page joined by operation anchor

If none exist → leave `required_fields` empty and keep the soft gap.
**Never** infer required-ness from REST Example JSON keys.

Every recovered field carries `derivation_source` set to one of the three.

## Result (product roots, 176 matched Endpoint sections)

| Metric | Before | After |
| --- | ---: | ---: |
| Missing Required Fields | 57 | **30** |
| Matched with Required Fields | (119) | **146** |
| Missing REST Example | 17 | 17 (unchanged) |
| Missing both | 16 | **10** |

Field tags this run: `api_fields_link` + `required_fields_section` (sibling
join available via `load_sibling_req_field_pages` for child-guide ingest).

## Gap-report headline cleanup

`artifacts/content_engine/boarding/gap-report.md` headline 1 now reads
**215/278** and points at `composition-report.json` → `sequence_totals.ratio`
/ `outcome_missing` flags. Stale 222/277 and 220/257 are marked superseded.
