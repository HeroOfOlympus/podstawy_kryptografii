from utils import *

KEY = b'sixteen byte key'
IV = b'fdsadafdsafdadaf'

messageFile = open('message.txt', 'r')
messageStr = messageFile.read()
message = strToBytes(messageStr)

modes = [
    0, # ecb
    1, # cbc
    2  # pbc
]

def test(message: bytes, aesMode: int):
    print('')
    def decode(em: bytes, m: int) -> bytes:
        if m == 0:
            return unfill(aesDecodeEcb(em, KEY))
        elif m == 1:
            return unfill(aesDecodeCbc(em, KEY, IV))
        else:
            return unfill(aesDecodePbc(em, KEY, IV))
    encodedMessage = b''
    if aesMode == 0:
        print('EBC')
        encodedMessage = aesEncodeEcb(message, KEY)
    elif aesMode == 1:
        print('CBC')
        encodedMessage = aesEncodeCbc(message, KEY, IV)
    else:
        print('PBC')
        encodedMessage = aesEncodePbc(message, KEY, IV)

    print('unaffected       ', decode(encodedMessage, aesMode))
    print('dropWholeBlock   ', decode(dropWholeBlock(encodedMessage), aesMode))
    print('duplicateOneBlock', decode(duplicateOneBlock(encodedMessage), aesMode))
    print('flipBlocks       ', decode(flipBlocks(encodedMessage), aesMode))
    print('changeOneByte    ', decode(changeOneByte(encodedMessage), aesMode))
    print('flipBytesInBlock ', decode(flipBytesInBlock(encodedMessage), aesMode))
    print('deleteOneByte    ', decode(deleteOneByte(encodedMessage), aesMode))
    print('')

# drop second block from the end
def dropWholeBlock(encryptedMessage: bytes) -> bytes:
    blocks = sliceIntoBlocks(encryptedMessage)
    return joinBlocks(blocks[:-2] + blocks[-1:])

# duplicate second block from the end
def duplicateOneBlock(encryptedMessage: bytes) -> bytes:
    blocks = sliceIntoBlocks(encryptedMessage)
    return joinBlocks(blocks[0:-2] + [blocks[-1]] + blocks[-1:])

# flip blocks
def flipBlocks(encryptedMessage: bytes) -> bytes:
    blocks = sliceIntoBlocks(encryptedMessage)
    return joinBlocks(blocks[0:-3] + [blocks[-2]] + [blocks[-3]] + blocks[-1:])

# change one byte
def changeOneByte(encryptedMessage: bytes) -> bytes:
    blocks = sliceIntoBlocks(encryptedMessage)
    block = blocks[-2]
    # print(block)
    # print(block[:-1])
    newBlock = block[:-1] + b'X'
    # print('BLOCK', x)
    return joinBlocks(blocks[:-3] + [newBlock] + blocks[:-1])

# flip bytes in block
def flipBytesInBlock(encryptedMessage: bytes) -> bytes:
    blocks = sliceIntoBlocks(encryptedMessage)
    return joinBlocks(blocks[0:-2] + [blocks[-1][::-1]] + blocks[-1:])

# delete one byte
def deleteOneByte(encryptedMessage: bytes) -> bytes:
    blocks = sliceIntoBlocks(encryptedMessage)
    block = blocks[-2]
    block = block[0:-2]
    return joinBlocks(blocks)

for mode in modes:
    test(message, mode)


# blocks = [1,2,3,4,5,6,7,8]
# print(blocks[:-2] + blocks[-1:])