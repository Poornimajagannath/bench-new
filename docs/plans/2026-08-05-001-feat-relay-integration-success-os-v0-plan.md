# Plan: Integration Success OS V0 (assemble pack)

**ID:** 2026-08-05-001
**Status:** Implemented (local prototype)
**Scope:** Local assemble/serve proof for `products/relay/integration-success-os-spec.md`

## Honest label

This is **not** the full Integration Success OS. It assembles already-promoted Relay artifacts into one developer-facing pack.

| Capability | In V0? |
|------------|--------|
| Live sandbox "Test in sandbox" button | **No** |
| Humanify editor workflow | **No** |
| Real DocETL / Tempo | **No** |
| Role-based quickstarts beyond backend_developer | **No** |

## Pipeline

```text
content_engine (quickstart)
+ specs_to_docs (Payment Gateway-shaped OpenAPI)
+ workflow contract bundle
-> integration_success_pack.json/.md
   - guided steps
   - API reference ops
   - test scenario seeds
   - go-live checklist
   - lineage
```

## Command

```bash
python3 pipelines/run_integration_success_v0.py
```

## Definition of Done

- [x] Assembler module + CLI
- [x] Pack includes steps, ops, scenarios, checklist
- [x] No network / secrets / PAN
- [x] Unit tests pass with existing compile lanes
- [x] Links to Integration Success OS product promise
