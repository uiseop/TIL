import sys
import heapq

input = sys.stdin.readline

class Graph:
    def __init__(self):
        self.items = {}
    
    def addVertex(self,v):
        self.items[v] = {}
    
    def addEdge(self, v1,v2,w):
        if self.items[v1].get(v2):
            self.items[v1][v2] = w if w < self.items[v1][v2] else self.items[v1][v2]
        else:
            self.items[v1][v2] = w
    
    def dijkstra(self, start):
        dist = {}
        edges = {}
        for vertex in self.items.keys():
            dist[vertex] = float("inf")
            edges[vertex] = self.items[vertex].copy()
        
        dist[start] = 0
        heap = [[0,start]]
        while heap:
            distance, node = heapq.heappop(heap)
            if edges.get(node):
                for d_node, weight in edges[node].items():
                    if weight + distance < dist[d_node]:
                        dist[d_node] = weight + distance
                        heapq.heappush(heap,[dist[d_node], d_node])
                del edges[node]
        
        for i in dist.keys():
            if dist[i] == float("inf"):
                dist[i] = 0
        
        return list(dist.values())


n = int(input())
m = int(input())

graph = Graph()

for i in range(n):
    graph.addVertex(i)

for _ in range(m):
    v1,v2,w = map(int,input().split())
    graph.addEdge(v1-1, v2-1, w)

answer = []
for i in range(n):
    answer.append(graph.dijkstra(i))

for i in answer:
    print(" ".join(map(str, i)))