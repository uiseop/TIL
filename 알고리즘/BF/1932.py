import sys

input = sys.stdin.readline

n = int(input())

triangles = [list(map(int,input().split())) for _ in range(n)]

dp = list([0 for _ in range(n+1)] for _ in range(n))

dp[0][0] = triangles[0][0]

for i in range(1,n):
    for j in range(n):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangles[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangles[i][j]
            break
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangles[i][j]

print(max(dp[n-1]))