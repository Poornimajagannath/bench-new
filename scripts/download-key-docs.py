#!/usr/bin/env python3
"""Fetch key Payment Gateway integration docs for the Relay pipeline"""
import re
import os
import json
import urllib.request

DOCS_URLS = [
    "https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started.md",
    "https://developer.example.com/docs/gateway/en-us/payments/developer/ctv/rest/payments.md",
    "https://developer.example.com/docs/gateway/en-unified-checkout/developer/all/rest/unified-checkout.md",
    "https://developer.example.com/docs/gateway/en-us/security-keys/user/all/ada/security-keys.md",
    "https://developer.example.com/docs/gateway/en-us/tms/developer/all/rest/tms.md",
    "https://developer.example.com/docs/gateway/en-us/payer-authentication/developer/all/rest/payer-auth.md",
    "https://developer.example.com/docs/gateway/en-us/credentials/developer/ctv/rest/credentials.md",
    "https://developer.example.com/hello-world/sandbox.md",
    "https://developer.example.com/hello-world/testing-guide.md",
    "https://developer.example.com/docs/gateway/en-us/unified-checkout/quick-start/all/na/uc-qsg.md",
]

OUTPUT_DIR = "gateway-docs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

results = []
for url in DOCS_URLS:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Payment Gateway-Relay/1.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode('utf-8')
            filename = url.split('/')[-1]
            filepath = os.path.join(OUTPUT_DIR, filename)
            with open(filepath, 'w') as f:
                f.write(f"# Source: {url}\n\n")
                f.write(content)
            results.append({"url": url, "status": "ok", "lines": len(content.split('\n'))})
            print(f"OK: {filename} ({len(content.split(chr(10)))} lines)")
    except Exception as e:
        results.append({"url": url, "status": "fail", "error": str(e)})
        print(f"FAIL: {url} - {e}")

with open(os.path.join(OUTPUT_DIR, '.index.json'), 'w') as f:
    json.dump({"docs_fetched": len([r for r in results if r['status'] == 'ok']), "results": results}, f, indent=2)

print(f"\nFetched {len([r for r in results if r['status'] == 'ok'])}/{len(DOCS_URLS)} docs")
