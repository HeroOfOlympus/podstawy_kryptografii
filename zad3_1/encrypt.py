messageFile = open('message.txt', 'r')
messageEncryptedFile = open('message_encrypted.txt', 'w')

message = messageFile.read()
messageArray = [ord(c) for c in message]

print(messageArray)
publicKey = input('public key: ')
eStr, nStr = publicKey.split(' ')
e, n = int(eStr), int(nStr)
print(e, n)

messageEncrypted = [pow(m, e, n) for m in messageArray]

print(messageEncrypted)
messageEncryptedFile.writelines([str(m) + '\n' for m in messageEncrypted])

messageFile.close()
messageEncryptedFile.close()