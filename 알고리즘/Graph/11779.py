import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

class Graph:
    def __init__(self):
        self.items = {}
    
    def addVertex(self,v):
        self.items[v] = {}
    
    def addEdge(self,v1,v2,w):
        if self.items[v1].get(v2):
            self.items[v1][v2] = min(self.items[v1][v2], w)
            return
        self.items[v1][v2] = w

    def dijkstar(self, start):
        dist = {}
        prev = [i for i in range(n+1)]
        for i in range(1,n+1):
            dist[i] = float("inf")
        dist[start] = 0

        heap = [[0,start]]
        while heap:
            weight, node = heapq.heappop(heap)
            for n_node,n_weight in self.items[node].items():
                if dist[n_node] > weight + n_weight:
                    dist[n_node] = weight + n_weight
                    heapq.heappush(heap, [dist[n_node], n_node])
                    prev[n_node] = node

        return dist, prev

graph = Graph()

for i in range(1,n+1):
    graph.addVertex(i)

for _ in range(m):
    v1,v2,w = map(int,input().split())
    graph.addEdge(v1,v2,w)

start, end = map(int,input().split())

dist, prev = graph.dijkstar(start)
print(dist[end])

log = []

node = end

while node != start:
    log.append(node)
    node = prev[node]

log.append(start)

print(len(log))
for i in log[::-1]:
    print(i, end=" ")