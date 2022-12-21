from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
from utils import *

class AES_ECB:
    def __init__(self, key):
        self.key = md5(key.encode(CHARACTER_ENCODING)).hexdigest()

    def encrypt(self, raw):
        print('raw1 ', raw)
        raw = fillToBlockSize(raw)
        print('raw2 ', raw)
        cipher = AES.new(self.key.encode(CHARACTER_ENCODING), AES.MODE_ECB)
        return b64encode(cipher.encrypt(raw.encode(CHARACTER_ENCODING)))

    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = AES.new(self.key.encode(CHARACTER_ENCODING), AES.MODE_ECB)
        return unfill(cipher.decrypt(enc)).decode(CHARACTER_ENCODING)
