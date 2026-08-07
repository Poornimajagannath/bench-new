# Wave 2 boarding — gap report

## Headline finding (production docs site)

**CyberSource `llms.txt` — the file that exists so AI agents can discover the docs — does not expose a distinct Merchant Boarding API family under `/merchant-boarding/`, and that path’s machine-readable `.md` endpoint returns HTTP 500 while the HTML variant redirects into the Business Center boarding guide.**

Evidence (live probe, this run):

| Probe | Result |
| --- | --- |
| `…/merchant-boarding/developer/all/rest/merchant-boarding.md` | **HTTP 500** (`Error`) |
| `…/merchant-boarding/developer/all/rest/merchant-boarding.html` | **200**, redirects to `…/boarding/user/all/ebc/boarding-user/boarding-intro-overview.html` |
| `merchant-boarding` listed in `llms.txt` | **No** |
| Programmatic boarding surface that *does* exist | `/docs/cybs/en-us/boarding/developer/all/rest/boarding/` (site TOC) |

Any agent (Cursor, Claude, a customer bot) that relies on the site’s own agent-readiness surface cannot discover or read boarding through the `/merchant-boarding/` alias at all. The working surface is the Boarding REST family under `/boarding/…`, which `llms.txt` only partially indexes.

This finding is about the **production docs site**, found by the prototype doing ordinary corpus work. It belongs at the top of any internal briefing on Wave 2.

---

## Denominator honesty

| Source | Count | Role |
| --- | ---: | --- |
| Prior local corpus (llms/filename slice) | **9** | Thin fetch — looked like a thin product |
| `llms.txt` boarding-related `.md` URLs | **27** | Incomplete discovery aid |
| **Site HTML TOC (denominator)** | **236** | Source of truth for this census |
| Fetched OK | **236** | 100% of TOC |
| Via `.md` | **236** | |
| Via HTML→markdown fallback | **0** | (fallback reserved for `.md` 500s such as merchant-boarding) |
| Usable (≥40 bytes) | **236** | |
| Census eligible after quarantine | **182** | |
| Quarantined (`index_navigation` etc.) | **54** | |

**Invariant (extends coverage rule):** a coverage denominator must come from the source of truth. `llms.txt` is not one — the site’s own navigation/TOC tree is. Every future family census must state where its denominator came from.

Denominator for this report: **site HTML TOC** of Boarding REST, Boarding Business Center, and Boarding Template Management (`pipelines/fetch_boarding_toc.py`).

---

## What the thin “9 docs / 6 shells” number really was

The earlier boarding census (9 files, 6 quarantined as index) measured a **thin fetch**, not a thin product. Expanding the fetch from the site TOC lifts the corpus from 9 → **236** pages and eligible guides from 3 → **182**.

The Merchant Boarding API / Connect-equivalent surface (create/search orgs, hierarchies, product templates, status changes, PECS/BRS enablement) lives under the Boarding REST TOC and is now in-corpus.

---

## Family breakdown (TOC → fetch → usable)

| Family | TOC topics | Fetched | Usable |
| --- | ---: | ---: | ---: |
| Boarding REST API | 110 | 110 | 110 |
| Boarding Business Center | 98 | 98 | 98 |
| Boarding Template Management | 28 | 28 | 28 |
| **Total** | **236** | **236** | **236** |

Artifacts: `toc-fetch-report.md`, `census-report.md`, `quarantine-list.md`.

---

## Additions from composition (step 4)

6. **Field semantics documented only in the mega-guide.** `boardingFlow`
   (`ENTERPRISE` creates one organization; `SMB` behavior), `mode` ("not
   currently supported"), and `configurable` (`true` for merchant orgs,
   `false` for transacting) are specified nowhere in the per-topic child
   pages — only in the family compendium. A partner reading topic pages never
   sees them; an agent deep-linking anchors cannot cite them.
7. **Expected outcomes are largely unstated.** Across the six composed
   workflows, 220 of 257 steps have no stated outcome ("what should I see if
   it worked") in the source prose — visible as explicit gaps in the
   generated pages.

## Next (not done in this pass)

- Boarding workflow schema + portal pages against the 182 eligible docs
- Specs-to-docs / gap matrix for partner onboarding (Connect analogue)
- File internal ticket: fix `merchant-boarding.md` 500 + add the family (or canonical redirect) to `llms.txt`
