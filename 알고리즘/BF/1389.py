from collections import defaultdict
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = defaultdict(list)

for _ in range(m):
  v1,v2 = map(int,input().split())
  v1 -= 1
  v2 -= 1
  graph[v1].append(v2)
  graph[v2].append(v1)

inf = float("INF")

dist = [[inf for _ in range(n)] for _ in range(n)]

for key in graph:
  for node in graph[key]:
    dist[key][node] = 1

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i == j: continue
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

result = inf
answer = 0

for i in range(n):
  cur = result
  result = min(result, sum(dist[i][:i]) + sum(dist[i][i+1:]))
  if cur != result:
    answer = i

print(answer + 1)