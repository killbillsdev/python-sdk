import hmac
import hashlib
import json

def cipher_hmac_payload(payload, hmac_key):  
    h = hmac.new(hmac_key.encode('utf-8'), json.dumps(payload).encode('utf-8'), hashlib.sha256 ).hexdigest()
    return h
