import sys

input = sys.stdin.readline

L,C = map(int,input().split())

alpha = list(map(str, input().split()))
alpha.sort()

answer = 0

def isPrintable(word):
    mo = 0
    ja = 0
    for i in word:
        if i in ['a', 'e', 'i', 'o', 'u']:
            mo += 1
        else:
            ja += 1
    if mo and ja >= 2:
        return True
    return False

def backtrack(idx, word):
    global answer
    left = C - idx
    if left + len(word) < L:
        return
    if len(word) == L:
        if isPrintable(word):
            print(word)
        return
    
    backtrack(idx+1, word+alpha[idx])
    backtrack(idx+1, word)

backtrack(0, '')