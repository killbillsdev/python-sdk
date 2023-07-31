import pytest
import os,time,re
from dotenv import load_dotenv
load_dotenv()


from sendTransaction import send_transaction

invalid_payload = {
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

test_payload = {
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

def test_send_banking_transaction_valid_payload():
    result = send_transaction('dev', test_payload, os.environ.get("TEST_HMAC"))
    assert result['status'] == 'success'
    assert result['message'] == 'published to gate transaction'
    
def test_send_banking_transaction_INvalid_payload():

    with pytest.raises(ValueError) as exc_info:
        send_transaction('dev', invalid_payload, os.environ.get("TEST_HMAC"))
    expected_error_message = (
        "5 validation errors for TransactionPayload\n"
        "bank_id\n"
        "  String should have at least 36 characters [type=string_too_short, input_value='1234', input_type=str]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/string_too_short\n"
        "partner_name\n"
        "  Field required [type=missing, input_value={'bank_id': '1234', 'call...illing_descriptor': ''}}, input_type=dict]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/missing\n"
        "receipt_format\n"
        "  Input should be 'json','pdf','svg' or 'png' [type=enum, input_value='INVALID_FORMAT', input_type=str]\n"
        "transaction.amount\n"
        "  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=-10.5, input_type=float]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/int_from_float\n"
        "transaction.transaction_date\n"
        "  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='INVALID_DATE', input_type=str]\n"
        "    For further information visit https://errors.pydantic.dev/2.0.3/v/int_parsing"
    )

    assert str(exc_info.value) == expected_error_message

    
    
   

