from collections import deque
import sys
input = sys.stdin.readline

class Graph:
    def __init__(self):
        self.items = {}
    
    def addVertex(self,v):
        self.items[v] = {}
    
    def addEdge(self,v1,v2):
        if self.items[v1].get(v2):
            return
        self.items[v1][v2] = True
        
    def isTouched(self,start,dest,n):
        edges = {}
        visited = [False for _ in range(n)]
        visited[start] = True
        for i in range(n):
            edges[i] = self.items[i].copy()
        q = deque([start])
        while q:
            node = q.popleft()
            if edges.get(node):
                for d_node in edges[node].keys():
                    if d_node == dest:
                        return True
                    if not visited[d_node]:
                        visited[d_node] = True
                        q.append(d_node)
                del edges[node]
        
        return False

n = int(input())
m = int(input())

graph = Graph()
for i in range(n):
    graph.addVertex(i)

for v1 in range(n):
    lst = list(map(int,input().split()))
    for v2 in range(n):
        if lst[v2] == 1:
            graph.addEdge(v1,v2)
            graph.addEdge(v2,v1)

inRoad = list(map(int,input().split()))
for i in range(len(inRoad)-1):
    if inRoad[i] == inRoad[i+1]: continue
    if graph.isTouched(inRoad[i]-1, inRoad[i+1]-1,n): continue
    else:
        print("NO")
        break
else:
    print("YES")


