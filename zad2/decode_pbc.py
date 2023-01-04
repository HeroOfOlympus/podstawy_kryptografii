from utils import *

encodedMessageFile = open('encoded_message.txt', 'rb')
ivFile = open('iv.txt', 'rb')
keyStr = input('key: ')
key = strToBytes(keyStr)
encodedMessage = encodedMessageFile.read()
iv = ivFile.read()

message = aesDecodePbc(encodedMessage, key, iv)
messageStr = bytesToStr(unfill(message))
print(messageStr)

encodedMessageFile.close()
ivFile.close()