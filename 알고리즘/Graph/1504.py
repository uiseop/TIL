import heapq
import sys
input = sys.stdin.readline

class Graph:
    def __init__(self):
        self.items = {}

    def addVertex (self, v):
        self.items[v] = {}
    
    def addEdge (self,v1,v2,w):
        if self.items[v1].get(v2):
            self.items[v1][v2] = w if w < self.items[v1][v2] else self.items[v1][v2]
        else:
            self.items[v1][v2] = w
    
    def dijkstra(self, start, target, N):
        distance = {}
        edges = {}
        heap = [[0, start]]
        for i in range(1,N+1):
            distance[i] = float("inf")
            edges[i] = self.items[i].copy()
        distance[start] = 0
        while heap:
            dist, node = heapq.heappop(heap)
            if edges.get(node):
                for n_node, weight in edges[node].items():
                    if distance[n_node] > dist + weight:
                        distance[n_node] = dist + weight
                        heapq.heappush(heap,[distance[n_node], n_node])
                del edges[node]

        return distance[target]

n,e = map(int,input().split())
graph = Graph()
for i in range(1,n+1):
    graph.addVertex(i)

for _ in range(e):
    v1,v2,w = map(int,input().split())
    graph.addEdge(v1,v2,w)
    graph.addEdge(v2,v1,w)

v1,v2 = map(int,input().split())
answer = min(graph.dijkstra(1,v1,n) + graph.dijkstra(v1,v2,n) + graph.dijkstra(v2,n,n),graph.dijkstra(1,v2,n) + graph.dijkstra(v2,v1,n) + graph.dijkstra(v1,n,n))

if answer == float("inf"):
    print(-1)
else:
    print(answer)