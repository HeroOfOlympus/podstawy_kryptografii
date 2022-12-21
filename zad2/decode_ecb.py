from utils import *
from aes_ecb import AES_ECB

file = open('encoded_aes_ecb.txt', 'rb')
print('decoding from file encoded_aes_ecb.txt')
pwd = input('key: ')

content = file.read()
d = AES_ECB(pwd).decrypt(content)

print(d)

file.close()