from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

v,e = map(int,input().split())

graph = defaultdict(list)

dist = [[float("inf") for _ in range(v+1)] for _ in range(v+1)]

heap = []

for _ in range(e):
    v1,v2,w = map(int,input().split())
    graph[v1].append([v2,w])
    dist[v1][v2] = w
    heapq.heappush(heap, [w,v1,v2])

while heap:
    weight, target, cur = heapq.heappop(heap)

    if target == cur:
        print(weight)
        break

    for n_node, n_weight in graph[cur]:
        n_dist = weight + n_weight
        if dist[target][n_node] > n_dist:
            dist[target][n_node] = n_dist
            heapq.heappush(heap, [n_dist, target, n_node])

else:
    print(-1)