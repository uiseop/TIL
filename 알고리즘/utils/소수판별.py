def getPrimsNumbers(n):
    arr = [True for _ in range(n+1)]
    arr[0] = False
    arr[1] = False

    for i in range(2, n+1):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1
    return arr
    # result = []
    # for i in range(n+1):
    #     if arr[i]:
    #         result.append(i)

    # return result # 0~n까지의 소수를 리턴해준다

import math

# 소수 판별 함수
def isPrimeNumber(x):
    if x == 1: return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임