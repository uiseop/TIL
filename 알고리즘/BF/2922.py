import sys

input = sys.stdin.readline

word = list(input().rstrip())

M = 'AEIOU'

def backTracking(i, ja, mo, lExist):
    if ja >= 3 or mo >= 3:
        return 0
    if i == len(word):
        return lExist
    result = 0
    if word[i] == "_":
        result += backTracking(i+1, ja + 1, 0, lExist) * 20
        result += backTracking(i+1, ja + 1, 0, 1)
        result += backTracking(i+1, 0, mo + 1, lExist) * 5
    else:
        if word[i] in M:
            result += backTracking(i+1, 0, mo + 1, lExist)
        else:
            if word[i] == "L":
                result += backTracking(i+1, ja + 1, 0, 1)
            else:
                result += backTracking(i + 1, ja + 1, 0, lExist)
    return result

print(backTracking(0,0,0,0))