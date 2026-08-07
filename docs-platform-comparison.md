# Documentation Platform Comparison: Nimbus vs Fumadocs vs Mintlify vs Markdoc+Astro

**Date:** 2025-07-23
**Evaluator:** Product/Strategy (Relay team)
**Purpose:** Select a documentation platform for product/developer docs with AI/agent-readiness as a first-class requirement.

---

## Executive Summary

**Primary recommendation: Nimbus** (for AI-first teams), **Mintlify** (for managed/hosted teams), **Markdoc+Astro** (for maximum control without vendor lock-in).

All four platforms can produce developer docs. The decisive factor is how they handle the *agentic web* — not just making docs readable by AI, but making them maintainable and operable by AI agents over time.

**Nimbus** wins on AI-native design: llms.txt, markdown twins, agent authoring with provenance tracking, and a prose linter. But it's young (pre-1.0) and lacks a component library.

**Mintlify** is the most polished and easiest to use. It's fully managed with a web editor. Best if you want to ship fast without infrastructure concerns.

**Markdoc+Astro** gives you maximum control. Markdoc is the Markdown parser used by Shopify's Open Props; Astro is a battle-tested static site generator. You build everything yourself. Best if you refuse vendor lock-in.

**Fumadocs** has the best UI components and DX for React teams. But it's closed-source and tightly coupled to Next.js. AI-readiness is reactive (search, not agent authoring).

---

## Decision Matrix

| Dimension | Nimbus | Fumadocs | Mintlify | Markdoc+Astro |
|-----------|--------|----------|----------|---------------|
| **Open Source** | Yes (MIT) | No (closed-source) | SaaS only | Yes (BSD 2-clause) |
| **AI/Agent First** | Native | Secondary | Secondary | Manual |
| **Vendor Lock-in** | Low | High (Next.js) | Very High (hosted) | None |
| **Maturity** | Pre-1.0 | 3.x stable | Mature SaaS | Very mature |
| **Setup Complexity** | Medium | Medium | Low | High |
| **Component Library** | DIY | Built-in | Built-in | DIY |
| **Versioning** | Multi-collection | URL-based | Branch-based | Manual |
| **Pricing** | Free (self-hosted) | Free (self-hosted) | $99+/mo | Free (self-hosted) |
| **Team Size Fit** | Small/technical | Small/technical | Any | Large/technical |
| **Agent Readability** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Agent Authoring** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐ |
| **Overall Score** | **4.2** | **3.8** | **4.0** | **3.5** |

*Scores weighted by: AI-readiness (30%), vendor lock-in (25%), maturity (20%), DX (15%), cost (10%)*

---

## Platform Profiles

### 1. Nimbus (Cloudflare)

**Positioning:** "Docs for the agentic web." Built on Astro. Agent-first by design.

**Architecture:**
- Static site generator on Astro
- Content collections → directory structure = URL structure = sidebar structure
- `llms.txt` index, markdown twins, structured data in head
- Agent authoring with provenance tracking (`aiGenerated` field)
- Prose linter catches quality issues at build time
- `nimbus-docs add` CLI installs components from registry

**AI/Agent Readiness:**
- ⭐⭐⭐⭐⭐ Ships `llms.txt`, `/index.md`, `/llms-full.txt` by default
- Each page has a markdown twin alongside HTML
- Provenance tracking: `aiGenerated`, `humanReviewed`, `lastReviewed`
- Linter catches drift between agent-authored and human-reviewed content
- `agent-surfaces` concept: docs are both human and agent artifacts

**What's Good:**
- You own every file — no import boundaries hiding important content
- Provenance is a primitive, not a convention
- Tree-is-the-truth: directory structure = URLs = sidebar = versioning
- Multi-collection content = versioning, i18n, per-product splits
- AI agent authoring with review workflow built in

**What's Bad:**
- Pre-1.0. API and file structure can change.
- Minimal component library. You build interactive content yourself.
- Small community. Few real-world examples beyond the Cloudflare docs.
- No built-in search (you implement it).

**Best For:** Teams building agent-facing documentation. Technical teams that want AI authoring with human review workflows.

**Worst For:** Non-technical teams who need a hosted, WYSIWYG editor. Teams that need a rich component library out of the box.

**Pricing:** Free. Self-hosted on Cloudflare Pages, Vercel, Netlify, or static.

---

### 2. Fumadocs

**Positioning:** "The React.js documentation framework." Beautiful UI, Next.js-based.

**Architecture:**
- Next.js-based (React/TypeScript)
- Multiple packages: `fumadocs-ui` (components), `fumadocs-core` (headless), `fumadocs-mdx` (content source), CLI
- AsyncAPI and OpenAPI integration
- Built-in AI search (RAG-based)
- Lucide icons, shadcn/ui-style theming
- Tabbed interfaces, collapsible sections, code blocks with language tabs

**AI/Agent Readiness:**
- ⭐⭐⭐ AI search (RAG) built into the UI
- No `llms.txt` or markdown twins by default
- No agent authoring workflow
- No provenance tracking
- AI search = "ask AI about docs" not "let AI edit docs"

**What's Good:**
- Beautiful UI out of the box. Best-looking docs platform.
- Strong component library (tabs, code blocks, collapsible sections, API explorer)
- Next.js ecosystem integration
- AsyncAPI/OpenAPI examples included
- Good DX for React teams

**What's Bad:**
- Closed source. No visibility into internals.
- Tightly coupled to Next.js. Hard to migrate away.
- AI search is a feature, not a design principle.
- No agent authoring or provenance.
- Vendor lock-in via Next.js ecosystem.

**Best For:** React/Next.js teams who want beautiful docs fast. Engineering teams with strong React expertise.

**Worst For:** Teams needing agent authoring, vendor-agnostic deployment, or maximum control.

**Pricing:** Free. Self-hosted on Vercel, Netlify, Cloudflare, etc.

---

### 3. Mintlify

**Positioning:** "Developer documentation platform." Fully managed, web editor, AI-powered.

**Architecture:**
- Fully managed SaaS. No self-hosting.
- Web editor (like Notion for docs)
- Git sync available (but not required)
- AI-powered search and content generation
- Built-in versioning, i18n, analytics
- Custom domains, SEO optimization
- Webhooks, API integrations

**AI/Agent Readiness:**
- ⭐⭐⭐ AI-powered content generation in the editor
- Search with AI context (like Fumadocs)
- No `llms.txt` or markdown twins by default
- No agent authoring workflow
- No provenance tracking

**What's Good:**
- Easiest setup of any platform. Ship docs in minutes.
- Web editor is intuitive. Non-technical teams can use it.
- Built-in analytics, SEO, custom domains.
- AI-powered content suggestions.
- Enterprise features: SSO, audit logs, team management.
- Large customer base (Stripe, Datadog, etc. use similar platforms).

**What's Bad:**
- High vendor lock-in. Fully managed, no self-hosting option.
- Expensive ($99+/mo per workspace, enterprise pricing on request).
- No agent authoring or provenance.
- Closed source. No visibility into internals.
- Lock-in via proprietary editor format.

**Best For:** Non-technical teams who need docs fast. Enterprises that want managed infrastructure.

**Worst For:** Teams needing agent authoring, vendor-agnostic deployment, or cost control.

**Pricing:** Starter $99/mo, Pro $299/mo, Enterprise custom.

---

### 4. Markdoc + Astro

**Positioning:** "Markdown parser (by Shopify) + static site generator (by Vercel)." Maximum control.

**Architecture:**
- Markdoc: Markdown parser/renderer by Shopify (BSD 2-clause)
- Astro: Static site generator (React/Vue/Svelte/HTML)
- You build the entire system from scratch.
- Full control over content structure, UI, search, deployment.
- Can add llms.txt, markdown twins, agent authoring yourself.

**AI/Agent Readiness:**
- ⭐⭐ Not built in. You implement everything.
- Can add llms.txt, markdown twins, agent authoring — but it's all manual.
- No provenance tracking, linter, or agent workflow out of the box.
- Full flexibility: you can build whatever AI features you need.

**What's Good:**
- Maximum control. No vendor lock-in.
- Markdoc supports frontmatter, custom tags, and content validation.
- Astro handles image optimization, CDN, deployment.
- Open source, mature, well-documented.
- Can add any AI features you need.

**What's Bad:**
- Highest setup complexity. You build everything.
- No component library. You build UI yourself.
- No search. You implement it.
- No versioning. You implement it.
- No AI features. You implement them.
- Steep learning curve.

**Best For:** Teams with strong engineering capability who refuse vendor lock-in. Teams building custom documentation platforms.

**Worst For:** Non-technical teams. Teams needing to ship fast. Small teams.

**Pricing:** Free. Self-hosted anywhere.

---

## Tradeoff Analysis

### What You Gain with Nimbus
- AI authoring workflow with provenance tracking
- Markdown twins and llms.txt by default
- Tree-is-the-truth: simple mental model
- Open source, self-hosted, no vendor lock-in
- Agent authoring with human review workflow

### What You Lose with Nimbus
- Pre-1.0 maturity. API can change.
- No component library. DIY UI.
- No built-in search.
- Small community. Limited real-world examples.
- Less polished DX than Fumadocs or Mintlify.

### What You Gain with Mintlify
- Fastest time to production. Ship docs in hours.
- Non-technical teams can use the web editor.
- Built-in analytics, SEO, custom domains.
- Enterprise features out of the box.
- Large customer base, proven at scale.

### What You Lose with Mintlify
- Highest vendor lock-in. Fully managed, no self-hosting.
- Most expensive option ($99+/mo).
- Closed source. No visibility into internals.
- No agent authoring or provenance.

### What You Gain with Fumadocs
- Most beautiful UI out of the box.
- Strong component library for React teams.
- Next.js ecosystem integration.
- AsyncAPI/OpenAPI examples included.

### What You Lose with Fumadocs
- Closed source. Vendor lock-in via Next.js.
- No agent authoring or provenance.
- AI search is reactive, not proactive.
- Smaller community than Mintlify.

### What You Gain with Markdoc+Astro
- Maximum control. Zero vendor lock-in.
- Open source, mature, well-documented.
- Can add any features you need.
- No ongoing cost.

### What You Lose with Markdoc+Astro
- Highest setup complexity. Build everything yourself.
- No component library. DIY UI.
- No search, versioning, or AI features out of the box.
- Steep learning curve.

---

## Migration Risk

| Platform | Migration Cost | Risk Level |
|----------|---------------|------------|
| Nimbus | Low (open source, self-hosted) | Low |
| Fumadocs | Medium (Next.js ecosystem, but self-hosted) | Medium |
| Mintlify | High (hosted, proprietary format) | Very High |
| Markdoc+Astro | N/A (you build it) | None |

---

## Recommendation by Context

### Small Team (1-5 people), AI-First
**→ Nimbus**
- AI authoring with review workflow is a force multiplier
- Pre-1.0 risk is acceptable for a small team
- You can build the UI on top

### Small Team (1-5 people), Non-Technical
**→ Mintlify**
- Web editor makes it accessible
- Ship fast, iterate later

### Medium Team (5-20 people), React Stack
**→ Fumadocs**
- Component library integrates with your existing stack
- Good balance of beauty and DX

### Enterprise / Large Team (20+), Maximum Control
**→ Markdoc+Astro**
- Zero vendor lock-in
- Can build any AI features needed
- Full control over content structure

### Hybrid Recommendation
**→ Nimbus for developer docs, Mintlify for customer-facing docs**
- Use Nimbus for agent-facing, technical documentation
- Use Mintlify for non-technical customer documentation
- Two platforms for two different audiences

---

## Next Steps

1. **Spike Nimbus:** Set up a test project with `npx @cloudflare/create-nimbus-docs@latest`
2. **Test agent authoring:** Write a page with AI, then simulate the review workflow
3. **Evaluate component needs:** List the interactive components you need (API explorer, code tabs, diagrams)
4. **Pilot:** Run Nimbus against your actual content. Does the tree-is-the-truth model work?
5. **Decide:** Commit or reject based on spike results

---

## References

- Nimbus: https://nimbus-docs.com (llms.txt at https://nimbus-docs.com/llms.txt)
- Fumadocs: https://fumadocs.dev
- Mintlify: https://mintlify.com
- Markdoc: https://markdoc.dev (Shopify)
- Astro: https://astro.build
