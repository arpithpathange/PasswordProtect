#!/usr/bin/python

'''
Version:    0.0.1
Author:     Arpith Vittal Pathange

This class ecrypts and decrypts the data using Cipher package of python. The secrete key is used to b64encode and decode it.
The secrete key needs to move out of this file.

todo:
Move the secrete key from this file.

'''
from Crypto.Cipher import AES
import base64
from logger import logbase
import sys

class SafeData:
    cipher = None
    pass_key = '1234123412341234'
    log = logbase()

    def encrypt(self, text):
        try:

            msg_text = text.rjust(32)
            cipher = AES.new(self.pass_key, AES.MODE_ECB) # never use ECB in strong systems obviously
            encoded = base64.b64encode(cipher.encrypt(msg_text))

        except:
            self.log.logerror("Error in entrypting the data (def)(encrypt) == (class)(SafeData)")
        return encoded

    def decrypt(self,decryptdata, secret_key):
            try:

                cipher = AES.new(secret_key, AES.MODE_ECB) # never use ECB in strong systems obviously
                decoded = cipher.decrypt(base64.b64decode(decryptdata))

            except:
                self.log.logerror("Error is decrypting data (def)(decrypt) == (Class)(SafeData)")
            return decoded


