import heapq
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

def dfs(frm):
    if not tree[frm]:
        return
    for to,weight in tree[frm]:
        if visited[to]:
            continue
        visited[to] = True
        dfs(to)
        if sumList[to]:
            weight += -sumList[to][0]
        heapq.heappush(sumList[frm], -weight)

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append([b,1])
    tree[b].append([a,1])

sumList = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
visited[1] = True
dfs(1)
r = -sumList[1][0]

for sums in sumList:
    if len(sums) >= 2:
        left = -heapq.heappop(sums)
        right = -heapq.heappop(sums)
        if r < left + right:
            r = left + right

print((1+r) // 2)