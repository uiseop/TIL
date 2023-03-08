import sys

input = sys.stdin.readline

n,m = map(int,input().split())

arr = list(list(map(int,(list(input().rstrip())))) for _ in range(n))

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

maxL = 0

for c in range(1,m+1):
    for r in range(1,n+1):
        if arr[r-1][c-1]:
            dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
            maxL = max(dp[r][c], maxL)

print(maxL ** 2)