# DX Issue Taxonomy

## Buckets

| Bucket | Description |
|--------|-------------|
| `missing-docs` | Documentation doesn't exist or is hard to find |
| `wrong-docs` | Documentation has incorrect information |
| `missing-api-field` | SDK/API requires a field not documented |
| `wrong-sdk-field` | SDK field name differs from documentation |
| `ambiguous-api-response` | API response is unclear or undocumented |
| `rate-limiting` | Sandbox/API is rate-limited without documentation |
| `auth-mechanism` | Authentication is unclear or broken |
| `sdk-installation` | SDK installation fails or is undocumented |
| `sdk-usage` | SDK usage is unclear or requires workarounds |
| `error-handling` | Error responses are unclear or undocumented |

## Severity

| Severity | When to use |
|----------|-------------|
| `low` | Minor issue, doesn't block integration |
| `medium` | Significant issue, causes retry or confusion |
| `high` | Critical issue, blocks integration or causes wrong behavior |
