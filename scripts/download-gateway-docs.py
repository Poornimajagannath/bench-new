#!/usr/bin/env python3
"""Download Payment Gateway docs in batches, write index progressively"""
import re
import os
import json
import urllib.request
import time

LLMS_URL = "https://developer.example.com/llms.txt"
OUTPUT_DIR = "gateway-docs"
BATCH_SIZE = 20

os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_urls(text):
    urls = re.findall(r'https://developer\.payment-gateway\.com/docs/gateway/[^\s\)]+?\.md', text)
    urls += re.findall(r'https://developer\.example\.com/docs/[^\s\)]+?\.md', text)
    urls += re.findall(r'https://developer\.payment-gateway\.com/hello-world/[^\s\)"]+?\.md', text)
    urls += re.findall(r'https://developer\.payment-gateway\.com/support/[^\s\)"]+?\.md', text)
    urls += re.findall(r'https://developer\.payment-gateway\.com/technology-partners\.md', text)
    return list(dict.fromkeys(urls))

def url_to_path(url):
    path = url.replace('https://developer.example.com/docs/gateway/', '')
    path = path.replace('https://developer.example.com/docs/', '')
    path = path.replace('https://developer.example.com/hello-world/', '')
    path = path.replace('https://developer.example.com/support/', '')
    path = path.replace('https://developer.example.com/', '')
    path = path.replace('/', '_')
    return path + '.md'

print("Fetching llms.txt...")
req = urllib.request.Request(LLMS_URL, headers={'User-Agent': 'Payment Gateway-Relay/1.0'})
with urllib.request.urlopen(req, timeout=30) as resp:
    llms_content = resp.read().decode('utf-8')

urls = extract_urls(llms_content)
print(f"Found {len(urls)} markdown docs")

# Load partial state
state_file = os.path.join(OUTPUT_DIR, '_state.json')
if os.path.exists(state_file):
    with open(state_file) as f:
        state = json.load(f)
else:
    state = {"downloaded": [], "failed": []}

total = len(urls)
done = len(state["downloaded"])
print(f"Already downloaded: {done}/{total}")

ok = 0
fail = 0
start = done

for i in range(start, total):
    url = urls[i]
    filepath = os.path.join(OUTPUT_DIR, url_to_path(url))
    
    if filepath in state["downloaded"]:
        ok += 1
        continue
    
    try:
        req2 = urllib.request.Request(url, headers={'User-Agent': 'Payment Gateway-Relay/1.0'})
        with urllib.request.urlopen(req2, timeout=15) as resp:
            content = resp.read().decode('utf-8')
            with open(filepath, 'w') as f:
                f.write(content)
            state["downloaded"].append(filepath)
            ok += 1
    except Exception as e:
        state["failed"].append({"url": url, "error": str(e)})
        fail += 1
    
    if (i + 1) % BATCH_SIZE == 0 or i == total - 1:
        # Save state periodically
        with open(state_file, 'w') as f:
            json.dump(state, f)
        print(f"  Batch {i+1}/{total}: {ok} OK, {fail} fail, {len(state['downloaded'])} saved")
    
    time.sleep(0.1)

# Write final index
index = {
    "total": total,
    "downloaded": len(state["downloaded"]),
    "failed": len(state["failed"]),
    "examples": state["downloaded"][:10]
}
with open(os.path.join(OUTPUT_DIR, '.index.json'), 'w') as f:
    json.dump(index, f, indent=2)

print(f"\nDone! {ok} OK, {fail} failed")
