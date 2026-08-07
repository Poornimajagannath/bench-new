# Engine upstream

The runnable engine (`content_bench/`, shared pipelines, portal, mcp-server, style,
A2/A3, tests) is synced from public
[`content-bench`](https://github.com/Poornimajagannath/content-bench) at tag
`v0.1-stripe-proof`.

**Rule:** engine fixes land in content-bench first, then sync here the same day.
This repo holds **configuration + private CyberSource corpus** only — do not fork
engine modules for product-specific behavior; pass paths/ids via registry and CLI.

Sync command (from a checkout of both repos):

```bash
git -C ../content-bench archive v0.1-stripe-proof content_bench portal mcp-server \
  agents style pipelines scripts/check_content_render.py | tar -x -C .
```
