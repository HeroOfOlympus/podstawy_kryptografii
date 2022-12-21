from utils import *

def generateKey(suffix):
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

    file = open(f'keys_{suffix}.txt', 'w')
    file.write(f'public key {e} {n}\n')
    file.write(f'private key {d} {n}')

generateKey('a')
generateKey('b')