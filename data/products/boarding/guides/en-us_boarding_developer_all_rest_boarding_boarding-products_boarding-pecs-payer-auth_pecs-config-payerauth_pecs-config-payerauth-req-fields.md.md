Required Fields for Configuring `Payer Authentication` Using the PECS API {#pecs-config-payerauth-req-fields}
=============================================================================================================

Use these required fields to configure `Payer Authentication` for these card types.

American Express SafeKey-Specific Fields
----------------------------------------

Include these fields in addition to the required fields to enable and configure American Express SafeKey:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. amexSafeKey.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. amexSafeKey.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. amexSafeKey.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. amexSafeKey.enabled
:
Set to `true`.

Cartes Bancaires-Specific Fields
--------------------------------

Include these fields in addition to the required fields to enable and configure Cartes Bancaires:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. CB.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. CB.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. CB.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes.CB.enabled
:
Set to `true`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes.CB.requestorId
:

Discover/Diners Club ProtectBuy-Specific Fields
-----------------------------------------------

Include these fields in addition to the required fields to enable and configure Discover/Diners Club ProtectBuy:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. dinersClubInternationalProtectBuy.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. dinersClubInternationalProtectBuy.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. dinersClubInternationalProtectBuy.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. dinersClubInternationalProtectBuy.enabled
:
Set to `true`.

ELO-Specific Fields
-------------------

Include these fields in addition to the required fields to enable and configure ELO:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. ELO.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. ELO.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. ELO.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes.ELO.enabled
:
Set to `true`.

JCB J/Secure-Specific Fields
----------------------------

Include these fields in addition to the required fields to enable and configure JCB J/Secure:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. jCBJSecure.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. jCBJSecure.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. jCBJSecure.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. jCBJSecure.enabled
:
Set to `true`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. jCBJSecure.securePasswordForJCB
:

Mastercard/Meeza Identity Check-Specific Fields
-----------------------------------------------

Include these fields in addition to the required fields to enable and configure Mastercard/Meeza Identity Check:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. masterCardSecureCode.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. masterCardSecureCode.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. masterCardSecureCode.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. masterCardSecureCode.enabled
:
Set to `true`.

UnionPay 3-D Secure-Specific Fields
-----------------------------------

Include these fields in addition to the required fields to enable and configure UnionPay 3-D Secure:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. UPI.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. UPI.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. UPI.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. UPI.enabled
:
Set to `true`.

Visa Secure-Specific Fields
---------------------------

Include these fields in addition to the required fields to enable and configure Visa Secure:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. verifiedByVisa.currencies\[\].acquirerId
:
The acquirer ID is the BIN of the merchant's acquiring bank and must be from 4 to 20 alphanumeric characters or a hyphen, and include `-1000`. For example, `123456-1000`.
:
For testing purposes, use Acquirer ID: `cybersource`.

payments.payerAuthentication.configurationInformation.configurations.cardTypes. verifiedByVisa.currencies\[\].currencyCodes\[\]
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. verifiedByVisa.currencies\[\].processorMerchantId
:

payments.payerAuthentication.configurationInformation.configurations.cardTypes. verifiedByVisa.enabled
:
Set to `true`.
