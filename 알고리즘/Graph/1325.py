import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

class Graph:

    def __init__(self):
        self.items = {}
    
    def addVertex(self, v):
        self.items[v] = {}
    
    def addEdge(self, v1, v2):
        self.items[v1][v2] = True

n,m = map(int,input().split())

graph = Graph()
Count = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(1,n+1):
    graph.addVertex(i)

for _ in range(m):
    v1,v2 = map(int, input().split())
    graph.addEdge(v2, v1)

for i in range(1,n+1):
    if Count[i] == 0:
        dfs(i)