N = int(input())

ranks = [0] + list(map(int,input().split()))

dp = [0 for _ in range(N+1)]

for i in range(2, N+1):
  minVal = ranks[i]
  maxVal = ranks[i]

  j = i -1 
  while j >= 1:
    minVal = min(minVal, ranks[j])
    maxVal = max(maxVal, ranks[j])
    dp[i] = max(dp[i], dp[j-1] + maxVal - minVal)
    j -= 1

print(dp[N])