# 최장 증가 부분 수열
# Longest Increasing Subsequence

# 완전탐색 풀이법

n = int(input())
nums = list(map(int,input().split()))

def lis(arr):
    if not arr:
        return 0
    
    ret = 1
    for i in range(len(arr)):
        nxt = []
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                nxt.append(arr[j])
        ret = max(ret, 1 + lis(nxt))
    return ret

print(lis(nums))

# 시간복잡도는 2^N 으로 매우 크기때문에 이러한 풀이는 매우 효율성이 떨어진다.

# DP풀이법

dp = [1] * (n)

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i] , dp[j] + 1)

print(dp[n-1])

# 이는 각 단계에서 1,2,3, .... n-1번 비교하기때문에 모두 더하면 n^2의 시간복잡도를 갖습니다.

# 이진탐색을 통한 최적화

INF = float("inf")
C = [INF] * (n+1)
C[0] = -INF
C[1] = arr[0]

def search(low, high, n):
    if low == high:
        return low
    