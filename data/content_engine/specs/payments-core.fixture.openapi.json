{
  "openapi": "3.0.3",
  "info": {
    "title": "CyberSource Payments Core (local Relay fixture)",
    "version": "0.1.0-local",
    "description": "Frozen local OpenAPI fixture for Specs-to-Docs V0. Not a live CyberSource download. No secrets or PAN."
  },
  "servers": [
    {
      "url": "https://apitest.cybersource.com",
      "description": "Sandbox host reference only \u2014 V0 makes no network calls"
    }
  ],
  "components": {
    "securitySchemes": {
      "httpSignature": {
        "type": "apiKey",
        "in": "header",
        "name": "v-c-merchant-id",
        "description": "HTTP Signature auth using PGW_MERCHANT_ID / PGW_KEY_ID / PGW_SHARED_SECRET env vars (never hardcode)"
      }
    },
    "schemas": {
      "CreatePaymentRequest": {
        "type": "object",
        "required": [
          "clientReferenceInformation",
          "orderInformation",
          "paymentInformation"
        ],
        "properties": {
          "clientReferenceInformation": {
            "type": "object",
            "required": [
              "code"
            ],
            "properties": {
              "code": {
                "type": "string",
                "description": "Merchant reference code for the transaction"
              }
            }
          },
          "orderInformation": {
            "type": "object",
            "required": [
              "amountDetails"
            ],
            "properties": {
              "amountDetails": {
                "type": "object",
                "required": [
                  "totalAmount",
                  "currency"
                ],
                "properties": {
                  "totalAmount": {
                    "type": "string",
                    "description": "Order total amount"
                  },
                  "currency": {
                    "type": "string",
                    "description": "ISO 4217 currency code"
                  }
                }
              },
              "billTo": {
                "type": "object",
                "properties": {
                  "firstName": {
                    "type": "string"
                  },
                  "lastName": {
                    "type": "string"
                  }
                }
              }
            }
          },
          "paymentInformation": {
            "type": "object",
            "required": [
              "card"
            ],
            "properties": {
              "card": {
                "type": "object",
                "properties": {
                  "number": {
                    "type": "string",
                    "description": "Tokenized instrument or test card id \u2014 do not send raw PAN"
                  },
                  "expirationMonth": {
                    "type": "string"
                  },
                  "expirationYear": {
                    "type": "string"
                  },
                  "type": {
                    "type": "string",
                    "enum": [
                      "001",
                      "002"
                    ],
                    "description": "Card type code"
                  }
                }
              }
            }
          }
        }
      },
      "Payment": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "status": {
            "type": "string"
          }
        }
      },
      "CaptureRequest": {
        "type": "object",
        "required": [
          "orderInformation"
        ],
        "properties": {
          "clientReferenceInformation": {
            "type": "object",
            "properties": {
              "code": {
                "type": "string"
              }
            }
          },
          "orderInformation": {
            "type": "object",
            "required": [
              "amountDetails"
            ],
            "properties": {
              "amountDetails": {
                "type": "object",
                "required": [
                  "totalAmount"
                ],
                "properties": {
                  "totalAmount": {
                    "type": "string"
                  },
                  "currency": {
                    "type": "string"
                  }
                }
              }
            }
          }
        }
      },
      "CreditRequest": {
        "type": "object",
        "required": [
          "orderInformation"
        ],
        "properties": {
          "clientReferenceInformation": {
            "type": "object",
            "properties": {
              "code": {
                "type": "string"
              }
            }
          },
          "orderInformation": {
            "type": "object",
            "required": [
              "amountDetails"
            ],
            "properties": {
              "amountDetails": {
                "type": "object",
                "required": [
                  "totalAmount"
                ],
                "properties": {
                  "totalAmount": {
                    "type": "string"
                  },
                  "currency": {
                    "type": "string"
                  }
                }
              }
            }
          }
        }
      },
      "CustomerRequest": {
        "type": "object",
        "required": [
          "buyerInformation"
        ],
        "properties": {
          "buyerInformation": {
            "type": "object"
          },
          "clientReferenceInformation": {
            "type": "object"
          }
        }
      },
      "Customer": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "buyerInformation": {
            "type": "object"
          }
        }
      },
      "MppCredentialRequest": {
        "type": "object",
        "required": [
          "clientReferenceInformation"
        ],
        "properties": {
          "clientReferenceInformation": {
            "type": "object"
          },
          "processingInformation": {
            "type": "object"
          }
        }
      },
      "MppCredential": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "status": {
            "type": "string"
          }
        }
      },
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "reason": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "details": {
            "type": "array",
            "items": {
              "type": "object"
            }
          }
        }
      }
    }
  },
  "security": [
    {
      "httpSignature": []
    }
  ],
  "paths": {
    "/pts/v2/payments": {
      "post": {
        "operationId": "createPayment",
        "tags": [
          "Payments"
        ],
        "summary": "Create a payment authorization",
        "description": "Authorize a payment in sandbox using tokenized or instrument identifiers. Do not send raw PAN.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreatePaymentRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Payment created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Payment"
                }
              }
            }
          },
          "400": {
            "description": "Invalid request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "401": {
            "description": "Authentication failed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          }
        }
      }
    },
    "/pts/v2/payments/{id}": {
      "get": {
        "operationId": "getPayment",
        "tags": [
          "Payments"
        ],
        "summary": "Retrieve a payment",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Payment found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Payment"
                }
              }
            }
          },
          "404": {
            "description": "Payment not found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          }
        }
      }
    },
    "/pts/v2/payments/{id}/captures": {
      "post": {
        "operationId": "capturePayment",
        "tags": [
          "Captures"
        ],
        "summary": "Capture an authorized payment",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CaptureRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Capture created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Payment"
                }
              }
            }
          },
          "400": {
            "description": "Invalid capture request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          }
        }
      }
    },
    "/pts/v2/credits": {
      "post": {
        "operationId": "createCredit",
        "tags": [
          "Credits"
        ],
        "summary": "Create a credit",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreditRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Credit created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Payment"
                }
              }
            }
          },
          "400": {
            "description": "Invalid credit request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          }
        }
      }
    },
    "/tms/v2/customers": {
      "post": {
        "operationId": "createCustomer",
        "tags": [
          "Customers"
        ],
        "summary": "Create a TMS customer",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CustomerRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Customer created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Customer"
                }
              }
            }
          },
          "400": {
            "description": "Invalid customer request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          }
        }
      }
    },
    "/tms/v2/customers/{customerId}": {
      "get": {
        "operationId": "getCustomer",
        "tags": [
          "Customers"
        ],
        "summary": "Retrieve a TMS customer",
        "parameters": [
          {
            "name": "customerId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Customer found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Customer"
                }
              }
            }
          },
          "404": {
            "description": "Customer not found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          }
        }
      }
    },
    "/risk/v1/authentication-setups": {
      "post": {
        "operationId": "createMppCredentialSetup",
        "tags": [
          "MPP Credentials"
        ],
        "summary": "Create payer authentication / MPP credential setup",
        "description": "Payer Authentication setup prerequisite before enrollment. Microform tokenize alone is not 3DS completion.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MppCredentialRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Setup created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MppCredential"
                }
              }
            }
          },
          "400": {
            "description": "Invalid setup request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          },
          "401": {
            "description": "Authentication failed",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          }
        }
      }
    },
    "/risk/v1/authentications": {
      "post": {
        "operationId": "checkMppEnrollment",
        "tags": [
          "MPP Credentials"
        ],
        "summary": "Check payer authentication enrollment",
        "description": "Enrollment may return FRICTIONLESS, CHALLENGE, or UNAVAILABLE paths.",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MppCredentialRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Enrollment checked",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MppCredential"
                }
              }
            }
          },
          "400": {
            "description": "Invalid enrollment request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorResponse"
                }
              }
            }
          }
        }
      }
    }
  }
}
