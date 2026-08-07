# Boarding corpus fidelity check

**Rule:** a paraphrase must never enter `raw/` — raw is verbatim evidence of what
the source said. A machine summary of a doc is not that.

## Context

The architect's separately-delivered `boarding-docs.zip` (80 pages) carries at
least 4 files marked `fidelity: SUSPECT_PARAPHRASE` — its fetcher summarizes.
That zip is not ingested here. The in-repo corpus was fetched independently by
`pipelines/fetch_boarding_toc.py` using a plain HTTP client (urllib) with no
summarization step: `.md` responses are written byte-for-byte (trailing newline
normalized only).

## Verification (this run)

| Check | Result |
| --- | --- |
| Corpus files (denominator: site TOC, 3 families) | 236 |
| Files with `SUSPECT_PARAPHRASE` / `fidelity:` markers | **0** |
| Files from HTML→markdown fallback in final corpus | **0** (all `ok_md`) |
| 10% spot-check: re-fetch + byte-compare vs disk | **23/23 verbatim, no diffs** |

Sample selection: seeded random (`seed=80`) over the 236 `ok_md` fetch results;
compare `disk.rstrip("\n") == remote.rstrip("\n")`.

## Count reconciliation

The zip reports 80 pages for "the family"; this corpus holds 236 across three
families (Boarding REST 110, Business Center 98, Template Management 28). The
census denominator statement must name its source: **site HTML TOC per family**
(`toc-fetch-report.md`). If the 80-page zip covers a single family slice, its
number is not in conflict — but ingestion uses this verbatim corpus, not the zip.
