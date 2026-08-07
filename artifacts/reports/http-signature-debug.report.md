# Content Bench V0 Report — `http-signature-debug`

Local proof only. No network. No live credentials.

## 1. What developers were confused about

- My HTTP Signature request looks correct but CyberSource returns Authentication Failed on apitest.cybersource.com
- Am I using the wrong SDK field names for key id and secret
- entity:HTTP Signature
- entity:Authentication Failed
- entity:keyId
- entity:secretKey
- entity:apitest.example.com
- HTTP Signature signed headers include host,date,digest but we still get 401. Do we need request-target and v-c-merchant-id in the signature base on apitest?
- entity:v-c-merchant-id
- alt_goal:Resolve developer confusion involving HTTP Signature, v-c-merchant-id, apitest.example.com
- Authentication Failed every time on sandbox
- entity:merchantKeyId
- alt_goal:Resolve developer confusion involving Authentication Failed, keyId, secretKey, merchantKeyId
- Is Authentication Failed expected, and what host should sandbox use
- alt_goal:what host should sandbox use?
- Our manual HMAC matches locally but apitest still rejects the request
- alt_goal:How should the digest and signature base string be built for CyberSource HTTP Signature?
- Does logging the shared secret in debug headers cause Authentication Failed, or is the issue only field names like keyId vs merchantKeyId on HTTP Signature
- alt_goal:Resolve developer confusion involving HTTP Signature, Authentication Failed, keyId, merchantKeyId

## 2. What Content Bench discovered

- Am I using the wrong SDK field names for key id and secret?
- stages:load_sandbox_env_vars,build_digest,build_signature_base,attach_vc_headers,interpret_auth_failure
- fact:Sandbox host is apitest.example.com
- fact:SDK expects merchantKeyId and merchantsecretKey (not keyId/secretKey)
- fact:Signed headers typically include host, date, request-target, digest, v-c-merchant-id

## 3. What the bad answer got wrong

- Uses doc field names and production host; omits request-target and v-c-merchant-id
- credential_fields: expected=['merchantKeyId', 'merchantsecretKey'] actual=['keyId', 'secretKey']
- endpoint_host: expected='apitest.example.com' actual='api.example.com'
- signed_headers contains_all ['host', 'date', 'request-target', 'digest', 'v-c-merchant-id']: False

## 4. How the verifier caught it

- failed check `sdk_field_names`
- failed check `sandbox_host`
- failed check `signed_headers_complete`

## 5. What product surface improves next

- Clarify HTTP Signature Debug stage ordering in public docs
- Align SDK credential field names with docs (or docs with SDK)
- Ship a Content CLI workflow verifier for this contract

## Classification

- category: `auth-mechanism`
- summary: Bad answer for http-signature-debug failed 3 verifier check(s).

## Artifacts

- task pack: `artifacts/task_packs/http-signature-debug.agent_task.json`
- verifier results: `artifacts/verifier_results/http-signature-debug.result.json`

## Content CLI workflow verifier (recommended)

- goal: Am I using the wrong SDK field names for key id and secret?
- command: `content workflow verify --id http-signature-debug --fixture local`
- readiness checks:
  - Frozen seeds present under data/seeds/
  - No live credentials exported
  - Local fixture id resolved for workflow
  - Stage ready: load_sandbox_env_vars
  - Stage ready: build_digest
  - Stage ready: build_signature_base
  - Stage ready: attach_vc_headers
  - Stage ready: interpret_auth_failure
- recovery path:
  - Re-run discovery to refresh typed candidate
  - Compare agent plan stages against workflow contract stages
  - Apply verifier-private checks to the candidate answer only
  - Emit support-safe evidence without secrets or PAN
