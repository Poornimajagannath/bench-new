# L2 proposals — disposition

## Drafts from the local-Qwen run (the cut-off table)

| ID | Status | Proposal |
| --- | --- | --- |
| L2-endpoint-required-fields-augment | **CLEARED → shipped** | Capture Required Fields next to matched endpoints (57/176 soft gap). |
| L2-boarding-step-outcome-gap-marker | **APPROVED → merged** | Flag steps with no stated outcome as `outcome_missing` (not invent results). |
| L2-prerequisite-prose-extractor | discarded | Stale — L1 already expanded `_PREREQUISITE_PATTERN`. |

---

## Outcome gap marker — APPROVED

**Denominator (confirm before quoting):**

| Figure | Source | Status |
| --- | --- | --- |
| 222/277 | `gap-report.md` opening headline | **Stale** — LLM cited this |
| 220/257 | Wave 2 closeout / pre-API UI-only | Superseded |
| **215/278** | `gap-report-wave-rerun.md` / `wave2-boarding-report.md` | Last measured before this flag |
| **Live** | `composition-report.json` → `sequence_totals.ratio` | Recounted each compose from `outcome_missing: true` flags |

Implementation: every sequence step in `content/boarding/workflows/*.md` now carries
`outcome_missing: true|false`. Composition report exposes
`sequence_totals.outcome_missing` and states the denominator source. Do not
quote 222/277.

---

## Required Fields augment — CLEARED and shipped

See `l2-required-fields-shipped.md` for post-merge counts (57 → 30 missing RF).

### Derivation answer (pre-clear)

**Question:** where would the fields come from for the 57 soft gaps?

**Answer — investigated against product-root + child guides:**

1. **Many of the 57 are not “absent from source.”** Example: boarding
   `POST /boarding/v1/registrations` (“Add a Structural Organization…”) is
   flagged `missing_required_fields`, but the mega-guide contains a full
   setext section `Required Fields for Boarding a Structural Organization`
   with definition-list terms (`organizationInformation.type`, etc.), and a
   sibling TOC page `…-req-fields.md.md` carries the same list.

2. **Why the soft gap fires anyway:** `_parse_required_fields` only accepts
   markdown-link DL terms (`[field](api-fields-url)`). Plain terms like
   `organizationInformation.type` followed by `:` produce **zero parsed
   fields**, so `missing_required_fields=True` even when the section exists.
   That is an extractor attachment/parse gap, not a missing-doc gap.

3. **Sibling pages:** of 13 boarding RF soft gaps, **7** already have a
   `*-req-fields*` child guide. Legitimate capture = join by operation
   anchor / follow the Required Fields heading already in source.

4. **Truly empty endpoints** (e.g. some OMS retrieve ops with no RF section
   and no sibling page): correct behavior is **refuse / keep the gap**, not
   guess.

5. **Example JSON is not an authority.** A key appearing in a REST Example
   request does **not** make it required. Inferring required-ness from
   examples would invent obligations. The no-invention prose guard would not
   catch that.

**Scan of all 57 soft gaps against product roots:**

| Bucket | Count |
| --- | ---: |
| Soft gaps flagged missing RF | 57 |
| Have a nearby `Required Fields` heading in product root | 21 |
| Of those, plain DL terms (name + `:`) — current parser yields 0 | 17 |
| Of those, link-style `[field](url)` DL terms | 0 |
| No RF heading found near the operation in product root | 36 |

So ~21/57 are **extractor false gaps** (section exists; parser too narrow).
The remaining ~36 need sibling-page join or stay as real gaps — still not
example-JSON inference.

**Condition to clear this proposal later:**

- State derivation source per field: `required_fields_section` (same-page
  heading) or `sibling_req_fields_page` (anchor-joined child) or
  `api_fields_link` (explicit link target).
- Mark each field with that source in `extras`.
- If none of those exist for an endpoint, leave `required_fields` empty and
  keep the soft-gap finding — never populate from example JSON keys.

Until that contract is in the implementation plan, **do not merge** the
required-fields augment.
