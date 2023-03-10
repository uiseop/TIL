from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

arr = list(list(map(int,input().split())) for _ in range(n))

visited = [[False for _ in range(m)] for _ in range(n)]

dir = [[1,0], [-1,0], [0,1], [0,-1]]

def bfs(row,col):
    dq = deque()
    dq.append([row,col])

    while dq:
        r,c = dq.popleft()

        for dr, dc in dir:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and arr[nr][nc]:
                visited[row][col] += 1
                visited[nr][nc] = [row, col]
                dq.append([nr,nc])

blocks = []

for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j]:
            visited[i][j] = 1
            bfs(i,j)
        elif not arr[i][j]:
            blocks.append([i,j])

maxLen = 0

for row,col in blocks:
    temp = 1
    setList = set()
    for dr, dc in dir:
        nr = row + dr
        nc = col + dc
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc]:
            if type(visited[nr][nc]) == type(1):
                setList.add((nr,nc))
            else:
                r,c = visited[nr][nc]
                setList.add((r,c))
    
    for r,c in setList:
        temp += visited[r][c]
    maxLen = max(maxLen, temp)

print(maxLen)