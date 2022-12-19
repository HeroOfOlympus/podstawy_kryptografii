from utils import bitArrayXor, fileToArray, getRandomBloomNumber, generateBbs

# bbs XOR decoded -> encoded
# bbs XOR encoded -> decoded

n = getRandomBloomNumber() # losowa duża liczba Blooma
a = 124321321313 # liczba naturalna taka ze NWD(a, n) = 1

filename = input("Nazwa pliku do zaszyfrowania/odszyfrowania [z rozszerzeniem]: ")
decode = input("Dekoduj [y/n]: ")

messageFile = open(filename, 'r')
resultFile = open('encoder_result.txt', 'w')

message = fileToArray(messageFile)

bbs = []
if decode == 'y':
    bbsFile = open('encoder_bbs.txt', 'r')
    bbs = fileToArray(bbsFile)
    bbsFile.close()
else:
    bbsFile = open('encoder_bbs.txt', 'w')
    bbs = generateBbs(n, len(message), a)
    for bit in bbs:
        bbsFile.write(str(bit))
    bbsFile.close()

result = bitArrayXor(message, bbs)

for bit in result:
    resultFile.write(str(bit))

messageFile.close()
bbsFile.close()
resultFile.close()
