from collections import defaultdict

def s2num(s):
  return ord(s) - 97

n = int(input())

graph = defaultdict(list)

for _ in range(n):
  v1,_,v2 = input().split()
  graph[v1].append(v2)

dist = [[float("INF") for _ in range(26)] for _ in range(26)]

for node in graph.keys():
  num_node = s2num(node)
  for to_node in graph[node]:
    num_to_node = s2num(to_node)
    dist[num_node][num_to_node] = 1

for k in range(26):
  for i in range(26):
    for j in range(26):
      if i == j: continue
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

m = int(input())
for _ in range(m):
  v1,_,v2 = input().split()
  num_v1 = s2num(v1)
  num_v2 = s2num(v2)
  if dist[num_v1][num_v2] != float("INF"): print("T")
  else: print("F")