import sys

input = sys.stdin.readline

N = int(input())

alpha = [0 for _ in range(26)]
result = []

def alphaToNum(s):
    _s = s.upper()
    num = ord(_s) - 65
    return num

def setFirstWordPossible(words):
    lst = words.split()

    for word in lst:
        w = alphaToNum(word[0])
        if alpha[w]:
            continue
        else:
            alpha[w] = True
            wordIndex = words.index(word)
            result.append(words[:wordIndex] + '[' + words[wordIndex][0] + ']' + words[wordIndex][1:] + words[wordIndex+1:])
            return True
    else:
        return False

def setWord(words):
    lst = words.split()

    for word in lst:
        for _w in word:
            w = alphaToNum(_w)
            if alpha[w]:
                continue
            else:
                alpha[w] = True
                wordIndex = words.index(_w)
                result.append(words[:wordIndex] + '[' + words[wordIndex][0] + ']' + words[wordIndex][1:] + words[wordIndex+1:])
                return
    result.append(words)

for _ in range(N):
    words = input().rstrip()

    if not setFirstWordPossible(words):
        setWord(words)

for r in result:
    print(r)