import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(2)
    exit()
elif n == 2:
    print(7)
    exit()

memo = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 2
dp[2] = 7

memo[0] = 1
memo[1] = 3
memo[2] = 10

for i in range(3, n+1):
    dp[i] = (2*dp[i-1] + 3*dp[i-2] + 2*memo[i-3]) % 1000000007
    memo[i] = memo[i-1] + dp[i]

print(dp[n])