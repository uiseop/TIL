n = int(input())
nums = []
dp = [1] * n

for _ in range(n):
    nums.append(int(input()))

for i in range(1,n):
    for j in range(i):
        if nums[j] <= nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))