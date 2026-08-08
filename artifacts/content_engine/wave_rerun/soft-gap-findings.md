# Soft-gap findings — API reference

Matched Endpoint sections that document a verb+URL but omit the Required Fields list and/or a REST Example leave a partner unable to form a valid request. These are gap-report findings, not extractor warnings.

Denominator: **176** matched Endpoint sections (source: product-roots via extract_api_reference_claims).

- Missing Required Fields: **30** / 176
- Missing REST Example: **17** / 176
- Missing both: **10** / 176
- Matched with Required Fields recovered: **146** / 176

## Derivation contract

Every recovered field is tagged with exactly one of: `api_fields_link`, `required_fields_section`, `sibling_req_fields_page`. Example JSON keys are never used as required fields.

Field tags observed this run: api_fields_link=7631, required_fields_section=3263

## Endpoints with no Required Fields list

- `GET /oms/v1/organizations` — Retrieve a List of Organizations (boarding)
- `GET /oms/v1/organizations/{organizationId}` — Retrieve Organization Details (boarding)
- `GET /oms/v1/organizations/{organizationId}` — Update an Organization's Information (boarding)
- `GET /oms/v1/organizations/{organizationId}` — Change an Organization's Status (boarding)
- `GET /flex/v2/payment-details/` — Payment Details API (click-to-pay)
- `GET /flex/v2/payment-credentials/` — Payment Credentials API (click-to-pay)
- `GET /flex/v2/payment-details/` — Payment Details API (click-to-pay)
- `GET /flex/v2/payment-credentials/` — Payment Credentials API (click-to-pay)
- `POST /pts/v2/payments/` — Captures (click-to-pay)
- `POST /pts/v2/payments/` — Captures (click-to-pay)
- `POST /pts/v2/payments/` — Captures (digital-accept-flex)
- `POST /pts/v2/payments/` — Captures (digital-accept-flex)
- `POST /pts/v2/payments` — Authorizations with a Transient Token (digital-accept-flex)
- `GET /flex/v2/payment-details/` — Payment Details API (digital-accept-flex)
- `GET /flex/v2/payment-details/` — Payment Details API (digital-accept-flex)
- `GET /flex/v2/payment-credentials/` — Payment Credentials API (digital-accept-flex)
- `POST /pts/v2/payments` — Authorization with a Transient Token (digital-accept-flex)
- `POST /pts/v2/payments` — Field Specific to this Use Case (payments)
- `POST /tms/v2/tokenize` — Create Tokens (tms)
- `GET /tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` — Retrieve an Instrument Identifier (tms)
- `PATCH /tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}` — Update an Instrument Identifier (tms)
- `GET /tms/v1/instrumentidentifiers/{instrumentIdentifierTokenId}/paymentinstruments?` — Retrieve an Instrument Identifier's Payment Instruments (tms)
- `GET /tms/v2/customers/` — Retrieve a Customer Shipping Address (tms)
- `GET /tms/v2/customers/` — Retrieve All Customer Shipping Addresses (tms)
- `DELETE /tms/v2/tokenized-cards/{id}/bindings/{clientDeviceID}` — Delete Binding (tms)
- `POST /tms/v2/tokenized-cards/` — Validate a One-Time Password or Issuer Authentication Code (tms)
- `POST /pts/v2/payments/` — Captures (unified-checkout)
- `POST /pts/v2/payments/` — Captures (unified-checkout)
- `POST /pts/v2/payments` — Authorizations with a Transient Token (unified-checkout)
- `GET /flex/v2/payment-details/` — Payment Details API (unified-checkout)
