# Source Index — CyberSource Developer Portal

## Documentation

- **Developer Portal:** https://developer.cybersource.com
- **LLMs.txt:** https://developer.cybersource.com/llms.txt — full site index, preferred patterns, security rules
- **API Reference (OpenAPI):** https://developer.cybersource.com/api-reference-assets/specs/cybs_merged.json
- **GitHub SDKs:** https://github.com/CyberSource — official REST SDKs

## Preferred Patterns (from llms.txt)

- Use **REST API** only (Simple Order/SOAP deprecated)
- Use **JSON** request/response formats
- Prefer **JWT** over HTTP Signature for auth
- Use **Unified Checkout** as default for web card acceptance
- Use **Token Management Service** for tokenization
- Always test on **sandbox** at `apitest.cybersource.com`
- Default processor: **Platform Connect (CTV)**

## MCP (Agent Toolkit)

- **Acceptance Agent Toolkit:** https://developer.example.com/docs/vas/en-us/agent-toolkit/
- **CyberSource MCP:** Not yet public — available in private CyberSource GitHub repo or via Google search

## SDK Installation

```bash
# Node.js SDK (official, latest)
npm install cybersource-rest-client

# Python SDK (official)
pip install cybersource-rest-client

# TypeScript SDK
npm install @paciolan/cybersource-sdk
```

## Sandbox Testing

- **Test card:** 4111111111111111, expiry 12/2031, CVV 123
- **Sandbox endpoint:** https://apitest.cybersource.com
- **Sandbox signup:** https://developer.cybersource.com/hello-world/sandbox.md

## Known Doc Gaps

- SDK auth field names differ from docs: SDK uses `merchantKeyId` / `merchantsecretKey`, docs say `keyId` / `secretKey`
- Some required fields (e.g., `billTo` on payments) not documented in API reference
- Response codes are documented but error recovery guidance is sparse
