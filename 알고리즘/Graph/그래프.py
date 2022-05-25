# 가중치 있는 그래프구현 python.ver
# 정점 추가와 간선 추가 기능이 있는 Graph 클래스를 통해 dijkstra 탐색이 가능하다.
# 어떻게? heapq를 사용하면 돼. 모든 정점을 float("inf")로 설정해두고 탐색을 시작하는 노드를 0으로 둔 다음 heap에 추가해서 while문을 돌리면 돼

class Graph:
    def __init__(self):
        self.items = {}
    
    def addVertex(self,v):
        self.items[v] = {}

    def addEdge(self,v1,v2,w):
        if self.items[v1].get(v2):
            self.items[v1][v2] = w if w < self.items[v1][v2] else self.items[v1][v2]
            return
        self.items[v1][v2] = w
    
graph = Graph()

for i in range(1,5):
    graph.addVertex(i)

graph.addEdge(1,3,5)
graph.addEdge(1,3,1)
graph.addEdge(1,2,7)
graph.addEdge(1,4,5)
graph.addEdge(2,3,5)

print(graph.items)
