import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(arr, color):
    r,c = arr
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            if color == colors[nr][nc]:
                visited[nr][nc] = True
                dfs([nr,nc], color)


n = int(input())
colors = []
for _ in range(n):
    colors.append(list(input().rstrip()))

dr = [1,-1,0,0]
dc = [0,0,1,-1]
visited = [[False for _ in range(n)] for _ in range(n)]
origin = 0
nonOrigin = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            dfs([i,j], colors[i][j])
            origin += 1

for i in range(n):
    for j in range(n):
        if colors[i][j] == "G":
            colors[i][j] = "R"

visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            dfs([i,j], colors[i][j])
            nonOrigin += 1

print(origin, nonOrigin)