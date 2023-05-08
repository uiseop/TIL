from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

n,d = map(int,input().split())

graph = defaultdict(list)

for i in range(d+1):
  graph[i].append([i+1, 1])

for _ in range(n):
  v1, v2, w = map(int,input().split())
  if v2 > d: continue

  graph[v1].append([v2,w])

inf = float("INF")

dist = [inf for _ in range(d+1)]
dist[0] = 0

def dijkstra(start):
  heap = []

  heapq.heappush(heap, [0, start])
  
  while heap:
    weight, start = heapq.heappop(heap)

    if weight > dist[start]: continue

    if start == d:
      print(weight)
      return
    
    for node, w in graph[start]:
      if dist[node] > weight + w:
        dist[node] = weight + w
        heapq.heappush(heap, [dist[node], node])

dijkstra(0)
