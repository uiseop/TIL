from collections import deque
import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

peoples = [i for i in range(1,n+1)]

population = [0] + list(map(int,input().split()))

adj = [{} for _ in range(n+1)]

for i in range(1,n+1):
    edges = list(map(int,input().split()))[1:]
    for edge in edges:
        adj[i][edge] = True
        adj[edge][i] = True

def bfs(combi):
    visited = [False for i in range(n+1)]
    visited[combi[0]] = True
    q = deque()
    q.append(combi[0])
    _sum = population[combi[0]]
    cnt = 1

    while q:
        N = q.popleft()
        for node in adj[N].keys():
            if node in combi and not visited[node]:
                visited[node] = True
                q.append(node)
                cnt += 1
                _sum += population[node]
    
    return _sum, cnt


result = float("inf")

for i in range(1, n//2 + 1):
    combis = combinations(peoples, i)
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(1,n+1) if i not in combi])
        if v1 + v2 == n:
            result = min(result, abs(sum1-sum2))

if result != float("inf"):
    print(result)
else:
    print(-1)