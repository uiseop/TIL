import sys

input = sys.stdin.readline

n = int(input())

devs = list(map(int,input().split()))

left = 0
right = len(devs)-1

result = 0

while left < right:
    result = max(result, min(devs[left], devs[right]) * (right - left - 1))

    if devs[left] < devs[right]:
        left += 1
    else:
        right -= 1

print(result)