from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())

tree = defaultdict(dict)
inf = float("inf")
dist = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(n-1):
    n1, n2, w = map(int,input().split())
    tree[n1][n2] = w
    tree[n2][n1] = w
    dist[n1][n2] = w
    dist[n2][n1] = w

for i in range(n):
    for del_node, weight in tree[i].items():
        dist[i][del_node] = inf
        dist[del_node][i] = inf