from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

n = int(input())

graph = defaultdict(list)

max_r = 0

for _ in range(n-1):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))

def dfs(node, weights):
    if not graph[node]:
        return -weights
    temp = []
    for n_node,weight in graph[node]:
        temp_w = []
        if not visited[n_node] and not isCalculated[n_node]:
            visited[n_node] = True
            heapq.heappush(temp_w, dfs(n_node, weights + weight))
            visited[n_node] = False
        heapq.heappush(temp,heapq.heappop(temp_w))
    return temp

        

isCalculated = [False] * (n+1)
visited = [False] * (n+1)

for i in range(1,n+1):
    visited[i] = True
    isCalculated[i] = True
    w_list = dfs(i, 0)
    print(w_list)
    # temp = 0
    # if len(w_list) > 1:
    #     temp = -1 * heapq.heappop(w_list) + -1 * heapq.heappop(w_list)
    # elif w_list:
    #     temp = -1 * w_list[0]
    # max_r = max(max_r, temp)
    # visited[i] = False

print(max_r)