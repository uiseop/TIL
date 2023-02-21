import sys

input = sys.stdin.readline

n,k = map(int,input().split())

factorials = [0, 1, 2]

for i in range(3,5001):
    factorials.append(factorials[i-1] * i)

dp = [[0] * 5001 for _ in range(5001)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if i == 1:
            dp[i][j] = j
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1])