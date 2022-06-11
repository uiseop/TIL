import heapq
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

class Graph:

    def __init__(self):
        self.items = {}

    def addVertex(self,v):
        self.items[v] = {}
    
    def addEdge(self,v1,v2,w):
        if self.items[v1].get(v2):
            self.items[v1][v2] = max(self.items[v1][v2],w)
        else:
            self.items[v1][v2] = w
        
        if self.items[v2].get(v1):
            self.items[v2][v1] = max(self.items[v2][v1],w)
        else:
            self.items[v2][v1] = w

    def dijkstra(self, start):
        weight = {}
        for i in self.items.keys():
            weight[i] = 0
        weight[start] = float("inf")
        heap = []
        for n,w in self.items[start].items():
            heapq.heappush(heap, [-w, start])
        while heap:
            w1, node = heapq.heappop(heap)
            for n,w2 in self.items[node].items():
                if w2 < -w1 and weight[n] < w2: # 최대 하중보다 지금 갖고있는 무게가 많아서 못가.
                    weight[n] = w2
                    heapq.heappush(heap, [-weight[n], n])

                elif w2 >= -w1 and weight[n] < -w1: # 현재 갖고있는 무게가 이전에 옮겻던 무게보다 커.
                    weight[n] = -w1

                    heapq.heappush(heap, [-weight[n], n])
                # if weight[n] > w1 + w2:
                #     weight[n] = w1 + w2
                #     heapq.heappush(heap,[weight[n], n])
        return weight
        


graph = Graph()

for i in range(1,n+1):
    graph.addVertex(i)

for _ in range(m):
    v1,v2,w = map(int,input().split())
    graph.addEdge(v1,v2,w)

start,end = map(int,input().split())

print(graph.dijkstra(start)[end])