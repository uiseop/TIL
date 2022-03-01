import sys
from collections import deque

def bfs(row, col):
    global cnt
    dq = deque([[row,col]])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cp = [[0 for _ in range(m)] for _ in range(n)]
    rest = 0
    while dq:
        r,c = dq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if cheese[nr][nc] > 0:
                    cp[nr][nc] += 1
                else:
                    visited[nr][nc] = 1
                    dq.append([nr,nc])
    for r in range(n):
        for c in range(m):
            if cp[r][c] >= 2:
                cheese[r][c] = 0
            elif cheese[r][c] == 1:
                rest += 1
    if rest:
        cnt += 1
        bfs(0,0)

dr = [1,-1,0,0]
dc = [0,0,1,-1]

input = sys.stdin.readline

n,m = map(int,input().split())

cheese = list(list(map(int,input().split())) for _ in range(n))
cnt = 0
bfs(0,0)

print(cnt + 1)