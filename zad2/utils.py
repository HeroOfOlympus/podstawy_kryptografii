BLOCK_SIZE = 16
CHARACTER_ENCODING = 'utf-8'

def fillToBlockSize(s):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

def unfill(s):
    return s[:-ord(s[len(s) - 1:])]

def printSeparated(content: str):
    for dada in [content[i:i + BLOCK_SIZE] for i in range(0, len(content), BLOCK_SIZE)]:
        print(dada)