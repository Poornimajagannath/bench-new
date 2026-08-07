Required Fields for Deleting a Processor Using the PECS API {#pecs-delete-processor-req-fields}
===============================================================================================

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
