from collections import deque
import sys
input = sys.stdin.readline

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs(r,c):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[r][c] = True
    dist = deque()
    dist.append([r,c])
    d = -1
    while dist:
        size = len(dist)
        for _ in range(size):
            row,col = dist.popleft()
            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and land[nr][nc] == "L":
                    visited[nr][nc] = True
                    dist.append([nr,nc])
        d += 1
    return d
                        
n,m = map(int,input().split())
land = list(list(input().rstrip()) for _ in range(n))
answer = 0
for r in range(n):
    for c in range(m):
        if land[r][c] == "L":
            answer = max(answer, bfs(r,c))

print(answer)