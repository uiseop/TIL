from collections import deque

dr = [1,-1,0,0]
dc = [0,0,-1,1]

def bfs(row,col, color):
    dq = deque([[row,col]])
    while dq:
        r,c = dq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 12 and 0 <= nc < 6 and not visited[nr][nc] and yo[nr][nc] == color:
                visited[nr][nc] = 1 
                chain.append([nr,nc])
                dq.append([nr,nc])

def down():
    for r in range(10, -1, -1):
        for c in range(6):
            for k in range(11, r, -1):
                if yo[k][c] == '.' and yo[r][c] != '.':
                    yo[k][c] = yo[r][c]
                    yo[r][c] = '.'


yo = list(list(input()) for _ in range(12))

ans = 0

while True:
    isPang = False
    visited = [[0 for _ in range(6)] for _ in range(12)]
    for r in range(12):
        for c in range(6):
            if yo[r][c] != "." and visited[r][c] == 0:
                visited[r][c] = 1
                chain = [[r,c]]
                bfs(r,c, yo[r][c])
                if len(chain) >= 4:
                    isPang = True
                    for row,col in chain:
                        yo[row][col] = "."
    if not isPang:
        break
    down()
    ans += 1

print(ans)