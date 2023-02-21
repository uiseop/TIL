from math import sqrt
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
nums = []

answer = 0

for _ in range(n):
    in_nums = list(map(int, list(input().rstrip())))
    nums.append(in_nums)

def isPossible(selected):
    if len(selected) == 1: return True
    dr = abs(selected[0][0] - selected[1][0])
    dc = abs(selected[0][1] - selected[1][1])
    for i in range(1, len(selected)-1):
        if abs(selected[i][0] - selected[i+1][0]) == dr and abs(selected[i][1] - selected[i+1][1]) == dc:
            continue
        break
    else:
        return True
    return False

def getPerfectNumber(selected):
    global answer
    temp = ''
    for r,c in selected:
        temp += str(nums[r][c])
    if int(sqrt(int(temp))) ** 2 == int(temp):
        answer = max(answer, int(temp))
    return

for i in range(n):
    for j in range(m):
        for a in range(-n, n):
            for b in range(-m, m):
                