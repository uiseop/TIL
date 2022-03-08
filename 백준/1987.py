import sys

input = sys.stdin.readline

def dfs(r,c,cnt):
    global ans
    if cnt == 26:
        ans = cnt
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and not visited[board[nr][nc]]:
            visited[board[nr][nc]] = True
            ans = max(ans, cnt+1)
            dfs(nr,nc,cnt+1)
            visited[board[nr][nc]] = False

dr = [1,-1,0,0]
dc = [0,0,1,-1]

n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(input().rstrip()))

visited = {chr(i):False for i in range(65, 91)}
visited[board[0][0]] = True
ans = 0
dfs(0,0,1)
print(ans)