import requests
import json
import hashlib

from killbills_sdk.cryptoService import cipher_hmac_payload

def send_data_with_hmac(env, endpoint, data, hmac_signature, validator):

    if not data or not hmac_signature or hmac_signature == '':
        raise ValueError(f"You have not provided Data or Hmac Signature:\nData: {data}\nhmacSignature: {hmac_signature}")

    payload_validation_result = validator(data)

    if payload_validation_result is not True:
        raise ValueError(payload_validation_result)

    hashed_payload = cipher_hmac_payload(data, hmac_signature)
    headers = {
        'Authorization': f'hmac {hashed_payload}',
        'Content-Type': 'application/json'
    }

    url = f'https://in.{env + "." if env != "prod" else "."}killbills.{"dev" if env != "prod" else "co"}/{endpoint}'
    response = requests.post(url, data=json.dumps(data), headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)

    return response.json()


