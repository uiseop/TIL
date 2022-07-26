import heapq
import sys

input = sys.stdin.readline

N,E = map(int,input().split())

graph = [{} for _ in range(N+1)]
for _ in range(E):
    v1,v2,w = map(int,input().split())
    if v2 in graph[v1]:
        graph[v1][v2] = min(graph[v1][v2], w)
        graph[v2][v1] = min(graph[v2][v1], w)
    else:
        graph[v1][v2] = w
        graph[v2][v1] = w

def dijkstra(start, target):
    dist = [float("inf") for _ in range(N+1)]
    dist[start] = 0
    heap = [[0,start]]
    while heap:
        weight, node = heapq.heappop(heap)
        for n_node, n_weight in graph[node].items():
            if dist[n_node] > weight + n_weight:
                dist[n_node] = weight + n_weight
                heapq.heappush(heap, [dist[n_node], n_node])
    return dist[target]

n1,n2 = map(int,input().split())

dist_start = dijkstra(1)
dist_n1 = dijkstra(n1)
dist_n2 = dijkstra(n2)

answer = min(dist_start[n1] + dist_n1[n2] + dist_n2[N], dist_start[n2] + dist_n2[n1] + dist_n1[N])

print(answer if answer != float("inf") else -1)

