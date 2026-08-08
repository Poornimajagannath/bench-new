# Wave 2 boarding — gap report

## The three headline findings

**1. The boarding docs tell a partner what to click but not what should
happen.** Of **278** sequence steps in the six composed workflows (API + UI),
**215 have no stated outcome** (live recount: `composition-report.json` →
`sequence_totals.ratio` / per-step `outcome_missing: true` flags on
`content/boarding/workflows/*.md`). A developer following these steps has no
way to know whether a step worked. Do not quote older 222/277 or 220/257
figures — they are superseded.

**2. The programmatic boarding path has no procedural documentation.** Of the
257 composed steps, **233 are Business Center UI steps and 24 are REST API
steps** (source: actor counts across `content/boarding/workflows/*.md`). The
flagship workflow — Create a Merchant Organization — has **31 UI steps and 0
API steps**. The REST family exists as reference material (endpoints, field
tables) only: for a partner boarding merchants through the API — the Stripe
Connect equivalent — there is nothing to follow.

**3. The agent-discovery surface is broken** (detail below): `llms.txt` omits
the Merchant Boarding alias, whose `.md` endpoint returns HTTP 500.

## Headline finding (production docs site)

**CyberSource `llms.txt` — the file that exists so AI agents can discover the docs — does not expose a distinct Merchant Boarding API family under `/merchant-boarding/`, and that path’s machine-readable `.md` endpoint returns HTTP 500 while the HTML variant redirects into the Business Center boarding guide.**

Evidence (live probe, this run):

| Probe | Result |
| --- | --- |
| `…/merchant-boarding/developer/all/rest/merchant-boarding.md` | **HTTP 500** (`Error`) |
| `…/merchant-boarding/developer/all/rest/merchant-boarding.html` | **200**, redirects to `…/boarding/user/all/ebc/boarding-user/boarding-intro-overview.html` |
| `merchant-boarding` listed in `llms.txt` | **No** |
| Programmatic boarding surface that *does* exist | `/docs/cybs/en-us/boarding/developer/all/rest/boarding/` (site TOC) |

Any agent (Cursor, Claude, a customer bot) that relies on the site’s own agent-readiness surface cannot discover or read boarding through the `/merchant-boarding/` alias at all. The working surface is the Boarding REST family under `/boarding/…`, which `llms.txt` only partially indexes.

This finding is about the **production docs site**, found by the prototype doing ordinary corpus work. It belongs at the top of any internal briefing on Wave 2.

---

## Denominator honesty

| Source | Count | Role |
| --- | ---: | --- |
| Prior local corpus (llms/filename slice) | **9** | Thin fetch — looked like a thin product |
| `llms.txt` boarding-related `.md` URLs | **27** | Incomplete discovery aid |
| **Site HTML TOC (denominator)** | **236** | Source of truth for this census |
| Fetched OK | **236** | 100% of TOC |
| Via `.md` | **236** | |
| Via HTML→markdown fallback | **0** | (fallback reserved for `.md` 500s such as merchant-boarding) |
| Usable (≥40 bytes) | **236** | |
| Census eligible after quarantine | **182** | |
| Quarantined (`index_navigation` etc.) | **54** | |

**Invariant (extends coverage rule):** a coverage denominator must come from the source of truth. `llms.txt` is not one — the site’s own navigation/TOC tree is. Every future family census must state where its denominator came from.

Denominator for this report: **site HTML TOC** of Boarding REST, Boarding Business Center, and Boarding Template Management (`pipelines/fetch_boarding_toc.py`).

---

## What the thin “9 docs / 6 shells” number really was

The earlier boarding census (9 files, 6 quarantined as index) measured a **thin fetch**, not a thin product. Expanding the fetch from the site TOC lifts the corpus from 9 → **236** pages and eligible guides from 3 → **182**.

The Merchant Boarding API / Connect-equivalent surface (create/search orgs, hierarchies, product templates, status changes, PECS/BRS enablement) lives under the Boarding REST TOC and is now in-corpus.

---

## Family breakdown (TOC → fetch → usable)

| Family | TOC topics | Fetched | Usable |
| --- | ---: | ---: | ---: |
| Boarding REST API | 110 | 110 | 110 |
| Boarding Business Center | 98 | 98 | 98 |
| Boarding Template Management | 28 | 28 | 28 |
| **Total** | **236** | **236** | **236** |

Artifacts: `toc-fetch-report.md`, `census-report.md`, `quarantine-list.md`.

---

## Additions from composition (step 4)

6. **Field semantics documented only in the mega-guide.** `boardingFlow`
   (`ENTERPRISE` creates one organization; `SMB` behavior), `mode` ("not
   currently supported"), and `configurable` (`true` for merchant orgs,
   `false` for transacting) are specified nowhere in the per-topic child
   pages — only in the family compendium. A partner reading topic pages never
   sees them; an agent deep-linking anchors cannot cite them.
7. **Expected outcomes are largely unstated.** Across the six composed
   workflows, **215 of 278** steps have no stated outcome ("what should I see
   if it worked") — machine-readable as `outcome_missing: true` on each step
   and recounted in `composition-report.json` → `sequence_totals.ratio`.

## Next (not done in this pass)

- Boarding workflow schema + portal pages against the 182 eligible docs
- Specs-to-docs / gap matrix for partner onboarding (Connect analogue)
- File internal ticket: fix `merchant-boarding.md` 500 + add the family (or canonical redirect) to `llms.txt`

---

# Developers can see the endpoint and still cannot call it

Matched Endpoint sections that document a verb+URL but omit the Required Fields list and/or a REST Example leave a partner unable to form a valid request. These are gap-report findings, not extractor warnings.

Denominator: **176** matched Endpoint sections (source: `api_reference.extract_api_reference_claims over raw/product-roots` with RF derivation contract).

- Missing Required Fields: **30** / 176
- Missing REST Example: **17** / 176
- Missing both: **10** / 176

## Endpoints with no Required Fields list

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-reg-create-structural-api |
| boarding | `GET` | `/oms/v1/organizations` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-organizations |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-an-organization |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-information-api |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-change-org-status |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-pecs-tms-enable-intro |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-pecs-tms-enable-intro |
| click-to-pay | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#boarding-click-to-pay-enable-intro |
| click-to-pay | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#boarding-click-to-pay-auth-enable-intro |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#ctp-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#boarding-click-to-pay-enable-intro |
| digital-accept-flex | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#boarding-click-to-pay-auth-enable-intro |
| digital-accept-flex | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#ctp-token-get-pymnt-credentials |
| digital-accept-flex | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-token-get-pymnt-details |
| digital-accept-flex | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-token-get-pymnt-details |
| digital-accept-flex | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-auth-tokens |
| digital-accept-flex | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#da-processing-auth-token-task |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#pnt-auth-intro |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-debit-prepaid-disable-part-auth-intro_section_brd_jvn_sxb |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-amex-intro_section_kl3_tbh_xwb |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-jcb-intro |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-mc-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-create-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-create-device-tkn-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tap-create-ii-intro |
| tms | `DELETE` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-delete-intro |
| tms | `GET` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-retrieve-intro |
| tms | `PATCH` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-update-intro |
| tms | `GET` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}/paymentinstruments?` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-retrieve-pi-intro |
| tms | `DELETE` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-delete-intro |
| tms | `GET` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-retrieve-intro |
| tms | `GET` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-retrieve-all-intro |
| tms | `PATCH` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-update-intro |
| tms | `POST` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-create-intro |
| tms | `POST` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-add-nondefault-addr-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-cust-pi-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-create-trans-token-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| tms | `DELETE` | `/tms/v2/tokenized-cards/{id}/bindings/{clientDeviceID}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ctf-delete-binding-intro |
| unified-checkout | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-token-get-pymnt-details |
| unified-checkout | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-auth-tokens |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

## Endpoints with no REST Example

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| invoicing | `POST` | `/invoicing/v2/invoices` | https://developer.cybersource.com/docs/cybs/en-us/invoicing/developer/all/rest/invoicing.html#invoicing-services-create-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

## Endpoints missing both

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

---

# Developers can see the endpoint and still cannot call it

Matched Endpoint sections that document a verb+URL but omit the Required Fields list and/or a REST Example leave a partner unable to form a valid request. These are gap-report findings, not extractor warnings.

Denominator: **176** matched Endpoint sections (source: `api_reference.extract_api_reference_claims over raw/product-roots` with RF derivation contract).

- Missing Required Fields: **30** / 176
- Missing REST Example: **17** / 176
- Missing both: **10** / 176

## Endpoints with no Required Fields list

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-reg-create-structural-api |
| boarding | `GET` | `/oms/v1/organizations` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-organizations |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-an-organization |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-information-api |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-change-org-status |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-pecs-tms-enable-intro |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-pecs-tms-enable-intro |
| click-to-pay | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#boarding-click-to-pay-enable-intro |
| click-to-pay | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#boarding-click-to-pay-auth-enable-intro |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#ctp-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#boarding-click-to-pay-enable-intro |
| digital-accept-flex | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#boarding-click-to-pay-auth-enable-intro |
| digital-accept-flex | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#ctp-token-get-pymnt-credentials |
| digital-accept-flex | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-token-get-pymnt-details |
| digital-accept-flex | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-token-get-pymnt-details |
| digital-accept-flex | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-auth-tokens |
| digital-accept-flex | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#da-processing-auth-token-task |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#pnt-auth-intro |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-debit-prepaid-disable-part-auth-intro_section_brd_jvn_sxb |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-amex-intro_section_kl3_tbh_xwb |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-jcb-intro |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-mc-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-create-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-create-device-tkn-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tap-create-ii-intro |
| tms | `DELETE` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-delete-intro |
| tms | `GET` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-retrieve-intro |
| tms | `PATCH` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-update-intro |
| tms | `GET` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}/paymentinstruments?` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-retrieve-pi-intro |
| tms | `DELETE` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-delete-intro |
| tms | `GET` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-retrieve-intro |
| tms | `GET` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-retrieve-all-intro |
| tms | `PATCH` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-update-intro |
| tms | `POST` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-create-intro |
| tms | `POST` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-add-nondefault-addr-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-cust-pi-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-create-trans-token-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| tms | `DELETE` | `/tms/v2/tokenized-cards/{id}/bindings/{clientDeviceID}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ctf-delete-binding-intro |
| unified-checkout | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-token-get-pymnt-details |
| unified-checkout | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-auth-tokens |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

## Endpoints with no REST Example

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| invoicing | `POST` | `/invoicing/v2/invoices` | https://developer.cybersource.com/docs/cybs/en-us/invoicing/developer/all/rest/invoicing.html#invoicing-services-create-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

## Endpoints missing both

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

---

# Developers can see the endpoint and still cannot call it

Matched Endpoint sections that document a verb+URL but omit the Required Fields list and/or a REST Example leave a partner unable to form a valid request. These are gap-report findings, not extractor warnings.

Denominator: **176** matched Endpoint sections (source: `api_reference.extract_api_reference_claims over raw/product-roots` with RF derivation contract).

- Missing Required Fields: **30** / 176
- Missing REST Example: **17** / 176
- Missing both: **10** / 176

## Endpoints with no Required Fields list

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-reg-create-structural-api |
| boarding | `GET` | `/oms/v1/organizations` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-organizations |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-an-organization |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-information-api |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-change-org-status |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-pecs-tms-enable-intro |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-pecs-tms-enable-intro |
| click-to-pay | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#boarding-click-to-pay-enable-intro |
| click-to-pay | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#boarding-click-to-pay-auth-enable-intro |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#ctp-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#boarding-click-to-pay-enable-intro |
| digital-accept-flex | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#boarding-click-to-pay-auth-enable-intro |
| digital-accept-flex | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#ctp-token-get-pymnt-credentials |
| digital-accept-flex | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-token-get-pymnt-details |
| digital-accept-flex | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-token-get-pymnt-details |
| digital-accept-flex | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-auth-tokens |
| digital-accept-flex | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#da-processing-auth-token-task |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#pnt-auth-intro |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-debit-prepaid-disable-part-auth-intro_section_brd_jvn_sxb |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-amex-intro_section_kl3_tbh_xwb |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-jcb-intro |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-mc-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-create-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-create-device-tkn-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tap-create-ii-intro |
| tms | `DELETE` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-delete-intro |
| tms | `GET` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-retrieve-intro |
| tms | `PATCH` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-update-intro |
| tms | `GET` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}/paymentinstruments?` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-retrieve-pi-intro |
| tms | `DELETE` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-delete-intro |
| tms | `GET` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-retrieve-intro |
| tms | `GET` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-retrieve-all-intro |
| tms | `PATCH` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-update-intro |
| tms | `POST` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-create-intro |
| tms | `POST` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-add-nondefault-addr-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-cust-pi-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-create-trans-token-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| tms | `DELETE` | `/tms/v2/tokenized-cards/{id}/bindings/{clientDeviceID}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ctf-delete-binding-intro |
| unified-checkout | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-token-get-pymnt-details |
| unified-checkout | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-auth-tokens |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

## Endpoints with no REST Example

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| invoicing | `POST` | `/invoicing/v2/invoices` | https://developer.cybersource.com/docs/cybs/en-us/invoicing/developer/all/rest/invoicing.html#invoicing-services-create-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

## Endpoints missing both

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

---

# Developers can see the endpoint and still cannot call it

Matched Endpoint sections that document a verb+URL but omit the Required Fields list and/or a REST Example leave a partner unable to form a valid request. These are gap-report findings, not extractor warnings.

Denominator: **176** matched Endpoint sections (source: `api_reference.extract_api_reference_claims over raw/product-roots` with RF derivation contract).

- Missing Required Fields: **30** / 176
- Missing REST Example: **17** / 176
- Missing both: **10** / 176

## Endpoints with no Required Fields list

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-reg-create-structural-api |
| boarding | `GET` | `/oms/v1/organizations` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-organizations |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-retrieve-an-organization |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-information-api |
| boarding | `GET` | `/oms/v1/organizations/{organizationId}` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-change-org-status |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-pecs-tms-enable-intro |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-pecs-tms-enable-intro |
| click-to-pay | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#boarding-click-to-pay-enable-intro |
| click-to-pay | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#boarding-click-to-pay-auth-enable-intro |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#ctp-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#boarding-click-to-pay-enable-intro |
| digital-accept-flex | `POST` | `/boarding/v1/registrations` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#boarding-click-to-pay-auth-enable-intro |
| digital-accept-flex | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#ctp-token-get-pymnt-credentials |
| digital-accept-flex | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-token-get-pymnt-details |
| digital-accept-flex | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-token-get-pymnt-details |
| digital-accept-flex | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-auth-tokens |
| digital-accept-flex | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#da-processing-auth-token-task |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#pnt-auth-intro |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-debit-prepaid-disable-part-auth-intro_section_brd_jvn_sxb |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-amex-intro_section_kl3_tbh_xwb |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-jcb-intro |
| payments | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/payments/developer/ctv/rest/payments.html#payments-processing-pa-mc-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-create-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-create-device-tkn-intro |
| tms | `POST` | `/tms/v1/instrumentidentifiers` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tap-create-ii-intro |
| tms | `DELETE` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-delete-intro |
| tms | `GET` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-retrieve-intro |
| tms | `PATCH` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-update-intro |
| tms | `GET` | `/tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}/paymentinstruments?` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ii-tkn-retrieve-pi-intro |
| tms | `DELETE` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-delete-intro |
| tms | `GET` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-retrieve-intro |
| tms | `GET` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-retrieve-all-intro |
| tms | `PATCH` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-update-intro |
| tms | `POST` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-tkn-create-intro |
| tms | `POST` | `/tms/v2/customers/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ship-addr-add-nondefault-addr-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-cust-pi-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-create-trans-token-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| tms | `DELETE` | `/tms/v2/tokenized-cards/{id}/bindings/{clientDeviceID}` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-ctf-delete-binding-intro |
| unified-checkout | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-token-get-pymnt-details |
| unified-checkout | `POST` | `/pts/v2/payments` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-auth-tokens |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

## Endpoints with no REST Example

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| invoicing | `POST` | `/invoicing/v2/invoices` | https://developer.cybersource.com/docs/cybs/en-us/invoicing/developer/all/rest/invoicing.html#invoicing-services-create-intro |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

## Endpoints missing both

| Product | Method | Path | Deep link |
|---|---|---|---|
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#boarding-update-product-api |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-update-batch |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-add-delete-processor |
| boarding | `POST` | `/products/v1/product-setups` | https://developer.cybersource.com/docs/cybs/en-us/boarding/developer/all/rest/boarding.html#pecs-config-payerauth |
| click-to-pay | `GET` | `/flex/v2/payment-credentials/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-credentials |
| click-to-pay | `GET` | `/flex/v2/payment-details/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-token-get-pymnt-details |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-wallet-captures |
| click-to-pay | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/click-to-pay/developer/all/rest/click-to-pay.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-bnpl-captures |
| digital-accept-flex | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/digital-accept-flex/developer/all/rest/digital-accept-flex.html#uc-pay-methods-wallet-captures |
| tms | `POST` | `/tms/v2/tokenize` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-tokenize-intro |
| tms | `POST` | `/tms/v2/tokenized-cards/` | https://developer.cybersource.com/docs/cybs/en-us/tms/developer/all/rest/tms.html#tms-net-tkn-card-validate-otp-intro |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-bnpl-captures |
| unified-checkout | `POST` | `/pts/v2/payments/` | https://developer.cybersource.com/docs/cybs/en-us/unified-checkout/developer/all/rest/unified-checkout.html#uc-pay-methods-wallet-captures |

