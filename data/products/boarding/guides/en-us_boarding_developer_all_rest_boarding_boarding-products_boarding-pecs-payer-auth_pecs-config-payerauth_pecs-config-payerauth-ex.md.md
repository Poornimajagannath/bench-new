Example: Configuring Payer Authentication Using the PECS API {#pecs-config-payerauth-ex}
========================================================================================

Request to Configure American Express SafeKey

```
{"organizationId":"lrsebctest20001",
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "amexSafeKey": {
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure Cartes Bancaires

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "CB": {
              "requestorId": "reqtestid",
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure Discover/Diners Club ProtectBuy

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "dinersClubInternationalProtectBuy": {
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure ELO

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "ELO": {
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure JCB J/Secure

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "jCBJSecure": {
              "securePasswordForJCB": "testpassword",
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure Mastercard/Meeza Identity Check

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "masterCardSecureCode": {
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure UnionPay 3-D Secure

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "UPI": {
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

Request to Configure Visa Secure

```
{
  "payments": {
    "payerAuthentication": {
      "configurationInformation": {
        "configurations": {
          "cardTypes": {
            "verifiedByVisa": {
              "enabled": true,
              "currencies": [
                {
                  "currencyCodes": [
                    "ALL",
                    "978"
                  ],
                  "acquirerId": "acquirertest-1000",
                  "processorMerchantId": "procmerchtest"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

{#pecs-config-payerauth-ex_codeblock_ulf_bvh_jzb}  
Response to a Successful Request

```
{
    "configurationId": "7593E16A-21D0-452E-8F7F-53805C1AE571",
    "submitTimeUtc": "2024-05-17T12:39:28Z",
    "status": "SUCCESS"
}
```

{#pecs-config-payerauth-ex_codeblock_wtf_m4g_lzb}For more information on response reason codes, see [Reason Codes](/docs/cybs/en-us/boarding/developer/all/rest/boarding/boarding-error-codes.md "").
