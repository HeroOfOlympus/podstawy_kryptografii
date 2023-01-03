from utils import *

publicKeyA= input('public key A: ')
publicKeyB= input('public key B: ')
eStrA, nStrA = publicKeyA.split(' ')
eStrB, nStrB = publicKeyB.split(' ')
eA, nA = int(eStrA), int(nStrA)
eB, nB = int(eStrB), int(nStrB)

messageEncryptedFileA = open('message_encrypted_a.txt', 'r')
messageEncryptedFileB = open('message_encrypted_b.txt', 'r')

messageEncryptedA = messageEncryptedFileA.read().splitlines()
messageEncryptedB = messageEncryptedFileB.read().splitlines()

messageAwithA = rsaCrypt([int(m) for m in messageEncryptedA], eA, nA)
messageAwithB = rsaCrypt([int(m) for m in messageEncryptedA], eB, nB)
messageBwithB = rsaCrypt([int(m) for m in messageEncryptedB], eB, nB)
messageBwithA = rsaCrypt([int(m) for m in messageEncryptedB], eA, nA)

def messageArrayToMessage(messageArray):
    message = ''
    for m in messageArray:
        try:
            message += chr(m)
        except ValueError:
            message += '#'
    return message

print('A with key A: ', messageArrayToMessage(messageAwithA))
print('A with key B: ', messageArrayToMessage(messageAwithB))
print('B with key B: ', messageArrayToMessage(messageBwithB))
print('B with key A: ', messageArrayToMessage(messageBwithA))

messageEncryptedFileA.close()
messageEncryptedFileB.close()