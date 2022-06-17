from collections import deque
import sys

input = sys.stdin.readline

R,C = map(int,input().split())
visited = [[False for _ in range(C)] for _ in range(R)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]

maze = []

jihoon = deque()
fire = deque()


for r in range(R):
    lst = list(input().rstrip())
    maze.append(lst)

for r in range(R):
    for c in range(C):
        if maze[r][c] == "#":
            visited[r][c] = True
        elif maze[r][c] == "F":
            visited[r][c] = True
            fire.append([r,c])
        elif maze[r][c] == "J":
            if r == 0 or r == R-1 or c == 0 or c == C-1:
                print(1)
                exit()
            jihoon.append([r,c])
            visited[r][c] = 1

Escape = False

while True:
    temp_fire = deque()
    temp_jihoon = deque()
    while fire:
        r,c = fire.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                visited[nr][nc] = True
                temp_fire.append([nr,nc])

    while jihoon:
        r,c = jihoon.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if nr == 0 or nr == R-1 or nc == 0 or nc == C-1:
                    visited[nr][nc] = visited[r][c] + 1
                    Escape = visited[nr][nc]
                    break
                visited[nr][nc] = visited[r][c] + 1
                temp_jihoon.append([nr,nc])
        if Escape:
            break
    
    if Escape:
        break
    if not temp_jihoon:
        break
    jihoon = temp_jihoon
    fire = temp_fire

if Escape:
    print(Escape)
else:
    print("IMPOSSIBLE")
