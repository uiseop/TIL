import sys

input = sys.stdin.readline

n = int(input())

passengers = [0] + list(map(int,input().split()))

m = int(input())

acc = [0 for _ in range(n+1)]

dp = [[0 for _ in range(n+1)] for _ in range(3)]

for i in range(1,n+1):
  acc[i] = acc[i-1] + passengers[i]

for i in range(3):
  for j in range((i+1)*m, n+1):
    if i == 0:
      dp[i][j] = max(dp[i][j-1], acc[j] - acc[j-m])
    else:
      dp[i][j] = max(dp[i][j-1], dp[i-1][j-m] + acc[j] - acc[j-m])

print(dp[-1][-1])