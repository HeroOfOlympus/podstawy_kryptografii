from Crypto.Cipher import AES

BLOCK_SIZE = 16
CHARACTER_ENCODING = 'utf-8'
BYTEORDER_FOR_DECODING = 'big'

def fillToBlockSize(b: bytes) -> bytes:
    if len(b) % BLOCK_SIZE == 0:
        # print(len(b))
        return b
    x = (BLOCK_SIZE - len(b) % BLOCK_SIZE)
    y = (BLOCK_SIZE - len(b) % BLOCK_SIZE).to_bytes(1, BYTEORDER_FOR_DECODING)
    # print(len(b), BLOCK_SIZE, x, y)
    return b + x * y

def unfill(b: bytes) -> bytes:
    x = len(b) - 1
    y = b[x:]
    z = int.from_bytes(y, BYTEORDER_FOR_DECODING)
    return b[:-z]

def printSeparated(content: str):
    for dada in [content[i:i + BLOCK_SIZE] for i in range(0, len(content), BLOCK_SIZE)]:
        print(dada)

def bytesXor(a: bytes, b: bytes) -> bytes:
    return bytes([_a ^ _b for _a, _b in zip(a, b)])

def strToBytes(text: str) -> bytes:
    return text.encode(CHARACTER_ENCODING)

def bytesToStr(bytes: bytes) -> str:
    return bytes.decode(CHARACTER_ENCODING)

def joinBlocks(blocks) -> bytes:
    x = b''
    for i in range(len(blocks)):
        x += blocks[i]
    return x

def sliceIntoBlocks(b: bytes):
    return [b[i:i + BLOCK_SIZE] for i in range(0, len(b), BLOCK_SIZE)]

##########################
# AES ECB
##########################

def aesEncodeEcb(message: bytes, key: bytes) -> bytes:
    filledKey = fillToBlockSize(key)
    filledMessage = fillToBlockSize(message)
    cipher = AES.new(filledKey, AES.MODE_ECB)
    return cipher.encrypt(filledMessage)

def aesDecodeEcb(encodedMessage: bytes, key: bytes) -> bytes:
    filledKey = fillToBlockSize(key)
    cipher = AES.new(filledKey, AES.MODE_ECB)
    message = cipher.decrypt(encodedMessage)
    return message

##########################
# AES CBC using ECB
##########################

def aesEncodeCbc(message: bytes, key: bytes, iv: bytes) -> bytes:
    filledKey = fillToBlockSize(key)
    filledMessage = fillToBlockSize(message)
    blocks = sliceIntoBlocks(filledMessage)

    [print(x, len(x)) for x in blocks]

    encodedBlocks = []
    encodedBlocks.append(aesEncodeEcb(bytesXor(blocks[0], iv), filledKey))
    for i in range(1, len(blocks)):
        xor = bytesXor(blocks[i], blocks[i - 1])
        print('dadada', xor)
        encodedBlocks.append(aesEncodeEcb(xor, filledKey))

    [print(x, len(x)) for x in encodedBlocks]

    return joinBlocks(encodedBlocks)

def aesDecodeCbc(encodedMessage: bytes, key: bytes, iv: bytes) -> bytes:
    filledKey = fillToBlockSize(key)
    encodedBlocks = sliceIntoBlocks(encodedMessage)

    # [print(x, len(x)) for x in encodedBlocks]

    blocks = []
    blocks.append(bytesXor(aesDecodeEcb(encodedBlocks[0], filledKey), iv))
    for i in range(1, len(encodedBlocks)):
        blocks.append(bytesXor(aesDecodeEcb(encodedBlocks[i], filledKey), blocks[i - 1]))

    # [print(x, len(x)) for x in blocks]

    return joinBlocks(blocks)

##########################
# AES PBC using ECB
##########################

def aesEncodePbc(message: bytes, key: bytes, iv: bytes) -> bytes:
    return

def aesDecodePbc(encryptedMessage: bytes, key: bytes, iv: bytes) -> bytes:
    return
    