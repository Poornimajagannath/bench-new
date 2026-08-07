Required Fields for Adding and Deleting a Processor Using the PECS API {#pecs-add-delete-processor-req-fields}
==============================================================================================================

Use these required fields to delete a processor.

organizationId
:

payments.cardProcessing.configurationInformation.configurations. common.processors.\[processorName\].batchGroup
:
Where `[processorName]` is the payment processor.

payments.cardProcessing.configurationInformation.configurations. common.processors.\[processorName\].paymentTypes.\[paymentType\].enabled
:
Where \[processor\] is the payment processor and \[paymentTypes\] is the payment type.

    Set to `false`. IMPORTANT You must include this field for all card types configured for the processor.

payments.cardProcessing.subscriptionInformation.enabled
:

payments.cardProcessing.subscriptionInformation.features.cardNotPresent.enabled
:

payments.cardProcessing.subscriptionInformation.features.cardPresent.enabled
:

organizationId
:

payments.cardProcessing.configurationInformation.configurations.common.merchantCategoryCode
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.city
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.country
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.name
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.phone
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.zip
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.state
:

payments.cardProcessing.configurationInformation.configurations.common.merchantDescriptorInformation.street
:

payments.cardProcessing.configurationInformation.configurations.common. processors.\[processorName\].currencies.\[currency\].serviceEnablementNumber
:
Where \[processorName\] is the payment processor and \[currency\] is the currency.

payments.cardProcessing.configurationInformation.features.cardNotPresent. processors.\[processorName\]relaxAddressVerificationSystem
:
Where \[processorName\] is the payment processor.

payments.cardProcessing.configurationInformation.features.cardNotPresent. processors.\[processorName\]relaxAddressVerificationSystemAllowExpiredCard
:
Where \[processorName\] is the payment processor.

payments.cardProcessing.configurationInformation.features.cardNotPresent. processors.\[processorName\]relaxAddressVerificationSystemAllowZipWithoutCountry
:
Where \[processorName\] is the payment processor.

payments.cardProcessing.configurationInformation.templateId
:

payments.cardProcessing.subscriptionInformation.enabled
:
