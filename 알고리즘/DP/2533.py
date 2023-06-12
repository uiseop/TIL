from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())

graph = defaultdict(list)

for _ in range(n-1):
  v1,v2 = map(int,input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

visited = [0 for _ in range(n+1)]
dp = [[0,1] for _ in range(n+1)]
stack = [1]

while stack:
  start = stack[-1]
  isLeaf = True

  if not visited[start]:
    visited[start] = 1
    for node in graph[start]:
      if visited[node] == 0:
        stack.append(node)
        isLeaf = False

  if isLeaf:
    child = stack.pop()

    for parent in graph[child]:
      dp[parent][0] += dp[child][1]
      dp[parent][1] += min(dp[child][0], dp[child][1])


print(min(dp[1]))