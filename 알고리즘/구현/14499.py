from collections import deque
import sys

input = sys.stdin.readline
n,m, x,y, k = map(int,input().split())

Map = list(list(map(int,input().split())) for _ in range(n))
ops = list(map(int,input().split()))

dir = [(0,0), (0,1), (0,-1), (-1,0), (1,0)]

dice_row = deque([4,1,3])
dice_col = deque([2,1,5])
dice_top = 6
cur = dice_row[1]
dice = [0 for _ in range(7)]

def getCalculatedXY(d,x,y):
    nx,ny = x + dir[d][0], y + dir[d][1]
    return nx,ny

def getRolledCur(d):
    global dice_top
    if d == 1:
        p_num = dice_row.popleft()
        dice_row.append(dice_top)
        dice_top = p_num
        dice_col[1] = dice_row[1]
    elif d == 2:
        p_num = dice_row.pop()
        dice_row.appendleft(dice_top)
        dice_top = p_num
        dice_col[1] = dice_row[1]
    elif d == 3:
        p_num = dice_col.pop()
        dice_col.appendleft(dice_top)
        dice_top = p_num
        dice_row[1] = dice_col[1]
    elif d == 4:
        p_num = dice_col.popleft()
        dice_col.append(dice_top)
        dice_top = p_num
        dice_row[1] = dice_col[1]
    return dice_row[1]

for op in ops:
    if 0 <= x + dir[op][0] < n and 0 <= y + dir[op][1] < m:
        cur = getRolledCur(op)
        x,y = getCalculatedXY(op,x,y)
        if Map[x][y] == 0:
            Map[x][y] = dice[cur]
        else:
            dice[cur] = Map[x][y]
            Map[x][y] = 0
        print(dice[dice_top])