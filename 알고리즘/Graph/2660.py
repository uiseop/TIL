import sys

input = sys.stdin.readline

N = int(input())

dist = [[float("inf") for _ in range(N)] for _ in range(N)]

while True:
    nodes = list(map(int,input().split()))
    n,m = nodes[0]-1, nodes[1]-1
    if n == -2:
        break
    dist[n][m] = 1
    dist[m][n] = 1
    dist[n][n] = 0
    dist[m][m] = 0

min_list = [0 for _ in range(N)]
minVal = float("inf")

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(N):
    for j in range(N):
        min_list[i] = max(min_list[i], dist[i][j])
        minVal = min(min_list)

ans = []

for i in range(N):
    if min_list[i] == minVal:
        ans.append(i)

print(minVal, len(ans))
for i in ans:
    print(i+1, end=" ")
