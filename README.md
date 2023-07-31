
# KillBills - SDK (Python)

The main purpose of this Software Development Kit (SDK) is to facilitates the integration of KillBills' services into Python applications. The SDK will act as an intermediary layer, allowing developers to communicate with the KillBills API and access its features in a straightforward manner. By providing a consistent and easy-to-use interface, the SDK aims to simplify & speed up the process of integrating KillBills' services into Python applications.




## Dependancies

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Features

- getStores : The method getStores returns a list of killbills integrated stores as an array of objects with relevant properties.
- sendTransaction : The method sendTransaction validates and send transaction to the killbills gate transaction.
- sendReceipt : The method sendReceipt validates and send a receipt to the killbills gate receipt.



## Installation

##### with pip :
```bash
pip install killbills-sdk
```

## Usage/Examples
 
#### Method getStores :
```python
import killbills_sdk
from killbills_sdk.getStores import get_stores

print(get_stores('dev','your-api-key'))

```
##### Output:
```yaml
[
  {
    "id": "id",
    "billing_descriptor": "store billing descriptor",
    "store_name": "store name",
    "merchant_name": "merchant name",
    "full_address": "00 street, 00000, city",
    "siret": 00000000000000
  },
   {
    "id": "id",
    "billing_descriptor": "store billing descriptor",
    "store_name": "store name",
    "merchant_name": "merchant name",
    "full_address": "00 street, 00000, city",
    "siret": 00000000000000
  },
  //...other results
]
```
# 
#### Method sendTransaction :
##### note that the transactionData object only contains minimal required values see (insert link to all possibilities)
```python
import killbills_sdk
from killbills_sdk.sendTransaction import send_transaction

payload = {...}
print(send_transaction('dev',payload,'your-hmac-key'))
```
##### Output: 
```yaml
{
"status": "success",
"message": "published to gate transaction",
"messageId": "xxxxxxxxxxxxxxxxx",
"previewLink": "https://banks.killbills.co/payloads/xxxxxxxxxxxxxxxxx"
}
```
# 
#### Method sendReceipt :
##### note that the receiptData object only contains minimal required values see (insert link to all possibilities)
```python
from sendReceipt import send_receipt
receiptData = {...}
print(send_receipt('prod', receiptData,'your-hmac-key' ))
```
##### Output: 
```yaml
{
"status": "success",
"message": "published to gate receipt",
"messageId": "xxxxxxxxxxxxxxxxx",
"previewLink": "https://merchants.killbills.co/payloads/xxxxxxxxxxxxxxxxx"
}
```

## Transaction & Receipt Architecture

#### TRANSACTION :
```typescript
transactionData = {
    bank_id: '', // string (36 caractères)
    callback_url: '', // string
    partner_name: '', // string
    kb_features: [], // tableau de chaînes de caractères ou nombres vides
    receipt_format: '', // string ('JSON', 'PDF', 'SVG', 'PNG')
    transaction: {
        reference_id: '', // string
        amount: '', // number (positif)
        customer_id: '', // string
        transaction_date: '', // date (au format chaîne de caractères)
        store_name: '', // string ou vide
        billing_descriptor: '', // string
        siret: '', // string ou vide
        payment: '', // objet vide
        currency: '', // string ou vide
        pos_name: '', // string ou vide
        merchant_name: '' // string ou vide
    }
};
```
#### RECEIPT :
```typescript
receiptData = {
    reference_id: '', // string (alphanumérique)
    amount: 0, // number
    total_tax_amount: '', // number ou vide
    currency: '', // string ('EUR' ou 'USD')
    date: '', // string (au format 'YYYY-MM-DDTHH:mm:ss')
    covers: 0, // number ou vide
    table: '', // string ou vide
    invoice: 0, // number ou vide
    total_discount: 0, // number ou vide
    mode: 0, // number ou vide
    partner_name: '', // string
    merchant: {
        merchant_name: '', // string ou vide
        reference_id: '', // string
        merchant_id: 0 // number ou vide
    },
    store: {
        store_name: '', // string
        reference_id: '', // string
        billing_descriptor: '', // string
        siret: '', // string (14 caractères)
        code_ape: '', // string ou vide
        tva_intra: '', // string ou vide
        address: {
            postal_code: 0, // number
            street_address: '', // string ou vide
            country: '', // string ou vide
            city: '', // string ou vide
            full_address: '', // string ou vide
            number: 0 // number ou vide
        }
    },
    taxes: [{ 
        description: '', // string ou vide
        amount: 0, // number
        rate: 550 // number (550, 1000 ou 2000) ou vide
    }],
    items: [{
        reference_id: '', // string ou vide
        name: '', // string
        description: '', // string ou vide
        type: '', // string ou vide
        quantity: 0, // number
        price: 0, // number
        discount: 0, // number ou vide
        total_amount: 0, // number ou vide
        tax: {
            description: '', // string ou vide
            amount: 0, // number
            rate: 550 // number (550, 1000 ou 2000) ou vide
        },
        subitems: [{
            reference_id: '', // string ou vide
            name: '', // string
            description: '', // string ou vide
            quantity: 0, // number ou vide
            price: 0, // number ou vide
            discount: 0, // number ou vide
            total_amount: 0, // number ou vide
            tax: {
                description: '', // string ou vide
                amount: 0, // number
                rate: 550 // number (550, 1000 ou 2000) ou vide
            }
        }]
    }],
    payments: [{
        bin: '', // string ou vide
        last_four: '', // string ou vide
        auth_code: '', // string ou vide
        scheme: '', // string ou vide
        amount: 0, // number
        transaction_date: '', // string (au format 'YYYY-MM-DDTHH:mm:ss')
        transaction_id: '', // string ou vide
        payment_type: '' // string ou vide
    }]
};
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/killbillsdev/python-sdk
```

Go to the project directory

```bash
  cd python-sdk
```

Install dependencies

```bash
make install
```

Build project 

```bash
make build
```


## Running Tests

To run tests, run the following command

```bash
make test
```


## Feedback

If you have any feedback, please reach out to us at :

https://freeonlinesurveys.com/s/8biYAZPa
## License

[MIT](https://choosealicense.com/licenses/mit/) [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


