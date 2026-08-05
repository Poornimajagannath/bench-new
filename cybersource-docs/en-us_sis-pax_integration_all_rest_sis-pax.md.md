Acceptance Devices \| PAX Acceptance Devices App Integration Guide {#semi-integrated-solution-pax-about-guide}
==============================================================================================================

Use this information to use this guide and where to find further information.

Audience and Purpose
--------------------

This guide is written for partner developers, system architects, and independent software vendors (ISVs) who wish to integrate their point-of-sale system with PAX terminals in a semi-integrated manner.  
Implementing the PAX Acceptance Devices App requires software development skills. You must write code that uses the API request and response fields to integrate the solution into your point-of-sale system.

Conventions
-----------

These statements appear in this document:

> IMPORTANT
> An *Important* statement contains information essential to successfully completing a task or learning a concept.
> WARNING
> A *Warning* contains information or instructions, which, if not heeded, can result in a security risk, irreversible loss of data, or significant cost in time or revenue or both.

Support
-------

For support information about any service, visit the Support Center:  
<http://support.visaacceptance.com>

Recent Revisions to This Document {#sis-pax-doc-revisions}
==========================================================

26.06.01
--------

:
Added support for Kiosk Mode in [Customizable Common Parameters](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/sis-ad-app-customize-intro/sis-ad-app-customize-common.md "").
:
Updated Acceptance Devices app to version 1.23.0. See [Acceptance Devices App Version 1.23.0 Release Notes](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-release-notes-intro/sis-rel-notes-intro-ad-app-v123.md "").

26.05.01
--------

:
Updated Acceptance Devices app to version 1.22.0. See [Acceptance Devices App Version 1.22.0 Release Notes](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-release-notes-intro/sis-rel-notes-intro-ad-app-v122.md "").

26.04.01
--------

:
Added support for these items in [Supported Payment Terminals and Capabilities](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-intro/sis-pax-supported-terminals.md ""):

    * PAX terminals A50, A99, A6630, and A6650
    * Meeza card type with Visa Platform Connect payment processor
    {#sis-pax-doc-revisions_ul_m11_lyb_fjc}

:
Added new feature: [Enable Kiosk Mode](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/sis-ad-app-enable-kiosk-mode.md "").
:
Added support for new Local Mode features:

    * [Sale with Lodging Details](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-pymnt-svcs-semi-sale-lodging-intro.md "")
    * [Custom Printing](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-pymnt-svcs-semi-custom-print-intro.md "")
    * [Custom Screens](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-pymnt-svcs-semi-custom-screens-intro.md "")
    {#sis-pax-doc-revisions_ul_ows_psz_2jc}

:
Added support for new Cloud Mode features:

    * [Sale with Lodging Details](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-sale-lodging-intro.md "")
    * [Custom Printing](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-custom-print-intro.md "")
    * [Custom Screens](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-custom-screens-intro.md "")
    {#sis-pax-doc-revisions_ul_gq5_zsz_2jc}

:
Updated Acceptance Devices app to version 1.21.0. See [Acceptance Devices App Version 1.21.0 Release Notes](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-release-notes-intro/sis-rel-notes-intro-ad-app-v121.md "").

26.03.01
--------

Updated Acceptance Devices app to version 1.20. See [Acceptance Devices App Version 1.20.0 Release Notes](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-release-notes-intro/sis-rel-notes-intro-ad-app-v120.md "").

26.02.01
--------

:
Added two offline transaction parameters: [Customizable Common Parameters](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/sis-ad-app-customize-intro/sis-ad-app-customize-common.md "").
:
Added support for new payment service: [Sale with Payment Facilitator Details](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-pymnt-svcs-semi-sale-pymnt-facil-details-intro.md "").

25.12.02
--------

:
Replaced Payment Terminals Supported by the PAX Acceptance Devices App section with [Supported Payment Terminals and Capabilities](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-intro/sis-pax-supported-terminals.md "").

25.12.01
--------

:
Added PAX A3700 to list of supported devices in [Supported Payment Terminals and Capabilities](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-intro/sis-pax-supported-terminals.md "").
:
Reorganized [Customizable Common Parameters](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/sis-ad-app-customize-intro/sis-ad-app-customize-common.md ""). Made no technical changes.
:
Added Enable payment facilitator details parameter to [Customizable Standalone Mode Parameters](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/sis-ad-app-customize-intro/sis-ad-app-customize-standalone.md "").
:
Added option to enable or disable Offline mode using a REST API request in [Offline Transactions](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-pymnt-svcs-offline-txn-intro.md "").
:
Added note stating that meta keys are not supported in [Generate a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro/sis-pymnt-svcs-cloud-mode-bearer-token-task.md "").
:
Updated Acceptance Devices app to version 1.18.0. See [Acceptance Devices App Version 1.18.0 Release Notes](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-release-notes-intro/sis-release-notes-archive-intro/sis-rel-notes-intro-ad-app-v118.md "").

Introduction to Acceptance Devices \| PAX Acceptance Devices App {#semi-integrated-solution-pax-intro}
======================================================================================================

The PAX Acceptance Devices App enables partners to easily integrate their point-of-sale (POS) systems with supported PAX terminals in a semi-integrated manner using Local and Cloud modes. Leveraging the Acceptance Devices Android app and using API requests, your POS system can accept payments by communicating with the PAX terminal over a local Wi-Fi network or the cloud.  
The solution can also be operated in Standalone mode. This mode does not require integration with a POS system and enables you to start transactions directly from the PAX terminal.  
For more information about the modes available in the Acceptance Devices app, see:

* [Local Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro.md "")
* [Cloud Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro.md "")
* [Standalone Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro.md "")

{#semi-integrated-solution-pax-intro_ul_l5b_yqm_3fc}  
For information about the current version of the Acceptance Devices Android app, see the [Release Notes for PAX Acceptance Devices App](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-release-notes-intro.md "").

Supported Payment Terminals and Capabilities {#sis-pax-supported-terminals}
===========================================================================

The PAX All-in-One Android Solution supports a variety of PAX payment terminals, card types, and payment services, as shown in the tables.

> IMPORTANT Processor support differs across terminals, card types, and payment services.

|                    ![Payment Terminals](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/payment-terminal-icon-135x75.svg/jcr:content/renditions/original)                     | ![Features and Specifications](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/features-icon-165x75.svg/jcr:content/renditions/original) | ![Connectivity](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/connectivity-icon-95x75.svg/jcr:content/renditions/original) |                                                                                                             ![Product Guide](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/prod-guide-icon-110x75.svg/jcr:content/renditions/original)                                                                                                              |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                                                                                                                                                                                                                                                                                                                                                                                                         ![All terminals support retail, food and beverage, and travel and hospitality](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/terminal-support-bar-570x17.svg/jcr:content/renditions/original)                                                                                                                                                                                                                                                                                                                                                                                                         ||||
|             ![PAX A35 countertop payment terminal](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/pax-a35-terminal-250x115.svg/jcr:content/renditions/original)              |                                                                           Android 10 PCI PTS 6.0 4-inch display Privacy shield                                                                            |                                                                                        Ethernet Wi-Fi                                                                                         |                                                                                                                                                [PAX A35](https://developer.cybersource.com/docs/cybs/en-us/pax-a35/activation/all/pax-a35/pax-a35/pax-a35-intro.md "")                                                                                                                                                 |
|            ![PAX A3700 countertop payment terminal](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/pax-a3700-terminal-250x95.svg/jcr:content/renditions/original)            |                                                                              Android 11 PCI PTS 6.0 7-inch display Portable                                                                               |                                                                                        Ethernet Wi-Fi                                                                                         |                                                                                                                                              [PAX A3700](https://developer.cybersource.com/docs/cybs/en-us/pax-a3700/activation/all/pax-a3700/pax-a3700/home-merch.md "")                                                                                                                                              |
|              ![PAX A50 handheld payment terminal](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/pax-a50-terminal-250x115.svg/jcr:content/renditions/original)               |                                                                                   Android 10 PCI PTS 6.0 4-inch display                                                                                   |                                                                                           Wi-Fi 4G                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                        |
|              ![PAX A77 handheld payment terminal](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/pax-a77-terminal-250x115.svg/jcr:content/renditions/original)               |                                                                        Android 8 PCI PTS 6.0 5.5-inch display Professional scanner                                                                        |                                                                                           Wi-Fi 4G                                                                                            |                                                                                                                                                [PAX A77](https://developer.cybersource.com/docs/cybs/en-us/pax-a77/activation/all/pax-a77/pax-a77/pax-a77-intro.md "")                                                                                                                                                 |
|              ![PAX A99 handheld payment terminal](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/pax-a99-terminal-250x115.svg/jcr:content/renditions/original)               |                                                                              Android 12 PCI PTS 6.0 5.5-inch display Printer                                                                              |                                                                                           Wi-Fi 4G                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                        |
|            ![PAX A6630 handheld payment terminal](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/pax-a6630-terminal-250x115.svg/jcr:content/renditions/original)             |                                                                       Android 12 PCI PTS 6.0 6.5-inch display Professional scanner                                                                        |                                                                                           Wi-Fi 4G                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                        |
|            ![PAX A6650 handheld payment terminal](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/pax-a6650-terminal-250x115.svg/jcr:content/renditions/original)             |                                                                       Android 12 PCI PTS 6.0 6.5-inch display Professional scanner                                                                        |                                                                                           Wi-Fi 4G                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ![PAX A920, A920 PRO, and A920 MAX handheld payment terminals](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/pax-a920-terminal-250x130.svg/jcr:content/renditions/original) |                                                                        Android 8 or 10 PCI PTS 6.0 5.5- or 6-inch display Printer                                                                         |                                                                                           Wi-Fi 4G                                                                                            | [PAX A920](https://developer.cybersource.com/docs/cybs/en-us/pax-a920/activation/all/pax-a920/pax-a920/pax-a920-intro.md "") [PAX A920 PRO](https://developer.cybersource.com/docs/cybs/en-us/pax-a920pro/activation/all/pax-a920pro/pax-a920pro/pax-a920pro-intro.md "") [PAX A920 MAX](https://developer.cybersource.com/docs/cybs/en-us/pax-a920max/activation/all/pax-a920max/pax-a920max/pax-a920max-intro.md "") |
|            ![PAX IM30 unattended payment terminal](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/pax-im30-terminal-250x115.svg/jcr:content/renditions/original)             |                                                                          Android 10 PCI PTS 6.0 5-inch display Mounting bracket                                                                           |                                                                                        Ethernet Wi-Fi                                                                                         |                                                                                                                                              [PAX IM30](https://developer.cybersource.com/docs/cybs/en-us/pax-im30/activation/all/pax-im30/pax-im30/pax-im30-intro.md "")                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                         ![All terminals support retail, food and beverage, and travel and hospitality](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/terminal-support-bar-570x17.svg/jcr:content/renditions/original)                                                                                                                                                                                                                                                                                                                                                                                                         ||||
[Supported PAX Payment Terminals]

|     Card Type     |                                                                                                                                                                                                               Processor                                                                                                                                                                                                                ||                     Payment Service                      |                                                                                                                                                                                                               Processor                                                                                                                                                                                                                ||
|     Card Type     |                                                                                                FDC Nashville Global                                                                                                |                                                                                               Visa​ Platform Connect                                                                                               |                     Payment Service                      |                                                                                                FDC Nashville Global                                                                                                |                                                                                               Visa​ Platform Connect                                                                                               |
|:-----------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| American Express  | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |                   Account verification                   | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
|  China Union Pay  | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |    ![grey circle with dash icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circle-line-filled-26x26.svg/jcr:content/renditions/original)    |                         Capture                          | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
|      Diners       | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |                         Cashback                         |    ![grey circle with dash icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circle-line-filled-26x26.svg/jcr:content/renditions/original)    | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
|     Discover      | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |                     Custom card read                     | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
|        EBT        |    ![grey circle with dash icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circle-line-filled-26x26.svg/jcr:content/renditions/original)    | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |                Incremental authorization                 |    ![grey circle with dash icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circle-line-filled-26x26.svg/jcr:content/renditions/original)    | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
|        JCB        | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |    ![grey circle with dash icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circle-line-filled-26x26.svg/jcr:content/renditions/original)    |           Mail order or telephone order (MOTO)           | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
|    Mastercard     | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | Offline sale (Deferred authorization/​Store and Forward) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
|       Meeza       |    ![grey circle with dash icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circle-line-filled-26x26.svg/jcr:content/renditions/original)    | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |                    On-reader tipping                     | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
| U.S. Common Debit | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |                    On-receipt tipping                    | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
|       Visa        | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |                    Pre-​authorization                    | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
|                   |                                                                                                                                                                                                                    |                                                                                                                                                                                                                    |                          Refund                          | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
|                   |                                                                                                                                                                                                                    |                                                                                                                                                                                                                    |                           Sale                           | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
|                   |                                                                                                                                                                                                                    |                                                                                                                                                                                                                    |                    Stand-alone credit                    | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
|                   |                                                                                                                                                                                                                    |                                                                                                                                                                                                                    |                       Token refund                       | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) | ![green circle with checkmark icon](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/circlecheck-filled-26x26.svg/jcr:content/renditions/original) |
[Supported Card Types, Processors, and Payment Services]

Transaction Workflow for the PAX Acceptance Devices App {#semi-integrated-solution-pax-workflow}
================================================================================================

This is the transaction workflow for the PAX Acceptance Devices App.

#### Figure: {#semi-integrated-solution-pax-workflow_fig_jtg_4nz_yxb1}

PAX Acceptance Devices App Transaction Workflow ![PAX Acceptance Devices App transaction workflow showing the sequence of
events](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/pax-sis-sequence-diagram.svg/jcr:content/renditions/original)  
The PAX Acceptance Devices App workflow typically includes this sequence of events:

1. The point-of-sale (POS) system, running on Windows, Android, or iOS, integrates to the PAX Acceptance Devices App APIs.
2. The merchant's POS system sends an API request, using the local Wi-Fi network or the cloud, to the Acceptance Devices app that is running on the PAX terminal.
3. The Acceptance Devices app user interface shows on the PAX terminal screen and displays prompts to guide the customer through the payment flow.
4. The Acceptance Devices app sends an API response to the POS system with the transaction result and details, which completes the transaction.
   {#semi-integrated-solution-pax-workflow_ol_xhq_lnz_yxb1}

Getting Started with the Acceptance Devices App {#semi-integrated-solution-pax-get-started-intro}
=================================================================================================

Use this information to get started with using the Acceptance Devices app. After completing device set up and app configuration, you can process payments in these modes:

* [Local Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro.md "")
* [Cloud Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro.md "")
* [Standalone Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro.md "")
  {#semi-integrated-solution-pax-get-started-intro_ul_mjg_kkm_d2c}

Set Up a PAX Terminal {#semi-integrated-solution-pax-setup-terminal}
====================================================================

To set up a PAX terminal, the Acceptance Devices app must be open on the terminal. This app is automatically and remotely installed the first time the terminal connects to the internet.
IMPORTANT Regularly update the Acceptance Devices App to take advantage of the latest features, performance improvements, and security enhancements. Only the five most recent versions are supported and made available.  
For details about the current version of the Acceptance Devices app, see the [Release Notes for PAX Acceptance Devices App](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-release-notes-intro.md ""). Follow these steps to set up the PAX terminal in the Acceptance Devices app.

1. Open the Acceptance Devices app on the PAX terminal.

2. On the Welcome screen, tap Start Configuration.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-setting-up-pax-terminal-2.png/jcr:content/renditions/original)

3. On the Select Language screen, choose the language you want to use on the terminal. Tap Continue.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-setting-up-pax-terminal-3.png/jcr:content/renditions/original)

4. On the Create a Passcode screen, enter a unique passcode. The passcode must consist of six digits. Confirm the passcode by entering it a second time. Tap Save Passcode.

   #### ADDITIONAL INFORMATION

   IMPORTANT You will use this passcode to access the app, so choose a code that you will remember. The app does not include an option to reset the passcode. If you forget the it, you must reinstall the Acceptance Devices app and complete the set-up process again.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-setting-up-pax-terminal-4.png/jcr:content/renditions/original)

5. When your device is not connected to the internet, the Connect to Internet screen appears. Tap Connect to Internet, and choose your Wi-Fi network from the list that appears.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-setting-up-pax-terminal-5.png/jcr:content/renditions/original)

6. When your device is connected to the internet, the Internet Connected screen appears. Tap Continue.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-setting-up-pax-terminal-6.png/jcr:content/renditions/original)

7. On the Appearance Preferences screen, you are promoted to allow changes to system settings such as screen brightness. Take one of these actions:

   * To change the appearance preferences, tap Allow.
   * To keep the default settings, tap Skip. You can make changes later. The next set-up screen appears.  
     ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-setting-up-pax-terminal-7.png/jcr:content/renditions/original)
8. If you allow changes to the appearance preferences, the Can Modify System Settings screen appears. To enable Allow modify system settings, slide the toggle switch to the right. Tap the back navigation arrow to return to the Adjust Screen Brightness screen.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-setting-up-pax-terminal-8.png/jcr:content/renditions/original)

9. On the Adjust Screen Brightness screen, move the slider left or right to adjust screen brightness. Tap Continue.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-setting-up-pax-terminal-9.png/jcr:content/renditions/original)

10. On the Automatic Standby Time screen, you can choose how long the device screen remains active when there is no activity. Select a standby time, and then tap Continue. If your terminal has an integrated printer, the Load Paper screen appears. See [Load Paper in the PAX Terminal with an Integrated Printer](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/semi-integrated-solution-pax-setup-terminal-load-p.md ""). If the terminal does not have a printer, you are prompted to activate your terminal in the Acceptance Devices app. See [Activating a Terminal in the Acceptance Devices App](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/semi-integrated-solution-ad-app-activate-terminal-.md "").  
    ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-setting-up-pax-terminal-10.png/jcr:content/renditions/original)

Load Paper in the PAX Terminal with an Integrated Printer {#semi-integrated-solution-pax-setup-terminal-load-paper}
===================================================================================================================

If your PAX terminal is equipped with an integrated printer, a roll of printer paper is included with the device when sent to you. Have the paper roll available. The Load Paper screen appears on the device during terminal set up only when a terminal has an integrated printer. To print transaction receipts, the paper roll must be loaded into the terminal.  
Follow these steps to load printer paper in the PAX terminal.

1. On back of the terminal, open the printer hatch by moving the printer cover switch toward the bottom of the device.
2. Review the diagram on the inside of the hatch, which shows the correct way to insert the paper roll.
3. Insert the paper roll.
4. Pull out approximately 1 inch of the paper beyond the hatch. This step reduces the possibility of a paper jam occurring when you print the first receipt.
5. Close the hatch.
6. Tap Continue. You are prompted to activate your terminal in the Acceptance Devices app. See [Activating a Terminal in the Acceptance Devices App](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/semi-integrated-solution-ad-app-activate-terminal-.md "").  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-loading-printer-paper-1.png/jcr:content/renditions/original)

Activating a Terminal in the Acceptance Devices App {#semi-integrated-solution-ad-app-activate-terminal-intro}
==============================================================================================================

To process payments on your PAX device using the Acceptance Devices app and your point-of-sale (POS) system, you must activate a terminal in the Acceptance Devices app by using an activation code. You can generate the code in the `Business Center` or by using an API request. After generating the activation code, you must enter it in the Acceptance Devices app.

Generate a Terminal Activation Code in the `Business Center` {#semi-integrated-ad-app-activation-code-ebc}
==========================================================================================================

The terminal activation code that you generate in the `Business Center` is valid for 24 hours.  
Follow these steps to generate a terminal activation code.

1. In the `Business Center`, go to the left navigation panel and choose Acceptance Devices \&gt; Activation Codes. The Activation Codes page appears.
2. Click the Select Transacting MID drop-down menu.
3. Choose a transacting MID from the list.
4. Click the Select number of Activation Codes drop-down menu.
5. Choose the number of activation codes that you want to generate. The maximum number of codes is 15.
6. Click Generate. The activation codes display on the page. To copy the codes to your clipboard, click the icon next to the code.
7. To download a text file containing the activation codes, click the Download codes as a .txt file button.
8. Navigate to the Download folder on your computer to access the text file.

Generate a Terminal Activation Code Using a REST API Request {#semi-integrated-ad-app-activation-code-api-intro}
================================================================================================================

Before activating the terminal in the Acceptance Devices app, you must generate a terminal activation code.  
You can use a REST API request to generate a terminal activation code, which is valid for 24 hours.  
You must authenticate each request that you send to a `Cybersource` API. In order to authenticate an API request, you can use a REST shared secret key or a REST certificate. For more information about authentication requirements, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "").

Endpoints
---------

The POST request must include the transacting merchant ID (MID) that is sending the request and the quantity of activation codes to be generated. You can request up to 15 activation codes in a single request.  
**Test:** `POST ``https://apitest.cybersource.com``/dms/v2/merchants/{transacting mid}/activation-codes?size={number of activation codes}`  
**Production:** `POST ``https://api.cybersource.com``/dms/v2/merchants/{transacting mid}/activation-codes?size={number of activation codes}`

Required Fields for Generating a Terminal Activation Code {#semi-integrated-ad-app-activation-code-api-reqfields}
=================================================================================================================

The body of the API request is empty. The POST request must include the information required to return the response.

REST Example: Generating a Terminal Activation Code {#semi-integrated-ad-app-activation-code-api-ex-rest}
=========================================================================================================

Request  
The body of the request is empty. The POST request includes the information required to return the response.

```
{
}
```

Response to a Successful Request  
The response includes the activation code (token field) and the amount of time (ttl field) that the activation code is valid. The ttl field value is shown in milliseconds. The activation code is valid for 24 hours.

```
{
    "tokens": [
        {
            "token": "%N5wU2jH",
            "ttl": 86399805
        }
    ]
}
```

Enter an Activation Code in the Acceptance Devices App {#semi-integrated-solution-ad-app-enter-activation-code}
===============================================================================================================

Before activating a terminal, you must generate a terminal activation code for the device in the `Business Center` or by using a REST API request. The activation code is valid for 24 hours. Follow these steps to enter a terminal activation code in the Acceptance Devices app.

1. On the Device Activation screen, enter the activation code that you generated. Tap Continue.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-activating-terminal-1.png/jcr:content/renditions/original)
2. When the activation code is accepted, the Activation Successful screen appears. Tap Confirm.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-activating-terminal-2.png/jcr:content/renditions/original)

#### AFTER COMPLETING THE TASK

If you are using the app in Local mode with Mutual Transport Layer Security (mTLS) enabled, you must activate a secure mTLS connection between your point-of-sale (POS) system and the Android device in the Acceptance Devices app. See [Activating a Secure mTLS Connection](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-activate-mtls-connection-intro.md "").  
If you are using the app in Local mode with Transport Layer Security (TLS) enabled or in Cloud mode, you must start the Acceptance Devices app server. See [Start the Acceptance Devices App Server](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/semi-integrated-ad-app-starting-server-intro/semi-integrated-ad-app-start-server.md "").

Getting Started with the Acceptance Devices App Server {#semi-integrated-ad-app-starting-server-intro}
======================================================================================================

To process payments on your payment terminal using the Acceptance Devices app and your point-of-sale (POS) system, you must first start the Acceptance Devices app server on the terminal.

Start the Acceptance Devices App Server {#semi-integrated-ad-app-start-server}
==============================================================================

Before you can start the Acceptance Devices app server, you must activate a terminal in the Acceptance Devices app. For more information, see [Activating a Terminal in the Acceptance Devices App](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/semi-integrated-solution-ad-app-activate-terminal-.md ""). Follow these steps to start the Acceptance Devices app server.

1. Before you start the server, the Device Status screen shows the *Device is not connected* message. Tap Connect Device.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-getting-started-acceptance-devices-app-server-1.png/jcr:content/renditions/original)
2. After you start the server, the Device Status screen shows the *Device connected* message. The terminal is activated and ready to accept transactions.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-getting-started-acceptance-devices-app-server-2.png/jcr:content/renditions/original)
3. Tap the back navigation arrow to finish setup.

Customizing the Acceptance Devices App {#sis-ad-app-customize-intro}
====================================================================

Use this information to customize the Acceptance Devices app in the `Business Center` or by using a REST API request.  
The Acceptance Devices Customizations feature in the `Business Center` enables you to customize these parameters for a portfolio, merchant, or transacting merchant ID (MID):

* User interface

* Common

* Local mode

* Standalone mode
  {#sis-ad-app-customize-intro_ul_ups_rql_fgc}  
  You can use a REST API request to perform these customization tasks:

* Retrieve and review your current parameter customization settings.

* Update customization settings for user interface, common, Local mode, and Standalone mode parameters.
  {#sis-ad-app-customize-intro_ul_nms_mtz_1bc}

Customizable User Interface Parameters {#sis-ad-app-customize-ui}
=================================================================

You can customize these user interface parameters for the Acceptance Devices app when it is in Local, Standalone, or Cloud mode.

Home screen logo
:
This parameter defines the logo that is shown on the home screen of the app.

Toolbar logo
:
This parameter defines the logo that is shown on the app screen during transaction processing.

Primary color
:
This parameter defines the color of the primary buttons.

Color on primary
:
This parameter defines the color of the text on the primary buttons.

Background color
:
This parameter defines the color of the screen background.

Color on background
:
This parameter defines the color of the text on the screen background.

Button shape
:
This parameter defines the shape of the buttons.

Customizable Common Parameters {#sis-ad-app-customize-common}
=============================================================

You can customize these common parameters in the Acceptance Devices app when it is operating in Local, Standalone, or Cloud mode.

Operating mode
:
This parameter enables you to choose one of these operating modes:

    * `Semi-Integrated with Standalone:` The Acceptance Devices app operates in Local and Standalone modes. This setting is the default.
    * `Semi-Integrated:` The Acceptance Devices app operates in Local mode only.
    * `Standalone:` The Acceptance Devices app operates in Standalone mode only.
    * `Cloud with Standalone:` The Acceptance Devices app operates in Cloud and Standalone modes.
    * `Cloud:` The Acceptance Devices app operates in Cloud mode only.

Automatic receipt printing
:
This parameter enables the automatic printing of the merchant or customer receipt after each transaction. This feature is available only on terminals with integrated printers. The default setting is `Disabled`.

Accessibility options
:
This parameter enables accessibility features during transaction processing. For example, voice-over capabilities that provide information to visually impaired customers. The default setting is `True`.

Enable Offline mode
:
This parameter enables Offline mode, which you can use to process transactions when an internet connection is not available. The default setting is `False`.

MOTO options
:
This parameter enables you to activate these MOTO options:

    * `MOTO address required:` This parameter enables the customer's address as a required data input for mail order or telephone order (MOTO) transactions. The default setting is `True`.
    * `MOTO show confirmation screen:` This parameter enables a Confirmation screen to appear during MOTO transactions. The merchant reviews and confirms the MOTO address data shown on the screen before the payment is processed. The default setting is `False`.
    * `MOTO CVV required:` This parameter enables the Card Verification Value (CVV) as a required data input for MOTO transactions. The default setting is `True`.
    {#sis-ad-app-customize-common_ul_cky_pyb_nhc}

Offline transaction maximum amount
:
This parameter defines the maximum amount allowed for an offline transaction.

Offline transaction batch maximum amount
:
This parameter defines the maximum amount allowed for an offline transaction batch submitted for authorization.

Tipping options
:
This parameter enables you to choose one of these tipping types:

    * `Percentage:` The customer chooses from three pre-defined tip percentages or enters a custom tip amount. Define the tip values in the Tipping percentage values parameter. This setting is the default tipping type.
    * `Tip amount:` The customer enters a custom tip amount.
    * `Total amount:` The customer enters the total amount to be charged, including the tip amount.

Tipping percentage values
:
This parameter defines the three tipping percentages that appear on the screen. The customer can choose an option. This parameter applies only when the Tipping Type parameter is set to `Percentage`. The default settings are `10, 15, 20`.

Tipping confirmation screen
:
This parameter enables the Tipping Confirmation screen to appear on the device during a sale with on-reader tipping. The customer reviews and confirms the tip amount before the payment is processed. The default setting is `False`.

Transaction history view
:
This parameter defines whether the transaction history view is shown at the merchant or device level. The default setting is `Merchant`.

Enable kiosk mode
:
This parameter enables Kiosk Mode on the PAX device. This mode locks the Acceptance Devices app to the device screen. Users cannot exit the app or access other terminal functions, which helps prevent unauthorized use. The default setting is `False`.

Customizable Local Mode Parameters {#sis-ad-app-customize-semi-integrated}
==========================================================================

You can customize these local mode parameters for the Acceptance Devices app.

Port
:
This parameter defines the port number used by the server on the terminal. The default setting is `8443`.

Security
:
This parameter defines whether the server on the terminal uses two-way verification (mTLS) or one-way verification (TLS). The default setting is `mTLS`.

Protocol
:
This parameter defines the protocol that is used to process transactions. The default setting is `ADP`.

Signature capture type
:
This parameter defines whether the signature is captured on the terminal screen or paper receipt, or is skipped. The default setting is `On screen`.

Skip summary screen
:
This parameter keeps the Summary screen from appearing after each transaction. The default setting is `True`.

Customizable Standalone Mode Parameters {#sis-ad-app-customize-standalone}
==========================================================================

You can customize these standalone mode parameters for the Acceptance Devices app.

Enable LAC installments
:
This parameter enables the processing of Latin America and the Caribbean (LAC) installment payments. The default setting is `Disabled`.

Enable tax details
:
This parameter enables tax details to be shown in the app. The default setting is `Disabled`.

Enable payment facilitator details
:
This parameter enables the payment facilitator details to be shown in the app. The default setting is `Disabled`.

Additional transaction types
:
This parameter enables you to choose additional transaction types that the app supports. Sale and refund transactions are supported by default. The default setting for additional transaction types is `None`.

Customize Parameters in the `Business Center` {#sis-ad-app-customize-ebc}
=========================================================================

Follow these steps to customize common, Local mode, and Standalone mode parameters for the Acceptance Devices app.

1. In the `Business Center`, go to the left navigation panel and choose Acceptance Devices **\&gt;** Customizations. The Customizations page appears.
2. Click the Load customization parameter for drop-down menu.
3. Choose a user level from the list. Click Load.
4. Scroll down to see the various parameter sections and which elements you can customize for the chosen user level.
5. Choose parameters to customize. To see a description of a parameter, hover your mouse over the Information icon.
6. Click Apply Changes.

Retrieve Parameters Using a REST API Request {#sis-ad-app-customize-retrieve-param-rest-api-intro}
==================================================================================================

You can use a REST API request to retrieve and view customizable parameters and their current values. Your account settings determine the values you can view for a portfolio, merchant, or transacting merchant ID (MID).  
You must authenticate each request that you send to a `Cybersource` API. In order to authenticate an API request, you can use a REST shared secret key or a REST certificate. For more information about authentication requirements, see the [Getting Started with REST Developer Guide](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "").

Endpoints
---------

The GET request must include the organization ID for the portfolio, merchant, or transacting merchant ID that is sending the request.  
**Test:** `GET ``https://apitest.cybersource.com``/dms/v2/customization?type=organization&id={{organization id}}`  
**Production:** `GET ``https://api.cybersource.com``/dms/v2/customization?type=organization&id={{organization id}}`

Required Fields to Retrieve Parameters Using a REST API Request {#sis-ad-app-customize-retrieve-param-rest-api-reqfields}
=========================================================================================================================

The body of the API request is empty. The GET request must include the information required to return the response.

REST Example: Retrieve Parameters Using a REST API Request {#sis-ad-app-customize-retrieve-param-api-ex-rest}
=============================================================================================================

Request  
The body of the request is empty. The GET request includes the information required to return the response.

```
{
}
```

Response to a Successful Request

```
{
    "id": "{{organization id}}",
    "customizations": {
        Your configured parameters response data appears here.
    },
    "customizationMetadata": {
        Your possible values for parameters response data appears here.
    }
}
```

Customize Parameters Using a REST API Request {#sis-ad-app-customize-param-rest-api-intro}
==========================================================================================

You can use a REST API request to update customizable parameters for a portfolio, merchant, or transacting merchant ID (MID).  
You must authenticate each request that you send to a `Cybersource` API. In order to authenticate an API request, you can use a REST shared secret key or a REST certificate. For more information about authentication requirements, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "").

Endpoints
---------

**Test:** `PUT ``https://apitest.cybersource.com``/dms/v2/customization`  
**Production:** `PUT ``https://api.cybersource.com``/dms/v2/customization`

Required Fields for Customizing Parameters Using a REST API Request {#sis-ad-app-customize-param-rest-api-reqfields}
====================================================================================================================

type
:
Set the value to `organization`.

id
:
Set the value to `organization id` for the portfolio, merchant, or transacting MID.

customizations
:
Set the value to the parameters to be updated.

REST Example: Customizing Parameters Using a REST API Request {#sis-ad-app-customize-param-rest-api-ex-rest}
============================================================================================================

Request

```
{
    "type": "organization",
    "id": "{{organization id}}",
    "customizations":
    {
        "OPERATING_MODE": "SEMI_INTEGRATED",
        "TIPPING_TYPE": "TIP_AMOUNT",
        "SIGNATURE_TYPE": "ON_RECEIPT"
    }
}
```

Response to a Successful Request  
The body of the response is empty. A successful response is indicated with a `200 OK` status.

```
{
}
```

Enable Kiosk Mode {#sis-ad-app-enable-kiosk-mode}
=================================================

Enable Kiosk Mode to hide the navigation and status bars on a PAX terminal. This mode locks the Acceptance Devices app to the screen. When enabled, users cannot exit the app or access other terminal functions, which helps prevent unauthorized use.  
Follow these steps to enable Kiosk Mode in the Acceptance Devices app.

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Kiosk Mode.
4. Toggle Enable Kiosk Mode to ON.
5. If prompted to allow the app to display over other apps, tap Allow.
6. Tap the back navigation arrow to return to the home screen.

Local Mode Payment Services {#semi-integrated-pymnt-svcs-intro}
===============================================================

Use this information to process payment services available in the Acceptance Devices app when operated in Local mode.  
These are some Local mode features:

* The point-of-sale (POS) system communicates with the Acceptance Devices app on the terminal over a local Wi-Fi network.

* You can retrieve the Root CA certificate to validate the Acceptance Devices app server's certificate.

* You have the option to activate an mTLS connection in the Acceptance Devices app.

* You have the option to implement hostname validation in your client.
  {#semi-integrated-pymnt-svcs-intro_ul_rts_tjh_bbc}  
  For information about other modes available in the Acceptance Devices app, see:

* [Cloud Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro.md "")

* [Standalone Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro.md "")
  {#semi-integrated-pymnt-svcs-intro_ul_l5b_yqm_3fc}

Communication Protocol Used in Local Mode {#semi-integrated-ad-app-comm-protocol}
=================================================================================

When using the solution in Local mode, the communication protocol used between the Acceptance Devices app and the point-of-sale (POS) system is a single WebSocket channel. Through this channel, simultaneous, two-way communication occurs between the Acceptance Devices app and the POS system.

Retrieving the Root CA Certificate {#semi-integrated-ad-app-retrieve-rootca-cert-intro}
=======================================================================================

When the app is operating in Local mode, you can validate the Acceptance Devices app server's certificate by adding the Root CA certificate to your trust store. This action is required if you want to use an mTLS connection. For more information, see [Activating a Secure mTLS Connection](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-activate-mtls-connection-intro.md "").  
You can retrieve the Root CA certificate in the `Business Center` or by using a REST API request.

Retrieve the Root CA Certificate in the `Business Center` {#sis-ad-app-retrieve-rootca-cert-ebc}
================================================================================================

Follow these steps to retrieve the Root CA certificate in the Business Center:

1. In the `Business Center`, go to the left navigation panel and choose Acceptance Devices \&gt; Activation Codes. The Activation Codes page appears.
2. Click Download Root CA Certificate. When the download is complete, the browser window shows a download completion message.
3. In the local folder directory of your computer, navigate to the Download folder to access the Root CA certificate file.

Retrieve the Root CA Certificate Using a REST API Request {#semi-integrated-ad-app-retrieve-rootca-cert-task}
=============================================================================================================

You can use a REST API request to retrieve the Acceptance Devices app server's Root CA certificate when the app is operating in Local mode. You would then add the certificate to your trust store.  
You must authenticate each API request you send to a `Cybersource` API by using a REST shared secret key or a REST certificate. For more information about authentication requirements, see the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.md "").

Endpoints
---------

**Test:** `GET ``https://apitest.cybersource.com``/dms/v2/devices/certificates/rootca`  
**Production:** `GET ``https://api.cybersource.com``/dms/v2/devices/certificates/rootca`

Required Fields to Retrieve the Root CA Certificate Using a REST API Request {#semi-integrated-ad-app-retrieve-rootca-cert-api-reqfields}
=========================================================================================================================================

The body of the API request is empty.

REST Example: Retrieve the Root CA Certificate Using a REST API Request {#semi-integrated-ad-app-retrieve-rootca-cert-api-ex-rest}
==================================================================================================================================

Request  
The body of the request is empty.

```
{
}
```

Response to a Successful Request  
The response includes a PEM--encoded certificate chain.

```
{
    "certificateChain": "-----BEGIN CERTIFICATE-----Your certificate response data appears here.-----END CERTIFICATE-----"
}
```

Activating a Secure mTLS Connection {#sis-activate-mtls-connection-intro}
=========================================================================

When the app is operating in Local mode, using a Mutual Transport Layer Security (mTLS) connection creates an additional layer of security for communication between the Acceptance Devices app running on your PAX terminal and point-of-sale (POS) system.  
Using the mTLS protocol is recommended because it employs two-way verification. The minimum requirement for providing end-to-end data security is using the Transport Layer Security (TLS) protocol.  
Before activating an mTLS connection, you must retrieve the Root CA certificate. For more information, see [Retrieving the Root CA Certificate](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/semi-integrated-ad-app-retrieve-rootca-cert-intro.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** `POST https://{terminal IP address:port number}/ or wss://{terminal IP address:port number}/`  
**Production:** `POST https://{terminal IP address:port number}/ or wss://{terminal IP address:port number}/`

Generate a POS Connection Code for the Point-of-Sale System {#sis-activate-mtls-pos-setup-code}
===============================================================================================

Before you can sync the terminal with the point-of-sale (POS) system to establish a secure connection, you must activate the terminal. For more information, see [Activating a Terminal in the Acceptance Devices App](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/semi-integrated-solution-ad-app-activate-terminal-.md ""). To ensure the security of the data sent over the internet between your POS system and the PAX terminal, you must establish a secure connection (sync) between your system and the terminal. You must complete this procedure one time only for each POS system you are using.  
If Mutual Transport Layer Security (mTLS) is enabled, and terminal activation is complete, the Generate Code screen appears during terminal set up.  
Follow these steps to generate a POS connection code for a POS system in the Acceptance Devices app:

1. On the Generate Code screen, tap Generate Code.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-activating-secure-mtls-connection-1.png/jcr:content/renditions/original)
2. Record the eight-character code that appears on the screen. You will use this code to request a certificate from the POS system. The screen shows an expiration timer for the code, which refreshes every 300 seconds.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-activating-secure-mtls-connection-2.png/jcr:content/renditions/original)

Request Certificates for the Point-of-Sale System {#sis-activate-mtls-pos-setup-request-cert}
=============================================================================================

Before you can request certificates, you must generate a set-up code for the POS system. To finish activating the secure mTLS connection, request certificates for the POS system by sending a request to the PAX terminal through the POS system.

1. On the Generate Code screen, tap the Details arrow. The Details section expands to show the HTTP and WSS (WebSocket) addresses and the port number.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-activating-secure-mtls-connection-3.png/jcr:content/renditions/original)
2. Record the HTTP and WSS addresses and port number shown in the Details section. You will use this information to request a certificate through the POS system, using the HTTPS or WSS address.
3. To request the certificates, send an API request through the POS system to the HTTP or WSS address and port number, along with the POS connection code shown on the terminal and a unique POS ID.
4. After the certificates are retrieved by the POS system and the sync between your POS system and the PAX terminal is complete, the *POS Activation Successful* message appears. Tap Close. The next set-up screen appears.  
   ![](/content/dam/documentation/cybs/en-us/topics/payments-processing/card-processing/semi-integrated-solution/images/sis-activating-secure-mtls-connection-4.png/jcr:content/renditions/original)

Required Fields to Request Certificates for the Point-of-Sale System {#sis-activate-mtls-pos-setup-request-cert-api-reqfields}
==============================================================================================================================

posId
:
Set the value to a unique, user-defined ID for the POS system.

setupCode
:
Set the value to the POS connection code shown on the Generate POS Connection Code screen in the Acceptance Devices app.

REST Example: Request Certificates for the Point-of-Sale System {#sis-activate-mtls-pos-setup-request-cert-api-ex-rest}
=======================================================================================================================

Request

```
{
  "posId" : "123",
  "setupCode" : "8QW1YS1D"
}
```

Response to a Successful Request  
The response includes the private key and certificates required to establish the secure Mutual Transport Layer Security (mTLS) connection between the PAX terminal and the POS system. For security reasons, this example does not show actual private key and certificate response data.

```
-----BEGIN RSA PRIVATE KEY-----
Your RSA private key response data appears here.
-----END RSA PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
Your certificate response data appears here.
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
Your certificate response data appears here.
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
Your certificate response data appears here.
-----END CERTIFICATE-----
```

Implementing Hostname Validation in Local Mode {#sis-local-ad-app-hostname-validate}
====================================================================================

When operating in Local mode, your app can optionally perform hostname validation for enhanced security. When the terminal is activated, a certificate is generated on the device. The certificate includes a Subject Alternative Name (SAN). This SAN appears as a Domain Name System (DNS) entry for the Acceptance Devices app server.  
This is the SAN format:

```
{terminal-serial-number}.cybs.seclib.io
```

To enable hostname validation or connect to the terminal using the SAN instead of its IP address, update your system's `hosts` file to include both the terminal's IP address and its corresponding SAN.

Sale {#semi-integrated-pax-pymnt-svcs-sale-api-intro}
=====================================================

Use this information to process a sale transaction when the app is in Local mode. This type of transaction combines an authorization and a capture into a single transaction.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale {#semi-integrated-pax-pymnt-svcs-sale-api-reqfields}
===============================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Sale {#semi-integrated-pax-pymnt-svcs-sale-api-ex-rest}
=====================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "1541387b383d456aabb81cdf558b4e8e",
        "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc" : "2023-12-01T20:24:47+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "1.00",
          "refundableAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014622903166318504010"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Refund {#sis-pymnt-svcs-refund-api-intro}
=========================================

Use this information to process a refund when the app is in Local Mode mode. This type of refund includes a reference to the original transaction for a full or partial transaction amount. Stand-alone credits are also supported in this Acceptance Devices solution. For more information, see [Stand-Alone Credit](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-local-standalone-credit-api-intro.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Refund {#sis-pymnt-svcs-refund-api-reqfields}
===================================================================

type
:
Set the value to `LinkedRefundRequest`.

transactionId
:
Set the value to the `id` field value from the original transaction.

Optional Fields for a Refund {#sis-pymnt-svcs-refund-api-optfields}
===================================================================

Use the optional amount and currency fields to process a partial refund. Otherwise, the full amount will be refunded.

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Refund {#sis-pymnt-svcs-refund-api-ex-rest}
=========================================================

Request

```
{
      "type": "LinkedRefundRequest",
      "transactionId": "8fe5fa21d0814424bcec4997c9dc89c4",
      "amountDetails": {
        "amount": "1.00",
        "currency": "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
      "type" : "LinkedRefundResponse",
      "message" : "Refund approved",
      "transactionDetails" : {
        "id" : "8fe5fa21d0814424bcec4997c9dc89c4",
        "merchantReferenceCode" : "e94e3aa304514140ae1700ba0959c7c5",
        "submitTimeUtc" : "2023-12-01T20:57:30+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "0.00",
          "refundableAmount" : "0.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014642534986108604008"
      },
      "linkedOperations" : [ {
        "id" : "b383db1aecab46d89f1dbec8b0a9aa90",
        "type" : "REFUND",
        "amount" : "1.00",
        "status" : "APPROVED",
        "submitTimeUtc" : "2023-12-01T20:57:48+0000"
      } ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nVoid\n-£1.00\n\n\nReversal accepted.\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Keyed\n\nAuthorization: -\nMerchant ID: **37599\nTerminal ID: ****0063\n\nb383db1aecab46d89f1dbec8b0a9aa90\n21:57:50: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Void"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "b383db1aecab46d89f1dbec8b0a9aa90"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:57:50"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Reversal accepted."
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nVoid\n-£1.00\n\n\nReversal accepted.\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Keyed\n\nAuthorization: -\nMerchant ID: **37599\nTerminal ID: ****0063\n\nb383db1aecab46d89f1dbec8b0a9aa90\n21:57:50: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Void"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "b383db1aecab46d89f1dbec8b0a9aa90"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:57:50"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Reversal accepted."
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Stand-Alone Credit {#sis-local-standalone-credit-api-intro}
===========================================================

Use this information to process a stand-alone credit when the app is in Local mode. This type of transaction is used to process a credit without reference to the original transaction. The customer is required to present their card for this type of transaction.

> WARNING
> When processing a stand-alone credit, there is no limit on the credit amount because there is no reference to the original transaction amount. The recommendation is to use a refund transaction whenever possible. For more information, see [Refund](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-pymnt-svcs-refund-api-intro.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Stand-Alone Credit {#sis-local-standalone-credit-api-reqfields}
=====================================================================================

type
:
Set the value to `StandaloneRefundRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Stand-Alone Credit {#sis-local-standalone-credit-api-ex-rest}
===========================================================================

Request

```
{
      "type": "StandaloneRefundRequest",
      "merchantReferenceCode": "2490c8ec0e2f4b509526815714313e33",
      "amountDetails": {
        "amount": "1.00",
        "currency": "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
      "type" : "StandaloneRefundResponse",
      "message" : "Refund approved",
      "transactionDetails" : {
        "id" : "3043e0b61fad4c5483db3d498309460f",
        "merchantReferenceCode" : "2490c8ec0e2f4b509526815714313e33",
        "submitTimeUtc" : "2023-12-01T21:04:19+0000",
        "amountDetails" : {
          "amount" : "1.00",
          "currency" : "GBP"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "AMERICAN_EXPRESS",
          "maskedPan" : "374245XXXXX0001"
        }
      },
      "additionalInformation" : {
        "requestId" : "7014646720206287504012"
      },
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nRefund\n-£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks AMEX\nAccount: *** **** **** 0001\nEntry Mode: Chip\nAID: A0000000250100\n\nTransaction: -\nAuthorization: -\nMerchant ID: *****67890\nTerminal ID: ****0026\n\n3043e0b61fad4c5483db3d498309460f\n10:04:19 PM: 12/1/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks AMEX"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "*** **** **** 0001"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000250100"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Chip"
              },
              "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
                "label" : "Transaction",
                "value" : "-"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "*****67890"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0026"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Refund"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "3043e0b61fad4c5483db3d498309460f"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "12/1/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "10:04:19 PM"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nRefund\n-£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks AMEX\nAccount: *** **** **** 0001\nEntry Mode: Chip\nAID: A0000000250100\n\nTransaction: -\nAuthorization: -\nMerchant ID: *****67890\nTerminal ID: ****0026\n\n3043e0b61fad4c5483db3d498309460f\n10:04:19 PM: 12/1/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks AMEX"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "*** **** **** 0001"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000250100"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Chip"
              },
              "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
                "label" : "Transaction",
                "value" : "-"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "*****67890"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0026"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Refund"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "3043e0b61fad4c5483db3d498309460f"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "12/1/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "10:04:19 PM"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Request a Check Transaction Status {#semi-integrated-pax-pymnt-svcs-txn-status-api-intro}
=========================================================================================

Use this information to request a check transaction status when the app is in Local mode. This transaction is used to obtain response data for a transaction that was lost or timed out.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields to Request a Check Transaction Status {#semi-integrated-pax-pymnt-svcs-txn-status-api-reqfields}
================================================================================================================

type
:
Set the value to `TransactionLookupRequest`.

idType
:
Set the value to `TRANSACTION_ID` or `MERCHANT_REFERENCE_CODE`.

id
:
Set the value to the `id` or merchantReferenceCode field value from the original transaction.

REST Example: Request a Check Transaction Status {#semi-integrated-pax-pymnt-svcs-txn-status-api-ex-rest}
=========================================================================================================

Request

```
{
      "type": "TransactionLookupRequest",
      "idType": "TRANSACTION_ID",
      "id": "1541387b383d456aabb81cdf558b4e8e"
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
      "type" : "TransactionLookupResponse",
      "transactionDetails" : {
        "id" : "1541387b383d456aabb81cdf558b4e8e",
        "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc" : "2023-12-01T20:24:47+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "1.00",
          "refundableAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014622903166318504010"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Cancel Transaction {#semi-integrated-pax-pymnt-svcs-cancel-txn-api-intro}
=========================================================================

Use this information to process a cancel transaction request in Local mode. This request is sent to interrupt an in-process transaction.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** `wss://{terminal IP address:port number}/`  
**Production:** `wss://{terminal IP address:port number}/`

Required Fields to Cancel Transaction {#semi-integrated-pax-pymnt-svcs-cancel-txn-api-reqfields}
================================================================================================

type
:
Set the value to `CancelRequest`.

REST Example: Cancel Transaction {#semi-integrated-pax-pymnt-svcs-cancel-txn-api-ex-rest}
=========================================================================================

Request

```
{
      "type": "CancelRequest"
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment aborted",
      "transactionDetails" : {
        "id" : "b6522aeb9d8d49b386f7c67852581145",
        "merchantReferenceCode" : "50c86aaa02ed4c0bb4b4b596379713f7",
        "submitTimeUtc" : "2023-12-01T20:30:05+0000",
        "captured" : false,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "0.00",
          "refundableAmount" : "0.00"
        }
      },
      "processingDetails" : {
        "status" : "ABORTED",
        "verificationMethod" : "UNKNOWN",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "00",
          "expirationYear" : "00",
          "type" : "UNKNOWN",
          "maskedPan" : ""
        }
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nCanceled transaction.\n\n\nEntry Mode: Contactless\nAID: NULL\n\n\nb6522aeb9d8d49b386f7c67852581145\n21:30:05: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "NULL"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "b6522aeb9d8d49b386f7c67852581145"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:30:05"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Canceled transaction."
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nCanceled transaction.\n\n\nEntry Mode: Contactless\nAID: NULL\n\n\nb6522aeb9d8d49b386f7c67852581145\n21:30:05: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "NULL"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "b6522aeb9d8d49b386f7c67852581145"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:30:05"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Canceled transaction."
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with On-Reader Tipping {#sis-local-sale-on-reader-tip-api-intro}
=====================================================================

Use this information to process a sale with on-reader tipping in Local mode. At the start of each transaction, the terminal prompts the customer to add a tip by showing suggested tip amounts. The customer selects or enters a tip amount on the terminal before presenting their payment card.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale with On-Reader Tipping {#sis-local-sale-on-reader-tip-api-reqfields}
===============================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

askForTip
:
Set the value to `ON_DEVICE`.

REST Example: Sale with On-Reader Tipping {#sis-local-sale-on-reader-tip-api-ex-rest}
=====================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "adf0fa5ca70d462ba5fc0249436b656c",
      "amountDetails" : {
        "amount" : "5.00",
        "currency" : "GBP"
      },
      "askForTip" : "ON_DEVICE"
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "55678c8b152046f7b1d77fd2286ce392",
        "merchantReferenceCode" : "adf0fa5ca70d462ba5fc0249436b656c",
        "submitTimeUtc" : "2023-12-01T21:01:23+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "6.00",
          "capturedAmount" : "6.00",
          "refundableAmount" : "6.00",
          "includedTipAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014644863036208304012"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\nPurchase Amount: £5.00\nTip Amount: £1.00\nTotal Amount: £6.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938252\nMerchant ID: **37599\nTerminal ID: ****0063\n\n55678c8b152046f7b1d77fd2286ce392\n22:01:27: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938252"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "55678c8b152046f7b1d77fd2286ce392"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£6.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "22:01:27"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\nPurchase Amount: £5.00\nTip Amount: £1.00\nTotal Amount: £6.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938252\nMerchant ID: **37599\nTerminal ID: ****0063\n\n55678c8b152046f7b1d77fd2286ce392\n22:01:27: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938252"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "55678c8b152046f7b1d77fd2286ce392"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£6.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "22:01:27"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with On-Receipt Tipping {#sis-pymnt-svcs-sale-on-receipt-tip-intro}
========================================================================

Use this information to process a sale with on-receipt tipping when the app is in Local mode. After the original transaction is pre-authorized, the customer writes the tip or total amount on the printed receipt. A follow-on tip adjust request must be sent within 24 hours to capture the transaction. For more information, see [Tip Adjust](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-pymnt-svcs-sale-on-receipt-tip-intro/sis-pymnt-svcs-tip-adjust-on-receipt-sale-intro.md "").

> WARNING
> By using this feature, you assume the risk of overcaptures being declined and increased chargebacks, so use it only when necessary. Process sales with on-reader tipping, whenever possible. For more information, see [Sale with On-Reader Tipping](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-local-sale-on-reader-tip-api-intro.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale with On-Receipt Tipping {#sis-pymnt-svcs-sale-on-receipt-tip-api-reqfields}
======================================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

capture
:
Set the value to `false`.

askForTip
:
Set the value to `ON_RECEIPT`.

REST Example: Sale with On-Receipt Tipping {#sis-pymnt-svcs-sale-on-receipt-tip-api-ex-rest}
============================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "1ce594be142142f4913cca805830a176",
      "amountDetails" : {
        "amount" : "20.00",
        "currency" : "USD"
      },
      "capture" : false,
      "askForTip" : "ON_RECEIPT"
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
  "type" : "PaymentResponse",
  "message" : "Payment approved",
  "transactionDetails" : {
    "id" : "c6174c80b81f4413a4b9f2065c5431c7",
    "merchantReferenceCode" : "1ce594be142142f4913cca805830a176",
    "submitTimeUtc" : "2024-03-20T09:19:41+0000",
    "captured" : false,
    "amountDetails" : {
      "currency" : "USD",
      "amount" : "20.00",
      "capturedAmount" : "20.00",
      "refundableAmount" : "20.00"
    }
  },
  "processingDetails" : {
    "status" : "APPROVED",
    "verificationMethod" : "NONE",
    "entryMode" : "NFC_ICC",
    "card" : {
      "expirationMonth" : "12",
      "expirationYear" : "2025",
      "type" : "VISA",
      "maskedPan" : "476173XXXXXX0119",
      "countryCode" : "840"
    }
  },
  "additionalInformation" : {
    "instrumentId" : "7030000000022690119",
    "requestId" : "7109263864326505004007"
  },
  "linkedOperations" : [ ],
  "tipAdjustStatus" : "ADJUSTABLE",
  "receipts" : {
    "merchantReceipt" : {
      "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n1234567\n\nSale\n$20.00\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 002000\nMerchant ID: **37599\nTerminal ID: ****0063\n\n\nc6174c80b81f4413a4b9f2065c5431c7\n\n\n\n10:19:46: 20/03/2024\n\n\n\nTIP:\n___________________\n\nTOTAL:\n___________________\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks VISA"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0119"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000031010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Contactless"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "None"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****0063"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Merchant Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Sale"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "c6174c80b81f4413a4b9f2065c5431c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$20.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "10:19:46"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : true,
        "totalLineRequired" : true
      }
    },
    "customerReceipt" : {
      "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n1234567\n\nSale\n$20.00\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 002000\nMerchant ID: **37599\nTerminal ID: ****0063\n\n\nc6174c80b81f4413a4b9f2065c5431c7\n\n\n\n10:19:46: 20/03/2024\n\n\n\nTIP:\n___________________\n\nTOTAL:\n___________________\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks VISA"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0119"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000031010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Contactless"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "None"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****0063"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Cardholder Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Sale"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "c6174c80b81f4413a4b9f2065c5431c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$20.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "10:19:46"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : true,
        "totalLineRequired" : true
      }
    }
  }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Tip Adjust {#sis-pymnt-svcs-tip-adjust-on-receipt-sale-intro}
=============================================================

Use this information to process a tip adjust when the app is in Local Mode mode. This follow-on transaction is required when processing an on-receipt tipping transaction. The tip adjust request must be sent within 24 hours to capture the transaction.  
After the original transaction is pre-authorized, the customer writes the tip or total amount on the printed receipt. A follow-on tip adjust request is then sent to capture the additional tip amount. This transaction is also referred to as an *overcapture* . For more information, see [Sale with On-Receipt Tipping](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-pymnt-svcs-sale-on-receipt-tip-intro.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Tip Adjust {#sis-pymnt-svcs-tip-adjust-on-receipt-sale-api-reqfields}
===========================================================================================

type
:
Set the value to `TipAdjustRequest`.

transactionId
:
Set the value to the id field value from the original transaction.

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Tip Adjust {#sis-pymnt-svcs-tip-adjust-on-receipt-sale-api-ex-rest}
=================================================================================

Request

```
{
      "type": "TipAdjustRequest",
      "transactionId": "c6174c80b81f4413a4b9f2065c5431c7",
      "amountDetails": {
        "amount": "4.00",
        "currency": "USD"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
  "type" : "TipAdjustResponse",
  "message" : "Payment approved",
  "transactionDetails" : {
    "id" : "c6174c80b81f4413a4b9f2065c5431c7",
    "merchantReferenceCode" : "1ce594be142142f4913cca805830a176",
    "submitTimeUtc" : "2024-03-20T09:19:41+0000",
    "captured" : true,
    "amountDetails" : {
      "currency" : "USD",
      "amount" : "24.00",
      "capturedAmount" : "24.00",
      "refundableAmount" : "24.00",
      "includedTipAmount" : "4.00"
    }
  },
  "processingDetails" : {
    "status" : "APPROVED",
    "verificationMethod" : "NONE",
    "entryMode" : "NFC_ICC",
    "card" : {
      "expirationMonth" : "12",
      "expirationYear" : "2025",
      "type" : "VISA",
      "maskedPan" : "476173XXXXXX0119",
      "countryCode" : "840"
    }
  },
  "additionalInformation" : {
    "instrumentId" : "7030000000022690119",
    "requestId" : "7109265975966653104007"
  },
  "linkedOperations" : [ ],
  "tipAdjustStatus" : "ADJUSTED",
  "receipts" : {
    "merchantReceipt" : {
      "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n1234567\n\nCapture\nPurchase Amount: $20.00\nTip Amount: $4.00\nTotal Amount: $24.00\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 002000\nMerchant ID: **37599\nTerminal ID: ****7478\n\n\nc6174c80b81f4413a4b9f2065c5431c7\n\n10:23:17: 20/03/2024\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks VISA"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0119"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000031010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Contactless"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "None"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****7478"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Merchant Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Capture"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "c6174c80b81f4413a4b9f2065c5431c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$24.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "10:23:17"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    },
    "customerReceipt" : {
      "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n1234567\n\nCapture\nPurchase Amount: $20.00\nTip Amount: $4.00\nTotal Amount: $24.00\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 002000\nMerchant ID: **37599\nTerminal ID: ****7478\n\n\nc6174c80b81f4413a4b9f2065c5431c7\n\n10:23:17: 20/03/2024\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks VISA"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0119"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000031010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Contactless"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "None"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****7478"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Cardholder Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Capture"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "c6174c80b81f4413a4b9f2065c5431c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$24.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "10:23:17"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    }
  }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Token Refund {#semi-integrated-pax-pymnt-svcs-token-refund-api-intro}
=====================================================================

Use this information to process a token refund when the app is in Local mode. A token refund transaction enables you to process a stand-alone credit against a tokenized card. To process a credit through a token, you must have the `Token Management Service` product enabled and an existing (saved) token from a tokenized transaction. For more information, see [Token Management Service](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/ctv/rest/tms/tms-overview.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Token Refund {#semi-integrated-pax-pymnt-svcs-token-refund-api-reqfields}
===============================================================================================

type
:
Set the value to `TokenRefundRequest`.

instrumentId
:
Set the value to the Instrument Identifier token.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Token Refund {#semi-integrated-pax-pymnt-svcs-token-refund-api-ex-rest}
=====================================================================================

Request

```
{
      "type": "TokenRefundRequest",
      "instrumentId": "7030000000022690119",
      "merchantReferenceCode": "30ed45dc7b3f4fb9905413940ac30363",
      "amountDetails": {
        "amount": "1.00",
        "currency": "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
      "type" : "TokenRefundResponse",
      "message" : "Refund approved",
      "transactionDetails" : {
        "id" : "596b797178fe45e39ce3a8b8fdf432d6",
        "merchantReferenceCode" : "30ed45dc7b3f4fb9905413940ac30363",
        "submitTimeUtc" : "2023-12-01T21:02:50+0000",
        "amountDetails" : {
          "amount" : "1.00",
          "currency" : "GBP"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "MANUAL",
        "card" : {
          "expirationMonth" : "00",
          "expirationYear" : "00",
          "type" : "VISA",
          "maskedPan" : "703000XXXXXXXXX0119"
        }
      },
      "additionalInformation" : {
        "requestId" : "7014645711206245404009"
      },
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nRefund\n-£1.00\n\n\nPlease retain receipt!\n\n\nCard: VISA\nAccount: *** **** **** **** 0119\nEntry Mode: Keyed\n\nTransaction: -\nAuthorization: -\nMerchant ID: **37599\nTerminal ID: *************L_ID\n\n596b797178fe45e39ce3a8b8fdf432d6\n10:02:50 PM: 12/1/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "*** **** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
                "label" : "Transaction",
                "value" : "-"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "*************L_ID"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Refund"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "596b797178fe45e39ce3a8b8fdf432d6"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "12/1/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "10:02:50 PM"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nRefund\n-£1.00\n\n\nPlease retain receipt!\n\n\nCard: VISA\nAccount: *** **** **** **** 0119\nEntry Mode: Keyed\n\nTransaction: -\nAuthorization: -\nMerchant ID: **37599\nTerminal ID: *************L_ID\n\n596b797178fe45e39ce3a8b8fdf432d6\n10:02:50 PM: 12/1/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "*** **** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
                "label" : "Transaction",
                "value" : "-"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "*************L_ID"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Refund"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "596b797178fe45e39ce3a8b8fdf432d6"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "12/1/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "10:02:50 PM"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Pre-Authorization {#semi-integrated-pax-pymnt-svcs-pre-auth-api-intro}
======================================================================

Use this information to process a pre-authorization for an initial amount in Local mode. A pre-authorization transaction places a temporary hold on the customer's payment card. The transaction amount can be captured at a later time.  
Most authorizations expire in 5 to 7 days. The issuing bank sets the length of time before expiration. When an authorization expires with the issuing bank, your bank or processor might require you to re-submit an authorization request and include a request for capture in the same message. For more information, see [Capture](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/semi-integrated-pax-pymnt-svcs-capture-api-intro.md "").

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Pre-Authorization {#semi-integrated-pax-pymnt-svcs-pre-auth-api-reqfields}
================================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

capture
:
Set the value to `false`.

REST Example: Pre-Authorization {#semi-integrated-pax-pymnt-svcs-pre-auth-api-ex-rest}
======================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "47bd9ed54f3f4bfabb9d3ee94cfa3008",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "GBP"
      },
      "capture" : false
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "e43069fbf85543659e478edd8d50f244",
        "merchantReferenceCode" : "47bd9ed54f3f4bfabb9d3ee94cfa3008",
        "submitTimeUtc" : "2023-12-01T20:38:14+0000",
        "captured" : false,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "0.00",
          "refundableAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014630972006630604008"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nAuth only\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938242\nMerchant ID: **37599\nTerminal ID: ****0063\n\ne43069fbf85543659e478edd8d50f244\n21:38:18: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938242"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Auth only"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "e43069fbf85543659e478edd8d50f244"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:38:18"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nAuth only\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938242\nMerchant ID: **37599\nTerminal ID: ****0063\n\ne43069fbf85543659e478edd8d50f244\n21:38:18: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938242"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Auth only"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "e43069fbf85543659e478edd8d50f244"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:38:18"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Incremental Authorization {#semi-integrated-pax-pymnt-svcs-increm-auth-api-intro}
=================================================================================

Use this information to process an incremental authorization in Local mode. This type of request can be made on a pre-authorization transaction to increase the authorized amount before it is captured.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for an Incremental Authorization {#semi-integrated-pax-pymnt-svcs-increm-auth-api-reqfields}
============================================================================================================

type
:
Set the value to `IncrementalAuthorizationRequest`.

transactionId
:
Set the value to the `id` field value from the original transaction.

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Incremental Authorization {#semi-integrated-pax-pymnt-svcs-increm-auth-api-ex-rest}
=================================================================================================

Request

```
{
      "type": "IncrementalAuthorizationRequest",
      "transactionId": "e43069fbf85543659e478edd8d50f244",
      "amountDetails": {
        "amount": "2.00",
        "currency": "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
      "type" : "IncrementalAuthorizationResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "6da4aff381e8483ebc65ebf4fbb27ec8",
        "merchantReferenceCode" : "47bd9ed54f3f4bfabb9d3ee94cfa3008",
        "submitTimeUtc" : "2023-12-01T20:39:43+0000",
        "captured" : false,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "2.00",
          "capturedAmount" : "0.00",
          "refundableAmount" : "0.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "MANUAL",
        "card" : {
          "expirationMonth" : "00",
          "expirationYear" : "00",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119"
        }
      },
      "additionalInformation" : {
        "requestId" : "7014631843806649604009"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nTop-up\n£2.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Keyed\nVerification: None\n\nAuthorization: 938243\nMerchant ID: **37599\nTerminal ID: ****0063\n\n6da4aff381e8483ebc65ebf4fbb27ec8\n21:39:45: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938243"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Top-up"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "6da4aff381e8483ebc65ebf4fbb27ec8"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£2.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:39:45"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nTop-up\n£2.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Keyed\nVerification: None\n\nAuthorization: 938243\nMerchant ID: **37599\nTerminal ID: ****0063\n\n6da4aff381e8483ebc65ebf4fbb27ec8\n21:39:45: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938243"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Top-up"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "6da4aff381e8483ebc65ebf4fbb27ec8"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£2.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:39:45"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Capture {#semi-integrated-pax-pymnt-svcs-capture-api-intro}
===========================================================

Use this information to capture a pre-authorized transaction in Local mode. The capture request references the approved pre-authorization request.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Capture {#semi-integrated-pax-pymnt-svcs-capture-api-reqfields}
=====================================================================================

type
:
Set the value to `CaptureRequest`.

transactionId
:
Set the value to the `id` field value from the original transaction.

Optional Fields for a Capture {#sis-pymnt-svcs-capture-api-optfields}
=====================================================================

Use the optional amount and currency fields to process a partial capture. Otherwise, the full amount will be captured.

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Capture {#semi-integrated-pax-pymnt-svcs-capture-api-ex-rest}
===========================================================================

Request

```
{
      "type": "CaptureRequest",
      "transactionId": "cb6475bafbb94d03b0f984629c63c294",
      "amountDetails": {
        "amount": "3.00",
        "currency": "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
      "type" : "CaptureResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "cb6475bafbb94d03b0f984629c63c294",
        "merchantReferenceCode" : "dd02499055544be18ba7fa0397909d65",
        "submitTimeUtc" : "2023-12-01T20:43:03+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "3.00",
          "capturedAmount" : "3.00",
          "refundableAmount" : "3.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014633860196734504012"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£3.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938244\nMerchant ID: **37599\nTerminal ID: ****0063\n\ncb6475bafbb94d03b0f984629c63c294\n21:43:07: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938244"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "cb6475bafbb94d03b0f984629c63c294"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£3.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:43:07"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£3.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938244\nMerchant ID: **37599\nTerminal ID: ****0063\n\ncb6475bafbb94d03b0f984629c63c294\n21:43:07: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938244"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "cb6475bafbb94d03b0f984629c63c294"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£3.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:43:07"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Mail Order or Telephone Order {#sis-local-moto-trxns-intro}
===========================================================

Use this information to process a mail order or telephone order (MOTO) sale and other transactions in Local mode. The payment card is not presented physically at the terminal for a MOTO transaction because it is a card-not-present transaction.  
You can also process these MOTO transactions in Local mode:

Account Verification
:
A MOTO account verification request submits a zero-amount authorization request to validate the payment card.

Pre-authorization
:
A MOTO pre-authorization request places a temporary hold on the customer's payment card, enabling the transaction to be captured at a later time. Most authorizations expire within 5 to 7 days. However, the exact duration is determined by the issuing bank.

    When an authorization expires, your bank, the payment processor, or issuing bank might require you to re-submit the authorization request. In such cases, you might be required to include the capture instructions in the same message to ensure successful processing.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for Mail Order or Telephone Order {#sis-local-moto-trxns-reqfields}
===================================================================================

type
:
Set the value to `PaymentRequest` for a sale or to `AccountVerificationRequest` for an account verification.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

paymentMode
:
Set the value to `MOTO`.

Optional Fields for Mail Order or Telephone Order {#sis-local-moto-trxns-optfields}
===================================================================================

capture
:
Set the value to `false` for a pre-authorization.

REST Example: Mail Order or Telephone Order Sale {#sis-local-moto-trxns-sale-ex-rest}
=====================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "a7fbcdc92425456fa0db29c8670a3150",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "GBP"
      },
      "paymentMode": "MOTO"
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "4348c35f258c4f8d8c89b9898e3f1b63",
        "merchantReferenceCode" : "a7fbcdc92425456fa0db29c8670a3150",
        "submitTimeUtc" : "2023-12-01T20:51:09+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "1.00",
          "refundableAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "MANUAL",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "411111******1111"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7038380000019631111",
        "requestId" : "7014638853776978504011"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nCVV MATCH ONLY\n\n\nCard: VISA\nAccount: **** **** **** 1111\nEntry Mode: Keyed\nVerification: Cardholder Not Present\n\nAuthorization: 938246\nMerchant ID: **37599\nTerminal ID: ****0063\n\n4348c35f258c4f8d8c89b9898e3f1b63\n21:51:27: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 1111"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "Cardholder Not Present"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938246"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "4348c35f258c4f8d8c89b9898e3f1b63"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:51:27"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "CVV MATCH ONLY"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: VISA\nAccount: **** **** **** 1111\nEntry Mode: Keyed\nVerification: Cardholder Not Present\n\nAuthorization: 938246\nMerchant ID: **37599\nTerminal ID: ****0063\n\n4348c35f258c4f8d8c89b9898e3f1b63\n21:51:27: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 1111"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "Cardholder Not Present"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938246"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "4348c35f258c4f8d8c89b9898e3f1b63"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:51:27"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Account Verification {#sis-local-acct-verif-api-intro}
======================================================

Use this information to process an account verification when the app is in Local mode. The account verification transaction submits a zero-amount authorization request to validate the payment card.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** `wss://{terminal IP address:port number}/`  
**Production:** `wss://{terminal IP address:port number}/`

Required Fields for an Account Verification {#sis-local-acct-verif-api-reqfields}
=================================================================================

type
:
Set the value to `AccountVerificationRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.currency
:
Set the value to the currency code.

REST Example: Account Verification {#sis-local-acct-verif-api-ex-rest}
======================================================================

Request

```
{
      "type": "AccountVerificationRequest",
      "merchantReferenceCode": "ec119c3b377542b09132867d236dc834",
      "amountDetails": {
        "currency": "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
 {
      "type" : "AccountVerificationResponse",
      "message" : "Verification successful",
      "transactionDetails" : {
        "id" : "2dd6beb00d8d4bb8bf1a4718917a3003",
        "merchantReferenceCode" : "ec119c3b377542b09132867d236dc834",
        "submitTimeUtc" : "2023-12-01T20:27:02+0000",
        "amountDetails" : {
          "currency" : "GBP"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014624258386432804007"
      },
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nAccount Verification\n£0.00\n\n\nAccount Valid.\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938239\nMerchant ID: **37599\nTerminal ID: ****0063\n\n2dd6beb00d8d4bb8bf1a4718917a3003\n21:27:07: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938239"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Account Verification"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "2dd6beb00d8d4bb8bf1a4718917a3003"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£0.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:27:07"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Account Valid."
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nAccount Verification\n£0.00\n\n\nAccount Valid.\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938239\nMerchant ID: **37599\nTerminal ID: ****0063\n\n2dd6beb00d8d4bb8bf1a4718917a3003\n21:27:07: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938239"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Account Verification"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "2dd6beb00d8d4bb8bf1a4718917a3003"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£0.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:27:07"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Account Valid."
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Offline Transactions {#sis-pymnt-svcs-offline-txn-intro}
========================================================

Offline mode is an optional feature that you can use to process offline sale and refund transactions when an internet connection is not available. The device must be operating in Local mode to enable or disable this feature. The default setting is `Disabled`.  
You can enable or disable Offline mode in the Acceptance Devices app, through a REST API request, or in the `Business Center`, where you can also customize settings. For more information, see [Customizing the Acceptance Devices App](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/sis-ad-app-customize-intro.md "").

> WARNING
> By using this feature, you assume the risk of failed transactions and the possibility of increased fraud and chargebacks. Process transactions offline only when required, such as during an internet outage. Whenever possible, process transactions online instead. For more information, see [Sale](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/semi-integrated-pax-pymnt-svcs-sale-api-intro.md "").  
> When an internet connect is available, you must submit the offline transactions batch for authorization while the app is in Offline mode. For more information, see [Submit an Offline Transactions Batch for Authorization](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro/sis-pymnt-svcs-offline-txn-intro/sis-pymnt-svcs-offline-txn-batch-auth.md "").

Enable or Disable Offline Mode in the Acceptance Device App {#sis-pymnt-svcs-offline-txn-ad-app}
================================================================================================

IMPORTANT The recommendation is to resume operating in online mode as soon as an internet connection is available. To do so, you must first disable Offline mode.  
Follow these steps to enable or disable Offline mode in the Acceptance Device App:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Offline Mode.
4. Toggle Enable Offline Mode to ON or OFF.
5. Tap the back navigation arrow to return to the home screen.

Enable or Disable Offline Mode Using a REST API Request {#sis-pymnt-svcs-offline-txn-api-intro}
===============================================================================================

Use this information to enable or disable Offline mode in your POS system by using a REST API request.  
When Offline mode is disabled, the offline transactions batch is automatically submitted for authorization. Make sure that an internet connection is available before disabling Offline mode.

> IMPORTANT The recommendation is to resume operating in online mode as soon as an internet connection is available. To do so, you must first disable Offline mode.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields to Enable or Disable Offline Mode Using a REST API Request {#sis-pymnt-svcs-offline-txn-api-reqfields}
======================================================================================================================

type
:
Set the value to `OfflineModeRequest`.

enabled
:
Set the value to `true` to enable Offline mode or to `false` to disable Offline mode.

REST Example: Enable or Disable Offline Mode Using a REST API Request {#sis-pymnt-svcs-offline-txn-apii-ex-rest}
================================================================================================================

Request

```
{
  "type": "OfflineModeRequest",
  "enabled": true
}
```

Mid-Transaction Status Updates  
During the operation, you might receive one or more update responses indicating the current status of the operation. You can choose to display these updates on your point-of-sale (POS) system.

```
{
  "type": "OperationStatusResponse",
  "message": "Status update to display."
}
```

Response to a Successful Request

```
{
  "type": "OfflineModeResponse",
  "message": "Offline mode enabled."
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
    "type": "ErrorResponse",
    "message": "Error message to display.",
    "developerDescription": "Detailed description of error."
}
```

Offline Sale {#sis-pymnt-svcs-offline-txn-sale-intro}
=====================================================

Use this information to process an offline sale when the app is in Local mode and Offline mode is enabled to process transactions. This type of transaction combines an authorization and a capture into a single transaction.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for an Offline Sale {#sis-pymnt-svcs-offline-txn-sale-api-reqfields}
====================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

REST Example: Offline Sale {#sis-pymnt-svcs-offline-txn-sale-api-ex-rest}
=========================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "GBP"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment accepted",
      "transactionDetails" : {
        "id" : "1541387b383d456aabb81cdf558b4e8e",
        "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc" : "2023-12-01T20:24:47+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "1.00",
          "refundableAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "ACCEPTED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014622903166318504010"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Offline Refund {#sis-pymnt-svcs-offline-txn-refund}
===================================================

Follow these steps to process an offline refund when the app is in Local mode and Offline mode is enabled to process transactions.

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Offline Mode.
4. Tap the transaction you want to refund.
5. Tap Refund.
6. Enter the transaction amount.
7. Tap Refund to start the transaction.

Submit an Offline Transactions Batch for Authorization {#sis-pymnt-svcs-offline-txn-batch-auth}
===============================================================================================

IMPORTANT The recommendation is to submit the batch for authorization as soon as an internet connection is available. To submit a batch, Offline mode must be enabled.  
Follow these steps to submit an offline transactions batch for authorization when Offline mode is enabled.

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Offline Mode.
4. Tap Submit Offline Batch.

Cashback {#semi-integrated-pymnt-svcs-cashback-intro}
=====================================================

Use this information to process a cashback transaction when the app is in Local mode. This type of transaction enables customers to request that a specified amount of cash to be given to them as part of the transaction. A cashback transaction can be processed with or without a purchase.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Cashback {#semi-integrated-pymnt-svcs-cashback-api-reqfields}
===================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

amountDetails.cashbackAmount
:
Set the value to the cashback amount.

REST Example: Cashback {#semi-integrated-pymnt-svcs-cashback-api-ex-rest}
=========================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "bd74d30930e349548fd9d125f88291bc",
      "amountDetails" : {
        "amount" : "20.00",
        "currency" : "GBP",
        "cashbackAmount" : "5.00"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
  "type" : "PaymentResponse",
  "message" : "Payment approved",
  "transactionDetails" : {
    "id" : "218b28d38bf3424ab4ade95b9be1c75b",
    "merchantReferenceCode" : "bd74d30930e349548fd9d125f88291bc",
    "submitTimeUtc" : "2024-03-20T08:55:37+0000",
    "captured" : true,
    "amountDetails" : {
      "currency" : "GBP",
      "amount" : "20.00",
      "capturedAmount" : "25.00",
      "refundableAmount" : "20.00",
      "cashbackAmount" : "5.00"
    }
  },
  "processingDetails" : {
    "status" : "APPROVED",
    "verificationMethod" : "PIN",
    "entryMode" : "ICC",
    "card" : {
      "expirationMonth" : "12",
      "expirationYear" : "2025",
      "type" : "MASTERCARD",
      "maskedPan" : "541333XXXXXX0011",
      "countryCode" : "276"
    }
  },
  "additionalInformation" : {
    "instrumentId" : "7030000000232230011",
    "requestId" : "7109249459396751504008"
  },
  "linkedOperations" : [ ],
  "tipAdjustStatus" : "NOT_ADJUSTABLE",
  "receipts" : {
    "merchantReceipt" : {
      "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nCashback\n£25.00\nPurchase Amount: £20.00\nCashback: £5.00\nPlease retain receipt!\n\nCard: Payworks MASTER\nAccount: **** **** **** 0011\nEntry Mode: Chip\nAID: A0000000041010\nCard Number: 0\nVerification: PIN\n\nAuthorization: 002500\nMerchant ID: **37599\nTerminal ID: ****0063\n\n\n218b28d38bf3424ab4ade95b9be1c75b\n\n09:55:46: 20/03/2024\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "UB3 2EA"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "London"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United Kingdom"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks MASTER"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0011"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000041010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Chip"
          },
          "PAYMENT_DETAILS_ACCOUNT_SEQUENCE_NUMBER" : {
            "label" : "Card Number",
            "value" : "0"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "PIN"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002500"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****0063"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Merchant Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Cashback"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "218b28d38bf3424ab4ade95b9be1c75b"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "09:55:46"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    },
    "customerReceipt" : {
      "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nCashback\n£25.00\nPurchase Amount: £20.00\nCashback: £5.00\nPlease retain receipt!\n\nCard: Payworks MASTER\nAccount: **** **** **** 0011\nEntry Mode: Chip\nAID: A0000000041010\nCard Number: 0\nVerification: PIN\n\nAuthorization: 002500\nMerchant ID: **37599\nTerminal ID: ****0063\n\n\n218b28d38bf3424ab4ade95b9be1c75b\n\n09:55:46: 20/03/2024\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "UB3 2EA"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "London"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United Kingdom"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks MASTER"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0011"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000041010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Chip"
          },
          "PAYMENT_DETAILS_ACCOUNT_SEQUENCE_NUMBER" : {
            "label" : "Card Number",
            "value" : "0"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "PIN"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002500"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****0063"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Cardholder Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Cashback"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "218b28d38bf3424ab4ade95b9be1c75b"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "09:55:46"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    }
  }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with Installment Details {#sis-pymnt-svcs-semi-sale-installment-details-intro}
===================================================================================

Use this information to process a sale transaction with installment details when the app is in Local mode. This type of transaction can be used to include the required installment details as part of the sale transaction.  
This transaction is available only in the Latin American and Caribbean (LAC) region.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale with Installment Details {#sis-pymnt-svcs-semi-sale-installment-details-reqfields}
=============================================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Installment Details {#sis-pymnt-svcs-semi-sale-installment-details-optfields}
=============================================================================================================

Use one or more of the optional installmentDetails fields to provide additional installment details.

installmentDetails.numberOfInstallments
:
Set the value to the number of installments.

installmentDetails.planType
:
Set the value to `MERCHANT_FUNDED` or `ISSUER_FUNDED`.

installmentDetails.interestPlan
:
Set the value to `true` or `false`.

installmentDetails.governmentPlan
:
Set the value to `true` or `false`.

REST Example: Sale with Installment Details {#sis-pymnt-svcs-semi-sale-installment-details-ex-rest}
===================================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
      "amountDetails" : {
        "amount" : "20.00",
        "currency" : "USD"
      },
      "installmentDetails": {
        "numberOfInstallments": 5,
        "planType": "MERCHANT_FUNDED",
        "interestPlan": true,
        "governmentPlan": true
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
    "type": "PaymentResponse",
    "message": "Payment approved",
    "transactionDetails": {
        "id": "8ccb150a88bd4c6f9a00a687f39ca97d",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc": "2024-09-20T08:15:12+0000",
        "captured": true,
        "amountDetails": {
            "amount": "20.00",
            "currency": "USD",
            "capturedAmount": "20.00",
            "refundableAmount": "20.00"
        }
    },
    "processingDetails": {
        "status": "APPROVED",
        "verificationMethod": "NONE",
        "entryMode": "NFC_ICC",
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2025",
            "type": "VISA",
            "maskedPan": "476173XXXXXX0119",
            "countryCode": "840"
        }
    },
    "additionalInformation": {
        "requestId": "7268201146336069504011"
    },
    "linkedOperations": [],
    "receipts": {
        "merchantReceipt": {
            "preformattedReceipt": "Merchant Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$20.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 546712\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n8ccb150a88bd4c6f9a00a687f39ca97d\n\n4:15:12 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "546712"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Merchant Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "8ccb150a88bd4c6f9a00a687f39ca97d"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$20.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "4:15:12 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        },
        "customerReceipt": {
            "preformattedReceipt": "Cardholder Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$20.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 546712\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n8ccb150a88bd4c6f9a00a687f39ca97d\n\n4:15:12 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "546712"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Cardholder Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "8ccb150a88bd4c6f9a00a687f39ca97d"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$20.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "4:15:12 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        }
    },
    "installmentDetails": {
        "numberOfInstallments": 5,
        "planType": "MERCHANT_FUNDED",
        "interestPlan": true,
        "governmentPlan": true
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with Payment Facilitator Details {#sis-pymnt-svcs-semi-sale-pymnt-facil-details-intro}
===========================================================================================

Use this information to process a sale transaction with payment facilitator details when the app is in Local mode. This type of transaction can be used to include the required payment facilitator details as part of the sale transaction.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale with Payment Facilitator Details {#sis-pymnt-svcs-semi-sale-pymnt-facil-details-reqfields}
=====================================================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Payment Facilitator Details {#sis-pymnt-svcs-semi-sale-pymnt-facil-details-optfields}
=====================================================================================================================

Use one or more of the optional merchantDetails fields to provide additional payment facilitator details.

merchantDetails.salesOrganizationId
:
Set the value to the sales organization identifier.

merchantDetails.subMerchantId
:
Set the value to the sub-merchant identifier.

merchantDetails.descriptorName
:
Set the value to the descriptor name.

REST Example: Sale with Payment Facilitator Details {#sis-pymnt-svcs-semi-sale-pymnt-facil-details-ex-rest}
===========================================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "USD"
      },
      "merchantDetails": {
        "salesOrganizationId": "12345",
        "subMerchantId": "SM67890",
        "descriptorName": "ExampleMerchant"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
    "type": "PaymentResponse",
    "message": "Payment approved",
    "transactionDetails": {
        "id": "940d49ee94444764acb1c898e2254954",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc": "2024-09-20T07:53:36+0000",
        "captured": true,
        "amountDetails": {
            "amount": "1.00",
            "currency": "USD",
            "capturedAmount": "1.00",
            "refundableAmount": "1.00"
        }
    },
    "processingDetails": {
        "status": "APPROVED",
        "verificationMethod": "NONE",
        "entryMode": "NFC_ICC",
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2025",
            "type": "VISA",
            "maskedPan": "476173XXXXXX0119",
            "countryCode": "840"
        }
    },
    "additionalInformation": {
        "requestId": "7268188188226629104009"
    },
    "linkedOperations": [],
    "receipts": {
        "merchantReceipt": {
            "preformattedReceipt": "Merchant Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$1.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 545814\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n940d49ee94444764acb1c898e2254954\n\n3:53:36 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "545814"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Merchant Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "940d49ee94444764acb1c898e2254954"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$1.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "3:53:36 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        },
        "customerReceipt": {
            "preformattedReceipt": "Cardholder Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$1.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 545814\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n940d49ee94444764acb1c898e2254954\n\n3:53:36 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "545814"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Cardholder Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "940d49ee94444764acb1c898e2254954"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$1.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "3:53:36 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        }
    },
    "merchantDetails": {
        "salesOrganizationId": "12345",
        "subMerchantId": "SM67890",
        "descriptorName": "ExampleMerchant"
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with Tax Details {#sis-pymnt-svcs-semi-sale-tax-details-intro}
===================================================================

Use this information to process a sale transaction with tax details when the app is in Local mode. This type of transaction can be used to include the required tax details as part of the sale transaction.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale with Tax Details {#sis-pymnt-svcs-semi-sale-tax-details-reqfields}
=============================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Tax Details {#sis-pymnt-svcs-semi-sale-tax-details-optfields}
=============================================================================================

Use one or more of the optional taxDetails fields to provide additional tax details.

taxDetails.taxId
:
Set the value to the merchant tax identifier.

taxDetails.salesSlipNumber
:
Set the value to the sales slip number.

taxDetails.includedTaxAmount
:
Set the value to the tax amount.

taxDetails.includedLocalTaxAmount
:
Set the value to the local tax amount.

taxDetails.includedNationalTaxAmount
:
Set the value to the national tax amount.

REST Example: Sale with Tax Details {#sis-pymnt-svcs-semi-sale-tax-details-ex-rest}
===================================================================================

Request

```
{
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
      "amountDetails" : {
        "amount" : "20.00",
        "currency" : "USD"
      },
      "taxDetails": {
        "taxId": "TaxID1234",
        "salesSlipNumber": 12345678,
        "includedTaxAmount": "5.00",
        "includedLocalTaxAmount": "1.00",
        "includedNationalTaxAmount": "2.00"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
    "type": "PaymentResponse",
    "message": "Payment approved",
    "transactionDetails": {
        "id": "4bebd72cf0ff4a9ea212baca0c6d9faf",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc": "2024-09-20T07:15:25+0000",
        "captured": true,
        "amountDetails": {
            "amount": "20.00",
            "currency": "USD",
            "capturedAmount": "20.00",
            "refundableAmount": "20.00"
        }
    },
    "processingDetails": {
        "status": "APPROVED",
        "verificationMethod": "NONE",
        "entryMode": "NFC_ICC",
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2025",
            "type": "VISA",
            "maskedPan": "476173XXXXXX0119",
            "countryCode": "840"
        }
    },
    "additionalInformation": {
        "requestId": "7268165283576248404007"
    },
    "linkedOperations": [],
    "receipts": {
        "merchantReceipt": {
            "preformattedReceipt": "Merchant Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$20.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 129702\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n4bebd72cf0ff4a9ea212baca0c6d9faf\n\n3:15:25 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "129702"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Merchant Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "4bebd72cf0ff4a9ea212baca0c6d9faf"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$20.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "3:15:25 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        },
        "customerReceipt": {
            "preformattedReceipt": "Cardholder Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$20.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 129702\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n4bebd72cf0ff4a9ea212baca0c6d9faf\n\n3:15:25 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "129702"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Cardholder Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "4bebd72cf0ff4a9ea212baca0c6d9faf"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$20.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "3:15:25 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        }
    },
    "taxDetails": {
        "taxId": "TaxID1234",
        "salesSlipNumber": 12345678,
        "includedTaxAmount": "5.00",
        "includedLocalTaxAmount": "1.00",
        "includedNationalTaxAmount": "2.00"
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with Lodging Details {#sis-pymnt-svcs-semi-sale-lodging-intro}
===================================================================

Use this information to process a sale transaction with lodging details in Local mode. This transaction includes required lodging details as part of the sale transaction.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for a Sale with Lodging Details {#sis-pymnt-svcs-semi-sale-lodging-reqfields}
=============================================================================================

type
:
Set the value to `PaymentRequest`.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Lodging Details {#sis-pymnt-svcs-semi-sale-lodging-optfields}
=============================================================================================

Use one or more of the optional fields to include additional details in the transaction.

lodgingDetails.duration
:
Set this field to the number of nights of the lodging stay.

lodgingDetails.checkInDate
:
Set this field to the check-in date in MMDDYY format.

lodgingDetails.checkOutDate
:
Set this field to the check-out date in MMDDYY format.

lodgingDetails.guestSmokingPreference
:
Set this field to Y or N to indicate the guest's smoking preference.

lodgingDetails.numberOfGuests
:
Set this field to the number of guests.

lodgingDetails.numberOfRoomsBooked
:
Set this field to the number of rooms booked.

lodgingDetails.guestName
:
Set this field to the name of the guest.

lodgingDetails.roomLocation
:
Set this field to the room location description.

lodgingDetails.roomTaxElements
:
Set this field to the applicable room tax elements.

lodgingDetails.roomBedType
:
Set this field to the type of bed in the room.

lodgingDetails.roomRateType
:
Set this field to the room rate type.

lodgingDetails.specialProgramCode
:
Set this field to the special program code.

lodgingDetails.dailyRoomRate1
:
Set this field to the daily room rate for the first rate tier.

lodgingDetails.dailyRoomRate2
:
Set this field to the daily room rate for the second rate tier.

lodgingDetails.dailyRoomRate3
:
Set this field to the daily room rate for the third rate tier.

lodgingDetails.roomNights1
:
Set this field to the number of nights at the first rate tier.

lodgingDetails.roomNights2
:
Set this field to the number of nights at the second rate tier.

lodgingDetails.roomNights3
:
Set this field to the number of nights at the third rate tier.

lodgingDetails.corporateClientCode
:
Set this field to the corporate client code.

lodgingDetails.promotionalCode
:
Set this field to the promotional code.

lodgingDetails.additionalCoupon
:
Set this field to an additional coupon code.

lodgingDetails.travelAgencyCode
:
Set this field to the travel agency code.

lodgingDetails.travelAgencyName
:
Set this field to the name of the travel agency.

lodgingDetails.customerServicePhoneNumber
:
Set this field to the customer service phone number.

lodgingDetails.tax
:
Set this field to the total tax amount.

lodgingDetails.prepaidCost
:
Set this field to the prepaid cost amount.

lodgingDetails.foodAndBeverageCost
:
Set this field to the food and beverage cost.

lodgingDetails.roomTax
:
Set this field to the room tax amount.

lodgingDetails.adjustmentAmount
:
Set this field to the adjustment amount.

lodgingDetails.phoneCost
:
Set this field to the phone cost.

lodgingDetails.restaurantCost
:
Set this field to the restaurant cost.

lodgingDetails.roomServiceCost
:
Set this field to the room service cost.

lodgingDetails.miniBarCost
:
Set this field to the mini bar cost.

lodgingDetails.laundryCost
:
Set this field to the laundry cost.

lodgingDetails.miscellaneousCost
:
Set this field to the miscellaneous cost.

lodgingDetails.giftShopCost
:
Set this field to the gift shop cost.

lodgingDetails.movieCost
:
Set this field to the movie cost.

lodgingDetails.healthClubCost
:
Set this field to the health club cost.

lodgingDetails.valetParkingCost
:
Set this field to the valet parking cost.

lodgingDetails.cashDisbursementCost
:
Set this field to the cash disbursement cost.

lodgingDetails.nonRoomCost
:
Set this field to the non-room cost.

lodgingDetails.businessCenterCost
:
Set this field to the business center cost.

lodgingDetails.loungeBarCost
:
Set this field to the lounge or bar cost.

lodgingDetails.transportationCost
:
Set this field to the transportation cost.

lodgingDetails.gratuityCost
:
Set this field to the gratuity cost.

lodgingDetails.conferenceRoomCost
:
Set this field to the conference room cost.

lodgingDetails.audioVisualCost
:
Set this field to the audio/visual equipment cost.

lodgingDetails.banquetCost
:
Set this field to the banquet cost.

lodgingDetails.internetAccessCost
:
Set this field to the internet access cost.

lodgingDetails.earlyCheckOutCost
:
Set this field to the early check-out cost.

lodgingDetails.nonRoomTax
:
Set this field to the non-room tax amount.

REST Example: Sale with Lodging Details {#sis-pymnt-svcs-semi-sale-lodging-ex-rest}
===================================================================================

Request

```
{
      "type": "PaymentRequest",
      "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
      "amountDetails": {
        "amount": "500.00",
        "currency": "USD"
      },
      "lodgingDetails": {
        "duration": 3,
        "checkInDate": "030125",
        "checkOutDate": "030425",
        "guestSmokingPreference": "N",
        "numberOfGuests": 2,
        "numberOfRoomsBooked": 1,
        "guestName": "John Doe",
        "roomLocation": "Ocean View",
        "roomTaxElements": "VAT",
        "roomBedType": "KING",
        "roomRateType": "CORPORATE",
        "specialProgramCode": "1",
        "dailyRoomRate1": "150.00",
        "dailyRoomRate2": "160.00",
        "dailyRoomRate3": "170.00",
        "roomNights1": 1,
        "roomNights2": 1,
        "roomNights3": 1,
        "corporateClientCode": "CORP123456",
        "promotionalCode": "PROMO2025",
        "additionalCoupon": "DISCOUNT10",
        "travelAgencyCode": "TA789",
        "travelAgencyName": "Premium Travel Agency",
        "customerServicePhoneNumber": "1-800-555-0199",
        "tax": "45.00",
        "prepaidCost": "200.00",
        "foodAndBeverageCost": "125.00",
        "roomTax": "30.00",
        "adjustmentAmount": "15.00",
        "phoneCost": "8.00",
        "restaurantCost": "95.00",
        "roomServiceCost": "40.00",
        "miniBarCost": "25.00",
        "laundryCost": "18.00",
        "miscellaneousCost": "12.00",
        "giftShopCost": "35.00",
        "movieCost": "10.00",
        "healthClubCost": "20.00",
        "valetParkingCost": "30.00",
        "cashDisbursementCost": "5.00",
        "nonRoomCost": "40.00",
        "businessCenterCost": "15.00",
        "loungeBarCost": "55.00",
        "transportationCost": "75.00",
        "gratuityCost": "45.00",
        "conferenceRoomCost": "120.00",
        "audioVisualCost": "65.00",
        "banquetCost": "180.00",
        "internetAccessCost": "12.00",
        "earlyCheckOutCost": "20.00",
        "nonRoomTax": "25.00"
      }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "TransactionStatusResponse",
      "message": "Status update to display.",
      "canBeAborted": true/false
}
```

Response to a Successful Request

```
{
    "type": "PaymentResponse",
    "message": "Payment approved",
    "transactionDetails": {
        "id": "8ccb150a88bd4c6f9a00a687f39ca97d",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc": "2024-09-20T08:15:12+0000",
        "captured": true,
        "amountDetails": {
            "amount": "500.00",
            "currency": "USD",
            "capturedAmount": "500.00",
            "refundableAmount": "500.00"
        }
    },
    "processingDetails": {
        "status": "APPROVED",
        "verificationMethod": "NONE",
        "entryMode": "NFC_ICC",
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2025",
            "type": "VISA",
            "maskedPan": "476173XXXXXX0119",
            "countryCode": "840"
        }
    },
    "additionalInformation": {
        "requestId": "7268201146336069504011"
    },
    "linkedOperations": [],
    "receipts": {
        "merchantReceipt": {
            "preformattedReceipt": "Merchant Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$500.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 546712\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n8ccb150a88bd4c6f9a00a687f39ca97d\n\n4:15:12 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "546712"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Merchant Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "8ccb150a88bd4c6f9a00a687f39ca97d"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$500.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "4:15:12 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        },
        "customerReceipt": {
            "preformattedReceipt": "Cardholder Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$500.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 546712\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n8ccb150a88bd4c6f9a00a687f39ca97d\n\n4:15:12 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "546712"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Cardholder Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "8ccb150a88bd4c6f9a00a687f39ca97d"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$500.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "4:15:12 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        }
    },
    "lodgingDetails": {
        "duration": 3,
        "checkInDate": "030125",
        "checkOutDate": "030425",
        "guestSmokingPreference": "N",
        "numberOfGuests": 2,
        "numberOfRoomsBooked": 1,
        "guestName": "John Doe",
        "roomLocation": "Ocean View",
        "roomTaxElements": "VAT",
        "roomBedType": "KING",
        "roomRateType": "CORPORATE",
        "specialProgramCode": "1",
        "dailyRoomRate1": "150.00",
        "dailyRoomRate2": "160.00",
        "dailyRoomRate3": "170.00",
        "roomNights1": 1,
        "roomNights2": 1,
        "roomNights3": 1,
        "corporateClientCode": "CORP123456",
        "promotionalCode": "PROMO2025",
        "additionalCoupon": "DISCOUNT10",
        "travelAgencyCode": "TA789",
        "travelAgencyName": "Premium Travel Agency",
        "customerServicePhoneNumber": "1-800-555-0199",
        "tax": "45.00",
        "prepaidCost": "200.00",
        "foodAndBeverageCost": "125.00",
        "roomTax": "30.00",
        "adjustmentAmount": "15.00",
        "phoneCost": "8.00",
        "restaurantCost": "95.00",
        "roomServiceCost": "40.00",
        "miniBarCost": "25.00",
        "laundryCost": "18.00",
        "miscellaneousCost": "12.00",
        "giftShopCost": "35.00",
        "movieCost": "10.00",
        "healthClubCost": "20.00",
        "valetParkingCost": "30.00",
        "cashDisbursementCost": "5.00",
        "nonRoomCost": "40.00",
        "businessCenterCost": "15.00",
        "loungeBarCost": "55.00",
        "transportationCost": "75.00",
        "gratuityCost": "45.00",
        "conferenceRoomCost": "120.00",
        "audioVisualCost": "65.00",
        "banquetCost": "180.00",
        "internetAccessCost": "12.00",
        "earlyCheckOutCost": "20.00",
        "nonRoomTax": "25.00"
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Electronic Benefits Transfer {#sis-pymnt-svcs-local-ebt-intro}
==============================================================

Public assistance programs in the United States use Electronic Benefits Transfer (EBT) payment cards to issue monthly food and cash benefits to eligible people. EBT cards function like prepaid debit cards that can be used at authorized retailers. Food benefits are issued through the Supplemental Nutrition Assistance Program (SNAP), which helps people with low incomes purchase eligible food items.  
Use this information to process EBT SNAP (food benefits) and EBT Cash transactions when the app is in Local mode.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for Electronic Benefits Transfer {#sis-pymnt-svcs-local-ebt-reqfields}
======================================================================================

type
:
Set the value to `PaymentRequest` for a sale or to `StandaloneRefundRequest` for a stand-alone credit.

merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

amountDetails.amount
:
Set the value to the transaction amount.

amountDetails.currency
:
Set the value to the currency code.

paymentMode
:
Set the value to `EBT`.

ebtDetails.category
:
Set the value to `FOOD` for EBT SNAP (food benefits) and `CASH` for EBT Cash.

Optional Fields for Electronic Benefits Transfer {#sis-pymnt-svcs-local-ebt-optfields}
======================================================================================

ebtDetails.isBalanceInquiry
:
Set the value to `true` for a balance inquiry. The transaction amount must be set to `0`.

ebtDetails.isVoucher
:
Set the value to `true` for a voucher transaction.

amountDetails.cashbackAmount
:
Set the value to the cashback amount for a cashback transaction.

REST Example: Electronic Benefits Transfer SNAP Sale {#sis-pymnt-svcs-local-ebt-ex-rest}
========================================================================================

Request

```
{
  "type": "PaymentRequest",
  "merchantReferenceCode": "82910b8b430a414dbe224e4494545b02",
  "paymentMode": "EBT",
  "amountDetails": {
    "amount": "1.00",
    "currency": "USD"
  },
  "ebtDetails": {
    "category": "FOOD"
  }
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
  "type": "TransactionStatusResponse",
  "message": "Status update to display.",
  "canBeAborted": true
}
```

Response to a Successful Request

```
{
  "type": "PaymentResponse",
  "message": "Payment approved",
  "transactionDetails": {
    "id": "bd9c4ddd5bb84aafa42f16f2660f76c7",
    "merchantReferenceCode": "82910b8b430a414dbe224e4494545b02",
    "submitTimeUtc": "2025-09-29T09:04:02+0000",
    "captured": true,
    "amountDetails": {
      "currency": "USD",
      "amount": "1.00",
      "capturedAmount": "1.00",
      "refundableAmount": "1.00"
    }
  },
  "processingDetails": {
    "status": "APPROVED",
    "verificationMethod": "PIN",
    "entryMode": "MAGNETIC_STRIPE",
    "card": {
      "expirationMonth": "00",
      "expirationYear": "00",
      "type": "EBT",
      "maskedPan": "507719XXXXXX4720"
    }
  },
  "additionalInformation": {
    "requestId": "7591366618376609904603"
  },
  "linkedOperations": [],
  "tipAdjustStatus": "NOT_ADJUSTABLE",
  "receipts": {
    "merchantReceipt": {
      "preformattedReceipt": "Merchant Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n555555555\n\nPayment\n$1.00\n\nPlease retain receipt!\n\nCard: EBT\nAccount: **** **** **** 4720\nEntry Mode: Magstripe\nVerification: Verified by PIN\n\nTransaction: 673579\nAuthorization: 831000\nMerchant ID: ******************nt001\nTerminal ID: ****1459\n\n\nbd9c4ddd5bb84aafa42f16f2660f76c7\n\n2:34:22 PM: 9/29/2025\n\n\n",
      "receiptData": {
        "lines": {
          "MERCHANT_DETAILS_PUBLIC_NAME": {
            "label": "Name",
            "value": "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS": {
            "label": "Address",
            "value": "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP": {
            "label": "Zip",
            "value": "55555"
          },
          "MERCHANT_DETAILS_CITY": {
            "label": "City",
            "value": "New York"
          },
          "MERCHANT_DETAILS_COUNTRY": {
            "label": "Country",
            "value": "United States"
          },
          "MERCHANT_DETAILS_CONTACT": {
            "label": "Contact",
            "value": "555555555"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
            "label": "Additional Information",
            "value": ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
            "label": "Card",
            "value": "EBT"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT": {
            "label": "Account",
            "value": "**** **** **** 4720"
          },
          "PAYMENT_DETAILS_SOURCE": {
            "label": "Entry Mode",
            "value": "Magstripe"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
            "label": "Verification",
            "value": "Verified by PIN"
          },
          "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
            "label": "Transaction",
            "value": "673579"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE": {
            "label": "Authorization",
            "value": "831000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
            "label": "Merchant ID",
            "value": "******************nt001"
          },
          "CLEARING_DETAILS_TERMINAL_ID": {
            "label": "Terminal ID",
            "value": "****1459"
          },
          "RECEIPT_TYPE": {
            "label": "Receipt Type",
            "value": "Merchant Receipt"
          },
          "TRANSACTION_TYPE": {
            "label": "Type",
            "value": "Payment"
          },
          "SUBJECT": {
            "label": "Description",
            "value": ""
          },
          "IDENTIFIER": {
            "label": "PWID",
            "value": "bd9c4ddd5bb84aafa42f16f2660f76c7"
          },
          "AMOUNT_AND_CURRENCY": {
            "label": "Amount",
            "value": "$1.00"
          },
          "DATE": {
            "label": "Date",
            "value": "9/29/2025"
          },
          "TIME": {
            "label": "Time",
            "value": "2:34:22 PM"
          },
          "STATUS_TEXT": {
            "label": "Information",
            "value": "Please retain receipt!"
          }
        },
        "signatureLineRequired": false,
        "tipLineRequired": false,
        "totalLineRequired": false
      }
    },
    "customerReceipt": {
      "preformattedReceipt": "Cardholder Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n555555555\n\nPayment\n$1.00\n\nPlease retain receipt!\n\nCard: EBT\nAccount: **** **** **** 4720\nEntry Mode: Magstripe\nVerification: Verified by PIN\n\nTransaction: 673579\nAuthorization: 831000\nMerchant ID: ******************nt001\nTerminal ID: ****1459\n\n\nbd9c4ddd5bb84aafa42f16f2660f76c7\n\n2:34:22 PM: 9/29/2025\n\n\n",
      "receiptData": {
        "lines": {
          "MERCHANT_DETAILS_PUBLIC_NAME": {
            "label": "Name",
            "value": "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS": {
            "label": "Address",
            "value": "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP": {
            "label": "Zip",
            "value": "55555"
          },
          "MERCHANT_DETAILS_CITY": {
            "label": "City",
            "value": "New York"
          },
          "MERCHANT_DETAILS_COUNTRY": {
            "label": "Country",
            "value": "United States"
          },
          "MERCHANT_DETAILS_CONTACT": {
            "label": "Contact",
            "value": "555555555"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
            "label": "Additional Information",
            "value": ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
            "label": "Card",
            "value": "EBT"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT": {
            "label": "Account",
            "value": "**** **** **** 4720"
          },
          "PAYMENT_DETAILS_SOURCE": {
            "label": "Entry Mode",
            "value": "Magstripe"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
            "label": "Verification",
            "value": "Verified by PIN"
          },
          "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
            "label": "Transaction",
            "value": "673579"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE": {
            "label": "Authorization",
            "value": "831000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
            "label": "Merchant ID",
            "value": "******************nt001"
          },
          "CLEARING_DETAILS_TERMINAL_ID": {
            "label": "Terminal ID",
            "value": "****1459"
          },
          "RECEIPT_TYPE": {
            "label": "Receipt Type",
            "value": "Cardholder Receipt"
          },
          "TRANSACTION_TYPE": {
            "label": "Type",
            "value": "Payment"
          },
          "SUBJECT": {
            "label": "Description",
            "value": ""
          },
          "IDENTIFIER": {
            "label": "PWID",
            "value": "bd9c4ddd5bb84aafa42f16f2660f76c7"
          },
          "AMOUNT_AND_CURRENCY": {
            "label": "Amount",
            "value": "$1.00"
          },
          "DATE": {
            "label": "Date",
            "value": "9/29/2025"
          },
          "TIME": {
            "label": "Time",
            "value": "2:34:22 PM"
          },
          "STATUS_TEXT": {
            "label": "Information",
            "value": "Please retain receipt!"
          }
        },
        "signatureLineRequired": false,
        "tipLineRequired": false,
        "totalLineRequired": false
      }
    }
  },
  "ebtDetails": {
    "category": "FOOD"
  }
}
```

Custom Card Read {#sis-pymnt-svcs-local-custom-card-card-intro}
===============================================================

Use this information to obtain data from custom cards such as gift cards, loyalty program cards, and employee cards when the app is in Local mode. This service cannot be used to perform payment functions.
IMPORTANT Custom Card Read is supported for non-PCI cards only. To use this service, the card type must be on your allowlist. To add a card type to your allowlist, contact your implementation manager.  
To retrieve the card data, swipe the card's magnetic stripe through the payment device. The custom card read-only function reads and returns the raw card identifier to your app or point-of-sale (POS) system. You can then use the raw data within your app or POS system.  
These are examples of how you might use the Custom Card Read feature:

* **Custom gift card:** Use the card number to check a balance or process a payment in your private gift card network.
* **Employee card:** Use the card number to look up an employee's profile or account.
  {#sis-pymnt-svcs-local-custom-card-card-intro_ul_snq_dyx_xgc}

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields to Perform a Custom Card Read {#sis-pymnt-svcs-local-custom-card-read-reqfields}
================================================================================================

type
:
Set the value to `ReadCardRequest`.

REST Example: Custom Card Read {#sis-pymnt-svcs-local-custom-card-read-ex-rest}
===============================================================================

Request

```
{
   "type" : "ReadCardRequest"
}
```

Mid-Transaction Status Updates  
During the transaction, you might receive one or more update responses indicating the current status of the transaction. You can choose to display these updates on your point-of-sale (POS) system.

```
{
   "type": "OperationStatusResponse",
   "message": "Status update to display."
}
```

Response to a Successful Request

```
{
  "type": "ReadCardResponse",
  "message": "Read Card Successfully",
  "cardDetails": {
    "expiryMonth": 12,
    "expiryYear": 2025,
    "track1": "%B4111111111111111^DOE/JOHN^2512101?",
    "track2": "4111111111111111=25121010000?",
    "cardNumber": "4111111111111111"
  }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
   "type": "ErrorResponse",
   "message": "Error message to display.",
   "developerDescription": "Detailed description of error."
}
```

Printing a Customer or Merchant Receipt {#sis-pymnt-svcs-receipt-print-intro}
=============================================================================

Use this information to print a customer or merchant receipt from a previous transaction when the app is in Local mode. This feature can only be used with terminals that have integrated printers.

Endpoint
--------

The endpoint is the same for the test and production environments.  
**Test:** `wss://{terminal IP address:port number}/`  
**Production:** `wss://{terminal IP address:port number}/`

Required Fields to Print a Customer or Merchant Receipt {#sis-pymnt-svcs-receipt-print-reqfields}
=================================================================================================

type
:
Set the value to `PrintReceiptRequest`.

transactionId
:
Set the value to the ID field value from the original transaction.

receiptType
:
Set the value to CUSTOMER or MERCHANT.

REST Example: Print a Customer or Merchant Receipt {#sis-pymnt-svcs-receipt-print-ex-rest}
==========================================================================================

Request

```
{
    "type": "PrintReceiptRequest",
    "transactionId": "8fe5fa21d0814424bcec4997c9dc89c4",
    "receiptType": "CUSTOMER"
}
```

Mid-Operation Status Updates  
During the operation, you might receive one or more update responses indicating the current status of the operation. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "OperationStatusResponse",
      "message": "Status update to display."
}
```

Response to a Successful Request

```
{
    "type": "PrintReceiptResponse",
    "message": "Receipt printed successfully."
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
    "type": "ErrorResponse",
    "message": "Error message to display.",
    "developerDescription": "Detailed description of error."
}
```

Custom Printing {#sis-pymnt-svcs-semi-custom-print-intro}
=========================================================

Use this information to send a custom print request in Local mode. This feature enables you to print custom content directly to the integrated printer of a PAX terminal, including text, label-value pairs, images, barcodes, and QR codes.

> IMPORTANT  
> The Custom Printing feature does not affect your configuration for printing standard customer or merchant receipts.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for Custom Printing {#sis-pymnt-svcs-semi-custom-print-reqfields}
=================================================================================

type
:
Set this field to `CustomPrintRequest`.

printLayout.sections
:
Set this field to a list of one or more print sections. Each section must include a sectionType field to identify the type of custom content to print.

Required Fields for Custom Printing by Section Type {#sis-pymnt-svcs-semi-custom-print-sec-type-reqfields}
==========================================================================================================

Use these fields to define the required content for each custom print section in the printLayout.sections field. Each section in this field must include a sectionType field that identifies the type of content to print. The printLayout.sections field supports these sectionType values: `TEXT`, `SPACER`, `BARCODE`, and `IMAGE`. These values are case sensitive.

TEXT Section
------------

printLayout.sections\[n\].sectionType
:
Set this field to `TEXT`.

printLayout.sections\[n\].textContent.textType
:
Set this field to identify the type of text content. Supported values are `PARAGRAPH`, `LABEL_VALUE`, and `NO_LINE`.

TEXT Section: PARAGRAPH Text Content Required Fields
----------------------------------------------------

printLayout.sections\[n\].textContent.lines
:
Set this field to a list of one or more strings to print as paragraph lines.

TEXT Section: LABEL_VALUE Text Content Required Fields
------------------------------------------------------

printLayout.sections\[n\].textContent.content
:
Set this field to a list of one or more label-value pairs.

printLayout.sections\[n\].textContent.content\[n\].label.labelText
:
Set this field to the label text string.

printLayout.sections\[n\].textContent.content\[n\].value.valueText
:
Set this field to the value text string.

BARCODE Section
---------------

printLayout.sections\[n\].sectionType
:
Set this field to `BARCODE`.

printLayout.sections\[n\].content
:
Set this field to the data to encode in the barcode.

printLayout.sections\[n\].barcodeType
:
Set this field to the barcode format. Supported values are `CODE39`, `CODE128`, `EAN13`, `EAN128`, `PDF417`, and `QRCODE`.

IMAGE Section
-------------

printLayout.sections\[n\].sectionType
:
Set this field to `IMAGE`.

printLayout.sections\[n\].imageData
:
Set this field to a Base64-encoded image. Supported formats are `PNG`, `JPEG`, and `BMP`. The maximum image width and height is 384 pixels.

SPACER Section
--------------

printLayout.sections\[n\].sectionType
:
Set this field to `SPACER`.

Optional Fields for Custom Printing {#sis-pymnt-svcs-semi-custom-print-optfields}
=================================================================================

Use these fields to define optional content and formatting for custom print sections in the printLayout.sections field. Optional fields are supported for `TEXT` and `SPACER` sections.

> IMPORTANT  
> If you do not specify the value for an optional field, the default value is used.

TEXT Section: PARAGRAPH Optional Fields
---------------------------------------

printLayout.sections\[n\].textContent.align
:
Set this field to `LEFT`, `CENTER`, or `RIGHT`. The default value is `LEFT`.

printLayout.sections\[n\].textContent.textStyle.size
:
Set this field to `SMALL`, `MEDIUM`, or `LARGE`. The default value is `MEDIUM`.

printLayout.sections\[n\].textContent.textStyle.style
:
Set this field to `NORMAL` or `EMPHASIZE`. The default value is `NORMAL`.

TEXT Section: LABEL_VALUE Optional Fields
-----------------------------------------

printLayout.sections\[n\].textContent.content\[n\].label.textStyle.size
:
Set this field to `SMALL`, `MEDIUM`, or `LARGE`. The default value is `MEDIUM`.

printLayout.sections\[n\].textContent.content\[n\].label.textStyle.style
:
Set this field to `NORMAL` or `EMPHASIZE`. The default value is `NORMAL`.

printLayout.sections\[n\].textContent.content\[n\].value.textStyle.size
:
Set this field to `SMALL`, `MEDIUM`, or `LARGE`. The default value is `MEDIUM`.

printLayout.sections\[n\].textContent.content\[n\].value.textStyle.style
:
Set this field to `NORMAL` or `EMPHASIZE`. The default value is `NORMAL`.

SPACER Section Optional Fields
------------------------------

printLayout.sections\[n\].lines
:
Set this field to the number of blank lines to insert. The default value is `1`.

REST Example: Custom Printing {#sis-pymnt-svcs-semi-custom-print-ex-rest}
=========================================================================

Request

```
{
    "type": "CustomPrintRequest",
    "printLayout": {
        "sections": [
            {
                "sectionType": "TEXT",
                "textContent": {
                    "textType": "PARAGRAPH",
                    "lines": ["ACME STORE", "123 Main St"],
                    "align": "CENTER",
                    "textStyle": {
                        "size": "LARGE",
                        "style": "NORMAL"
                    }
                }
            },
            {
                "sectionType": "IMAGE",
                "imageData": "iVBORw0KGgoAAAANS..."
            },
            {
                "sectionType": "SPACER",
                "lines": 1
            },
            {
                "sectionType": "TEXT",
                "textContent": {
                    "textType": "LABEL_VALUE",
                    "content": [
                        {
                            "label": {
                                "labelText": "Subtotal",
                                "textStyle": { "size": "MEDIUM", "style": "NORMAL" }
                            },
                            "value": {
                                "valueText": "$23.45",
                                "textStyle": { "size": "MEDIUM", "style": "NORMAL" }
                            }
                        },
                        {
                            "label": {
                                "labelText": "Total",
                                "textStyle": { "size": "LARGE", "style": "NORMAL" }
                            },
                            "value": {
                                "valueText": "$25.99",
                                "textStyle": { "size": "LARGE", "style": "NORMAL" }
                            }
                        }
                    ]
                }
            },
            {
                "sectionType": "BARCODE",
                "content": "TXN123456789",
                "barcodeType": "CODE128"
            }
        ]
    }
}
```

Mid-Transaction Status Updates  
During the operation, you might receive one or more update responses indicating the current status of the operation. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "OperationStatusResponse",
      "message": "Status update to display."
}
```

Response to a Successful Request

```
{
    "type": "CustomPrintResponse",
    "message": "Custom Print successfully"
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
          "type": "ErrorResponse",
          "message": "Error message to display.",
          "developerDescription": "Detailed description of error."
    }
```

Custom Screens {#sis-pymnt-svcs-semi-custom-screens-intro}
==========================================================

Use this information to send a custom screen request in Local mode. This feature enables you to show one or more customized screens on the payment terminal. Custom screen can show informational text, collect text input, or capture a digital signature.

Endpoints
---------

The endpoint is the same for the test and production environments.  
**Test:** ` wss://{terminal IP address:port number}/`  
**Production:** ` wss://{terminal IP address:port number}/`

Required Fields for Custom Screens {#sis-pymnt-svcs-semi-custom-screens-reqfields}
==================================================================================

type
:
Set this field to `CustomScreenRequest`.

screens
:
Set this field to a list of one or more screen objects. Each screen must include a screenType field to identify the type of custom screens to show on the payment terminal.

Required Fields for Custom Screens by Screen Type {#sis-pymnt-svcs-semi-custom-screens-type-reqfields}
======================================================================================================

Use these fields to define the required content for each custom screen in the screens field. Each screen in this field must include a screenType field that identifies the type of custom screen to show on the payment terminal. The screens field supports these screenType values: `textDisplay`, `textInput`, and `signatureCapture`.

textDisplay Screen
------------------

screens\[n\].screenType
:
Set this field to `textDisplay`.

screens\[n\].title
:
Set this field to the screen title. The title cannot exceed 20 characters.

textInput Screen
----------------

screens\[n\].screenType
:
Set this field to `textInput`.

screens\[n\].title
:
Set this field to the screen title. The title cannot exceed 20 characters.

screens\[n\].textInputs
:
Set this field to a list of one or more text input fields.

screens\[n\].textInputs\[n\].textInputLabel
:
Set this field to the label for the input field. The label cannot exceed 25 characters.

screens\[n\].textInputs\[n\].textInputConfig.textInputType
:
Set this field to the type of input to accept. Supported values are `NUMERIC`, `ALPHANUMERIC`, `EMAIL`, and `PHONE`.

signatureCapture Screen
-----------------------

screens\[n\].screenType
:
Set this field to `signatureCapture`.

screens\[n\].title
:
Set this field to the screen title. The title cannot exceed 20 characters.

Optional Fields for Custom Screens {#sis-pymnt-svcs-semi-custom-screens-optfields}
==================================================================================

Use these fields to define optional content and formatting for custom screens in the screens field. Optional fields are available for all screen types, with additional optional fields supported for textDisplay and textInput screens.

> IMPORTANT  
> If you do not specify the value for an optional field, the default value is used.

Optional Fields Available on All Screen Types
---------------------------------------------

screens\[n\].description
:
Set this field to a descriptive message displayed below the title.

screens\[n\].isSkippable
:
Set this field to `true` to allow the cardholder to skip the screen. The default value is `false`.

textDisplay Screen Optional Fields
----------------------------------

screens\[n\].toggles
:
Set this field to a list of toggle items for the cardholder to accept or decline.

screens\[n\].toggles\[n\].label
:
Set this field to the label displayed next to the toggle. The label cannot exceed 40 characters.

screens\[n\].toggles\[n\].required
:
Set this field to `true` to require the cardholder to enable the toggle before proceeding. The default value is `false`.

textInput Screen Optional Fields
--------------------------------

screens\[n\].textInputs\[n\].textInputHint
:
Set this field to placeholder hint text displayed inside the input field.

screens\[n\].textInputs\[n\].textInputConfig.masked
:
Set this field to `true` to mask the input characters as the cardholder types. The default value is `false`.

screens\[n\].textInputs\[n\].textInputConfig.length.min
:
Set this field to the minimum number of characters required. Must be greater than zero.

screens\[n\].textInputs\[n\].textInputConfig.length.max
:
Set this field to the maximum number of characters allowed. Must be greater than zero and not less than the defined minimum number of characters.

screens\[n\].textInputs\[n\].textInputConfig.patternConfig.pattern
:
Set this field to a regular expression that the input value must match.

screens\[n\].textInputs\[n\].textInputConfig.patternConfig.patternError
:
Set this field to the error message displayed when the input does not match the pattern.

screens\[n\].toggles
:
Set this field to a list of toggle items for the cardholder to accept or decline.

screens\[n\].toggles\[n\].label
:
Set this field to the label displayed next to the toggle. The label cannot exceed 40 characters.

screens\[n\].toggles\[n\].required
:
Set this field to `true` to require the cardholder to enable the toggle before proceeding. The default value is `false`.

REST Example: Custom Screens {#sis-pymnt-svcs-semi-custom-screens-ex-rest}
==========================================================================

Request

```
{
    "type": "CustomScreenRequest",
    "screens": [
        {
            "screenType": "signatureCapture",
            "title": "Confirm Receipt",
            "description": "I certify that I am the authorized representative to receive these goods...",
            "isSkippable": false
        },
        {
            "screenType": "textDisplay",
            "title": "Liability Waiver",
            "description": "By proceeding, you acknowledge inspection of goods...",
            "isSkippable": false,
            "toggles": [
                {
                    "label": "I accept the terms",
                    "required": true
                }
            ]
        },
        {
            "screenType": "textInput",
            "title": "Purchase Order (PO)",
            "description": "Please enter the authorized Purchase Order (PO) number...",
            "isSkippable": false,
            "textInputs": [
                {
                    "textInputLabel": "Authorized PO Number",
                    "textInputHint": "PO518736",
                    "textInputConfig": {
                        "textInputType": "ALPHANUMERIC",
                        "masked": true,
                        "length": {
                            "min": 5,
                            "max": 10
                        },
                        "patternConfig": {
                            "pattern": "^[a-zA-Z0-9]*$",
                            "patternError": "Only letters and numbers allowed"
                        }
                    }
                }
            ],
            "toggles": [
                {
                    "label": "I accept the terms",
                    "required": true
                }
            ]
        }
    ]
}
```

Mid-Transaction Status Updates  
During the operation, you might receive one or more update responses indicating the current status of the operation. You can choose to display these updates on your point-of-sale (POS) system.

```
{
      "type": "OperationStatusResponse",
      "message": "Status update to display."
}
```

Response to a Successful Request

```
{
    "type": "CustomScreenResponse",
    "message": "Data capture successful",
    "customScreenDetails": {
        "status": "COMPLETED",
        "screens": [
            {
                "screenType": "signatureCapture",
                "title": "Confirm Receipt",
                "signatureData": "iVBORw0KGgoAAAANSUhEUg....",
                "skipped": false
            },
            {
                "screenType": "textDisplay",
                "title": "Liability Waiver",
                "toggles": [
                    {
                        "label": "I accept the terms",
                        "value": true
                    }
                ],
                "skipped": false
            },
            {
                "screenType": "textInput",
                "title": "Purchase Order (PO)",
                "inputs": [
                    {
                        "label": "Authorized PO Number",
                        "value": "PO518736"
                    }
                ],
                "toggles": [
                    {
                        "label": "I accept the terms",
                        "value": true
                    }
                ],
                "skipped": false
            }
        ]
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
          "type": "ErrorResponse",
          "message": "Error message to display.",
          "developerDescription": "Detailed description of error."
    }
```

Cloud Mode Payment Services {#sis-pymnt-svcs-cloud-mode-intro}
==============================================================

Use this information to process payment services available in the Acceptance Devices app when operated in Cloud mode. In this mode, the point-of-sale (POS) system communicates over the cloud with the Acceptance Devices app on the terminal.  
For information about other modes available in the Acceptance Devices app, see:

* [Local Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro.md "")
* [Standalone Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro.md "")
  {#sis-pymnt-svcs-cloud-mode-intro_ul_l5b_yqm_3fc}

Communication Protocol Used in Cloud Mode {#sis-pymnt-svcs-cloud-mode-comm-protocol}
====================================================================================

When operating the solution in Cloud mode, the communication protocol used between the Acceptance Devices app and the point-of-sale (POS) system is a single HTTPS request to the backend.  
The transaction response can be sent either synchronously or asynchronously:

Synchronously
:
The POS system keeps the connection open until the transaction is completed and the response is provided with the full transaction details. The backend timeout setting is 180 seconds.

Asynchronously
:
The POS system receives a response with an interaction identifier after the transaction is started. The interaction identifier can then be used to check the transaction events. After the transaction is completed, the interaction identifier can be used to get the transaction identifier. The transaction identifier can then be used to get the full transaction and receipt details. For more information, see [Receiving Transaction Responses Asynchronously](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-txn-resp-async-api-intro.md "").
{#sis-pymnt-svcs-cloud-mode-comm-protocol_dl_fc1_kvl_wbc}

Generating a Bearer Token for Authentication {#sis-pymnt-svcs-cloud-mode-bearer-tkn-intro}
==========================================================================================

Use this information to generate a bearer token for authentication. A unique bearer token is required to authenticate each payment transaction request when the app is in Cloud mode.

Generate a Bearer Token for Authentication {#sis-pymnt-svcs-cloud-mode-bearer-token-task}
=========================================================================================

Generate a new bearer token before sending a transaction request.
IMPORTANT Meta keys are not supported for bearer token generation.  
Follow these steps to generate a bearer token:

1. Create a P12 certificate for the transacting merchant ID (MID).
2. Construct a message using a JSON web Token (JWT) by following the steps shown in the [*Getting Started with REST Developer Guide*](https://developer.cybersource.com/docs/cybs/en-us/platform/developer/all/rest/rest-getting-started/restgs-jwt-message-intro/restgs-jwt-const-intro.md "").
3. Set the digest field (message body) in the JWT as blank.
4. Use the JWT as the bearer token to authenticate the payment transaction request.

Sale {#sis-pymnt-svcs-cloud-sale-api-intro}
===========================================

Use this information to process a sale transaction when the app is in Cloud mode. This transaction combines an authorization and a capture into a single transaction.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Sale {#sis-pymnt-svcs-cloud-sale-api-reqfields}
=====================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Sale {#sis-pymnt-svcs-cloud-sale-api-ex-rest}
===========================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "PaymentRequest",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "amountDetails": {
            "amount": "1.00",
            "currency": "GBP"
        }
    }
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "1541387b383d456aabb81cdf558b4e8e",
        "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc" : "2023-12-01T20:24:47+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "1.00",
          "refundableAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014622903166318504010"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Refund {#sis-pymnt-svcs-cloud-refund-api-intro}
===============================================

Use this information to process a refund when the app is in Cloud mode. This type of refund includes a reference to the original transaction for a full or partial transaction amount. Stand-alone credits are also supported in this Acceptance Devices solution. For more information, see [Stand-Alone Credit](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-cloud-standalone-credit-api-intro.md "").  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Refund {#sis-pymnt-svcs-cloud-refund-api-reqfields}
=========================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `LinkedRefundRequest`.

request.transactionId
:
Set the value to the `id` field value from the original transaction.

Optional Fields for a Refund {#sis-pymnt-svcs-cloud-refund-api-optfields}
=========================================================================

Use the optional amount and currency fields to process a partial refund. Otherwise, the full amount will be refunded.

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Refund {#sis-pymnt-svcs-cloud-refund-api-ex-rest}
===============================================================

Request

```
{ 
    "serialNumber": "1850000000",
    "request": {
        "type": "LinkedRefundRequest",
        "transactionId": "8fe5fa21d0814424bcec4997c9dc89c4",
        "amountDetails": {
            "amount": "1.00",
            "currency": "GBP"
        }
    }
}
```

Response to a Successful Request

```
{
      "type" : "LinkedRefundResponse",
      "message" : "Refund approved",
      "transactionDetails" : {
        "id" : "8fe5fa21d0814424bcec4997c9dc89c4",
        "merchantReferenceCode" : "e94e3aa304514140ae1700ba0959c7c5",
        "submitTimeUtc" : "2023-12-01T20:57:30+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "0.00",
          "refundableAmount" : "0.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014642534986108604008"
      },
      "linkedOperations" : [ {
        "id" : "b383db1aecab46d89f1dbec8b0a9aa90",
        "type" : "REFUND",
        "amount" : "1.00",
        "status" : "APPROVED",
        "submitTimeUtc" : "2023-12-01T20:57:48+0000"
      } ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nVoid\n-£1.00\n\n\nReversal accepted.\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Keyed\n\nAuthorization: -\nMerchant ID: **37599\nTerminal ID: ****0063\n\nb383db1aecab46d89f1dbec8b0a9aa90\n21:57:50: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Void"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "b383db1aecab46d89f1dbec8b0a9aa90"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:57:50"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Reversal accepted."
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nVoid\n-£1.00\n\n\nReversal accepted.\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Keyed\n\nAuthorization: -\nMerchant ID: **37599\nTerminal ID: ****0063\n\nb383db1aecab46d89f1dbec8b0a9aa90\n21:57:50: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Void"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "b383db1aecab46d89f1dbec8b0a9aa90"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:57:50"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Reversal accepted."
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Stand-Alone Credit {#sis-cloud-standalone-credit-api-intro}
===========================================================

Use this information to process a stand-alone credit in Cloud mode. This type of transaction is used to process a credit without reference to the original transaction. The customer is required to present their card for this type of transaction.

> WARNING
> When processing a stand-alone credit, there is no limit on the credit amount because there is no reference to the original transaction amount. The recommendation is to use a refund transaction whenever possible. For more information, see [Refund](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-refund-api-intro.md "").  
> Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Stand-Alone Credit {#sis-cloud-standalone-credit-api-reqfields}
=====================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `StandaloneRefundRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Stand-Alone Credit {#sis-cloud-standalone-credit-api-ex-rest}
===========================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
       "type": "StandaloneRefundRequest",
       "merchantReferenceCode": "2490c8ec0e2f4b509526815714313e33",
       "amountDetails": {
           "amount": "1.00",
           "currency": "GBP"
       }
    }
}
```

Response to a Successful Request

```
{
      "type" : "StandaloneRefundResponse",
      "message" : "Refund approved",
      "transactionDetails" : {
        "id" : "3043e0b61fad4c5483db3d498309460f",
        "merchantReferenceCode" : "2490c8ec0e2f4b509526815714313e33",
        "submitTimeUtc" : "2023-12-01T21:04:19+0000",
        "amountDetails" : {
          "amount" : "1.00",
          "currency" : "GBP"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "AMERICAN_EXPRESS",
          "maskedPan" : "374245XXXXX0001"
        }
      },
      "additionalInformation" : {
        "requestId" : "7014646720206287504012"
      },
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nRefund\n-£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks AMEX\nAccount: *** **** **** 0001\nEntry Mode: Chip\nAID: A0000000250100\n\nTransaction: -\nAuthorization: -\nMerchant ID: *****67890\nTerminal ID: ****0026\n\n3043e0b61fad4c5483db3d498309460f\n10:04:19 PM: 12/1/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks AMEX"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "*** **** **** 0001"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000250100"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Chip"
              },
              "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
                "label" : "Transaction",
                "value" : "-"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "*****67890"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0026"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Refund"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "3043e0b61fad4c5483db3d498309460f"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "12/1/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "10:04:19 PM"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nRefund\n-£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks AMEX\nAccount: *** **** **** 0001\nEntry Mode: Chip\nAID: A0000000250100\n\nTransaction: -\nAuthorization: -\nMerchant ID: *****67890\nTerminal ID: ****0026\n\n3043e0b61fad4c5483db3d498309460f\n10:04:19 PM: 12/1/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks AMEX"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "*** **** **** 0001"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000250100"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Chip"
              },
              "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
                "label" : "Transaction",
                "value" : "-"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "*****67890"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0026"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Refund"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "3043e0b61fad4c5483db3d498309460f"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "12/1/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "10:04:19 PM"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Requesting a Check Transaction Status {#sis-pymnt-svcs-cloud-txn-status-api-intro}
==================================================================================

Use this information to request a check transaction status in Cloud mode. This transaction is used to obtain response data for a transaction that was lost or timed out.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields to Request a Check Transaction Status {#sis-pymnt-svcs-cloud-txn-status-api-reqfields}
======================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `TransactionLookupRequest`.

request.idType
:
Set the value to `TRANSACTION_ID` or `MERCHANT_REFERENCE_CODE`.

request.id
:
Set the value to the `id` or merchantReferenceCode field value from the original transaction.

REST Example: Request a Check Transaction Status {#sis-pymnt-svcs-cloud-txn-status-api-ex-rest}
===============================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "TransactionLookupRequest",
        "idType": "TRANSACTION_ID",
        "id": "1541387b383d456aabb81cdf558b4e8e"
    }
}
```

Response to a Successful Request

```
{
      "type" : "TransactionLookupResponse",
      "transactionDetails" : {
        "id" : "1541387b383d456aabb81cdf558b4e8e",
        "merchantReferenceCode" : "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc" : "2023-12-01T20:24:47+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "1.00",
          "refundableAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014622903166318504010"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938238\nMerchant ID: **37599\nTerminal ID: ****0063\n\n1541387b383d456aabb81cdf558b4e8e\n21:24:51: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938238"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "1541387b383d456aabb81cdf558b4e8e"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:24:51"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Cancel Transaction {#sis-pymnt-svcs-cloud-cancel-txn-api-intro}
===============================================================

Use this information to process a cancel transaction request in Cloud mode. This request is sent to interrupt an in-process transaction.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields to Cancel Transaction {#sis-pymnt-svcs-cloud-cancel-txn-api-reqfields}
======================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `CancelRequest`.

REST Example: Cancel Transaction {#sis-pymnt-svcs-cloud-cancel-txn-api-ex-rest}
===============================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "CancelRequest"
    }
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment aborted",
      "transactionDetails" : {
        "id" : "b6522aeb9d8d49b386f7c67852581145",
        "merchantReferenceCode" : "50c86aaa02ed4c0bb4b4b596379713f7",
        "submitTimeUtc" : "2023-12-01T20:30:05+0000",
        "captured" : false,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "0.00",
          "refundableAmount" : "0.00"
        }
      },
      "processingDetails" : {
        "status" : "ABORTED",
        "verificationMethod" : "UNKNOWN",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "00",
          "expirationYear" : "00",
          "type" : "UNKNOWN",
          "maskedPan" : ""
        }
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nCanceled transaction.\n\n\nEntry Mode: Contactless\nAID: NULL\n\n\nb6522aeb9d8d49b386f7c67852581145\n21:30:05: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "NULL"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "b6522aeb9d8d49b386f7c67852581145"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:30:05"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Canceled transaction."
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nCanceled transaction.\n\n\nEntry Mode: Contactless\nAID: NULL\n\n\nb6522aeb9d8d49b386f7c67852581145\n21:30:05: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "NULL"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "b6522aeb9d8d49b386f7c67852581145"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:30:05"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Canceled transaction."
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
    }
```

Sale with On-Reader Tipping {#sis-pymnt-svcs-cloud-sale-on-reader-tip-api-intro}
================================================================================

Use this information to process a sale with on-reader tipping in Cloud mode. At the start of each transaction, the terminal prompts the customer to add a tip by showing suggested tip amounts. The customer selects or enters a tip amount on the terminal before presenting their payment card.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Sale with On-Reader Tipping {#sis-pymnt-svcs-cloud-sale-on-reader-tip-api-reqfields}
==========================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

request.askForTip
:
Set the value to `ON_DEVICE`.

REST Example: Sale with On-Reader Tipping {#sis-pymnt-svcs-cloud-sale-on-reader-tip-api-ex-rest}
================================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "adf0fa5ca70d462ba5fc0249436b656c",
      "amountDetails" : {
        "amount" : "5.00",
        "currency" : "GBP"
        },
      "askForTip" : "ON_DEVICE"
    }
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "55678c8b152046f7b1d77fd2286ce392",
        "merchantReferenceCode" : "adf0fa5ca70d462ba5fc0249436b656c",
        "submitTimeUtc" : "2023-12-01T21:01:23+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "6.00",
          "capturedAmount" : "6.00",
          "refundableAmount" : "6.00",
          "includedTipAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014644863036208304012"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\nPurchase Amount: £5.00\nTip Amount: £1.00\nTotal Amount: £6.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938252\nMerchant ID: **37599\nTerminal ID: ****0063\n\n55678c8b152046f7b1d77fd2286ce392\n22:01:27: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938252"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "55678c8b152046f7b1d77fd2286ce392"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£6.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "22:01:27"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\nPurchase Amount: £5.00\nTip Amount: £1.00\nTotal Amount: £6.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938252\nMerchant ID: **37599\nTerminal ID: ****0063\n\n55678c8b152046f7b1d77fd2286ce392\n22:01:27: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938252"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "55678c8b152046f7b1d77fd2286ce392"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£6.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "22:01:27"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with On-Receipt Tipping {#sis-cloud-sale-on-receipt-tip-intro}
===================================================================

Use this information to process a sale with on-receipt tipping when the app is in Cloud mode. After the original transaction is pre-authorized, the customer writes the tip or total amount on the printed receipt. A follow-on tip adjust request must be sent within 24 hours to capture the transaction. For more information, see [Tip Adjust](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-cloud-sale-on-receipt-tip-intro/sis-cloud-sale-on-receipt-tip-adjust-intro.md "").

> WARNING
> By using this feature, you assume the risk of overcaptures being declined and increased chargebacks, so use it only when necessary. Process sales with on-reader tipping, whenever possible. For more information, see [Sale with On-Reader Tipping](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-sale-on-reader-tip-api-intro.md "").  
> Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Sale with On-Receipt Tipping {#sis-cloud-sale-on-receipt-tip-api-reqfields}
=================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

request.capture
:
Set the value to `false`.

request.askForTip
:
Set the value to `ON_RECEIPT`.

REST Example: Sale with On-Receipt Tipping {#sis-cloud-sale-on-receipt-tip-api-ex-rest}
=======================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "1ce594be142142f4913cca805830a176",
      "amountDetails" : {
        "amount" : "20.00",
        "currency" : "USD"
      },
      "capture" : false,
      "askForTip" : "ON_RECEIPT"
      }
}
```

Response to a Successful Request

```
{
  "type" : "PaymentResponse",
  "message" : "Payment approved",
  "transactionDetails" : {
    "id" : "c6174c80b81f4413a4b9f2065c5431c7",
    "merchantReferenceCode" : "1ce594be142142f4913cca805830a176",
    "submitTimeUtc" : "2024-03-20T09:19:41+0000",
    "captured" : false,
    "amountDetails" : {
      "currency" : "USD",
      "amount" : "20.00",
      "capturedAmount" : "20.00",
      "refundableAmount" : "20.00"
    }
  },
  "processingDetails" : {
    "status" : "APPROVED",
    "verificationMethod" : "NONE",
    "entryMode" : "NFC_ICC",
    "card" : {
      "expirationMonth" : "12",
      "expirationYear" : "2025",
      "type" : "VISA",
      "maskedPan" : "476173XXXXXX0119",
      "countryCode" : "840"
    }
  },
  "additionalInformation" : {
    "instrumentId" : "7030000000022690119",
    "requestId" : "7109263864326505004007"
  },
  "linkedOperations" : [ ],
  "tipAdjustStatus" : "ADJUSTABLE",
  "receipts" : {
    "merchantReceipt" : {
      "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n1234567\n\nSale\n$20.00\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 002000\nMerchant ID: **37599\nTerminal ID: ****0063\n\n\nc6174c80b81f4413a4b9f2065c5431c7\n\n\n\n10:19:46: 20/03/2024\n\n\n\nTIP:\n___________________\n\nTOTAL:\n___________________\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks VISA"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0119"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000031010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Contactless"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "None"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****0063"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Merchant Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Sale"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "c6174c80b81f4413a4b9f2065c5431c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$20.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "10:19:46"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : true,
        "totalLineRequired" : true
      }
    },
    "customerReceipt" : {
      "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n1234567\n\nSale\n$20.00\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 002000\nMerchant ID: **37599\nTerminal ID: ****0063\n\n\nc6174c80b81f4413a4b9f2065c5431c7\n\n\n\n10:19:46: 20/03/2024\n\n\n\nTIP:\n___________________\n\nTOTAL:\n___________________\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks VISA"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0119"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000031010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Contactless"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "None"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****0063"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Cardholder Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Sale"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "c6174c80b81f4413a4b9f2065c5431c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$20.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "10:19:46"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : true,
        "totalLineRequired" : true
      }
    }
  }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Tip Adjust {#sis-cloud-sale-on-receipt-tip-adjust-intro}
========================================================

Use this information to process a tip adjust when the app is in Cloud mode. This follow-on transaction is required when processing an on-receipt tipping transaction. The tip adjust request must be sent within 24 hours to capture the transaction.  
After the original transaction is pre-authorized, the customer writes the tip or total amount on the printed receipt. A follow-on tip adjust request is then sent to capture the additional tip amount. This transaction is also referred to as an *overcapture* . For more information, see [Sale with On-Receipt Tipping](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-cloud-sale-on-receipt-tip-intro.md "").  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Required Fields for a Tip Adjust {#sis-cloud-sale-on-receipt-tip-adjust-api-reqfields}
======================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `TipAdjustRequest`.

request.transactionId
:
Set the value to the id field value from the original transaction.

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Tip Adjust {#sis-cloud-sale-on-receipt-tip-adjust-api-ex-rest}
============================================================================

Endpoints
---------

Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").  
**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions` Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type" : "TipAdjustRequest",
      "transactionId" : "c6174c80b81f4413a4b9f2065c5431c7",
      "amountDetails" : {
        "amount" : "4.00",
        "currency" : "USD"
      }
   }
}
```

Response to a Successful Request

```
{
  "type" : "TipAdjustResponse",
  "message" : "Payment approved",
  "transactionDetails" : {
    "id" : "c6174c80b81f4413a4b9f2065c5431c7",
    "merchantReferenceCode" : "1ce594be142142f4913cca805830a176",
    "submitTimeUtc" : "2024-03-20T09:19:41+0000",
    "captured" : true,
    "amountDetails" : {
      "currency" : "USD",
      "amount" : "24.00",
      "capturedAmount" : "24.00",
      "refundableAmount" : "24.00",
      "includedTipAmount" : "4.00"
    }
  },
  "processingDetails" : {
    "status" : "APPROVED",
    "verificationMethod" : "NONE",
    "entryMode" : "NFC_ICC",
    "card" : {
      "expirationMonth" : "12",
      "expirationYear" : "2025",
      "type" : "VISA",
      "maskedPan" : "476173XXXXXX0119",
      "countryCode" : "840"
    }
  },
  "additionalInformation" : {
    "instrumentId" : "7030000000022690119",
    "requestId" : "7109265975966653104007"
  },
  "linkedOperations" : [ ],
  "tipAdjustStatus" : "ADJUSTED",
  "receipts" : {
    "merchantReceipt" : {
      "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n1234567\n\nCapture\nPurchase Amount: $20.00\nTip Amount: $4.00\nTotal Amount: $24.00\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 002000\nMerchant ID: **37599\nTerminal ID: ****7478\n\n\nc6174c80b81f4413a4b9f2065c5431c7\n\n10:23:17: 20/03/2024\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks VISA"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0119"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000031010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Contactless"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "None"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****7478"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Merchant Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Capture"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "c6174c80b81f4413a4b9f2065c5431c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$24.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "10:23:17"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    },
    "customerReceipt" : {
      "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n1234567\n\nCapture\nPurchase Amount: $20.00\nTip Amount: $4.00\nTotal Amount: $24.00\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 002000\nMerchant ID: **37599\nTerminal ID: ****7478\n\n\nc6174c80b81f4413a4b9f2065c5431c7\n\n10:23:17: 20/03/2024\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks VISA"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0119"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000031010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Contactless"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "None"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****7478"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Cardholder Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Capture"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "c6174c80b81f4413a4b9f2065c5431c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$24.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "10:23:17"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    }
  }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Token Refund {#sis-pymnt-svcs-cloud-token-refund-api-intro}
===========================================================

Use this information to process a token refund in Cloud mode. A token refund transaction enables you to process a stand-alone credit against a tokenized card. In order to process a credit through a token, you must have the `Token Management Service` product enabled and an existing (saved) token from a tokenized transaction. For more information, see [Token Management Service](https://developer.cybersource.com/docs/cybs/en-us/tms/developer/ctv/rest/tms/tms-overview.md "").  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Token Refund {#sis-pymnt-svcs-cloud-token-refund-api-reqfields}
=====================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `TokenRefundRequest`.

request.instrumentId
:
Set the value to the Instrument Identifier token.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Token Refund {#sis-pymnt-svcs-cloud-token-refund-api-ex-rest}
===========================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type": "TokenRefundRequest",
      "instrumentId": "7030000000022690119",
      "merchantReferenceCode": "30ed45dc7b3f4fb9905413940ac30363",
      "amountDetails": {
        "amount": "1.00",
        "currency": "GBP"
      }
   }
}
```

Response to a Successful Request

```
{
      "type" : "TokenRefundResponse",
      "message" : "Refund approved",
      "transactionDetails" : {
        "id" : "596b797178fe45e39ce3a8b8fdf432d6",
        "merchantReferenceCode" : "30ed45dc7b3f4fb9905413940ac30363",
        "submitTimeUtc" : "2023-12-01T21:02:50+0000",
        "amountDetails" : {
          "amount" : "1.00",
          "currency" : "GBP"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "MANUAL",
        "card" : {
          "expirationMonth" : "00",
          "expirationYear" : "00",
          "type" : "VISA",
          "maskedPan" : "703000XXXXXXXXX0119"
        }
      },
      "additionalInformation" : {
        "requestId" : "7014645711206245404009"
      },
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nRefund\n-£1.00\n\n\nPlease retain receipt!\n\n\nCard: VISA\nAccount: *** **** **** **** 0119\nEntry Mode: Keyed\n\nTransaction: -\nAuthorization: -\nMerchant ID: **37599\nTerminal ID: *************L_ID\n\n596b797178fe45e39ce3a8b8fdf432d6\n10:02:50 PM: 12/1/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "*** **** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
                "label" : "Transaction",
                "value" : "-"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "*************L_ID"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Refund"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "596b797178fe45e39ce3a8b8fdf432d6"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "12/1/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "10:02:50 PM"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nRefund\n-£1.00\n\n\nPlease retain receipt!\n\n\nCard: VISA\nAccount: *** **** **** **** 0119\nEntry Mode: Keyed\n\nTransaction: -\nAuthorization: -\nMerchant ID: **37599\nTerminal ID: *************L_ID\n\n596b797178fe45e39ce3a8b8fdf432d6\n10:02:50 PM: 12/1/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "*** **** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
                "label" : "Transaction",
                "value" : "-"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "-"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "*************L_ID"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Refund"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "596b797178fe45e39ce3a8b8fdf432d6"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "-£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "12/1/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "10:02:50 PM"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Pre-Authorization {#sis-pymnt-svcs-cloud-pre-auth-api-intro}
============================================================

Use this information to process a pre-authorization for an initial amount in Cloud mode. A pre-authorization transaction places a temporary hold on the customer's payment card. The transaction amount can be captured at a later time.  
Most authorizations expire in 5 to 7 days. The issuing bank sets the length of time before expiration. When an authorization expires with the issuing bank, your bank or processor might require you to re-submit an authorization request and include a request for capture in the same message.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Pre-Authorization {#sis-pymnt-svcs-cloud-pre-auth-api-reqfields}
======================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

request.capture
:
Set the value to `false`.

REST Example: Pre-Authorization {#sis-pymnt-svcs-cloud-pre-auth-api-ex-rest}
============================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "47bd9ed54f3f4bfabb9d3ee94cfa3008",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "GBP"
      },
      "capture" : false
    }
}ß
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "e43069fbf85543659e478edd8d50f244",
        "merchantReferenceCode" : "47bd9ed54f3f4bfabb9d3ee94cfa3008",
        "submitTimeUtc" : "2023-12-01T20:38:14+0000",
        "captured" : false,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "0.00",
          "refundableAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014630972006630604008"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nAuth only\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938242\nMerchant ID: **37599\nTerminal ID: ****0063\n\ne43069fbf85543659e478edd8d50f244\n21:38:18: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938242"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Auth only"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "e43069fbf85543659e478edd8d50f244"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:38:18"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nAuth only\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938242\nMerchant ID: **37599\nTerminal ID: ****0063\n\ne43069fbf85543659e478edd8d50f244\n21:38:18: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938242"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Auth only"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "e43069fbf85543659e478edd8d50f244"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:38:18"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Incremental Authorization {#sis-pymnt-svcs-cloud-increm-auth-api-intro}
=======================================================================

Use this information to process an incremental authorization in Cloud mode. This type of request can be made on a pre-authorization transaction to increase the authorized amount before it is captured.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for an Incremental Authorization {#sis-pymnt-svcs-cloud-increm-auth-api-reqfields}
==================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `IncrementalAuthorizationRequest`.

request.transactionId
:
Set the value to the `id` field value from the original transaction.

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Incremental Authorization {#sis-pymnt-svcs-cloud-increm-auth-api-reqfields-ex-rest}
=================================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type": "IncrementalAuthorizationRequest",
      "transactionId": "e43069fbf85543659e478edd8d50f244",
      "amountDetails": {
        "amount": "2.00",
        "currency": "GBP"
      }
    }
}
```

Response to a Successful Request

```
{
      "type" : "IncrementalAuthorizationResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "6da4aff381e8483ebc65ebf4fbb27ec8",
        "merchantReferenceCode" : "47bd9ed54f3f4bfabb9d3ee94cfa3008",
        "submitTimeUtc" : "2023-12-01T20:39:43+0000",
        "captured" : false,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "2.00",
          "capturedAmount" : "0.00",
          "refundableAmount" : "0.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "MANUAL",
        "card" : {
          "expirationMonth" : "00",
          "expirationYear" : "00",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119"
        }
      },
      "additionalInformation" : {
        "requestId" : "7014631843806649604009"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nTop-up\n£2.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Keyed\nVerification: None\n\nAuthorization: 938243\nMerchant ID: **37599\nTerminal ID: ****0063\n\n6da4aff381e8483ebc65ebf4fbb27ec8\n21:39:45: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938243"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Top-up"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "6da4aff381e8483ebc65ebf4fbb27ec8"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£2.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:39:45"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nTop-up\n£2.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Keyed\nVerification: None\n\nAuthorization: 938243\nMerchant ID: **37599\nTerminal ID: ****0063\n\n6da4aff381e8483ebc65ebf4fbb27ec8\n21:39:45: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938243"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Top-up"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "6da4aff381e8483ebc65ebf4fbb27ec8"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£2.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:39:45"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Capture {#sis-pymnt-svcs-cloud-capture-api-intro}
=================================================

Use this information to capture a pre-authorized transaction in Cloud mode. The capture request references the approved pre-authorization request.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Capture {#sis-pymnt-svcs-cloud-capture-api-reqfields}
===========================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `CaptureRequest`.

request.transactionId
:
Set the value to the `id` field value from the original transaction.

Optional Fields for a Capture {#sis-pymnt-svcs-cloud-capture-api-optfields}
===========================================================================

Use the optional amount and currency fields to process a partial capture. Otherwise, the full amount will be captured.

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Capture {#sis-pymnt-svcs-cloud-capture-api-ex-rest}
=================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type": "CaptureRequest",
      "transactionId": "cb6475bafbb94d03b0f984629c63c294",
      "amountDetails": {
        "amount": "3.00",
        "currency": "GBP"
      }
   }
}
```

Response to a Successful Request

```
{
      "type" : "CaptureResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "cb6475bafbb94d03b0f984629c63c294",
        "merchantReferenceCode" : "dd02499055544be18ba7fa0397909d65",
        "submitTimeUtc" : "2023-12-01T20:43:03+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "3.00",
          "capturedAmount" : "3.00",
          "refundableAmount" : "3.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014633860196734504012"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£3.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938244\nMerchant ID: **37599\nTerminal ID: ****0063\n\ncb6475bafbb94d03b0f984629c63c294\n21:43:07: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938244"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "cb6475bafbb94d03b0f984629c63c294"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£3.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:43:07"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£3.00\n\n\nPlease retain receipt!\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938244\nMerchant ID: **37599\nTerminal ID: ****0063\n\ncb6475bafbb94d03b0f984629c63c294\n21:43:07: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938244"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "cb6475bafbb94d03b0f984629c63c294"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£3.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:43:07"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Mail Order or Telephone Order {#sis-pax-pymnt-svcs-cloud-moto-trxns-intro}
==========================================================================

Use this information to process a mail order or telephone order (MOTO) sale and other transactions in Cloud mode. The payment card is not presented physically at the terminal for a MOTO transaction because it is a card-not-present transaction.  
You can also process these MOTO transactions in Cloud mode:

Account Verification
:
A MOTO account verification request submits a zero-amount authorization request to validate the payment card.

Pre-authorization
:
A MOTO pre-authorization request places a temporary hold on the customer's payment card, enabling the transaction to be captured at a later time. Most authorizations expire within 5 to 7 days. However, the exact duration is determined by the issuing bank.

    When an authorization expires, your bank, the payment processor, or issuing bank might require you to re-submit the authorization request. In such cases, you might be required to include the capture instructions in the same message to ensure successful processing.

{#sis-pax-pymnt-svcs-cloud-moto-trxns-intro_dl_y4k_5p1_bhc}  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for Mail Order or Telephone Order {#sis-pax-pymnt-svcs-cloud-moto-trxns-reqfields}
==================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest` for a sale or to `AccountVerificationRequest` for an account verification.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

request.paymentMode
:
Set the value to `MOTO`.

Optional Fields for Mail Order or Telephone Order {#sis-pax-pymnt-svcs-cloud-moto-trxns-optfields}
==================================================================================================

capture
:
Set the value to `false` for a pre-authorization.

REST Example: Mail Order or Telephone Order Sale {#sis-pax-pymnt-svcs-cloud-moto-trxns-ex-rest}
===============================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type" : "PaymentRequest",
      "merchantReferenceCode" : "a7fbcdc92425456fa0db29c8670a3150",
      "amountDetails" : {
        "amount" : "1.00",
        "currency" : "GBP"
      },
      "paymentMode": "MOTO"
   }
}
```

Response to a Successful Request

```
{
      "type" : "PaymentResponse",
      "message" : "Payment approved",
      "transactionDetails" : {
        "id" : "4348c35f258c4f8d8c89b9898e3f1b63",
        "merchantReferenceCode" : "a7fbcdc92425456fa0db29c8670a3150",
        "submitTimeUtc" : "2023-12-01T20:51:09+0000",
        "captured" : true,
        "amountDetails" : {
          "currency" : "GBP",
          "amount" : "1.00",
          "capturedAmount" : "1.00",
          "refundableAmount" : "1.00"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "MANUAL",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "411111******1111"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7038380000019631111",
        "requestId" : "7014638853776978504011"
      },
      "linkedOperations" : [ ],
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nCVV MATCH ONLY\n\n\nCard: VISA\nAccount: **** **** **** 1111\nEntry Mode: Keyed\nVerification: Cardholder Not Present\n\nAuthorization: 938246\nMerchant ID: **37599\nTerminal ID: ****0063\n\n4348c35f258c4f8d8c89b9898e3f1b63\n21:51:27: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 1111"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "Cardholder Not Present"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938246"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "4348c35f258c4f8d8c89b9898e3f1b63"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:51:27"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "CVV MATCH ONLY"
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nSale\n£1.00\n\n\nPlease retain receipt!\n\n\nCard: VISA\nAccount: **** **** **** 1111\nEntry Mode: Keyed\nVerification: Cardholder Not Present\n\nAuthorization: 938246\nMerchant ID: **37599\nTerminal ID: ****0063\n\n4348c35f258c4f8d8c89b9898e3f1b63\n21:51:27: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 1111"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Keyed"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "Cardholder Not Present"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938246"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Sale"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "4348c35f258c4f8d8c89b9898e3f1b63"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£1.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:51:27"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Please retain receipt!"
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Account Verification {#sis-pymnt-svcs-cloud-acct-verif-api-intro}
=================================================================

Use this information to process an account verification in Cloud mode. The account verification transaction submits a zero-amount authorization request to validate the payment card.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for an Account Verification {#sis-pymnt-svcs-cloud-acct-verif-api-reqfields}
============================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `AccountVerificationRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.currency
:
Set the value to the currency code.

REST Example: Account Verification {#sis-pymnt-svcs-cloud-acct-verif-api-ex-rest}
=================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
      "type": "AccountVerificationRequest",
      "merchantReferenceCode": "ec119c3b377542b09132867d236dc834",
      "amountDetails": {
        "currency": "GBP"
      }
   }
}
```

Response to a Successful Request

```
 {
      "type" : "AccountVerificationResponse",
      "message" : "Verification successful",
      "transactionDetails" : {
        "id" : "2dd6beb00d8d4bb8bf1a4718917a3003",
        "merchantReferenceCode" : "ec119c3b377542b09132867d236dc834",
        "submitTimeUtc" : "2023-12-01T20:27:02+0000",
        "amountDetails" : {
          "currency" : "GBP"
        }
      },
      "processingDetails" : {
        "status" : "APPROVED",
        "verificationMethod" : "NONE",
        "entryMode" : "NFC_ICC",
        "card" : {
          "expirationMonth" : "12",
          "expirationYear" : "2025",
          "type" : "VISA",
          "maskedPan" : "476173XXXXXX0119",
          "countryCode" : "840"
        }
      },
      "additionalInformation" : {
        "instrumentId" : "7030000000022690119",
        "requestId" : "7014624258386432804007"
      },
      "receipts" : {
        "merchantReceipt" : {
          "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nAccount Verification\n£0.00\n\n\nAccount Valid.\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938239\nMerchant ID: **37599\nTerminal ID: ****0063\n\n2dd6beb00d8d4bb8bf1a4718917a3003\n21:27:07: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938239"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Merchant Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Account Verification"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "2dd6beb00d8d4bb8bf1a4718917a3003"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£0.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:27:07"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Account Valid."
              }
            },
            "signatureLineRequired" : false
          }
        },
        "customerReceipt" : {
          "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nAccount Verification\n£0.00\n\n\nAccount Valid.\n\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: None\n\nAuthorization: 938239\nMerchant ID: **37599\nTerminal ID: ****0063\n\n2dd6beb00d8d4bb8bf1a4718917a3003\n21:27:07: 01/12/2023\n\n\n",
          "receiptData" : {
            "lines" : {
              "MERCHANT_DETAILS_PUBLIC_NAME" : {
                "label" : "Name",
                "value" : "CP Test"
              },
              "MERCHANT_DETAILS_ADDRESS" : {
                "label" : "Address",
                "value" : "Sample Street"
              },
              "MERCHANT_DETAILS_ZIP" : {
                "label" : "Zip",
                "value" : "UB3 2EA"
              },
              "MERCHANT_DETAILS_CITY" : {
                "label" : "City",
                "value" : "London"
              },
              "MERCHANT_DETAILS_COUNTRY" : {
                "label" : "Country",
                "value" : "United Kingdom"
              },
              "MERCHANT_DETAILS_CONTACT" : {
                "label" : "Contact",
                "value" : "1234567"
              },
              "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
                "label" : "Additional Information",
                "value" : ""
              },
              "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
                "label" : "Card",
                "value" : "Payworks VISA"
              },
              "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
                "label" : "Account",
                "value" : "**** **** **** 0119"
              },
              "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
                "label" : "AID",
                "value" : "A0000000031010"
              },
              "PAYMENT_DETAILS_SOURCE" : {
                "label" : "Entry Mode",
                "value" : "Contactless"
              },
              "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
                "label" : "Verification",
                "value" : "None"
              },
              "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
                "label" : "Authorization",
                "value" : "938239"
              },
              "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
                "label" : "Merchant ID",
                "value" : "**37599"
              },
              "CLEARING_DETAILS_TERMINAL_ID" : {
                "label" : "Terminal ID",
                "value" : "****0063"
              },
              "RECEIPT_TYPE" : {
                "label" : "Receipt Type",
                "value" : "Cardholder Receipt"
              },
              "TRANSACTION_TYPE" : {
                "label" : "Type",
                "value" : "Account Verification"
              },
              "SUBJECT" : {
                "label" : "Description",
                "value" : ""
              },
              "IDENTIFIER" : {
                "label" : "PWID",
                "value" : "2dd6beb00d8d4bb8bf1a4718917a3003"
              },
              "AMOUNT_AND_CURRENCY" : {
                "label" : "Amount",
                "value" : "£0.00"
              },
              "DATE" : {
                "label" : "Date",
                "value" : "01/12/2023"
              },
              "TIME" : {
                "label" : "Time",
                "value" : "21:27:07"
              },
              "STATUS_TEXT" : {
                "label" : "Information",
                "value" : "Account Valid."
              }
            },
            "signatureLineRequired" : false
          }
        }
      }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Cashback {#sis-pymnt-svcs-cloud-cashback-api-intro}
===================================================

Use this information to process a cashback transaction in Cloud mode. This type of transaction enables a customer to request that a specified amount of cash be given to them as part of the transaction. A cashback transaction can be processed with or without a purchase.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Cashback {#sis-pymnt-svcs-cloud-cashback-api-reqfields}
=============================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

request.amountDetails.cashbackAmount
:
Set the value to the cashback amount.

REST Example: Cashback {#sis-pymnt-svcs-cloud-cashback-api-ex-rest}
===================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "PaymentRequest",
        "merchantReferenceCode": "bd74d30930e349548fd9d125f88291bc",
        "amountDetails": {
            "amount": "20.00",
            "currency": "GBP",
            "cashbackAmount": "5.00"
        }
    }
}
```

Response to a Successful Request

```
{
  "type" : "PaymentResponse",
  "message" : "Payment approved",
  "transactionDetails" : {
    "id" : "218b28d38bf3424ab4ade95b9be1c75b",
    "merchantReferenceCode" : "bd74d30930e349548fd9d125f88291bc",
    "submitTimeUtc" : "2024-03-20T08:55:37+0000",
    "captured" : true,
    "amountDetails" : {
      "currency" : "GBP",
      "amount" : "20.00",
      "capturedAmount" : "25.00",
      "refundableAmount" : "20.00",
      "cashbackAmount" : "5.00"
    }
  },
  "processingDetails" : {
    "status" : "APPROVED",
    "verificationMethod" : "PIN",
    "entryMode" : "ICC",
    "card" : {
      "expirationMonth" : "12",
      "expirationYear" : "2025",
      "type" : "MASTERCARD",
      "maskedPan" : "541333XXXXXX0011",
      "countryCode" : "276"
    }
  },
  "additionalInformation" : {
    "instrumentId" : "7030000000232230011",
    "requestId" : "7109249459396751504008"
  },
  "linkedOperations" : [ ],
  "tipAdjustStatus" : "NOT_ADJUSTABLE",
  "receipts" : {
    "merchantReceipt" : {
      "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nCashback\n£25.00\nPurchase Amount: £20.00\nCashback: £5.00\nPlease retain receipt!\n\nCard: Payworks MASTER\nAccount: **** **** **** 0011\nEntry Mode: Chip\nAID: A0000000041010\nCard Number: 0\nVerification: PIN\n\nAuthorization: 002500\nMerchant ID: **37599\nTerminal ID: ****0063\n\n\n218b28d38bf3424ab4ade95b9be1c75b\n\n09:55:46: 20/03/2024\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "UB3 2EA"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "London"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United Kingdom"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks MASTER"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0011"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000041010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Chip"
          },
          "PAYMENT_DETAILS_ACCOUNT_SEQUENCE_NUMBER" : {
            "label" : "Card Number",
            "value" : "0"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "PIN"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002500"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****0063"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Merchant Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Cashback"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "218b28d38bf3424ab4ade95b9be1c75b"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "09:55:46"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    },
    "customerReceipt" : {
      "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\nUB3 2EA London\nUnited Kingdom\n1234567\n\nCashback\n£25.00\nPurchase Amount: £20.00\nCashback: £5.00\nPlease retain receipt!\n\nCard: Payworks MASTER\nAccount: **** **** **** 0011\nEntry Mode: Chip\nAID: A0000000041010\nCard Number: 0\nVerification: PIN\n\nAuthorization: 002500\nMerchant ID: **37599\nTerminal ID: ****0063\n\n\n218b28d38bf3424ab4ade95b9be1c75b\n\n09:55:46: 20/03/2024\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "UB3 2EA"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "London"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United Kingdom"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "1234567"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "Payworks MASTER"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 0011"
          },
          "PAYMENT_DETAILS_EMV_APPLICATION_ID" : {
            "label" : "AID",
            "value" : "A0000000041010"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Chip"
          },
          "PAYMENT_DETAILS_ACCOUNT_SEQUENCE_NUMBER" : {
            "label" : "Card Number",
            "value" : "0"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "PIN"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "002500"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "**37599"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****0063"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Cardholder Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Cashback"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "218b28d38bf3424ab4ade95b9be1c75b"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "20/03/2024"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "09:55:46"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    }
  }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with Installment Details {#sis-pymnt-svcs-cloud-sale-installment-details-intro}
====================================================================================

Use this information to process a sale transaction with installment details when the app is in Cloud mode. This type of transaction can be used to include the required installment details as part of the sale transaction.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").  
This transaction is available only in the Latin America and Caribbean (LAC) region.

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Sale with Installment Details {#sis-pymnt-svcs-cloud-sale-installment-details-reqfields}
==============================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Installment Details {#sis-pymnt-svcs-cloud-sale-installment-details-optfields}
==============================================================================================================

Use one or more of the optional installmentDetails fields to provide additional installment details.

request.installmentDetails.numberOfInstallments
:
Set the value to the number of installments.

request.installmentDetails.planType
:
Set the value to `MERCHANT_FUNDED` or `ISSUER_FUNDED`.

request.installmentDetails.interestPlan
:
Set the value to `true` or `false`.

request.installmentDetails.governmentPlan
:
Set the value to `true` or `false`.

REST Example: Sale with Installment Details {#sis-pymnt-svcs-cloud-sale-installment-details-ex-rest}
====================================================================================================

Request

```
{
  "serialNumber": "1850000000",
  "request": {
    "type": "PaymentRequest",
    "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
    "amountDetails": {
      "amount": "20.00",
      "currency": "USD"
    },
    "installmentDetails": {
      "numberOfInstallments": 5,
      "planType": "MERCHANT_FUNDED",
      "interestPlan": true,
      "governmentPlan": true
    }
  }
}
```

Response to a Successful Request

```
{
    "type": "PaymentResponse",
    "message": "Payment approved",
    "transactionDetails": {
        "id": "8ccb150a88bd4c6f9a00a687f39ca97d",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc": "2024-09-20T08:15:12+0000",
        "captured": true,
        "amountDetails": {
            "amount": "20.00",
            "currency": "USD",
            "capturedAmount": "20.00",
            "refundableAmount": "20.00"
        }
    },
    "processingDetails": {
        "status": "APPROVED",
        "verificationMethod": "NONE",
        "entryMode": "NFC_ICC",
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2025",
            "type": "VISA",
            "maskedPan": "476173XXXXXX0119",
            "countryCode": "840"
        }
    },
    "additionalInformation": {
        "requestId": "7268201146336069504011"
    },
    "linkedOperations": [],
    "receipts": {
        "merchantReceipt": {
            "preformattedReceipt": "Merchant Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$20.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 546712\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n8ccb150a88bd4c6f9a00a687f39ca97d\n\n4:15:12 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "546712"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Merchant Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "8ccb150a88bd4c6f9a00a687f39ca97d"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$20.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "4:15:12 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        },
        "customerReceipt": {
            "preformattedReceipt": "Cardholder Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$20.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 546712\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n8ccb150a88bd4c6f9a00a687f39ca97d\n\n4:15:12 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "546712"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Cardholder Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "8ccb150a88bd4c6f9a00a687f39ca97d"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$20.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "4:15:12 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        }
    },
    "installmentDetails": {
        "numberOfInstallments": 5,
        "planType": "MERCHANT_FUNDED",
        "interestPlan": true,
        "governmentPlan": true
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with Payment Facilitator Details {#sis-pymnt-svcs-cloud-sale-pymnt-facil-details-intro}
============================================================================================

Use this information to process a sale transaction with payment facilitator details when the app is in Cloud mode. This type of transaction can be used to include the required payment facilitator details as part of the sale transaction.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Sale with Payment Facilitator Details {#sis-pymnt-svcs-cloud-sale-pymnt-facil-details-reqfields}
======================================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Payment Facilitator Details {#sis-pymnt-svcs-cloud-sale-pymnt-facil-details-optfields}
======================================================================================================================

Use one or more of the optional merchantDetails fields to provide the required payment facilitator details.

request.merchantDetails.salesOrganizationId
:
Set the value to the sales organization identifier.

request.merchantDetails.subMerchantId
:
Set the value to the sub-merchant identifier.

request.merchantDetails.descriptorName
:
Set the value to the descriptor name.

REST Example: Sale with Payment Facilitator Details {#sis-pymnt-svcs-cloud-sale-pymnt-facil-details-ex-rest}
============================================================================================================

Request

```
{
  "serialNumber": "1850000000",
  "request": {
    "type": "PaymentRequest",
    "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
    "amountDetails": {
      "amount": "1.00",
      "currency": "USD"
    },
    "merchantDetails": {
      "salesOrganizationId": "12345",
      "subMerchantId": "SM67890",
      "descriptorName": "ExampleMerchant"
    }
  }
}
```

Response to a Successful Request

```
{
    "type": "PaymentResponse",
    "message": "Payment approved",
    "transactionDetails": {
        "id": "940d49ee94444764acb1c898e2254954",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc": "2024-09-20T07:53:36+0000",
        "captured": true,
        "amountDetails": {
            "amount": "1.00",
            "currency": "USD",
            "capturedAmount": "1.00",
            "refundableAmount": "1.00"
        }
    },
    "processingDetails": {
        "status": "APPROVED",
        "verificationMethod": "NONE",
        "entryMode": "NFC_ICC",
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2025",
            "type": "VISA",
            "maskedPan": "476173XXXXXX0119",
            "countryCode": "840"
        }
    },
    "additionalInformation": {
        "requestId": "7268188188226629104009"
    },
    "linkedOperations": [],
    "receipts": {
        "merchantReceipt": {
            "preformattedReceipt": "Merchant Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$1.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 545814\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n940d49ee94444764acb1c898e2254954\n\n3:53:36 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "545814"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Merchant Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "940d49ee94444764acb1c898e2254954"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$1.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "3:53:36 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        },
        "customerReceipt": {
            "preformattedReceipt": "Cardholder Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$1.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 545814\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n940d49ee94444764acb1c898e2254954\n\n3:53:36 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "545814"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Cardholder Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "940d49ee94444764acb1c898e2254954"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$1.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "3:53:36 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        }
    },
    "merchantDetails": {
        "salesOrganizationId": "12345",
        "subMerchantId": "SM67890",
        "descriptorName": "ExampleMerchant"
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with Tax Details {#sis-pymnt-svcs-cloud-sale-tax-details-intro}
====================================================================

Use this information to process a sale transaction with tax details when the app is in Cloud mode. This type of transaction can be used to include the required tax details as part of the sale transaction.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Sale with Tax Details {#sis-pymnt-svcs-cloud-sale-tax-details-reqfields}
==============================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Tax Details {#sis-pymnt-svcs-cloud-sale-tax-details-optfields}
==============================================================================================

Use one or more of the optional taxDetails fields to provide the required tax details.

request.taxDetails.taxId
:
Set the value to the merchant tax identifier.

request.taxDetails.salesSlipNumber
:
Set the value to the sales slip number.

request.taxDetails.includedTaxAmount
:
Set the value to the tax amount.

request.taxDetails.includedLocalTaxAmount
:
Set the value to the local tax amount.

request.taxDetails.includedNationalTaxAmount
:
Set the value to the national tax amount.

REST Example: Sale with Tax Details {#sis-pymnt-svcs-cloud-sale-tax-details-ex-rest}
====================================================================================

Request

```
{
  "serialNumber": "1850000000",
  "request": {
    "type": "PaymentRequest",
    "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
    "amountDetails": {
      "amount": "20.00",
      "currency": "USD"
    },
    "taxDetails": {
      "taxId": "TaxID1234",
      "salesSlipNumber": 12345678,
      "includedTaxAmount": "5.00",
      "includedLocalTaxAmount": "1.00",
      "includedNationalTaxAmount": "2.00"
    }
  }
}
```

Response to a Successful Request

```
{
    "type": "PaymentResponse",
    "message": "Payment approved",
    "transactionDetails": {
        "id": "4bebd72cf0ff4a9ea212baca0c6d9faf",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc": "2024-09-20T07:15:25+0000",
        "captured": true,
        "amountDetails": {
            "amount": "20.00",
            "currency": "USD",
            "capturedAmount": "20.00",
            "refundableAmount": "20.00"
        }
    },
    "processingDetails": {
        "status": "APPROVED",
        "verificationMethod": "NONE",
        "entryMode": "NFC_ICC",
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2025",
            "type": "VISA",
            "maskedPan": "476173XXXXXX0119",
            "countryCode": "840"
        }
    },
    "additionalInformation": {
        "requestId": "7268165283576248404007"
    },
    "linkedOperations": [],
    "receipts": {
        "merchantReceipt": {
            "preformattedReceipt": "Merchant Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$20.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 129702\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n4bebd72cf0ff4a9ea212baca0c6d9faf\n\n3:15:25 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "129702"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Merchant Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "4bebd72cf0ff4a9ea212baca0c6d9faf"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$20.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "3:15:25 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        },
        "customerReceipt": {
            "preformattedReceipt": "Cardholder Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$20.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 129702\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n4bebd72cf0ff4a9ea212baca0c6d9faf\n\n3:15:25 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "129702"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Cardholder Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "4bebd72cf0ff4a9ea212baca0c6d9faf"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$20.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "3:15:25 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        }
    },
    "taxDetails": {
        "taxId": "TaxID1234",
        "salesSlipNumber": 12345678,
        "includedTaxAmount": "5.00",
        "includedLocalTaxAmount": "1.00",
        "includedNationalTaxAmount": "2.00"
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Sale with Lodging Details {#sis-pymnt-svcs-cloud-sale-lodging-intro}
====================================================================

Use this information to process a sale transaction with lodging details in Cloud mode. This transaction includes required lodging details as part of the sale transaction.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Sale with Lodging Details {#sis-pymnt-svcs-cloud-sale-lodging-reqfields}
==============================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest`.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

Optional Fields for a Sale with Lodging Details {#sis-pymnt-svcs-cloud-sale-lodging-optfields}
==============================================================================================

Use one or more of the optional fields to include additional details in the transaction.

request.lodgingDetails.duration
:
Set this field to the number of nights of the lodging stay.

request.lodgingDetails.checkInDate
:
Set this field to the check-in date in MMDDYY format.

request.lodgingDetails.checkOutDate
:
Set this field to the check-out date in MMDDYY format.

request.lodgingDetails.guestSmokingPreference
:
Set this field to Y or N to indicate the guest's smoking preference.

request.lodgingDetails.numberOfGuests
:
Set this field to the number of guests.

request.lodgingDetails.numberOfRoomsBooked
:
Set this field to the number of rooms booked.

request.lodgingDetails.guestName
:
Set this field to the name of the guest.

request.lodgingDetails.roomLocation
:
Set this field to the room location description.

request.lodgingDetails.roomTaxElements
:
Set this field to the applicable room tax elements.

request.lodgingDetails.roomBedType
:
Set this field to the type of bed in the room.

request.lodgingDetails.roomRateType
:
Set this field to the room rate type.

request.lodgingDetails.specialProgramCode
:
Set this field to the special program code.

request.lodgingDetails.dailyRoomRate1
:
Set this field to the daily room rate for the first rate tier.

request.lodgingDetails.dailyRoomRate2
:
Set this field to the daily room rate for the second rate tier.

request.lodgingDetails.dailyRoomRate3
:
Set this field to the daily room rate for the third rate tier.

request.lodgingDetails.roomNights1
:
Set this field to the number of nights at the first rate tier.

request.lodgingDetails.roomNights2
:
Set this field to the number of nights at the second rate tier.

request.lodgingDetails.roomNights3
:
Set this field to the number of nights at the third rate tier.

request.lodgingDetails.corporateClientCode
:
Set this field to the corporate client code.

request.lodgingDetails.promotionalCode
:
Set this field to the promotional code.

request.lodgingDetails.additionalCoupon
:
Set this field to an additional coupon code.

request.lodgingDetails.travelAgencyCode
:
Set this field to the travel agency code.

request.lodgingDetails.travelAgencyName
:
Set this field to the name of the travel agency.

request.lodgingDetails.customerServicePhoneNumber
:
Set this field to the customer service phone number.

request.lodgingDetails.tax
:
Set this field to the total tax amount.

request.lodgingDetails.prepaidCost
:
Set this field to the prepaid cost amount.

request.lodgingDetails.foodAndBeverageCost
:
Set this field to the food and beverage cost.

request.lodgingDetails.roomTax
:
Set this field to the room tax amount.

request.lodgingDetails.adjustmentAmount
:
Set this field to the adjustment amount.

request.lodgingDetails.phoneCost
:
Set this field to the phone cost.

request.lodgingDetails.restaurantCost
:
Set this field to the restaurant cost.

request.lodgingDetails.roomServiceCost
:
Set this field to the room service cost.

request.lodgingDetails.miniBarCost
:
Set this field to the mini bar cost.

request.lodgingDetails.laundryCost
:
Set this field to the laundry cost.

request.lodgingDetails.miscellaneousCost
:
Set this field to the miscellaneous cost.

request.lodgingDetails.giftShopCost
:
Set this field to the gift shop cost.

request.lodgingDetails.movieCost
:
Set this field to the movie cost.

request.lodgingDetails.healthClubCost
:
Set this field to the health club cost.

request.lodgingDetails.valetParkingCost
:
Set this field to the valet parking cost.

request.lodgingDetails.cashDisbursementCost
:
Set this field to the cash disbursement cost.

request.lodgingDetails.nonRoomCost
:
Set this field to the non-room cost.

request.lodgingDetails.businessCenterCost
:
Set this field to the business center cost.

request.lodgingDetails.loungeBarCost
:
Set this field to the lounge or bar cost.

request.lodgingDetails.transportationCost
:
Set this field to the transportation cost.

request.lodgingDetails.gratuityCost
:
Set this field to the gratuity cost.

request.lodgingDetails.conferenceRoomCost
:
Set this field to the conference room cost.

request.lodgingDetails.audioVisualCost
:
Set this field to the audio/visual equipment cost.

request.lodgingDetails.banquetCost
:
Set this field to the banquet cost.

request.lodgingDetails.internetAccessCost
:
Set this field to the internet access cost.

request.lodgingDetails.earlyCheckOutCost
:
Set this field to the early check-out cost.

request.lodgingDetails.nonRoomTax
:
Set this field to the non-room tax amount.

REST Example: Sale with Lodging Details {#sis-pymnt-svcs-cloud-sale-lodging-ex-rest}
====================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "PaymentRequest",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "amountDetails": {
            "amount": "500.00",
            "currency": "USD"
        },
        "lodgingDetails": {
            "duration": 3,
            "checkInDate": "030125",
            "checkOutDate": "030425",
            "guestSmokingPreference": "N",
            "numberOfGuests": 2,
            "numberOfRoomsBooked": 1,
            "guestName": "John Doe",
            "roomLocation": "Ocean View",
            "roomTaxElements": "VAT",
            "roomBedType": "KING",
            "roomRateType": "CORPORATE",
            "specialProgramCode": "1",
            "dailyRoomRate1": "150.00",
            "dailyRoomRate2": "160.00",
            "dailyRoomRate3": "170.00",
            "roomNights1": 1,
            "roomNights2": 1,
            "roomNights3": 1,
            "corporateClientCode": "CORP123456",
            "promotionalCode": "PROMO2025",
            "additionalCoupon": "DISCOUNT10",
            "travelAgencyCode": "TA789",
            "travelAgencyName": "Premium Travel Agency",
            "customerServicePhoneNumber": "1-800-555-0199",
            "tax": "45.00",
            "prepaidCost": "200.00",
            "foodAndBeverageCost": "125.00",
            "roomTax": "30.00",
            "adjustmentAmount": "15.00",
            "phoneCost": "8.00",
            "restaurantCost": "95.00",
            "roomServiceCost": "40.00",
            "miniBarCost": "25.00",
            "laundryCost": "18.00",
            "miscellaneousCost": "12.00",
            "giftShopCost": "35.00",
            "movieCost": "10.00",
            "healthClubCost": "20.00",
            "valetParkingCost": "30.00",
            "cashDisbursementCost": "5.00",
            "nonRoomCost": "40.00",
            "businessCenterCost": "15.00",
            "loungeBarCost": "55.00",
            "transportationCost": "75.00",
            "gratuityCost": "45.00",
            "conferenceRoomCost": "120.00",
            "audioVisualCost": "65.00",
            "banquetCost": "180.00",
            "internetAccessCost": "12.00",
            "earlyCheckOutCost": "20.00",
            "nonRoomTax": "25.00"
        }
    }
}
```

Response to a Successful Request

```
{
    "type": "PaymentResponse",
    "message": "Payment approved",
    "transactionDetails": {
        "id": "8ccb150a88bd4c6f9a00a687f39ca97d",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "submitTimeUtc": "2024-09-20T08:15:12+0000",
        "captured": true,
        "amountDetails": {
            "amount": "500.00",
            "currency": "USD",
            "capturedAmount": "500.00",
            "refundableAmount": "500.00"
        }
    },
    "processingDetails": {
        "status": "APPROVED",
        "verificationMethod": "NONE",
        "entryMode": "NFC_ICC",
        "card": {
            "expirationMonth": "12",
            "expirationYear": "2025",
            "type": "VISA",
            "maskedPan": "476173XXXXXX0119",
            "countryCode": "840"
        }
    },
    "additionalInformation": {
        "requestId": "7268201146336069504011"
    },
    "linkedOperations": [],
    "receipts": {
        "merchantReceipt": {
            "preformattedReceipt": "Merchant Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$500.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 546712\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n8ccb150a88bd4c6f9a00a687f39ca97d\n\n4:15:12 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "546712"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Merchant Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "8ccb150a88bd4c6f9a00a687f39ca97d"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$500.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "4:15:12 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        },
        "customerReceipt": {
            "preformattedReceipt": "Cardholder Receipt\nTest\nSample Street 123\n34351 New York\nUnited States\n12345678\n\nPayment\nUSD$500.00\n\nPlease retain receipt!\n\nCard: Payworks VISA\nAccount: **** **** **** 0119\nEntry Mode: Contactless\nAID: A0000000031010\nVerification: No Verification\n\nTransaction: 546712\nAuthorization: 831000\nMerchant ID: ************st051\nTerminal ID: ****7069\n\n\n8ccb150a88bd4c6f9a00a687f39ca97d\n\n4:15:12 AM: 9/20/2024\n\n\n",
            "receiptData": {
                "signatureLineRequired": false,
                "lines": {
                    "MERCHANT_DETAILS_PUBLIC_NAME": {
                        "label": "Name",
                        "value": "Test"
                    },
                    "MERCHANT_DETAILS_ADDRESS": {
                        "label": "Address",
                        "value": "Sample Street 123"
                    },
                    "MERCHANT_DETAILS_ZIP": {
                        "label": "Zip",
                        "value": "34351"
                    },
                    "MERCHANT_DETAILS_CITY": {
                        "label": "City",
                        "value": "New York"
                    },
                    "MERCHANT_DETAILS_COUNTRY": {
                        "label": "Country",
                        "value": "United States"
                    },
                    "MERCHANT_DETAILS_CONTACT": {
                        "label": "Contact",
                        "value": "12345678"
                    },
                    "MERCHANT_DETAILS_ADDITIONAL_INFORMATION": {
                        "label": "Additional Information",
                        "value": ""
                    },
                    "PAYMENT_DETAILS_SCHEME_OR_LABEL": {
                        "label": "Card",
                        "value": "Payworks VISA"
                    },
                    "PAYMENT_DETAILS_MASKED_ACCOUNT": {
                        "label": "Account",
                        "value": "**** **** **** 0119"
                    },
                    "PAYMENT_DETAILS_EMV_APPLICATION_ID": {
                        "label": "AID",
                        "value": "A0000000031010"
                    },
                    "PAYMENT_DETAILS_SOURCE": {
                        "label": "Entry Mode",
                        "value": "Contactless"
                    },
                    "PAYMENT_DETAILS_CUSTOMER_VERIFICATION": {
                        "label": "Verification",
                        "value": "No Verification"
                    },
                    "CLEARING_DETAILS_TRANSACTION_IDENTIFIER": {
                        "label": "Transaction",
                        "value": "546712"
                    },
                    "CLEARING_DETAILS_AUTHORIZATION_CODE": {
                        "label": "Authorization",
                        "value": "831000"
                    },
                    "CLEARING_DETAILS_MERCHANT_IDENTIFIER": {
                        "label": "Merchant ID",
                        "value": "************st051"
                    },
                    "CLEARING_DETAILS_TERMINAL_ID": {
                        "label": "Terminal ID",
                        "value": "****7069"
                    },
                    "RECEIPT_TYPE": {
                        "label": "Receipt Type",
                        "value": "Cardholder Receipt"
                    },
                    "TRANSACTION_TYPE": {
                        "label": "Type",
                        "value": "Payment"
                    },
                    "SUBJECT": {
                        "label": "Description",
                        "value": ""
                    },
                    "IDENTIFIER": {
                        "label": "PWID",
                        "value": "8ccb150a88bd4c6f9a00a687f39ca97d"
                    },
                    "AMOUNT_AND_CURRENCY": {
                        "label": "Amount",
                        "value": "USD$500.00"
                    },
                    "DATE": {
                        "label": "Date",
                        "value": "9/20/2024"
                    },
                    "TIME": {
                        "label": "Time",
                        "value": "4:15:12 AM"
                    },
                    "STATUS_TEXT": {
                        "label": "Information",
                        "value": "Please retain receipt!"
                    }
                },
                "tipLineRequired": false,
                "totalLineRequired": false
            }
        }
    },
    "lodgingDetails": {
        "duration": 3,
        "checkInDate": "030125",
        "checkOutDate": "030425",
        "guestSmokingPreference": "N",
        "numberOfGuests": 2,
        "numberOfRoomsBooked": 1,
        "guestName": "John Doe",
        "roomLocation": "Ocean View",
        "roomTaxElements": "VAT",
        "roomBedType": "KING",
        "roomRateType": "CORPORATE",
        "specialProgramCode": "1",
        "dailyRoomRate1": "150.00",
        "dailyRoomRate2": "160.00",
        "dailyRoomRate3": "170.00",
        "roomNights1": 1,
        "roomNights2": 1,
        "roomNights3": 1,
        "corporateClientCode": "CORP123456",
        "promotionalCode": "PROMO2025",
        "additionalCoupon": "DISCOUNT10",
        "travelAgencyCode": "TA789",
        "travelAgencyName": "Premium Travel Agency",
        "customerServicePhoneNumber": "1-800-555-0199",
        "tax": "45.00",
        "prepaidCost": "200.00",
        "foodAndBeverageCost": "125.00",
        "roomTax": "30.00",
        "adjustmentAmount": "15.00",
        "phoneCost": "8.00",
        "restaurantCost": "95.00",
        "roomServiceCost": "40.00",
        "miniBarCost": "25.00",
        "laundryCost": "18.00",
        "miscellaneousCost": "12.00",
        "giftShopCost": "35.00",
        "movieCost": "10.00",
        "healthClubCost": "20.00",
        "valetParkingCost": "30.00",
        "cashDisbursementCost": "5.00",
        "nonRoomCost": "40.00",
        "businessCenterCost": "15.00",
        "loungeBarCost": "55.00",
        "transportationCost": "75.00",
        "gratuityCost": "45.00",
        "conferenceRoomCost": "120.00",
        "audioVisualCost": "65.00",
        "banquetCost": "180.00",
        "internetAccessCost": "12.00",
        "earlyCheckOutCost": "20.00",
        "nonRoomTax": "25.00"
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Receiving Transaction Responses Asynchronously {#sis-pymnt-svcs-cloud-txn-resp-async-api-intro}
===============================================================================================

Use this information to receive transaction responses asynchronously when the app is in Cloud mode. There is a follow-on service for this type of request. For more information, see [Check Transaction Events](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-txn-resp-async-api-intro/sis-pymnt-svcs-cloud-check-txn-events-intro.md "").  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions/async`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions/async`

Receive Transaction Responses Asynchronously {#sis-pymnt-svcs-cloud-txn-resp-async-api-task}
============================================================================================

Asynchronous endpoints can be used to receive transaction responses for most types of transaction requests when the app is in Cloud mode.  
Follow these steps to receive transaction responses asynchronously:

1. Use the asynchronous endpoints shown in the example to process a transaction and receive an interaction identifier. The example shows how to process a sale asynchronously.
2. After the transaction is completed, use the interaction identifier returned in the response to check the transaction events and to get a transaction identifier.
3. Use the transaction identifier to process a Check Transaction Status request. The response will contain full transaction and receipt details. For more information, see [Requesting a Check Transaction Status](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-txn-status-api-intro.md "").

REST Example: Receive Transaction Responses Asynchronously {#sis-pymnt-svcs-cloud-txn-resp-async-sale-api-ex-rest}
==================================================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "PaymentRequest",
        "merchantReferenceCode": "058ed6c3430e436dab91b782f4113fd2",
        "amountDetails": {
            "amount": "1.00",
            "currency": "GBP"
        }
    }
}
```

Response to a Successful Request

```
{
    "interactionId": "0c292d7f-6bf9-460c-afc3-d75c189f2f99"
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Check Transaction Events {#sis-pymnt-svcs-cloud-check-txn-events-intro}
=======================================================================

Use this information to process a Check Transaction Events request when the app is in Cloud mode. This type of request is a follow-on service for receiving transaction responses asynchronously. For more information, see [Receiving Transaction Responses Asynchronously](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-txn-resp-async-api-intro.md "").  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

The GET request must include the interaction identifier (`interactionId`).  
**Test:** `GET https://terminalstest.cybersource.com/v1/cloud/interactions/{interactionId}/events`  
**Production:** `GET https://terminals.cybersource.com/v1/cloud/interactions/{interactionId}/events`

Required Fields to Check Transaction Events {#sis-pymnt-svcs-cloud-check-txn-events-reqfields}
==============================================================================================

The body of the API request is empty. The GET request must include the information required to return the response. If you want to receive only the latest transaction event, set a query parameter of `limit=1`.

REST Example: Check Transaction Events {#sis-pymnt-svcs-cloud-check-txn-events-api-ex-rest}
===========================================================================================

Request  
The body of the request is empty. The GET request includes the information required to return the response.

```
{
}
```

Response to a Successful Request

```
{
    "interactionId": "0c292d7f-6bf9-460c-afc3-d75c189f2f99",
    "transactionEvents": [
        {
            "type": "PaymentResponse",
            "message": "Payment approved",
            "transactionId": "c9f966ef0e0e4a9186c0cfb75c90841a",
            "createdAt": "2024-05-28 13:11:30:939"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "Payment approved",
            "createdAt": "2024-05-28 13:11:30:556"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "Processing payment...",
            "createdAt": "2024-05-28 13:11:28:928"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "1.00 GBP - Present card",
            "createdAt": "2024-05-28 13:11:28:093"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "1.00 GBP - Present card",
            "createdAt": "2024-05-28 13:11:27:439"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "1.00 GBP - Present card",
            "createdAt": "2024-05-28 13:11:27:217"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "Registering transaction",
            "createdAt": "2024-05-28 13:11:27:022"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "Registering transaction",
            "createdAt": "2024-05-28 13:11:26:485"
        },
        {
            "type": "TransactionStatusResponse",
            "message": "Connecting to card reader",
            "createdAt": "2024-05-28 13:11:24:649"
        },
        {
            "type": "AcknowledgementResponse",
            "createdAt": "2024-05-28 13:11:23:823"
        }
    ]
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Electronic Benefits Transfer {#sis-pymnt-svcs-cloud-ebt-intro}
==============================================================

Public assistance programs in the United States use Electronic Benefits Transfer (EBT) payment cards to issue monthly food and cash benefits to eligible people. EBT cards function like prepaid debit cards that can be used at authorized retailers. Food benefits are issued through the Supplemental Nutrition Assistance Program (SNAP), which helps people with low incomes purchase eligible food items.  
Use this information to process EBT SNAP (food benefits) and EBT Cash transactions when the app is in Cloud mode.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for Electronic Benefits Transfer {#sis-pymnt-svcs-cloud-ebt-reqfields}
======================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PaymentRequest` for a sale or to `StandaloneRefundRequest` for a stand-alone credit.

request.merchantReferenceCode
:
Set the value to a unique, user-defined reference code. The code can consist of up to 50 alphanumeric characters, underscores (_), and dashes (-). Avoid using formatting that resembles a telephone number (XXX-XXX-XXXX) or a Social Security number (XXX-XX-XXXX).

request.amountDetails.amount
:
Set the value to the transaction amount.

request.amountDetails.currency
:
Set the value to the currency code.

request.paymentMode
:
Set the value to `EBT`.

request.ebtDetails.category
:
Set the value to `FOOD` for EBT SNAP and `CASH` for EBT Cash.

Optional Fields for Electronic Benefits Transfer {#sis-pymnt-svcs-cloud-ebt-optfields}
======================================================================================

request.ebtDetails.isBalanceInquiry
:
Set the value to `true` for a balance inquiry. The transaction amount must be set to `0`.

request.ebtDetails.isVoucher
:
Set the value to `true` for a voucher transaction.

request.amountDetails.cashbackAmount
:
Set the value to the cashback amount for a cashback transaction.

REST Example: Electronic Benefits Transfer SNAP Sale {#sis-pymnt-svcs-cloud-ebt-ex-rest}
========================================================================================

Request

```
{
   "serialNumber": "1850000000",
   "request": 
       {
       "type" : "PaymentRequest",
       "merchantReferenceCode" : "82910b8b430a414dbe224e4494545b02",
       "paymentMode" : "EBT",
       "amountDetails" : {
         "amount" : "1.00",
         "currency" : "USD"
       },
       "ebtDetails" : {
         "category" : "FOOD"
       }
    }
}
```

Response to a Successful Request

```
{
  "type" : "PaymentResponse",
  "message" : "Payment approved",
  "transactionDetails" : {
    "id" : "bd9c4ddd5bb84aafa42f16f2660f76c7",
    "merchantReferenceCode" : "82910b8b430a414dbe224e4494545b02",
    "submitTimeUtc" : "2025-09-29T09:04:02+0000",
    "captured" : true,
    "amountDetails" : {
      "currency" : "USD",
      "amount" : "1.00",
      "capturedAmount" : "1.00",
      "refundableAmount" : "1.00"
    }
  },
  "processingDetails" : {
    "status" : "APPROVED",
    "verificationMethod" : "PIN",
    "entryMode" : "MAGNETIC_STRIPE",
    "card" : {
      "expirationMonth" : "00",
      "expirationYear" : "00",
      "type" : "EBT",
      "maskedPan" : "507719XXXXXX4720"
    }
  },
  "additionalInformation" : {
    "requestId" : "7591366618376609904603"
  },
  "linkedOperations" : [ ],
  "tipAdjustStatus" : "NOT_ADJUSTABLE",
  "receipts" : {
    "merchantReceipt" : {
      "preformattedReceipt" : "Merchant Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n555555555\n\nPayment\n$1.00\n\nPlease retain receipt!\n\nCard: EBT\nAccount: **** **** **** 4720\nEntry Mode: Magstripe\nVerification: Verified by PIN\n\nTransaction: 673579\nAuthorization: 831000\nMerchant ID: ******************nt001\nTerminal ID: ****1459\n\n\nbd9c4ddd5bb84aafa42f16f2660f76c7\n\n2:34:22 PM: 9/29/2025\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "555555555"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "EBT"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 4720"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Magstripe"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "Verified by PIN"
          },
          "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
            "label" : "Transaction",
            "value" : "673579"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "831000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "******************nt001"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****1459"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Merchant Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Payment"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "bd9c4ddd5bb84aafa42f16f2660f76c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$1.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "9/29/2025"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "2:34:22 PM"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    },
    "customerReceipt" : {
      "preformattedReceipt" : "Cardholder Receipt\nCP Test\nSample Street\n55555 New York\nUnited States\n555555555\n\nPayment\n$1.00\n\nPlease retain receipt!\n\nCard: EBT\nAccount: **** **** **** 4720\nEntry Mode: Magstripe\nVerification: Verified by PIN\n\nTransaction: 673579\nAuthorization: 831000\nMerchant ID: ******************nt001\nTerminal ID: ****1459\n\n\nbd9c4ddd5bb84aafa42f16f2660f76c7\n\n2:34:22 PM: 9/29/2025\n\n\n",
      "receiptData" : {
        "lines" : {
          "MERCHANT_DETAILS_PUBLIC_NAME" : {
            "label" : "Name",
            "value" : "CP Test"
          },
          "MERCHANT_DETAILS_ADDRESS" : {
            "label" : "Address",
            "value" : "Sample Street"
          },
          "MERCHANT_DETAILS_ZIP" : {
            "label" : "Zip",
            "value" : "55555"
          },
          "MERCHANT_DETAILS_CITY" : {
            "label" : "City",
            "value" : "New York"
          },
          "MERCHANT_DETAILS_COUNTRY" : {
            "label" : "Country",
            "value" : "United States"
          },
          "MERCHANT_DETAILS_CONTACT" : {
            "label" : "Contact",
            "value" : "555555555"
          },
          "MERCHANT_DETAILS_ADDITIONAL_INFORMATION" : {
            "label" : "Additional Information",
            "value" : ""
          },
          "PAYMENT_DETAILS_SCHEME_OR_LABEL" : {
            "label" : "Card",
            "value" : "EBT"
          },
          "PAYMENT_DETAILS_MASKED_ACCOUNT" : {
            "label" : "Account",
            "value" : "**** **** **** 4720"
          },
          "PAYMENT_DETAILS_SOURCE" : {
            "label" : "Entry Mode",
            "value" : "Magstripe"
          },
          "PAYMENT_DETAILS_CUSTOMER_VERIFICATION" : {
            "label" : "Verification",
            "value" : "Verified by PIN"
          },
          "CLEARING_DETAILS_TRANSACTION_IDENTIFIER" : {
            "label" : "Transaction",
            "value" : "673579"
          },
          "CLEARING_DETAILS_AUTHORIZATION_CODE" : {
            "label" : "Authorization",
            "value" : "831000"
          },
          "CLEARING_DETAILS_MERCHANT_IDENTIFIER" : {
            "label" : "Merchant ID",
            "value" : "******************nt001"
          },
          "CLEARING_DETAILS_TERMINAL_ID" : {
            "label" : "Terminal ID",
            "value" : "****1459"
          },
          "RECEIPT_TYPE" : {
            "label" : "Receipt Type",
            "value" : "Cardholder Receipt"
          },
          "TRANSACTION_TYPE" : {
            "label" : "Type",
            "value" : "Payment"
          },
          "SUBJECT" : {
            "label" : "Description",
            "value" : ""
          },
          "IDENTIFIER" : {
            "label" : "PWID",
            "value" : "bd9c4ddd5bb84aafa42f16f2660f76c7"
          },
          "AMOUNT_AND_CURRENCY" : {
            "label" : "Amount",
            "value" : "$1.00"
          },
          "DATE" : {
            "label" : "Date",
            "value" : "9/29/2025"
          },
          "TIME" : {
            "label" : "Time",
            "value" : "2:34:22 PM"
          },
          "STATUS_TEXT" : {
            "label" : "Information",
            "value" : "Please retain receipt!"
          }
        },
        "signatureLineRequired" : false,
        "tipLineRequired" : false,
        "totalLineRequired" : false
      }
    }
  },
  "ebtDetails" : {
    "category" : "FOOD"
  }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
   "type": "ErrorResponse",
   "message": "Error message to display.",
   "developerDescription": "Detailed description of error."
   }
```

Custom Card Read {#sis-pymnt-svcs-cloud-custom-card-card-intro}
===============================================================

Use this information to obtain data from custom cards such as gift cards, loyalty program cards, and employee cards when the app is in Cloud mode. This service cannot be used to perform payment functions.
IMPORTANT Custom Card Read is supported for non-PCI cards only. To use this service, the card type must be on your allowlist. To add a card type to your allowlist, contact your implementation manager.  
To retrieve the card data, swipe the card's magnetic stripe through the payment device. The custom card read-only function reads and returns the raw card identifier to your app or point-of-sale (POS) system. You can then use the raw data within your app or POS system.  
These are examples of how you might use the Custom Card Read feature:

* **Custom gift card:** Use the card number to check a balance or process a payment in your private gift card network.
* **Employee card:** Use the card number to look up an employee's profile or account.
  {#sis-pymnt-svcs-cloud-custom-card-card-intro_ul_snq_dyx_xgc}  
  Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for a Custom Card Read {#sis-pymnt-svcs-cloud-custom-card-read-api-reqfields}
=============================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `ReadCardRequest`.

REST Example: Custom Card Read {#sis-pymnt-svcs-cloud-custom-card-read-ex-rest}
===============================================================================

Request

```
{
  "serialNumber": "1850000000",
  "request": {
    "type": "ReadCardRequest"
  }
}
```

Response to a Successful Request

```
{
   "type": "ReadCardResponse",
   "message": "Read Card Successfully",
   "cardDetails": {
     "expiryMonth": 12,
     "expiryYear": 2025,
     "track1": "%B4111111111111111^DOE/JOHN^2512101?",
     "track2": "4111111111111111=25121010000?",
     "cardNumber": "4111111111111111"
   }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
   "type": "ErrorResponse",
   "message": "Error message to display.",
   "developerDescription": "Detailed description of error."
}
```

Printing a Customer or Merchant Receipt {#sis-pymnt-svcs-cloud-receipt-print-intro}
===================================================================================

Use this information to print a customer or merchant receipt from a previous transaction when the app is in Cloud mode. This feature can be used only with terminals that have integrated printers.  
Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields to Print a Customer or Merchant Receipt {#sis-pymnt-svcs-cloud-receipt-print-reqfield}
======================================================================================================

serialNumber
:
Set the value to the serial number of the terminal.

request.type
:
Set the value to `PrintReceiptRequest`.

request.transactionId
:
Set the value to the ID field value from the original transaction.

request.receiptType
:
Set the value to CUSTOMER or MERCHANT.

REST Example: Print a Customer or Merchant Receipt {#sis-pymnt-svcs-cloud-receipt-print-ex-rest}
================================================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "PrintReceiptRequest",
        "transactionId": "8fe5fa21d0814424bcec4997c9dc89c4",
        "receiptType": "CUSTOMER"
    }
}
```

Response to a Successful Request

```
{
    "type": "PrintReceiptResponse",
    "message": "Receipt printed successfully."
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
    "type": "ErrorResponse",
    "message": "Error message to display.",
    "developerDescription": "Detailed description of error."
}
```

Custom Printing {#sis-pymnt-svcs-cloud-custom-print-intro}
==========================================================

Use this information to send a custom print request in Cloud mode. This feature enables you to print custom content directly to the integrated printer of a PAX terminal, including text, label-value pairs, images, barcodes, and QR codes.

> IMPORTANT  
> The Custom Printing feature does not affect your configuration for printing standard customer or merchant receipts.  
> Generate a bearer token before sending each request. For more information, see [Generating a Bearer Token for Authentication](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro/sis-pymnt-svcs-cloud-mode-bearer-tkn-intro.md "").

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for Custom Printing {#sis-pymnt-svcs-cloud-custom-print-reqfields}
==================================================================================

serialNumber
:
Set this field to the serial number of the terminal.

request.type
:
Set this field to `CustomPrintRequest`.

request.printLayout.sections
:
Set this field to a list of one or more print sections. Each section must include a sectionType field to identify the type of custom content to print.

Required Fields for Custom Printing by Section Type {#sis-pymnt-svcs-cloud-custom-print-sec-type-reqfields}
===========================================================================================================

Use these fields to define the required content for each custom print section in the request.printLayout.sections field. Each section in this field must include a sectionType field that identifies the type of content to print. The request.printLayout.sections field supports these sectionType values: `TEXT`, `BARCODE`, `IMAGE`, and `SPACER`. These values are case sensitive.

TEXT Section
------------

request.printLayout.sections\[n\].sectionType
:
Set this field to `TEXT`.

request.printLayout.sections\[n\].textContent.textType
:
Set this field to identify the type of text content. Supported values are `PARAGRAPH`, `LABEL_VALUE`, and `NO_LINE`.

TEXT Section: PARAGRAPH Text Content Required Fields
----------------------------------------------------

request.printLayout.sections\[n\].textContent.lines
:
Set this field to a list of one or more strings to print as paragraph lines.

TEXT Section: LABEL_VALUE Text Content Required Fields
------------------------------------------------------

request.printLayout.sections\[n\].textContent.content
:
Set this field to a list of one or more label-value pairs.

request.printLayout.sections\[n\].textContent.content\[n\].label.labelText
:
Set this field to the label text string.

request.printLayout.sections\[n\].textContent.content\[n\].value.valueText
:
Set this field to the value text string.

BARCODE Section
---------------

request.printLayout.sections\[n\].sectionType
:
Set this field to `BARCODE`.

request.printLayout.sections\[n\].content
:
Set this field to the data to encode in the barcode.

request.printLayout.sections\[n\].barcodeType
:
Set this field to the barcode format. Supported values are `CODE39`, `CODE128`, `EAN13`, `EAN128`, `PDF417`, and `QRCODE`.

IMAGE Section
-------------

request.printLayout.sections\[n\].sectionType
:
Set this field to `IMAGE`.

request.printLayout.sections\[n\].imageData
:
Set this field to a Base64-encoded image. Supported formats are `PNG`, `JPEG`, and `BMP`. The maximum image width and height is 384 pixels.

SPACER Section
--------------

request.printLayout.sections\[n\].sectionType
:
Set this field to `SPACER`.

Optional Fields for Custom Printing {#sis-pymnt-svcs-cloud-custom-print-optfields}
==================================================================================

Use these fields to define optional content and formatting for custom print sections in the request.printLayout.sections field. Optional fields are supported for `TEXT` and `SPACER` sections.

> IMPORTANT  
> If you do not specify the value for an optional field, the default value is used.

TEXT Section: PARAGRAPH Optional Fields
---------------------------------------

request.printLayout.sections\[n\].textContent.align
:
Set this field to `LEFT`, `CENTER`, or `RIGHT`. The default value is `LEFT`.

request.printLayout.sections\[n\].textContent.textStyle.size
:
Set this field to `SMALL`, `MEDIUM`, or `LARGE`. The default value is `MEDIUM`.

request.printLayout.sections\[n\].textContent.textStyle.style
:
Set this field to `NORMAL` or `EMPHASIZE`. The default value is `NORMAL`.

TEXT Section: LABEL_VALUE Optional Fields
-----------------------------------------

request.printLayout.sections\[n\].textContent.content\[n\].label.textStyle.size
:
Set this field to `SMALL`, `MEDIUM`, or `LARGE`. The default value is `MEDIUM`.

request.printLayout.sections\[n\].textContent.content\[n\].label.textStyle.style
:
Set this field to `NORMAL` or `EMPHASIZE`. The default value is `NORMAL`.

request.printLayout.sections\[n\].textContent.content\[n\].value.textStyle.size
:
Set this field to `SMALL`, `MEDIUM`, or `LARGE`. The default value is `MEDIUM`.

request.printLayout.sections\[n\].textContent.content\[n\].value.textStyle.style
:
Set this field to `NORMAL` or `EMPHASIZE`. The default value is `NORMAL`.

SPACER Section Optional Fields
------------------------------

request.printLayout.sections\[n\].lines
:
Set this field to the number of blank lines to insert. The default value is `1`.

REST Example: Custom Printing {#sis-pymnt-svcs-cloud-custom-print-ex-rest}
==========================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "CustomPrintRequest",
        "printLayout": {
            "sections": [
                {
                    "sectionType": "TEXT",
                    "textContent": {
                        "textType": "PARAGRAPH",
                        "lines": ["ACME STORE", "123 Main St"],
                        "align": "CENTER",
                        "textStyle": {
                            "size": "LARGE",
                            "style": "NORMAL"
                        }
                    }
                },
                {
                    "sectionType": "IMAGE",
                    "imageData": "iVBORw0KGgoAAAANS..."
                },
                {
                    "sectionType": "SPACER",
                    "lines": 1
                },
                {
                    "sectionType": "TEXT",
                    "textContent": {
                        "textType": "LABEL_VALUE",
                        "content": [
                            {
                                "label": {
                                    "labelText": "Subtotal",
                                    "textStyle": { "size": "MEDIUM", "style": "NORMAL" }
                                },
                                "value": {
                                    "valueText": "$23.45",
                                    "textStyle": { "size": "MEDIUM", "style": "NORMAL" }
                                }
                            },
                            {
                                "label": {
                                    "labelText": "Total",
                                    "textStyle": { "size": "LARGE", "style": "NORMAL" }
                                },
                                "value": {
                                    "valueText": "$25.99",
                                    "textStyle": { "size": "LARGE", "style": "NORMAL" }
                                }
                            }
                        ]
                    }
                },
                {
                    "sectionType": "BARCODE",
                    "content": "TXN123456789",
                    "barcodeType": "CODE128"
                }
            ]
        }
    }
}
```

Response to a Successful Request

```
{
    "type": "CustomPrintResponse",
    "message": "Custom Print successfully"
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
      "type": "ErrorResponse",
      "message": "Error message to display.",
      "developerDescription": "Detailed description of error."
}
```

Custom Screens {#sis-pymnt-svcs-cloud-custom-screens-intro}
===========================================================

Use this information to send a custom screen request in Cloud mode. This feature enables you to show one or more customized screens on the payment terminal. Custom screen can show informational text, collect text input, or capture a digital signature.

Endpoints
---------

**Test:** `POST https://terminalstest.cybersource.com/v1/cloud/transactions`  
**Production:** `POST https://terminals.cybersource.com/v1/cloud/transactions`

Required Fields for Custom Screens {#sis-pymnt-svcs-cloud-custom-screens-reqfields}
===================================================================================

serialNumber
:
Set this field to the serial number of the terminal.

request.type
:
Set this field to `CustomScreenRequest`.

request.screens
:
Set this field to a list of one or more screen objects. Each screen must include a screenType field to identify the type of custom screens to show on the payment terminal.

Required Fields for Custom Screens by Screen Type {#sis-pymnt-svcs-cloud-custom-screens-type-reqfields}
=======================================================================================================

Use these fields to define the required content for each custom screen in the request.screens field. Each screen in this field must include a screenType field that identifies the type of custom screen to show on the payment terminal. The request.screens field supports these screenType values: `textDisplay`, `textInput`, and `signatureCapture`.

textDisplay Screen
------------------

request.screens\[n\].screenType
:
Set this field to `textDisplay`.

request.screens\[n\].title
:
Set this field to the screen title. The title cannot exceed 20 characters.

textInput Screen
----------------

request.screens\[n\].screenType
:
Set this field to `textInput`.

request.screens\[n\].title
:
Set this field to the screen title. The title cannot exceed 20 characters.

request.screens\[n\].textInputs
:
Set this field to a list of one or more text input fields.

request.screens\[n\].textInputs\[n\].textInputLabel
:
Set this field to the label for the input field. The label cannot exceed 25 characters.

request.screens\[n\].textInputs\[n\].textInputConfig.textInputType
:
Set this field to the type of input to accept. Supported values are `NUMERIC`, `ALPHANUMERIC`, `EMAIL`, and `PHONE`.

signatureCapture Screen
-----------------------

request.screens\[n\].screenType
:
Set this field to `signatureCapture`.

request.screens\[n\].title
:
Set this field to the screen title. The title cannot exceed 20 characters.

Optional Fields for Custom Screens {#sis-pymnt-svcs-cloud-custom-screens-optfields}
===================================================================================

Use these fields to define optional content and formatting for custom screens in the request.screens field. Optional fields are available for all screen types, with additional optional fields supported for textDisplay and textInput screens.

> IMPORTANT  
> If you do not specify the value for an optional field, the default value is used.

Optional Fields Available on All Screen Types
---------------------------------------------

request.screens\[n\].description
:
Set this field to a descriptive message displayed below the title.

request.screens\[n\].isSkippable
:
Set this field to `true` to allow the cardholder to skip the screen. The default value is `false`.

textDisplay Screen Optional Fields
----------------------------------

request.screens\[n\].toggles
:
Set this field to a list of toggle items for the cardholder to accept or decline.

request.screens\[n\].toggles\[n\].label
:
Set this field to the label displayed next to the toggle. The label cannot exceed 40 characters.

request.screens\[n\].toggles\[n\].required
:
Set this field to `true` to require the cardholder to enable the toggle before proceeding. The default value is `false`.

textInput Screen Optional Fields
--------------------------------

request.screens\[n\].textInputs\[n\].textInputHint
:
Set this field to placeholder hint text displayed inside the input field.

request.screens\[n\].textInputs\[n\].textInputConfig.masked
:
Set this field to `true` to mask the input characters as the cardholder types. The default value is `false`.

request.screens\[n\].textInputs\[n\].textInputConfig.length.min
:
Set this field to the minimum number of characters required. Must be greater than zero.

request.screens\[n\].textInputs\[n\].textInputConfig.length.max
:
Set this field to the maximum number of characters allowed. Must be greater than zero and not less than the defined minimum number of characters

request.screens\[n\].textInputs\[n\].textInputConfig.patternConfig.pattern
:
Set this field to a regular expression that the input value must match.

request.screens\[n\].textInputs\[n\].textInputConfig.patternConfig.patternError
:
Set this field to the error message displayed when the input does not match the pattern.

request.screens\[n\].toggles
:
Set this field to a list of toggle items for the cardholder to accept or decline.

request.screens\[n\].toggles\[n\].label
:
Set this field to the label displayed next to the toggle. The label cannot exceed 40 characters.

request.screens\[n\].toggles\[n\].required
:
Set this field to `true` to require the cardholder to enable the toggle before proceeding. The default value is `false`.

REST Example: Custom Screens {#sis-pymnt-svcs-cloud-custom-screens-ex-rest}
===========================================================================

Request

```
{
    "serialNumber": "1850000000",
    "request": {
        "type": "CustomScreenRequest",
        "screens": [
            {
                "screenType": "signatureCapture",
                "title": "Confirm Receipt",
                "description": "I certify that I am the authorized representative to receive these goods...",
                "isSkippable": false
            },
            {
                "screenType": "textDisplay",
                "title": "Liability Waiver",
                "description": "By proceeding, you acknowledge inspection of goods...",
                "isSkippable": false,
                "toggles": [
                    {
                        "label": "I accept the terms",
                        "required": true
                    }
                ]
            },
            {
                "screenType": "textInput",
                "title": "Purchase Order (PO)",
                "description": "Please enter the authorized Purchase Order (PO) number...",
                "isSkippable": false,
                "textInputs": [
                    {
                        "textInputLabel": "Authorized PO Number",
                        "textInputHint": "PO518736",
                        "textInputConfig": {
                            "textInputType": "ALPHANUMERIC",
                            "masked": true,
                            "length": {
                                "min": 5,
                                "max": 10
                            },
                            "patternConfig": {
                                "pattern": "^[a-zA-Z0-9]*$",
                                "patternError": "Only letters and numbers allowed"
                            }
                        }
                    }
                ],
                "toggles": [
                    {
                        "label": "I accept the terms",
                        "required": true
                    }
                ]
            }
        ]
    }
}
```

Response to a Successful Request

```
{
    "type": "CustomScreenResponse",
    "message": "Data capture successful",
    "customScreenDetails": {
        "status": "COMPLETED",
        "screens": [
            {
                "screenType": "signatureCapture",
                "title": "Confirm Receipt",
                "signatureData": "iVBORw0KGgoAAAANSUhEUg....",
                "skipped": false
            },
            {
                "screenType": "textDisplay",
                "title": "Liability Waiver",
                "toggles": [
                    {
                        "label": "I accept the terms",
                        "value": true
                    }
                ],
                "skipped": false
            },
            {
                "screenType": "textInput",
                "title": "Purchase Order (PO)",
                "inputs": [
                    {
                        "label": "Authorized PO Number",
                        "value": "PO518736"
                    }
                ],
                "toggles": [
                    {
                        "label": "I accept the terms",
                        "value": true
                    }
                ],
                "skipped": false
            }
        ]
    }
}
```

Response to an Unsuccessful Request  
When the request is unsuccessful, you receive an error response with details.

```
{
          "type": "ErrorResponse",
          "message": "Error message to display.",
          "developerDescription": "Detailed description of error."
    }
```

Standalone Mode Payment Services {#sis-pymnt-svcs-standalone-mode-intro}
========================================================================

Use this information to process payment services available in the Acceptance Devices app when operated in Standalone mode.  
These are some benefits of using Standalone mode:

* You can start transactions directly from the terminal.

* This mode is the fastest way to begin accepting payments.

* There is no integration required when using this mode with a point-of-sale (POS) system.

* Use this mode as a backup option when your POS system is unavailable for Local or Cloud semi-integrated modes.
  {#sis-pymnt-svcs-standalone-mode-intro_ul_f1b_dhp_vzb}
  IMPORTANT When the Acceptance Devices app is in Standalone mode, the terminal does not communicate with your POS system to exchange transaction details. You are responsible for reconciling transactions with your internal systems and records.  
  For information about other modes available in the Acceptance Devices app, see:

* [Local Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-pymnt-svcs-intro.md "")

* [Cloud Mode Payment Services](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-cloud-mode-intro.md "")
  {#sis-pymnt-svcs-standalone-mode-intro_ul_l5b_yqm_3fc}

Enable Standalone Mode in the Acceptance Devices App {#sis-standalone-mode-enable}
==================================================================================

Follow these steps to enable Standalone mode in the Acceptance Devices app:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Standalone Mode.
4. Toggle Enable Standalone Mode to ON.
5. Choose the currency in which you want to process transactions. Tap Save.
6. If you want to enable custom merchant reference codes, toggle Custom Transaction Reference to ON.
7. Tap the back navigation arrow to return to the home screen. You can now process transactions in Standalone mode.

Sale {#sis-standalone-mode-sale}
================================

Use this information to process a sale transaction when the app is in Standalone mode. This type of transaction combines an authorization and a capture into a single transaction.  
Follow these steps to process a sale transaction:

1. In the Acceptance Devices app, tap Sale.
2. Enter the transaction amount.
3. Tap Submit to start the transaction.

Refund {#sis-standalone-mode-refund}
====================================

Use this information to process a refund when the app is in Standalone mode. This type of refund includes a reference to the original transaction for a full or partial transaction amount.  
Stand-alone credits are also supported in this Acceptance Devices solution. For more information, see [Stand-Alone Credit](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro/sis-standalone-mode-standalone-credit.md "").  
Follow these steps to process a refund:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Transaction History.
4. Tap the transaction you want to refund.
5. Enter the transaction amount.
6. Tap Refund to start the transaction.

Stand-Alone Credit {#sis-standalone-mode-standalone-credit}
===========================================================

Use this information to process a stand-alone credit when the app is in Standalone mode. This type of transaction is used to process a credit without reference to the original transaction. The customer is required to present their card for this type of transaction.

> WARNING
> When processing a stand-alone credit, there is no limit on the credit amount because there is no reference to the original transaction amount. The recommendation is to use a refund transaction whenever possible. For more information, see [Refund](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro/sis-standalone-mode-refund.md "").  
> Follow these steps to process a stand-alone credit:

1. In the Acceptance Devices app, tap Other Transactions.
2. Tap Refund.
3. Enter your Acceptance Devices app passcode.
4. Enter the transaction amount.
5. Tap Submit to start the transaction.

Sale with On-Reader Tipping {#sis-standalone-mode-sale-on-reader-tip}
=====================================================================

Use this information to process a sale with on-reader tipping in Standalone mode. At the start of each transaction, the terminal prompts the customer to add a tip by showing suggested tip amounts. The customer selects or enters a tip amount on the terminal before presenting their payment card.  
Follow these steps to process a sale with on-reader tipping:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Standalone Mode.
4. Toggle Ask for Tip to ON.
5. Tap the back navigation arrow to return to the home screen.
6. Tap Sale.
7. Enter the transaction amount.
8. Tap Submit to start the transaction.

Pre-Authorization {#sis-standalone-mode-pre-auth}
=================================================

Use this information to process a pre-authorization for an initial amount in Standalone mode. A pre-authorization transaction places a temporary hold on the customer's payment card. The transaction amount can be captured at a later time.  
Most authorizations expire in 5 to 7 days. The issuing bank sets the length of time before expiration. When an authorization expires with the issuing bank, your bank or processor might require you to re-submit an authorization request and include a request for capture in the same message. For more information, see [Capture](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro/sis-standalone-mode-capture.md "").  
Follow these steps to process a pre-authorization:

1. In the Acceptance Devices app, tap Other Transactions.
2. Tap Pre-Authorization.
3. Enter the transaction amount.
4. Tap Submit to start the transaction.

Capture {#sis-standalone-mode-capture}
======================================

Use this information to capture a pre-authorized transaction in Standalone mode. The capture request references the approved pre-authorization request.  
Follow these steps to process a capture:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Transaction History.
4. Tap the transaction you want to capture.
5. Tap Capture.
6. Enter the transaction amount.
7. Tap Capture to start the transaction.

Mail Order or Telephone Order Sale {#sis-standalone-mode-moto-sale}
===================================================================

Use this information to process a mail order or telephone order (MOTO) sale in Standalone mode. The payment card is not physically tapped, inserted, or swiped in the terminal for a MOTO transaction.  
Follow these steps to process a MOTO sale:

1. In the Acceptance Devices app, tap Other Transactions.
2. Tap MOTO.
3. Enter the transaction amount.
4. Tap Submit to start the transaction.

Account Verification {#sis-standalone-mode-acct-verif}
======================================================

Use this information to process an account verification when the app is in Standalone mode. The account verification transaction submits a zero-amount authorization request to validate the payment card.  
Follow these steps to process an account verification:

1. In the Acceptance Devices app, tap Other Transactions.
2. Tap Account Verification to start the transaction.

Offline Transactions {#sis-standalone-mode-offline-txn-intro}
=============================================================

Offline mode is a feature that you can enable and customize in the `Business Center`. The default setting is `Disabled`. For more information, see [Customizing the Acceptance Devices App](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/semi-integrated-solution-pax-get-started-intro/sis-ad-app-customize-intro.md "").

> WARNING
> By using this feature, you assume the risk of failed transactions and the possibility of increased fraud and chargebacks. Process transactions offline only when required such as during an internet outage. Whenever possible, process transactions online instead. For more information, see [Sale](/docs/cybs/en-us/sis-pax/integration/all/rest/sis-pax/sis-pymnt-svcs-standalone-mode-intro/sis-standalone-mode-sale.md "").  
> When an internet connection is available, submit the offline transactions batch for authorization while in Offline mode.  
> Use this information to enable and disable Offline mode when the app is in Standalone mode. When an internet connection is not available, you can use this mode to process offline sale and refund transactions.

Enable or Disable Offline Mode {#sis-standalone-mode-offline-txn-enable-disable}
================================================================================

IMPORTANT The recommendation is to resume operating in online mode as soon as an internet connection is available. To do so, you must first disable Offline mode.  
Follow these steps to enable or disable Offline mode.

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Offline Mode.
4. Toggle Enable Offline Mode to ON or OFF.
5. Tap the back navigation arrow to return to the home screen.

Offline Sale {#sis-standalone-mode-offline-txn-sale}
====================================================

Follow these steps to process an offline sale with Offline mode enabled:

1. In the Acceptance Devices app, tap Sale.
2. Enter the transaction amount.
3. Tap Submit to start the transaction.

Offline Refund {#sis-standalone-mode-offline-txn-refund}
========================================================

Follow these steps to process an offline refund with Offline mode enabled:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Offline Mode.
4. Tap the transaction you want to refund.
5. Tap Refund.
6. Enter the transaction amount.
7. Tap Refund to start the transaction.

Submit an Offline Transactions Batch for Authorization {#sis-standalone-mode-offline-txn-batch-auth}
====================================================================================================

IMPORTANT The recommendation is to submit the batch as soon as an internet connection is available. Offline mode must be enabled before you can submit a batch for authorization.  
Follow these steps to submit an offline transactions batch for authorization with Offline mode enabled:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Offline Mode.
4. Tap Submit Offline Batch.

Sale with Installment Details {#sis-standalone-mode-sale-install-details}
=========================================================================

Use this information to process a sale transaction with installment details when the app is in Standalone mode. This payment service enables you to include the required installment details as part of the sale transaction.

> IMPORTANT  
> This transaction is available only in the Latin American and Caribbean (LAC) region.  
> Follow these steps to process a sale transaction with installment details:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Standalone Mode.
4. Tap Installment Details.
5. Toggle Enable Installment Details to ON.
6. Configure the installment details.
7. Tap the back navigation arrow to return to the home screen.
8. Tap Sale.
9. Enter the transaction amount.
10. Tap Submit to start the transaction.

Sale with Payment Facilitator Details {#sis-standalone-mode-pymt-fac-details}
=============================================================================

Use the information to process a sale transaction with payment facilitator details when the app is in Standalone mode. This payment service enables you to include required payment facilitator details as part of the sale transaction.  
Follow these steps to process a sale transaction with payment facilitator details:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Standalone Mode.
4. Tap Payment Facilitator Details.
5. Toggle Enable Payment Facilitator Details to ON.
6. Configure the payment facilitator details.
7. Tap the back navigation arrow to return to the home screen.
8. Tap Sale.
9. Enter the transaction amount.
10. Tap Submit to start the transaction.

Sale with Tax Details {#sis-standalone-mode-sale-tax-details}
=============================================================

Use this information to process a sale transaction with tax details when the app is in Standalone mode. This type of transaction can be used to include the required tax details as part of the sale transaction.  
Follow these steps to process a sale transaction with tax details:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Standalone Mode.
4. Tap Tax Details.
5. Toggle Enable Tax Details to ON.
6. Configure the tax details.
7. Tap the back navigation arrow to return to the home screen.
8. Tap Sale
9. Enter the transaction amount.
10. Tap Submit to start the transaction.

Print a Customer or Merchant Receipt {#sis-standalone-mode-print-cust-merchant-recpt}
=====================================================================================

Use this information to print a customer or merchant receipt from a previous transaction when the app is in Standalone mode. This feature can only be used with terminals that have integrated printers.  
Follow these steps to print a customer or merchant receipt:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Transaction History.
4. Tap the transaction for which you want to email the receipt.
5. Tap Print Customer Receipt or Print Merchant Receipt.

Email a Customer Receipt {#sis-standalone-mode-email-cust-recpt}
================================================================

Use this information to email a customer receipt from a previous transaction when the app is in Standalone mode.  
Follow these steps to email a customer receipt:

1. In the Acceptance Devices app, tap Settings.
2. Enter your Acceptance Devices app passcode.
3. Tap Transaction History.
4. Tap the transaction for which you want to email the receipt.
5. Tap Send Receipt.

Release Notes for PAX Acceptance Devices App {#sis-release-notes-intro}
=======================================================================

These release notes are organized by release name and version, from newest to oldest.  
Each release note includes these details:

* Name of release
* Type of release: app or SDK
* Version number
* Operating system: Android or iOS
* Release date: MM-DD-YYYY format

These are the types of release notes published:


* General information
* Improvements
* New features
* Fixed issues
* Updated requirements
* Security updates
* Hot fixes

Acceptance Devices App Version 1.23.0 Release Notes {#sis-rel-notes-intro-ad-app-v123}
======================================================================================

These release notes are for the Acceptance Devices app, version 1.23.0 for Android. The app is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 06-24-2026.

Improvements {#sis-rel-notes-improve-ad-app-v123}
=================================================

* Added support for Kiosk Mode in Customization parameters.
* Updated the SDK version to 2.113.0.
  {#sis-rel-notes-improve-ad-app-v123_ul_xys_s1n_rjc}

Fixed Issues {#sis-rel-notes-fixes-ad-app-v123}
===============================================

Fixed an intermittent issue where Transaction History did not show recently completed transactions.

Acceptance Devices App Version 1.22.0 Release Notes {#sis-rel-notes-intro-ad-app-v122}
======================================================================================

These release notes are for the Acceptance Devices app, version 1.22.0 for Android. The app is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 05-07-2026.

Improvements {#sis-rel-notes-improve-ad-app-v122}
=================================================

Updated the SDK version to 2.112.0.

Fixed Issues {#sis-rel-notes-fixes-ad-app-v122}
===============================================

* Fixed an issue in Standalone mode where the Sales Slip Number and Merchant Tax ID fields were missing from the payment request for transactions without taxes.
* Fixed an issue that intermittently prevented Transaction History from displaying recently completed transactions.
* Applied general UI fixes.

Acceptance Devices App Version 1.21.0 Release Notes {#sis-rel-notes-intro-ad-app-v121}
======================================================================================

These release notes are for the Acceptance Devices app, version 1.21.0 for Android. The app is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 04-14-2026.

New Features {#sis-rel-notes-features-ad-app-v121}
==================================================

Added support for these devices and features:

* PAX A6650, A6630, A99, and A50 payment terminals.
* Meeza card type, Egypt's national payment scheme.
* Enabling Kiosk mode on PAX terminals.
* Spanish (Argentina) and Spanish (Mexico) language variants.
* Printing custom content when using PAX terminals with integrated printers.
* Displaying custom screens to show informational text, collect text input, or capture a digital signature.
* Providing lodging details during a transaction.

Improvements {#sis-rel-notes-improve-ad-app-v121}
=================================================

* The toolbar logo now appears on the Enter Amount screen when the app is in Standalone mode.
* On the PAX A35 payment terminal, pressing the Cancel button on the integrated PIN keypad no longer closes the AD app on the home screen.
* Applied general improvements to UI.
* Updated the SDK version to 2.111.0.

Acceptance Devices App Version 1.20.0 Release Notes {#sis-rel-notes-intro-ad-app-v120}
======================================================================================

These release notes are for the Acceptance Devices app, version 1.20.0 for Android. The app is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 03-12-2026.

New Features {#sis-rel-notes-features-ad-app-v120}
==================================================

* Tap to Pay: Added support for processing transactions in multiple currencies with a single device enrollment.
* Added support for configuring the maximum amount allowed for an offline transaction and the maximum amount allowed for an offline transaction batch submitted for authorization.

Improvements {#sis-rel-notes-improve-ad-app-v120}
=================================================

* Improved the user experience when performing a sale with tax details in Standalone mode.

{#sis-rel-notes-improve-ad-app-v120_ul_h12_lv3_33c}


* Updated the SDK version to 2.110.0.
  {#sis-rel-notes-improve-ad-app-v120_ul_g2s_lv3_33c}

Fixed Issues {#sis-rel-notes-fixes-ad-app-v120}
===============================================

* Fixed the issue that caused the app to close when the Back button was tapped on the Check Device screen.
* Applied general fixes to the UI.
  {#sis-rel-notes-fixes-ad-app-v120_ul_ns4_5w3_33c}

Archive of Release Notes {#sis-release-notes-archive-intro}
===========================================================

This archive of release notes for the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App is organized by release name and version, from newest to oldest. For more information, see the current release notes.  
Each release note includes these details:

* Name of release
* Type of release: app or SDK
* Version number
* Operating system: Android or iOS
* Release date: MM-DD-YYYY format

{#sis-release-notes-archive-intro_ul_qcb_lvk_k1c1}  
These are the types of release notes published:

* General information
* Improvements
* New features
* Fixed issues
* Updated requirements
* Security updates
* Hot fixes
  {#sis-release-notes-archive-intro_ul_l24_23q_h1c1}

Acceptance Devices App Version 1.18.0 Release Notes {#sis-rel-notes-intro-ad-app-v118}
======================================================================================

These release notes are for the Acceptance Devices app, version 1.18.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 12-11-2025.

New Features {#sis-rel-notes-features-ad-app-v118}
==================================================

* Added support for the PAX A3700 terminal.
* Added support for landscape mode on large-screen devices.
* Added the ability to enable and disable Offline mode from the POS system.

Improvements {#sis-rel-notes-improve-ad-app-v118}
=================================================

Updated the SDK version to 2.108.0.

Fixed Issues {#sis-rel-notes-fixes-ad-app-v118}
===============================================

Fixed an issue where EBT transactions failed when optional REST API fields were omitted.

Acceptance Devices App Version 1.17.0 Release Notes {#sis-rel-notes-intro-ad-app-v117}
======================================================================================

These release notes are for the Acceptance Devices app, version 1.17.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 10-28-2025.

New Features {#sis-rel-notes-features-ad-app-v117}
==================================================

* PAX: Added the ability to process Electronic Benefits Transfer (EBT) payment card transactions.
* PAX: Added the ability to read non-PCI custom magstripe cards such as gift cards and loyalty program cards.

Improvements {#sis-rel-notes-improve-ad-app-v117}
=================================================

* Improved the tax calculation logic when the app is operating in Standalone mode.
* Updated the SDK version to 2.106.0.
  {#sis-rel-notes-improve-ad-app-v117_ul_vnh_hbh_dhc}

Fixed Issues {#sis-rel-notes-fixes-ad-app-v117}
===============================================

Fixed the issue caused by using 10-digit transaction amounts with certain currencies in Standalone mode.

Acceptance Devices App Version 1.16.0 Release Notes {#sis-rel-notes-intro-ad-app-v116}
======================================================================================

These release notes are for the Acceptance Devices app, version 1.16.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 09-30-2025.

Improvements {#sis-rel-notes-improve-ad-app-v116}
=================================================

Updated the SDK version to 2.105.0.

Fixed Issues {#sis-rel-notes-fixes-ad-app-v116}
===============================================

Fixed the issue that caused users to be limited to entering only 7 digits for the transaction amount when using certain currencies in Standalone mode.

Acceptance Devices App Version 1.15.0 Release Notes {#sis-rel-notes-intro-ad-app-v115}
======================================================================================

These release notes are for the Acceptance Devices app, version 1.15.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 08-21-2025.

New Features {#sis-rel-notes-features-ad-app-v115}
==================================================

* Added the ability to configure the transaction history to show all transactions from the merchant or show only transactions from the device.
* Added the ability to customize user interface parameters.

Improvements {#sis-rel-notes-improve-ad-app-v115}
=================================================

Updated the SDK version to 2.103.1.

Fixed Issues {#sis-rel-notes-fixes-ad-app-v115}
===============================================

Tap to Pay: Fixed the issue that caused the app to occasionally crash after installing the Tap to Pay Ready app during the activation process.

Acceptance Devices App Version 1.14.0 Release Notes {#sis-rel-notes-intro-ad-app-v114}
======================================================================================

These release notes are for the Acceptance Devices app, version 1.14.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 07-07-2025.

New Features {#sis-rel-notes-features-ad-app-v114}
==================================================

Tap to Pay: The solution is now PCI-MPoC compliant, which requires the Tap to Pay Ready app to be installed on the Android devices used to process transactions. After upgrading to this version of the Acceptance Devices app, re-enroll your devices.

Improvements {#sis-rel-notes-improve-ad-app-v114}
=================================================

* Tap to Pay: The process used to select the currency in Standalone mode is now automated and based on the merchant configuration.
* Updated the SDK version to 2.102.0.

Acceptance Devices App Version 1.13.0 Release Notes {#sis-rel-notes-intro-ad-app-v113}
======================================================================================

These release notes are for the Acceptance Devices app, version 1.13.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 06-18-2025.

Improvements {#sis-rel-notes-improve-ad-app-v113}
=================================================

* Improved the reconnect mechanism when using the app in Cloud mode.
* Updated the SDK version to 2.101.1.

Acceptance Devices App Version 1.12.0 Release Notes {#sis-release-notes-intro-ad-app-v112}
==========================================================================================

These release notes are for the Acceptance Devices app, version 1.12.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 05-13-2025.

Improvements {#sis-release-notes-improve-ad-app-v112}
=====================================================

* Updated the UI to use Google Material Design 3.
* Updated the SDK version to 2.100.0.

Acceptance Devices App Version 1.11.0 Release Notes {#sis-release-notes-intro-ad-app-v111}
==========================================================================================

These release notes are for the Acceptance Devices app, version 1.11.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 04-14-2025.

Improvements {#sis-release-notes-improve-ad-app-v111}
=====================================================

* Improved the experience when using the app with the Arabic language.
* Tap to Pay: Improved the error messages that can appear during enrollment.
* Updated the SDK version to 2.99.0.

Fixed Issues {#sis-release-notes-bug-fixes-ad-app-v111}
=======================================================

Fixed the issue that caused the language not to change correctly when switching to Arabic.

Acceptance Devices App Version 1.10.0 Release Notes {#sis-release-notes-intro-ad-app-v110}
==========================================================================================

These release notes are for the Acceptance Devices app, version 1.10.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 03-05-2025.

New Features {#sis-release-notes-new-features-ad-app-v110}
==========================================================

Added Arabic as a supported language.

Improvements {#sis-release-notes-improvements-ad-app-v110}
==========================================================

* Tap to Pay: Improved the device enrollment experience by removing the need to provide an International Mobile Equipment Identity (IMEI) number. After upgrading to Acceptance Devices app version 1.10.0, devices must be re-enrolled.
* Updated the SDK version to 2.98.0.

Acceptance Devices App Version 1.9.0 Release Notes {#sis-release-notes-intro-ad-app-v190}
=========================================================================================

These release notes are for the Acceptance Devices app, version 1.9.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 02-03-2025.

New Features {#sis-release-notes-new-features-ad-app-v190}
==========================================================

Added the ability to print a customer or merchant receipt when using a terminal with an integrated printer.

Improvements {#sis-release-notes-improvements-ad-app-v190}
==========================================================

* Tap to Pay: Added a device requirements screen during the set-up process.
* Improved the validation process when entering an activation code so that it accepts only 8 characters.
* Improved the app behavior when attempting to access transaction history when the internet connection is not available.
* Improved the reconnect mechanism when using the app in Cloud mode.
* The mid-transaction status updates now indicate if the current transaction can be cancelled.
* Updated the SDK version to 2.97.0.

Acceptance Devices App Version 1.8.0 Release Notes {#sis-release-notes-intro-ad-app-v180}
=========================================================================================

These release notes are for the Acceptance Devices app, version 1.8.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 10-31-2024.

Improvements {#sis-release-notes-improvements-ad-app-v180}
==========================================================

Updated the SDK version to 2.95.0.

Fixed Issues {#sis-release-notes-bug-fixes-ad-app-v180}
=======================================================

Fixed the issue that caused today's transactions to not appear in the transaction history if the end date was manually set to `Today`.

Acceptance Devices App Version 1.7.0 Release Notes {#sis-release-notes-intro-ad-app-v170}
=========================================================================================

These release notes are for the Acceptance Devices app, version 1.7.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 09-30-2024.

New Features {#sis-release-notes-new-features-ad-app-v170}
==========================================================

* Added the ability to provide these details when performing a transaction:
  * Payment facilitator details.
  * Tax details.
  * Installment details for the Latin America and Caribbean (LAC) region.
    {#sis-release-notes-new-features-ad-app-v170_ul_hhw_nvy_2dc}
* Added support for additional languages in the Acceptance Devices app.
* Acceptance Devices app can now be used with Tap to Pay.

Improvements {#sis-release-notes-improvements-ad-app-v170}
==========================================================

Updated the SDK version to 2.94.0.

Fixed Issues {#sis-release-notes-bug-fixes-ad-app-v170}
=======================================================

* Fixed the issue that caused the Acceptance Devices app to crash when an unsupported character was entered during activation code entry.
* Fixed the issue that caused the Print Receipt button to appear on the Summary screen of devices without a printer.

Acceptance Devices App Version 1.6.0 Release Notes {#sis-release-notes-intro-ad-app-v160}
=========================================================================================

These release notes are for the Acceptance Devices app, version 1.6.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 07-22-2024.

Improvements {#sis-release-notes-improvements-ad-app-v160}
==========================================================

* Acceptance Devices app server now provides the full certificate chain for TLS.
* Transaction summary reports can now show multiple currencies.
* Improved the UI on several screens.
* Improved the WebSocket connection handling.
* Updated the SDK version to 2.92.0.

Acceptance Devices App Version 1.5.0 Release Notes {#sis-release-notes-intro-ad-app-v150}
=========================================================================================

These release notes are for the Acceptance Devices app, version 1.5.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 06-25-2024.

New Features {#sis-release-notes-new-features-ad-app-v150}
==========================================================

* Added the option to set a custom merchant reference code for transactions when the Acceptance Devices app is in Standalone mode.
* Signature capture type can now be set to `NONE` to skip signature capture.
* Added support for the Oracle Payment Interface.

Improvements {#sis-release-notes-improvements-ad-app-v150}
==========================================================

* PAX IM30: Settings button is now hidden.
* Settings menu now has an idle timeout of 2 minutes for the PAX IM30 and 5 minutes for all other supported PAX devices.
* Status notification now indicates when a device is operating in Standalone mode.
* Updated the SDK version to 2.91.0.

Fixed Issues {#sis-release-notes-bug-fixes-ad-app-v150}
=======================================================

* Fixed the issue that caused POS Setup to fail when you attempt set up again after canceling.
* Fixed the issue that caused Offline mode not to be shown when the Acceptance Devices app is in Cloud with Standalone mode.
* PAX A35: Fixed the issue that caused some text in the transaction summary report to not display correctly.

Acceptance Devices App Version 1.4.0 Release Notes {#sis-release-notes-intro-ad-app-v1-4-0}
===========================================================================================

These release notes are for the Acceptance Devices app, version 1.4.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 05-29-2024.

New Features {#sis-release-notes-new-features-ad-app-v1-4-0}
============================================================

* Added support for PAX IM30 and PAX A920 MAX devices.
* Added support for asynchronous responses for transactions when the Acceptance Devices app is in Cloud mode.

Improvements {#sis-release-notes-improvements-ad-app-v1-4-0}
============================================================

Updated the SDK version to 2.90.0.

Fixed Issues {#sis-release-notes-bug-fixes-ad-app-v1-4-0}
=========================================================

* Fixed the issue that rarely caused the app to crash when an invalid request was attempted.
* Fixed the issue that caused null receipt fields to be shown in the response when processing an offline transaction.

Acceptance Devices App Version 1.3.0 Release Notes {#sis-release-notes-intro-ad-app-v1-3-0}
===========================================================================================

These release notes are for the Acceptance Devices app, version 1.3.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 04-23-2024.

New Features {#sis-release-notes-new-features-ad-app-v1-3-0}
============================================================

Acceptance Devices App now supports:

* Offline transactions (also known as *deferred authorization* or *store and forward*) in Local and Standalone modes
* On-receipt tipping in Local mode
* Cloud mode
* Transaction summary reports
  {#sis-release-notes-new-features-ad-app-v1-3-0_ul_kpv_lfj_x1c}

Improvements {#sis-release-notes-improvements-ad-app-v1-3-0}
============================================================

* Added support for TLS v1.3.
* Removed support for TLS v1.0 and TLS v1.1.
* Updated the SDK version to 2.88.0.

Fixed Issues {#sis-release-notes-bug-fixes-ad-app-v1-3-0}
=========================================================

* Fixed the issue that caused the transaction history not to display transactions when the PAX terminal was set to certain time zones.
* PAX A35 terminal: Fixed the issue that caused the Acceptance Devices app not to auto-start.

Acceptance Devices App Version 1.2.0 Release Notes {#sis-release-notes-intro-ad-app-v1-2-0}
===========================================================================================

These release notes are for the Acceptance Devices app, version 1.2.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 01-31-2024.

Improvements {#sis-release-notes-improvements-ad-app-v1-2-0}
============================================================

* Capture API requests now return `CaptureResponse` in the Type field.
* If there is no internet access, the Start Server button is not available in the Acceptance Devices app.
* Improved the responsiveness of the Settings menu.
* Updated the SDK version to 2.86.

Fixed Issues {#sis-release-notes-bug-fixes-ad-app-v1-2-0}
=========================================================

* Fixed the issue that caused the Acceptance Devices app to crash occasionally when starting a transaction from the background.
* On the Enter Amount screen, fixed the issue that caused the Backspace key to not work properly for some keyboard settings.
* On the PAX A35 terminal, fixed the issue that caused the green and red physical buttons to be ignored on the Passcode screen.
* Fixed the issue that caused authentication to fail after reactivation when operating in Standalone mode.

Acceptance Devices App Version 1.1.0 Release Notes {#sis-release-notes-intro-ad-app-v1-1-0}
===========================================================================================

These release notes are for the Acceptance Devices app, version 1.1.0 for Android, which is used in the PAX Acceptance Devices App and Tap to Pay on Android Acceptance Devices App. The release date is 12-22-2023.

New Features {#sis-release-notes-new-features-ad-app-v1-1-0}
============================================================

* **Acceptance Devices protocol:** The Acceptance Devices app features the new, streamlined Acceptance Devices protocol. This protocol replaces the ATICA (ISO20022) protocol and is the default integration method for the PAX Acceptance Devices App.
* **WebSockets support:** The Acceptance Devices app now supports WebSockets, enabling a two-way connection between the point-of-sale (POS) system and the terminal.
* **Standalone mode:** A new standalone operating mode was added to the Acceptance Devices app. This mode enables merchants to enter transaction amounts directly on the terminal.
* **Transaction history:** Merchant transaction history is now accessible from the Settings menu in the Acceptance Devices app. This feature includes quick filtering options and linked operations.
  {#sis-release-notes-new-features-ad-app-v1-1-0_ul_ibl_pwk_h1c}

