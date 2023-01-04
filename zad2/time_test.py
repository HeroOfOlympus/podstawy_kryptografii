from utils import *
from time import time

KEY16 = b'sixteen byte key'
KEY32 = b'thirty two byte key aaaaaaaaaaaa'
IV = b'fdsadafdsafdadaf'
NONCE = b'noooncee'

messageShortFile = open('test_files/message_short.txt', 'r')
messageMediumFile = open('test_files/message_medium.txt', 'r')
messageLongFile = open('test_files/message_long.txt', 'r')

MODES = {
    'ECB': AES.MODE_ECB,
    'CTR': AES.MODE_CTR,
}

IV_MODES = {
    'CBC': AES.MODE_CBC,
    'CFB': AES.MODE_CFB,
    'OFB': AES.MODE_OFB,
    'OPENPGP': AES.MODE_OPENPGP,
    'EAX': AES.MODE_EAX,
    'GCM': AES.MODE_GCM,
}

NONCE_MODES = {
    'CCM': AES.MODE_CCM,
    'OCB': AES.MODE_OCB,
}

EAD_MODES = {
    'SIV': AES.MODE_SIV,
}

def test(message: bytes):
    filledMessage = fillToBlockSize(message)
    for modeName in MODES:
        eStart = time()
        cipher = AES.new(KEY16, MODES[modeName])
        encodedMessage = cipher.encrypt(filledMessage)
        eStop = time()
        cipher = AES.new(KEY16, MODES[modeName])
        cipher.decrypt(encodedMessage)
        dStop = time()
        print(modeName, 'encrypting [s]:', eStop - eStart, 'decrypting [s]:', dStop - eStop)

    for modeName in IV_MODES:
        eStart = time()
        cipher = AES.new(KEY16, IV_MODES[modeName], IV)
        encodedMessage = cipher.encrypt(filledMessage)
        eStop = time()
        cipher = AES.new(KEY16, IV_MODES[modeName], IV)
        cipher.decrypt(encodedMessage)
        dStop = time()
        print(modeName, 'encrypting [s]:', eStop - eStart, 'decrypting [s]:', dStop - eStop)

    for modeName in NONCE_MODES:
        eStart = time()
        cipher = AES.new(KEY16, NONCE_MODES[modeName], nonce = NONCE)
        encodedMessage = cipher.encrypt(filledMessage)
        eStop = time()
        cipher = AES.new(KEY16, NONCE_MODES[modeName], nonce = NONCE)
        cipher.decrypt(encodedMessage)
        dStop = time()
        print(modeName, 'encrypting [s]:', eStop - eStart, 'decrypting [s]:', dStop - eStop)


    for modeName in EAD_MODES:
        eStart = time()
        cipher = AES.new(KEY32, EAD_MODES[modeName], IV)
        encodedMessage, mac = cipher.encrypt_and_digest(filledMessage)
        eStop = time()
        cipher = AES.new(KEY32, EAD_MODES[modeName], IV)
        cipher.decrypt_and_verify(encodedMessage, mac)
        dStop = time()
        print(modeName, 'encrypting [s]:', eStop - eStart, 'decrypting [s]:', dStop - eStop)


print('\n short file')
test(fillToBlockSize(strToBytes(messageShortFile.read())))

print('\n medium file')
test(fillToBlockSize(strToBytes(messageMediumFile.read())))

print('\n long file')
test(fillToBlockSize(strToBytes(messageLongFile.read())))




# def testEcb(message: bytes):
#     start = time()
#     messageEncrypted = aesEncodeEcb(strToBytes(message), KEY)
#     stop = time()
#     print('ECB encoding: ', stop - start)
#     start = time()
#     aesDecodeEcb(messageEncrypted, KEY)
#     stop = time()
#     print('ECB decoding: ', stop - start)

# def testCbc(message: bytes):
#     start = time()
#     messageEncrypted = aesEncodeCbc(strToBytes(message), KEY, IV)
#     stop = time()
#     print('CBC encoding: ', stop - start)
#     start = time()
#     aesDecodeCbc(messageEncrypted, KEY, IV)
#     stop = time()
#     print('CBC decoding: ', stop - start)

# def testPbc(message: bytes):
#     start = time()
#     messageEncrypted = aesEncodePbc(strToBytes(message), KEY, IV)
#     stop = time()
#     print('PBC encoding: ', stop - start)
#     start = time()
#     aesDecodePbc(messageEncrypted, KEY, IV)
#     stop = time()
#     print('PBC decoding: ', stop - start)

# print('for short file (about 5000 bytes)')
# messageShort = messageShortFile.read()
# testEcb(messageShort)
# testCbc(messageShort)
# testPbc(messageShort)

# print('for medium file (about 50 000 bytes)')
# messageMedium = messageMediumFile.read()
# testEcb(messageMedium)
# testCbc(messageMedium)
# testPbc(messageMedium)

# print('for long file (about 500 000 bytes)')
# messageLong = messageLongFile.read()
# testEcb(messageLong)
# testCbc(messageLong)
# testPbc(messageLong)

messageShortFile.close()
messageMediumFile.close()
messageLongFile.close()