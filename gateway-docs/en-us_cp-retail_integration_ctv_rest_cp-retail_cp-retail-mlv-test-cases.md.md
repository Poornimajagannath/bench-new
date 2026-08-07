Retail Message-Level Validation Test Cases {#cp-retail-mlv-test-cases}
======================================================================

Use these test cases to validate your integration with Card Present Connect \| Retail services. Follow-on transaction test cases are shown in their respective tables. PIN debit test cases are not included.

Retail Sale Test Cases
----------------------

Use these test cases to validate retail transaction integrations.

| Transaction Type and Entry Mode |                         Card Type                         | Amount  |
|---------------------------------|-----------------------------------------------------------|---------|
| **Retail Sale**                                                                                     |||
| Contact                         | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
| Contactless                     | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
| EMV fallback                    | Relay                                                      | 9601.00 |
| Magnetic stripe                 | Relay                                                      | 9601.00 |
| Manual entry                    | Relay                                                      | 9604.00 |
| **Retail Transaction Search**                                                                       |||
| ---                             | Previous contact Relay                                     | ---     |
| **Retail Sale Timeout Void**                                                                        |||
| ---                             | Previous contact Relay                                     | ---     |
| **Retail Sale Void**                                                                                |||
| ---                             | Previous contact Mastercard                               | ---     |
| **Retail Sale Refund**                                                                              |||
| ---                             | Previous contactless Relay                                 | 9900.00 |
| ---                             | Previous contactless Mastercard                           | 9900.00 |
| **Retail Refund Void**                                                                              |||
| ---                             | Void previous refund Relay                                 | ---     |
| **Retail Refund Timeout Void**                                                                      |||
| ---                             | Timeout void previous refund Mastercard                   | ---     |
| **Retail Sale Partial Authorization**                                                               |||
| Contact                         | Relay                                                      | 9901.00 |
| Contactless                     | Relay                                                      | 9901.00 |
| **Retail Partial Authorization Capture**                                                            |||
| Contact                         | Previous partial authorization Relay                       | 3000.00 |
| **Retail Partial Authorization Reversal**                                                           |||
| Contactless                     | Previous partial authorization Relay                       | 3000.00 |
[Retail Sale Test Cases]

Retail Online PIN Test Cases
----------------------------

Use these test cases to validate retail transaction integrations.

| Transaction Type and Entry Mode |                         Card Type                         | Amount  |
|---------------------------------|-----------------------------------------------------------|---------|
| **Retail Online PIN**                                                                               |||
| Contact                         | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
[Retail Online PIN Test Cases]

Retail Online PIN, Cashback Surcharge Test Cases
------------------------------------------------

Use these test cases to validate retail transaction integrations.

| Transaction Type and Entry Mode | Card Type | Amount  |
|---------------------------------|-----------|---------|
| **Retail Online PIN, Cashback Surcharge**           |||
| Contact                         | Relay      | 9900.00 |
[Retail Online PIN, Cashback Surcharge Test Cases]

Retail Online PIN, PIN Pad Down Test Cases
------------------------------------------

Use these test cases to validate retail transaction integrations.

| Transaction Type and Entry Mode | Card Type | Amount  |
|---------------------------------|-----------|---------|
| **Retail Online PIN, PIN Pad Down**                 |||
| Contact                         | Relay      | 9900.00 |
[Retail Online PIN, PIN Pad Down Test Cases]

Retail Credit Test Cases
------------------------

Use these test cases to validate retail transaction integrations.

| Transaction Type and Entry Mode |                         Card Type                         | Amount  |
|---------------------------------|-----------------------------------------------------------|---------|
| **Retail Credit**                                                                                   |||
| Contact                         | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
| Contactless                     | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
| **Retail Credit Timeout Void**                                                                      |||
| Contact                         | Previous credit Relay                                      | ---     |
| **Retail Credit Void**                                                                              |||
| Contactless                     | Previous credit Relay                                      | ---     |
[Retail Credit Test Cases]

Retail Authorization with Follow-On Test Cases
----------------------------------------------

Use these test cases to validate retail transaction integrations.

| Transaction Type and Entry Mode |                         Card Type                         | Amount  |
|---------------------------------|-----------------------------------------------------------|---------|
| **Retail Authorization**                                                                            |||
| Contact                         | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
| Contactless                     | Relay, Mastercard, American Express, Discover, Diners, JCB | 9900.00 |
| **Retail Capture**                                                                                  |||
| Contact                         | Previous authorization Relay                               | 9900.00 |
| Contact                         | Previous authorization Mastercard                         |         |
| Contactless                     | Previous authorization Relay                               | 9900.00 |
| **Retail Capture Timeout Void**                                                                     |||
| Contact                         | Previous capture Relay                                     | ---     |
| **Retail Capture Void**                                                                             |||
| Contactless                     | Previous capture Relay                                     | ---     |
| **Retail Authorization Capture Refund**                                                             |||
| Contact                         | Previous capture Mastercard                               | 9900.00 |
| **Retail Authorization Reversal**                                                                   |||
| Contact                         | Previous authorization Mastercard                         | 9900.00 |
| **Retail Authorization Timeout Reversal**                                                           |||
| Contactless                     | Previous authorization Mastercard                         | 9900.00 |
| **Retail Partial Authorization**                                                                    |||
| Contact or Contactless          | Relay                                                      | 9901.00 |
| **Retail Partial Authorization Capture**                                                            |||
| Previous entry mode             | Previous partial authorization Relay                       | 3000.00 |
| **Retail Balance Inquiry**                                                                          |||
| Contact                         | Relay                                                      | 0.00    |
[Retail Authorization with Follow-On Test Cases]

