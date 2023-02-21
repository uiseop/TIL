import sys

input = sys.stdin.readline

T = int(input())

def getLeft(idx, N):
    return arr[idx-1] * N - (pSum[idx] - pSum[idx - N])

while T > 0:
    T -= 1

    answer = 0

    nums = list(map(int,input().split()))
    N = nums[0]
    arr = nums[1:]

    arr.sort()

    pSum = [0]
    for i in range(N):
        pSum.append(pSum[i] + arr[i])
    

    for i in range(2, N+1):
        minVal = float("inf")
        for j in range(i, N+1):
            minVal = min(minVal, getLeft(j, i))
        answer += minVal

    print(answer)
