from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

potal = defaultdict(int)

for _ in range(n+m):
  x,y = map(int,input().split())
  potal[x] = y

pan = [False for _ in range(101)]

heap = [[0, 1]]
pan[1] = True

while heap:
  cnt, pos = heapq.heappop(heap)

  if pos == 100:
    print(cnt)
    exit()

  for i in range(1,7):
    next_pos = pos + i
    if next_pos > 100: continue
    if potal[next_pos]:
      next_pos = potal[next_pos]
    if pan[next_pos]: continue
    pan[next_pos] = True
    heapq.heappush(heap, [cnt+1, next_pos])