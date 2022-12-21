from utils import *

p = findFourDigitPrime()
q = findFourDigitPrime()
n = p * q
phi = (p - 1) * (q - 1)
e = findE(phi)
d = findD(e, phi)

print('p', p)
print('q', q)
print('n', n)
print('phi', phi)
print('e', e)
print('d', d)

print('public key: ', e, n)
print('private key: ', d, n)

file = open('keys.txt', 'w')
file.write(f'public key {e} {n}\n')
file.write(f'private key {d} {n}')