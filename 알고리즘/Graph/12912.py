import heapq
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def getSumList(frm, del_node):
    if not tree[frm]:
        return
    for to, cost in tree[frm]:
        if to == del_node or visited[to]:
            continue
        visited[to] = True
        getSumList(to, del_node)
        visited[to] = False
        if sumList[to]:
            cost += -sumList[to][0]
        heapq.heappush(sumList[frm], -cost)

def getR(r):
    for sums in sumList:
        if len(sums) >= 2:
            first = -heapq.heappop(sums)
            second = -heapq.heappop(sums)
            if r < first + second:
                r = first + second
    return r

n = int(input())

tree = [[] for _ in range(n)]

edges = []

for _ in range(n-1):
    frm, to, cost = map(int,input().split())
    tree[frm].append([to, cost])
    tree[to].append([frm, cost])
    edges.append([frm, to, cost])

max_r = 0
visited = [False] * n

for edge in edges:
    frm, to, cost = edge

    sumList = [[] for _ in range(n)]

    visited[frm] = True
    getSumList(frm, to)
    visited[frm] = False

    r1 = -sumList[frm][0] if sumList[frm] else 0
    r1 = getR(r1)
    
    sumList = [[] for _ in range(n)]

    visited[to] = True
    getSumList(to, frm)
    visited[to] = False
    
    r2 = -sumList[to][0] if sumList[to] else 0
    r2 = getR(r2)

    max_r = max(max_r, r1 + r2 + cost)

print(max_r)
            

