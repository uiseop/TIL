from collections import deque
import sys

dr = [1,-1,0,0]
dc = [0,0,1,-1]

input = sys.stdin.readline

n,m = map(int,input().split())

picture = list(list(map(int, input().split())) for _ in range(n))
visited = [[False for _ in range(m)] for _ in range(n)]
count = 0
answer = 0

def inRange(r,c):
    if 0 <= r < n and 0 <= c < m:
        return True
    return False

for r in range(n):
    for c in range(m):
        if picture[r][c] and not visited[r][c]:
            visited[r][c] = True
            count += 1
            temp = 1
            q = deque([[r,c]])
            while q:
                row, col = q.popleft()
                for i in range(4):
                    nr = row + dr[i]
                    nc = col + dc[i]
                    if inRange(nr,nc) and not visited[nr][nc] and picture[nr][nc]:
                        visited[nr][nc] = True
                        temp += 1
                        q.append([nr,nc])
            answer = max(answer, temp)

print(count)
print(answer)