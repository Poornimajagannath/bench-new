Mass Transit Payment Services Using TMS Tokens {#um-processing-tms}
===================================================================

Use TMS tokens to request these mass transit payment services:

* Authorization for account verification and debt recovery

* Sale for aggregated fares and debt recovery

* Stand-alone credit  
  In card-present EMV contactless requests, include the transient token ID in the tokenInformation.jti field in place of track 2 data.  
  When submitting a tap token creation request, you can include EMV tag-length-value (TLV) tags in the paymentInformation.fluidData.value field or as part of the payment transaction request within the pointOfSaleInformation.emv.tags field.  
  If you send EMV tags in the tap token create request, do not send EMV tags in the payment transaction request.  
  When EMV TLV tags are present in both the payment transaction and the token vault, `Payment Gateway` reads the value provided in the payment transaction rather than the values stored in the vault.  
  Mastercard EMV transactions include these three field values, which can be handled automatically:

* paymentInformation.card.initiationChannel

* pointOfSaleInformation.emv.cardSequenceNumber

* pointOfSaleInformation.serviceCode  
  Your account can be configured to read these values automatically from the EMV TLV tags and track 2 equivalent. When that option is enabled, do not include those three fields in EMV payment requests.  
  If any of these values are present in both the separate fields and the EMV TLV and track 2 equivalent, `Payment Gateway` reads the value provided in the separate fields rather than the values present in the EMV TLV and track 2 equivalent.

#### Figure:

Payment Processing with a Token Workflow  
![Diagram showing Payment Processing with a Token workflow](/content/dam/documentation/pgw/en-us/topics/payments-processing/card-processing/mass-transit/images/mtt-backoffice-390x290.svg/jcr:content/renditions/original)
