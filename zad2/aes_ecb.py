from utils import *

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
