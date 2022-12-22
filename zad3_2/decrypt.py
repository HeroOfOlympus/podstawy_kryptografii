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

messageA = rsaCrypt([int(m) for m in messageEncryptedA], eA, nA)
messageB = rsaCrypt([int(m) for m in messageEncryptedB], eB, nB)

def messageArrayToMessage(messageArray):
    message = ''
    for m in messageArray:
        message += chr(m)
    return message
print('A: ', messageArrayToMessage(messageA))
print('B: ', messageArrayToMessage(messageB))

messageEncryptedFileA.close()
messageEncryptedFileB.close()