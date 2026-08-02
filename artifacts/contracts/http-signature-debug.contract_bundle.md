# Workflow Contract Bundle — `http-signature-debug`

schema_version: `relay.workflow_contract_bundle.v0`

Local proof only. DocETL-style extraction and Harbor/Tempo-style eval export are inspirations — not live upstream integrations.

## 1. What source confusion became this contract?

**Goal:** Am I using the wrong SDK field names for key id and secret?

Confusion points:
- My HTTP Signature request looks correct but CyberSource returns Authentication Failed on apitest.cybersource.com
- Am I using the wrong SDK field names for key id and secret
- entity:HTTP Signature
- entity:Authentication Failed
- entity:keyId
- entity:secretKey
- entity:apitest.cybersource.com
- HTTP Signature signed headers include host,date,digest but we still get 401. Do we need request-target and v-c-merchant-id in the signature base on apitest?
- entity:v-c-merchant-id
- alt_goal:Resolve developer confusion involving HTTP Signature, v-c-merchant-id, apitest.cybersource.com
- Authentication Failed every time on sandbox
- entity:merchantKeyId
- alt_goal:Resolve developer confusion involving Authentication Failed, keyId, secretKey, merchantKeyId
- Is Authentication Failed expected, and what host should sandbox use
- alt_goal:what host should sandbox use?
- Our manual HMAC matches locally but apitest still rejects the request
- alt_goal:How should the digest and signature base string be built for CyberSource HTTP Signature?
- Does logging the shared secret in debug headers cause Authentication Failed, or is the issue only field names like keyId vs merchantKeyId on HTTP Signature
- alt_goal:Resolve developer confusion involving HTTP Signature, Authentication Failed, keyId, merchantKeyId

Source seed ids: `seed-httpsig-01, seed-httpsig-02, seed-httpsig-03, seed-httpsig-04, seed-httpsig-05, seed-httpsig-06`

## 2. What did PM approve or edit?

- pm_decision: `approve`
- title: HTTP Signature Debug
- stages: `load_sandbox_env_vars, build_digest, build_signature_base, attach_vc_headers, interpret_auth_failure`

API/SDK facts:
- Sandbox host is apitest.cybersource.com
- SDK expects merchantKeyId and merchantsecretKey (not keyId/secretKey)
- Signed headers typically include host, date, request-target, digest, v-c-merchant-id

## 3. What agent-visible task pack was created?

- task_pack_path: `artifacts/task_packs/http-signature-debug.agent_task.json`
- agent_visible_path: `artifacts/task_packs/http-signature-debug.agent_task.json`
- The agent pack is the public contract surface (instruction, stages, allowed context). It must not include oracle, bad answer, or private checks.

## 4. What hidden truth exists, without showing it?

- hidden_truth_path: `artifacts/task_packs/http-signature-debug.verifier_private.json`
- oracle_present: `True`
- bad_answer_present: `True`
- private_checks_present: `True`
- agent_pack_omits_oracle: `True`
- agent_pack_omits_bad_answer: `True`
- agent_pack_omits_private_checks: `True`
- oracle_field_count: `4`
- bad_answer_field_count: `5`
- private_check_count: `4`
- hidden_truth_sha256: `0318a7735e7f495c8233af7050d680dbb520ddc40049c1d944f4cb91b2909184`

Hidden truth content is intentionally omitted from this bundle.

## 5. How would this map to a future Harbor/Tempo-style eval task?

- preview_only: `True`
- runner_integration: `not implemented`
- environment.mode: `local-simulated`
- test_ref.workflow_id: `http-signature-debug`
- expected_artifact: A structured plan listing each stage, the API/SDK fact it depends on, and the readiness check before moving to the next stage.
- isolation_note: V0 does not run Harbor, tempo-evals, or Docker isolation. This preview documents how a future eval export could package the agent-visible task against verifier-private fixtures.

## 6. What verifier result or product action exists now?

- verifier_result_path: _(not present yet)_
- improvement_actions: _(not present yet)_
