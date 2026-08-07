Required Fields for Enabling `Payer Authentication` {#boarding-payer-auth-enable-reqfields}
===========================================================================================

[organizationInformation.businessInformation.address.address1](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-address1.md "")
:

[organizationInformation.businessInformation.address.administrativeArea](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-admin-area.md "")
:

[organizationInformation.businessInformation.address.country](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-country.md "")
:

[organizationInformation.businessInformation.address.locality](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-locality.md "")
:

[organizationInformation.businessInformation.address.postalCode](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-address-postal-code.md "")
:

[organizationInformation.businessInformation.businessContact.email](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-contact-email.md "")
:

[organizationInformation.businessInformation.businessContact.firstName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-first-name.md "")
:

[organizationInformation.businessInformation.businessContact.lastName](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-last-name.md "")
:

[organizationInformation.businessInformation.businessContact.phoneNumber](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-business-contact-phone-num.md "")
:

[organizationInformation.businessInformation.businessContact.websiteUrl](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-website-url.md "")
:
Must be in the format `http://www.example.com`.

[organizationInformation.businessInformation.name](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-business-info-name.md "")
:

[organizationInformation.configurable](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-configurable.md "")
:
Set to `false`.

[organizationInformation.parentOrganizationId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-parent-organization-id.md "")
:

[organizationInformation.type](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/org-info-aa/org-info-type.md "")
:
Set to `TRANSACTING`.

[registrationInformation.boardingFlow](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/reg-info-aa/reg-info-boarding-flow.md "")
:
Set to `ADDPRODUCT`.

American Express SafeKey-Specific Fields
----------------------------------------

Include these fields in addition to the required fields to enable and configure American Express SafeKey:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.amexSafeKey.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-0.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
{#boarding-payer-auth-enable-reqfields_boarding-acq-id}
{#boarding-payer-auth-enable-reqfields_boarding-acq-id}
:
For testing purposes, use Acquirer ID: `cybersource`.
{#boarding-payer-auth-enable-reqfields_boarding-acq-id-test}
{#boarding-payer-auth-enable-reqfields_boarding-acq-id-test}

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.amexSafeKey.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-1.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.amexSafeKey.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-2.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.amexSafeKey.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-4.md "")
:
Set to `true`.

Cartes Bancaires-Specific Fields
--------------------------------

Include these fields in addition to the required fields to enable and configure Cartes Bancaires:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.CB.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-5.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.CB.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-6.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.CB.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-7.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.CB.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-10.md "")
:
Set to `true`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.CB.requestorId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-conf-8.md "")
:

Discover/Diners Club ProtectBuy-Specific Fields
-----------------------------------------------

Include these fields in addition to the required fields to enable and configure Discover/Diners Club ProtectBuy:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.dinersClubInternationalProtectBuy.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-12.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.dinersClubInternationalProtectBuy.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-13.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.dinersClubInternationalProtectBuy.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-14.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.dinersClubInternationalProtectBuy.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-17.md "")
:
Set to `true`.

ELO-Specific Fields
-------------------

Include these fields in addition to the required fields to enable and configure ELO:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.ELO.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-18.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.ELO.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-19.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.ELO.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-20.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.ELO.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-23.md "")
:
Set to `true`.

JCB J/Secure-Specific Fields
----------------------------

Include these fields in addition to the required fields to enable and configure JCB J/Secure:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.jCBJSecure.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-25.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.jCBJSecure.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-26.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.jCBJSecure.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-27.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.jCBJSecure.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-29.md "")
:
Set to `true`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.jCBJSecure.securePasswordForJCB](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-30.md "")
:

Mastercard/Meeza Identity Check-Specific Fields
-----------------------------------------------

Include these fields in addition to the required fields to enable and configure Mastercard/Meeza Identity Check:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.masterCardSecureCode.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-33.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.masterCardSecureCode.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-34.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.masterCardSecureCode.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-35.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.masterCardSecureCode.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-36.md "")
:
Set to `true`.

UnionPay 3-D Secure-Specific Fields
-----------------------------------

Include these fields in addition to the required fields to enable and configure UnionPay 3-D Secure:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.UPI.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-37.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.UPI.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-38.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.UPI.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-39.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.UPI.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-42.md "")
:
Set to `true`.

Visa Secure-Specific Fields
---------------------------

Include these fields in addition to the required fields to enable and configure Visa Secure:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.verifiedByVisa.currencies\[\].acquirerId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-44.md "")
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.verifiedByVisa.currencies\[\].currencyCodes\[\]](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-45.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.verifiedByVisa.currencies\[\].processorMerchantId](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-46.md "")
:

[productInformation.selectedProducts.payments.payerAuthentication.configurationInformation. configurations.cardTypes.verifiedByVisa.enabled](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/prod-info-aa/prod-info-sel-prod-pay-payerauth-conf-info-con-48.md "")
:
Set to `true`.

Related Information
-------------------

* [API Field Reference for the REST API](https://developer.cybersource.com/docs/cybs/en-us/api-fields/reference/all/rest/api-fields/api-fields-about-guide.md "")
  {#boarding-payer-auth-enable-reqfields_ul_kpc_xzz_sxb}

