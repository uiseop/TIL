import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
bing = list(list(map(int,input().split())) for _ in range(n))

dr = [1,-1,0,0]
dc = [0,0,1,-1]

year = 0
while True:
    melt = []
    cnt = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for row in range(1,n-1):
        dq = deque()
        for col in range(1,m-1):
            if bing[row][col] and not visited[row][col]:
                dq.append([row,col])
                cnt += 1
                while dq:
                    r,c = dq.popleft()
                    visited[r][c] = 1
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                            if bing[nr][nc] == 0:
                                melt.append([r,c])
                            else:
                                dq.append([nr,nc])
                for r,c in melt:
                    bing[r][c] -= 1
    if cnt == 0:
        year = 0
        break
    if cnt >= 2:
        break
    year += 1

print(year)
    
