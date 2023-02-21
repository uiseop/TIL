from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n)]

def dfs(i, cnt):
    if cnt == 5:
        print(1)
        exit()
    for next in graph[i]:
        if not visited[next]:
            visited[next] = True
            dfs(next, cnt + 1)
            visited[next] = False


for i in range(n):
    visited[i] = True
    dfs(i, 1)
    visited[i] = False

print(0)