import heapq
import sys

input =sys.stdin.readline

dir = [(1,0), (-1,0), (0,1), (0,-1)]

def dijkstart():
  visited = [[False for _ in range(n)] for _ in range(n)]
  visited[0][0] = True
  r = 0
  c = 0

  heap = []
  heapq.heappush(heap, [maze[r][c], r,c])

  while heap:
    w, r,c = heapq.heappop(heap)

    if r == n-1 and c == n-1:
      print(f"Problem {cnt}: {w}")
      return

    for dr, dc in dir:
      nr = r + dr
      nc = c + dc
      if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
        visited[nr][nc] = True
        heapq.heappush(heap, [w + maze[nr][nc], nr,nc])

cnt = 1

while True:

  n = int(input())
  if not n:
    break

  maze = []

  for _ in range(n):
    maze.append(list(map(int,input().split())))
  
  dijkstart()
  cnt += 1


