from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

class Graph:

    def __init__(self):
        self.items = {}
    
    def addVertex(self,v):
        self.items[v] = {}
    
    def addEdge(self, v1,v2):
        self.items[v1][v2] = True

graph = Graph()
count_in = [0 for _ in range(n+1)]
answer = []

for i in range(1, n+1):
    graph.addVertex(i)

for _ in range(m):
    v1,v2 = map(int,input().split())
    graph.addEdge(v1,v2)
    count_in[v2] += 1

q = deque()

for i in range(1,n+1):
    if count_in[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    answer.append(node)
    if graph.items.get(node):
        for n_node in graph.items[node].keys():
            count_in[n_node] -= 1
            if count_in[n_node] == 0:
                q.append(n_node)

print(" ".join(map(str, answer)))