from Crypto.Cipher import AES
import base64

class SafeData:
    cipher = None
    pass_key = '1234123412341234'

    def encrypt(self, text):
        msg_text = text.rjust(32)
        cipher = AES.new(self.pass_key, AES.MODE_ECB) # never use ECB in strong systems obviously
        encoded = base64.b64encode(cipher.encrypt(msg_text))
        return encoded

    def decrypt(self,decryptdata, secret_key):
            cipher = AES.new(secret_key, AES.MODE_ECB) # never use ECB in strong systems obviously
            decoded = cipher.decrypt(base64.b64decode(decryptdata))
            return decoded


