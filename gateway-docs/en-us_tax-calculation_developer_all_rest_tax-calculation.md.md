Tax Calculation Developer Guide {#tax-about-guide}
==================================================

This section describes the audience and purpose of this guide as well as conventions and related documentation.

Audience and Purpose
--------------------

This guide is written for application developers who want to use the `REST API` to integrate tax calculation into an order management system.  
Implementing the tax calculation service requires software development skills. You must write code that uses the API request and response fields to integrate the tax calculation service into an existing order management system.

Conventions
-----------

The following special statements are used in this document:

> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.
> WARNING
> A *Warning* contains information or instructions, which, if not heeded, can result in a security risk, irreversible loss of data, or significant cost in time or revenue or both.

Testing
-------

We recommend you test all use uses to ensure the tax engine is calculating taxes as expected before going live. Contact `Payment Gateway` Customer Support to have your test account set up to return production-level tax rates for short-term testing needs. You will be required to use a production merchant for testing if you have long-term testing needs that require production-level data for ongoing validation.  
Use the Developer Center to test Value Added Services:  
[https://developer.example.com/api-reference-assets/index.html#value-added-service_taxes_value-added-service](https://developer.example.com/api-reference-assets/index.md#value-added-service_taxes_value-added-service "")

Related Documentation
---------------------

Refer to the Support Center for complete technical documentation:  
[https://docs.example.com/en/index.html](https://developer.example.com/docs.md "")

Customer Support
----------------

For support information about any service, visit the Support Center:  
<http://support.example.com>

Recent Revisions to This Document {#tax-recent-revisions}
=========================================================

26.03.01
--------

This revision contains only editorial changes and no technical updates.

24.02
-----

This revision contains only editorial changes and no technical updates.

24.01
-----

Removed references to `Business Center`.

23.02
-----

This revision contains only editorial changes and no technical updates.

23.01
-----

This revision contains only editorial changes and no technical updates.

21.02
-----

Updated Invalid Tax Calculation.

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Payment Gateway for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Payment Gateway.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR PAYMENT GATEWAY WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.

Overview of Tax Calculation {#tax-overview}
===========================================

The tax calculation service provides real-time tax calculation for worldwide orders placed with your business. It also enables you to avoid the risk and complexity of managing online tax calculation.  
The key services provided allow you to:

* [Calculate Taxes](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-request-calculating-overview.md "")
* [Tax Reporting](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro.md "")

> {#tax-overview_ul_vy3_4ml_z5b} IMPORTANT  
> **IMPORTANT NOTICE FOR USERS OF PAYMENT GATEWAY TAX SERVICES**  
> The tax calculation is based on the location of the customer's taxing jurisdiction, your nexus locations, and the tax and product codes that you provide to Payment Gateway. The order price and quantity are included in the calculation to determine the order's total tax amount. You are solely responsible for selecting the appropriate tax and product codes for your business and its goods and services, including with respect to shipping and handling, and providing those codes to Payment Gateway.  
> PAYMENT GATEWAY DOES NOT PROVIDE TAX CONSULTATION SERVICES, ACCOUNTING OR LEGAL ADVICE AND ASSUMES NO OBLIGATION, LIABILITY OR RESPONSIBILITY FOR ANY INCORRECT, INACCURATE, OR INCOMPLETE INFORMATION PROVIDED TO PAYMENT GATEWAY, OR FOR ANY INCORRECT TAX CALCULATIONS RESULTING FROM SUCH INFORMATION. PAYMENT GATEWAY STRONGLY RECOMMENDS THAT YOU CONSULT WITH A TAX PROFESSIONAL IN CONNECTION WITH YOUR SELECTION OF TAX-RELATED DATA FOR INPUT INTO THE PAYMENT GATEWAY TAX CALCULATION SYSTEM. TO THE EXTENT CUSTOMER USES PAYMENT GATEWAY'S TAX CALCULATION SERVICE, CUSTOMER UNDERSTANDS AND AGREES THAT NEITHER PAYMENT GATEWAY NOR ITS THIRD-PARTY LICENSORS CAN GUARANTEE THE ACCURACY OF TAX OR VAT RATES OBTAINED FROM TAXING AUTHORITIES, AND, (ii) THAT CUSTOMER BEARS THE ULTIMATE RESPONSIBILITY FOR THE PROPER PAYMENT AND REPORTING OF TAXES APPLICABLE TO CUSTOMER'S SALE OF ITS PRODUCTS OR SERVICES.

Additional Information
----------------------

In the `Business Center`, you can view transaction details, process customers' transactions, and manage the Tax Detail Report.  
For more information about tax calculation using the `Business Center`, see [`https://businesscenter.example.com`](https://businesscenter.example.com "").

Prerequisites for Tax Calculation {#tax-plan-planning-for-tax-calculation}
==========================================================================

Before implementing the tax calculation service, you must know the following:

1. Where your business is required to pay tax, and register there. See [Tax Nexus](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview/tax-plan-planning-for-tax-calculation/tax-plan-nexus.md "").
2. Whether any products require special product codes for tax purposes. See [Product Codes](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview/tax-plan-planning-for-tax-calculation/tax-plan-product-codes.md "").
3. The correct address information. See [Address Requirements](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview/tax-plan-planning-for-tax-calculation/tax-plan-address-intro.md "").
4. When to calculate tax in your check out flow. See [When to Calculate Taxes](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview/tax-plan-planning-for-tax-calculation/tax-plan-when-to-calculate-taxes.md "").
   {#tax-plan-planning-for-tax-calculation_ol_gkn_4cb_mvb}

Tax Nexus {#tax-plan-nexus}
===========================

When your company has *nexus* in the US or Canada, you might be required to collect sales tax or sellers use tax in those countries. You can establish nexus in a state or province in various ways. For example:

* Your company has a physical presence in the US or Canada such as office space, warehouse space, paid staff, or inventory.
* Your company sells a sufficiently large volume of goods in the US or Canada to have *economic* nexus.

Each state and province has its own rules for determining nexus. Consult your tax advisor to determine where you have nexus.

> IMPORTANT  
> In your tax calculation service request, specify the states in which you have nexus by populating the taxInformation.nexus or taxInformation.noNexus API fields. When you do not include one of these fields in a tax calculation service request, the tax system makes its calculations as if you have nexus in every state.  
> For more information, see [Step 1: Nexus](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-request-calculating-overview/tax-overview-us-sales-tax-descr/tax-request-calculating-us-and-canadian-tax.md#tax-request-calculating-us-and-canadian-tax_step-one-nexus "").

Product Codes {#tax-plan-product-codes}
=======================================

When you request the tax calculation service, you can provide a separate product code for each item in the order. A product code is required in order to trigger product-based rules and exemptions. When you do not include a product code in your request, or when you include an invalid product code, the tax calculation service assumes that the product has no product-based tax exemptions and is fully taxable.

> IMPORTANT To use a product code that is not listed in the available guides, contact customer support for information about how to proceed.

US and Canadian Tax
-------------------

Products that are fully taxable in all states do not need a product code because they do not have tax exemption in any state. For tax-exempt products or those with non-standard tax rates, use the product codes in the `Payment Gateway` tax codes guide, which can be requested each month from customer support.  
To use a product code that is not listed in the guide, contact customer support for information about how to proceed. Until the product code is supported, you can override the tax amount for the product by sending the amount of tax to apply to the item in the orderInformation.amountDetails.taxAmount field.  
For more information, see [Step 2: Product Codes](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-request-calculating-overview/tax-overview-us-sales-tax-descr/tax-request-calculating-us-and-canadian-tax.md#tax-request-calculating-us-and-canadian-tax_step-two-codes "").

International Tax and VAT
-------------------------

For a list of available product codes for international taxes or VAT, see the `Payment Gateway` tax codes guide. For information about these codes, contact customer support.

Address Requirements {#tax-plan-address-intro}
==============================================

The tax calculation service requires specific address information be provided in order to properly calculate tax. This section goes over how the tax calculation service uses address information to calculate tax.

> IMPORTANT
> There is additional address related information in the US and Canada section that explains specific request fields. See [US and Canadian Addresses](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-request-calculating-overview/tax-overview-us-sales-tax-descr/tax-request-calculating-us-and-canadian-tax.md#tax-request-calculating-us-and-canadian-tax_address "").

Multiple Shipping Destinations in a Single Order
------------------------------------------------

You cannot specify a different shipping address for each item in an order. When the order contains multiple items that are going to different addresses, you must send a separate tax calculation service request for each shipping address.

Missing Origin Addresses
------------------------

The destination address is substituted for the origin address when no origin address or a partial origin address is specified. For the best results, use fully validated origin and destination addresses.

Invalid Address Combination Correction
--------------------------------------

The tax calculation service performs an implicit address validation; if successful, the entire address is used for tax calculation  
In case the full address validation failed, engine looks for "Zip + 4" -- if it has been provided. If provided, tax is calculated with the "Zip + 4". If "Zip + 4" is not provided or is incorrect, engine looks for "City \& State" or Zip; if either are provided and are accurate, tax is calculated based on these details. If the zip code does NOT lie within the state, then the city and state are used to determine the region for the tax calculation. Note: In certain cases, Zip alone is not enough to accurately determine the jurisdictions; in such cases, engine looks for additional information -- such as Address Lines or City and State. If either is provided and enables identification of the jurisdictions, the successful tax calculation is returned. As Jurisdiction data is in a regular state of change, partial addresses can produce different results over time as the jurisdictions and tax authorities change.  
Abbreviations used for some city and county names are acceptable in more than one form. For example, St. Louis is acceptable as *Saint Louis* , *St Louis* , and *St. Louis* . See [City Abbreviations](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-info-city-abbrevs.md "").

When to Calculate Taxes {#tax-plan-when-to-calculate-taxes}
===========================================================

You can calculate tax at these times during the order process:

* When the customer prompts for a subtotal or total.
* When the customer performs a final check out.
* When the order ships, which ensures that the current tax rate is applied to the order.

> IMPORTANT  
> As you determine how and where to implement the Tax Calculation Service on your website, consider that the Global Tax Calculation Service is billable for each request. To offset your costs and optimize your pricing, consider waiting to request a tax calculation until after your customer has entered their shipping or billing address on the checkout page. This minimizes the number of tax calculation requests for a single transaction. To ensure that your business complies with tax laws, work with a tax advisor to determine when to calculate tax.  
> For more information on when to calculate US and Canadian taxes, see [Step 4: When to Calculate Tax](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-request-calculating-overview/tax-overview-us-sales-tax-descr/tax-request-calculating-us-and-canadian-tax.md#tax-request-calculating-us-and-canadian-tax_step-four-when "").

Tax Calculation {#concept_xxx_tqb_mvb}
======================================

The service can calculate the following types of taxes:

* US sales and sellers use tax
* Canadian sales tax (GST, PST, HST, QST)
* International (non-US/Canadian) and Value-Added Tax (VAT)

{#concept_xxx_tqb_mvb_ul_gbt_sxd_bwb}  
The calculation is based on the location of the customer's taxing jurisdiction, your nexus locations, and the product codes that you provide. The order price and quantity are included in the calculation.  
The tax calculation service is not recommended for merchants conducting business with unsupported countries. See [Supported Countries and Regions](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-info-supported-country-regions.md "").

US and Canadian Tax Calculation {#tax-overview-us-sales-tax-descr}
==================================================================

The tax calculation service uses the same request to calculate US and Canadian sales tax due to their similarities, but there are some distinguishing factors that should be known.

US Sales Tax
------------

Sales tax is imposed on a transfer of property. Some states do not have sales tax. For US orders, the tax calculation service includes the total tax value for the transaction and tax values and rates per jurisdiction, divided into national, state, county, city, and special taxes. Some states do not have sales tax.

Canadian Taxes
--------------

The same procedures apply to calculating taxes for Canada as for the United States. Use only Canadian dollars for all Canadian taxes. The tax calculation service returns:

* GST as a country-level tax
* PST and QST as state-level taxes
* HST as the sum of GST and PST

If you want the tax calculation service to return HST as one field, contact customer support to configure your account accordingly.

Calculating US and Canadian Tax {#tax-request-calculating-us-and-canadian-tax}
==============================================================================

To receive the most accurate tax calculation, you will need specific information for the field values. Follow these steps to determine the values for the fields.
IMPORTANT One tax service request should not include more than 50 line items. When you send a request with more than 50 line items, the request could time out.  
The Tax Calculation Service uses line-level rounding. Tax amounts for each jurisdictional detail will be rounded and then aggregated to the line. For example, 8.5% total tax that includes 1.25% city tax, 1.25% county tax, and 6% state tax, levied on a 10.00 item would result in a total tax of 0.86 based on amounts of 0.13 city tax, 0.13 county tax, and 0.60 state tax.

Step 1: Nexus {#tax-request-calculating-us-and-canadian-tax_step-one-nexus}
---------------------------------------------------------------------------

Identify the location of your company's nexus. Products are taxable only when the customer's orderInformation.shipTo.administrativeArea field value matches a state or province in which your company has nexus. If the ship to fields are not included in the request, the service will use the bill to fields to determine the tax amount. Use the taxInformation.nexus field to list the states or provinces in which your company has nexus. Alternatively, you can use the taxInformation.noNexus field to list states that should not be taxed.

> IMPORTANT
> You cannot combine the taxInformation.nexus and taxInformation.noNexus fields in the same request.  
> When you do not specify your nexus locations, the tax calculation service processes your request as if every state or province is taxable.

* When you do not specify your nexus locations, or when a value of the nexus field matches the value for the orderInformation.shipTo.administrativeArea field, the service calculates the applicable tax for the product.
* When the value for the orderInformation.shipTo.administrativeArea field does not match any state or province where you have nexus, the service assigns zero tax.

For more information, see [Tax Nexus](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview/tax-plan-planning-for-tax-calculation/tax-plan-nexus.md "").

Step 2: Product Codes {#tax-request-calculating-us-and-canadian-tax_step-two-codes}
-----------------------------------------------------------------------------------

If the product has special tax considerations, you can provide the appropriate tax product code in the orderInformation.lineItems.productCode field in the request.  
For more information, see [Product Codes](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview/tax-plan-planning-for-tax-calculation/tax-plan-product-codes.md "").

Step 3: Addresses {#tax-request-calculating-us-and-canadian-tax_address}
------------------------------------------------------------------------

To receive the most accurate tax calculation possible, include the following address information in the request:

* Ship-to address, in fields in the orderInformation.shipTo object. When multiple cities are within a postal code area, the optional request field orderInformation.shipTo.locality value improves the accuracy of the calculated tax.
* Ship-from address, in fields in the orderInformation.shipFrom object.
* Point-of-order acceptance, in fields in the orderInformation.orderAcceptance object.
* Point-of-order origin, in fields in the orderInformation.orderOrigin object.
* Product code, in the orderInformation.lineItems.productCode field.
* Nexus, in the taxInformation.nexus field---or if it is easier, you can use the taxInformation.noNexus field to provide a list of states in which you do not have nexus.

When the tax calculation service succeeds, the response includes the orderInformation.amountDetails.totalAmount field. When the optional request-level field taxInformation.showTaxPerLineItem is set to `yes`, the response also includes the following fields for each offer:

* orderInformation.taxDetails.type with the value of `city`, `country`, `county`, `special`, or `state`.
* orderInformation.lineItems.jurisdiction object fields that provide detailed tax information.

For more address-related information, see [Address Requirement](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview/tax-plan-planning-for-tax-calculation/tax-plan-address-intro.md "").

Step 4: When to Calculate Tax {#tax-request-calculating-us-and-canadian-tax_step-four-when}
-------------------------------------------------------------------------------------------

Determine when you will provide tax calculations during the customer transaction. Tax calculation can occur before or after determining the final order total. See Tax Reporting to know how this service can impact when you would want to request the tax service.  
For more information, see [When to Calculate Taxes](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview/tax-plan-planning-for-tax-calculation/tax-plan-when-to-calculate-taxes.md "").

Endpoint {#tax-request-calculating-us-and-canadian-tax_tax-endpoint}
--------------------------------------------------------------------

`POST ``https://api.example.com``/vas/v2/tax`{#tax-request-calculating-us-and-canadian-tax_restinitiate-altpay}

Required Fields for a Tax Calculation Using the `REST API` {#tax-calc-req-required-fields}
==========================================================================================

Use these fields to perform a tax calculation.

clientReferenceInformation.code
:

orderInformation.lineItems.unitPrice
:

orderInformation.billTo.country
:

orderInformation.billTo.postalCode
:

orderInformation.billTo.locality
:

orderInformation.billTo.administrativeArea
:

taxInformation.showTaxPerLineItem
:

taxInformation.nexus
:
If you include this field, do not include the taxInformation.noNexus field.

taxInformation.noNexus
:
If you include this field, do not include the taxInformation.nexus field.

Optional Fields for a Tax Calculation Using the REST API {#tax-calc-req-opt-fields}
===================================================================================

Use these optional fields to perform a tax calculation.

clientReferenceInformation.code
:

clientReferenceInformation.partner.developerId
:

clientReferenceInformation.partner.solutionId
:

orderInformation.amountDetails.currency
:

orderInformation.billTo.address1
:

orderInformation.billTo.address2
:

orderInformation.invoiceDetails.invoiceDate
:

orderInformation.lineItems.orderAcceptance.administrativeArea
:

orderInformation.lineItems.orderAcceptance.country
:

orderInformation.lineItems.orderAcceptance.locality
:

orderInformation.lineItems.orderAcceptance.postalCode
:

orderInformation.lineItems.orderOrigin.administrativeArea
:

orderInformation.lineItems.orderOrigin.country
:

orderInformation.lineItems.orderOrigin.locality
:

orderInformation.lineItems.orderOrigin.postalCode
:

orderInformation.lineItems.productCode
:

orderInformation.lineItems.productName
:

orderInformation.lineItems.productSku
:

orderInformation.lineItems.quantity
:

orderInformation.lineItems.shipFromAdministrativeArea
:

orderInformation.lineItems.shipFromCountry
:

orderInformation.lineItems.shipFromLocality
:

orderInformation.lineItems.shipFromPostalCode
:

orderInformation.lineItems.taxAmount
:

orderInformation.orderAcceptance.administrativeArea
:

orderInformation.orderAcceptance.country
:

orderInformation.orderAcceptance.locality
:

orderInformation.orderAcceptance.postalCode
:

orderInformation.orderOrigin.administrativeArea
:

orderInformation.orderOrigin.country
:

orderInformation.orderOrigin.locality
:

orderInformation.orderOrigin.postalCode
:

orderInformation.shippingDetails.shipFromAdministrativeArea
:

orderInformation.shippingDetails.shipFromCountry
:

orderInformation.shippingDetails.shipFromLocality
:

orderInformation.shippingDetails.shipFromPostalCode
:

orderInformation.shipTo.address1
:

orderInformation.shipTo.address2
:

orderInformation.shipTo.address3
:

orderInformation.shipTo.administrativeArea
:

orderInformation.shipTo.country
:

orderInformation.shipTo.locality
:

orderInformation.shipTo.postalCode
:

taxInformation.commitIndicator
:
Set field to `true` to commit tax calculation.

taxInformation.dateOverrideReason
:

taxInformation.refundIndicator
:

taxInformation.reportingDate
:

taxInformation.showTaxPerLineItem
:

Example: Processing a Tax Calculation Using the REST API {#tax-calc-req-ex-rest}
================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "TAX_TC001"
  },
  "taxInformation": {
    "nexus":["CA","TX","AL"],
    "showTaxPerLineItem": "Yes"
  },
  "orderInformation": {
    "amountDetails": {
      "currency": "USD"
    },
    "billTo": {
      "address1": "1 Market St",
      "locality": "San Francisco",
      "administrativeArea": "CA",
      "postalCode": 94105,
      "country": "US"
    },
    "lineItems": [
      {
        "productSKU": "07-12-00657",
        "productCode": "PO000000",
        "quantity": 1,
        "productName": "Chewing Gum",
        "unitPrice": 1200
      }
    ]
  }
}
```

Response

```
{
  "_links": {
    "void": {
      "method": "PATCH",
      "href": "/vas/v2/tax/6679349380866991503954"
    }
  },
  "clientReferenceInformation": {
    "code": "TAX_TC001"
  },
  "id": "6679349380866991503954",
  "orderInformation": {
    "lineItems": [
      {
        "taxableAmount": "1200.00",
        "taxDetails": [
          {
            "amount": "0.00",
            "type": "city"
          },
          {
            "amount": "28.50",
            "type": "special"
          },
          {
            "amount": "72.00",
            "type": "state"
          },
          {
            "amount": "3.00",
            "type": "county"
          },
          {
            "amount": "0.00",
            "type": "national"
          }
        ],
        "jurisdiction": [
          {
            "country": "US",
            "code": "06",
            "taxable": "1200.00",
            "rate": "0.060000",
            "name": "CALIFORNIA",
            "type": "State",
            "region": "CA",
            "taxAmount": "72.00",
            "taxName": "CA STATE TAX"
          },
          {
            "country": "US",
            "code": "075",
            "taxable": "1200.00",
            "rate": "0.002500",
            "name": "SAN FRANCISCO",
            "type": "County",
            "region": "CA",
            "taxAmount": "3.00",
            "taxName": "CA COUNTY TAX"
          },
          {
            "country": "US",
            "code": "EMBE0",
            "taxable": "1200.00",
            "rate": "0.013750",
            "name": "SAN FRANCISCO COUNTY DISTRICT TAX SP",
            "type": "Special",
            "region": "CA",
            "taxAmount": "16.50",
            "taxName": "CA SPECIAL TAX"
          },
          {
            "country": "US",
            "code": "EMTV0",
            "taxable": "1200.00",
            "rate": "0.010000",
            "name": "SAN FRANCISCO CO LOCAL TAX SL",
            "type": "Special",
            "region": "CA",
            "taxAmount": "12.00",
            "taxName": "CA SPECIAL TAX"
          }
        ],
        "exemptAmount": "0.00",
        "taxAmount": "103.50"
      }
    ],
    "taxableAmount": "1200.00",
    "taxDetails": [
      {
        "amount": "28.50",
        "type": "special"
      },
      {
        "amount": "72.00",
        "type": "state"
      },
      {
        "amount": "0.00",
        "type": "national"
      },
      {
        "amount": "3.00",
        "type": "county"
      },
      {
        "amount": "0.00",
        "type": "city"
      }
    ],
    "exemptAmount": "0.00",
    "taxAmount": "103.50",
    "amountDetails": {
      "totalAmount": "1303.50",
      "currency": "USD"
    }
  },
  "status": "COMPLETED",
  "submitTimeUtc": "2022-11-08T19:15:38Z",
  "taxInformation": {
    "commitIndicator": "true",
    "refundIndicator": "false"
  }
}
```

International Taxes and Value-Added Tax (VAT) Calculation {#tax-overview-intl-vat-descr}
========================================================================================

International taxes are calculated for countries other than the US Specifically, some countries have a VAT, which is sales tax chargeable on most goods and services. A VAT seller registration number is assigned to sellers and required to calculate international taxes in most countries. International and VAT calculation is supported in specific countries. See [Supported Countries and Regions](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-info-supported-country-regions.md "").  
When you request the tax service and the product is being shipped to or consumed in one of the following countries, tax is calculated by default. The seller registration number is not required in order to calculate tax in these locations:

* Canada
* China
* Congo, Republic of the
* Congo, the Democratic Republic of the
* Lake Lugano, Territorial Waters of
* Lao People's Democratic Republic
* Macedonia, Republic of North
* South Georgia and the South Sandwich Islands
* United Kingdom
* United States

Calculating International Tax and VAT {#tax-request-calculating-international-tax-vat}
======================================================================================

Before calculating international tax, make sure that the country is on the list of [Supported Countries and Regions](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-info-supported-country-regions.md "").

> IMPORTANT One tax service request should not include more than 50 line items. When you send a request with more than 50 line items, the request could time out.

VAT Number
----------

When you include the `merchantInformation.vatRegistrationNumber` or `orderInformation.lineItems.vatRegistrationNumber` field and VAT rules and rates are applicable, the service calculates a VAT tax, and the relevant tax amounts are returned in the response.  
There are some countries where VAT registration is not required. More details are mentioned in [Supported Countries and Regions](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-info-supported-country-regions.md "").

Product Codes
-------------

If a product is subject to special tax considerations, provide the appropriate tax product code in the `orderInformation.lineItems.productCode` field in the request. To use a product code that is not listed in the available guides, contact customer support for information about how to proceed.

Tax Per Item
------------

When the tax calculation service succeeds, the response includes a tax amount for each item and indicates whether the tax amount was calculated by the tax calculation service or provided by you.

Endpoint {#tax-request-calculating-international-tax-vat_tax-endpoint}
----------------------------------------------------------------------

`POST ``https://api.example.com``/vas/v2/tax`{#tax-request-calculating-international-tax-vat_restinitiate-altpay}

Required Fields for an International Tax and VAT Calculation Using the `REST API` {#tax-calc-req-int-required-fields}
=====================================================================================================================

Use these fields to perform a tax calculation.

merchantInformation.vatRegistrationNumber
:

orderInformation.amountDetails.currency
:

orderInformation.billTo.country
:

orderInformation.lineItems.unitPrice
:
{#tax-calc-req-int-required-fields_dl_mmz_1ys_lvb}

Optional Fields for an International Tax and VAT Calculation Using the `REST API` {#tax-calc-req-int-optional-fields}
=====================================================================================================================

Select from these optional fields to perform a tax calculation.

buyerInformation.vatRegistrationNumber
:

clientReferenceInformation.code
:

clientReferenceInformation.partner.developerId
:

clientReferenceInformation.partner.solutionId
:

orderInformation.billTo.address1
:

orderInformation.billTo.address2
:

orderInformation.billTo.administrativeArea
:

orderInformation.billTo.locality
:

orderInformation.billTo.postalCode
:

orderInformation.invoiceDetails.invoiceDate
:

orderInformation.lineItems.buyerVatRegistrationNumber
:

orderInformation.lineItems.orderAcceptance.administrativeArea
:

orderInformation.lineItems.orderAcceptance.country
:

orderInformation.lineItems.orderAcceptance.locality
:

orderInformation.lineItems.orderAcceptance.postalCode
:

orderInformation.lineItems.orderOrigin.administrativeArea
:

orderInformation.lineItems.orderOrigin.country
:

orderInformation.lineItems.orderOrigin.locality
:

orderInformation.lineItems.orderOrigin.postalCode
:

orderInformation.lineItems.productCode
:

orderInformation.lineItems.productName
:

orderInformation.lineItems.productSku
:

orderInformation.lineItems.quantity
:

orderInformation.lineItems.sellerVatRegistrationNumber
:

orderInformation.lineItems.shipFromAdministrativeArea
:

orderInformation.lineItems.shipFromCountry
:

orderInformation.lineItems.shipFromLocality
:

orderInformation.lineItems.shipFromPostalCode
:

orderInformation.lineItems.taxAmount
:

orderInformation.orderAcceptance.administrativeArea
:

orderInformation.orderAcceptance.country
:

orderInformation.orderAcceptance.locality
:

orderInformation.orderAcceptance.postalCode
:

orderInformation.orderOrigin.administrativeArea
:

orderInformation.orderOrigin.country
:

orderInformation.orderOrigin.locality
:

orderInformation.orderOrigin.postalCode
:

orderInformation.shippingDetails.shipFromAdministrativeArea
:

orderInformation.shippingDetails.shipFromCountry
:

orderInformation.shippingDetails.shipFromLocality
:

orderInformation.shippingDetails.shipFromPostalCode
:

orderInformation.shipTo.address1
:

orderInformation.shipTo.address2
:

orderInformation.shipTo.address3
:

orderInformation.shipTo.administrativeArea
:

orderInformation.shipTo.country
:

orderInformation.shipTo.locality
:

orderInformation.shipTo.postalCode
:

taxInformation.commitIndicator
:
Set field to `true` to commit tax calculation.

taxInformation.dateOverrideReason
:

taxInformation.nexus
:
If you include this field, do not include the taxInformation.noNexus field.

taxInformation.noNexus
:
If you include this field, do not include the taxInformation.nexus field.

taxInformation.refundIndicator
:

taxInformation.reportingDate
:

taxInformation.showTaxPerLineItem
:

Example: Processing an International Tax Calculation Using the REST API {#tax-calc-req-int-ex-rest}
===================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "TAX_TC001"
  },
  "taxInformation": {
    "showTaxPerLineItem": "Yes"
  },
  "orderInformation": {
    "amountDetails": {
      "currency": "EUR"
    },
    "billTo": {
      "country": "FR"
    },
    "lineItems": [
      {
        "productSKU": "07-12-00657",
        "productCode": "P0000000",
        "quantity": 1,
        "productName": "Chewing Gum",
        "unitPrice": 1200
      }
    ]
  },
  "merchantInformation": {
    "vatRegistrationNumber": "123456789"
  }
}
```

Response

```
{
  "_links": {
    "void": {
      "method": "PATCH",
      "href": "/vas/v2/tax/6679363184546074003954"
    }
  },
  "clientReferenceInformation": {
    "code": "TAX_TC001"
  },
  "id": "6679363184546074003954",
  "orderInformation": {
    "lineItems": [
      {
        "taxDetails": [
          {
            "amount": "240.00",
            "type": "national"
          }
        ],
        "jurisdiction": [
          {
            "country": "FR",
            "code": "FR",
            "taxable": "1200.00",
            "rate": "0.200000",
            "name": "FRANCE",
            "type": "Country",
            "region": "FR",
            "taxAmount": "240.00",
            "taxName": "Standard"
          }
        ],
        "taxAmount": "240.00"
      }
    ],
    "taxDetails": [
      {
        "amount": "240.00",
        "type": "national"
      }
    ],
    "taxAmount": "240.00",
    "amountDetails": {
      "totalAmount": "1440.00",
      "currency": "EUR"
    }
  },
  "status": "COMPLETED",
  "submitTimeUtc": "2022-11-08T19:38:38Z",
  "taxInformation": {
    "commitIndicator": "false",
    "refundIndicator": "false"
  }
}
```

Tax Reporting {#concept_grm_2ks_lvb}
====================================

The tax reporting features are available for businesses who use the `Payment Gateway` Tax Calculation service. These features are used to populate the Tax Detail Report for tax reporting and reconciliation. They have no impact on the payment transactions.  
Tax Reporting features include these services:

* [Commit Tax Calculation](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-com-call-intro.md "")
* [Refund Tax Calculation](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-calc-refund-intro.md "")
* [Void Tax Calculation](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-void-intro.md "")

{#concept_grm_2ks_lvb_ul_ksx_k31_mvb} IMPORTANT One tax service request should not include more than 50 line items. When you send a request with more than 50 line items, the request could time out.

Commit Tax Calculation {#tax-com-call-intro}
============================================

Commit a tax calculation to indicate in the Tax Detail Report that the calculated tax amount in the tax request was added to a successful capture or refund transaction.

Tax Detail Report
-----------------

The commit request will set the Status field in the Tax Detail Report to Committed.

Fields specific to this Use Case
--------------------------------

Include the following information with a standard tax calculation request when you want to include the request to your Tax Detail Report:

* To commit a tax calculation request, set the taxInformation.commitIndicator field to `true`.

{#tax-com-call-intro_ul_sxk_l4t_lvb} IMPORTANT
The Status field in the Tax Detail Report will default to ` uncommitted ` if the taxInformation.commitIndicator field is not present.

Commit Tax Calculation Scenarios {#tax-scenario-com-intro}
==========================================================

You can commit tax calculation requests at different moments in a transaction.  
Use these scenario examples to determine when it would be best for you to commit a tax calculation.  
Possible scenarios:

* [Scenario 1: Pre-authorization](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-com-call-intro/tax-scenario-com-intro/tax-scenario-com-one.md "")
* [Scenario 2: Post-capture](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-com-call-intro/tax-scenario-com-intro/tax-scenario-com-two.md "")
* [Scenario 3: Partial Captures](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-com-call-intro/tax-scenario-com-intro/tax-scenario-com-three.md "")
  {#tax-scenario-com-intro_ul_tvk_gn3_vwb}

Scenario 1: Pre-authorization {#tax-scenario-com-one}
=====================================================

You can commit a tax calculation request before requesting an authorization. For example:

1. Request the tax calculation service with the taxInformation.commitIndicator field set to `true`.{#tax-scenario-com-one_step1}
   {#tax-scenario-com-one_step1}
2. Authorize and capture payment.{#tax-scenario-com-one_step2}
   {#tax-scenario-com-one_step2}
3. If the authorization or capture fails, void the previously committed tax calculation request. See [Void Tax Calculation](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-void-intro.md "").{#tax-scenario-com-one_step3}
   {#tax-scenario-com-one_step3} {#tax-scenario-com-one_steps-commit}

Scenario 2: Post-capture {#tax-scenario-com-two}
================================================

You can commit a tax request after a capture. If you implement the tax service in this way, you will have to request the tax calculation service at least twice per request. For example:

1. Request the tax calculation service with the commit indicator field set to taxInformation.commitIndicator set to `false`.
2. Authorize and capture the payment.
3. If the authorization and capture are successful, request the tax calculation service with the taxInformation.commitIndicator set to `true`.

Scenario 3: Partial Captures {#tax-scenario-com-three}
======================================================

You can commit a tax request for partial captures. For example:

1. Request the tax calculation service with the commit indicator field set to taxInformation.commitIndicator set to `false`.
2. Authorize the payment for $0 or wait to authorize partial payments as items are transferred to the customer.
3. Implement [Scenario 1](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-com-call-intro/tax-scenario-com-intro/tax-scenario-com-one.md "") or [Scenario 2](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-com-call-intro/tax-scenario-com-intro/tax-scenario-com-two.md "") as you make authorizations and captures.

US and Canada Tax Commit {#tax-request-calculating-uscan}
=========================================================

This section shows the fields necessary to commit US and Canadian tax calculation.  
To commit a tax calculation, include the taxInformation.commitIndicator field set to `true` in a tax calculation request.

Endpoint {#tax-request-calculating-uscan_tax-endpoint}
------------------------------------------------------

`POST ``https://api.example.com``/vas/v2/tax`{#tax-request-calculating-uscan_restinitiate-altpay}

Required Fields for a Committed Tax Request Using the REST API {#tax-com-call-required-fields}
==============================================================================================

Use these fields to perform a committed tax request.

clientReferenceInformation.code
:

orderInformation.billTo.administrativeArea
:

orderInformation.billTo.country
:

orderInformation.billTo.locality
:

orderInformation.billTo.postalCode
:

orderInformation.lineItems.unitPrice
:

taxInformation.nexus
:
If you include this field, do not include the taxInformation.noNexus field.

taxInformation.noNexus
:
If you include this field, do not include the taxInformation.nexus field.

taxInformation.showTaxPerLineItem
:

taxInformation.commitIndicator
:
Set to `true`.
{#tax-com-call-required-fields_dl_yms_3mh_vwb}

Optional Fields for a Committed Tax Request Using the REST API {#tax-com-call-optional-fields}
==============================================================================================

Select from these optional fields to commit a tax request.

clientReferenceInformation.code
:

clientReferenceInformation.partner.developerId
:

clientReferenceInformation.partner.solutionId
:

orderInformation.amountDetails.currency
:

orderInformation.billTo.address1
:

orderInformation.billTo.address2
:

orderInformation.invoiceDetails.invoiceDate
:

orderInformation.lineItems.orderAcceptance.administrativeArea
:

orderInformation.lineItems.orderAcceptance.country
:

orderInformation.lineItems.orderAcceptance.locality
:

orderInformation.lineItems.orderAcceptance.postalCode
:

orderInformation.lineItems.orderOrigin.administrativeArea
:

orderInformation.lineItems.orderOrigin.country
:

orderInformation.lineItems.orderOrigin.locality
:

orderInformation.lineItems.orderOrigin.postalCode
:

orderInformation.lineItems.productCode
:

orderInformation.lineItems.productName
:

orderInformation.lineItems.productSku
:

orderInformation.lineItems.quantity
:

orderInformation.lineItems.shipFromAdministrativeArea
:

orderInformation.lineItems.shipFromCountry
:

orderInformation.lineItems.shipFromLocality
:

orderInformation.lineItems.shipFromPostalCode
:

orderInformation.lineItems.taxAmount
:

orderInformation.orderAcceptance.administrativeArea
:

orderInformation.orderAcceptance.country
:

orderInformation.orderAcceptance.locality
:

orderInformation.orderAcceptance.postalCode
:

orderInformation.orderOrigin.administrativeArea
:

orderInformation.orderOrigin.country
:

orderInformation.orderOrigin.locality
:

orderInformation.orderOrigin.postalCode
:

orderInformation.shippingDetails.shipFromAdministrativeArea
:

orderInformation.shippingDetails.shipFromCountry
:

orderInformation.shippingDetails.shipFromLocality
:

orderInformation.shippingDetails.shipFromPostalCode
:

orderInformation.shipTo.address1
:

orderInformation.shipTo.address2
:

orderInformation.shipTo.address3
:

orderInformation.shipTo.administrativeArea
:

orderInformation.shipTo.country
:

orderInformation.shipTo.locality
:

orderInformation.shipTo.postalCode
:

taxInformation.commitIndicator
:
Set field to `true` to commit tax calculation.

taxInformation.dateOverrideReason
:

taxInformation.refundIndicator
:

taxInformation.reportingDate
:

taxInformation.showTaxPerLineItem
:

Example: Processing a Committed Tax Request Using the REST API {#tax-com-call-ex-rest}
======================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "TAX_TC001"
  },
  "taxInformation": {
    "nexus": ["CA","TX","AL"],
    "showTaxPerLineItem": "Yes",
    "commitIndicator": "true"
  },
  "orderInformation": {
    "amountDetails": {
      "currency": "USD"
    },
    "billTo": {
      "address1": "1 Market St",
      "locality": "San Francisco",
      "administrativeArea": "CA",
      "postalCode": 94105,
      "country": "US"
    },
    "lineItems": [
      {
        "productSKU": "07-12-00657",
        "productCode": "PO000000",
        "quantity": 1,
        "productName": "Chewing Gum",
        "unitPrice": 1200
      }
    ]
  }
}
```

Response

```
{
  "_links": {
    "void": {
      "method": "PATCH",
      "href": "/vas/v2/tax/6679349380866991503954"
    }
  },
  "clientReferenceInformation": {
    "code": "TAX_TC001"
  },
  "id": "6679349380866991503954",
  "orderInformation": {
    "lineItems": [
      {
        "taxableAmount": "1200.00",
        "taxDetails": [
          {
            "amount": "0.00",
            "type": "city"
          },
          {
            "amount": "28.50",
            "type": "special"
          },
          {
            "amount": "72.00",
            "type": "state"
          },
          {
            "amount": "3.00",
            "type": "county"
          },
          {
            "amount": "0.00",
            "type": "national"
          }
        ],
        "jurisdiction": [
          {
            "country": "US",
            "code": "06",
            "taxable": "1200.00",
            "rate": "0.060000",
            "name": "CALIFORNIA",
            "type": "State",
            "region": "CA",
            "taxAmount": "72.00",
            "taxName": "CA STATE TAX"
          },
          {
            "country": "US",
            "code": "075",
            "taxable": "1200.00",
            "rate": "0.002500",
            "name": "SAN FRANCISCO",
            "type": "County",
            "region": "CA",
            "taxAmount": "3.00",
            "taxName": "CA COUNTY TAX"
          },
          {
            "country": "US",
            "code": "EMBE0",
            "taxable": "1200.00",
            "rate": "0.013750",
            "name": "SAN FRANCISCO COUNTY DISTRICT TAX SP",
            "type": "Special",
            "region": "CA",
            "taxAmount": "16.50",
            "taxName": "CA SPECIAL TAX"
          },
          {
            "country": "US",
            "code": "EMTV0",
            "taxable": "1200.00",
            "rate": "0.010000",
            "name": "SAN FRANCISCO CO LOCAL TAX SL",
            "type": "Special",
            "region": "CA",
            "taxAmount": "12.00",
            "taxName": "CA SPECIAL TAX"
          }
        ],
        "exemptAmount": "0.00",
        "taxAmount": "103.50"
      }
    ],
    "taxableAmount": "1200.00",
    "taxDetails": [
      {
        "amount": "28.50",
        "type": "special"
      },
      {
        "amount": "72.00",
        "type": "state"
      },
      {
        "amount": "0.00",
        "type": "national"
      },
      {
        "amount": "3.00",
        "type": "county"
      },
      {
        "amount": "0.00",
        "type": "city"
      }
    ],
    "exemptAmount": "0.00",
    "taxAmount": "103.50",
    "amountDetails": {
      "totalAmount": "1303.50",
      "currency": "USD"
    }
  },
  "status": "COMPLETED",
  "submitTimeUtc": "2022-11-08T19:15:38Z",
  "taxInformation": {
    "commitIndicator": "true",
    "refundIndicator": "false"
  }
}
```

International Tax and VAT Committed Tax Calculation {#tax-com-call-int-intro}
=============================================================================

Use a committed tax calculation to include the owed tax amount with a capture.  
To commit a tax calculation, include the taxInformation.commitIndicator field set to `true` in a tax calculation request.

Endpoint {#tax-com-call-int-intro_tax-endpoint}
-----------------------------------------------

`POST ``https://api.example.com``/vas/v2/tax`{#tax-com-call-int-intro_restinitiate-altpay}

Required Fields for an International Tax and VAT Committed Tax Calculation Using the REST API {#tax-com-call-int-required-fields}
=================================================================================================================================

Use these fields to perform a committed tax request.

merchantInformation.vatRegistrationNumber
:

orderInformation.amountDetails.currency
:

orderInformation.billTo.country
:

orderInformation.lineItems.unitPrice
:

taxInformation.showTaxPerLineItem. commitIndicator
:
Set to `true`.
{#tax-com-call-int-required-fields_dl_mmz_1ys_lvb}

Optional Fields for an International Tax and VAT Committed Tax Calculation Using the REST API {#tax-com-call-int-optional-fields}
=================================================================================================================================

Use these fields to perform a committed tax request.

buyerInformation.vatRegistrationNumber
:

clientReferenceInformation.code
:

clientReferenceInformation.partner.developerId
:

clientReferenceInformation.partner.solutionId
:

orderInformation.billTo.address1
:

orderInformation.billTo.address2
:

orderInformation.billTo.administrativeArea
:

orderInformation.billTo.locality
:

orderInformation.billTo.postalCode
:

orderInformation.invoiceDetails.invoiceDate
:

orderInformation.lineItems.buyerVatRegistrationNumber
:

orderInformation.lineItems.orderAcceptance.administrativeArea
:

orderInformation.lineItems.orderAcceptance.country
:

orderInformation.lineItems.orderAcceptance.locality
:

orderInformation.lineItems.orderAcceptance.postalCode
:

orderInformation.lineItems.orderOrigin.administrativeArea
:

orderInformation.lineItems.orderOrigin.country
:

orderInformation.lineItems.orderOrigin.locality
:

orderInformation.lineItems.orderOrigin.postalCode
:

orderInformation.lineItems.productCode
:

orderInformation.lineItems.productName
:

orderInformation.lineItems.productSku
:

orderInformation.lineItems.quantity
:

orderInformation.lineItems.sellerVatRegistrationNumber
:

orderInformation.lineItems.shipFromAdministrativeArea
:

orderInformation.lineItems.shipFromCountry
:

orderInformation.lineItems.shipFromLocality
:

orderInformation.lineItems.shipFromPostalCode
:

orderInformation.lineItems.taxAmount
:

orderInformation.orderAcceptance.administrativeArea
:

orderInformation.orderAcceptance.country
:

orderInformation.orderAcceptance.locality
:

orderInformation.orderAcceptance.postalCode
:

orderInformation.orderOrigin.administrativeArea
:

orderInformation.orderOrigin.country
:

orderInformation.orderOrigin.locality
:

orderInformation.orderOrigin.postalCode
:

orderInformation.shippingDetails.shipFromAdministrativeArea
:

orderInformation.shippingDetails.shipFromCountry
:

orderInformation.shippingDetails.shipFromLocality
:

orderInformation.shippingDetails.shipFromPostalCode
:

orderInformation.shipTo.address1
:

orderInformation.shipTo.address2
:

orderInformation.shipTo.address3
:

orderInformation.shipTo.administrativeArea
:

orderInformation.shipTo.country
:

orderInformation.shipTo.locality
:

orderInformation.shipTo.postalCode
:

taxInformation.commitIndicator
:
Set field to `true` to commit tax calculation.

taxInformation.dateOverrideReason
:

taxInformation.nexus
:
If you include this field, do not include the taxInformation.noNexus field.

taxInformation.noNexus
:
If you include this field, do not include the taxInformation.nexus field.

taxInformation.refundIndicator
:

taxInformation.reportingDate
:

taxInformation.showTaxPerLineItem
:

Example: Processing an International Tax and VAT Committed Tax Calculation Using the REST API {#tax-com-call-int-ex-rest}
=========================================================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "TAX_TC001"
  },
  "taxInformation": {
    "showTaxPerLineItem": "Yes",
    "commitIndicator": true
  },
  "orderInformation": {
    "amountDetails": {
      "currency": "USD"
    },
    "billTo": {
      "locality": "San Francisco",
      "administrativeArea": "CA",
      "postalCode": 94105,
      "country": "US"
    },
    "lineItems": [
      {
        "unitPrice": 1200
      }
    ]
  }
}
```

Response

```
{
  "_links": {
    "void": {
      "method": "PATCH",
      "href": "/vas/v2/tax/6632667159226346003954"
    }
  },
  "clientReferenceInformation": {
    "code": "TAX_TC001"
  },
  "id": "6632667159226346003954",
  "orderInformation": {
    "lineItems": [
      {
        "taxableAmount": "1200.00",
        "taxDetails": [
          {
            "amount": "0.00",
            "type": "city"
          },
          {
            "amount": "28.50",
            "type": "special"
          },
          {
            "amount": "72.00",
            "type": "state"
          },
          {
            "amount": "3.00",
            "type": "county"
          },
          {
            "amount": "0.00",
            "type": "national"
          }
        ],
        "jurisdiction": [
          {
            "country": "US",
            "code": "06",
            "taxable": "1200.00",
            "rate": "0.060000",
            "name": "CALIFORNIA",
            "type": "State",
            "region": "CA",
            "taxAmount": "72.00",
            "taxName": "CA STATE TAX"
          },
          {
            "country": "US",
            "code": "075",
            "taxable": "1200.00",
            "rate": "0.002500",
            "name": "SAN FRANCISCO",
            "type": "County",
            "region": "CA",
            "taxAmount": "3.00",
            "taxName": "CA COUNTY TAX"
          },
          {
            "country": "US",
            "code": "EMBE0",
            "taxable": "1200.00",
            "rate": "0.013750",
            "name": "SAN FRANCISCO COUNTY DISTRICT TAX SP",
            "type": "Special",
            "region": "CA",
            "taxAmount": "16.50",
            "taxName": "CA SPECIAL TAX"
          },
          {
            "country": "US",
            "code": "EMTV0",
            "taxable": "1200.00",
            "rate": "0.010000",
            "name": "SAN FRANCISCO CO LOCAL TAX SL",
            "type": "Special",
            "region": "CA",
            "taxAmount": "12.00",
            "taxName": "CA SPECIAL TAX"
          }
        ],
        "exemptAmount": "0.00",
        "taxAmount": "103.50"
      }
    ],
    "taxableAmount": "1200.00",
    "taxDetails": [
      {
        "amount": "28.50",
        "type": "special"
      },
      {
        "amount": "72.00",
        "type": "state"
      },
      {
        "amount": "0.00",
        "type": "national"
      },
      {
        "amount": "3.00",
        "type": "county"
      },
      {
        "amount": "0.00",
        "type": "city"
      }
    ],
    "exemptAmount": "0.00",
    "taxAmount": "103.50",
    "amountDetails": {
      "totalAmount": "1303.50",
      "currency": "USD"
    }
  },
  "status": "COMPLETED",
  "submitTimeUtc": "2022-09-15T18:31:57Z",
  "taxInformation": {
    "commitIndicator": "true",
    "refundIndicator": "false"
  }
}
```

Refund Tax Calculation {#tax-calc-refund-intro}
===============================================

A refund tax calculation is a request that sets the transaction type field in the Tax Detail Report to refunded and makes the reported amount negative. Tax amounts are returned as positive amounts in response messages, but they are saved in reports as negative amounts. The tax software enables you to accurately calculate the aggregate amounts.  
You can also commit a refund tax calculation to include the refunded tax amount with a payment refund.

Tax Detail Report
-----------------

The refund request will set the Transaction Type field to Refund in the Tax Detail Report and will make the value of the Tax Amount negative.

Fields specific to this Use Case
--------------------------------

Include the following information with a standard refund tax calculation request when you want to include the refund request to your Tax Detail Report:

* To commit a tax calculation refund request, set the taxInformation.commitIndicator field to `true`.
* To apply the same rate from the day of the original transaction, set the invoiceDetails.invoiceDate field to the original transaction date.
  {#tax-calc-refund-intro_ul_sxk_l4t_lvb}

Endpoint {#tax-calc-refund-intro_tax-endpoint}
----------------------------------------------

`POST ``https://api.example.com``/vas/v2/tax`{#tax-calc-refund-intro_restinitiate-altpay}

Refund Tax Calculation Scenarios {#tax-scenario-refund-intro}
=============================================================

You can report a refund tax calculation at different moments in a transaction.  
Use these scenario examples to determine when you should report refund a tax calculation.  
Possible scenarios:

* [Scenario 1: Full or Partial Refund](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-calc-refund-intro/tax-scenario-refund-intro/tax-scenario-com-refund-one.md "")
* [Scenario 2: Stand-alone Credit](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-calc-refund-intro/tax-scenario-refund-intro/tax-scenario-com-refund-two.md "")
  {#tax-scenario-refund-intro_ul_xxh_ph3_vwb}

Scenario 1: Full or Partial Refund {#tax-scenario-com-refund-one}
=================================================================

You can refund a tax calculation request before requesting an authorization if you have access to the original transaction data. For example:

1. Refund the full or partial amount of the original transaction.
2. If the refund is successful, request the tax calculation service for the refunded item(s) and include the refund indicator by using the `taxInformation.refundIndicator` field set to `true`.

> IMPORTANT
> To ensure the same tax rate as the original transaction, use the invoice date of the original transaction in the ` orderInformation.invoiceDetails.invoiceDate ` field.  
> You can include the commit indicator by setting the `taxInformation.commitIndicator` field to `true` to indicate when the refund was successfully processed in the Tax Detail Report.

Scenario 2: Stand-alone Credit {#tax-scenario-com-refund-two}
=============================================================

You can credit a transaction if you do not have access to the original transaction data. For example:

1. Request the tax service with the `taxInformation.refundIndicator` field set to `true`.{#tax-scenario-com-refund-two_step1}
   {#tax-scenario-com-refund-two_step1}
2. Credit the payment.{#tax-scenario-com-refund-two_step2}
   {#tax-scenario-com-refund-two_step2}

{#tax-scenario-com-refund-two_steps-refund} You can include the commit indicator by setting the taxInformation.commitIndicator field to `true` to indicate the credit was successfully processed in the Tax Detail Report. The commit indicator can also be sent during the first tax service request, such as [Scenario 1](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-com-call-intro/tax-scenario-com-intro/tax-scenario-com-one.md ""), or in subsequent tax service requests, such as [Scenario 2](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-com-call-intro/tax-scenario-com-intro/tax-scenario-com-two.md ""). If the credit fails, void the previously committed tax service request. See [Void Tax Calculation](/docs/gateway/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-reporting-intro/tax-void-intro.md "").

Required Fields for a Tax Refund Calculation Using the REST API {#tax-calc-refund-required-fields}
==================================================================================================

Use these fields to perform a tax refund calculation.

clientReferenceInformation.code
:

invoiceDetails.invoiceDate
:
Set this field to original transaction date.

orderInformation.lineItems\[\].unitPrice
:

orderInformation.billTo.country
:

orderInformation.billTo.postalCode
:

orderInformation.billTo.locality
:

orderInformation.billTo.administrativeArea
:

taxInformation.refundIndicator
:
Set the value of this field to `true`.

taxInformation.showTaxPerLineItem
:

taxInformation.nexus
:
If you include this field, do not include the taxInformation.noNexus field.

taxInformation.noNexus
:
If you include this field, do not include the taxInformation.nexus field.

Example: Processing a Tax Refund Calculation Using the REST API {#tax-calc-refund-ex-rest}
==========================================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "TAX_TC001"
  },
  "taxInformation": {
    "nexus": ["CA","TX","AL"],
    "showTaxPerLineItem": "Yes",
    "commitIndicator": "true",
    "refundIndicator": "true"
  },
  "orderInformation": {
    "amountDetails": {
      "currency": "USD"
    },
    "billTo": {
      "address1": "1 Market St",
      "locality": "San Francisco",
      "administrativeArea": "CA",
      "postalCode": 94105,
      "country": "US"
    },
    "lineItems": [
      {
        "productSKU": "07-12-00657",
        "productCode": "PO000000",
        "quantity": 1,
        "productName": "Chewing Gum",
        "unitPrice": 1200
      }
    ],
    "invoiceDetails": {
      "invoiceDate": "20221010"
    }
  }
}
```

Response

```
{
  "_links": {
    "void": {
      "method": "PATCH",
      "href": "/vas/v2/tax/6679353637266069103955"
    }
  },
  "clientReferenceInformation": {
    "code": "TAX_TC001"
  },
  "id": "6679353637266069103955",
  "orderInformation": {
    "lineItems": [
      {
        "taxableAmount": "1200.00",
        "taxDetails": [
          {
            "amount": "0.00",
            "type": "city"
          },
          {
            "amount": "28.50",
            "type": "special"
          },
          {
            "amount": "72.00",
            "type": "state"
          },
          {
            "amount": "3.00",
            "type": "county"
          },
          {
            "amount": "0.00",
            "type": "national"
          }
        ],
        "jurisdiction": [
          {
            "country": "US",
            "code": "06",
            "taxable": "1200.00",
            "rate": "0.060000",
            "name": "CALIFORNIA",
            "type": "State",
            "region": "CA",
            "taxAmount": "72.00",
            "taxName": "CA STATE TAX"
          },
          {
            "country": "US",
            "code": "075",
            "taxable": "1200.00",
            "rate": "0.002500",
            "name": "SAN FRANCISCO",
            "type": "County",
            "region": "CA",
            "taxAmount": "3.00",
            "taxName": "CA COUNTY TAX"
          },
          {
            "country": "US",
            "code": "EMBE0",
            "taxable": "1200.00",
            "rate": "0.013750",
            "name": "SAN FRANCISCO COUNTY DISTRICT TAX SP",
            "type": "Special",
            "region": "CA",
            "taxAmount": "16.50",
            "taxName": "CA SPECIAL TAX"
          },
          {
            "country": "US",
            "code": "EMTV0",
            "taxable": "1200.00",
            "rate": "0.010000",
            "name": "SAN FRANCISCO CO LOCAL TAX SL",
            "type": "Special",
            "region": "CA",
            "taxAmount": "12.00",
            "taxName": "CA SPECIAL TAX"
          }
        ],
        "exemptAmount": "0.00",
        "taxAmount": "103.50"
      }
    ],
    "taxableAmount": "1200.00",
    "taxDetails": [
      {
        "amount": "28.50",
        "type": "special"
      },
      {
        "amount": "72.00",
        "type": "state"
      },
      {
        "amount": "0.00",
        "type": "national"
      },
      {
        "amount": "3.00",
        "type": "county"
      },
      {
        "amount": "0.00",
        "type": "city"
      }
    ],
    "exemptAmount": "0.00",
    "taxAmount": "103.50",
    "amountDetails": {
      "totalAmount": "1303.50",
      "currency": "USD"
    }
  },
  "status": "COMPLETED",
  "submitTimeUtc": "2022-11-08T19:22:44Z",
  "taxInformation": {
    "commitIndicator": "true",
    "refundIndicator": "true"
  }
}
```

Void Tax Calculation {#tax-void-intro}
======================================

Use the void tax calculation request to indicate when a previously committed tax transaction either:

* Was not successfully captured or refunded
* Was successfully voided

{#tax-void-intro_ul_jzv_fj5_lvb}  
This feature can only be used to void the full original tax service request. It cannot be used to void a single line item.  
Contact customer support to have your account enabled to test this feature in the `Payment Gateway` Developer Center.

Tax Detail Report
-----------------

When you void a tax calculation request, a line item is added to the Tax Detail Report with a `Cancelled` value in the Status field. The cancelled line item will have a request ID of the original committed transaction in the LinkToRequestID field. Use the value of the LinkToRequestID to identify the original tax amounts that were not successfully debited or credited from a cardholder bank account.

Endpoint {#tax-void-intro_tax-endpoint}
---------------------------------------

`POST ``https://api.example.com``/vas/v2/tax/{id}`{#tax-void-intro_restinitiate-altpay}

Required Fields for a Tax Void Using the REST API {#tax-void-required-fields}
=============================================================================

Use this field to perform a tax void.

clientReferenceInformation.code
:

Example: Processing a Tax Void Using the REST API {#tax-void-ex-rest}
=====================================================================

Request

```
{
  "clientReferenceInformation": {
    "code": "TAX_TC001"
  }
}
```

Response

```
{
  "clientReferenceInformation": {
    "code": "TAX_TC001"
  },
  "id": "6679355473836204603955",
  "status": "VOIDED",
  "submitTimeUtc": "2022-11-08T19:25:47Z",
  "voidAmountDetails": {
    "currency": "USD",
    "voidAmount": "-103.5"
  }
}
```

Supported Countries and Regions {#tax-info-supported-country-regions}
=====================================================================

|---------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| Afghanistan                                                                                                   | Lebanon                                      |
| Albania                                                                                                       | Lesotho                                      |
| Algeria                                                                                                       | Liberia                                      |
| Andorra                                                                                                       | Libyan Arab Jamahiriya                       |
| Angola                                                                                                        | Liechtenstein                                |
| Anguilla                                                                                                      | Lithuania                                    |
| Antigua and Barbuda                                                                                           | Livigno                                      |
| Argentina                                                                                                     | Luxembourg                                   |
| Armenia                                                                                                       | Macau                                        |
| Aruba                                                                                                         | Macedonia, the Former Yogoslav Republic of   |
| Australia                                                                                                     | Madagascar                                   |
| Austria                                                                                                       | Malawi                                       |
| Azerbaijan                                                                                                    | Malaysia                                     |
| Bahamas                                                                                                       | Maldives                                     |
| Bahrain                                                                                                       | Mali                                         |
| Bangladesh                                                                                                    | Malta                                        |
| Barbados                                                                                                      | Marshall Islands                             |
| Belarus                                                                                                       | Mauritania                                   |
| Belgium                                                                                                       | Mauritius                                    |
| Belize                                                                                                        | Mayotte                                      |
| Benin                                                                                                         | Mexico                                       |
| Bermuda                                                                                                       | Micronesia                                   |
| Bhutan                                                                                                        | Moldova                                      |
| Bolivia                                                                                                       | Monaco                                       |
| Bosnia and Herzegovina                                                                                        | Mongolia                                     |
| Botswana                                                                                                      | Montenegro                                   |
| British Indian Ocean Territory                                                                                | Montserrat                                   |
| Brunei Darussalam                                                                                             | Morocco                                      |
| Bulgaria                                                                                                      | Mozambique                                   |
| Burkina Faso                                                                                                  | Myanmar                                      |
| Burundi                                                                                                       | Namibia                                      |
| Cambodia                                                                                                      | Nauru                                        |
| Cameroon                                                                                                      | Nepal                                        |
| Campione D'Italia                                                                                             | Netherlands                                  |
| Canada                                                                                                        | New Caledonia                                |
| Canary Islands                                                                                                | New Zealand                                  |
| Cape Verde                                                                                                    | Nicaragua                                    |
| Caribbean Netherlands (Bonaire)                                                                               | Niger                                        |
| Caribbean Netherlands (Sint Eustatius and Saba)                                                               | Nigeria                                      |
| Cayman Islands                                                                                                | Niue                                         |
| Central African Republic                                                                                      | Norway                                       |
| Chad                                                                                                          | Oman                                         |
| Chile                                                                                                         | Pakistan                                     |
| China > IMPORTANT Regional tax is not supported in China. Tax determination defaults to the federal tax rate. | Palau                                        |
| Christmas Island                                                                                              | Palestine Occupied Territory                 |
| Cocos (Keeling) Islands                                                                                       | Panama                                       |
| Colombia                                                                                                      | Papua New Guinea                             |
| Comoros                                                                                                       | Paraguay                                     |
| Congo, Republic of the                                                                                        | Peru                                         |
| Congo, The Democratic Republic of the                                                                         | Philippines                                  |
| Coral Sea Islands                                                                                             | Pitcairn Islands                             |
| Costa Rica                                                                                                    | Poland                                       |
| Cote D'Ivoire                                                                                                 | Portugal                                     |
| Croatia                                                                                                       | Puerto Rico                                  |
| Curacao                                                                                                       | Qatar                                        |
| Cyprus                                                                                                        | Republic of Korea (South Korea)              |
| Czech Republic                                                                                                | Romania                                      |
| Denmark                                                                                                       | Russian Federation                           |
| Djibouti                                                                                                      | Rwanda                                       |
| Dominica                                                                                                      | Saint Helena                                 |
| Dominican Republic                                                                                            | Saint Kitts and Nevis                        |
| Ecuador                                                                                                       | Saint Lucia                                  |
| El Salvador                                                                                                   | Saint Martin                                 |
| Equatorial Guinea                                                                                             | Saint Pierre and Miquelon                    |
| Eritrea                                                                                                       | Saint Vincent and the Grenadines             |
| Estonia                                                                                                       | Samoa                                        |
| Ethiopia                                                                                                      | San Marino                                   |
| Falkland Islands (Malvinas)                                                                                   | Sao Tome and Principe                        |
| Faroe Islands                                                                                                 | Saudi Arabia                                 |
| Fiji                                                                                                          | Senegal                                      |
| Finland (includes Aland Island)                                                                               | Serbia                                       |
| France                                                                                                        | Seychelles                                   |
| French Guiana                                                                                                 | Sierra Leone                                 |
| French Polynesia                                                                                              | Singapore                                    |
| French Southern Territories                                                                                   | Sint Maarten                                 |
| Gabon                                                                                                         | Slovakia                                     |
| Gambia                                                                                                        | Slovenia                                     |
| Georgia                                                                                                       | Somalia                                      |
| Germany                                                                                                       | South Africa                                 |
| Ghana                                                                                                         | South Georgia and the South Sandwich Islands |
| Gibraltar                                                                                                     | Spain                                        |
| Greece                                                                                                        | Sri Lanka                                    |
| Greenland                                                                                                     | Suriname                                     |
| Grenada                                                                                                       | Svalbard and Jan Mayen                       |
| Guadeloupe                                                                                                    | Swaziland                                    |
| Guam                                                                                                          | Sweden                                       |
| Guatemala                                                                                                     | Switzerland                                  |
| Guernsey                                                                                                      | Taiwan                                       |
| Guinea                                                                                                        | Tajikistan                                   |
| Guinea-Bissau                                                                                                 | Tanzania                                     |
| Guyana                                                                                                        | Thailand                                     |
| Haiti                                                                                                         | Timor-Leste                                  |
| Heligoland                                                                                                    | Togo                                         |
| Holy See                                                                                                      | Tokelau                                      |
| Honduras                                                                                                      | Tonga                                        |
| Hong Kong                                                                                                     | Trinidad and Tobago                          |
| Hungary                                                                                                       | Tunisia                                      |
| Iceland                                                                                                       | Turkey                                       |
| Indonesia                                                                                                     | Turkmenistan                                 |
| Iraq                                                                                                          | Turks and Caicos Islands                     |
| Ireland                                                                                                       | Tuvalu                                       |
| Israel                                                                                                        | Uganda                                       |
| Italy                                                                                                         | Ukraine                                      |
| Jamaica                                                                                                       | United Arab Emirates                         |
| Japan                                                                                                         | United Kingdom                               |
| Jersey                                                                                                        | United States                                |
| Jordan                                                                                                        | Uruguay                                      |
| Kazakhstan                                                                                                    | Uzbekistan                                   |
| Kenya                                                                                                         | Vanuatu                                      |
| Kiribati                                                                                                      | Venezuela                                    |
| Kosovo                                                                                                        | Vietnam                                      |
| Kuwait                                                                                                        | Virgin Islands, British                      |
| Kyrgyzstan                                                                                                    | Wallis and Futuna                            |
| Lake Lugano, Territorial Waters of                                                                            | Yemen                                        |
| Lao People's Democratic Republic                                                                              | Zambia                                       |
| Latvia                                                                                                        | Zimbabwe                                     |
[Supported Countries and Regions]

City Abbreviations {#tax-info-city-abbrevs}
===========================================

Several applications expand some commonly used city-name abbreviations, which enables the tax calculation service to correctly evaluate city names for tax purposes. The US Postal Service also maintains a list of common abbreviations. When a customer uses abbreviations not accepted by either entity, the tax calculation service might not recognize the combination of city, state, and postal code, in which case the request fails and returns a reason code of `400`.  
The following table provides a list of the abbreviations used by the tax calculation service and the US Postal Service.

| Abbreviation |  Expansion  |           Abbreviation            |   Expansion   |
|--------------|-------------|-----------------------------------|---------------|
| bch          | beach       | n                                 | north         |
| crk          | creek       | ny                                | new york      |
| cty          | city        | pk                                | park          |
| cyn          | canyon      | pkwy                              | parkway       |
| e            | east        | pt                                | point         |
| ft           | fort        | s                                 | south         |
| grdn         | garden      | sf                                | san francisco |
| hbr          | harbor      | st (only for the US country code) | saint         |
| hgts, hts    | heights     | spr                               | spring        |
| jct, jctn    | junction    | sprs                              | springs       |
| la           | los angeles | vly                               | valley        |
| mt, mtn      | mountain    | w                                 | west          |
[Expanded City Abbreviations]

REST Reason Codes {#reference_csk_11f_nvb}
==========================================

| Reason Code |                                                                                                                                                          Description                                                                                                                                                           |     STATUS      |             REASON             |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|--------------------------------|
| 201         | Successful transaction.                                                                                                                                                                                                                                                                                                        | COMPLETED       | N/A                            |
| 400         | The request is missing one or more required fields. See the information about missing and invalid fields in Getting Started with `Payment Gateway` Advanced for the Simple Order API. Possible action: See the reply fields missingField_0...N for which fields are missing. Resend the request with the complete information.     | INVALID_REQUEST | MISSING_FIELD                  |
| 400         | One or more fields in the request contains invalid data. See the information about missing and invalid fields in Getting Started with `Payment Gateway` Advanced for the Simple Order API. Possible action: See the reply fields invalidField_0...N for which fields are invalid. Resend the request with the correct information. | INVALID_REQUEST | INVALID_DATA                   |
| 400         | There is a problem with your `Payment Gateway` merchant configuration. Possible action: Do not resend the request. Contact Customer Support to correct the configuration problem.                                                                                                                                                  | INVALID_REQUEST | INVALID_MERCHANT_CONFIGURATION |
| 400         | Address verification failed. Typically occurs if one part of the address is not consistent with another part. For example, occurs if the postal code is not consistent with the rest of the address. Possible action: Verify all parts of the address are correct and resend request.                                          | INVALID_REQUEST | AVS_FAILED                     |
| 502         | Error: The request was received but there was a server timeout. This error does not include timeouts between the client and the server. See the documentation for your `Payment Gateway` client for information about how to handle retries in the case of system errors.                                                          | SERVER_ERROR    | SERVER_TIMEOUT                 |
| 502         | Error: The request was received but there was a service timeout. See the documentation for your `Payment Gateway` client for information about how to handle retries in the case of system errors.                                                                                                                                 | SERVER_ERROR    | SERVICE_TIMEOUT                |
| 502         | Error: General system failure. See the documentation for your `Payment Gateway` client for information about how to handle retries in the case of system errors.                                                                                                                                                                   | SERVER_ERROR    | SYSTEM_ERROR                   |
[Tax Calculation Reason Codes]

