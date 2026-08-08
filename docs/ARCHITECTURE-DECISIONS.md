# Architecture decisions (maintained with the architect)

Invariants, in priority order:
1. Nothing is ever served from raw/. raw/ is verbatim evidence, never edited,
   never a paraphrase.
2. Everything published reaches content/ only through a PR a human approves.
   No hand-edited pages, ever. Fix the source and regenerate.
3. The doc agent answers only from generated docs, and says "gap" rather
   than guessing.
4. Every eval and hand test leaves evidence. Failures are kept, not replaced.
5. Denominators and eval expectations are computed from the source of truth
   at runtime, never hard-coded. For docs corpus coverage the **product
   root** mega-guide is the denominator (verbatim `*.md` at the family
   guide path). The family HTML TOC is a cross-check that reports pages
   whose content does not appear in the root. `llms.txt` is never a
   denominator.

Eval taxonomy: the deterministic task eval gates PRs. The live parity eval
runs nightly as evidence and never gates a build.

Two repos: content-bench is the engine's home, the private repo configures it.
Engine fixes port back the same day. No private data ever moves to public.

Report format: every number arrives with its denominator and its source.
