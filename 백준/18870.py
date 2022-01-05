import sys
import heapq

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

set_nums = list(set(nums))
heap = []

for i in set_nums:
    heapq.heappush(heap,-i)

dic_nums = {}
while heap:
    num = -heapq.heappop(heap)
    dic_nums[num] = len(heap) if heap else 0

for i in nums:
    print(dic_nums[i], end=' ')