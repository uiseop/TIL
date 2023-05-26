from collections import deque


N,M = map(int,input().split())

room = list(list(map(int,input().split())) for _ in range(N))

winds = deque()
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
  for j in range(M):
    if room[i][j] == 9:
      winds.append([i,j,0])
      winds.append([i,j,1])
      winds.append([i,j,2])
      winds.append([i,j,3])
      visited[i][j] = True

dir = [(1,0), (-1,0), (0,1), (0,-1)] # 0:하, 1:상, 2:우, 3:좌

def changeDir(wall, curDirection):
  if curDirection == 0:
    if wall == 1: return curDirection
    if wall == 2: return 1
    if wall == 3: return 3
    if wall == 4: return 2
  if curDirection == 1:
    if wall == 1: return curDirection
    if wall == 2: return 0
    if wall == 3: return 2
    if wall == 4: return 3
  if curDirection == 2:
    if wall == 1: return 3
    if wall == 2: return curDirection
    if wall == 3: return 1
    if wall == 4: return 0
  if curDirection == 3:
    if wall == 1: return 2
    if wall == 2: return curDirection
    if wall == 3: return 0
    if wall == 4: return 1

answer = 0

while winds:
  r,c,d = winds.popleft()
  nr = r + dir[d][0]
  nc = c + dir[d][1]

  if 0 <= nr < N and 0 <= nc < M:
    if room[nr][nc] == 9:
      continue
    visited[nr][nc] = True
    if room[nr][nc]:
      curDirection = changeDir(room[nr][nc], d)
      winds.append([nr,nc, curDirection])
    else:
      winds.append([nr,nc,d])


for v in visited:
  answer += v.count(True)

print(answer)