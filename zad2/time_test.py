from utils import *
from time import time

key = b'sixteen byte key'
iv = b'fdsadafdsafdadaf'

messageShortFile = open('test_files/message_short.txt', 'r')
messageMediumFile = open('test_files/message_medium.txt', 'r')
messageLongFile = open('test_files/message_long.txt', 'r')

def testEcb(message: bytes):
    start = time()
    messageEncrypted = aesEncodeEcb(strToBytes(message), key)
    stop = time()
    print('ECB encoding: ', stop - start)
    start = time()
    aesDecodeEcb(messageEncrypted, key)
    stop = time()
    print('ECB decoding: ', stop - start)

def testCbc(message: bytes):
    start = time()
    messageEncrypted = aesEncodeCbc(strToBytes(message), key, iv)
    stop = time()
    print('CBC encoding: ', stop - start)
    start = time()
    aesDecodeCbc(messageEncrypted, key, iv)
    stop = time()
    print('CBC decoding: ', stop - start)

def testPbc(message: bytes):
    start = time()
    messageEncrypted = aesEncodePbc(strToBytes(message), key, iv)
    stop = time()
    print('PBC encoding: ', stop - start)
    start = time()
    aesDecodePbc(messageEncrypted, key, iv)
    stop = time()
    print('PBC decoding: ', stop - start)

print('for short file (about 5000 bytes)')
messageShort = messageShortFile.read()
testEcb(messageShort)
testCbc(messageShort)
testPbc(messageShort)

print('for medium file (about 50 000 bytes)')
messageMedium = messageMediumFile.read()
testEcb(messageMedium)
testCbc(messageMedium)
testPbc(messageMedium)

print('for long file (about 500 000 bytes)')
messageLong = messageLongFile.read()
testEcb(messageLong)
testCbc(messageLong)
testPbc(messageLong)

messageShortFile.close()
messageMediumFile.close()
messageLongFile.close()