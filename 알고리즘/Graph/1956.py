import sys

input = sys.stdin.readline

v,e = map(int,input().split())

dist = [[float("inf") for _ in range(v)] for _ in range(v)]

for _ in range(e):
    v1,v2,w = map(int,input().split())
    dist[v1-1][v2-1] = w

answer = float("inf")

for k in range(v):
    for i in range(v):
        for j in range(v):
            if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            
for i in range(v):
    answer = min(answer, dist[i][i])

if answer != float("inf"):
    print(answer)
else:
    print(-1)
