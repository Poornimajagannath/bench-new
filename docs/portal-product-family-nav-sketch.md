# Portal product-family navigation — sketch (architect review)

**Status:** propose only. Do not implement until approved.  
**Constraint:** portal still serves only `content/*.md`; never `raw/`.

## Problem

Wave 1 left the portal as a flat slug list (`createPayment`, `getPayment`, …).  
Wave 2 adds boarding pages + a gap report. A flat list mixes product families and buries the boarding quickstart / gap deliverable.

## Proposal (one composition)

```
┌─────────────────────────────────────────────────────────────┐
│  Content portal                                             │
│  Serves generated pages only · never raw/                   │
├──────────────┬──────────────────────────────────────────────┤
│  Families    │  Payments                                    │
│              │                                              │
│  ● Payments  │  Quickstart (if present)                     │
│    Boarding  │  · First sandbox payment                     │
│              │                                              │
│              │  Reference                                   │
│              │  · createPayment                             │
│              │  · getPayment                                │
│              │  · … (ops from registry/payments.json)       │
│              │                                              │
│              │  Reports (Wave 1)                            │
│              │  · Source mix · Top drops (link out)         │
├──────────────┴──────────────────────────────────────────────┤
│  Switch family → Boarding                                   │
│                                                             │
│  Quickstart (step schema)                                   │
│  · Create registration → Track status → Activation          │
│                                                             │
│  Reference / workflow pages                                 │
│  · (generated boarding pages)                               │
│                                                             │
│  Gap report  ← first-class nav item, not a footer note      │
│  · boarding-gaps.md (one line per underspecified workflow)  │
└─────────────────────────────────────────────────────────────┘
```

## Rules

1. **Family = registry product** (`payments`, `boarding`, later …). Nav labels come from `registry/*.json` `product` keys that have ≥1 enabled source or ≥1 page tagged with that product.
2. **Page → family** via frontmatter or filename prefix convention decided at implement time; default: pages declare `product:` in YAML frontmatter written by the generator (not hand-edited).
3. **Within a family, three slots only:** Quickstart · Reference · Reports. No cards, no stats strip, no “this week.”
4. **Gap report is a Report slot item for boarding**, linked as a peer of Reference — docs-team deliverable, not hidden under artifacts/.
5. **Cross-family:** no mega-nav. Selecting a family replaces the main list; deep links stay `/<slug>` so MCP/evals do not break.
6. **Empty family:** show the empty-state copy for that family only (“No generated boarding pages yet”) plus the gap report if it exists.
7. **Lab / fixtures** stay out of the portal nav (registry `lab.json` is test-only).

## Out of scope for this sketch

- Visual redesign beyond structure (type/color can follow later).
- Live boarding eval, partner-portfolio auth.
- Changing the serve contract (`content/` only).

## Decision needed

Approve / amend this family → (Quickstart | Reference | Reports) model before Wave 2 portal wiring.
