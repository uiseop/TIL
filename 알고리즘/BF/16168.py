from collections import defaultdict
import sys

input = sys.stdin.readline

v,e = map(int,input().split())

graph = defaultdict(set)

visited = [[False for _ in range(v+1)] for _ in range(v+1)]

for _ in range(e):
  v1,v2 = map(int,input().split())
  graph[v1].add(v2)
  graph[v2].add(v1)


def backtrack(start, cnt):
  if cnt == e:
    print('YES')
    return True
  
  result = False
  for node in graph[start]:
     if visited[start][node]: continue

     visited[start][node] = True
     visited[node][start] = True
     if backtrack(node, cnt + 1):
        result = True
        break
     visited[start][node] = False
     visited[node][start] = False

  return result


if not backtrack(1,0): print('NO')
