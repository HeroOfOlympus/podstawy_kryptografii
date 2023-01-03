from utils import *
from pathlib import Path

path = Path.cwd()
print(path)

privateKeyA= input('private key A: ')
privateKeyB= input('private key B: ')
eStrA, nStrA = privateKeyA.split(' ')
eStrB, nStrB = privateKeyB.split(' ')
dA, nA = int(eStrA), int(nStrA)
dB, nB = int(eStrB), int(nStrB)

messageFile = open('./message.txt', 'r')
messageEncryptedFileA = open('message_encrypted_a.txt', 'w')
messageEncryptedFileB = open('message_encrypted_b.txt', 'w')

message = messageFile.read()
messageArray = [ord(c) for c in message]

messageEncryptedA = rsaCrypt(messageArray, dA, nA)
messageEncryptedB = rsaCrypt(messageArray, dB, nB)

messageEncryptedFileA.writelines([str(m) + '\n' for m in messageEncryptedA])
messageEncryptedFileB.writelines([str(m) + '\n' for m in messageEncryptedB])

messageFile.close()
messageEncryptedFileA.close()
messageEncryptedFileB.close()