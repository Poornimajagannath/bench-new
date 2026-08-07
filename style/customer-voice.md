# Customer voice (Content Bench)

Owned style guide for the A3 humanizer. Edit this file when a merged PR
teaches a better rule — the humanizer loads it at runtime; no code change
required for voice tweaks.

Humanizer may rewrite **prose** only. Templated **facts** (method, path,
fields, status codes, auth schemes, quickstart schema steps) are guarded by
`fact_hash` and must not change.

## Ten rules

1. **Plain sentences.** Prefer short, concrete sentences. Cut throat-clearing
   openers ("In order to", "It is important to note that").

2. **No internal jargon.** Do not ship eng-only terms (for example
   "lineage_origin", "fixture", "unit_id", "normalized claim") to customers.
   Say what the reader must do instead.

3. **No source boilerplate.** Strip phrases that only make sense next to a
   raw dump ("as described in the OpenAPI", "per the fixture", "from the
   reference unit").

4. **No revision histories.** Never paste changelog, "updated on", or
   "formerly known as" archaeology into a customer page.

5. **Second person.** Address the integrator as "you". Prefer "Send a POST"
   over "The client sends a POST".

6. **One idea per paragraph.** If a paragraph does two jobs, split it.

7. **No promotional fluff.** Ban vibrant / seamless / robust / leverage /
   unlock / empower / cutting-edge filler. Docs instruct; they do not sell.

8. **Active and direct.** Prefer "is" / "has" / "send" over "serves as",
   "stands as", "facilitates", or subjectless fragments.

9. **No AI vocabulary.** Drop delve, tapestry, landscape (abstract),
   pivotal, underscore, showcase, testament, and "It's not just X; it's Y".

10. **Uncertainty is a TODO.** If a detail is not backed by a templated fact,
    write `<!-- TODO: ... -->` instead of guessing. Never invent fields,
    status codes, or auth schemes in prose.
