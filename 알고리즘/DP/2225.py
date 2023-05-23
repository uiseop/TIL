N,K = map(int,input().split())

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

DIV = 10**9

dp[0][0] = 1

for i in range(N+1):
  for j in range(1, K+1):
    dp[j][i] = (dp[j-1][i] + dp[j][i-1]) % DIV

print(dp[K][N])

# dp[K][N] = dp[K-1][N-1] + dp[K-1][N-2] + ... dp[K-1][0]
# dp[K][N-1] = dp[K-1][N-2] + dp[K-1][N-3] + ... dp[K-1][0]