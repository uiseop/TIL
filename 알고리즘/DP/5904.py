import sys

input = sys.stdin.readline

n = int(input())

dp = [0,3]
k = 2

while True:
    if dp[k-1] <= n:
        dp.append(dp[k-1] + k + 2 + dp[k-1])
        k += 1
    else: break


def findMoo(k):
    global n
    if dp[k-1] + 1 <= n <= dp[k-1] + k+2:
        if dp[k-1] + 1 == n:
            return 'm'
        else:
            return 'o'
    
    if dp[k-1] < n:
        n -= (dp[k-1] + k+2)
    return findMoo(k-1)
    
print(findMoo(k-1))