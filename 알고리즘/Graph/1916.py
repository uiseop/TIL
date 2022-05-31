import heapq
import sys

input = sys.stdin.readline

class Graph:

    def __init__(self):
        self.items = {}
    
    def addVertex(self, v):
        self.items[v] = {}
    
    def addEdge(self, v1,v2,w):
        if self.items[v1].get(v2) != None:
            self.items[v1][v2] = min(self.items[v1][v2], w)
        else:
            self.items[v1][v2] = w

    def dijkstra(self, start, dest):
        distance = {}
        edges = {}
        for k in self.items.keys():
            distance[k] = float("inf")
            edges[k] = self.items[k].copy()

        distance[start] = 0
        heap = [[0, start]]
        while heap:
            dist, node = heapq.heappop(heap)
            if edges.get(node):
                for n_node, n_dist in edges[node].items():
                    if n_dist + dist < distance[n_node]:
                        distance[n_node] = n_dist + dist
                        heapq.heappush(heap, [distance[n_node], n_node])
                del edges[node]
        return distance[dest]


graph = Graph()

n = int(input())
m = int(input())

for i in range(1,n+1):
    graph.addVertex(i)

for _ in range(m):
    v1,v2,w = map(int,input().split())
    graph.addEdge(v1,v2,w)

start,dest = map(int, input().split())

print(graph.dijkstra(start, dest))

