n,k = map(int,input().split())

nums = list(int(input()) for _ in range(n))

dp = [1] + [0 for _ in range(k)]

for num in nums:
  for i in range(k+1 - num):
    dp[i+num] += dp[i]

print(dp[k])