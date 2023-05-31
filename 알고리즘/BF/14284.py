from collections import defaultdict
import heapq


n,m = map(int,input().split())
INF = float("INF")
graph = defaultdict(list)

for _ in range(m):
  v1,v2,w = map(int,input().split())
  graph[v1].append([v2,w])
  graph[v2].append([v1,w])

def dijkstra(start, end):
  dist = [INF for _ in range(n+1)]
  dist[start] = 0

  heap = []

  for node,weight in graph[start]:
    dist[node] = weight
    heapq.heappush(heap, [weight, node])
  
  while heap:
    w, v = heapq.heappop(heap)
    if v == end:
      return w
    for node, weight in graph[v]:
      if dist[node] > w + weight:
        dist[node] = w + weight
        heapq.heappush(heap, [dist[node], node])

s,t = map(int,input().split())

print(dijkstra(s,t))