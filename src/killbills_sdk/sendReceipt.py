from killbills_sdk.validatorService import validate_receipt_payload 
from killbills_sdk.sendDataWithHmac import send_data_with_hmac

def send_receipt(env, data, hmac_key):
    return send_data_with_hmac(env, 'receipt', data, hmac_key, validate_receipt_payload)
