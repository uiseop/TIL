from sys import stdin
from math import inf

n = int(stdin.readline())
m = int(stdin.readline())

# 이동 최소비용을 저장할 2차원 배열
cost = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

# 플로이드 와샬 알고리즘 적용
for k in range(n):
    cost[k][k] = 0
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

# 결과 출력
for row in cost:
    for i in range(n):
        # 갈 수 없는 경로인 경우, 0 출력
        if row[i] == inf:
            row[i] = 0
        print(row[i], end=" ")
    print()

