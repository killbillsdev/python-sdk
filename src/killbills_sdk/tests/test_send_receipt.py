import pytest
import os,time,re
from dotenv import load_dotenv
load_dotenv()

from sendReceipt import send_receipt

invalidPayload = {
    "date": "2023-07-16T09:04:08.823",
    "mode": 0,
    "items": [
      {
        "tax": {
          "rate": 1000,
          "amount": 85,
          "description": "TVA",
        },
        "name": "Salade ATCHOUM",
        "price": 850,
        "quantity": 1,
        "sub_items": [
          {
            "tax": {
              "rate": 1000,
              "amount": 30,
              "description": "TVA",
            },
            "name": "Atchoum V1",
            "type": "dish",
            "price": 1555,
            "quantity": 1,
            "description": "",
            "reference_id": "5df1e0fa-3bdc-461a-9170-a74bb2f0792b",
            "total_amount": 300,
          },
          {
            "tax": {
              "rate": 1000,
              "amount": 40,
              "description": "TVA",
            },
            "name": "Saucisses v1",
            "type": "dish",
            "quantity": 1,
            "description": "",
            "reference_id": "d15e20c6-925c-491a-8381-153c9352aadd",
            "total_amount": 400,
          },
          {
            "tax": {
              "rate": 1000,
              "amount": 25,
              "description": "TVA",
            },
            "name": "Thé v1",
            "type": "dish",
            "quantity": 1,
            "description": "",
            "reference_id": "72b2479f-9210-44fc-8187-a4f40bc31ee6",
            "total_amount": 250,
          },
        ],
        "description": "",
        "reference_id": "1c49ad5c-2610-4bd7-bbb5-e235639a0a42",
        "total_amount": 850,
      },
    ],
    "store": {
      "store_name": "RESTAU TEST",
      "siret": "6789",
      "address": {
        "city": "Paris",
        "number": 0,
        "country": "FRANCE",
        "postal_code": 75014,
        "street_address": "17 rue du Smart Receipt",
      },
      "code_ape": "4410",
      "tva_intra": "FR 000 000 00",
      "reference_id": "1",
      "business_name": "RESTAU TEST",
    },
    "table": "31",
    "taxes": [
      {
        "rate": 1000,
        "amount": 85,
        "description": "TVA",
      },
      {
        "rate": 2000,
        "amount": 190,
        "description": "TVA",
      },
    ],
    "amount": 871741,
    "covers": 2,
    "invoice": 1,
    "currency": "EUR",
    "merchant": {
      "name": "Restaurant test",
      "reference_id": "1234",
    },
    "payments": [
      {
        "bin": 0,
        "amount": 871741,
        "scheme": "",
        "auth_code": "",
        "last_four": 0,
        "payment_type": "CB",
        "transaction_id": None,
        "transaction_date": "2023-07-16T09:04:08.823",
      },
    ],
    "partner_name": os.environ['TEST_POS_PARTNER_NAME'],
    "reference_id": "1221554511",
  }


validPayload2 = {
    "date": "2023-07-16T09:04:08",
    "mode": 0,
    "items": [
      {
        "tax": {
          "rate": 1000,
          "amount": 85,
          "description": "TVA",
        },
        "name": "Salade ATCHOUM",
        "price": 850,
        "quantity": 1,
        "subitems": [
          {
            "tax": {
              "rate": 1000,
              "amount": 30,
              "description": "TVA",
            },
            "name": "Atchoum V1",
            "price": 1555,
            "quantity": 1,
            "description": "",
            "reference_id": "5df1e0fa-3bdc-461a-9170-a74bb2f0792b",
            "total_amount": 300,
          },
          {
            "tax": {
              "rate": 1000,
              "amount": 40,
              "description": "TVA",
            },
            "name": "Saucisses v1",
            "quantity": 1,
            "description": "",
            "reference_id": "d15e20c6-925c-491a-8381-153c9352aadd",
            "total_amount": 400,
          },
          {
            "tax": {
              "rate": 1000,
              "amount": 25,
              "description": "TVA",
            },
            "name": "Thé v1",
            "quantity": 1,
            "description": "",
            "reference_id": "72b2479f-9210-44fc-8187-a4f40bc31ee6",
            "total_amount": 250,
          },
        ],
        "description": "",
        "reference_id": "1c49ad5c-2610-4bd7-bbb5-e235639a0a42",
        "total_amount": 850,
      },
    ],
    "store": {
      "store_name": "RESTAU TEST",
      "siret": "66666666666666",
      "billing_descriptor": "RESTAU TEST",
      "address": {
        "city": "Paris",
        "number": 0,
        "country": "FRANCE",
        "postal_code": 75014,
        "street_address": "17 rue du Smart Receipt",
      },
      "code_ape": "4410",
      "tva_intra": "FR 000 000 00",
      "reference_id": "1",
    },
    "table": "31",
    "taxes": [
      {
        "rate": 1000,
        "amount": 85,
        "description": "TVA",
      },
      {
        "rate": 2000,
        "amount": 190,
        "description": "TVA",
      },
    ],
    "amount": 871741,
    "covers": 2,
    "invoice": 1,
    "currency": "EUR",
    "merchant": {
      "merchant_name": "Restaurant test",
      "reference_id": "1234",
    },
    "payments": [
      {
        "bin": "0",
        "amount": 871741,
        "scheme": "",
        "auth_code": "",
        "last_four": "0",
        "payment_type": "CB",
        "transaction_id": "null",
        "transaction_date": "2023-07-16T09:04:08",
      },
    ],
    "partner_name": os.environ['TEST_POS_PARTNER_NAME'] ,
    "reference_id": "1221554511",
  }

def test_send_receipt_empty_payload():
    with pytest.raises(ValueError) as exc_info:
        send_receipt("dev", {}, "hmac")
    expected_error_message = (
        "You have not provided Data or Hmac Signature:\n"
        "Data: {}\n"
        "hmacSignature: hmac"
        
    )
    assert str(exc_info.value) == expected_error_message

def test_send_receipt_Invalid_payload():
    with pytest.raises(ValueError) as exc_info:
        send_receipt("dev", {'tt':'toto'}, "hmac")
    expected_error_message = (
        "14 validation errors for ReceiptPayload\n"
        "reference_id\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "amount\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "currency\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "date\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "covers\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "table\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "invoice\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "mode\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "partner_name\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "merchant\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "store\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "taxes\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "items\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "payments\n"
        "  Field required [type=missing, input_value={'tt': 'toto'}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing"
        
    )
    assert str(exc_info.value) == expected_error_message
    
def test_send_receipt_valid_payload():
    result = send_receipt("dev", validPayload2, os.environ.get("TEST_POS_HMAC"))
    assert result['status'] == 'success'
    assert result['message'] == 'published to gate receipt'