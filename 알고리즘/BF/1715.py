import heapq
import sys

input = sys.stdin.readline

n = int(input())

nums = list(int(input()) for _ in range(n))

heapq.heapify(nums)

total = 0

while len(nums) >= 2:
  A,B = heapq.heappop(nums), heapq.heappop(nums)

  total += (A + B)
  heapq.heappush(nums, A+B)

print(total)