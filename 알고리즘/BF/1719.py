n,m = map(int,input().split())

inf = float("INF")
dist = [[inf for _ in range(n)] for _ in range(n)]
answer = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
  v1,v2,w = map(int,input().split())
  dist[v1-1][v2-1] = w
  dist[v2-1][v1-1] = w
  answer[v1-1][v2-1] = v2
  answer[v2-1][v1-1] = v1

for i in range(n):
  answer[i][i] = '-'

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i == j: continue
      if dist[i][j] > dist[i][k] + dist[k][j]:
        dist[i][j] = dist[i][k] + dist[k][j]
        answer[i][j] = answer[i][k]

for a in answer:
  print(*a)