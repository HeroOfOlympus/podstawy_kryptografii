import re
from utils import getRandomBloomNumber, generateBbs, nwd
from math import floor
from pathlib import Path

n = getRandomBloomNumber() # losowa duża liczba Blooma
print('Losowo wygenerowana liczba blooma: ', n)
r = 20000 # długość ciągu
a = 124321321313 # liczba naturalna taka ze NWD(a, n) = 1
print('NWD(a, n): ', nwd(a, n))

readFromFileInput = input('Czytać z pliku? [y/n]: ')

bArray = []
if readFromFileInput == 'y':
    file = open('bbs_input.txt', 'r')
    while True:
        x = file.read(1)
        if not x:
            break
        bArray.append(int(x))
    file.close
else:
    lengthInput = input('Podaj dlugosc [pomiń dla 20 000]: ')
    if len(lengthInput) > 0:
        r = int(lengthInput)
    file = open('bbs_output.txt', 'w')
    bArray = generateBbs(n, r, a)
    for bit in bArray:
        file.write(str(bit))
    file.close()

# test pojedynczych bitów
def singleBitsTest(bits) -> bool:
    ones, zeros = 0, 0
    for bit in bits[0:19999]:
        if bit == 1:
            ones += 1
        else:
            zeros += 1
    print('   dane testu pojedynczych bitów: liczba jedynek:', ones, ', liczba zer:', zeros)
    if 9725 <= ones <= 10275 and 9725 <= zeros <= 10275:
        return True
    return False

print("wynik testu pojedynczych bitów:", "SPELNIONY" if singleBitsTest(bArray) else "NIESPELNIONY")

# test serii
def seriesTest(bits) -> bool:
    series = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 }
    preOnes = 0 # dla testu serii liczone są ciągi następujących jedynek
    for bit in bits[0:19999]:
        if bit == 1:
            preOnes += 1
        elif bit == 0:
            if preOnes != 0 and preOnes <= 6:
                series[preOnes] += 1
            elif preOnes > 6:
                series[6] += 1
            preOnes = 0
    if preOnes != 0 and preOnes <= 6:
        series[preOnes] += 1
    elif preOnes > 6:
        series[6] += 1
    print('   dane dla testu serii:', series)

    if series[1] < 2315 and series[1] > 2685:
        if series[2] < 1114 and series[2] > 1386:
            if series[3] < 527 and series[3] > 723:
                if series[4] < 240 and series[4] > 384:
                    if series[5] < 103 and series[5] > 209:
                        if series[6] < 103 and series[6] > 209:
                            return False
    return True

print("wynik testu serii:             ", "SPELNIONY" if seriesTest(bArray) else "NIESPELNIONY")

# test długiej serii
def longSeriesTest(bits) -> bool:
    maxOnes, maxZeros, maxSeries = 0, 0, 0
    for bit in bits[0:19999]:
        if bit == 1:
            maxOnes += 1
            if maxZeros > maxSeries:
                maxSeries = maxZeros
            maxZeros = 0
        elif bit == 0:
            maxZeros += 1
            if maxOnes > maxSeries:
                maxSeries = maxOnes
            maxOnes = 0
    if maxZeros > maxSeries:
        maxSeries = maxZeros
    if maxOnes > maxSeries:
        maxSeries = maxOnes
    print('   dane dla testu długiej serii: liczba serii -', maxSeries)
    return maxSeries < 26
        
print("wynik testu dlugiej serii:     ", "SPELNIONY" if longSeriesTest(bArray) else "NIESPELNIONY")

# test pokerowy
def pokerTest(bits) -> bool:
    segments = {
        '0000': 0,
        '1000': 0,
        '0100': 0,
        '1100': 0,
        '0010': 0,
        '1010': 0,
        '0110': 0,
        '1110': 0,
        '0001': 0,
        '1001': 0,
        '0101': 0,
        '1101': 0,
        '0011': 0,
        '1011': 0,
        '0111': 0,
        '1111': 0
    }
    for index in range(floor(len(bits[0:19999]) / 4)):
        key = str(bits[index]) + str(bits[index + 1]) + str(bits[index + 2]) + str(bits[index + 3])
        segments[key] += 1
    sum = 0
    for key in segments:
        sum += segments[key] ** 2
    x = 16 / 5000 * sum - 5000
    print('   dane dla testu pokerowego: wygenerowana liczba X -', x)
    return x > 2.16 and x < 46.17

print("wynik testu pokerowego:        ",  "SPELNIONY" if pokerTest(bArray) else "NIESPELNIONY")


