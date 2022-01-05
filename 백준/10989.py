import sys
import math

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

nums = {}

for _ in range(int(input())):
    num = int(input())
    if nums.get(num):
        nums[num] += 1
    else:
        nums[num] = 1

key_nums = list(nums.keys())
sorted_keys = mergeSort(key_nums)
for i in sorted_keys:
    for j in range(nums[i]):
        print(i)
