# Developer corpus build report

Generated: 2026-08-08T06:14:26+00:00
Stamp date: `2026-08-07`

## Discovery (denominator)

Source: `llms.txt_derived_roots`

Corpus denominator is the deduped set of family-root paths derived from llms.txt subtopic URLs (plus docs.md supplements). Unfetchable roots remain in the denominator. Unfetchable reasons split derivation_miss (ours) from site_defect (theirs).

- llms.txt `.md` URLs: **475**
- llms.txt `.pdf` URLs: **0** (recorded unfetchable)
- Roots discovered (denominator): **212**
- From llms.txt: **212**
- docs.md-only supplements: **0**

## Derivation rule accuracy

Separate success rates for family-repeat vs guide-dir fallback.

| Rule | Discovered | Fetched OK | Unfetchable | Success rate |
|---|---:|---:|---:|---:|
| `already_root` | 47 | 45 | 2 | 95.7% |
| `family_repeat` | 19 | 17 | 2 | 89.5% |
| `guide_dir` | 146 | 70 | 76 | 47.9% |

## Unfetchable roots (split buckets)

404 on a constructed URL is **derivation_error** (ours). 500 on an exposed URL is **site_defect** (theirs). **empty_200** is its own diagnosis.

| Bucket | Count |
|---|---:|
| ours | 62 |
| theirs | 18 |

| Reason | Count |
|---|---:|
| `derivation_miss` | 21 |
| `empty_200` | 25 |
| `site_defect` | 10 |
| `unresolved_derivation` | 24 |

## Deep link spot check

Checked: **1** — anchors found: **1** / 1 — PASS

- `boarding` #boarding-intro-overview → ok (HTML 200)

## Fetch

- Roots fetched OK: **1** / 212 (source: `raw/2026-08-07/`)
- Total bytes: **268904**

## Per product

| Product | Root fetched | Bytes | Sections | Quarantined | Code blocks | TOC topics | TOC covered | TOC missed |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| boarding | yes | 268904 | 137 | 2 | 57 | 109 | 109 | 0 |

## TOC completeness

- Products checked: **1** / 1
- TOC topics: **109**
- Covered: **109** / 109
- Missed: **0**

## Sanitize

- Sections total: **137**
- Sections clean: **135** / 137
- Code blocks preserved: **57**

| Quarantine kind | Sections |
|---|---:|
| `about_guide_boilerplate` | 1 |
| `revision_history` | 1 |

## Source files

- Discovery: `artifacts/content_engine/corpus_build/discovery.json`
- Raw: `raw/2026-08-07/`
- Cleaned: `cleaned/2026-08-07/`
- Quarantine: `quarantine/2026-08-07/`
- TOC checkpoint: `artifacts/content_engine/corpus_build/toc-checkpoint/`
