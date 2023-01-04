from utils import *

# class AES_ECB:
#     def __init__(self, key):
#         self.key = md5(key.encode(CHARACTER_ENCODING)).hexdigest()

#     def encrypt(self, raw):
#         print('raw1 ', raw)
#         raw = fillToBlockSize(raw)
#         print('raw2 ', raw)
#         cipher = AES.new(self.key.encode(CHARACTER_ENCODING), AES.MODE_ECB)
#         return b64encode(cipher.encrypt(raw.encode(CHARACTER_ENCODING)))
#     def decrypt(self, enc):
#         enc = b64decode(enc)
#         cipher = AES.new(self.key.encode(CHARACTER_ENCODING), AES.MODE_ECB)
#         return unfill(cipher.decrypt(enc)).decode(CHARACTER_ENCODING)

messageStr = input('message: ')
message = strToBytes(messageStr)
keyStr = input('key: ')
key = strToBytes(keyStr)

encodedMessage = aesEncodeEcb(message, key)
print(encodedMessage)
decodedMessage = aesDecodeEcb(encodedMessage, key)
print(decodedMessage)
decodedMessageStr = bytesToStr(decodedMessage)
print(decodedMessageStr)
print(unfill(decodedMessage))
