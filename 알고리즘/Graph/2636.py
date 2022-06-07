from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

dr = [1,-1,0,0]
dc = [0,0,1,-1]

cheeses = list(list(map(int,input().split())) for _ in range(n))
count = 0

def findOutAir():
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    for r in range(n):
        for c in range(m):
            if not visited[r][c] and cheeses[r][c] == 0:
                visited[r][c] = 1
                q.append([r,c])
                while q:
                    row,col = q.popleft()
                    for i in range(4):   
                        nr = row + dr[i]
                        nc = col + dc[i]
                        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and cheeses[nr][nc] == 0:
                            visited[nr][nc] = 1
                            q.append([nr,nc])
                return visited
    return visited

while sum(sum(cheese) for cheese in cheeses) != 0:
    count += 1
    visited = [[False for _ in range(n)] for _ in range(m)]
    outAir = findOutAir()
    meltings = []
    for r in range(n):
        for c in range(m):
            if cheeses[r][c]:
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if outAir[nr][nc]:
                        meltings.append([r,c])
                        break
    
    for r,c in meltings:
        cheeses[r][c] = 0
    

print(count)
print(len(meltings))