n = int(input())
nums = list(map(int,input().split()))

dp = [1] * (n)

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i] , dp[j] + 1)

print(n - max(dp))
# DP를 사용해서 간단한 LIS문제를 풀어보았다. 다음엔 LIS알고리즘에 대해 공부해보자