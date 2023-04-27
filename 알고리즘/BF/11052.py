import sys

input = sys.stdin.readline

n = int(input())

prices = [0] + list(map(int,input().split()))

dp = [0 for _ in range(n+1)]

def getIndexDP(k):
  result = 0

  for i in range(k+1):
    result = max(result, dp[k-i] + prices[i])

  return result

for i in range(1, n+1):
  dp[i] = getIndexDP(i)

print(dp[n])