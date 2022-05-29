import heapq
import sys

class Graph:
    def __init__(self):
        self.items = {}
    
    def addVertex(self, v):
        self.items[v] = {}
    
    def addEdge(self, v1,v2):
        self.items[v1][v2] = True

input = sys.stdin.readline

n,m = map(int,input().split())
question = [0 for _ in range(n+1)] # 1~N까지 입력으로 받음
answer = []

graph = Graph()

for i in range(1,n+1):
    graph.addVertex(i)

for _ in range(m):
    pre,nxt = map(int,input().split())
    question[nxt] += 1
    graph.addEdge(pre, nxt)

q = []

for i in range(1,n+1):
    if question[i] == 0:
        heapq.heappush(q,i)

while q:
    node = heapq.heappop(q)
    answer.append(node)
    if graph.items[node]:
        for n_node in graph.items[node].keys():
            question[n_node] -= 1
            if question[n_node] == 0:
                heapq.heappush(q,n_node)


print(" ".join(map(str,answer)))