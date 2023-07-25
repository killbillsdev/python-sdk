from killbills_sdk.validatorService import validate_transaction_payload 
from killbills_sdk.sendDataWithHmac import send_data_with_hmac

def send_transaction(env, data, hmac_key):
    return send_data_with_hmac(env, 'transaction', data, hmac_key, validate_transaction_payload)