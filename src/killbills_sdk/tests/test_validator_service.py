import pytest
import os,time
from validatorService import validate_receipt_payload, validate_transaction_payload
from dotenv import load_dotenv
load_dotenv()


invalidPayload = {
    "bank_id": '1234',
    "callback_url": 'data:text/plain',
    "receipt_format": 'INVALID_FORMAT',
    "transaction": {
        "reference_id": '12345678',
        "amount": -10.50,
        "customer_id": 'INVALID_GUID',
        "transaction_date": 'INVALID_DATE',
        "store_name": '',
        "billing_descriptor": ''
    }
}

testPayload = {
	"bank_id": os.environ.get("TEST_BANK_ID"),
	"callback_url": os.environ.get("TEST_CALLBACK_URL"),
	"partner_name": os.environ.get("TEST_PARTNER_NAME"),
	"receipt_format": os.environ.get("TEST_RECEIPT_FORMAT"),
	"transaction": {
		"reference_id": os.environ.get("TEST_REFERENCE_ID"),
		"customer_id": os.environ.get("TEST_CUSTOMER_ID"),
		"amount": 1000,
		"currency": "EUR",
		"transaction_date": int(time.time() * 1000),
		"merchant_name": os.environ.get("TEST_MERCHANT_NAME"),
		"pos_name": os.environ.get("TEST_POS_NAME"),
		"billing_descriptor": os.environ.get("TEST_BILLING_DESCRIPTOR"),
		"siret": os.environ.get("TEST_SIRET"),
		"payment": {
			"bin": "487179",
			"lastFour": "1234",
			"auth_code": "a27s92",
			"scheme": "VISA",
			"transaction_id": os.environ.get("TEST_TRANSACTION_ID"),
		}
	}
}

def test_should_validate_valid_payload_without_error():
   assert validate_transaction_payload(testPayload) == True

def test_should_validate_invalid_payload_and_return_validation_error():
    with pytest.raises(ValueError) as exc_info:
        validate_transaction_payload(invalidPayload)

        expected_error_message = (
            "5 validation errors for TransactionPayload:\n"
            "bank_id\n  String should have at least 36 characters (type=string_too_short, "
            "value='1234', min_length=36)\n"
            "partner_name\n  field required (type=value_error.missing)\n"
            "receipt_format\n  value is not a valid enumeration member; permitted: 'JSON', 'PDF', 'SVG', 'PNG' (type=type_error.enum; enum_values=['JSON', 'PDF', 'SVG', 'PNG'], "
            "value='INVALID_FORMAT')\n"
            "transaction.amount\n  ensure this value is greater than 0 (type=value_error.number.not_gt; limit_value=0)\n"
            "transaction.transaction_date\n  value is not a valid date (type=value_error.datetime)"
        )
        assert str(exc_info.value) == expected_error_message

def test_should_return_an_error_if_the_payload_is_empty():
    with pytest.raises(ValueError) as exc_info:
        validate_transaction_payload({})

        expected_error_message = (
            "No payload to validate"
        )
        assert str(exc_info.value) == expected_error_message
