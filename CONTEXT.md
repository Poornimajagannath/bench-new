# CONTEXT.md — ubiquitous language

Domain vocabulary for this repo. Use these terms exactly, in code, reports,
PRs, and conversation. If a new concept earns a name, add it here in the same
PR that introduces it. Architecture invariants live in
`docs/ARCHITECTURE-DECISIONS.md`; this file only names things.

## Corpus and fetch

**Family** — one documentation product tree on the vendor site, rooted at its
own table of contents. Example: Boarding REST API, Boarding Business Center,
Boarding Template Management.

**Product root** — the family mega-guide markdown file at the guide path
(e.g. `…/boarding/developer/all/rest/boarding.md`). Canonical verbatim
corpus source. Derived from docs.md intro links by promoting the guide
directory to `{guide}.md` (the family name repeated when that directory
matches the family). Split into addressable sections by heading `{#anchor}`s.

**TOC** — the family's own HTML navigation tree on the vendor site. A
cross-check against the product root: any TOC page whose content does not
appear in the root is a real gap. Not the coverage denominator.

**Denominator** — the count a coverage claim is measured against. Always
computed at runtime from the source of truth (the **product root** for docs
corpus coverage; the registered spec for API operations). Never hard-coded,
never taken from `llms.txt`. Every reported number arrives with its
denominator and its source.

**llms.txt hint** — the vendor's agent-discovery file. A discovery aid only.
Demonstrated incomplete: 27 boarding URLs listed vs 236 pages in the family
TOCs.

**Verbatim fetch** — a page fetched byte-for-byte with a plain HTTP client
(trailing newline normalized only). The only thing allowed into `raw/`.

**Paraphrase** — any machine summary or rewording of a source page. Never
enters `raw/`. Marked `fidelity: SUSPECT_PARAPHRASE` when found in delivered
corpora.

**HTML fallback** — HTML converted to markdown because the `.md` endpoint is
broken (for example, returns HTTP 500). Marked in-band with an
`html-fallback` comment. A last resort, not a default.

## Triage and census

**Census** — the pre-ingestion pass that classifies every corpus file by kind
and produces the quarantine list. Implementation: `corpus_census.py`.

**Kind** — a census label: `how_to_guide`, `api_reference`, `index_navigation`,
`release_note`, `legal`, `marketing`, `other`.

**Quarantine** — the policy decision to exclude kinds (release notes, legal,
index/navigation) from ingestion. Recorded in a versioned policy file plus a
generated quarantine list. A quarantine skip is not a shell.

**Shell** — a navigation stub with no extractable facts: link lists, jumplists,
"see these topics" pages. Length alone never makes a page a shell. Every drop
labeled shell must carry the file's byte size and its first heading.

**Constraint page** — a page whose value is limits and obligations: TTLs,
validity windows, rate and reuse limits, PCI/compliance statements,
mandatory-header requirements, device-side or end-to-end encryption. The class
that keeps getting lost, and exactly what an integrating developer needs.
Constraint signals make a page substantive regardless of size.

**Triage** — the one shared definition of constraint page, shell, first
heading, and sentence split. Implementation: `triage.py`. Census and ingest
both import it; a test identity-checks that they do. They must never
re-implement it locally — census and ingest disagreeing is how the
transient-token TTL fact vanished.

## Ingestion and claims

**Ingestion** — the pass that stamps sources into `raw/<date>/`, extracts
claims, and writes `normalized/<date>.claims.json` plus an ingestion report.

**Claim** — one extracted fact with a schema, a source pointer, and stable id.
Schemas: `quickstart_step`, `endpoint_fact`, `error_case`, `prose_claim`,
`field_table`.

**API-reference pattern** — Endpoint + Required Fields + REST Example →
`endpoint_fact` (not `quickstart_step`). Soft gaps (matched Endpoint with no
Required Fields and/or no REST Example) are gap-report findings: a developer
can see the verb+URL and still cannot call it.

**Source noise → metadata** — brace anchors (`{#id}`), image refs, and line
ranges live on claim `extras` with a working `deep_link`. Generated pages
must never contain raw `{#…}`.

**Claim kind** — the constraint subtype on a prose claim: `ttl_or_validity`,
`ttl_and_reuse`, `reuse_or_rate_limit`, `pci_compliance`, `mandatory_header`,
`device_encryption`, `id_format_rule`, `hierarchy_limit`, `status_transition`,
`prerequisite`, `guidance`, `constraint`. The boarding classes (ID format,
hierarchy, status, prerequisite) are the family's own version of the
constraint-page class.

**Mega-guide** — a family-root compendium file that concatenates its child
pages (e.g. `boarding-user.md.md`). In composition the child page always wins
on duplicate claim text (more specific source pointer); mega-guide claims with
no child match are **residuals** — reported, never merged, because each is
either unique content or a failed/quarantined child ingest.

**Drop** — a source that produced no claims, recorded with a reason
(`shell`, `no_schema_match`, `quarantine_policy`, …). Failures are kept, not
replaced.

**Human-check sample** — ten drops per ingestion run listed with bytes and
first heading for a human to confirm shell vs missed claim. Replaces
labels-by-filename.

**Recall** — of pages that previously produced zero claims, how many now yield
claims. Always reported against a named frozen baseline.

## Serving and evals

**raw/** — immutable verbatim evidence. Never served, never edited.

**normalized/** — extracted claims. Readable by serve layers.

**content/** — generated pages. The only thing published, and only through a
human-approved PR. Fix the source and regenerate; never hand-edit.

**Gap report** — first-class deliverable listing workflows the prose mentions
but never fully specifies. Ships beside the generated pages, not as a footnote.

**Task eval** — deterministic; gates PRs.

**Parity eval** — live comparison; runs nightly as evidence; never gates.

## Repos

**content-bench** — the engine's home (public). Engine fixes port back the
same day.

**bench-new / visa-relay-bench** — the private lane that configures the
engine. Private corpus, traces, and drop logs never move to the public repo.
