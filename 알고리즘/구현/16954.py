import sys

input = sys.stdin.readline

dir = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1), (0,0)]

def isNoWalls(walls):
    for wall in walls:
        if wall[0] >= 8: continue
        else: return False
    return True

def moveDownWalls(walls):
    for wall in walls:
        wall[0] += 1

def moveUpWalls(walls):
    for wall in walls:
        wall[0] -= 1

def backtrack(r,c):
    if r == 0 and c == 7:
        return True
    if isNoWalls(walls):
        return True

    result = False
    for dr,dc in dir:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < 8 and 0 <= nc < 8 and [nr,nc] not in walls and [nr-1, nc] not in walls:
            moveDownWalls(walls)
            result = backtrack(nr,nc)
            if result: break
            moveUpWalls(walls)

    return result

chess = []
walls = []

for _ in range(8):
    chess.append(list(input().rstrip()))

for i in range(8):
    for j in range(8):
        if chess[i][j] == '#':
            walls.append([i,j])

x,y = 7,0

print(1) if backtrack(x,y) else print(0)