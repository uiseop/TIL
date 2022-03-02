import sys
input = sys.stdin.readline

def dfs(n, cost):
    visited[n] = True
    
    leafs = []
    for i in range(len(graph[n])):
        node = graph[n][i][0]
        if not visited[node]:
            leafs.append(graph[n][i])
    
    if len(leafs) == 0:  # 하위 노드가 없는 경우
        return cost
    
    ncost = 0  # 하위 노드들의 다리 폭파 비용 합
    for leaf in leafs:
        ncost += dfs(leaf[0], leaf[1])
    
    if cost > ncost:  # 상위 노드와 연결된 폭파 비용이 더 비싼 경우
        return ncost
    else:
        return cost

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        node1, node2, cost = map(int, input().split())
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))

    visited = [False] * (N+1)
    start = 0
    for i in range(len(graph[1])):
        start += graph[1][i][1]

    print(dfs(1, start))