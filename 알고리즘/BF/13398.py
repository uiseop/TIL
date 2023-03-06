import sys

input = sys.stdin.readline

n = int(input())

numList = list(map(int,input().split()))

def getContinueSum(numList):
    result = list([-1 * float('inf') for _ in range(len(numList))] for _ in range(2))
    result[0][0] = numList[0]

    for i in range(1,len(numList)):
        result[0][i] = max(numList[i], numList[i] + result[0][i-1])
        result[1][i] = max(result[0][i-1], result[1][i-1] + numList[i], numList[i]) # 현재 삭제한 합, 이전의 삭제 이력이 있으면 현재 값을 더함
    
    return max(max(result[0]), max(result[1]))

answer = -1 * float('inf')

print(getContinueSum(numList))