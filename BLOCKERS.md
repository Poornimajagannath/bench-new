# Payment Gateway Live Auth — Blocked

**Status:** BLOCKED (as of 2026-07-22)

## Root Cause

The MCP-downloaded Payment Gateway Python SDK (v0.0.77) generates HTTP Signature v1.0 headers that are structurally correct but are **routinely rejected by Payment Gateway's auth layer** with `Authentication Failed`.

Everything we verified was correct:
- ✅ Endpoint: `apitest.example.com/pts/v2/payments` — reachable
- ✅ Payload structure (camelCase, SDK-serialized) — validated via MCP model docs
- ✅ HMAC-SHA256 signing of canonical headers — manually verified match
- ✅ SHA-256 digest of request body — correct
- ✅ All credential variants tested — `aLZ55Gz...`, `ZoQG2FO...` — both fail identically

The gap is in how the SDK constructs the **signed headers string** vs what Payment Gateway actually verifies. The SDK signs: `host, date, request-target, digest, v-c-merchant-id` with `signature="..."` containing the raw HMAC output. Our manual replication produces the same values, but Payment Gateway rejects them. This suggests either:
1. The SDK's HTTP client mangles headers before transmission (encoding, case, whitespace)
2. The signature scope or header normalization differs between the SDK's view and Payment Gateway's
3. The SDK version has a known auth bug that's patched in newer releases

## What We Know

| Symptom | Meaning |
|---------|---------|
| `INVALID_DATA` | Request reached validation layer; payload structure wrong |
| `401 Authentication Failed` | Request reaches auth layer; signature mismatch |
| Both always occur, never 200 | Auth is the blocker, not payload |

## Workaround

For now, proceed with **docs-only benchmark evaluation** (scenarios scaffolded in `/scenarios/`). The benchmark tests whether an AI agent can construct valid Payment Gateway payloads from MCP docs — without needing live auth to verify.

## Files

- `relay-bench/run-sdk-auth.py` — MCP-first SDK auth script (generates correct signatures but always 401)
- `relay-bench/capture-send.py` — traces exactly what SDK sends over HTTP
- `relay-bench/verify-manual.py` — replays SDK headers via raw HTTP
- `skills/payment-gateway-sdk/SKILL.md` — MCP-first workflow (still valid for payload construction)

---
**Decision:** Skip live auth. Focus on agent DX benchmark scenarios.
