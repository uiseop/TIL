import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

N = int(input())

root = [set() for _ in range(N+1)]
visited = [False for _ in range(N+1)]


def makeRoot(root, node1, node2):
    root[node1].add(node2)
    root[node2].add(node1)

for _ in range(N-1):
    node1, node2 = map(int,input().split())
    makeRoot(root, node1,node2)

parent = [1 for _ in range(N+1)]
d = [1 for _ in range(N+1)]

def dfs(node, depth):
    visited[node] = True
    for nextNode in root[node]:
        if visited[nextNode]: continue
        parent[nextNode] = node
        d[nextNode] = depth + 1
        dfs(nextNode, depth + 1)

dfs(1, 1)

def getClosestParent(n1,n2):
    while d[n1] != d[n2]:
        if d[n1] > d[n2]:
            n1 = parent[n1]
        else:
            n2 = parent[n2]
    
    while n1 != n2:
        n1 = parent[n1]
        n2 = parent[n2]
    
    return n1

M = int(input())

for _ in range(M):
    node1, node2 = map(int,input().split())
    print(getClosestParent(node1, node2))


