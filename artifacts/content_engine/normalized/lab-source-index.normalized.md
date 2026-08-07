# Source Index — Payment Gateway Developer Portal

## Documentation

- **Developer Portal:** https://developer.example.com
- **LLMs.txt:** https://developer.example.com/llms.txt — full site index, preferred patterns, security rules
- **API Reference (OpenAPI):** https://developer.example.com/api-reference-assets/specs/gateway_merged.json
- **GitHub SDKs:** https://github.com/example — official REST SDKs

## Preferred Patterns (from llms.txt)

- Use **REST API** only (Simple Order/SOAP deprecated)
- Use **JSON** request/response formats
- Prefer **JWT** over HTTP Signature for auth
- Use **Unified Checkout** as default for web card acceptance
- Use **Token Management Service** for tokenization
- Always test on **sandbox** at `apitest.example.com`
- Default processor: **Platform Connect (CTV)**

## MCP (Agent Toolkit)

- **Acceptance Agent Toolkit:** https://developer.example.com/docs/vas/en-us/agent-toolkit/
- **Payment Gateway MCP:** Not yet public — available in private Payment Gateway GitHub repo or via Google search

## SDK Installation

```bash
# Node.js SDK (official, latest)
npm install payment-gateway-rest-client

# Python SDK (official)
pip install payment-gateway-rest-client

# TypeScript SDK
npm install @paciolan/payment-gateway-sdk
```

## Sandbox Testing

- **Test card:** 4111111111111111, expiry 12/2031, CVV 123
- **Sandbox endpoint:** https://apitest.example.com
- **Sandbox signup:** https://developer.example.com/hello-world/sandbox.md

## Known Doc Gaps

- SDK auth field names differ from docs: SDK uses `merchantKeyId` / `merchantsecretKey`, docs say `keyId` / `secretKey`
- Some required fields (e.g., `billTo` on payments) not documented in API reference
- Response codes are documented but error recovery guidance is sparse
