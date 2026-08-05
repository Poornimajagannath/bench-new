# Source: https://developer.cybersource.com/hello-world/testing-guide.md

![](/content/experience-fragments/developer-center/cybs-dev-center/testing-guide/master/jcr:content/root/contentwell/contentWell/contentwell/contentWell/banner/image.img.jpg/1682057789317.jpg)  
<br />

Testing Guides  
<br />

<br />

<br />

<br />

<br />

Testing guides  
We have over 20 processors that you can pick from.  
Select Processor  
Select Processor American Express Direct Barclays Chase Paymentech Solutions Comercio Latino Boleto FDC Compass FDC Nashville Global FDMS Nashville Litle Moneris Network International UAE OMNIPAYDIRECT SIX Streamline Visa Platform Connect
This field is required  
[Go](/hello-world/testing-guide/processor-testing-guide.md)  
Test in sandbox  
The sandbox simulates the live payment gateway. The sandbox never processes an actual payment. We do not submit sandbox transactions to financial institutions for processing. The sandbox environment is completely separate from the live production environment, and it requires separate credentials. If you use your production credentials in the sandbox or visa versa, you get a 401 HTTP error.  
[Create sandbox account](/hello-world/sandbox.md)  
Test card numbers  
The following test credit card numbers work only in the sandbox. If no expiration date is provided, use any expiration date after today's date. If the card verification code is required and is not provided, use any 3-digit combination for Visa, Mastercard, Discover, Diners Club and JCB; use a 4-digit combination for American Express.

|       Test card brand       |         Number          | CVV |
|-----------------------------|-------------------------|-----|
|                             |
| **Visa**                    | 4111 1111 1111 1111     |     |
| **Visa**                    | 4622 9431 2701 3705     | 838 |
| **Visa**                    | 4622 9431 2701 3713     | 043 |
| **Visa**                    | 4622 9431 2701 3721     | 258 |
| **Visa**                    | 4622 9431 2701 3739     | 942 |
| **Visa**                    | 4622 9431 2701 3747     | 370 |
| **Mastercard**              | 2222 4200 0000 1113     |     |
| **Mastercard**              | 2222 6300 0000 1125     |     |
| **Mastercard**              | 5555 5555 5555 4444     |     |
| **American Express**        | 3782 8224 6310 005      |     |
| **Discover**                | 6011 1111 1111 1117     |     |
| **JCB**                     | 3566 1111 1111 1113     |     |
| **Maestro (International)** | 5033 9619 8909 17       |     |
| **Maestro (International)** | 5868 2416 0825 5333 38  |     |
| **Maestro (UK Domestic)**   | 6759 4111 0000 0008     |     |
| **Maestro (UK Domestic)**   | 6759 5600 4500 5727 054 |     |
| **Maestro (UK Domestic)**   | 5641 8211 1116 6669     |     |
| **UATP**                    | 1354 1234 5678 911      |     |

Common payment transaction responses  
Review the tables below to find the payment transaction responses that you want to trigger. For example, to trigger an invalid amount response, pass the value -1 in the orderInformation.amountDetails.totalAmount request field. The triggered test responses below mostly depend on the value that you pass in the request field: orderInformation.amountDetails.totalAmount Also, please note the following when testing Payments transactions: For credit cards, the transaction decisions typically are: AUTHORIZED - Transaction accepted. Passed with a 201 HTTP response Code. DECLINE - Transaction declined. ERROR - Transaction failed. The response includes a ReasonCode. To obtain more information about an error, view the transaction's details in the Merchant Portal. The value of the requestID field will vary. The number increments with each Cybersource transaction (for all merchants).

|        Test information         |                          Input                           |                 Expected response                  |
|---------------------------------|----------------------------------------------------------|----------------------------------------------------|
| Valid transaction               | orderInformation.amountDetails.totalAmount=1             | **STATUS** AUTHORIZED                              |
| Invalid amount \< $0            | orderInformation.amountDetails.totalAmount=-1            | **STATUS** INVALID_REQUEST **REASON** INVALID_DATA |
| Invalid amount Amount too large | orderInformation.amountDetails.totalAmount= 100000000000 | **STATUS** INVALID_REQUEST **REASON**INVALID_DATA  |
| Empty credit card number        | paymentInformation.card.number = 42423482938483873       | **STATUS** DECLINE **REASON**INVALID_DATA          |
| Invalid expiration month        | paymentInformation.card.expirationMonth = 13             | **STATUS** INVALID_REQUEST **REASON**INVALID_DATA  |
| Invalid expiration year         | paymentInformation.card.expirationYear = 1998            | **STATUS** DECLINE **REASON**INVALID_DATA          |
| Invalid Luhn Mod 10             | paymentInformation.card.number = 4111111111111112        | **STATUS** DECLINE **REASON**INVALID_DATA          |
| 21-digit credit card number     | paymentInformatioon.card.number = 412345678912345678914  | **STATUS** DECLINE **REASON** INVALID_DATA         |

