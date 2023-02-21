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


import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(frm):
    if not tree[frm]:
        return
    for to,weight in tree[frm]:
        dfs(to)
        if sumList[to]:
            weight += -sumList[to][0]
        heapq.heappush(sumList[frm], -weight)
    return

n = int(input())
if n == 1:
    print(0)
    exit()
tree = [[] for _ in range(n + 1)]
sumList = [[] for _ in range(n + 1)]
for _ in range(n-1):
    frm, to, weight = map(int,input().split())
    tree[frm].append([to, weight])

dfs(1)
ans = -sumList[1][0]
# ⬆️ 반례 해결. 일자 트리일 때를 확인을 안함... ㄷㄷ
# 5
# 1 2 10
# 2 3 10
# 3 4 10
# 4 5 10
for sums in sumList:
    if len(sums) >= 2:
        first = -heapq.heappop(sums)
        second = -heapq.heappop(sums)
        if ans < first + second:
            ans = first + second

print(ans)
# dfs(1)

# for t in tree:
#     print(t)
# []
# [[2, 3], [3, 2]]
# [[4, 5]]
# [[5, 11], [6, 9]]
# [[7, 1], [8, 7]]
# [[9, 15], [10, 4]]
# [[11, 6], [12, 10]]
# []
# []
# []
# []
# []
# []

from sys import stdin
from collections import deque

read = stdin.readline
V = int(read())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    c = list(map(int, read().split()))  
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))


def bfs(start):
    visit = [-1] * (V + 1)
    que = deque()
    que.append(start)
    visit[start] = 0
    _max = [0, 0]

    while que:
        t = que.popleft()
        for e, w in graph[t]:
            if visit[e] == -1:
                visit[e] = visit[t] + w
                que.append(e)
                if _max[0] < visit[e]:
                    _max = visit[e], e

    return _max


dis, node = bfs(1)
dis, node = bfs(node)
print(dis)