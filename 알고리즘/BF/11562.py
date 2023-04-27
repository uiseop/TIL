from collections import defaultdict
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = defaultdict(set)

for _ in range(m):
  v1,v2,p = map(int,input().split())
  v1 -= 1
  v2 -= 1
  if p:
    graph[v1].add(v2)
    graph[v2].add(v1)
  else:
    graph[v1].add(v2)

dist = [[0 for _ in range(n)] for _ in range(n)]

def isOneWay(i,j):
  if j in graph[i] and i not in graph[j]:
    return True
  return False

def isBi(i,j):
  if j in graph[i] and i in graph[j]:
    return True
  return False

def isNoWay(i,j):
  if j not in graph[i] and not i not in graph[j]:
    return True
  return False

for i in range(n):
  for j in range(n):
    if isOneWay(i,j): dist[j][i] += 1
    elif isOneWay(j,i): dist[i][j] += 1
    elif isNoWay(i,j):
      dist[i][j] = float("INF")
      dist[j][i] = float("INF")

print(dist,'haha')

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i == j: continue
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


result = []
for _ in range(int(input())):
  v1,v2 = map(int,input().split())
  # print(dist[v1-1][v2-1])
  result.append(dist[v1-1][v2-1])

print(dist)