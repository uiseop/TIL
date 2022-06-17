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
            jihoon.append([r,c])
            visited[r][c] = 1

Escape = False

while jihoon:
    for v in visited:
        print(v)
    print("")
    temp_fire = deque()
    r,c = jihoon.popleft()
    if (r == 0 or r == R) and (c ==0 or c == C):
        Escape = visited[r][c]
        break
    visited[r][c] = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
            visited[nr][nc] = visited[r][c] + 1
            jihoon.append([nr,nc])
    
    while fire:
        r,c = fire.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                visited[nr][nc] = True
                temp_fire.append([nr,nc])
    
    fire = temp_fire

if Escape:
    print(Escape + 1)
else:
    print("IMPOSSIBLE")