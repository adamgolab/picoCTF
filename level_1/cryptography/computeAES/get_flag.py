#!/usr/bin/python

import base64
from Crypto.Cipher import AES

cipherText = base64.b64decode('rW4q3swEuIOEy8RTIp/DCMdNPtdYopSRXKSLYnX9NQe8z+LMsZ6Mx/x8pwGwofdZ')
key = base64.b64decode('6v3TyEgjUcQRnWuIhjdTBA==')

aes = AES.new(key, AES.MODE_ECB)
plaintext = aes.decrypt(cipherText)

print plaintext
