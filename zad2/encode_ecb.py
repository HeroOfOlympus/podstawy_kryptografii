from utils import *
from aes_ecb import AES_ECB

msg = input('message: ')
pwd = input('key: ')

file = open('encoded_aes_ecb.txt', 'wb')

c = AES_ECB(pwd).encrypt(msg)

decoded = AES_ECB(pwd).decrypt(c)
printSeparated(c)

file.write(c)

file.close()