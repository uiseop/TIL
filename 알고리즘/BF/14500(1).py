import sys

input = sys.stdin.readline

N,M = map(int,input().split())

points = []

for _ in range(N):
    points.append(list(map(int,input().split())))

dr = [1,-1,0,0]
dc = [0,0,1,-1]
max_val = max(map(max, points))

visited = [[False for _ in range(M)] for _ in range(N)]

def getTetromino():
    result = [0]
    def dfs(r,c, step, total):
        if result[0] >= total + max_val * (3-step):
            return
        if step == 3:
            result[0] = max(result[0], total)
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if step == 1:
                    visited[nr][nc] = True
                    dfs(r,c, step+1, total+points[nr][nc])
                    visited[nr][nc] = False
                visited[nr][nc] = True
                dfs(nr,nc, step+1, total+points[nr][nc])
                visited[nr][nc] = False
    
    for r in range(N):
        for c in range(M):
            visited[r][c] = True
            dfs(r,c,0,points[r][c])
            visited[r][c] = False

    return result[0]

print(getTetromino())