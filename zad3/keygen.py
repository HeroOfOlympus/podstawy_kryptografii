from utils import *

p = findFourDigitPrime()
q = findFourDigitPrime()
n = p * q
phi = (p - 1) * (q - 1)
e = findE(phi)
d = 