import math
import sys

input = sys.stdin.readline

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    leftPtr = 0
    rightPtr = 0
    result = []

    while leftPtr < len(left) or rightPtr < len(right):
        leftValue = left[leftPtr] if leftPtr < len(left) else math.inf
        rightValue = right[rightPtr] if rightPtr < len(right) else math.inf
        
        if leftValue < rightValue:
            result.append(leftValue)
            leftPtr += 1
        else:
            result.append(rightValue)
            rightPtr += 1

    return result


nums = []

for _ in range(int(input())):
    nums.append(int(input()))

res = mergeSort(nums)
print("\n".join(map(str, res)))