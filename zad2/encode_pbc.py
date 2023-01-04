from utils import *

messageFile = open('message.txt', 'r')
ivFile = open('iv.txt', 'rb')
encodedMessageFile = open('encoded_message.txt', 'wb')
iv = ivFile.read()
# print(iv)
keyStr = input('key: ')
messageStr = messageFile.read()
message, key = strToBytes(messageStr), strToBytes(keyStr)

encodedMessage = aesEncodePbc(message, key, iv)

encodedMessageFile.write(encodedMessage)

encodedMessageFile.close()
ivFile.close()