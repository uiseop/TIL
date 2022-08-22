doubles = [2**i for i in range(31)]
thriples = [3**i for i in range(31)]

def binary_search(K):
    left = 0
    right = len(doubles)-1
    while left <= right:
        mid = (left + right) // 2
        if K == doubles[mid]:
            return mid, 0
        elif K < doubles[mid]:
            right = mid - 1
        else:
            left = mid + 1
    print('what is ',left, right, K)
    return right, K-doubles[right]

def solution(n):
    answer = 0
    k, offset = binary_search(n)
    answer = thriples[k]
    while offset != 0:
        k, offset = binary_search(offset)
        answer += thriples[k]
    return print(answer)

solution()