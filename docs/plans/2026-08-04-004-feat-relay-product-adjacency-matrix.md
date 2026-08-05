# Plan: Relay Product Adjacency Opportunity Matrix

**ID:** 2026-08-04-004
**Status:** Planned (product strategy only)
**Scope:** Adjacent product opportunities for the Relay content/context engine
**Related plans:**

- `2026-08-04-001` — Content Engine V0
- `2026-08-04-002` — Specs-to-Docs V0
- `2026-08-04-003` — Service decomposition

## Honest label

This is a product opportunity plan. It does **not** implement release notes, MCP servers, brand portals, or production Relay services in `bench-new`.

Local bench work remains the place to prove shared schemas, lineage, and eval-gated promotion before productizing adjacencies.

## Core pattern (shared by every adjacency)

```text
structured source truth
-> ingest / normalize
-> extract typed objects
-> evaluate / promote
-> serve branded, agent-ready experiences
```

If a candidate product does not reuse that pattern, it is probably not a Relay adjacency.

## Recommended expansion sequence

```text
docs / quickstarts
-> release notes / product notes
-> MCP tooling
-> multi-brand portal specialization
```

Rationale: each step strengthens the same knowledge graph, schemas, evals, and brand rules instead of spawning separate stacks.

## Product opportunity matrix

Effort / leverage / risk are relative to current Relay design maturity in this chat (`bench-new` local proofs + SDD).

Scale: **L** = low, **M** = medium, **H** = high.

| Adjacent product | Effort | Leverage | Risk | Why Relay fits | Main reuse | Dependencies / blockers |
|---|---|---|---|---|---|---|
| Developer portal docs + wiki | M | H | L | Same compiled graph already aimed at docs/quickstarts | Intake, extraction, promote, serve | Content Engine V0 exists locally; live fetch/publish later |
| Onboarding quickstarts | M | H | M | Connects API truth to developer success via sequenced units | `quickstart_unit`, workflow contracts, evals | Needs workflow + contract alignment; avoid OpenAPI-only quickstarts |
| API reference generation | M | H | M | OpenAPI is structured source truth for freshness | Contract Compiler, reconciliation, contract checks | Specs-to-Docs V0 plan exists; exceptions/model drift need policy |
| Release / product notes | M | H | M | Change events → audience-specific notes at scale | Change Compiler, notes composer, validation | Needs GitHub/release signal model; template discipline |
| MCP tools + agent context | M | H | M | Typed objects map cleanly to tools/context packs | Serving layer, context packs, provenance | Must expose small high-value tools, not one giant search |
| White-label portal content | H | H | H | Late brand render + entitlement checks across domains | Brand overlay, validation, publishing | Multi-domain naming/entitlements; brand-leak risk is high |
| API governance / drift checks | M | M | M | Contract graph validates docs against source truth | Specs-to-docs, reconciliation | Needs clear exception model for intentional divergence |
| Onboarding assistant (Hermes/PAIGE consumer) | H | H | H | Uses quickstart/workflow units for guided setup | Quickstarts, evals, MCP/context packs | Assistant runtime is out of Relay scope; Relay supplies context only |

### Priority call

**Build next (platform leverage):**

1. Docs + quickstarts (already in flight locally)
2. API reference / specs-to-docs
3. Release intelligence (notes)
4. MCP tool surface
5. Multi-brand specialization

**Do not productize first:**

- Generalized long-term user memory
- Chat UI / assistant runtime as part of Relay
- CMS replacement debates before the compiler graph is trusted

## Three product bets (not just features)

### 1. Release Intelligence

**Buyer:** PMs, support, partner ops
**Job:** Turn PRs/spec diffs/changelogs/rollout metadata into canonical change objects and audience-specific notes.
**Relay domains:** Change Compiler + Trust and Quality + Delivery
**Why now:** High reuse of change events; clear pain vs manual portal-by-portal notes.

### 2. Developer Onboarding

**Buyer:** ISVs / integrators / DevEx
**Job:** Assemble trusted quickstarts and workflow contracts that agents and portals can both use.
**Relay domains:** Knowledge Compiler + Contract Compiler + Eval gates
**Why now:** Directly tied to integration success; already partially proven in `bench-new`.

### 3. Multi-brand Content Platform

**Buyer:** Portal / brand owners (Visa, CyberSource, shared)
**Job:** One factual graph, many branded renders with entitlement and domain checks.
**Relay domains:** Delivery Layer (Brand Overlay + Publishing + Feedback)
**Why later than 1–2:** Highest operational risk (brand leak, wrong product enablement) until facts/evals are solid.

## MCP shape (starting toolset)

Prefer a small typed toolset over one giant search tool:

| Tool | Backed by |
|------|-----------|
| `search_relay_context` | Serving index over trusted objects |
| `get_doc` | `relay_document` |
| `get_quickstart` | `quickstart_unit` bundles |
| `get_api_reference` | `api_reference_unit` |
| `get_release_notes` | `release_note` / change events |
| `get_brand_view` | Brand overlay render of a trusted artifact |
| `diff_contract` | Contract Intelligence diffs |
| `list_supported_products` | Source registry + entitlement metadata |
| `create_context_pack` | Existing context-pack compiler pattern |
| `get_evidence_for_claim` | Provenance / evidence quotes / lineage |

MCP should consume the **trusted Relay graph**, not raw snapshots.

## Fit test for any new adjacency

Approve a candidate only if all are true:

1. Has structured upstream truth (docs, specs, code, releases).
2. Needs typed intermediate objects, not only retrieved text.
3. Benefits from eval-gated promotion.
4. Can share the same graph with docs/quickstarts/notes.
5. Can keep brand rendering late.
6. Does not require Relay to become the chat runtime.

## Mapping to current bench work

| Adjacency | Local proof status |
|-----------|--------------------|
| Docs / quickstarts | Content Engine V0 prototype |
| Workflow contracts / agent eval preview | Contract compiler + verifier |
| API reference / specs-to-docs | Planned (`002`) |
| Service boundaries for productization | Planned (`003`) |
| Release notes / brand overlay / MCP server | Not started |

## Non-goals for this plan PR

- No MCP server implementation
- No release-notes pipeline
- No brand overlay engine
- No production portal wiring
- No new runtime dependencies

## Recommended decision

Treat Relay as the shared substrate for **docs, onboarding, release intelligence, MCP context, and multi-brand delivery**, sequenced as:

1. prove compile + promote locally
2. add specs-to-docs
3. add change/notes lane
4. expose MCP tools on trusted objects
5. specialize brand delivery last

This maximizes reuse of one knowledge graph and avoids fragmenting into separate “docs bot,” “notes bot,” and “portal CMS” stacks.
