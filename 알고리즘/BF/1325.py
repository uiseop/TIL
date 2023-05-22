from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = defaultdict(list)

for _ in range(m):
  v2,v1 = map(int,input().split())
  graph[v1].append(v2)

heap = []

visited = [False for _ in range(n+1)]

def isAllVisited(start):
  for node in graph[start]:
    if visited[node]:
      continue
    else:
      return False
  return True

def dfs(start,cnt,root):
  if not graph[start] or isAllVisited(start):
    heapq.heappush(heap, [-cnt, root])
    return
  for node in graph[start]:
    visited[node] = True
    dfs(node, cnt + 1,root)
    visited[node] = False

for start in range(1, n+1):
  if not graph[start]: continue
  visited[start] = True
  dfs(start,0,start)
  visited[start] = False

result = []

max_cnt = 0

sets = set()

while heap:
  cnt, node = heapq.heappop(heap)
  if node in sets: continue
  sets.add(node)

  cnt *= -1
  max_cnt = max(max_cnt, cnt)

  if max_cnt == cnt:
    result.append(node)
  else:
    break

result.sort()
print(result)