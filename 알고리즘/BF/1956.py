V,E = map(int,input().split())

dist = [[float("INF") for _ in range(V+1)] for _ in range(V+1)]

for _ in range(E):
  v1,v2,w = map(int,input().split())
  dist[v1][v2] = w

for k in range(1, V+1):
  for i in range(1, V+1):
    for j in range(1, V+1):
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

answer = float("INF")

for i in range(1, V+1):
  for j in range(i+1, V+1):
    answer = min(answer, dist[i][j] + dist[j][i])

print(answer) if answer != float("INF") else print(-1)

