N,M = map(int,input().split())

memories = list(map(int,input().split()))
costs = list(map(int,input().split()))

sumCosts = sum(costs)

dp = [[0 for _ in range(10001)] for _ in range(101)]

result = sumCosts

for i in range(N):
  for j in range(sumCosts+1):
    if j - costs[i] >= 0:
      dp[i][j] = max(dp[i][j], dp[i-1][j - costs[i]] + memories[i])
    
    dp[i][j] = max(dp[i][j], dp[i-1][j])

    if dp[i][j] >= M:
      result = min(result, j)

print(result)