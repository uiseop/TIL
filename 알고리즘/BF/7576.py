from collections import deque


M,N = map(int,input().split())

tomatoes = []

for _ in range(N):
  tomatoes.append(list(map(int,input().split())))

totalCounts = 0
curTomatoes = 0

completedTomatoes = deque()
visited = [[False for _ in range(M)] for _ in range(N)]

for r in range(N):
  for c in range(M):
    if tomatoes[r][c] == 0 or tomatoes[r][c] == 1:
      if tomatoes[r][c] == 1:
        completedTomatoes.append([r,c, 0])
        visited[r][c] = True
        curTomatoes += 1
      totalCounts += 1

DIR = [(1,0), (-1,0), (0,-1), (0,1)]

while completedTomatoes:
  r,c,curTime = completedTomatoes.popleft()

  for dr,dc in DIR:
    nr = r + dr
    nc = c + dc

    if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not tomatoes[nr][nc]:
      completedTomatoes.append([nr,nc,curTime+1])
      curTomatoes += 1
      visited[nr][nc] = True
      tomatoes[nr][nc] = 1

print(curTime) if curTomatoes == totalCounts else print(-1)