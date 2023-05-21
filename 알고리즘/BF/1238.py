from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

n,m,x = map(int,input().split())

inf = float("INF")

edges = defaultdict(list)

for _ in range(m):
  v1,v2,w = map(int,input().split())
  edges[v1].append([v2,w])

def dijkstra(start, end):
  dist = [inf for _ in range(n+1)]
  dist[start] = 0
  heap = []

  for node, weight in edges[start]:
    dist[node] = weight
    heapq.heappush(heap, [weight, node])
  
  while heap:
    weight, node = heapq.heappop(heap)
    if node == end:
      return weight

    for nextNode,nextWeight in edges[node]:
      totalWeight = weight + nextWeight
      if totalWeight < dist[nextNode]:
        dist[nextNode] = totalWeight
        heapq.heappush(heap, [totalWeight, nextNode])
  
  return dist

answer = 0

for i in range(1,n+1):
  party_dist = dijkstra(x, -1)

for i in range(1,n+1):
  if i == x: continue
  answer = max(answer, dijkstra(i,x) + party_dist[i])

print(answer)