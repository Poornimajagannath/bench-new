# Boarding TOC fetch report

- When: `2026-08-07T07:21:43+00:00`
- Denominator rule: Coverage denominator is the site's own HTML navigation/TOC tree for each family — not llms.txt. llms.txt is an incomplete discovery aid.

## Headline finding (production docs site)

**CyberSource `llms.txt` — the file that exists so AI agents can discover docs — does not list a distinct Merchant Boarding API family under `/merchant-boarding/`, and that path’s `.md` endpoint returns HTTP 500 while HTML redirects into the Business Center boarding guide.** Any agent that trusts the site’s own agent-readiness surface cannot reliably discover or read boarding via that alias.

- Probe: `merchant-boarding.md returns HTTP 500; HTML redirects to https://developer.cybersource.com/docs/cybs/en-us/boarding/user/all/ebc/boarding-user/boarding-intro-overview.html. Path alias is not a separate fetchable markdown family; programmatic surface lives under /boarding/developer/all/rest/boarding/.`
- `merchant-boarding` listed in llms.txt: **False**
- llms.txt boarding-related `.md` URLs found: **27**

## Denominator vs fetch (site TOC)

| Metric | Count |
| --- | ---: |
| Topics in site TOC (denominator) | 236 |
| Fetched OK | 236 |
| Via `.md` | 236 |
| Via HTML→markdown fallback | 0 |
| Failed | 0 |
| Usable (≥40 bytes) | 236 |
| Prior local corpus (llms/filename slice) | 9 |

## Families

| Family | TOC topics | Fetched | `.md` | HTML fallback | Failed | Usable |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Boarding REST API (`boarding_rest`) | 110 | 110 | 110 | 0 | 0 | 110 |
| Boarding Business Center (`boarding_user`) | 98 | 98 | 98 | 0 | 0 | 98 |
| Boarding Template Management (`boarding_template_mgmt`) | 28 | 28 | 28 | 0 | 0 | 28 |

## Invariant

A coverage denominator must come from the source of truth. `llms.txt` is not one — the site’s own navigation/TOC tree is. Every future family census must state where its denominator came from.
