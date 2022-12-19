import random

def generateBbs(n: int, length: int, a: int):
    array = []
    b = (a * a) % n
    array.append(lastBitValue(b))
    for i in range(length - 1):
        b = (b * b) % n
        array.append(lastBitValue(b))
    return array

def getRandomBloomNumber() -> int:
    a, b = 0, 0
    while a == 0:
        x = findNextPrime(random.randint(10000, 20000))
        if is4Mod3(x):
            a = x
    while b == 0:
        x = findNextPrime(random.randint(10000, 20000))
        if is4Mod3(x):
            b = x
    return a * b

def lastBitValue(a: int) -> int:
    return a % 2

def nwd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def is4Mod3(a: int) -> bool:
    return a % 4 == 3

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

def fileToArray(file):
    array = []
    while True:
        x = file.read(1)
        if not x:
            break
        array.append(int(x))
    return array

def bitArrayXor(a, b):
    if len(a) == len(b):
        return list(map(lambda x, y: xor(x, y), a, b))

def xor(a, b):
    if a != b:
        return 1
    return 0