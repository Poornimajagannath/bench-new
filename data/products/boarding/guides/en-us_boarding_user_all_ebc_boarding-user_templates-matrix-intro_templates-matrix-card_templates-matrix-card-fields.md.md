Processor-Specific Fields {#templates-matrix-card-fields}
=========================================================

These processor-specific fields are frequently configured in a card-processing template. For more information about these and other fields in the template, see the [*API Field Reference Guide*](https://docs.cybersource.com/en/reference/api-fields.md "").

Accepted Currencies
:
Select all of the currencies that the merchant accepts. The currencies listed in this field depend on the payment processor selected.

    As an example, if you are creating a card-processing template for the TSYS/Vital processor, the list of accepted currencies is as follows:

    * CAD (Canadian Dollar)
    * USD (US Dollar)


    For more information about currency codes, see [*ISO Standard Currency Codes*](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf "").

Accepted Payment Types
:
Select all of the card types that the merchant accepts. The card types listed in this field depend on the payment processor selected.

    Depending on your payment processor, these are some of the card types you can expect to see listed:

    * Visa
    * Mastercard
    * American Express
    * Diners Club


    For more information about the specific card types that your processor supports, log in to the `Business Center` and go to **Template Management for Card Processing**.

Batch Group
:
The Batch Group groups all of the capture (bill and credit) requests into a batch bound for your payment processor.

    Choose the batch group for processing capture requests.

    The name of a batch group identifies the time of day that capture requests are grouped into a batch and sent to your payment processor. The last two digits of the batch group name identify the hour (in 24-hour time) of the processor cutoff time for that batch group.

    As an example, if you are creating a card processing template for the American Express Direct processor, the list of batch group names you can select includes the following:

    * amexdirect_2 (processor cutoff time is 2:00 a.m. PST daily)
    * amexdirect_17 (processor cutoff time is 5:00 p.m. PST daily)
    * amexdirect_21 (processor cutoff time is 9:00 p.m. PST daily)


    > IMPORTANT Processor cutoff times identified in the batch group names are in Pacific Standard Time (PST).

Merchant ID
:
Enter the merchant's acquirer processing ID assigned by the acquiring bank.
:
Note that it is unlikely that you would specify this field in a card-processing template. Typically, the merchant ID is merchant specific. Also, many merchants have more than one merchant ID to support processing in multiple currencies or to process both card present (in store) transactions and card-not-present (e-commerce) transactions.

Terminal ID
:
Enter the terminal ID assigned by the acquirer or the processor. This value should not be overridden by any other party.
:
Enter the merchant's processing terminal ID assigned by the acquiring bank or payment processor.
:
Note that it is unlikely that you would specify this field in a card-processing template. Typically, the terminal ID is merchant specific. Also, many merchants have more than one terminal ID to support processing in multiple currencies or to process both card-present (in store) transactions and card-not-present (e-commerce) transactions.
