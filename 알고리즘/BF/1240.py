from collections import defaultdict, deque

N,M = map(int,input().split())
INF = float("INF")

edges = defaultdict(list)

for _ in range(N-1):
  v1,v2,w = map(int,input().split())
  edges[v1].append([v2, w])
  edges[v2].append([v1, w])

def findRoot():
  for node in range(1, N+1):
    if len(edges[node]) == 1:
      return node

root = findRoot()

visited = [False for _ in range(N+1)]

visited[root] = '0'

q = deque()
q.append(root)

while q:
  node = q.popleft()

  for nextNode, weight in edges[node]:
    if visited[nextNode]: continue
    visited[nextNode] = str(int(visited[node]) + weight)
    q.append(nextNode)

for _ in range(M):
  v1,v2 = map(int,input().split())

  print(abs(int(visited[v1]) - int(visited[v2])))


