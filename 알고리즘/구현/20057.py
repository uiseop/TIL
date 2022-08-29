from math import floor
import sys

input = sys.stdin.readline

n = int(input())

cur = [n // 2, n // 2]

dir = [(0,-1), (1,0), (0,1), (-1,0)] # 왼 밑 오 위

dusts = list(list(map(int,input().split())) for _ in range(n))

dustPercent = [
    [0, 0, 0.02, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, 0.45, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]
]

result = 0

def rotateDustPercent():
    tempDust = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tempDust[i][j] = dustPercent[i][j]
    
    for i in range(5):
        for j in range(5):
            dustPercent[5 - (j+1)][i] = tempDust[i][j]

def getLeftDust(y):
    return y - (floor(y * 0.01) * 2 + floor(y*0.02) * 2 + floor(y*0.07)*2 + floor(y*0.1)*2 + floor(y*0.05))
            
def moveDust(row, col):
    global result
    y = dusts[row][col]
    dusts[row][col] = 0

    if y == 0: return

    for i in range(-2, 3):
        for j in range(-2, 3):
            percent = dustPercent[i+2][j+2]

            if percent == 0: continue

            movedDust = 0
            if percent < 0.4:
                movedDust = floor(y * percent)
            else:
                movedDust = getLeftDust(y)
            
            r = row + i
            c = col + j

            if (r < 0 or r >= n or c < 0 or c >= n):
                result += movedDust
            else:
                dusts[r][c] += movedDust

cnt = 1
d = 0

while cur[0] + cur[1] != 0:
    for i in range(2):
        for j in range(cnt):
            cur[0] += dir[d][0]
            cur[1] += dir[d][1]

            moveDust(cur[0], cur[1])

            if cur[0] == 0 and cur[1] == 0:
                print(result)
                exit()
        
        d = (d+1) % 4
        rotateDustPercent()
    
    cnt += 1
