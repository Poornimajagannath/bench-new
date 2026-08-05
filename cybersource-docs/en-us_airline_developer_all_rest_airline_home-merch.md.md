Introduction to Airline Processing {#home-merch}
================================================

Airline data processing exceeds basic payment processing by enabling you to process specific travel data. To make use of this capability, you must submit additional information, such as:

* Carrier (airline)
* Departure date
* Destination airport
* Purchase date
* Originating airport
* Ticket class
* Travel legs (segments)
* Ticket Number

{#home-merch_ul_x5d_bnt_nwb}  
Before you can begin testing and processing airline payments, you must have airline transactions enabled for your merchant account. Contact your `Cybersource` account manager for more information.

> IMPORTANT
> ` Cybersource ` temporarily disables your account's airline data processing capability and contacts you if your airline data transactions produce batching errors when the information is sent to the processor. If this occurs, your request is not rejected, but you receive one of the above listed fields with the ` N ` value in the response indicating that airline data in the request has been ignored and not sent to the processor.

Prerequisite
------------

To begin processing payments through `Cybersource`, you must first set up your payment processing system to be REST compliant. If you have not set up secure communications between your client and server using either **JSON Web Token (JWT)** or **HTTP signature** messaging, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "").
