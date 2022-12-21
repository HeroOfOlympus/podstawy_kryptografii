messageEncryptedFile = open('message_encrypted.txt', 'r')
messageEncrypted = messageEncryptedFile.read().splitlines()

publicKey = input('private key: ')
dStr, nStr = publicKey.split(' ')
d, n = int(dStr), int(nStr)

messageArray = [chr(pow(int(c), d, n)) for c in messageEncrypted]
message = ''
for m in messageArray:
    message += m
print(message)