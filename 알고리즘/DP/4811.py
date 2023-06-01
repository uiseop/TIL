while True:
  N = int(input())
  if not N: break
  dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

  for i in range(1, N+1):
    dp[i][0] = 1

  dp[1][1] = 1

  for i in range(2, N+1):
    for j in range(1, i+1):
      dp[i][j] = dp[i-1][j] + dp[i][j-1]

  print(dp[N][-1])