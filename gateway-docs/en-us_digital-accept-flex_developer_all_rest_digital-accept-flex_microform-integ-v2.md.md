`Microform Integration` v2 {#microform-integ-v2}
================================================

`Microform Integration` replaces the sensitive payment input fields of a client application with secure `Payment Gateway`-hosted fields. These fields securely accept payment information, including card and check data, and replaces it with a non-sensitive tokens.  
You can style these fields to look and behave like any other field on your website, which could qualify you for PCI DSS assessments based on [SAQ A](https://www.pcisecuritystandards.org/documents/Understanding_SAQs_PCI_DSS_v3.pdf "").  
`Microform Integration` provides the most secure method for tokenizing card and check data. Sensitive data is encrypted on the customer's device before HTTPS transmission to `Payment Gateway`. This method reduces the potential for man-in-the middle attacks on the HTTPS connection.

> IMPORTANT
> Each request that you send to ` Payment Gateway ` requires header information. For information about constructing the headers for your request, see the [*Getting Started with REST Developer Guide*](https://developer.example.com/docs/gateway/en-us/platform/developer/all/rest/rest-getting-started/restgs-about-guide.md "").

