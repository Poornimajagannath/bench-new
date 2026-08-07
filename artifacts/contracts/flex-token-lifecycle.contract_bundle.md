# Workflow Contract Bundle — `flex-token-lifecycle`

schema_version: `relay.workflow_contract_bundle.v0`

Local proof only. DocETL-style extraction and Harbor/Tempo-style eval export are inspirations — not live upstream integrations.

## 1. What source confusion became this contract?

**Goal:** can I pass it straight into TMS to store a permanent instrument, or do I need another step?

Confusion points:
- TMS createInstrument rejects my Flex JWT when I send it as pan
- entity:Flex
- entity:Microform
- entity:TMS
- entity:createInstrument
- Support said not to treat the JWT like a reusable PAN, but checkout still fails when creating a permanent instrument
- entity:transientTokenJwt
- alt_goal:Resolve developer confusion involving Flex, Microform, TMS, transientTokenJwt
- Is persisting the Flex JWT wrong, and what is the correct permanent instrument path
- alt_goal:how transientTokenJwt but our backend stores it in Redis for later TMS createInstrument. Is persisting the Flex JWT wrong, and what is the correct permanent instrument path?
- Can TMS createInstrument accept a Flex Microform token without sending pan? We keep getting INVALID_DATA when we map transientTokenJwt into card number fields.
- alt_goal:Can TMS createInstrument accept a Flex Microform token without sending pan?
- We thought authorize with the transient token was enough and skipped TMS entirely
- alt_goal:which API creates a reusable instrument identifier?
- Our team mixes Flex Microform JWT handling with TMS instrument CRUD and auth keeps failing
- alt_goal:Resolve developer confusion involving Flex, Microform, TMS
- We authorize immediately with transientTokenJwt and later cannot reuse it
- entity:authorization
- alt_goal:What is the correct lifecycle from Flex Microform capture to permanent TMS instrument before authorization?

Source seed ids: `seed-flex-01, seed-flex-02, seed-flex-03, seed-flex-04, seed-flex-05, seed-flex-06, seed-flex-07`

## 2. What did PM approve or edit?

- pm_decision: `approve`
- title: Flex Token Lifecycle
- stages: `capture_transient_token, validate_token_type, create_permanent_instrument, authorize_with_instrument`

API/SDK facts:
- Flex Microform returns a short-lived transientTokenJwt
- TMS createInstrument accepts a Flex token via a dedicated transient-token path, not as raw pan
- Transient tokens must not be persisted as long-lived customer credentials

## 3. What agent-visible task pack was created?

- task_pack_path: `artifacts/task_packs/flex-token-lifecycle.agent_task.json`
- agent_visible_path: `artifacts/task_packs/flex-token-lifecycle.agent_task.json`
- The agent pack is the public contract surface (instruction, stages, allowed context). It must not include oracle, bad answer, or private checks.

## 4. What hidden truth exists, without showing it?

- hidden_truth_path: `artifacts/task_packs/flex-token-lifecycle.verifier_private.json`
- oracle_present: `true`
- bad_answer_present: `true`
- private_checks_present: `true`
- agent_pack_omits_oracle: `true`
- agent_pack_omits_bad_answer: `true`
- agent_pack_omits_private_checks: `true`
- oracle_field_count: `4`
- bad_answer_field_count: `5`
- private_check_count: `4`
- hidden_truth_sha256: `6d30eebb9b243e326da91e537140bcdd0793d64387c8f946b2ae926fdbb6a2bd`

Hidden truth content is intentionally omitted from this bundle.

## 5. How would this map to a future Harbor/Tempo-style eval task?

- preview_only: `true`
- runner_integration: `not implemented`
- environment.mode: `local-simulated`
- test_ref.workflow_id: `flex-token-lifecycle`
- expected_artifact: A structured plan listing each stage, the API/SDK fact it depends on, and the readiness check before moving to the next stage.
- isolation_note: V0 does not run Harbor, tempo-evals, or Docker isolation. This preview documents how a future eval export could package the agent-visible task against verifier-private fixtures.

## 6. What verifier result or product action exists now?

- verifier_result_path: `artifacts/verifier_results/flex-token-lifecycle.result.json`
- improvement_actions:
  - [docs] Clarify Flex Token Lifecycle stage ordering in public docs
  - [vap_cli] Ship a Relay CLI workflow verifier for this contract
