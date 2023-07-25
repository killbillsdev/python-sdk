import hashlib
import unittest
from cryptoService import cipher_hmac_payload

class TestCryptoService(unittest.TestCase):

    def test_sanity_check(self):
        self.assertTrue(True)

    def test_cipher_hmac_payload(self):
        payload = '{foo:bar}'
        hmac = 'myHmacKey'

        result = cipher_hmac_payload(payload, hmac)
        self.assertEqual(result, '8e159b87fe9eb6d9e2c5d0644f0c0cb0fa8ae7c1e82a058fd312a12130a2df31')
        self.assertEqual(hashlib.sha256(hmac.encode('utf-8')).hexdigest(), '8453b6b1eb476631d5b60397334211960927607f7b3805ccb94aaf93c3311c9a')

if __name__ == '__main__':
    unittest.main()

