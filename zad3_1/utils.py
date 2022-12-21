import random

def nwd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def findNextPrime(n: int) -> int:
    np = []
    primes = []
    for i in range (n + 1, n + 200):
        np.append(i)
    for j in np:
        isPrime = True
        for x in range(2, j - 1):
            if j % x == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(j)
    return min(primes)

def findFourDigitPrime():
    n = random.randint(1000,9999)
    while True:
        pn = findNextPrime(n)
        if pn < 10000:
            return pn
        n -= 1

def findE(n):
    while True:
        pn = findFourDigitPrime()
        if nwd(n, pn) == 1:
            return pn

def findD(e, phi):
    d = 1
    while True:
        # print(e, d, phi, (e * d) % phi)
        if (e * d) % phi == 1:
            return d
        d += 1