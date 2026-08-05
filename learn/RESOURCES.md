# Relay Bench Resources

## Knowledge

- [DocETL docs (UCB EPIC)](https://ucbepic.github.io/docetl/)
  Primary docs for the document ETL framework. Use for: what `map` / `code_map` / Frame actually mean upstream.
- [DocETL GitHub — ucbepic/docetl](https://github.com/ucbepic/docetl)
  Source of truth for API surface (e.g. `from_list`, `code_map`). Use for: verifying adapter claims against real package.
- [CyberSource llms.txt](https://developer.cybersource.com/llms.txt)
  Official developer-portal index for agents. Use for: what “real docs” means in this lab vs fixtures.
- [Archify — system maps for agents](https://tt-a1i.github.io/archify/)
  Diagram skill used for the Relay Bench runtime map. Use for: reading architecture / workflow artifacts.
- [Relay Integration Success OS spec (in-repo)](../products/relay/integration-success-os-spec.md)
  Product promise (TTFSC, living docs, evals). Use for: connecting local bench proof to customer claim.
- [Content Engine V0 plan (in-repo)](../docs/plans/2026-08-04-001-feat-relay-content-engine-v0-plan.md)
  Local compile slice definition of done + honesty boundaries.

## Wisdom (Communities)

- [CyberSource Developer Community](https://community.developer.cybersource.com/)
  Practitioner questions on auth field names, sandbox quirks. Use for: real integration failure modes.
- [DocETL discussions / issues](https://github.com/ucbepic/docetl/issues)
  Upstream behavior and version changes. Use for: when an adapter “should” work but doesn’t.

## Gaps

- No public Tempo Stable Bench / Harbor deep-dive bookmarked yet for the preview-only contract export story — add when that lane becomes mission-critical.
